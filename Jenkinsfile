pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                checkout scm
            }
        }

        stage('Run Python application') {
            steps {
                bat 'python --version'
                bat 'python hello.py'
            }
        }

        stage('Install dependencies and test') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker image') {
            steps {
                bat 'docker build -t mlops-hello .'
            }
        }
    }
}
