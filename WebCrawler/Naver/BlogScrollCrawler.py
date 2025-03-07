import json

import requests
from bs4 import BeautifulSoup

# data = requests.get('https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=31&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_hty.top&nso=&prank=30&ngn_country=KR&lgl_rcode=02192107&fgn_region=&fgn_city=&lgl_lat=37.48924&lgl_long=126.816765&enlu_query=IggCAF6CULhyAAAAtjQ5F3I1ndDcMKwJSjCQnzTWWo%2Fv%2BhtMoeVCN5yQwii7hmvaJu5QCami0L%2FfmALyCq4mMlWzEOgM4cHFz%2FHpd7ppWIJPGdRqnbr574%2F2bUK2td%2FsunS5sdRIBlPZB1k7fJqxwUwmGoRFGcOwclsb3odt6claaonZ55YFHPCdCWE%3D&enqx_theme=IggCAFaCULjiAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5k6tEn%2FafuHrrZte47kEtzz1FzCMTvSRXkqLRfoya9Xws%3D&abt=')
# data1 = json.loads(data.text)
# data2 = data['collection'][0]['html']
# print(data2)

url = 'https://s.search.naver.com/p/review/49/search.naver?ssc=tab.blog.all&api_type=8&query=%EC%82%AC%EA%B3%BC&start=31&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_hty.top&nso=&prank=30&ngn_country=KR&lgl_rcode=02192107&fgn_region=&fgn_city=&lgl_lat=37.48924&lgl_long=126.816765&enlu_query=IggCAF6CULhyAAAAtjQ5F3I1ndDcMKwJSjCQnzTWWo%2Fv%2BhtMoeVCN5yQwii7hmvaJu5QCami0L%2FfmALyCq4mMlWzEOgM4cHFz%2FHpd7ppWIJPGdRqnbr574%2F2bUK2td%2FsunS5sdRIBlPZB1k7fJqxwUwmGoRFGcOwclsb3odt6claaonZ55YFHPCdCWE%3D&enqx_theme=IggCAFaCULjiAAAAh%2FDtntZaiMLGh3DOFtIyqw%2Ft3q4clEos1p2O1NTRYn4NUJzpY2XWim4radqdYrSZDNiELd6nYNJwytlWzreKNul2xLfylQ7CjZHVqCLhCfDfLmMEOVaPYbdbw2RxiX5k6tEn%2FafuHrrZte47kEtzz1FzCMTvSRXkqLRfoya9Xws%3D&abt='

response = requests.get(url)

data = response.json()

print(data)