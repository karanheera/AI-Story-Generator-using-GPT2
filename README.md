# AI Story Generator using GPT-2

## Description

This app is an AI-powered story generation app using **GPT-2**, a language model from **Hugging Face's Transformers** library. The app takes a prompt provided by the user and generates a coherent short story based on it. Users can customize the story's length and creativity by adjusting parameters such as temperature, top-p sampling, and top-k sampling. The generated story can be downloaded in both **text** and **PDF** formats. This app is built with **Gradio** to provide an easy-to-use interface for interaction.

### Key Features:
- **Story Generation**: Generate a story from a given prompt using GPT-2.
- **Adjustable Parameters**: Control the story’s length, creativity, and randomness with sliders for maximum length, temperature, top-p, and top-k.
- **Download Options**: Download the generated story as a **text file** or **PDF**.
- **User-Friendly Interface**: The app is built using Gradio, allowing an intuitive web interface.
- **Footer Info**: Display details about the app, including the developer’s GitHub link and technologies used.

## Demo

Try out the app by providing a prompt, adjusting the settings for creativity and length, and receiving an AI-generated story. You can download the generated story in **TXT** or **PDF** formats.

## Technologies Used

- **Gradio**: A Python library for building machine learning demos with a simple web interface.
- **Hugging Face Transformers**: For utilizing the GPT-2 model to generate the story.
- **PyTorch**: The underlying framework for running the GPT-2 model efficiently on a CPU or GPU.
- **FPDF**: Used for generating and saving the story in PDF format.
- **Python**: The programming language used to implement the app.

## Installation

### Prerequisites

To run this project locally, you need to have Python installed on your system. Then, install the required dependencies listed in the `requirements.txt` file.

### Steps to Install and Run Locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/karanheera/AI-Story-Generator-using-GPT2.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd AI-Story-Generator-using-GPT2
   ```

3. **Install required dependencies** using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

To run the app locally, use the following command:
```bash
python app.py
```
The Gradio app will start running locally, usually at [http://127.0.0.1:7860](http://127.0.0.1:7860/).

## File Structure

```plaintext
/AI-Story-Generator
│
├── app.py              # Main app file that runs the Gradio interface and story generation logic.
├── CODE_OF_CONDUCT.md  # Code of conduct file.
├── CONTRIBUTING.md     # Contribution guidelines.
├── LICENSE             # MIT License file.
├── README.md           # This file.
├── requirements.txt    # List of required Python libraries.
```

## Usage

### Input Parameters:
- **Enter a prompt for your story**: Provide a starting point for the AI to generate the story.
- **Maximum Length of Story**: Adjust the slider to set the maximum number of tokens (words/characters) the generated story can have.
- **Creativity (Temperature)**: Controls the randomness of the generated text. Higher values make the model more creative.
- **Top-p Sampling**: Controls diversity via nucleus sampling. A higher value focuses on the top candidates.
- **Top-k Sampling**: Limits the number of potential tokens to the top-k, controlling the randomness.

### Story Output:
- Once the user clicks on "Generate", the app will generate a story, which will appear in the output box.
- The generated story will also be available for download in **text** or **PDF** format.

### Downloading the Story:
- The generated story can be downloaded in two formats:
  - **TXT**: Click on "Download as TXT".
  - **PDF**: Click on "Download as PDF".

## License

This project is licensed under the **MIT License** - see the LICENSE file for details.

## Acknowledgements

This project uses the following libraries and technologies:
- **[GPT-2](https://huggingface.co/gpt2)** from Hugging Face’s **Transformers** library for text generation.
- **[Gradio](https://gradio.app/)** for building the web interface.
- **[PyTorch](https://pytorch.org/)** for running the GPT-2 model.
- **[FPDF](https://pyfpdf.github.io/)** for generating PDFs.
- **[Hugging Face Transformers](https://huggingface.co/transformers/)** for implementing transformer models like GPT-2.

Special thanks to the **Hugging Face** team for providing powerful models, and **Gradio** for making it easy to create interactive demos.

## Contributing

Contributions are welcome! If you find a bug or want to add a feature, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your forked repository.
4. Create a pull request with a clear explanation of your changes.

## Contact

For any questions or inquiries, please contact the project maintainer:

**Karan Heera**  
- LinkedIn: [https://www.linkedin.com/in/karanheera/](https://www.linkedin.com/in/karanheera/)  
- GitHub: [https://github.com/karanheera](https://github.com/karanheera)

