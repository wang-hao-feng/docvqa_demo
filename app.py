import os
import gradio as gr

example_doc_path = ['image1.jpg', 'image2.jpg']
example_question = ['q1', 'q2']

with gr.Blocks(title='DocVQA') as demo:
    gr.Markdown(value='# <center> DocVQA </center>')
    with gr.Row():
        with gr.Column():
            image_board = gr.Image(height=500, type='pil')
        with gr.Column():
            question_text = gr.Textbox(label='question')
            answer_text = gr.Textbox(label='answer')
            with gr.Row():
                #clear = gr.Button(value='Clear')
                submit_btn = gr.Button(value='Submit')
    gr.Examples(examples=[list(pair) for pair in zip([os.path.join(os.path.join(os.path.dirname(__file__), 'image'), path) for path in example_doc_path], example_question)], 
                inputs=[image_board, question_text])
    
    # submit
    def submit(image, question):
        answer = 'a' + question[-1]
        return answer
    submit_btn.click(fn=submit, inputs=[image_board, question_text], outputs=answer_text)

demo.launch()