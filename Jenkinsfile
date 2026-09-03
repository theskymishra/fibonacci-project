pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Fibonacci project'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Checking Fibonacci Python file'
                sh 'python3 --version'
                sh 'python3 -m py_compile fibonacci.py'
            }
        }

        stage('Run Fibonacci') {
            steps {
                echo 'Running Fibonacci program'
                sh 'python3 fibonacci.py'
            }
        }
    }
}