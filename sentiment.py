def open_review(title):
    doc = ''
    # file = open('txt/%s_count3.txt'%title, 'r', encoding='utf-8')
    file = open('txt/%s_append3.txt' % title, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        doc += line
    file.close()

    # 빈도수를 2차원 배열로 저장
    doc = doc.split('\n')
    list = []
    doc_len = range(0, len(doc) - 1)
    for i in doc_len:
        # list.append(doc[i].split(' '))
        list.append(doc[i])

    return list

def open_review2(title):
    doc = ''
    file = open('txt/%s_count3.txt'%title, 'r', encoding='utf-8')
    lines = file.readlines()
    for line in lines:
        doc += line
    file.close()

    # make important word list
    fp = open("important_word_list.txt", "r", encoding = "utf-8")
    important_word_list = []
    while True:
        s = fp.readline()
        if s == "":
            break
        important_word_list.append(s.split(" ")[0])

    print(important_word_list)
    # 빈도수를 2차원 배열로 저장
    doc = doc.split('\n')
    list = []
    doc_len = range(0, len(doc) - 1)
    for i in doc_len:

        word = doc[i].split(" ")[0]
        cnt = int(doc[i].split(" ")[1])

        if word in important_word_list:
            #for _ in range(30):
            list.append([word, str(cnt)])
            print(1)

        #list.append([word, str(cnt)])

    return list

def open_pos(): #긍정사전 불러오기
    file_pos = open('긍정단어.txt','r', -1, "utf-8")
    positive = []
    lines1 = file_pos.readlines()
    for line in lines1:
        positive.append(line.replace("\n", ""))

    file_pos.close()
    return positive

def open_neg(): #부정사전 불러오기
    file_neg = open('부정단어.txt','r', -1, "utf-8")
    negative = []
    lines2 = file_neg.readlines()
    for line in lines2:
        negative.append(line.replace("\n", ""))
    file_neg.close()
    return negative

def print_senti(title):
    list = open_review(title)
    positive = open_pos()
    negative = open_neg()
    pos = 0
    neg = 0
    list_len = len(list)
    for i in range(0, list_len):
        if list[i][0] in positive:
            pos += int(list[i][1])
        elif list[i][0] in negative:
            neg += int(list[i][1])

    print("positive : %d" % pos)
    print("negative : %d" % neg)

    rate = ((pos)/(pos + neg))*100
    print("positive rate of this movie : %.2f%%"%rate)

