# 📄 Documents Mentor AI App

Welcome to the **Document Question Answering App**! This application utilizes [Streamlit](https://streamlit.io/), [donut-base-finetuned-docvqa](https://huggingface.co/naver-clova-ix/donut-base-finetuned-docvqa), [Hugging Face Transformers](https://huggingface.co/transformers/), and [pdf2image](https://github.com/Belval/pdf2image) to answer questions about your documents. 🚀

## 🌟 Features

- **Upload PDF or Image files**: Upload your documents in PDF, PNG, JPG, or JPEG formats.
- **Convert PDFs to Images**: Automatically convert PDF documents into images for processing.
- **Question Answering**: Use advanced AI models to answer questions about your uploaded documents.

## 📦 Installation

To get started with the Document Question Answering App, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/document-question-answering.git
    cd document-question-answering
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```bash
    streamlit run app.py
    ```

## 🛠️ Usage

1. **Upload your document**: Use the sidebar to upload your PDF or image file.
2. **View the uploaded document**: The document will be displayed in the main window.
3. **Ask questions**: Enter your question in the text input box and press Enter. The app will process your question and display the answer.

## 🧠 Technologies Used

- **Streamlit**: For building the interactive web application.
- **Hugging Face Transformers**: For the document question-answering model.
- **pdf2image**: For converting PDF documents to images.
- **PIL (Pillow)**: For image processing tasks.
