pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/ganesha1709/sample-CI.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install any dependencies listed in requirements.txt
                bat 'C:\\path\\to\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                // Run the Python script
                bat 'C:\\path\\to\\python.exe average_calculator.py'
            }
        }
    }
}
