# stopword 추가
import os.path
import glob

f = open("/content/stopwords_ko.txt", 'r')

stop_list = []

while True:
    line = f.readline()
    if not line: break
    line = line[:-1]
    stop_list.append(line)

f.close()

# print(stop_list)

dirName = "/content"
file_list = glob.glob(os.path.join(dirName, "*_count.txt"))

for inFile in file_list:
    filename = os.path.basename(inFile).split(".")[0]
    filename += '.txt'

    fp = open("/content/" + filename, 'r')

    out_name = os.path.basename(inFile).split(".")[0]
    out_file = open("/content/" + out_name + "3.txt", 'w')

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
