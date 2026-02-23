from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#.env 파일 불러오기
load_dotenv()

# ChatOpenAI 모델 생성
chat = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7
)

# 질문해보기
response = chat.invoke("안녕, 넌 누구지?")
print("AI:", response.content)