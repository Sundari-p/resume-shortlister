pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Sundari-p/resume-shortlister.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t resume-shortlister .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run resume-shortlister pytest tests/'
            }
        }

        stage('Deploy Container') {
            steps {
                bat 'docker run -d -p 5000:5000 resume-shortlister'
            }
        }
    }
}
