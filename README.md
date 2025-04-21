---
title: Email Classification API
emoji: ✉️
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 8000
---

# Email Classification System

API for classifying support emails with PII masking.

## API Usage

Send a POST request to `/` with JSON body:
```json
{
    "email_body": "Your email content here"
}