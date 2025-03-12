from openai import OpenAI
import gradio as gr
import os

def generate_response(api_key, prompt): 
    # Create a client with the OPENAI_API_KEY
    client = OpenAI(api_key=api_key)

    try: 
        response = client.responses.create(
                model="gpt-4o",
                input = prompt
        )
        return response.output_text
    except Exception as e:
        return f"Error: {str(e)}"

# Create Gradio interface
demo = gr.Interface(
        fn=generate_response,
        inputs=[
            gr.Textbox(
                placeholder="OpenAI API key",
                type="password",
                label="OpenAI API key",
                value=os.environ.get("OPENAI_API_KEY", "")
            ),
            gr.Textbox(
                lines=4,
                placeholder="Enter your query",
                label="Query"
            )
        ],
        outputs=gr.Textbox(lines=20, label="Response to Query"),
        title="CodeLabsProAI",
        description="Orchestration Framework for Agentic Business and Finance Workflow using private and secure LLMs",
        examples=[
            [None, "Predict the stock price of SHOPIFY this summer taking into account geopolitical and global economic factors"],
            [None, "Predict the defence spending by European Union members taking into account geopolitical factors"],
            [None, "Predict the increase in trade between EU and Canada in 2025 taking into consideration all relevant factors"]
        ]
)


if __name__ == "__main__":
        demo.launch()

