# -*- coding: utf-8 -*-

import get_review
from concurrent.futures import ThreadPoolExecutor
import freq

movie_code = input("Enter the Code : ")

with ThreadPoolExecutor(max_workers=5) as executor:
  executor.submit(get_review.fetch,int(movie_code))

title = get_review.getTitle(int(movie_code))
freq.main(title)
