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
                sh 'docker build -t resume-shortlister .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run resume-shortlister pytest tests/'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 5000:5000 resume-shortlister'
            }
        }
    }
}
