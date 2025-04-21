import re

PII_PATTERNS = {
    "full_name": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}/\d{2}/\d{4}\b",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2,4}\b"
}

def mask_email(email_text):
    entity_list = []
    masked_email = email_text
    for entity, pattern in PII_PATTERNS.items():
        for match in re.finditer(pattern, masked_email):
            start, end = match.span()
            entity_value = match.group()
            entity_list.append({
                "position": [start, end],
                "classification": entity,
                "entity": entity_value
            })
            masked_email = masked_email.replace(entity_value, f"[{entity}]")
    return masked_email, entity_list
