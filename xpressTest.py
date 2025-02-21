import requests

API_KEY = "your_xpress_ai_api_key"  # Replace with your actual API key
XPRESS_URL = "https://api.xpress.ai/generate"

def get_ai_response(player_input):
    data = {"prompt": player_input}
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.post(XPRESS_URL, json=data, headers=headers)
    return response.json()  # Returns AI-generated response

# Example Usage:
player_message = "Tell me a story about this kingdom."
ai_response = get_ai_response(player_message)
print("AI Response:", ai_response)
