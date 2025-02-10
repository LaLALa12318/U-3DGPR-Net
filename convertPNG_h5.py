#!/user/bin/env python3
# -*- coding: utf-8 -*-
import cv2
import h5py
import numpy as np
import os
import random
import h5py
import  matplotlib.pyplot as plt


def generateModelTarget():
    firstPath=r"F:\LFR_Data\3DReconstruction_Data\combineModel"
    firstDir=os.listdir(firstPath)[1:]
    for qqq in firstDir:
        secondPath=firstPath+"/"+qqq
        secondDir=os.listdir(secondPath)
        for j in secondDir:
            thirdPath=secondPath+"/"+j
            thirdDir=os.listdir(thirdPath)[:68]
            for m in thirdDir:
                fourthPath=thirdPath+"/"+m
                fourthDir=os.listdir(fourthPath)
                targetData=[]
                tempTargetData=[]


                f1 = open(r"E:\LFR_Project\3DResconstructionCommand\material_1.txt", "r")  
                allMaterial = f1.readlines() 
                materialData=[]
                for mmm in allMaterial:
                    if(mmm!="\n"):
                        materialData.append(float(mmm.split(":")[1].split(" ")[1]))


                for q in range(0,20):

                    modelTargetPath=(fourthPath+"/"+str(q)+"_W.png")
                    temp_img=cv2.imread(modelTargetPath,1)
                    temp_img=cv2.resize(temp_img,(temp_img.shape[1],512),interpolation=cv2.INTER_NEAREST)
                    img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
                    # cv2.imshow("a",img)
                    # cv2.waitKey(0)
                    data = np.ones((img.shape[0], img.shape[1])) * -1.0
                    for i in range(0, img.shape[0]):
                        for j in range(0, img.shape[1]):

                            if (img[i][j][0] == 160 and img[i][j][1] == 5 and img[i][j][2] == 24):  #
                                data[i][j] = materialData[0]
                            elif (img[i][j][0] == 108 and img[i][j][1] == 4 and img[i][j][2] == 17):  #
                                data[i][j] = materialData[1]
                            elif (img[i][j][0] == 247 and img[i][j][1] == 157 and img[i][j][2] == 231):  #
                                data[i][j] = materialData[2]
                            elif (img[i][j][0] == 95 and img[i][j][1] == 213 and img[i][j][2] == 89):  #
                                data[i][j] = materialData[3]
                            elif (img[i][j][0] == 27 and img[i][j][1] == 72 and img[i][j][2] == 88):  #
                                data[i][j] = materialData[4]
                            elif (img[i][j][0] == 100 and img[i][j][1] == 155 and img[i][j][2] == 146):  #
                                data[i][j] = materialData[5]
                            elif (img[i][j][0] == 177 and img[i][j][1] == 0 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[6]
                            elif (img[i][j][0] == 255 and img[i][j][1] == 30 and img[i][j][2] == 120):  #
                                data[i][j] = materialData[7]
                            elif (img[i][j][0] == 179 and img[i][j][1] == 167 and img[i][j][2] == 184):  #
                                data[i][j] = materialData[8]
                            elif (img[i][j][0] == 77 and img[i][j][1] == 67 and img[i][j][2] == 81):  #
                                data[i][j] = materialData[9]
                            elif (img[i][j][0] == 246 and img[i][j][1] == 98 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[10]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 166 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[11]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 132 and img[i][j][2] == 217):  #
                                data[i][j] = materialData[12]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 100 and img[i][j][2] == 181):  #
                                data[i][j] = materialData[13]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 69 and img[i][j][2] == 145):  #
                                data[i][j] = materialData[14]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 42 and img[i][j][2] == 111):  #
                                data[i][j] = materialData[15]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 81 and img[i][j][2] == 182):  #
                                data[i][j] = materialData[16]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 255 and img[i][j][2] == 219):  #
                                data[i][j] = materialData[17]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 203 and img[i][j][2] == 169):  #
                                data[i][j] = materialData[18]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 152 and img[i][j][2] == 122):  #
                                data[i][j] = materialData[19]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 104 and img[i][j][2] == 78):  #
                                data[i][j] = materialData[20]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 59 and img[i][j][2] == 38):  #
                                data[i][j] = materialData[21]
                            elif (img[i][j][0] == 163 and img[i][j][1] == 163 and img[i][j][2] == 163):  #
                                data[i][j] = materialData[22]
                            elif (img[i][j][0] == 146 and img[i][j][1] == 149 and img[i][j][2] == 154):  #
                                data[i][j] = materialData[23]
                            elif (img[i][j][0] == 125 and img[i][j][1] == 136 and img[i][j][2] == 144):  #
                                data[i][j] = materialData[24]
                            elif (img[i][j][0] == 102 and img[i][j][1] == 125 and img[i][j][2] == 131):  #
                                data[i][j] = materialData[25]
                            elif (img[i][j][0] == 81 and img[i][j][1] == 113 and img[i][j][2] == 113):  #
                                data[i][j] = materialData[26]
                            elif (img[i][j][0] == 166 and img[i][j][1] == 152 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[27]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 80):  #
                                data[i][j] = materialData[28]
                            elif (img[i][j][0] == 52 and img[i][j][1] == 18 and img[i][j][2] == 219):  #
                                data[i][j] = materialData[29]
                            elif (img[i][j][0] == 193 and img[i][j][1] == 130 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[30]
                            elif (img[i][j][0] == 96 and img[i][j][1] == 51 and img[i][j][2] == 250):  #
                                data[i][j] = materialData[31]
                            elif (img[i][j][0] == 187 and img[i][j][1] == 0 and img[i][j][2] == 183):  #
                                data[i][j] = materialData[32]
                            elif (img[i][j][0] == 255 and img[i][j][1] == 144 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[33]
                            elif (img[i][j][0] == 77 and img[i][j][1] == 0 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[34]
                            elif (img[i][j][0] == 223 and img[i][j][1] == 118 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[35]
                            elif (img[i][j][0] == 123 and img[i][j][1] == 35 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[36]
                            elif (img[i][j][0] == 85 and img[i][j][1] == 0 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[37]
                            elif (img[i][j][0] == 210 and img[i][j][1] == 107 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[38]
                            elif (img[i][j][0] == 255 and img[i][j][1] == 177 and img[i][j][2] == 150):  #
                                data[i][j] = materialData[39]
                            elif (img[i][j][0] == 208 and img[i][j][1] == 135 and img[i][j][2] == 109):  #
                                data[i][j] = materialData[40]
                            elif (img[i][j][0] == 163 and img[i][j][1] == 95 and img[i][j][2] == 71):  #
                                data[i][j] = materialData[41]
                            elif (img[i][j][0] == 119 and img[i][j][1] == 57 and img[i][j][2] == 36):  #
                                data[i][j] = materialData[42]
                            elif (img[i][j][0] == 196 and img[i][j][1] == 100 and img[i][j][2] == 68):  #
                                data[i][j] = materialData[43]
                            elif (img[i][j][0] == 139 and img[i][j][1] == 78 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[44]
                            elif (img[i][j][0] == 174 and img[i][j][1] == 107 and img[i][j][2] == 36):  #
                                data[i][j] = materialData[45]
                            elif (img[i][j][0] == 210 and img[i][j][1] == 138 and img[i][j][2] == 66):  #
                                data[i][j] = materialData[46]
                            elif (img[i][j][0] == 247 and img[i][j][1] == 170 and img[i][j][2] == 97):  #
                                data[i][j] = materialData[47]


                            # 地层材质
                            # 单层地层介质
                            elif (img[i][j][0] == 70 and img[i][j][1] == 70 and img[i][j][2] == 70):  #
                                data[i][j] = materialData[48]
                                # 多层地层介质
                            elif (img[i][j][0] == 155 and img[i][j][1] == 255 and img[i][j][2] == 172):  #
                                data[i][j] = materialData[49]
                            elif (img[i][j][0] == 255 and img[i][j][1] == 225 and img[i][j][2] == 205):  #
                                data[i][j] = materialData[50]
                            elif (img[i][j][0] == 220 and img[i][j][1] == 205 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[51]

                            # 金属管道
                            elif (img[i][j][0] == 231 and img[i][j][1] == 191 and img[i][j][2] == 200):  #
                                data[i][j] = materialData[52]
                            # 非金属管道
                            elif (img[i][j][0] == 234 and img[i][j][1] == 217 and img[i][j][2] == 153):  #
                                data[i][j] = materialData[53]

                            # 空气
                            elif (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[54]
                                # 水分子
                            elif (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 111):  #
                                data[i][j] = materialData[55]
                            # 管道中的水
                            elif (img[i][j][0] == 196 and img[i][j][1] == 224 and img[i][j][2] == 230):
                                data[i][j] = materialData[56]

                            else:
                                data[i][j] = materialData[random.randint(25, 48)]

                    tempTargetData.append(data.tolist())
                finalSaveTarget=[]
                for mqq in range(0,20):
                    tempSaveData=[]
                    for mp in range(12, 444, 8):
                        mean= np.array(tempTargetData[mqq])[:,mp:mp+16].mean(axis=1)
                        tempSaveData.append(mean)
                    finalSaveTarget.append(tempSaveData)
                finalSaveTarget=np.array(finalSaveTarget)
                finalSaveTarget=np.reshape(finalSaveTarget,(finalSaveTarget.shape[0]*finalSaveTarget.shape[1]*finalSaveTarget.shape[2],1))
                np.savetxt(fourthPath+"/undergroundTarget.txt",finalSaveTarget)
                print(fourthPath)
    for qqq in firstDir:
        secondPath = firstPath + "/" + qqq
        secondDir = os.listdir(secondPath)
        for j in secondDir:
            thirdPath = secondPath + "/" + j
            thirdDir = os.listdir(thirdPath)[68:]
            for m in thirdDir:
                fourthPath = thirdPath + "/" + m
                fourthDir = os.listdir(fourthPath)
                targetData = []
                tempTargetData = []

                f1 = open(r"E:\LFR_Project\3DResconstructionCommand\material_2.txt", "r")  # 你要打开的文件
                allMaterial = f1.readlines()  # 一行一行读
                materialData = []
                for mmm in allMaterial:
                    if (mmm != "\n"):
                        materialData.append(float(mmm.split(":")[1].split(" ")[1]))

                for q in range(0, 20):
                    # 地层模型的图片路径
                    modelTargetPath = (fourthPath + "/" + str(q) + "_W.png")
                    temp_img = cv2.imread(modelTargetPath, 1)
                    temp_img = cv2.resize(temp_img, (temp_img.shape[1], 512), interpolation=cv2.INTER_NEAREST)
                    img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)
                    # cv2.imshow("a",img)
                    # cv2.waitKey(0)
                    data = np.ones((img.shape[0], img.shape[1])) * -1.0
                    for i in range(0, img.shape[0]):
                        for j in range(0, img.shape[1]):
                            # 道路模型的材质排序
                            if (img[i][j][0] == 160 and img[i][j][1] == 5 and img[i][j][2] == 24):  #
                                data[i][j] = materialData[0]
                            elif (img[i][j][0] == 108 and img[i][j][1] == 4 and img[i][j][2] == 17):  #
                                data[i][j] = materialData[1]
                            elif (img[i][j][0] == 247 and img[i][j][1] == 157 and img[i][j][2] == 231):  #
                                data[i][j] = materialData[2]
                            elif (img[i][j][0] == 95 and img[i][j][1] == 213 and img[i][j][2] == 89):  #
                                data[i][j] = materialData[3]
                            elif (img[i][j][0] == 27 and img[i][j][1] == 72 and img[i][j][2] == 88):  #
                                data[i][j] = materialData[4]
                            elif (img[i][j][0] == 100 and img[i][j][1] == 155 and img[i][j][2] == 146):  #
                                data[i][j] = materialData[5]
                            elif (img[i][j][0] == 177 and img[i][j][1] == 0 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[6]
                            elif (img[i][j][0] == 255 and img[i][j][1] == 30 and img[i][j][2] == 120):  #
                                data[i][j] = materialData[7]
                            elif (img[i][j][0] == 179 and img[i][j][1] == 167 and img[i][j][2] == 184):  #
                                data[i][j] = materialData[8]
                            elif (img[i][j][0] == 77 and img[i][j][1] == 67 and img[i][j][2] == 81):  #
                                data[i][j] = materialData[9]
                            elif (img[i][j][0] == 246 and img[i][j][1] == 98 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[10]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 166 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[11]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 132 and img[i][j][2] == 217):  #
                                data[i][j] = materialData[12]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 100 and img[i][j][2] == 181):  #
                                data[i][j] = materialData[13]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 69 and img[i][j][2] == 145):  #
                                data[i][j] = materialData[14]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 42 and img[i][j][2] == 111):  #
                                data[i][j] = materialData[15]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 81 and img[i][j][2] == 182):  #
                                data[i][j] = materialData[16]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 255 and img[i][j][2] == 219):  #
                                data[i][j] = materialData[17]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 203 and img[i][j][2] == 169):  #
                                data[i][j] = materialData[18]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 152 and img[i][j][2] == 122):  #
                                data[i][j] = materialData[19]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 104 and img[i][j][2] == 78):  #
                                data[i][j] = materialData[20]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 59 and img[i][j][2] == 38):  #
                                data[i][j] = materialData[21]
                            elif (img[i][j][0] == 163 and img[i][j][1] == 163 and img[i][j][2] == 163):  #
                                data[i][j] = materialData[22]
                            elif (img[i][j][0] == 146 and img[i][j][1] == 149 and img[i][j][2] == 154):  #
                                data[i][j] = materialData[23]
                            elif (img[i][j][0] == 125 and img[i][j][1] == 136 and img[i][j][2] == 144):  #
                                data[i][j] = materialData[24]
                            elif (img[i][j][0] == 102 and img[i][j][1] == 125 and img[i][j][2] == 131):  #
                                data[i][j] = materialData[25]
                            elif (img[i][j][0] == 81 and img[i][j][1] == 113 and img[i][j][2] == 113):  #
                                data[i][j] = materialData[26]
                            elif (img[i][j][0] == 166 and img[i][j][1] == 152 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[27]
                            elif (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 80):  #
                                data[i][j] = materialData[28]
                            elif (img[i][j][0] == 52 and img[i][j][1] == 18 and img[i][j][2] == 219):  #
                                data[i][j] = materialData[29]
                            elif (img[i][j][0] == 193 and img[i][j][1] == 130 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[30]
                            elif (img[i][j][0] == 96 and img[i][j][1] == 51 and img[i][j][2] == 250):  #
                                data[i][j] = materialData[31]
                            elif (img[i][j][0] == 187 and img[i][j][1] == 0 and img[i][j][2] == 183):  #
                                data[i][j] = materialData[32]
                            elif (img[i][j][0] == 255 and img[i][j][1] == 144 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[33]
                            elif (img[i][j][0] == 77 and img[i][j][1] == 0 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[34]
                            elif (img[i][j][0] == 223 and img[i][j][1] == 118 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[35]
                            elif (img[i][j][0] == 123 and img[i][j][1] == 35 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[36]
                            elif (img[i][j][0] == 85 and img[i][j][1] == 0 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[37]
                            elif (img[i][j][0] == 210 and img[i][j][1] == 107 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[38]
                            elif (img[i][j][0] == 255 and img[i][j][1] == 177 and img[i][j][2] == 150):  #
                                data[i][j] = materialData[39]
                            elif (img[i][j][0] == 208 and img[i][j][1] == 135 and img[i][j][2] == 109):  #
                                data[i][j] = materialData[40]
                            elif (img[i][j][0] == 163 and img[i][j][1] == 95 and img[i][j][2] == 71):  #
                                data[i][j] = materialData[41]
                            elif (img[i][j][0] == 119 and img[i][j][1] == 57 and img[i][j][2] == 36):  #
                                data[i][j] = materialData[42]
                            elif (img[i][j][0] == 196 and img[i][j][1] == 100 and img[i][j][2] == 68):  #
                                data[i][j] = materialData[43]
                            elif (img[i][j][0] == 139 and img[i][j][1] == 78 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[44]
                            elif (img[i][j][0] == 174 and img[i][j][1] == 107 and img[i][j][2] == 36):  #
                                data[i][j] = materialData[45]
                            elif (img[i][j][0] == 210 and img[i][j][1] == 138 and img[i][j][2] == 66):  #
                                data[i][j] = materialData[46]
                            elif (img[i][j][0] == 247 and img[i][j][1] == 170 and img[i][j][2] == 97):  #
                                data[i][j] = materialData[47]


                            # 地层材质
                            # 单层地层介质
                            elif (img[i][j][0] == 70 and img[i][j][1] == 70 and img[i][j][2] == 70):  #
                                data[i][j] = materialData[48]
                                # 多层地层介质
                            elif (img[i][j][0] == 155 and img[i][j][1] == 255 and img[i][j][2] == 172):  #
                                data[i][j] = materialData[49]
                            elif (img[i][j][0] == 255 and img[i][j][1] == 225 and img[i][j][2] == 205):  #
                                data[i][j] = materialData[50]
                            elif (img[i][j][0] == 220 and img[i][j][1] == 205 and img[i][j][2] == 255):  #
                                data[i][j] = materialData[51]

                            # 金属管道
                            elif (img[i][j][0] == 231 and img[i][j][1] == 191 and img[i][j][2] == 200):  #
                                data[i][j] = materialData[52]
                            # 非金属管道
                            elif (img[i][j][0] == 234 and img[i][j][1] == 217 and img[i][j][2] == 153):  #
                                data[i][j] = materialData[53]

                            # 空气
                            elif (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 0):  #
                                data[i][j] = materialData[54]
                                # 水分子
                            elif (img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 111):  #
                                data[i][j] = materialData[55]
                            # 管道中的水
                            elif (img[i][j][0] == 196 and img[i][j][1] == 224 and img[i][j][2] == 230):
                                data[i][j] = materialData[56]

                            else:
                                data[i][j] = materialData[random.randint(25, 48)]

                    tempTargetData.append(data.tolist())
                finalSaveTarget = []
                for mqq in range(0, 20):
                    tempSaveData = []
                    for mp in range(12, 444, 8):
                        mean = np.array(tempTargetData[mqq])[:, mp:mp + 16].mean(axis=1)
                        tempSaveData.append(mean)
                    finalSaveTarget.append(tempSaveData)
                finalSaveTarget = np.array(finalSaveTarget)
                finalSaveTarget = np.reshape(finalSaveTarget, (
                finalSaveTarget.shape[0] * finalSaveTarget.shape[1] * finalSaveTarget.shape[2], 1))
                np.savetxt(fourthPath + "/undergroundTarget.txt", finalSaveTarget)
                print(fourthPath)




if __name__ == '__main__':
    generateModelTarget()
