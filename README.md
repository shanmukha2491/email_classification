# Email Classification API

## Setup

```bash
git clone <repo_url>
cd email_classifier
pip install -r requirements.txt
python app.py  # trains the model
uvicorn api:app --reload
