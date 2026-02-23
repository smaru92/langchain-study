from langchain_openai import ChatOpenAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")
history = ChatMessageHistory()

def chat_with_memory(user_input):
    history.add_user_message(user_input)
    response = chat.invoke(history.messages)
    history.add_ai_message((response.content
                            ))