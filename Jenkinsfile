pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Fibonacci project'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                sh '/usr/local/bin/docker build -t fibonacci-app:${BUILD_NUMBER} .'
            }
        }

        stage('Run Fibonacci Container') {
            steps {
                echo 'Running Fibonacci application'
                sh '/usr/local/bin/docker run --rm fibonacci-app:${BUILD_NUMBER}'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker image'
            sh '/usr/local/bin/docker image rm fibonacci-app:${BUILD_NUMBER} || true'
        }
    }
}