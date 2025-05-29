pipeline {
    agent any
    environment {
        IMAGE_NAME = "msa-product-app"
    }
    stages {
        stage('Clone') {
            steps {
                git url: 'git@github.com:moveho/jpub-myrepo.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker compose -f docker-compose.yml build'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'docker compose -f docker-compose.yml up -d'
                }
            }
        }
    }
}

