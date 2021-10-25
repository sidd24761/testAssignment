pipeline {
    agent any
    stages {
        stage('Compile') {
            steps {
                echo 'Python compile done'
            }
        }
        stage("Unit Test"){
            steps{
                sh "python test.py"
            }
        }
    }
}
