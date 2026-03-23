pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout([$class: 'GitSCM',
                          branches: [[name: '*/main']],
                          userRemoteConfigs: [[url: 'https://github.com/virajnandalikar-sudo/newrepo.git']]
                ])
            }
        }

        stage('Build') {
            steps {
                echo 'Building project...'
                sh 'echo "Simulating build process"'
            }
        }

        stage('Lint') {
            steps {
                echo 'Running lint checks...'
                sh 'echo "Simulating linting process"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "Simulating test execution"'
            }
        }

        stage('Run Python Script') {
            steps {
                echo 'Executing Python file...'
                sh 'python3 script.py'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'echo "Simulating deployment"'
            }
        }

        stage('Notify') {
            steps {
                echo 'Sending out notification message...'
                echo 'Pipeline completed successfully!'
            }
        }
    }
}


