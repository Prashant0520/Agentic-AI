import streamlit as st
from langchain_groq import ChatGroq
import json
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers.json import SimpleJsonOutputParser
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
import anyio

load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Define Pydantic model for product details
class ProductDetails(BaseModel):
    name: str = Field(description="Name of the product")
    detail: str = Field(description="Description of the product")
    price: int = Field(description="Tentative price in USD")

# Initialize model and prompt without singleton
model = ChatGroq(model="gemma2-9b-it", temperature=0.7, streaming=True)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. When asked about any product, respond in JSON with product name, details, and a tentative price in USD (integer)."),
        ("human", "{question}"),
    ]
)
runnable = prompt | model | SimpleJsonOutputParser(pydantic_object=ProductDetails, indent=2)

st.title("Product Details AI Assistant")

user_input = st.text_input("Ask about any product:")

if st.button("Get Product Details") and user_input.strip():
    async def run_query(question: str):
        result = await runnable.ainvoke({"question": question})
        return result

    # Run async call in Streamlit sync context
    result = anyio.run(run_query, user_input)

    json_string = json.dumps(result, indent=2)
    st.code(json_string, language="json")
