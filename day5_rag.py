from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

# 1. PDF 로드
print("PDF 로딩 중...")
loader = PyPDFLoader("company_info.pdf")
pages = loader.load()

# 2. 텍스트 분할
print("텍스트 분할 중...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
)
chunks = splitter.split_documents(pages)
print(f"총 {len(chunks)}개 청크 생성")


# 3. 벡터 DB생성(한국어 모델)
print("벡터 DB 생성중...")
embeddings = HuggingFaceEmbeddings(
    model_name="jhgan/ko-sroberta-multitask",
)
vectordb = Chroma.from_documents(documents=chunks, embedding=embeddings)

# 4. LLM 준비
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 5. RAG 프롬프트
prompt = ChatPromptTemplate.from_template("""
아래 문서를 참고해서 질문에 답변해주세요.
문서에 없는 내용은 "문서에 해당 정보가 없습니다"라고 답해주세요.

[참고 문서]
{context}

[질문]
{question}

[답변]
""")

def ask_pdf(question):
    docs = vectordb.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    chain = prompt | chat
    response = chain.invoke({"context":context, "question":question})

    return response.content

# 7. 대화형 Q&A
print("\n" + "=" * 50)
print("PDF Q&A 시스템 준비 완료!")
print("질문을 입력하세요. (종료: q)")
print("="*50 + "\n")

while True:
    question = input("질문: ")
    if question.lower() == 'q':
        print("종료합니다.")
        break

    answer = ask_pdf(question)
    print(f"답변: {answer}\n")