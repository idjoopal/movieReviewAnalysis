from tkinter.filedialog import *
import similarity
import csv
import os.path
import glob
import numpy as np
import matplotlib.pyplot as plt
from sklearn import manifold

import networkx as nx
# import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib as plt

font_name = plt.font_manager.FontProperties(fname="C:/Windows/Fonts/malgun.ttf").get_name()
plt.rc('font', family=font_name)


mLst = ["블랙팬서","캡틴마블","다크나이트","다크나이트라이즈","하모니","트랜스포머","트랜스포머_패자의역습","보헤미안랩소디","레미제라블","국가대표","택시운전사","방자전","쌍화점","라라랜드","비긴어게인","아이언맨3","아이언맨2","아이언맨","그시절,우리가좋아했던소녀","건축학개론","원티드","테이큰"]
# def search_most_similar_movie(standard_title):
#     global G, max
#     resList = []
#
#     # DB 폴더를 선택
#     dirName = "txt"
#     file_list = glob.glob(os.path.join(dirName, "*_count3.txt"))
#     dic = {}
#
#     resList.append(standard_title)
#     # 폴더 내의 txt파일
#     for inFile in file_list:
#
#         # 파일명 추출
#         filename = os.path.basename(inFile).split(".")[0]
#         filename = filename[:-7]
#         # print(filename)
#
#         # 같은 파일끼리는 X
#         if filename == standard_title:
#             resList.append(0)
#         else:
#             dist = similarity.main(standard_title, filename)
#             # print(standard_title, "--", filename, dist)\
#             resList.append(35 - dist)
#
#         # # similarity 계산 후 dictionary에 저장 (key : filename, value : similarity)
#         # if filename not in dic.keys():
#         #     # G.add_edge(standard_title, filename, distance= 35-dist)
#         #     dic[filename] = dist
#     return resList

def search_most_similar_movie(standard_title):
    global G, max, mLst
    resList = []

    # DB 폴더를 선택
    dirName = "txt"
    file_list = glob.glob(os.path.join(dirName, "*_append3.txt"))
    dic = {}

    resList.append(standard_title)
    # 폴더 내의 txt파일
    for inFile in file_list:

        # 파일명 추출
        filename = os.path.basename(inFile).split(".")[0]
        filename = filename[:-8]
        # print(filename)
        for str in mLst:
            if filename == str:
                # 같은 파일끼리는 X
                if filename == standard_title:
                    resList.append(0)
                else:
                    cor = 0
                    dist = similarity.main(standard_title, filename)
                    print(standard_title, "--", filename, dist)
                    # if dist > 70:
                    #     cor = 100
                    # elif dist > 60:
                    #     cor = 80
                    # elif dist > 50:
                    #     cor = 60
                    # elif dist > 40:
                    #     cor = 50
                    # elif dist > 30:
                    #     cor = 40
                    # elif dist > 20:
                    #     cor = 30
                    # elif dist > 15:
                    #     cor = 20
                    # elif dist > 10:
                    #     cor = 10
                    # elif dist > 5:
                    #     cor = 5
                    # else:
                    #     cor = 1
                    resList.append(1/dist)

        # # similarity 계산 후 dictionary에 저장 (key : filename, value : similarity)
        # if filename not in dic.keys():
        #     # G.add_edge(standard_title, filename, distance= 35-dist)
        #     dic[filename] = dist
    return resList

# DB 폴더를 선택
dirName = "txt"
file_list = glob.glob(os.path.join(dirName, "*_append3.txt"))
file_count = len(file_list)
totalList = []
# G = nx.Graph()

# 폴더 내의 txt파일
for inFile in file_list:
    # 파일명 추출
    filename = os.path.basename(inFile).split(".")[0]
    filename = filename[:-8]

    for str in mLst:
        if filename == str:
            print("processing", filename)
            totalList.append( search_most_similar_movie(filename) )

# search_most_similar_movie("아이언맨")
# nx.draw(G, with_labels=True)

# H = nx.DiGraph(G)   # create a DiGraph using the connections from G
# print(list(H.edges()))


dists = []
movies = []
for d in totalList:
    print(d)
    movies.append(d[0])
    dists.append(d[1:])

adist = np.array(dists)
amax = np.amax(adist)
adist /= amax

mds = manifold.MDS(n_components=2, dissimilarity="precomputed", random_state=6)
results = mds.fit(adist)

coords = results.embedding_

plt.pyplot.subplots_adjust(bottom = 0.1)
plt.pyplot.scatter(
    coords[:, 0], coords[:, 1], marker = 'o'
    )
for label, x, y in zip(movies, coords[:, 0], coords[:, 1]):
    plt.pyplot.annotate(
        label,
        xy = (x, y), xytext = (-20, 20),
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))

plt.pyplot.show()
