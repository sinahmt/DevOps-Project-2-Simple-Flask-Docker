# Containerizing a Flask App with Docker

## Overview

This project demonstrates how to containerize a simple Flask web application using Docker. It includes a `Dockerfile` to build a Docker image and instructions on how to run the application within a Docker container.

## Prerequisites

* **Docker:** Ensure you have Docker installed on your system. You can find installation instructions for various operating systems on the official Docker website.
* **Git:** (Optional but recommended) For cloning the repository.

## Running with Docker

This is the primary method for this project.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/sinahmt/DevOps-Project-2-Simple-Flask-Docker.git

    cd DevOps-Project-2-Containerizing-Flask-App
    ```

2.  **Build the Docker image:**
    Navigate to the project directory containing the `Dockerfile` and run:
    ```bash
    docker build -t flask-app .
    ```
    This command builds a Docker image named `flask-app` using the instructions in the `Dockerfile`.

3.  **Run the Docker container:**
    ```bash
    docker run -p 5000:5000 flask-app
    ```
    This command starts a Docker container from the `flask-app` image and maps port 5000 on your host machine to port 5000 inside the container.

4.  **Access the application:**
    Open your web browser and go to `http://localhost:5000/`. You should see the "Hello from Flask!" message along with the current date and time.

    You can also try the `/hello/<name>` endpoint, for example: `http://localhost:5000/hello/DockerUser`.

## Repository Contents

* `app.py`: The Flask web application code with the `/` and `/hello/<name>` endpoints.
* `Dockerfile`: Instructions for building the Docker image.
* `requirements.txt`: A list of Python dependencies (currently Flask).
* `README.md`: This documentation file.
* `LICENSE`: The project's license (MIT License).
