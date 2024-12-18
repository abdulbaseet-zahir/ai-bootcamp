import os
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer


# Define a Pydantic model for the request body
class TranslationRequest(BaseModel):
    text: str


app = FastAPI()

# CORS configuration (optional, if needed)
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the translation model
model_path = os.getenv("MODEL_PATH")
if not model_path:
    print("The environment variable MODEL_PATH is not set!")
    model_path = "t5-en-de"


model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained("t5-small")
pipe = pipeline("translation_en_to_de", model=model, tokenizer=tokenizer)


# Define the POST endpoint
@app.post("/translate/")
async def translate(request: TranslationRequest):
    translation = pipe(request.text)[0]["translation_text"]
    return {"translation": translation}
