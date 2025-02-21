import requests

API_KEY = "your_morph_api_key"  # Replace with your actual API key
MORPH_URL = "https://api.morph-data.io/generate"

def get_ai_response(player_input):
    data = {"prompt": player_input}
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.post(MORPH_URL, json=data, headers=headers)
    return response.json()  # Morph AI returns a JSON object

# Example Usage:
player_message = "Hello, NPC!"
ai_response = get_ai_response(player_message)
print("AI Response:", ai_response)