# Labs 1-2

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

# Labs 3-4

### Best practices for writing unit tests in Python

1. Use *pytest* testing framework.

I prefered *pytest* to *unittest* since this framework is easier to use than a former one. Testing with *pytest* is faster , and you produce more compact pieces of code.

2. Write tests in a separate file from the code itself.

That's why there are test files to test creation of application itself, correctness of shown time, completeness of the shown sentence's template ("The current time in Moscow is: %H:%M:%S").

3. One of the appropriate naming conventions is to call test files *test_\<module_or_function_name>.py*.

4. Not only test favourable outcomes, but also write tests that might break the behaviour of the program.

It increases test coverage of your program.

4. Using *pytest*, create fixtures.

To reduce amount of boilerplate code and simplify the process of writing and running tests.

5. Tests should be simple and fast.

For such a simple application as mine, *pytest* provide the best variant: just define the functions and assert the conditions inside them (no need to import modules and create test classes).  

6. Tests should not be duplicates of the implementation logic.

I realised that I violated this practice while testing the function for showing time. That's why I removed the code generating time from the test, and just added a regular expression to check the format of the time.    