# Deploy a Python (Django) app to Azure to Azure Containers Apps

This Python app is a simple restaurant review application built with the [Flask](https://flask.palletsprojects.com/en/2.1.x/) framework. The app uses stores application data in PostgreSQL with environment variables defining the connection info.

Here are some scenarios for using this repo:

* You can run the web app locally in a virtual environment. Make sure to define *.env* file with environment settings.

* You can create a container locally and run it in Docker. For this scenario, set REMOTE_POSTGRESQL=1 in *.env* file and use the command: `docker run -it --env-file .env --publish 8000:8000/tcp pythoncontainer:latest` set environment variables for container. See the *.env.example* file for details.

  If you want to use PostgreSQL instance locally, you add `--add-host` to the Docker command. For more information, see the [Docker run](https://docs.docker.com/engine/reference/commandline/run/) command. For an example of how to do this with MongoDB, see [Build and test a containerized Python web app locally](https://docs.microsoft.com/azure/developer/python/tutorial-containerize-deploy-python-web-app-azure-02).

* Deploy the code to App Service. For guidance on how to deploy code, see [Quickstart: Deploy a Python (Django or Flask) web app to Azure App Service](https://docs.microsoft.com/azure/app-service/quickstart-python) and [Overview: Deploy a Python web app to Azure with managed identity](https://docs.microsoft.com/azure/developer/python/tutorial-python-managed-identity-01).

* Create a container from this repo and deploy to Web Apps for Containers (App Service). See [Overview: Containerized Python web app on Azure](https://docs.microsoft.com/azure/developer/python/tutorial-containerize-deploy-python-web-app-azure-01).

* Create a container from this repo and deploy to [Azure Container Apps](https://azure.microsoft.com/services/container-apps/). **This repo is targeting this scenario.** **TBD**

If you need an Azure account, you can [create on for free](https://azure.microsoft.com/free/).

A Django sample application with similar functionality is at **TBD**.

## Requirements

The [requirements.txt](./requirements.txt) has the following packages:

| Package | Description |
| ------- | ----------- |
| [Flask](https://pypi.org/project/Flask/) | Web application framework. |
| [SQLAlchemy](https://pypi.org/project/SQLAlchemy/) | Provides a database abstraction layer to communicate with PostgreSQL. |
| [Flask-SQLAlchemy](https://pypi.org/project/Flask-SQLAlchemy/) | Adds SQLAlchemy support to Flask application by simplifying using SQLAlchemy. Requires SQLAlchemy. |
| [Flask-Migrate](https://pypi.org/project/Flask-Migrate/) | SQLAlchemy database migrations for Flask applications using Alembic. Allows functionality parity with Django version of this sample app.|
| [pyscopg2-binary](https://pypi.org/project/psycopg2/) | PostgreSQL database adapter for Python. |
| [gunicorn](https://pypi.org/project/gunicorn/) | WSGI HTTP Server for UNIX. Required for running containers in [VS Code](https://code.visualstudio.com/docs/containers/quickstart-python#_gunicorn-modifications-for-djangoflask-apps) and required for deployment in Azure Containers Apps. |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from .env file and set them as environment variables. In this sample app, environment variables describe how to connect to the database and storage resources. Because managed identity is used no sensitive information is included in environment variables. <br><br> Flask's [dotenv support](https://flask.palletsprojects.com/en/2.1.x/cli/#environment-variables-from-dotenv) sets environment variables automatically from an `.env` file. |
| [flask_wtf](https://pypi.org/project/Flask-WTF/) | Form rendering, validation, and CSRF protection for Flask with WTForms. Uses CSRFProtect extension. |

The steps to do this are covered more completely in the **TBD** tutorial. Briefly, here are the steps:

1. Fork and then clone locally.
1. Build a container image from the repo.
1. Create a PostgreSQL Flexible Server instance.
1. Create a database on the server.
1. Deploy the web app container to Container Apps.