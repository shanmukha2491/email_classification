from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from utils import mask_email  # Custom utility to mask entities like names, emails, etc.
import uvicorn

# Create an instance of the FastAPI app
app = FastAPI()

# Load the pre-trained machine learning model for email classification
# This model should be trained and saved as 'email_classification_system.pkl'
model = joblib.load("email_classification_system.pkl")

# Define the structure of the incoming request using Pydantic
# It expects a JSON with one field: 'email_body'
class EmailRequest(BaseModel):
    email_body: str

# Define a POST endpoint at the root URL "/"
@app.post("/")
async def classify_email(request: EmailRequest):
    """
    Takes an email body as input, masks sensitive entities,
    classifies the email into a category, and returns the result.
    """
    # Extract the email body from the incoming request
    email_body = request.email_body

    # Mask sensitive or identifiable parts of the email
    # e.g., names, email addresses — this helps generalize the content
    masked_text, entity_list = mask_email(email_body)

    # Use the ML model to predict the category of the masked email
    category = model.predict([masked_text])[0]

    # Return a detailed response with original and processed content
    return {
        "input_email_body": email_body,
        "list_of_masked_entities": entity_list,
        "masked_email": masked_text,
        "category_of_the_email": category
    }

# This block allows the app to run with Uvicorn when executed directly (e.g., python api.py)
if __name__ == "__main__":
    # 'api:app' points to this file ('api.py') and the app object inside it
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
