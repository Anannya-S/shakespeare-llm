import gradio as gr
from ollama import Client

# ----------------------------------
# CONFIG
# ----------------------------------
APP_TITLE = "Ask Shakespeare"
APP_SUBTITLE = "Enter thy query, and the Bard shall reply!"
BACKGROUND_COLOR = "#8598DE"   
FONT_FAMILY = "Georgia"        
TEXT_COLOR = "#2c2c2c"
TITLE_COLOR = "#4b2e83"       

SHAKESPEARE_IMAGE = "shakespeare_portrait.png"  # path to Shakespeare portrait

# Predefined prompts 
prompts = {
    "Love Advice": "What is love, in thy noble words?",
    "Battle Speech": "Give me a fiery speech before a battle!",
    "Philosophy": "What thinkest thou of life and death?",
    "Comedy": "Tell me a humorous jest in thine own tongue.",
    "Friendship": "What say’st thou of true friendship?",
    "Betrayal": "Speak of treachery most foul.",
    "Dreams": "What dreams may come, wise bard?",
    "Wisdom": "Share thy timeless wisdom."
}

# ----------------------------------
# MODEL (Ollama client)
# ----------------------------------
client = Client()

def ask_custom(prompt):
    """Handle custom queries."""
    response = client.chat(
        model="shakespeare-model",  
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

def ask_predefined(prompt):
    """Handle predefined prompts."""
    response = client.chat(
        model="shakespeare-model",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]


# ----------------------------------
# BUILD GRADIO APP
# ----------------------------------
def create_app():
    with gr.Blocks(
        css=f"""
        body {{
            background-color: {BACKGROUND_COLOR};
            font-family: {FONT_FAMILY}, serif;
            color: {TEXT_COLOR};
        }}
        h1 {{
            color: {TITLE_COLOR};
            text-align: center;
            font-size: 5em;
        }}
        h2 {{
            text-align: center;
            font-size: 1.2em;
            margin-bottom: 20px;
        }}
        #bard {{
            display: block;
            margin-left: auto;
            margin-right: auto;
            border-radius: 20px;
            max-width: 300px;
            margin-bottom: 20px;
        }}
        """
    ) as demo:

        # Title & Image
        gr.Markdown(f"<h1>{APP_TITLE}</h1>")
        gr.Image(SHAKESPEARE_IMAGE, elem_id="bard", show_label=False)
        gr.Markdown(f"<h2>{APP_SUBTITLE}</h2>")

        # Custom Query Section
        user_input = gr.Textbox(lines=2, placeholder="Enter thy question...")
        ask_button = gr.Button("Ask the Bard")
        output_text = gr.Markdown(label="Shakespeare's Answer")

        ask_button.click(fn=ask_custom, inputs=user_input, outputs=output_text)

        # Predefined Prompts Section
        gr.Markdown("### Or choose a question below:")

        with gr.Row():
            for key in list(prompts.keys())[:4]:  # First row
                gr.Button(key).click(
                    fn=ask_predefined,
                    inputs=gr.Textbox(value=prompts[key], visible=False),
                    outputs=output_text
                )
        with gr.Row():
            for key in list(prompts.keys())[4:]:  # Second row
                gr.Button(key).click(
                    fn=ask_predefined,
                    inputs=gr.Textbox(value=prompts[key], visible=False),
                    outputs=output_text
                )

    return demo


if __name__ == "__main__":
    demo = create_app()
    demo.launch()
