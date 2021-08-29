# Labs 1-2

## Best practices for writing a Dockerfile

1. Use the smallest base image.

As a base image I used *python:3.9-slim*. 

2. Use multi-stage builds.

To leverage build cache, I firstly copied app's requirements add then other app's files.  

3. Avoid the use of ADD, use COPY instead.

4. Avoid building unnecessary files into images

So, I wrote a *.dockerignore* file which includes: *Dockerfile*, *PYTHON.md*, *DOCKER.md*, and *venv/*.

6. Use a docker-compose.yml file

To ease the process of running and testing the container, I created a *docker-compose.yml* file which includes exposure of ports to establish a connection between the local machine and the container.

# Labs 3-4