from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.business_service import BusinessService
from data_access.openai_data_access import OpenAIDataAccess
from infrastructure.openai_service import OpenAIService
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

router = APIRouter()

class TopicRequest(BaseModel):
    topic: str
    lang: str

# Dependency injection
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key is not set in the environment variables.")

openai_service = OpenAIService(api_key=api_key)
data_access = OpenAIDataAccess(openai_service=openai_service)
business_service = BusinessService(data_access=data_access)

@router.post("/generate-topic")
async def generate_topic(request: TopicRequest):
    try:
        print("aqui entro al enrutador")
        response = business_service.generate_business_response(request.topic, request.lang)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))