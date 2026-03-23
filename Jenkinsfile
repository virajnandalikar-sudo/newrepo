pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the project...'
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

        stage('Package') {
            steps {
                echo 'Packaging artifacts...'
                sh 'echo "Simulating packaging step"'
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
                // Example: Slack notification (requires Slack plugin configured)
                // slackSend(channel: '#builds', message: "Build pipeline completed successfully!")
                
                // For simplicity, just echoing a message here
                echo 'Build pipeline completed successfully!'
            }
        }
    }
}


