import requests

from bs4 import BeautifulSoup

# finviz url
# url = 'https://s.search.naver.com/p/newssearch/2/search.naver?abt=%5B%7B%22eid%22%3A%22NATIVE-LAZY-LOAD%22%2C%22value%22%3A%7B%22bt%22%3A%222%22%2C%22is_control%22%3Atrue%7D%7D%5D&cluster_rank=77&de=&ds=&eid=&field=0&force_original=&is_dts=0&is_sug_officeid=0&mynews=0&news_office_checked=&nlu_query=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22finance%22%2C%22source%22%3A%22NLU%22%7D%7D%7D&nso=%26nso%3Dso%3Ar%2Cp%3Aall%2Ca%3Aall&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&office_category=0&office_section_code=0&office_type=0&pd=0&photo=0&query=%ED%95%B4%EC%99%B8%EC%A3%BC%EC%8B%9D&query_original=&rev=31&service_area=0&sort=0&spq=0&start=41&where=news_tab_api&nso=so:r,p:all,a:all'

# html로 반복문 돌려서 찾는게 나을듯?

# class로 찾는 경우
# <a href="https://www.cnbc.com/2025/03/10/stock-market-today-live-updates.html" target="_blank" class="nn-tab-link relative -top-px" rel="nofollow">S&amp;P 500 futures edges up after recession fears triggered a market sell-off: Live updates</a>

# 2번째 class
# <a href="https://www.cnbc.com/2025/03/10/stock-market-today-live-updates.html" target="_blank" class="nn-tab-link relative -top-px" rel="nofollow">S&amp;P 500 futures edges up after recession fears triggered a market sell-off: Live updates</a>

# 블로그
def searchData(search):
    url = f'https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query={search}&start=1&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_hty.top&nso=&prank=30&ngn_country=KR&lgl_rcode=02192107&fgn_region=&fgn_city=&lgl_lat=37.48924&lgl_long=126.816765&enlu_query=IggCAF6CULgpAAAA94CCHN2nXekVm8x1ohP7Uf%2BKYUA4L3vA3r8bxtIuZ6FvuGnRvNov%2BA3yj4REvrcijXNSSXl8BmfouYfEaXfsTZNApaEaUzaurcMvLmmqaVa%2BQiqNxuQJ2SvR1xNxQ%2B%2BFxxoHf6wfUSHv1eqcy1inB%2FNeP5Dl%2FZm6pKZXF%2FZcmzw%3D&enqx_theme=IggCAEeCULgRAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5kzvQc%2BH53BTcRGA4hvzLyCw%3D%3D&abt='
    result = requests.get(url)
    soup = BeautifulSoup(result.text.replace('\\', ''), 'html.parser')
    resultList = soup.select('a.title_link')
    
    for i in range(30):
        print(resultList[i]['href'] + '\n')
        print(resultList[i].text + '\n')

# searchData('테슬라')

def searchNews():
    url = f'https://s.search.naver.com/p/newssearch/2/search.naver?abt=%5B%7B%22eid%22%3A%22NATIVE-LAZY-LOAD%22%2C%22value%22%3A%7B%22bt%22%3A%222%22%2C%22is_control%22%3Atrue%7D%7D%5D&cluster_rank=77&de=&ds=&eid=&field=0&force_original=&is_dts=0&is_sug_officeid=0&mynews=0&news_office_checked=&nlu_query=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22finance%22%2C%22source%22%3A%22NLU%22%7D%7D%7D&nso=%26nso%3Dso%3Ar%2Cp%3Aall%2Ca%3Aall&nx_and_query=&nx_search_hlquery=&nx_search_query=&nx_sub_query=&office_category=0&office_section_code=0&office_type=0&pd=0&photo=0&query=%ED%95%B4%EC%99%B8%EC%A3%BC%EC%8B%9D&query_original=&rev=31&service_area=0&sort=0&spq=0&start=41&where=news_tab_api&nso=so:r,p:all,a:all'
    result = requests.get(url)
    soup = BeautifulSoup(result.text.replace('\\', ''), 'html.parser')
    
    print(soup)

# { "collection" : [{ "script": "", "style": "", "html": "          딕셔너리 > 리스트 > 딕셔너리 
        
searchNews()