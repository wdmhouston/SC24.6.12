# SC24.6.12
Springboard training unit SC24.6.12

git clone git@github.com:wdmhouston/SC24.6.12.git
git remote set-url origin git@github.com:wdmhouston/SC24.6.12.git

unit test/train test
python3 -m unittest tests.train

unit test/predict test
python3 -m unittest tests.predict

test results:
(env_tf) deming@ml-instance:/data/SC24.6.12/project$ python3 -m unittest tests.train
Found 180 files belonging to 3 classes.
Found 180 files belonging to 3 classes.
Found 29 files belonging to 3 classes.
Model: "sequential"
_________________________________________________________________\
Layer (type)                 Output Shape              Param #
=================================================================
conv2d (Conv2D)              (None, 222, 222, 32)      896
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 111, 111, 32)      0
_________________________________________________________________
batch_normalization (BatchNo (None, 111, 111, 32)      128
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 109, 109, 32)      9248
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 54, 54, 32)        0
_________________________________________________________________
batch_normalization_1 (Batch (None, 54, 54, 32)        128
_________________________________________________________________
dropout (Dropout)            (None, 54, 54, 32)        0
_________________________________________________________________
flatten (Flatten)            (None, 93312)             0
_________________________________________________________________
dense (Dense)                (None, 128)               11944064
_________________________________________________________________
dense_1 (Dense)              (None, 3)                 387
=================================================================
Total params: 11,954,851
Trainable params: 11,954,723
Non-trainable params: 128
_________________________________________________________________
Epoch 1/20
6/6 [==============================] - 10s 1s/step - loss: 11.7353 - accuracy: 0.5778 - val_loss: 145.9407 - val_accuracy: 0.5517
Epoch 2/20
6/6 [==============================] - 9s 1s/step - loss: 4.0728 - accuracy: 0.8056 - val_loss: 187.6859 - val_accuracy: 0.6552
Epoch 3/20
6/6 [==============================] - 9s 1s/step - loss: 1.1810 - accuracy: 0.9333 - val_loss: 218.0785 - val_accuracy: 0.5172
Epoch 4/20
6/6 [==============================] - 9s 1s/step - loss: 0.3676 - accuracy: 0.9500 - val_loss: 190.5133 - val_accuracy: 0.4828
Epoch 5/20
6/6 [==============================] - 9s 1s/step - loss: 0.4761 - accuracy: 0.9500 - val_loss: 168.2971 - val_accuracy: 0.4483
Epoch 6/20
6/6 [==============================] - 9s 1s/step - loss: 0.3889 - accuracy: 0.9611 - val_loss: 176.5318 - val_accuracy: 0.5172
Epoch 7/20
6/6 [==============================] - 9s 1s/step - loss: 0.1416 - accuracy: 0.9722 - val_loss: 170.4995 - val_accuracy: 0.5517
Epoch 8/20
6/6 [==============================] - 9s 1s/step - loss: 0.0864 - accuracy: 0.9944 - val_loss: 199.7224 - val_accuracy: 0.5172
Epoch 9/20
6/6 [==============================] - 9s 1s/step - loss: 0.2700 - accuracy: 0.9722 - val_loss: 191.8402 - val_accuracy: 0.5172
Epoch 10/20
6/6 [==============================] - 9s 1s/step - loss: 0.0383 - accuracy: 0.9889 - val_loss: 186.1131 - val_accuracy: 0.5172
Epoch 11/20
6/6 [==============================] - 9s 1s/step - loss: 0.0461 - accuracy: 0.9889 - val_loss: 185.8825 - val_accuracy: 0.5172
Epoch 12/20
6/6 [==============================] - 9s 1s/step - loss: 8.5195e-06 - accuracy: 1.0000 - val_loss: 187.1375 - val_accuracy: 0.5172
Epoch 13/20
6/6 [==============================] - 9s 1s/step - loss: 4.7512e-06 - accuracy: 1.0000 - val_loss: 173.9263 - val_accuracy: 0.5172
Epoch 14/20
6/6 [==============================] - 9s 1s/step - loss: 0.0075 - accuracy: 0.9944 - val_loss: 150.7794 - val_accuracy: 0.5517
Epoch 15/20
6/6 [==============================] - 9s 1s/step - loss: 4.2398e-05 - accuracy: 1.0000 - val_loss: 120.6784 - val_accuracy: 0.5517
Epoch 16/20
6/6 [==============================] - 9s 1s/step - loss: 6.6433e-06 - accuracy: 1.0000 - val_loss: 97.0573 - val_accuracy: 0.5517
Epoch 17/20
6/6 [==============================] - 9s 1s/step - loss: 1.7602e-04 - accuracy: 1.0000 - val_loss: 79.0100 - val_accuracy: 0.5862
Epoch 18/20
6/6 [==============================] - 9s 1s/step - loss: 7.0544e-05 - accuracy: 1.0000 - val_loss: 64.2499 - val_accuracy: 0.6207
Epoch 19/20
6/6 [==============================] - 9s 1s/step - loss: 1.5906e-06 - accuracy: 1.0000 - val_loss: 51.8230 - val_accuracy: 0.6207
Epoch 20/20
6/6 [==============================] - 9s 1s/step - loss: 8.5228e-07 - accuracy: 1.0000 - val_loss: 40.9994 - val_accuracy: 0.6207
model trained. model is saved to /data/SC24.6.12/project/data/model/model.h5

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
(env_tf) deming@ml-instance:/data/SC24.6.12/project$ python3 -m unittest tests.predict
Found 180 files belonging to 3 classes.
actural object: apple   predicted object:apple

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK
