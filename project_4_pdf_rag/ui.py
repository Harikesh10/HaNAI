import gradio as gr
import json
import os
from pdf_rag import pdf_ragbot

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"branding.json"))) as f:
    brand_info = json.load(f)["brand"]

with gr.Blocks(theme="default",title = brand_info["organizationName"]) as pdf_app:
    gr.HTML = (f"""<div style="display:flex;justify-content:center;margin-bottom:20px;">
               <img src="{brand_info["logo"]["title"]}" alt={brand_info["organizationName"]} Logo" style="width:100px; height:400px">
               </div>""")
    gr.ChatInterface (
        fn = pdf_ragbot,
        chatbot=gr.Chatbot(height=400, avatar_images=(None,brand_info["chatbot"]["avatar"]),type = "messages"),
        type = "messages",
        title= brand_info["organizationName"],
        description= brand_info["slogan"],
    )
    
if __name__ =="__main__":
    pdf_app.launch(share=True)
