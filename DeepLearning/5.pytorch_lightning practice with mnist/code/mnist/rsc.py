'''
Mnist specific
    - resource related codes

Author : Sangkeun Jung (2019)
'''

import numpy as np
import random

def load_rsc(fn_dict):
    print("Data loading from {} and {}".format(
                                                fn_dict['image'],
                                                fn_dict['label']
                                                )
        )

    # train case:
        # image : [60000, 28, 28]
        # label : [60000, ]
    # test case  
        # image : [10000, 28, 28]
        # label : [10000, ]

    image_data = np.load(fn_dict['image'])  
    label_data = np.load(fn_dict['label'])

    num_exs = image_data.shape[0]

    # 1-2) preprocessing (2D --> 1D)
    image_data = image_data.reshape(num_exs, 784)  # [# of examples, 28, 28] --> [# of examples, 28*28]
    image_data = image_data.astype('float32')

    # 1-2) preprocessing (normalize to 0~1.0)
    image_data /= 255
    print(image_data.shape[0], 'Shape of the data')

    rsc = image_data, label_data
    return rsc 
    

def convert_to_tensor(rsc):
    # in case of mnist, 
    # the data is already converted as tensor

    return rsc



def make_batch_data(rsc, batch_size):
    # chunk the resource and make it as batch form
    #
    # rsc = [# of examples, 28*28]
    
    num_exs = rsc[0].shape[0]
    indices = list( range(0, num_exs) )
    random.shuffle(indices)

    # batches
    batches = []
    for i in range(0, len(indices), batch_size):
        a_batch_idx = indices[i:i+batch_size]
        
        a_batch_image = rsc[0][a_batch_idx]
        a_batch_label = rsc[1][a_batch_idx]
        
        batches.append( (a_batch_image, a_batch_label ) )

    return batches