from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

# 메시지 히스토리 생성
history = ChatMessageHistory()

def chat_with_memory(user_input):
    # 사용자 메시지 추가
    history.add_user_message(user_input)

    # AI 호출
    response = chat.invoke(history.messages)

    # AI 응답 저장
    history.add_ai_message(response.content)

    return response.content

# 대화 테스트
print("AI:", chat_with_memory("내 이름은 '황광연'이야"))
print("AI:", chat_with_memory("내 이름이 뭐야"))
print("AI:", chat_with_memory("내 이름으로 3행시 만들어줘"))

# 대화 기록 확인
print("\n=== 전체 대화 기록 ===")
for msg in history.messages:
    role = "나" if isinstance(msg, HumanMessage) else "AI"
    print(f"{role}: {msg.content}")