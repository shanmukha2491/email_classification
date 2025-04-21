from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
from utils import mask_email
import uvicorn

app = FastAPI()
model = joblib.load("email_classification_system.pkl")

class EmailRequest(BaseModel):
    email_body: str

@app.post("/")
async def classify_email(request: EmailRequest):
    email_body = request.email_body
    masked_text, entity_list = mask_email(email_body)
    category = model.predict([masked_text])[0]
    
    return {
        "input_email_body": email_body,
        "list_of_masked_entities": entity_list,
        "masked_email": masked_text,
        "category_of_the_email": category
    }


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
