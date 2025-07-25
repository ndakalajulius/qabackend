# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import openai
from config import OPENAI_API_KEY
from schemas import QuestionRequest, AnswerResponse


app = FastAPI(title="AI Q&A API")

# Allow frontend access (adjust if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = OPENAI_API_KEY

@app.get("/")
def read_root():
    return {"message": "AI Q&A API is running"}

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(payload: QuestionRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or any free-tier model
            messages=[{"role": "user", "content": payload.question}],
            temperature=0.7,
            max_tokens=300
        )

        return {"answer": response.choices[0].message["content"].strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
