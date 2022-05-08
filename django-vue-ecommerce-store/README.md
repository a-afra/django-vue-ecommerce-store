<h1 align="center">Django + Vue E-Commerce Store</h1>
<hr>

![](readme_assets\1.png)

<h2 align="center"><a  href="https://boutique-django.herokuapp.com/">Live Demo</a></h2>
**tip:** because of the heroku server, if the website doesn't show up, **change your IP address.**
<hr>

## Description
<hr>

<p align="center">
<img src="readme_assets\2.gif" alt="Demo gif">
</p>
Hi everyone!

Boutique is an online clothing store that you can register to it, view products and buy.
The purpose of this project for me, was to test my Django and Web Development skills.
I use django for the backend and Django Rest Framework for the APIs.
Authentication system is handled by Djoser.

For the frontend and vue.js part I used the help of 
<a href="https://www.youtube.com/c/CodeWithStein">codeWithStein</a> tutorials.
This project has a responsive design too!
<p align="center">
<img width="200" src="readme_assets\3.gif" alt="Demo gif">
</p>

The live demo of this project was deployed on heroku server.

## About the project
<hr>

Let's get into some details. a user can:

* Signup and Login
* View account information
* Search products
* View product in details
* Order products
* View cart
* And more

There are two categories to choose products from. Men and Women.

## Getting started
<hr>

### Dependencies
First, make sure you have `python3` and `node.js` installed.

Create a virtual environment and activate it:
```bash
python -m venv [directory]
[directory]\Scripts\activate.bat
```
Install dependencies:
```bash
pip install -r requirements.txt
```

### Start the project

Open a terminal:
```bash
python manage.py runserver
```
The server should be up at `http://localhost:8000`

Navigate to `django_ecommerce_vue` directory. open a terminal:
```bash
npm run serve
```
Now you can interact with the site at `http://localhost:8080`
