from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

# 메시지 히스토리 생성
history = ChatMessageHistory()

history.add_message(SystemMessage(content="""
너는 친절한 AI 비서야.
- 사용자의 이름을 기억해
- 이전 대화 내용을 참고해서 답변해
- 한국어로 답변해
"""));

print("=== AI 챗봇 ===")
print("(종료하려면 'quit' 입력)")
print()

while True:
    user_input = input("나: ")

    if user_input.lower() == "quit":
        print("대화를 종료합니다.")
        break;

    # 사용자 메시지 추가
    history.add_user_message(user_input)

    # AI 호출
    response = chat.invoke(history.messages)

    # AI 응답 저장 및 출력
    history.add_ai_message(response.content)
    print(f"AI: {response.content}")
    print()