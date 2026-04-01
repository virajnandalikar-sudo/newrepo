pipeline {
    agent any

    environment {
        SONARQUBE = 'MySonarQube'  // Must match the name of your SonarQube server configured in Jenkins (Manage Jenkins → Configure System)
    }

    stages {
        stage('Checkout') {
            steps {
                // Clone your repository
                git branch: 'main', url: 'https://github.com/virajnandalikar-sudo/newrepo.git'
            }
        }

        stage('Build') {
            steps {
                // Run Python file to verify execution
                sh 'python3 p1.py'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv("${SONARQUBE}") {
                        // Use the scanner tool configured in Jenkins Global Tool Configuration
			 withCredentials([string(credentialsId: 'SONAR_AUTH_TOKEN', variable: 'SONAR_AUTH_TOKEN')]) {
                        sh """
			    ${tool 'SonarQubeScanner'}/bin/sonar-scanner \
                            -Dsonar.projectKey=newrepo \
                            -Dsonar.projectName=newrepo \
                            -Dsonar.sources=. \
                            -Dsonar.python.version=3 \
		            -Dsonar.login=$SONAR_AUTH_TOKEN
			"""
                    }
                }
            }
        }
}
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Build and analysis completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}

