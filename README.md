


## Handwritten Text Generation using Machine Learning
A Machine Learning–based handwritten text generation project that converts typed text into handwritten-style output images using handwritten word samples from a dataset.
The system searches matching handwritten word images from the dataset, crops them, combines them together, and generates a final handwritten sentence image.
## Project Overview
Handwritten Text Generation is a dataset-based text-to-handwriting generation system developed using Python and Streamlit.
This project does not recognize handwriting.
Instead, it generates handwritten-style output from typed text input.
The application works by:
Taking text input from the user
Searching handwritten word samples from the dataset
Cropping matching handwritten words
Combining cropped words into a sentence
Generating a final handwritten output image
This project demonstrates concepts related to:
Machine Learning
Dataset Handling
Image Processing
Text-to-Handwriting Generation
Streamlit Web Applications
## Features
Convert typed text into handwritten-style output
Dataset-based handwriting generation
Handwritten word image cropping
Dynamic sentence image generation
Interactive Streamlit web interface
Lightweight and easy-to-use system
Multiple word sentence support
## Dataset Information

The original dataset is not fully included due to GitHub size limitations.

Removed folders:
- train/
- test/
- valid/

Dataset Link:
https://huggingface.co/datasets/corto-ai/handwritten-text/tree/main/data


## Technologies Used
1.Programming Language
Python
2.Libraries
Streamlit
Pillow (PIL)
## How the System Works
Step 1 — User Input
The user enters text in the web application.
Example:
Bash
Hello World
Step 2 — Text Splitting
The sentence is split into individual words.
Example:
Bash
["Hello", "World"]
Step 3 — Dataset Search
The application searches the dataset for matching handwritten word samples.
Step 4 — Word Cropping
Matching handwritten word images are cropped from dataset samples.
Step 5 — Sentence Generation
The cropped handwritten words are combined together on a blank canvas.
Step 6 — Final Output
The final handwritten-style image is generated and displayed to the user.
## Dataset Information
This project uses a handwritten word image dataset.
The dataset contains handwritten word samples used to generate handwritten-style output images.
Due to GitHub storage limitations, large dataset files may not be fully included in this repository.
## Project Structure

Handwritten_Text_Generation/
│
├── sample_images/
│
├── screenshots/
│   ├── output1.png
│   ├── output2.png
│   ├── output3.png
│   ├── output4.png
│   ├── output5.png
│   └── output6.png
│
├── app.py
├── check_dataset.py
├── extract_images.py
├── generate_from_dataset.py
├── requirements.txt
└── README.md
## Installation Guide
Clone Repository

git clone <your-github-repository-link>
Go to Project Folder
Bash
cd Handwritten_Text_Generation
## Install Requirements

pip install -r requirements.txt
## Requirements

streamlit
pillow
## Run the Application

streamlit run app.py
After running the command, open:

http://localhost:8501
# Output Screenshots

## Output 1
![Output 1](screenshots/output1.png)

## Output 2
![Output 2](screenshots/output2.png)

## Output 3
![Output 3](screenshots/output3.png)

## Output 4
![Output 4](screenshots/output4.png)

## Output 5
![Output 5](screenshots/output5.png)

## Output 6
![Output 6](screenshots/output6.png)
## Advantages
Simple and lightweight project
Easy to understand workflow
Good beginner Machine Learning project
Demonstrates dataset handling concepts
Demonstrates image generation concepts
User-friendly interface
## Limitations
Output depends on dataset availability
Some words may not exist in dataset
Alignment may not always be perfect
Handwriting style depends on dataset samples
## Future Improvements
Multiple handwriting styles
Better word spacing and alignment
Download generated image option
Notebook paper background support
Deep learning–based handwriting generation
Real-time handwriting generation
Better sentence formatting
## Learning Outcomes
This project helped in understanding:
Image processing basics
Dataset handling
Word cropping techniques
Streamlit application development
Handwritten image generation systems
## Use Cases
Educational projects
Handwriting simulation
Machine Learning practice
Image processing demonstrations
Text-to-handwriting applications
## Developed By
Nayana N S
Handwritten Text Generation using Machine Learning
