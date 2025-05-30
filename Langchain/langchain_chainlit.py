from langchain_groq import ChatGroq
import json
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers.json import SimpleJsonOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from pydantic import BaseModel, Field
from typing import cast
import os
from dotenv import load_dotenv
load_dotenv()

import chainlit as cl

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")


@cl.on_chat_start
async def on_chat_start():
    # Define your desired data structure.
    class ProductDetails(BaseModel):
        name: str = Field(description="Name of the product")
        detail: str = Field(description="Description of the product")
        price: int = Field(description="Tentative price in USD")
    
    model = ChatGroq(model="gemma2-9b-it",temperature=0.7, streaming=True)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant. When asked about any product, respond in JSON with product name, details, and a tentative price in USD (integer)."),
            ("human", "{question}"),
        ]
    )
    runnable = prompt | model | SimpleJsonOutputParser(pydantic_object=ProductDetails, indent=2)
    cl.user_session.set("runnable", runnable)


@cl.on_message
async def on_message(message: cl.Message):
    runnable = cast(Runnable, cl.user_session.get("runnable"))

    result = await runnable.ainvoke(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    )

    # Convert the parsed dict to a formatted JSON string
    json_string = json.dumps(result, indent=2)

    # Send the formatted JSON block as a message
    await cl.Message(
        content=f"```json\n{json_string}\n```"
    ).send()

