pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/2025sl93065-hash/bits-ls1-2025sl93065.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo "Build Stage"'
                sh 'ls'
            }
        }

        stage('Test') {
            steps {
                sh '''
                python3 - <<EOF
import calculator

assert calculator.add(2,3) == 5
assert calculator.multiply(2,3) == 6
assert calculator.divide(6,3) == 2

print("All tests passed")
EOF
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo "Deploy stage"'
            }
        }
    }
}
