import re

# Dictionary containing patterns to identify different types of Personally Identifiable Information (PII)
PII_PATTERNS = {
    "full_name": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",                        # Example: John Doe
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",         # Example: john.doe@example.com
    "phone_number": r"\b\d{10}\b",                                     # Example: 9876543210
    "dob": r"\b\d{2}/\d{2}/\d{4}\b",                                   # Example: 01/01/2000
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",                            # Example: 1234 5678 9012
    "credit_debit_no": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",     # Example: 1234 5678 9012 3456 or 1234-5678-9012-3456
    "cvv_no": r"\b\d{3}\b",                                            # Example: 123
    "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2,4}\b"                        # Example: 01/25
}

def mask_email(email_text):
    """
    This function scans the given email text for PII (Personally Identifiable Information),
    masks detected entities with placeholders, and returns both the masked text and a list of detected entities.
    
    Parameters:
    - email_text (str): The body of the email to scan and mask.

    Returns:
    - masked_email (str): The email text with sensitive data masked.
    - entity_list (list): A list of dictionaries containing position, classification, and actual entity value.
    """

    entity_list = []            # List to store details of each detected entity
    masked_email = email_text   # We'll apply masking to this variable (original remains untouched)

    # Loop through each type of PII and its associated regex pattern
    for entity, pattern in PII_PATTERNS.items():
        # Find all matches for the current pattern in the text
        for match in re.finditer(pattern, masked_email):
            start, end = match.span()         # Get start and end positions of the match
            entity_value = match.group()      # The actual matched text

            # Save the match details in a structured way
            entity_list.append({
                "position": [start, end],
                "classification": entity,
                "entity": entity_value
            })

            # Replace the matched value in the text with a placeholder
            masked_email = masked_email.replace(entity_value, f"[{entity}]")

    return masked_email, entity_list
