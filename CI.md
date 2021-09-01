# Labs 3-4

## Best practices for Continuous Integration and Continuous Development

1. Stay secure.

That's why it's recommended to use a Docker Hub access token rather than a password.

2. Reduce the build time.

By using the build cache (buildX) one can reuse layers already pulled and shorten the build time.

3. Push only release version of images to DockerHub.

I created a separate branch called *develop* to make commits there while developing. So, linting and testing workflows are configured to listen to both branches, building workflow listens to pushes to the main branch only.

## Best practices for Jetkins

1. Stay secure.

I created credentials in my Jetkins profile instead of just writing them in the Jetkinsfile. 

2. Make more atomic steps to ensure failures are detected as soon as possible.

3. Perform cleanup operations to avoid overloading the disk.

4. Name projects with a sane (e.g. alphanumeric) character set.

## Difference between GitHub Actions and Jenkins noticed while writing configurations:

1. Jenkins server needs installation. GitHub Actions are in the cloud.

2. Jenkins centers on builds (Java) and requires plugins for other CI/CD functionalities.