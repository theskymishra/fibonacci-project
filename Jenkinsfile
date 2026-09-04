pipeline {
    agent {
        dockerfile true
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out Fibonacci project'
            }
        }

        stage('Build') {
            steps {
                echo 'Building Fibonacci application'
                sh 'python3 --version'
                sh 'python3 -m py_compile fibonacci.py'
            }
        }

        stage('Run Fibonacci') {
            steps {
                echo 'Running Fibonacci application'
                sh 'python3 fibonacci.py'
            }
        }
    }
}