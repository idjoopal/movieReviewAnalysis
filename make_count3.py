# stopword 추가
import os.path
import glob

f = open("./stopwords_ko.txt", 'r', encoding='UTF8')

stop_list = []

while True:
    line = f.readline()
    if not line: break
    line = line[:-1]
    stop_list.append(line)

f.close()

# print(stop_list)

dirName = "txt"
file_list = glob.glob(os.path.join(dirName, "*_count.txt"))

for inFile in file_list:
    filename = os.path.basename(inFile).split(".")[0]
    filename += '.txt'

    fp = open("./txt/" + filename, 'r', encoding='UTF8')

    out_name = os.path.basename(inFile).split(".")[0]
    out_file = open("./txt/" + out_name + "3.txt", 'w', encoding='UTF8')

    while True:
        line = fp.readline()
        if not line: break
        line_st = line.split(' ')[0]

        if line_st in stop_list:
            pass
        else:
            out_file.write(line)

    fp.close()
    out_file.close()
