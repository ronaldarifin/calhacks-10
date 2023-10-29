import gradio as gr
from func import *


# def input_processing(alt1, alt2, alt3="hi"):
#     print(alt1, alt2)

# def similarity_search(alt1, alt2):
#     pass

def process_text(cv_content, job_description):
    latex_code = f"\\text{{Text 1: {cv_content}}}\\text{{Text 2: {job_description}}}"
    return latex_code

with gr.Blocks() as demo:
    with gr.Row():
        userInp = gr.Textbox(placeholder="What is your name?", label="Your Name")
        resumeInp = gr.Textbox(placeholder="Paste the entire contents of your Résume here", label="Your Resume")
        useGPT = gr.Radio(["GPT", "File", "JSON"], label="Resume Input", info="Which resume parser to use?")
    btn = gr.Button("Run")
    btn.click(fn=input_processing, inputs=[userInp, resumeInp, useGPT])

    gr.Interface(
        fn=similarity_search, 
        inputs=[gr.Textbox(lines=5, placeholder="Enter job description here...", label="Job Description")], 
        outputs=gr.Textbox(lines=10, label="Customized Resume"),  
        # live=True,
    )

demo.launch(inline=False, inbrowser=True)