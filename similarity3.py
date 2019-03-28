from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import glob

def open_review(title):
    lst = []
    file = open('%s_append3.txt' % title, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        lst.append(line[:-1])
    file.close()
    # print(lst)
    return lst


def main(title1, title2):
    # load review
    review1 = open_review(title1)
    review2 = open_review(title2)

    doc1 = ''
    doc2 = ''
    for word in review1:
        doc1 += word + '\n'
    for word in review2:
        doc2 += word + '\n'

    corpus = [doc1, doc2]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(corpus)
    X = X.todense()

    sim_rate = 100 * cosine_similarity(X[0], X[1])
    return sim_rate[0][0]


def search_most_similar_movie(title, n):  # title : 기준 파일 명, n : 유사한 영화 상위 n개 출력

    # DB 폴더를 선택
    file_list = glob.glob(os.path.join(dirName, "*_append3.txt"))

    max_similarity = 0
    most_similar_file_name = ""
    dic = {}

    # 폴더 내의 txt파일
    for inFile in file_list:

        # 파일명 추출
        filename = os.path.basename(inFile).split(".")[0]
        filename = filename[:-8]
        # print(filename)

        # 같은 파일끼리는 X
        if filename == title:
            continue

        # similarity 계산 후 dictionary에 저장 (key : filename, value : similarity)
        if filename not in dic.keys():
            dic[filename] = main(title, filename)

    # dictionary sort후 상위 n개 출력
    print("===== %d similar movie list =====" % n)
    sortedList = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    # print(dic)
    for i, d in enumerate(sortedList):
        if i >= n:
            break
        print("%s : %.2f%%" % (d[0], d[1]))


search_most_similar_movie("화려한휴가", 10)
