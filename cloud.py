import pytagcloud
import sentiment

def main(title):
    list = sentiment.open_review("%s"%title)

    try:
        positive = sentiment.open_pos()
        negative = sentiment.open_neg()
    except:
        print("wrong")
    taglist = []


    list_len = len(list)
    pos_word_l=[]
    pos_word_n=[]
    neg_word_l = []
    neg_word_n = []
    #neg_list=[]
    size=float(0)
    for i in range(0, list_len):
        if list[i][0] in positive:
            pos_word_l.append(list[i][0])
            pos_word_n.append(list[i][1])
            size+=float(list[i][1])
        if list[i][0] in negative:
            neg_word_l.append(list[i][0])
            neg_word_n.append(list[i][1])
            size += float(list[i][1])

    size=183/size
    list_len = len(pos_word_l)
    for i in range(0, list_len):
        taglist.append({'color': (70, 65, 217), 'size': int(float(int(pos_word_n[i])*4*size) + 20), 'tag': '%s' % pos_word_l[i]})
    list_len = len(neg_word_l)
    for i in range(0, list_len):
        taglist.append({'color': (255, 0, 0), 'size': int(float(int(neg_word_n[i])*4 * size) + 20), 'tag': '%s' % neg_word_l[i]})

    pytagcloud.create_tag_image(taglist,'wordcloud.jpg', size=(1000,500), fontname='malgunbd', rectangular=False)


