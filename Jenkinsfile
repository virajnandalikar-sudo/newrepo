pipeline {
    agent any

    stages {
        /* stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/virajnandalikar-sudo/newrepo.git'
            }
        }

        stage('Install Dependencies') {
    steps {
        sh 'python3 -m venv venv'
        sh './venv/bin/pip install --upgrade pip'
        sh './venv/bin/pip install -r requirements.txt || echo "No requirements.txt found"'
    }
}


       stage('Run Tests') {
    steps {
        script {
            if (fileExists('tests')) {
                sh './venv/bin/python -m unittest discover tests'
            } else {
                echo "No tests directory found, skipping..."
            }
        }
    }
}


        stage('Run Web Application') {
    steps {
        sh 'nohup ./venv/bin/python app.py > app.log 2>&1 &'
        echo "App started — check http://<your-server-ip>:5000"
    }
} */
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



