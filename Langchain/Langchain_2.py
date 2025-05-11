# info Website get data
from langchain_community.document_loaders import WebBaseLoader

# gpt 요약 자동화 함수
from langchain.chains.summarize import load_summarize_chain

# gpt 가져와
from langchain_openai import ChatOpenAI

# info pdf 파일 인터넷 혹은 다른 곳에서 불러와서 사용하고 싶으면
from langchain_community.document_loaders import PyPDFLoader

model = ChatOpenAI(model='gpt-4o-mini')

loader = WebBaseLoader('https://finviz.com/news.ashx')
docs = loader.load()

# info pdf 파일 불러오려면? ()안에 소괄호 한 번 더하는 이유는 튜플 형식일 수 있어서
# docs = PyPDFLoader((~~)).load()

# print(docs)

# chain type stuff는 다 집어넣어주세요 ㄷㄷ
chain = load_summarize_chain(model, chain_type='stuff')
result = chain.invoke(docs)

print(result)