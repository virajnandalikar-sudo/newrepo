pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/virajnandalikar-sudo/newrepo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './venv/bin/python -m unittest discover tests'
            }
        }

        stage('Run Web Application') {
            steps {
                sh './venv/bin/python app.py &'
                echo "App started — visit http://localhost:5000"
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}



