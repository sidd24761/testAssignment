pipeline {
    agent any
    stages {
        stage("Compile") {
            steps {
                echo 'Python compile done'
            }
        }
        stage("Unit Test 2"){
            steps{
                sh "python test2.py"
            }
        }
        stage("Unit Test"){
            steps{
                sh "python test1.py"
            }
        }
        
    }
}
