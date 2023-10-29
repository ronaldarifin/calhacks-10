import gradio as gr

def process_text(cv_content, job_description):
    latex_code = f"\\text{{Text 1: {cv_content}}}\\text{{Text 2: {job_description}}}"
    return latex_code

iface = gr.Interface(
    fn=process_text, 
    inputs=[gr.Textbox(lines=5, placeholder="Enter your CV content here...", label="CV Content"), 
            gr.Textbox(lines=5, placeholder="Enter job description here...", label="Job Description")], 
    outputs=gr.Textbox(lines=10, label="Customized Resume"),  
    live=True,
)


iface.launch(inline=False, inbrowser=True)