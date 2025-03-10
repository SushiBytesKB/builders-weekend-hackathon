from flask import Flask, request
from openai import OpenAI

# Setting Up Flask Server and API Requests
app = Flask(__name__)

# Eldrin AI Agent URL and Token from Xpress.ai
XPRESS_AI_URL = "https://kagolanu-sushant.ap.xpressai.cloud/api/npcscript-agent/"
XPRESS_AI_KEY = "f1189cbc-519c-4eaa-b63e-ab26a55e8dd3" 

# Memory for Remembering Conversation with Player
npc_memory = [] 

# POST Request for Sending NPC Response to UE5
@app.route('/chat', methods=['POST'])
def chat():
    #Receives plain text input, sends it to Eldrin AI, and returns response as plain text.
    player_input = request.data.decode("utf-8")  # Get raw text instead of JSON

    # Send the input to Xpress AI
    client = OpenAI(
        base_url=XPRESS_AI_URL,
        api_key=XPRESS_AI_KEY
    )

    messages = npc_memory + [{"role": "user", "content": player_input}]

    response = client.chat.completions.create(
        model="Eldrin",
        messages=messages
    )

    npc_reply = response.choices[0].message.content

    # Track conversation memory
    npc_memory.append({"role": "user", "content": player_input})
    npc_memory.append({"role": "assistant", "content": npc_reply})

    return npc_reply  # Return plain text response instead of JSON

# Runs with URL http://127.0.0.1:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
