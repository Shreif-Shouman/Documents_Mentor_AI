import streamlit as st
from transformers import DonutProcessor, VisionEncoderDecoderModel
from pdf2image import convert_from_path
import tempfile
import os
from PIL import Image

# Set the title for the app
st.title("Document Question Answering App")

# Initialize the Donut model and processor
processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")

# Function to convert PDF to images
def pdf_to_images(pdf_file):
    with tempfile.TemporaryDirectory() as temp_dir:
        images = convert_from_path(pdf_file, output_folder=temp_dir)
        image_paths = [os.path.join(temp_dir, f"{i}.png") for i in range(len(images))]
        for i, image in enumerate(images):
            image.save(image_paths[i], 'PNG')
        return image_paths

# Function to extract answer from the model response
def get_answer(image, question):
    pixel_values = processor(image, return_tensors="pt").pixel_values
    task_prompt = f"<s_docvqa><s_question>{question}</s_question><s_answer>"
    inputs = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt")
    outputs = model.generate(pixel_values, **inputs)
    answer = processor.batch_decode(outputs, skip_special_tokens=True)[0]
    # Clean the answer to remove the question and keep only the answer
    answer = answer.replace(f'{question}', '').replace('<s_answer>', '').replace('</s_answer>', '').strip()
    return answer

# Sidebar for file upload
st.sidebar.header("Upload your document")
uploaded_file = st.sidebar.file_uploader("Upload PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    # Handle PDF files
    if uploaded_file.type == "application/pdf":
        image_paths = pdf_to_images(uploaded_file)
    else:
        # Handle image files
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_file.flush()
            image_paths = [temp_file.name]

    # Display the uploaded document
    st.image(image_paths, caption="Uploaded Document", use_column_width=True)

    # Chat box for questions
    st.header("Ask a Question about the Document")
    user_question = st.text_input("Your question:", key="user_question")

    # Process the question when the user presses Enter
    if user_question:
        for i, image_path in enumerate(image_paths):
            image = Image.open(image_path).convert("RGB")
            answer = get_answer(image, user_question)
            st.write(f"Response from page {i + 1}: {answer}")
