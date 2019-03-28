# -*- coding: utf-8 -*-

import get_review
# from concurrent.futures import ThreadPoolExecutor
import freq

f = open("/content/code_list.txt", 'r')

while True:
    line = f.readline()
    if not line: break

    movie_code = line
    get_review2.fetch(int(movie_code))
    title = get_review2.getTitle(int(movie_code))
    freq.main(title)

f.close()
