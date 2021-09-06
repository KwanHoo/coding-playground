'''
    Sequential Encoding Practice with RNN
    with Pytorch Lightning

    (for education purpose)

    Dataset is from 
    https://www.kaggle.com/thebrownviking20/intro-to-recurrent-neural-networks-lstm-gru

    Author : Sangkeun Jung (2021)
'''

import torch
from torch import nn
from torch.nn import functional as F
from torch.utils.data import DataLoader
from torchvision import transforms
import pytorch_lightning as pl

from torch.utils.data import Dataset, DataLoader

class StockDataset(Dataset):
    """Stock dataset."""

    def __init__(self, dataset):
        # make chunks for sequential modeling 
        self.Xs, self.Y = self.make_chunks(dataset)
        # self.Xs : [#_of_exs, 60]
        # self.Y  : [#_of_exs, ]

    def __len__(self):
        return len(self.Xs) # <-- this is important!!

    def make_chunks(self, dataset):
        # Since we are doing sequential encoding 
        # so, we create 60 multiple items for past history and 1 output   ((N = 60))
        # So for each element of training set, we have 60 previous training set elements 

        N = 60
        T = len(dataset)
        
        X = []
        Y = []
        for i in range(N, T):
            X.append(dataset[i-N:i,0]) # slide window
            Y.append(dataset[i,0])
        X = np.array(X)
        Y = np.array(Y)

        X = np.expand_dims(X, axis=-1) # [#_of_exs, N] -> [#_of_exs, N, 1]
        return X, Y


    def __getitem__(self, idx):
        sample = [self.Xs[idx].astype(np.float32), self.Y[idx].astype(np.float32)]
        return sample


import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

def draw_dataset_overview(dataset):
    # We have chosen 'High' attribute for prices. Let's see what it looks like
    dataset["High"][:'2016'].plot(figsize=(16,4),legend=True)
    dataset["High"]['2017':].plot(figsize=(16,4),legend=True)
    plt.legend(['Training set (Before 2017)','Test set (2017 and beyond)'])
    plt.title('IBM stock price')
    plt.show()



import pandas as pd
import numpy as np
class StockDataModule(pl.LightningDataModule):
    def __init__(self, 
                 batch_size: int = 32):
        super().__init__()
        self.batch_size = batch_size

        # we just do same data splition as the reference site
        # (https://www.kaggle.com/thebrownviking20/intro-to-recurrent-neural-networks-lstm-gru)
        # for comparision

        dataset = pd.read_csv('./data/IBM_2006-01-01_to_2018-01-01.csv', index_col='Date', parse_dates=['Date'])
        training_set = dataset[:'2016'].iloc[:,1:2].values
        test_set     = dataset['2017':].iloc[:,1:2].values

        # draw plot for training & test comparison
        draw_dataset_overview(dataset)  # at the first 

        ## data normalization with min-max scaling
        from sklearn.preprocessing import MinMaxScaler
        self.sc = MinMaxScaler(feature_range=(0,1))
        training_set_scaled = self.sc.fit_transform(training_set) # [2769,1]

        ## data preparation for test
        ## # Now to get the test set ready in a similar way as the training set.
        #    The following has been done so forst 60 entires of test set have 60 previous values 
        #    which is impossible to get unless we take the whole 'High' attribute data for processing
        ##
        dataset_total = pd.concat((dataset["High"][:'2016'],dataset["High"]['2017':]),axis=0)
        inputs = dataset_total[len(dataset_total)-len(test_set) - 60:].values
        inputs = inputs.reshape(-1,1)
        testing_set_scaled = self.sc.transform(inputs)
        
        ## MAKE DATASET
        self.train_dataset = StockDataset(training_set_scaled)
        self.test_dataset  = StockDataset(testing_set_scaled)

    def train_dataloader(self):
        return DataLoader(self.train_dataset, batch_size=self.batch_size, shuffle=True) # NOTE : Shuffle

    def test_dataloader(self):
        return DataLoader(self.test_dataset, batch_size=self.batch_size)

    def teardown(self):
        # Used to clean-up when the run is finished
        ...



def plot_predictions(test, predicted):
    plt.plot(test, color='red',label='Real IBM Stock Price')
    plt.plot(predicted, color='blue',label='Predicted IBM Stock Price')
    plt.title('IBM Stock Price Prediction')
    plt.xlabel('Time')
    plt.ylabel('IBM Stock Price')
    plt.legend()
    plt.show()


from pytorch_lightning.metrics import functional as FM

class LSTMStockPrediction(pl.LightningModule): 
    # <-- note that nn.module --> pl.LightningModule
    def __init__(self, 
                 learning_rate=1e-3,
                 scaler=None):
        super().__init__()
        self.save_hyperparameters()  # <-- it store arguments to self.hparams.* 

        # network design 
        # LSTM
        self.seq_encoder = nn.LSTM(input_size=1, # scalar value
                                   hidden_size=50, 
                                   num_layers=4, 
                                   dropout=0.2,
                                   batch_first=True
                                   )
        self.to_output = nn.Linear(50, 1) # to get scalar value 

        
        # loss
        self.criterion = nn.MSELoss()

        # data scaler (for chart drawing only)
        self.scaler = scaler

    def forward(self, x):
        # LSTM expect input shape of [batch_size, seq_len, input_size]
        lstm_output, _ = self.seq_encoder(x)
        # output : [batch_size, seq_len, hidden_size]
        enc_output = lstm_output[:, -1, :]
        enc_output = self.to_output(enc_output)

        return enc_output.squeeze()

    def training_step(self, batch, batch_idx):
        Xs, y = batch 
        predicted = self(Xs)
        loss = self.criterion(predicted, y) 
        self.log('train_loss', loss, on_step=True, on_epoch=True, prog_bar=True, logger=True)
        return loss

    def test_step(self, batch, batch_idx):
        Xs, y = batch 
        predicted = self(Xs)
        loss = self.criterion(predicted, y)
        mse = FM.mean_squared_error(predicted, y)
        metrics = {
                    'test_mse': mse, 
                  }
        self.log_dict(metrics)

        return predicted, y

    def test_epoch_end(self, test_step_outputs):
        predicted = torch.cat([ x[0] for x in test_step_outputs ])
        reference = torch.cat([ x[1] for x in test_step_outputs ])
        total_mse = FM.mean_squared_error(predicted, reference)
        metrics = {
                    'final.test_mse': total_mse, 
                  }
        self.log_dict(metrics)

        ## inverse transform and draw chart
        predicted_stock_price = self.scaler.inverse_transform(predicted.unsqueeze(-1).cpu().numpy())
        reference_stock_price = self.scaler.inverse_transform(reference.unsqueeze(-1).cpu().numpy())

        # Visualizing the results for LSTM
        plot_predictions(reference_stock_price, predicted_stock_price)


    def configure_optimizers(self):
        optimizer = torch.optim.RMSprop(self.parameters(), lr=self.hparams.learning_rate)
        return optimizer

    @staticmethod
    def add_model_specific_args(parent_parser):
        parser = parent_parser.add_argument_group("MLP_MNIST_Classifier")
        parser.add_argument('--learning_rate', type=float, default=0.001)
        return parent_parser

from argparse import ArgumentParser
from pytorch_lightning.callbacks import EarlyStopping
def cli_main():
    pl.seed_everything(1234)

    # ------------
    # args
    # ------------
    parser = ArgumentParser()
    parser.add_argument('--batch_size', default=32, type=int)
    parser = pl.Trainer.add_argparse_args(parser)
    parser = LSTMStockPrediction.add_model_specific_args(parser)
    parser = StockDataModule.add_argparse_args(parser)
    args = parser.parse_args()

    # ------------
    # data
    # ------------
    dm = StockDataModule.from_argparse_args(args)

    # ------------
    # model
    # ------------
    model = LSTMStockPrediction(args.learning_rate, dm.sc)

    # ------------
    # training
    # ------------
    trainer = pl.Trainer(
                            max_epochs=50, 
                            gpus = 0 # <-- you can set your device numbers
                        )
    trainer.fit(model, datamodule=dm)

    # ------------
    # testing
    # ------------
    result = trainer.test(model, 
                          test_dataloaders=dm.test_dataloader())
    print(result)


if __name__ == '__main__':
    cli_main()