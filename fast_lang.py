#!/usr/bin/env python
from typing import List

from fastapi import FastAPI

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.agents import create_openai_functions_agent
from langchain.agents import AgentExecutor
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.messages import BaseMessage
from langserve import add_routes
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
llm = Ollama(model="llama2:13b-chat")
# 1. Load Retriever
loader = WebBaseLoader("https://docs.smith.langchain.com/user_guide")
docs = loader.load()
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
from langchain_community.embeddings import OllamaEmbeddings
embeddings = OllamaEmbeddings()
vector = FAISS.from_documents(documents, embeddings)
retriever = vector.as_retriever()

# 2. Create Tools
# retriever_tool = create_retriever_tool(
#     retriever,
#     "langsmith_search",
#     "Search for information about LangSmith. For any questions about LangSmith, you must use this tool!",
# )
# search = TavilySearchResults()
# tools = [search]
tools = []


# 3. Create Agent

prompt_template = PromptTemplate.from_template(
    "Tell me a {adjective} joke about {content}."
)
from langchain.chains import LLMChain
prompt = prompt_template.format(adjective="funny", content="chickens")
agent = LLMChain(llm= llm, prompt=prompt)
agent_executor = AgentExecutor(agent=agent,  verbose=True)


# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route

# We need to add these input/output schemas because the current AgentExecutor
# is lacking in schemas.

class Input(BaseModel):
    input: str
    chat_history: List[BaseMessage] = Field(
        ...,
        extra={"widget": {"type": "chat", "input": "location"}},
    )


class Output(BaseModel):
    output: str

add_routes(
    app,
    agent_executor.with_types(input_type=Input, output_type=Output),
    path="/agent",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)