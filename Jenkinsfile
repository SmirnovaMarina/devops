pipeline {
  agent {
    // Run this job within a Docker container built using Dockerfile.build
    // contained within your projects repository. This image should include
    // the core runtimes and dependencies required to run the job,
    // for example Python 3.x and NPM.
    dockerfile { filename 'Dockerfile' }
  }
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          pip install -r app_python/requirements.txt
          """
        }
      }
    }
    stage('Linting') { // Run pylint against your code
      steps {
        script {
          sh """
          flake8 app_python/ 
          """
        }
      }
    }
    stage('Unit Testing') { // Perform unit testing
      steps {
        script {
          sh """
          pytest app_python/tests/
          """
        }
      }
    }
    stage('Building and Pushing') { // Build docker image and push it to DockerHub
      steps {
        script {
          sh """
          docker build -t marinasmirnova/devops:latest .
	  docker push marinasmirnova/devops:latest
          """
        }
      }
    }
  }
}