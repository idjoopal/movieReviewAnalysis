##단어를 count하지 않고 하나하나 저장하는 코드
from konlpy.tag import Twitter
from collections import Counter


def get_words(text, ntags=500):
    spliter = Twitter()
    pos = spliter.pos(text)
    words = []
    for li in pos:
        if li[1] == 'Noun' or li[1] == 'Adjective':
            words.append(li[0])

    print(words)

    return words


file_list = glob.glob(os.path.join("*_count.txt"))
for inFile in file_list:
    filename = inFile[:-10]
    print(filename)
    text_file_name = "%s.txt" % filename
    output_file_name = "%s_append.txt" % filename
    try:
        open_text_file = open(text_file_name, 'r', -1, "utf-8")
        text = open_text_file.read()
    except:
        print("리뷰 파일이 없습니다")

    words = get_words(text, 500)
    open_text_file.close()
    open_output_file = open(output_file_name, 'w', -1, "utf-8")

    for word in words:
        open_output_file.write(word + '\n')

    open_output_file.close()
