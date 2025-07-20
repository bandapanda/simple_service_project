pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-pat', url: 'https://github.com/bandapanda/simple_service_project.git'
            }
        }

        stage('Build') {
            steps {
                sh 'make build VERSION=${VERSION}'
            }
        }

        stage('Run') {
            steps {
                sh 'make run-hello VERSION=${VERSION}'
            }
        }
    }
}