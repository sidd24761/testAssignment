pipeline {
    agent any
    parameters {
        choice(name: 'VERSION', choices: ['1.1.0', '1.2.0', '1.3.0'], description: '')
        booleanParam(name: 'executeTests', defaultValue: true, description: '')
    }
    stages {
        stage("Compile") {
            steps {
                echo 'Python compile done'
            }
        }
        stage("Unit Test 2"){
            when {
                expression {
                    params.executeTests
                }
            }
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
