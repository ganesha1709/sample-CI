pipeline {
    agent any

    stages {
        stage('init repo') {
            steps {
               git url:'https://github.com/ganesha1709/sample-CI.git',branch:'main'
        
            }
        }

        stage('Run Python Script') {
            steps {
                // Run the Python script with the correct path
                bat 'C:\\Users\\rsrin\\AppData\\Local\\Programs\\Python\\Launcher\\py.exe  average_calculator.py'
            }
        }
    }
}
