from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

# 1. 번역기 텐플릿
translator = PromptTemplate(
    input_variables=["language", "text"],
    template="다음 텍스트를 {language}로 번역해줘:\n{text}",
)

# 2. 요약기 템플릿
summarizer = PromptTemplate(
    input_variables=["text", "lines"],
    template="다음 텍스트를 {lines}줄로 요약해줘:\n{text}",
)

# 3. 코드설명하는 템플릿
code_explainer = PromptTemplate(
    input_variables=["code"],
    template="다음 코드를 초보자도 이해할 수 있게 설명해줘:\n```\n{code}\n```",
)
# 3. 코드 설명기 템플릿
code_explainer = PromptTemplate(
    input_variables=["code"],
    template="다음 코드를 초보자도 이해할 수 있게 설명해줘:\n```\n{code}\n```"
)

# 테스트
print("=== 번역기 ===")
prompt1 = translator.format(language="영어", text="안녕하세요, 저는 백엔드 개발자입니다.")
print(chat.invoke(prompt1).content)
print()

print("=== 요약기 ===")
long_text = """
LangChain은 대규모 언어 모델을 활용한 애플리케이션 개발을 위한 프레임워크입니다.
다양한 LLM을 쉽게 연결하고, 프롬프트 관리, 체인 구성, 메모리 관리 등의 기능을 제공합니다.
RAG, 에이전트, 챗봇 등 다양한 AI 애플리케이션을 만들 수 있습니다.
"""
prompt2 = summarizer.format(text=long_text, lines="2")
print(chat.invoke(prompt2).content)
print()

print("=== 코드 설명기 ===")
code = """
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
"""
prompt3 = code_explainer.format(code=code)
print(chat.invoke(prompt3).content)