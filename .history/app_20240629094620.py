from flask import Flask, request, jsonify
from llama_cpp import Llama
app = Flask(__name__)
llm = Llama(model_path="/content/final_weights_new/ggml-model-q4_k_m.gguf",n_gpu_layers=30)
@app.route('/api/deployment', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        username = request.args.get('message')
        return jsonify({'method': 'GET', 'username': username}), 200

    elif request.method == 'POST':
        data = request.get_json()
        username = data.get('message')
        return jsonify({'method': 'POST', 'username': username}), 200

if __name__ == '__main__':
    app.run(debug=True)