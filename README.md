# Blog API Documentation

Welcome to the Blog API, a simple RESTful API designed to create, update, delete, and fetch blog posts. This project serves as a test of backend architecture, database management, and API development using Django and Django REST Framework (DRF). Follow the instructions below to set up and interact with the API.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup & Installation](#setup--installation)
   - [Requirements](#requirements)
   - [Installation](#installation)
3. [Database Design](#database-design)
4. [API Endpoints](#api-endpoints)
   - [Fetch All Blog Posts](#fetch-all-blog-posts)
   - [Create a New Blog Post](#create-a-new-blog-post)
   - [Update an Existing Blog Post](#update-an-existing-blog-post)
   - [Delete a Blog Post](#delete-a-blog-post)
5. [Testing the API](#testing-the-api)
6. [Running Migrations](#running-migrations)
7. [Running the Server](#running-the-server)
8. [Technologies Used](#technologies-used)
9. [Contributing](#contributing)


## Project Overview
This project demonstrates the development of a simple blog API using Django. The API adheres to REST principles, with well-defined routes, proper HTTP methods, and standard error handling mechanisms.

The core features include:

- Creating, updating, and deleting blog posts
- Fetching individual or all blog posts
- Error handling for invalid data and bad requests


## Setup & Installation

### Requirements

- Python 3.x
- Django 4.x (or latest version)
- Django REST Framework (DRF)


### Installation
1. Clone the repository:
``` bash
git clone https://github.com/jamesunekwuojo/rexversityBlogapi.git
cd api cd Blog
```

2. Install the dependencies:
Create a new virtual env (optional)
Then install the dependencies using `requirements.txt`  file

```bash
pip install -r requirements.txt
```

3. Start a new Django project (if not done already):

```bash
django-admin startproject Blog
cd Blog
```

4. Create the blog app:

```bash
python manage.py startapp blogApi
```

5. Connect the app to the Django project:
In the settings.py file of the Blog project, add blogApi to the INSTALLED_APPS list:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'blogApi',
]
```

## Database Design
The blog application uses Django's ORM to handle database operations. Below is the sample model schema for the BlogPost model:

```python
from django.db import models

# Create your models here.
class BlogPost(models.Model):  # This gets all of the basic functionality of a database model
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True) # Don't need to manually set the time. it's going to automatically fill in the publishhed data.

    def __str__(self) : 
        return self.title
```
Make sure to run the migrations whenever changes are made to the models.


## API Endpoints
### Base URL

```plaintext
http://127.0.0.1:8000/api/blogposts/
```

### Fetch All Blog Posts
- `Endpoint:` /api/blogposts/
- `Method:` GET
- `Description:` Fetches all blog posts in the database.

```plaintext
GET http://127.0.0.1:8000/api/blogposts/
```
### Create a New Blog Post
- `Endpoint:` /api/blogposts/create/
- `Method:` POST
- `Description:` Creates a new blog post.
  
```plaintext
POST http://127.0.0.1:8000/api/blogposts/create/
```

`Request body:`
```json
{
    "title": "My First Blog",
    "content": "This is my first blog post."
}
```

### Update an Existing Blog Post
- `Endpoint:` `/api/blogposts/<id>/`
- `Method: PUT`
- `Description:` Updates the details of an existing blog post by its ID.

```plaintext
PUT http://127.0.0.1:8000/api/blogposts/3/
```

### Delete a Blog Post
- `Endpoint:` `/api/blogposts/<id>/`
- `Method:` DELETE
- `Description:` Deletes a blog post by its ID.

```plaintext
DELETE `http://127.0.0.1:8000/api/blogposts/3/`
```


## Testing the API
You can test the API using tools like [Postman](https://www.postman.com/) or [curl](https://curl.se/).

Example curl command for fetching blog posts:
``` bash
curl -X GET http://127.0.0.1:8000/api/blogposts/
```

## Running Migrations
Whenever changes are made to your models, you need to apply migrations to update the database schema.
1. `Create migrations:`

```bash
python manage.py makemigrations
```

2. `Apply migrations:`

```bash
python manage.py migrate
```

## Running the Server
To start the development server, run the following command:

```bash
python manage.py runserver
```
The API will be accessible at:
```plaintext
http://127.0.0.1:8000/
```


## Technologies Used
- `Django:` For creating the project and managing the application.
- `Django REST Framework (DRF):` To create the RESTful API.
- `SQLite (default):` For database management (it can change to PostgreSQL/MySQL as needed).

## Contributing
I welcome contributions to improve this project! If you want to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/feature-name`).
3. Commit your changes (`git commit -m "Add new feature" `).
4. Push the branch (`git push origin feature/feature-name`).
5. Open a pull request.


