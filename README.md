# Todo List API

Backend of a React Application build using Django, and django-restframework.

## About Project

Manages CRUD operation interactions with frontend app and manages a SQLite3 database that is used to store the tasks of user.
The tasks have 4 properties title, context and completed and recurring with are self explanatory. The context property is based on the principles of "Getting Things Done" book by David Allen.

## Getting Started

A working installation of `Python` and `Git` verison control system is enough to start the project.
Instructions for Python installation can be found [here](https://www.youtube.com/watch?v=4bUOrMj88Pc).
Instructions for Git installation can be found [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
Install and a virtual environment handles like [`venv`](https://docs.python.org/3/library/venv.html) or [`virtualenv`](https://virtualenv.pypa.io/en/latest/) .
Create and new directory and `cd` into it.

### Installation

This is build on the **Django** and **Django-rest-framework** python packages and a few others are necessary.

1. Clone the project from GitHub

```
git clone https://github.com/abhayhk2001/Django-Todo.git
```

2. Move into the created directory and start the native terminal in this directory. Create a virtual environment using preffered method. (here I have used venv), and activate the environment.

```
$ python -m venv env
$ env/Scripts/activate
```

3. Install the required python packages for the project by runnign the following command.

```
$ pip install -r requirements.txt
```

4. Start the Django API server with the following command.

```
$ cd todo
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/Ne wFeature`)
3.  Commit your Changes (`git commit -m 'Add some NewFeature'`)
4.  Push to the Branch (`git push origin feature/NewFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Abhay H Kashyap - [@twitter_handle](https://twitter.com/AbhayHKashyap1)

Project Link: [https://github.com/abhayhk2001/Django-Todo](https://github.com/abhayhk2001/Django-Todo)
