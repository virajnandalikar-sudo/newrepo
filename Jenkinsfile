pipeline {
    agent any

    stages {
        stage('Serve UI') {
            steps {
                //sh 'python3 app.py'
                //echo 'Flask UI is now available'
                    sh 'nohup python3 app.py > flask.log 2>&1 &'
        // Give Flask a few seconds to start
        sh 'sleep 5'
        // Check if the server responds
        sh 'curl -f http://localhost:5000 || echo "Flask not responding"'
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



