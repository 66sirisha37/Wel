from flask import Flask, render_template, request, jsonify
import os
from groq import Groq
app = Flask(__name__)

client = Groq(
    api_key= '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',
)

def generate_request(user_input):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "I have been running an exam for my students Just give me option instead of the explanation",
            },
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('user_input')
    # response = f"You said: {user_input}"  # Echo back the input text
    response = generate_request(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
# 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