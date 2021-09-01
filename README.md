# MosTime

Table of contents

1. [About the Project](#about)
    1. [Built With](#built-with)
2. [Getting Started](#getting-started)
    1. [Prerequisites](#prerequisites)
    2. [Installation](#installation)
3. [Usage](#usage)
4. [Testing](#testing)
    1. [Unit tests](#unit-tests)
5. [Workflows](#workflows)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)
9. [Acknowledgements](#acknowledgements)

## About the Project <a name="about"></a>

MosTime is a python web-application allowing you to get current time in Moscow any time you want. Precision of the time is in seconds! The interface is as simple and intuitive as possible! Refresh of the web-page refreshes the time, too!

### Built with <a name="built-with"></a>

- Python (Flask framework)
- HTML
- Markdown

## Getting Started <a name="getting-started"></a>

In order to run the app locally, follow the next steps.

### Prerequisites <a name="prerequisites"></a>

First of all, you need to

### Installation <a name="installation"></a>

1. Clone the repository with the project:

```bash
git clone https://github.com/SmirnovaMarina/devops.git
```

2. Set up a virtual environment by navigating to the project folder (app_python) on your terminal and typing the command:

```bash
python3 -m venv venv
```

Then, activate the virtual environment with the activation script:

```bash
source venv/bin/activate
```

3. Install packages required for the app to run appropriately:

```bash
python3 -m pip install -r requirements.txt
```

## Usage <a name="usage"></a>

You can run the app in two ways: using terminal or Docker.

For the first variant, proceed with the command in the terminal:

```bash
python3 main.py
```

Open a browser tab at http://127.0.0.1:5000/. Congratulations! You can see a page displaying Moscow's time.

For the second variant, you will need to pull the app's image from the Docker Hub.

```bash
docker pull marinasmirnova/devops:app-python-1
```

```bash
docker run -p 5000:5000 app-python-1
```

Voi la!

## Testing <a name="testing"></a>

### Unit tests <a name="unit-tests"></a>

To test the application, I wrote unit tests with Pytest framework. To look through them, go to the *tests* directory inside *app_python*. To read about best testing practices open file *PYTHON.md*.

To run a specific test with *test_\<function-name>.py*, execute the following command:

```bash
pytest tests/test_<function-name>.py
```

To run all tests, execute the following command:

```bash
pytest tests/
```

## Workflows <a name="workflows"></a>

[![Pylint](https://github.com/SmirnovaMarina/devops/actions/workflows/pylint.yml/badge.svg?branch=develop&event=push)](https://github.com/SmirnovaMarina/devops/actions/workflows/pylint.yml)

[![Python application](https://github.com/SmirnovaMarina/devops/actions/workflows/test-app.yml/badge.svg?branch=develop&event=push)](https://github.com/SmirnovaMarina/devops/actions/workflows/test-app.yml)

[![CI to Docker Hub](https://github.com/SmirnovaMarina/devops/actions/workflows/build-push-dockerhub.yml/badge.svg?branch=main&event=push)](https://github.com/SmirnovaMarina/devops/actions/workflows/build-push-dockerhub.yml)

## Contributing <a name="contributing"></a>

Contributions are welcome! Teamwork and collaboration boost development of ideas and accelerate improvement of projects. If you would like to contribute to the project, follow the steps:

1. Fork the Project
2. Create a separate branch for your feature (```git checkout -b feature/YourFeature```)
3. Commit your Changes (```git commit -m 'Added some feature'```)
4. Push to the Branch (```git push origin feature/YourFeature```)
5. Open a Pull Request

For major modifications, open an issue to discuss what you want to change.

## License <a name="license"></a>

Distributed under the [MIT license](https://choosealicense.com/licenses/mit/).

## Contact <a name="contact"></a>

Marina Smirnova – m.smirnova@innopolis.university

Project link – [https://github.com/SmirnovaMarina/devops](https://github.com/SmirnovaMarina/devops)

## Acknowledgements <a name="acknowledgements"></a>

Inspiration, used materials, code snippets, etc.

- [Best practices for writing python web-application](https://data-flair.training/blogs/python-best-practices/)
- [Best practices for writing Dockerfile](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Template for the README.md](https://github.com/othneildrew/Best-README-Template/blob/master/BLANK_README.md)
- [Online linter for Markdown](https://dlaa.me/markdownlint/)
- [Linter for python](https://flake8.pycqa.org/en/latest/)
- [Choosing best testing Python framework](https://www.pythonpool.com/python-unittest-vs-pytest/)
- [Basics of unit testing in Python](https://medium.com/swlh/unit-testing-in-python-code-confidently-and-break-stuff-on-purpose-d246e7167e79)
- [Best practices for writing unit tests in Python](https://www.testim.io/blog/unit-testing-best-practices/)
