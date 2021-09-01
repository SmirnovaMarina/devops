pipeline {
  agent any
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Setup') { // Install any dependencies you need to perform testing
      agent {docker { image 'python:3.9-slim' }}
      steps {
        script {
          sh """
          pip install -r app_python/requirements.txt
          flake8 app_python/
          pytest app_python/tests/
          """
        }
      }
    }
    stage('Building and Pushing') { // Build docker image and push it to DockerHub
      steps {
        script {
          sh """
          docker build -t marinasmirnova/devops:latest app_python/
	        docker push marinasmirnova/devops:latest
          """
        }
      }
    }
  }
  post {
    cleanup { cleanWs() }
  }
}