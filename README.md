# Demo App Using Django

This is a demo project using Django that predicts customer type based on income and score using a machine learning model.

## Table of Contents

- [Demo App Using Django](#demo-app-using-django)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
  - [Model](#model)
  - [Endpoints](#endpoints)
  - [Contributing](#contributing)

## Project Overview

This project is a web application built with Django. The main objective is to predict customer types based on income and score using a machine learning model.

## Installation

### Prerequisites

- Python 3.6 or newer
- pip
- virtualenv (recommended)

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SushilKumar045/Demo_App_Using_Django.git
   cd Demo_App_Using_Django
   cd Django_project
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv myenv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```bash
     myenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source myenv/bin/activate
     ```

4. **Install dependencies:**

   ```bash
   pip install django
   pip install sciket-learn
   pip install sklearn
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6.  **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the application:**

   Open your web browser and navigate to `http://127.0.0.1:8000/`.

2. **Admin Interface:**

   To access the Django admin interface, navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you created.

## Project Structure

```
Demo_App_Using_Django/
├── Django_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
├── Django_project_App/
│   ├── migrations
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── ...
├── templates
│   └──index.html 
├── db.sqlite3
├── Demo_App_Django.pkl
├── manage.py
└──
```

## Model

The machine learning model used for prediction is a pre-trained model saved as `Demo_App_Django.pkl`. Ensure this file is present in the root directory of the project.

## Endpoints

- `/`: The home page.
- `/predict/`: Endpoint for making predictions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

```
