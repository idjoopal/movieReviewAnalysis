# append에 stopword 추가
import os.path
import glob

f = open("stopwords_ko.txt", 'r')

stop_list = []

while True:
    line = f.readline()
    if not line: break
    line = line[:-1]
    stop_list.append(line)

f.close()

# print(stop_list)
file_list = glob.glob(os.path.join("*_append.txt"))
for inFile in file_list:
    filename = inFile[:-11]
    print(filename)
    input_file = "%s_append.txt" % filename
    output_file = "%s_append3.txt" % filename

    fp = open(input_file, 'r')
    out_file = open(output_file, 'w')

    while True:
        line = fp.readline()
        if not line: break
        line = line[:-1]
        if line in stop_list:
            pass
        else:
            out_file.write(line + '\n')

    fp.close()
    out_file.close()
