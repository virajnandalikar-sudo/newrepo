pipeline {
    agent any

    stages {
        stage('Serve UI') {
            steps {
                sh 'python3 app.py'
                echo 'Flask UI is now available'
            }}
        stage('Archive Logs') {
            steps {
                archiveArtifacts artifacts: 'flask.log', fingerprint: true
            }}

    }

    post {
        always {
            echo 'Pipeline finished!'
        }
    }
}



