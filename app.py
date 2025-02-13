#AI Story generator App

#Import necessary libraries
import gradio as gr
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from fpdf import FPDF


def load_model():
    """
    Load the pre-trained GPT-2 model and tokenizer with error handling.
    
    Returns:
        model (GPT2LMHeadModel): Pre-trained GPT-2 model.
        tokenizer (GPT2Tokenizer): Pre-trained GPT-2 tokenizer.
        None or str: Returns None and error message if loading fails.
    """
    try:
        model = GPT2LMHeadModel.from_pretrained("gpt2-medium")
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
        return model, tokenizer
    except Exception as e:
        return None, str(e)


# Load model and tokenizer
model, tokenizer = load_model()

# Ensure the model is placed on the correct device (GPU or CPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if model is not None:
    model = model.to(device)


@torch.no_grad()  # Prevent tracking gradients during inference
def generate_story(prompt, max_length=200, temperature=0.7, top_p=0.55, top_k=60):
    """
    Generate a story based on the provided prompt using the GPT-2 model.
    
    Args:
        prompt (str): The starting text for the story generation.
        max_length (int): The maximum length of the generated story.
        temperature (float): The temperature to control randomness of generation.
        top_p (float): The top-p value for nucleus sampling.
        top_k (int): The top-k value for top-k sampling.
    
    Returns:
        str: The generated story or error message.
    """
    try:
        if model is None or tokenizer is None:
            raise ValueError("Model and tokenizer are not loaded properly.")
        
        inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
        outputs = model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            temperature=temperature,
            top_p=top_p,
            top_k=top_k,
            do_sample=True,
            pad_token_id=50256,
            attention_mask=torch.ones(inputs.shape, device=device)
        )
        story = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return story
    except Exception as e:
        return f"Error generating story: {e}"


def save_as_pdf(story):
    """
    Save the generated story as a PDF file.
    
    Args:
        story (str): The generated story to save in a PDF format.
    
    Returns:
        str: The path to the saved PDF file.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, story)
    pdf_output = "generated_story.pdf"
    pdf.output(pdf_output)
    return pdf_output


def generate_and_save_story(prompt, max_length, temperature, top_p, top_k):
    """
    Generate a story, save it as both a text file and a PDF, and return the results.
    
    Args:
        prompt (str): The prompt to generate the story.
        max_length (int): The maximum length of the story.
        temperature (float): Controls randomness of generation.
        top_p (float): Top-p sampling parameter.
        top_k (int): Top-k sampling parameter.
    
    Returns:
        tuple: The generated story, text file path, PDF file path, and footer with info.
    """
    try:
        story = generate_story(prompt, max_length, temperature, top_p, top_k)
        if not story:
            raise ValueError("Story generation failed. Please try again with a different prompt.")
        
        # Save as text file
        with open("generated_story.txt", "w") as f:
            f.write(story)
        
        # Save as PDF file
        pdf_file = save_as_pdf(story)
        
        footer = """ 
            Developed by [Karan Heera](https://github.com/KaranHeera).  
            Technologies: Gradio, PyTorch, Transformers, FPDF.
            Version: 1.0.0  
            Source Code: [GitHub](https://github.com/karanheera/AI-Story-Generator-using-GPT2.git)
        """
        return story, "generated_story.txt", pdf_file, footer
    except Exception as e:
        return f"Error generating or saving story: {str(e)}", None, None, None


# Gradio Interface Components
prompt_input = gr.Textbox(label="Enter a prompt for your story", lines=2, placeholder="A Brave man on border patrol...")
max_length_slider = gr.Slider(minimum=50, maximum=500, step=1, value=200, label="Maximum Length of Story")
temperature_slider = gr.Slider(minimum=0.5, maximum=1.5, step=0.05, value=0.7, label="Creativity (Temperature)")
top_p_slider = gr.Slider(minimum=0.5, maximum=1.0, step=0.05, value=0.55, label="Top-p Sampling")
top_k_slider = gr.Slider(minimum=30, maximum=100, step=10, value=60, label="Top-k Sampling")

# File outputs for downloading the generated story
file_output_txt = gr.File(label="Download as TXT")
file_output_pdf = gr.File(label="Download as PDF")

# Textbox output for displaying generated story
story_output = gr.Textbox(label="Generated Story", lines=15, interactive=False, placeholder="Generated story will appear here...")

# Markdown footer with developer info
footer = gr.Markdown("""
    Developed by [Karan Heera](https://github.com/KaranHeera).  
    Technologies: Gradio, PyTorch, Transformers, FPDF.
    Version: 1.0.0  
    Source Code: [GitHub](https://github.com/karanheera/AI-Story-Generator-using-GPT2.git)
""")

# Create Gradio interface
interface = gr.Interface(
    fn=generate_and_save_story,
    inputs=[prompt_input, max_length_slider, temperature_slider, top_p_slider, top_k_slider],
    outputs=[story_output, file_output_txt, file_output_pdf, footer],
    title="AI Story Generator using GPT-2",
    description="This app generates diverse and coherent stories using GPT-2. Give your prompt, generate the story and download it as a text or PDF file.",
    flagging_mode="never",
    cache_examples=True
)

# Launch Gradio interface
if __name__ == "__main__":
    interface.launch()
