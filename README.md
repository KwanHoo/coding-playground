# DeepLearning_prac
 DeepLearning learn and practice


## Epoch
> 한번의 epoch은 인공 신경망에서 전체 데이터 셋에 대해 forward pass / backward pass 과정을 거친 것을 말함
> 즉, 전체 데이터 셋에 대해 한번 학습을 완료한 상태

## batch size
> 한번의 batch 마다 주는 데이터 샘플의 size
> 여기서 batch(보통 mini-batch라고 표현)는 나눠진 데이터 셋을 뜻함

## iteration
> epoch을 나누어서 실행하는 횟수라고 생각하면 편함


> > 전체 2000개의 데이터가 있고, epochs = 20, batch_size = 500 이라고 가정
> > 그렇다면 1 epoch은 각 데이터의 size가 500인 batch가 들어간 네번의 iteration으로 나누어짐
> > 그리고 전체 데이터 셋에 대해서는 20번의 학습이 이루어졌으며, itertation 기준으로 보자면 총 80번의 학습이 이루어진 것
