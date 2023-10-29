import gradio as gr
from func import *


def process_text(cv_content, job_description):
    latex_code = f"\\text{{Text 1: {cv_content}}}\\text{{Text 2: {job_description}}}"
    return latex_code

with gr.Blocks() as demo:
    inp = gr.Textbox(placeholder="What is your name?")
    btn = gr.Button("Run")
    btn.click(fn=input_processing, inputs=inp)

    gr.Interface(
        fn=similarity_search, 
        inputs=[gr.Textbox(lines=5, placeholder="Enter job description here...", label="Job Description")], 
        outputs=gr.Textbox(lines=10, label="Customized Resume"),  
        # live=True,
    )

demo.launch(inline=False, inbrowser=True)