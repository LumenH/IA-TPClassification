import os
import random

'''The differents categories'''
categories = ["pos", "neg"]

'''Source folder'''
source_folder = ["tagged/neg", "tagged/pos"]

target_folder = ["test/neg", "test/pos", "train/neg", "train/pos"]

'''The differents tags'''
tags = ["NOM", "ADJ", "VER", "ADV"]

'''Ratios'''
train_ratio = 0.8
train_pos_ratio = 0.5
train_neg_ratio = 0.5
test_ratio = 1 - train_ratio
test_pos_ratio = 0.5
test_neg_ratio = 1 - test_pos_ratio

'''Read the files in the sources folders and place them in the differents target folders'''
def process(source_folder, target_folder, files):
    for processed_file in files:
        with open("{0}/{1}".format(source_folder, processed_file), 'r') as input_f:
        #Decomment the following line for Windows
        #with open("{0}/{1}".format(source_folder, processed_file), 'r', encoding='latin-1') as input_f:
            strW = ""
            for line in input_f:
                if any(word in line for word in tags):
                    tagsWord = line.split("\t")[2]
                    strW += tagsWord.split("|")[0] if "|" in tagsWord else tagsWord
        with open("{0}/processed_{1}".format(target_folder, processed_file), 'w') as output_f:
        #Decomment the following line for Windows
        #with open("{0}/processed_{1}".format(target_folder, processed_file), 'w') as output_f:
            output_f.write(strW)

if __name__ == "__main__":

    print("start")

    negFiles = [filename for filename in os.listdir(source_folder[0])]
    posFiles = [filename for filename in os.listdir(source_folder[1])]

    nbNeg = len([filename for filename in os.listdir(source_folder[0])])
    nbPos = len([filename for filename in os.listdir(source_folder[1])])

    posTrainIndice = int(round(((nbNeg + nbPos) * train_ratio) * train_pos_ratio))
    negTrainIndice = int(round(((nbNeg + nbPos) * train_ratio) * train_neg_ratio))
    posTestIndice = int(round(((nbNeg + nbPos) * test_ratio) * test_pos_ratio))
    negTestIndice = int(round(((nbNeg + nbPos) * test_ratio) * test_neg_ratio))

    '''Random generation'''
    randomPosTrain = random.sample(range(nbPos), posTrainIndice)
    randomNegTrain = random.sample(range(nbNeg), negTrainIndice)
    randomPosTest = random.sample(range(nbPos), posTestIndice)
    randomNegTest = random.sample(range(nbNeg), negTestIndice)

    workingPosTrain = [posFiles[i] for i in randomPosTrain]
    workingNegTrain = [negFiles[i] for i in randomNegTrain]
    workingPosTest = [posFiles[i] for i in randomPosTest]
    workingNegTest = [negFiles[i] for i in randomNegTest]

    process(source_folder[0], target_folder[0], workingNegTest)
    process(source_folder[0], target_folder[2], workingNegTrain)
    process(source_folder[1], target_folder[1], workingPosTest)
    process(source_folder[1], target_folder[3], workingPosTrain)

    print("finish")
