pipeline {
    agent any

    environment {
        SONARQUBE_ENV = 'MySonarQube' // Name configured in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/virajnandalikar-sudo/newrepo.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv("${SONARQUBE_ENV}") {
                        sh '''
                            sonar-scanner \
                            -Dsonar.projectKey=newrepo \
                            -Dsonar.sources=. \
                            -Dsonar.host.url=http://your-sonarqube-server:9000 \
                            -Dsonar.login=$SONAR_AUTH_TOKEN
                        '''
                    }
                }
            }
        }

        stage('Serve UI') {
            steps {
                sh 'nohup python3 app.py > flask.log 2>&1 &'
                echo 'Flask UI is now available'
            }
        }

        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: 'flask.log', fingerprint: true
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}

