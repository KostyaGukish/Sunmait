# Sunmait Intership Project

## Project Description

This project is a simple FastAPI application that provides a API for Hugging Face model inference. Model solves the problem of text summarization.

## Model

The model used is `IlyaGusev/rut5_base_sum_gazeta` from Hugging Face. It is a pre-trained model for text summarization.

## API

The API provides the following endpoints:
- `/predict`: takes a text as input and returns a summary of the text.
- `/ping`: returns a simple message to check if the API is running.

## Tools

- **FastAPI**: for creating the API
- **Hugging Face**: for model inference
- **Python**: used programming language
- **uv**: for managing the project and its dependencies
- **Ruff**: for linting the code
- **pre-commit**: for managing pre-commit hooks
- **pytest**: for testing the code

## Requirements

All requirements are listed in `pyproject.toml` file. To install them, run:

```
pip install uv
uv venv
uv install
```

