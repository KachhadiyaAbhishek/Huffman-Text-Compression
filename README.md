# Huffman Compression Web Application

This is a simple web application built using Flask that implements Huffman coding for text compression and decompression. It allows users to compress and decompress text based on Huffman coding, a lossless data compression algorithm.

## Features

- **Compress**: Users can enter text, and the app will compress it using Huffman coding.
- **Decompress**: Users can decompress the previously compressed text back to its original form.
- **Display Compression Info**: The app shows the length of the compressed text.
- **Error Handling**: The app handles errors like empty input or missing compressed text.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **Python**: The main programming language used for implementing the Huffman compression algorithm.

## Project Structure


### main.py
This is the core Python file that handles the logic for:
- Constructing the Huffman tree (`huffman_tree`)
- Generating Huffman codes (`huffman_codes`)
- Compressing and decompressing the text (`compress` and `decompress`)
- Running the Flask web application

### index.html
This file provides the user interface for the application. It includes:
- A text input form for users to enter text
- Buttons to trigger compression and decompression
- Display areas for compressed text and decompressed text
