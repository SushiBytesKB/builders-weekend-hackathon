from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Xpress AI Agent API details
XPRESS_AI_URL = "https://kagolanu-sushant.ap.xpressai.cloud/api/npcscript-agent/"
XPRESS_AI_KEY = "f1189cbc-519c-4eaa-b63e-ab26a55e8dd3"  # Replace with your actual API key

# Memory to track past interactions
npc_memory = []

def get_npc_response(player_input):
    """Send player input to Xpress AI Eldrin agent and get response."""
    client = OpenAI(
        base_url=XPRESS_AI_URL,
        api_key=XPRESS_AI_KEY
    )

    # Create conversation history to maintain NPC memory
    messages = npc_memory + [{"role": "user", "content": player_input}]

    response = client.chat.completions.create(
        model="Eldrin",
        messages=messages
    )

    npc_reply = response.choices[0].message.content

    # Update memory to track NPC mood and respect level
    npc_memory.append({"role": "user", "content": player_input})
    npc_memory.append({"role": "assistant", "content": npc_reply})

    return npc_reply

@app.route('/eldrin', methods=['POST'])
def eldrin_chat():
    """API endpoint to receive player input from UE5 and return NPC dialogue."""
    data = request.json
    player_input = data.get("player_input", "")

    if not player_input:
        return jsonify({"error": "No input received"}), 400

    npc_response = get_npc_response(player_input)
    
    return jsonify({"npc_response": npc_response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)