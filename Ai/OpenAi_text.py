from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            # info 프롬프트 설명하는 곳
            "role": "developer",
            "content": "Talk like a pirate."
        },
        {
            # info user가 질문하는 곳
            "role": "user",
            "content": "Are semicolons optional in JavaScript?"
        }
            # note "role": "assistant"도 있는데 여기는 모범 답안을 적어두는 부분
    ]
)

print(response.output_text)