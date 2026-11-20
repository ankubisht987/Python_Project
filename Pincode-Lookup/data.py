import os
import json
from dotenv import load_dotenv
# from openai import OpenAI
from langchain_openai import ChatOpenAI

from langchain_core.messages import  SystemMessage, HumanMessage

load_dotenv()

llm = ChatOpenAI(
    model="openrouter/free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url=os.getenv("OPENROUTER_BASE_URL"),
    temperature=0
)

SYSTEM_PROMPT="""You are an Indian PIN code search assistant.

Understand natural language queries about Indian locations.

Extract:
- location
- city
- state
- district
- pincode
- intent

Possible intents:
- location_to_pincode
- pincode_to_location
- clarification_required

Never invent PIN codes.

Return JSON only in this format:

{
    "intent": "location_to_pincode",
    "location": "New Delhi",
    "city": "New Delhi",
    "state": "Delhi",
    "district": null,
    "pincode": null
}
"""

def understand_query(query: str):
    response = llm.invoke([
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=query)
        ]
    )
    try:
        result= json.loads(response.content)
    except(json.JSONDecodeError, TypeError):
        raise ValueError("AI Response invalid JSON")


    return result
