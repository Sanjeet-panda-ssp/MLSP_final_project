import numpy as np
import sklearn as sk

print("Hi, This is Panda's branch, dare not touch it")

import matplotlib.pyplot as mp
import numpy as np
import os
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import os
import numpy as np
from numpy.linalg import eig

def dataread(folder_location):
    arr = [[]]
    for file in sorted(os.listdir(folder_location)):
        s = plt.imread(folder_location+file)
        s = tf.convert_to_tensor(s, dtype=tf.float32)
        arr.append(s)
    arr=np.matrix(arr)
    return arr

yb1 = "/content/drive/MyDrive/CroppedYale/yaleB01/"
yb2 = "/content/drive/MyDrive/CroppedYale/yaleB02/"
yb3 = "/content/drive/MyDrive/CroppedYale/yaleB03/"
yb4 ="/content/drive/MyDrive/CroppedYale/yaleB04/"
yb5 ="/content/drive/MyDrive/CroppedYale/yaleB05/"
yb6 ="/content/drive/MyDrive/CroppedYale/yaleB06/"
yb7 ="/content/drive/MyDrive/CroppedYale/yaleB07/"
yb8 ="/content/drive/MyDrive/CroppedYale/yaleB08/"
yb9 ="/content/drive/MyDrive/CroppedYale/yaleB09/"
yb10 = "/content/drive/MyDrive/CroppedYale/yaleB10/"
yb11 = "/content/drive/MyDrive/CroppedYale/yaleB11/"
yb12="/content/drive/MyDrive/CroppedYale/yaleB12/"
yb13="/content/drive/MyDrive/CroppedYale/yaleB13/"
yb14="/content/drive/MyDrive/CroppedYale/yaleB14/"
yb15 ="/content/drive/MyDrive/CroppedYale/yaleB15/"
yb16 ="/content/drive/MyDrive/CroppedYale/yaleB16/"
yb17="/content/drive/MyDrive/CroppedYale/yaleB17/"
yb18= "/content/drive/MyDrive/CroppedYale/yaleB18/"
yb19= "/content/drive/MyDrive/CroppedYale/yaleB19/"
yb20="/content/drive/MyDrive/CroppedYale/yaleB20/"
yb21="/content/drive/MyDrive/CroppedYale/yaleB21/"
yb22="/content/drive/MyDrive/CroppedYale/yaleB22/"
yb23="/content/drive/MyDrive/CroppedYale/yaleB23/"
yb24="/content/drive/MyDrive/CroppedYale/yaleB24/"
yb25="/content/drive/MyDrive/CroppedYale/yaleB25/"
yb26= "/content/drive/MyDrive/CroppedYale/yaleB26/"
yb27= "/content/drive/MyDrive/CroppedYale/yaleB27/"
yb28 ="/content/drive/MyDrive/CroppedYale/yaleB28/"
yb29="/content/drive/MyDrive/CroppedYale/yaleB29/"
yb30="/content/drive/MyDrive/CroppedYale/yaleB30/"
yb31="/content/drive/MyDrive/CroppedYale/yaleB31/"
yb32="/content/drive/MyDrive/CroppedYale/yaleB32/"
yb33="/content/drive/MyDrive/CroppedYale/yaleB33/"
yb34= "/content/drive/MyDrive/CroppedYale/yaleB34/"
yb35= "/content/drive/MyDrive/CroppedYale/yaleB35/"
yb36="/content/drive/MyDrive/CroppedYale/yaleB36/"
yb37="/content/drive/MyDrive/CroppedYale/yaleB37/"
yb38="/content/drive/MyDrive/CroppedYale/yaleB38/"
yb39="/content/drive/MyDrive/CroppedYale/yaleB39/"

yb01 = dataread(yb1)
yb02 = dataread(yb2)
yb03 = dataread(yb3)
yb04 = dataread(yb4)
yb05 = dataread(yb5)
yb06 = dataread(yb6)
yb07 = dataread(yb7)
yb08 = dataread(yb8)
yb09 = dataread(yb9)
yb10 = dataread(yb10)
yb11 = dataread(yb11)
yb12 = dataread(yb12)
yb13 = dataread(yb13)
yb14 = dataread(yb14)
yb15 = dataread(yb15)
yb16 = dataread(yb16)
yb17 = dataread(yb17)
yb18 = dataread(yb18)
yb19 = dataread(yb19)
yb20 = dataread(yb20)
yb21 = dataread(yb21)
yb22 = dataread(yb22)
yb23 = dataread(yb23)
yb24 = dataread(yb24)
yb25 = dataread(yb25)
yb26 = dataread(yb26)
yb27 = dataread(yb27)
yb28 = dataread(yb28)
yb29 = dataread(yb29)
yb30 = dataread(yb30)
yb31 = dataread(yb31)
yb32 = dataread(yb32)
yb33 = dataread(yb33)
yb34 = dataread(yb34)
yb35 = dataread(yb35)
yb36 = dataread(yb36)
yb37 = dataread(yb37)
yb38 = dataread(yb38)
yb39 = dataread(yb39)

