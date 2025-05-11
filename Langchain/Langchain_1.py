from langchain_openai import ChatOpenAI

# info 가변적인 데이터를 넣고 답변을 받고 싶으면...
from langchain_core.prompts import ChatPromptTemplate

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
        ('system', '너는 이제 영어를 한국어로 번역하는 봇이야'),
        ('human', '{here}')    
        # ('ai', '여기는 예상 답변')
    ]
)

result = model.invoke(data.format_messages(here='i like kimchi'))
# result.content로 다른 내용은 제거
print(result.content)