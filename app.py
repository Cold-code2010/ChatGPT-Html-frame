from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process_request():
    user_input = request.json["user_input"]
    openai_key = request.json["openai_key"]
    selected_model = request.json["model"]
    
    # 设置 OpenAI 密钥
    openai.api_key = openai_key
    
    # 调用 ChatGPT 模型
    response = openai.ChatCompletion.create(
        model=selected_model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    
    # 提取 ChatGPT 的回复
    gpt_response = response.choices[0].message["content"]
    
    return jsonify({
        "user_input": user_input,
        "gpt_response": gpt_response
    })

if __name__ == "__main__":
    app.run()
