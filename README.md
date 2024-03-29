
# Python Flask Application Setup Guide

This guide provides instructions for setting up and running a simple Python Flask application. It covers the installation of Python, setting up a virtual environment, installing Flask, and running the application.

## Installing Python

### Windows

1. Download the Python installer from the [official Python website](https://www.python.org/downloads/windows/).
2. Run the installer and make sure to check the box that says "Add Python X.X to PATH" to ensure that the interpreter will be placed in your execution path.
3. Follow the rest of the installation prompts, choosing the default settings for the most part.

### macOS

1. The easiest way to install Python on macOS is via the [Homebrew](https://brew.sh/) package manager. If you have Homebrew installed, simply run:

```bash
brew install python
```

2. This will install Python and pip (Python's package installer).

### Linux (Ubuntu/Debian)

1. Python is usually pre-installed on many Linux distributions. To check if Python is installed, and which version, open a terminal and run:

```bash
python3 --version
```

2. If you need to install Python, run:

```bash
sudo apt update
sudo apt install python3
sudo apt install python3-pip
```

## Setting Up the Flask Application

### Setting Up a Virtual Environment

Before installing Flask and running the application, it's recommended to create a virtual environment. This will keep your project dependencies separate from your system's Python environment.

1. Navigate to your project directory:

```bash
cd /path/to/your/project
```

2. Create a virtual environment in the project directory:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

- On Windows, run:

```cmd
venv\Scripts\activate
```

- On macOS and Linux, run:

```bash
source venv/bin/activate
```

### Installing Flask

With your virtual environment activated, you can install Flask using `pip`:

```bash
pip install Flask
```

If your project has a `requirements.txt` file that lists all of its dependencies, you can install all required packages by running:

```bash
pip install -r requirements.txt
```

### Running the Flask Application

1. Ensure you are still in the project's root directory and your virtual environment is activated.

2. Set the Flask application to run:

```bash
export FLASK_APP=app.py
```

3. (Optional) If you want Flask to reload automatically when you make changes to the code, set the environment variable:

```bash
export FLASK_ENV=development
```

4. Start the Flask application:

```bash
flask run
```

This command will start a local server. By default, Flask applications run on port 5000.

5. Open your web browser and navigate to `http://localhost:5000` to view your application.
