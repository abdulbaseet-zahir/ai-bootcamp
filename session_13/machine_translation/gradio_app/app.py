import os
import gradio as gr
import requests


def translate_with_api(text):
    url = os.environ.get("API_URL")
    if not url:
        print("API_URL not found in environment variables")
        url = "http://localhost:8000/translate/"

    response = requests.post(url, json={"text": text})
    return response.json()["translation"]


iface = gr.Interface(
    fn=translate_with_api,
    inputs=gr.Textbox(label="Input English Text"),
    outputs=gr.Textbox(label="Translated German Text"),
    title="English to German Translator",
)

iface.launch(server_port=8080, server_name="0.0.0.0")
