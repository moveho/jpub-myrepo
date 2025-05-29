pipeline {
    agent any
    environment {
        IMAGE_NAME = "msa-product-app"
        COMPOSE_FILE = "/home/kevin/LABs/ch03/3.2.6/docker-compose.yml"
    }
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'git@github.com:moveho/jpub-myrepo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker compose -f ${COMPOSE_FILE} build"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker compose -f ${COMPOSE_FILE} up -d"
                }
            }
        }
    }
}

