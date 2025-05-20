import gradio as gr

from prompting_workshop.main import rag_app


def rag_app_wrapper(message, history):
    response, _ = rag_app(message)
    return response.content


gr.ChatInterface(fn=rag_app_wrapper, type="messages").launch()
