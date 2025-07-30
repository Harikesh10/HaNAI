import gradio as gr
from rag import rag_bot
import json
import os

with open(os.path.abspath(os.path.join(os.path.dirname(__file__),"branding.json"))) as f:
    brand_info = json.load(f)["brand"]

with gr.Blocks(theme = "default" , title = brand_info["organizationName"]) as rag_app:
    gr.HTML(f""" <div style = "display:flex; justify-content:center;margin-bottom :20px;"
            <img src="{brand_info["logo"]["title"]}" alt = "{brand_info["organizationName"]} Logo" style="height:300px;width:200px">
            </div>""")
    
    gr.ChatInterface (
        fn=rag_bot,
     chatbot = gr.Chatbot(height=400 ,avatar_images=(None,brand_info["chatbot"]["avatar"]),
                          type = "messages"),
        title = brand_info["organizationName"],
        description=brand_info["slogan"],
        type ="messages",
        examples =[
            ["Who are you"],
            ["What is the nvidia share price"],
            ["Why is learning ai important"]
        ]
    )
        
if __name__ == "__main__":
    rag_app.launch()
    
    
    
    
    
    
