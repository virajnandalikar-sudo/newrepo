pipeline {
    agent any

    environment {
        SONARQUBE_ENV = 'MySonarQube' // Name configured in Jenkins
    }

    stages {
         HEAD
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
          ba98341164eccc41b9b1d49b9408c9a7aec24191
        stage('Serve UI') {
            steps {
                sh 'python3 app.py'
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

