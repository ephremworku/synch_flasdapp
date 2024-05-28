# Flask App with uWSGI, Nginx, and Docker

This Flask application is constructed using the Clean Architecture method. It is a synchronous application designed to be scalable and maintainable. Below is the folder architecture of the project:

## Folder Structure
flask_app/
|-- adapter/
|-- controller/
|-- entities/
|-- repositories/
|-- services/
|-- templates/
|-- app.py
|-- config.py
|-- Dockerfile
nginx/
|-- nginx.conf
docker-compose.yml


### Folder Descriptions

- **flask_app/adapter/**: Contains adapters to connect external frameworks and tools to the application.
- **flask_app/controller/**: Houses the controllers responsible for handling HTTP requests and responses.
- **flask_app/entities/**: Defines the core entities and domain models of the application.
- **flask_app/repositories/**: Implements repository interfaces to interact with data storage.
- **flask_app/services/**: Encapsulates business logic and use case implementations.
- **flask_app/templates/**: Contains HTML templates for the Flask application.
- **flask_app/app.py**: The main entry point of the Flask application.
- **flask_app/config.py**: Configuration settings for the Flask application.
- **flask_app/Dockerfile**: Defines the Docker image for the Flask application.

### Nginx Configuration

- **nginx/nginx.conf**: Configuration file for Nginx, acting as a reverse proxy for the Flask application.

### Docker Compose

- **docker-compose.yml**: Defines the services, networks, and volumes for Docker Compose to orchestrate the Flask and Nginx containers.




## Environment Variables

If any secret key file or other environment variables are required, they should be added in the Dockerfile or the Docker Compose file.

## Application Overview

### Welcome Page

When you land on the page, you will get a welcome page with a navigation button to the registration screen. When you click the button, it will take you to the registration screen.

### Registration Screen

On the registration screen, you will be asked to fill out the form for registration. You are required to fill in:
- Username
- Sex
- Favorite Programming Language
- Email

After you finish filling the form, click the register button, and your data will be stored in the database (a file-based SQLite3 database). A form successfully submitted message will be displayed. If you want to fill out the form again, you need to go back and fill it again.

### Form Validation

- **Username and email are unique**: You cannot enter a name or email that is already registered in the database.


# Flask Application with uWSGI, Nginx, and Docker

## Build the Docker Images

1. Navigate to the project root directory and run:

    ```sh
    docker-compose build
    ```

## Start the Services

Use Docker Compose to start the application:

```sh
docker-compose up
```

Open your web browser and navigate to http://localhost/ to access the Flask application through Nginx.