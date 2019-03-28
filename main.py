# -*- coding: utf-8 -*-

import get_review
import freq
import sentiment
from concurrent.futures import ThreadPoolExecutor
import cloud
import similarity3

print("1 : 영화 리뷰 분석\n2 : 두가지 영화 리뷰 비교")
select = input("Enter 1 or 2 : ")

if select == '1' :
        print("Enter the Code : ")
        movie_code = input()

        with ThreadPoolExecutor(max_workers=5) as executor:
                executor.submit(get_review.fetch,int(movie_code))

        title = get_review.getTitle(int(movie_code))
        freq.main(title)

        sentiment.print_senti(title)
        cloud.main(title)

elif select == '2':
        print("Enter the first movie code :")
        code1 = int(input())
        print("Enter the second movie code :")
        code2 = int(input())
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.submit(get_review.fetch,int(code1))
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.submit(get_review.fetch,int(code2))

        title1 = get_review.getTitle(int(code1))
        title2 = get_review.getTitle(int(code2))
        
        freq.main(title1)
        freq.main(title2)

        similarity3.main(title1, title2)

else:
        print("Input Error : Enter valid number")
