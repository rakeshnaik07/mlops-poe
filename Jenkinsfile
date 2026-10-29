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

        stage('Install dependencies and test') {
            steps {
                bat 'python --version'
                bat 'python -m pip install --upgrade -r requirements.txt'
                bat 'python -m pip check'
                bat 'python -m pytest -v'
            }
        }

        stage('Run Python application') {
            steps {
                bat 'python hello.py'
            }
        }

        stage('Build Docker image') {
            steps {
                bat 'docker build -t mlops-hello .'
            }
        }
        stage('Evidently monitoring') {
            steps {
                bat 'python monitor.py'
                    archiveArtifacts artifacts: 'drift_report.html',
                         fingerprint: true
    }
}
    }
}
