# hector
Python package for general execution use

# Setup Python virtual environment && Activate virtual environment
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 freeze > requirements.txt


# Run your application with Typer Client
$ typer cli/main.py run

# You get a --help
$ typer cli/main.py run --help

# Output Colors & Layouts
$ python3 -m rich.markup