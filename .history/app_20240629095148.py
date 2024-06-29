from flask import Flask, request, jsonify
from llama_cpp import Llama
app = Flask(__name__)
llm = Llama(model_path="ggml-model-q4_k_m.gguf",n_gpu_layers=30)
input_prompt = """Below is a Human Input, write appropriate Response based on the input.

### Input:
{}

### Response:
{}"""
def model(message, max_tokens):
    prompt = input_prompt.format(
        message, # input
        ""              # leave blank as response generated by AI

    )

    output = llm(prompt, max_tokens=max_tokens)
    out = output['choices'][0]['text']
    generated_text = out
    first_response = generated_text.split('### Input:')[0].strip()
    return str(first_response)


@app.route('/api/deployment', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        username = request.args.get('message')
        response = response
        return jsonify({'response': username}), 200

    elif request.method == 'POST':
        data = request.get_json()
        username = data.get('message')
        return jsonify({'response': username}), 200

if __name__ == '__main__':
    app.run(debug=True)