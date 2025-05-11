# RAG
from langchain_community.document_loaders import WebBaseLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(model='gpt-4o-mini')

loader = WebBaseLoader('https://github.com/facebookresearch/segment-anything-2')
docs = loader.load()

template = ChatPromptTemplate.from_template("""
    질문에 대해서 context를 읽고 대답해줘
    context : {context}
    question : {question}
    answer :              
""")

chain = template | model | StrOutputParser()
result = chain.invoke({'context' : docs, 'question' : 'sam2 설치는 어떻게 해야해?'})

print(result)