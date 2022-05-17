# URL Shortener

## Table of contents:
1. [Prerequisites](#prereqs)
2. [Repository setup](#setup)


## Prerequisites <a name="prereqs"/>
1. [Python](https://www.python.org/) (version 3.9)


## Repository setup <a name="setup"/>
1. Create & and source virtual environment:
    1. Linux:
        ```sh
        VENV_DIR=".venv"
        python3 -m venv $VENV_DIR
        source $VENV_DIR/bin/activate
        ```
    2. Windows:
        ```powershell
        $VENV_DIR=".venv"
        python3 -m venv $VENV_DIR
        . $VENV_DIR\Scripts\activate
        ```

2. Install libraries:
    ```sh
    pip install poetry
    poetry install
    ```

3. Everything is READY!
    ```sh
    python url_shortener/app.py
    ```