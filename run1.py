from tkinter.filedialog import *
import similarity3
import csv
import os.path
import glob


def search_most_similar_movie(title, n):  # title : 기준 파일 명, n : 유사한 영화 상위 n개 출력

    # DB 폴더를 선택
    dirName = "/content"
    file_list = glob.glob(os.path.join(dirName, "*_count3.txt"))

    max_similarity = 0
    most_similar_file_name = ""
    dic = {}

    # 폴더 내의 txt파일
    for inFile in file_list:

        # 파일명 추출
        filename = os.path.basename(inFile).split(".")[0]
        filename = filename[:-7]
        # print(filename)

        # 같은 파일끼리는 X
        if filename == title:
            continue

        # similarity 계산 후 dictionary에 저장 (key : filename, value : similarity)
        if filename not in dic.keys():
            dic[filename] = similarity3.main(title, filename)

    # dictionary sort후 상위 n개 출력
    print("===== %d similar movie list =====" % n)
    sortedList = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    # print(dic)
    for i, d in enumerate(sortedList):
        if i >= n:
            break
        print("%s : %.2f%%" % (d[0], d[1]))

search_most_similar_movie("고지전", 10)
