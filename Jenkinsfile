pipeline {
    agent any

    parameters {
        choice(name: 'MODE', choices: ['hello', 'random'], description: 'Choose mode')
        string(name: 'VERSION', defaultValue: '1.0.0', description: 'Docker image version tag')
    }

    environment {
        IMAGE_NAME = 'simple_service_client'
    }



    stages {

        stage('Clone repo') {
            steps {
                git url: 'git@github.com:bandapanda/simple_service_project.git',
                credentialsId: 'jenkins-git',
                branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('simple_service_project') {
                    echo "IMAGE_NAME: ${IMAGE_NAME}"
                    echo "VERSION: ${VERSION}"
                    sh 'make build VERSION=${VERSION}'
                }
            }
        }

        stage('Run Client') {
            steps {
                dir('simple_service_project') {
                    script {
                        if (params.MODE == 'hello') {
                            sh 'make run-hello VERSION=${VERSION}'
                        } else {
                            sh 'make run-random VERSION=${VERSION}'
                        }
                    }
                }
            }
        }
    }

}