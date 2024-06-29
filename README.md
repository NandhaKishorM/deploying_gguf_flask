# GGUF Model Deployment Guide

Sample deployment configuration

## Prerequisites

- Python 3.8 or higher

## Installation

1. Install the required Python packages.

```sh
pip install llama-cpp-python
pip install flask
```
thows error
Download and install Anaconda python from [here](https://www.anaconda.com/download)

```sh
conda create -n deeplearning python=3.8
conda activate deeplearning
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install llama-cpp-python
pip install flask
```

2. Download the required model file from [here](https://drive.google.com/file/d/13UUBxOuFUrbrTGGuPxT7WXJpldSjbqXO/view).

## Deployment

1. Run the `app.py` script to start the Flask server.

```sh
python app.py
```

2. In a new terminal, run the `post_request.py` script to send a POST request to the server.

```sh
python post_request.py
```

## Code Explanation

`app.py` is the main server file that uses Flask to create a web API. It uses the Llama library to generate responses based on the input message.

`post_request.py` is a script that sends a POST request to the server with a message. The server then uses the Llama library to generate a response and sends it back to the client.

## Sample Request

You can send a POST request to `http://localhost:5000/api/deployment` with the following JSON body:

```json
{
    "message": "what are the best pesticides for crops in Kerala?"
}
```

The server will respond with the AI-generated response.

## Deploying flask in production
Clicke [here](https://medium.com/techfront/step-by-step-visual-guide-on-deploying-a-flask-application-on-aws-ec2-8e3e8b82c4f7) to learn more on how to deploy a flask application in production

