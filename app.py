import os
import gradio as gr

def saludar(nombre):
    return f"Hola {nombre}"

demo = gr.Interface(
    fn=saludar,
    inputs="text",
    outputs="text"
)

port = int(os.environ.get("PORT", 10000))

demo.launch(
    server_name="0.0.0.0",
    server_port=port
)
