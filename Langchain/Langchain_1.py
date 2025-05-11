from langchain_openai import ChatOpenAI

# info 가변적인 데이터를 넣고 답변을 받고 싶으면...
from langchain_core.prompts import ChatPromptTemplate

# result data를 parse하려면?
from langchain_core.output_parsers import StrOutputParser

# result data를 json으로 하려면?
from langchain_core.output_parsers import SimpleJsonOutputParser 

# pandas data frame으로는
from langchain_core.output_parsers import PandasDataFrameOutputParser

# info api key local 사용
# import os
# os.environ["OPENAI_API_KEY"] = '님들의 OpenAI API키'

# langchain 사용해서 open ai api 요청
model = ChatOpenAI(model='gpt-4o-mini')

# bug langchain은 아래와 같은 argument 인자를 쓸 수 있음 deveploper 사용 불가능
# "system"
# "human"
# "user"
# "assistant" (또는 "ai")
# "function" (특수 경우)

data = ChatPromptTemplate.from_messages(
    [
        ('system', '너는 이제 영어를 한국어로 번역하는 봇이야. 딕셔너리 형태로 대답하는데 key는 "context"를 사용해서 대답해'),
        ('human', '{here}')    
        # ('ai', '여기는 예상 답변')
    ]
)

# result = model.invoke(data.format_messages(here='i like kimchi'))
# info 다른 방법으로는 LCEL 문법, data를 model에 넣음
# info 이 문법이 매우 중요한 이유는 나중에 데이터를 끌고오면 데이터 | data | model 이런식으로 사용도 가능하기 때문
# model에서 나온 데이터를 정제하고 싶으면 model | analysisdata이런식으로도 가능

# FIX StrOutputParser() : parse, 
result = (data | model | SimpleJsonOutputParser()).invoke({ 'here' : 'i like gray cat bro'})

# result.content로 다른 내용은 제거
print(result)