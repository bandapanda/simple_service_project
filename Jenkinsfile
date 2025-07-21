pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                git url: 'git@github.com:bandapanda/simple_service_project.git', credentialsId: 'jenkins-git'
            }
        }
    }
}