import json

import requests
from bs4 import BeautifulSoup

# # url 변수에 저장
# url = 'https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=조예나&start=1&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_hty.top&nso=&prank=30&ngn_country=KR&lgl_rcode=02192107&fgn_region=&fgn_city=&lgl_lat=37.48924&lgl_long=126.816765&enlu_query=IggCAF6CULgpAAAA94CCHN2nXekVm8x1ohP7Uf%2BKYUA4L3vA3r8bxtIuZ6FvuGnRvNov%2BA3yj4REvrcijXNSSXl8BmfouYfEaXfsTZNApaEaUzaurcMvLmmqaVa%2BQiqNxuQJ2SvR1xNxQ%2B%2BFxxoHf6wfUSHv1eqcy1inB%2FNeP5Dl%2FZm6pKZXF%2FZcmzw%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt='

# # get 날리기
# response = requests.get(url)

# # response를 바로 json으로 안바꾸고 soup하면?
# # 만약에 백슬레쉬 있으면, .replace('\\', '') 사용
# soup = BeautifulSoup(response.text.replace('\\', ''), "html.parser")

# # + json 자료는 항상 다른 변수에 따로 넣어서 관리하는게 관리가 편함 ㄹㅇ
# # json 변환
# # data = response.json()

# # # json 변환 후 출력하는데 collection 벗겨서 출력하기 전에 타입 체크
# # print(data['collection'])

# # class="title_area" 가져와야함

# # soup = BeautifulSoup(data.dict, 'html.parser')
# list = soup.select('a.title_link')

# for i in range(30):
#     print(list[i]['href'] + '\n')
#     print(list[i].text + '\n')

def searchData(search):
    url = f'https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query={search}&start=1&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_hty.top&nso=&prank=30&ngn_country=KR&lgl_rcode=02192107&fgn_region=&fgn_city=&lgl_lat=37.48924&lgl_long=126.816765&enlu_query=IggCAF6CULgpAAAA94CCHN2nXekVm8x1ohP7Uf%2BKYUA4L3vA3r8bxtIuZ6FvuGnRvNov%2BA3yj4REvrcijXNSSXl8BmfouYfEaXfsTZNApaEaUzaurcMvLmmqaVa%2BQiqNxuQJ2SvR1xNxQ%2B%2BFxxoHf6wfUSHv1eqcy1inB%2FNeP5Dl%2FZm6pKZXF%2FZcmzw%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt='
    result = requests.get(url)
    soup = BeautifulSoup(result.text.replace('\\', ''), 'html.parser')
    resultList = soup.select('a.title_link')
    
    for i in range(30):
        print(resultList[i]['href'] + '\n')
        print(resultList[i].text + '\n')

searchData('사과')