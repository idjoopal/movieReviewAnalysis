import urllib
import urllib.request
import urllib.parse
import bs4
import re
import os
import time


def deleteTag(x):
    return re.sub("<[^>]*>", "", x)

def getTitle(code):
    http = urllib.request.urlopen("https://movie.naver.com/movie/bi/mi/basic.nhn?code=%d" % code)
    data2 = http.read().decode('utf-8')
    soup2 = bs4.BeautifulSoup(re.sub("&#(?![0-9])", "", data2), "html.parser")

    find_title = soup2.find_all('h3')
    idx2 = 0
    list = []
    for s in find_title:
        try:
            prop2 = s.get('class')
            if prop2 != None and prop2[0] == "h_movie":
                list.append(s.get_text())
        except UnicodeEncodeError:
            print("Error : %d" % (idx2))
        finally:
            idx2 += 1
    title_list = list[0].split('\n')
    title_list[1]=title_list[1].replace(" ","")
    return title_list[1]


def getComments(code):
    def makeArgs(code, page):
        params = {
            'code': code,
            'type': 'after',
            'isActualPointWriteExecute': 'false',
            'isMileageSubscriptionAlready': 'false',
            'isMileageSubscriptionReject': 'false',
            'page': page
        }
        return urllib.parse.urlencode(params)

    def innerHTML(s, sl=0):
        ret = ''
        for i in s.contents[sl:]:
            if i is str:
                ret += i.strip()
            else:
                ret += str(i)
        return ret

    def fText(s):
        if len(s): return innerHTML(s[0]).strip()
        return ''

    retList = []
    colSet = set()
    print("Processing: %d" % code)
    page = 1
    while page < 100:
        try:
            f = urllib.request.urlopen(
                "http://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?" + makeArgs(code, page))
            data = f.read().decode('utf-8')
        except:
            break
        soup = bs4.BeautifulSoup(re.sub("&#(?![0-9])", "", data), "html.parser")
        cs = soup.select(".score_result li")
        if not len(cs): break
        for link in cs:
            try:
                url = link.select('.score_reple em a')[0].get('onclick')
            except:
                print(page)
                print(data)
                raise ""
            m = re.search('[0-9]+', url)
            if m:
                url = m.group(0)
            else:
                url = ''
            if url in colSet: return retList
            colSet.add(url)
            cat = fText(link.select('.star_score em'))
            cont = fText(link.select('.score_reple p'))
            cont = re.sub('<span [^>]+>.+?</span>', '', cont)
            retList.append((url, cat, cont))
        page += 1

    return retList


def fetch(i):
    outname = '%s.txt' % getTitle(i)
    try:
        if os.stat(outname).st_size > 0: return
    except:
        None
    rs = getComments(i)
    if not len(rs): return
    f = open(outname, 'w', encoding='utf-8')
    for idx, r in enumerate(rs):
        if idx: f.write(',\n')
        f.write("%s" % (r[2].replace("'", "''").replace("\\", "\\\\")))
    f.write(';\n')
    f.close()
    # time.sleep(1)
