import gradio as gr
from fastapi import FastAPI


def saludar(nombre):
    return f"Hola {nombre}"


demo = gr.Interface(
    fn=saludar,
    inputs="textbox",
    outputs="textbox",
    title="Mi app Gradio"
)


app = FastAPI()

app = gr.mount_gradio_app(
    app,
    demo,
    path="/"
)
