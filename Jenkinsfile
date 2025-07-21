pipeline {
    agent any

    tools {
        allure 'allure'
    }

    environment {
        ALLURE_RESULTS_DIR = 'allure-results'
        ALLURE_REPORT_DIR = 'allure-report'
        BROWSER = 'chrome'
        ENVIRONMENT = 'DEV'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r conf/requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh "python3 -m pytest --alluredir=${ALLURE_RESULTS_DIR}" --browser=${BROWSER}" --env=${ENVIRONMENT}" --headless=True
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: "${ALLURE_RESULTS_DIR}"]],
                    reportBuildPolicy: 'ALWAYS'
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: "${ALLURE_RESULTS_DIR}/**", allowEmptyArchive: true
        }
    }
}