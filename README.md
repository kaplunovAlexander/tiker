# Video Generation Application

## Description

This Django-based application allows users to generate videos with custom text input. Users can provide text through a URL parameter, and the application processes this text to create a video where the text moves from right to left across the screen. Additionally, the application logs all incoming requests to the database for future reference.

## Features

- Generate videos with custom text input.
- Log all incoming requests, including text parameters, to the database.
- Admin interface for viewing and managing logged requests.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd yourrepository
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Apply database migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. Create a superuser for accessing the admin interface:
    ```bash
    python manage.py createsuperuser
    ```
6. Run the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and navigate to `http://127.0.0.1:8000/admin/` to log in to the admin interface using the superuser credentials.
2. To generate a video, use the following URL format:
    ```
    http://127.0.0.1:8000/videoapp/generate/?text=YourTextHere
    ```
3. The generated video will be available for download.

## Middleware and Request Logging

The application uses custom middleware to log all incoming requests. This includes details such as the request path, method, timestamp, remote address, query parameters, and user agent.

