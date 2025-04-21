# Import the training function from the models module
from models import train_model

# This block ensures the training only runs when this script is executed directly,
# and not when it's imported as a module elsewhere
if __name__ == "__main__":
    # Notify the user that model training has started
    print("🚀 Training the model...")

    # Call the function that handles model training
    train_model()

    # Let the user know that training is complete
    print("✅ Model training complete.")
