pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/virajnandalikar-sudo/newrepo.git'
            }
        }

        stage('Run Python') {
            steps {
                sh 'python3 p1.py'
            }
        }
    }
}

