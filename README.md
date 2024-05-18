# Developers Diary - a blog about my journy in Python and Linux

Blogentries related to Linux and Python

Resources:

[Blueprint](https://mayadevbe.me/page/2/)
[Deployment](https://realpython.com/django-nginx-gunicorn/)

Features:

The blog will have

- Landing page
- Blogentries
- Imprint    
- PrivacyPolicy
- Social Media
- About
- Link to all posts
- Search functionality
- Nice Error 404 Not found page

Navbar will have links to
- Home
- All posts 
- Topics
- About

base.html wil include:

title
abstract
navbar 
{{}}
footer 

Blog entries will have
- title
- published date
- body
- Related content


In Pipeline:
    Setup a basic Django project
        - Create and activate virtual environment
        - install django
        - startproject my_first_django_project
        - startapp hello_world
        - register app in settings.py
        - create route in f_d_p/urls.py
        - create route in hello_world.py
        - create view
        - create templates/hello_world/index.html
        - runserver
    Build a barebone blog
    Software Verification
    Setup Pentesting Lab
        Kali Linux
        Metasploitable
    Setup Deployment Lab
    Setup Server on Digital Ocean
    Secure Server
        secure root account
        ssh
    Deploy Django
        [Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
        Development Settings
        Production Settings
        Setup Gunicorn
        Setup Nginx
        Setup HTTP
        Setup HTTPS
    Secure Webapplication
    Networking 101 - IPv4 addresses
    Overthewire Walkthroughs
    

