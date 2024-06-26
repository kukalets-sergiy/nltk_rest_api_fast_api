# nltk_rest_api_fast_api

## Description
This project provides a REST API for performing text processing operations using the NLTK (Natural Language Toolkit) library.

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd rest_api_natural_language_toolkit
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Unix
    venv\Scripts\activate  # Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Download the necessary NLTK data:
    ```bash
    python setup_nltk.py
    ```

5. Run the application:
    ```bash
    uvicorn app.main:app --reload
    ```

## Endpoints

### /tokenize
- **Method:** POST
- **Parameters:** JSON with a `text` field.
- **Response:** JSON array of tokens.

### /pos_tag
- **Method:** POST
- **Parameters:** JSON with a `text` field.
- **Response:** JSON array of (token, tag) pairs.

### /ner
- **Method:** POST
- **Parameters:** JSON with a `text` field.
- **Response:** JSON array of entities and their types.
