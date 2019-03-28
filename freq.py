from konlpy.tag import Twitter
from collections import Counter

def get_tags(text, ntags=500):
    spliter = Twitter()
    pos = spliter.pos(text)
    words=[]
    for li in pos:
        if li[1]=='Noun' or li[1] == 'Adjective':
            words.append(li[0])
    count = Counter(words)
    return_list = []

    for n, c in count.most_common(ntags):
        temp = {'tag': n, 'count': c}
        return_list.append(temp)

    return return_list

def main(title):
    text_file_name = "%s.txt"%title
    noun_count = 500
    output_file_name = "%s_count.txt"%title
    try: 
        open_text_file = open(text_file_name, 'r', -1, "utf-8")
        text = open_text_file.read()
    except:
        print("리뷰 파일이 없습니다")
        return
    tags = get_tags(text, noun_count)
    open_text_file.close()
    open_output_file = open(output_file_name, 'w', -1, "utf-8")

    for tag in tags:
        noun = tag['tag']
        count = tag['count']
        open_output_file.write('{} {}\n'.format(noun, count))

    open_output_file.close()

if __name__=='__main__':
    main()
