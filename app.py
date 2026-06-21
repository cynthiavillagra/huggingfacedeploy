# app.py
import gradio as gr

def saludar(nombre):
    return f"Hola, {nombre} 👋"

demo = gr.Interface(
    fn=saludar,
    inputs="text",
    outputs="text",
    title="Mi primera app en Hugging Face Spaces"
)

demo.launch()