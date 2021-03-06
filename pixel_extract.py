import cv2
import numpy as np
from sklearn import datasets, linear_model

img = cv2.imread('Originals/1.jpg')
img2 = cv2.imread('Final/1.jpg')
img3 = cv2.imread('Originals/5.jpg')
rearr = img.reshape(530*800,3)
rearr2 = img2.reshape(530*800,3)
rearr3 = img3.reshape(534*800,3)
np.savetxt("original.csv", rearr, header="B,G,R", delimiter=",")
np.savetxt("final.csv", rearr, header="B,G,R", delimiter=",")
regrB = linear_model.LinearRegression()
regrG = linear_model.LinearRegression()
regrR = linear_model.LinearRegression()
originalB = np.reshape(rearr[:,0],(-1,1))
colorB = np.reshape(rearr2[:,0],(-1,1))
originalG = np.reshape(rearr[:,1],(-1,1))
colorG = np.reshape(rearr2[:,1],(-1,1))
originalR = np.reshape(rearr[:,2],(-1,1))
colorR = np.reshape(rearr2[:,2],(-1,1))
regrB.fit(originalB, colorB)
regrG.fit(originalG, colorG)
regrR.fit(originalR, colorR)
initialB = np.reshape(rearr3[:,0],(-1,1))
initialG = np.reshape(rearr3[:,1],(-1,1))
initialR = np.reshape(rearr3[:,2],(-1,1))

finalB = regrB.predict(initialB)
finalG = regrG.predict(initialG)
finalR = regrR.predict(initialR)
finalImage = np.concatenate((finalB, finalG, finalR), axis=1)
print(initialB.size)
finalImage = np.reshape(finalImage, img3.shape)
cv2.imwrite('correctedImage.png',finalImage)
print(np.around(finalImage))