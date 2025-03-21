import google.generativeai as genai
import base64

# Replace with your actual Gemini API key
API_KEY = "AIzaSyBa42s7OVktT90svedOoENZH0uKaxNrkQU"
genai.configure(api_key=API_KEY)

def encode_image(image_path):
    """Converts an image to a base64-encoded string."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_food_from_image(image_path):
    """Identifies food from an image using the updated Gemini API."""
    model = genai.GenerativeModel("gemini-1.5-flash")  # Updated model version
    image_base64 = encode_image(image_path)  # Convert image to base64
    
    response = model.generate_content([
        "Identify the food in this image.",
        {"mime_type": "image/jpeg", "data": image_base64}  # Corrected input format
    ])
    
    return response.text if response else "Food identification failed."

# Example usage (Pass the image path here)
IMAGE_PATH = "C:/web/project 1/food_image.jpg"  # Change this to your actual image file
food_item = get_food_from_image(IMAGE_PATH)
print("Identified Food:", food_item)
