# stopword list 만들기위해 모든 count.txt 파일의 키워드를 총합해서 모아주는 코드

from tkinter.filedialog import *
import os.path
import glob

# 폴더를 선택
dirName = askdirectory()
file_list = glob.glob(os.path.join(dirName, "*_count.txt"))

for i in file_list:
    print(i)

ss = set()
d = {}

for tn, inFile in enumerate(file_list):

   fp = open(inFile, "r", encoding = "utf-8")
   while True:
        s = fp.readline()
        if s == "":
            break

        tmp = s.split(" ")
        word = tmp[0]
        cnt = tmp[1].replace("\n", "")

        ss.add(word)

        if word in d.keys():
            d[word] += int(cnt)
        else:
            d[word] = int(cnt)

   fp.close()

sortedList = sorted(d.items(), key = lambda x:x[1], reverse = True)



writeFP = open("C:\\Users\\student\\Downloads\\keyword_list.txt", "w")
for i in sortedList:
    writeFP.writelines(i[0] + " " + str(i[1]) + "\n")

writeFP.close()





