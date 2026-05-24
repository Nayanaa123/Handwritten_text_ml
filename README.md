# Handwritten Text Recognition System

A Machine Learning–based Handwritten Text Recognition (HTR) project that converts handwritten images into readable text using image processing and trained models.

---

## 1. Project Overview

This project recognizes handwritten text from images using a trained ML model. The system processes images, crops them into word-level segments, and predicts each word using the model. Final output is generated from cropped word images.

---

## 2. Dataset Information

The original dataset is not fully included due to GitHub size limitations.

Removed folders:
- train/
- test/
- valid/

Dataset Link:
https://huggingface.co/datasets/corto-ai/handwritten-text/tree/main/data


---

## 3. Word Cropping Process

1. Input handwritten image is uploaded  
2. Image is preprocessed (grayscale, noise removal, resizing)  
3. Image is segmented into words (cropping)  
4. Each cropped word is passed to ML model  
5. Model predicts one word per image  
6. Final sentence is formed by combining all outputs  

---

## 4. Features

1. Handwritten image preprocessing  
2. Word-level segmentation  
3. ML model prediction  
4. Text generation from images  
5. Output visualization system  

---

## 5. Project Structure

```text
handwritten-project/
├── app.py
├── train.py
├── check_dataset.py
├── extract_dataset.py
├── requirements.txt
├── dataset/
├── models/
├── generated/
├── screenshots/
│   ├── output1.png
│   ├── output2.png
│   ├── output3.png
│   ├── output4.png
│   ├── output5.png
│   └── output6.png
└── README.md
