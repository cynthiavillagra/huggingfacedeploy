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

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860))
    )
