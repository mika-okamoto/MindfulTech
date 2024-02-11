from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain_openai import OpenAI, ChatOpenAI
from langchain.vectorstores import FAISS
from langchain_community.embeddings.openai import OpenAIEmbeddings
api_key = open('../api_key.txt').read()


def initModel():
    api_key = open('../api_key.txt').read()
    llm = OpenAI(api_key = api_key)

    template = """"You are a helpful and compassionate chatbot explaining about mental health disorders to employees in the tech industry at potential risk.
    They answered questions on a survey, and have been found to be at risk for {disorder}. 
    
    Context: {disorder_context}
    
    (if the context is irrelevant, ignore it and answer to the best of your abilities)
    
    Information about the person: 
    {survey}
    
    Their Past Prompts: {past_qs}
    
    Their Question: {question}
    
    Answer: """

    prompt = PromptTemplate.from_template(template)
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    past_questions = []
    db_anxiety = FAISS.load_local(f'../faiss_databases/{"anxiety"}', OpenAIEmbeddings(api_key=api_key))
    db_mood = FAISS.load_local(f'../faiss_databases/{"mood"}', OpenAIEmbeddings(api_key=api_key))

    return [llm_chain, past_questions, [db_anxiety, db_mood], 'Problem']


def chat(question, model):
    llm_chain = model[0]
    past_questions = model[1]
    dbs = model[2]
    problem = model[3]

    if 'quit' in question:
        return 'Thanks! Have a good day.'

    if problem is not None and problem == 'Anxiety':
        db = dbs[0]
    else:
        db = dbs[1]

    context = ""
    for t in db.similarity_search(question):
        context += t.page_content + "\n"

    memory_content = ""
    for i in past_questions:
        memory_content += i + "\n"

    ans = llm_chain.invoke({'disorder': problem, 'disorder_context': context, 'survey': "", 'question': question,
                            'past_qs': memory_content})['text']

    past_questions.append(question)
    if len(past_questions) > 5:
        past_questions.pop(0)

    return ans

