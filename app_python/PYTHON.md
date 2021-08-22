# Lab 1

## Best practices for writing a Python web application

1. Implement version control.

To monitor the status of the project, be able to work collaboratively and have access to the project not only locally, I used Git Version Control System.

2. Create understandable documentation.

To let others understand the purpose and the implementation of the project, I wrote documenting files: README.md with common information about the project, PYTHON.md with information about best practices for coding in python, DOCKER.md with information about best practices for writing a Dockerfile.

3. Use linter for code formatting.

Clean code promotes readability, reusability and maintainability, that's why I used a [linter](https://flake8.pycqa.org/en/latest/) to align my app with code conventions.

4. Use virtual environments.

To avoid library clashes (different projects may need different libraries or versions), it is recommended to create a virtual environment for each project. So, I used venv.

5. Import only necessary functions from packages.

To avoid overloading of unnecessary data and library clashes, it is recommended to import only functions used in the project, not the whole packages.  

6. Use production ready framework.

I chose Flask framework.