def FAILED_STAGE

pipeline {
    agent {
        node {
            label 'linux-1'
        }
    }
    environment {
        ENV_VERSION = '1.0.2'
        WEBHOOK_URL = ''
        USERID= '-'
        SERVICE_NAME= 'sample-service'
    }

    stages {
        stage('test') {
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'node -v'
                sh 'npm -v'
                sh "echo ${BRANCH_NAME}"

            }
        }
        }

        stage('run sonarque test') {
            when {
            	branch 'demo'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'sonar-scanner'
            }
        }
        }


        stage('unit test  ') {
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'sleep 1'
                //junit 'src/test/**/*.xml'
            }
        }
        }


        stage('build & push image branch master') {
            when {
            	branch 'master'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'docker build -t  sample-prod:1.0.${BUILD_NUMBER} .'
                sh 'docker push  sample-prod:1.0.${BUILD_NUMBER} '

             }
        }
        }

        stage('build & push image branch demo') {
            when {
            	branch 'demo'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'docker build -t  sample-prod-${BRANCH_NAME}:1.0.${BUILD_NUMBER} .'
                sh 'docker push  sample-prod-${BRANCH_NAME}:1.0.${BUILD_NUMBER} '

        }
            }
        }

        stage('build & push image branch develop') {
            when {
            	branch 'develop'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'docker build -t  sample-prod-${BRANCH_NAME}:1.0.${BUILD_NUMBER} .'
                sh 'docker push  sample-prod-${BRANCH_NAME}:1.0.${BUILD_NUMBER}'

        }
            }
        }

        stage('Deployment  sample-prod branch master') {
            when {
            	branch 'master'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh "sleep 1"
            }
            }
            }

        stage('Deployment  sample-prod branch demo') {
            when {
            	branch 'demo'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh "kubectl --kubeconfig ~/.kubeconfig/kubeconfig.-sample-prod.yaml  -n  sample-prod set image deployment/${SERVICE_NAME} ${SERVICE_NAME}=sample-prod-${BRANCH_NAME}:1.0.${BUILD_NUMBER}"
            }
            }
            }

        stage('Deployment sample-dev branch develop') {
            when {
            	branch 'develop'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh "kubectl --kubeconfig ~/.kubeconfig/kubeconfig.-sample-prod.yaml  -n  sample-prod-dev set image deployment/${SERVICE_NAME} ${SERVICE_NAME}=sample-prod-${BRANCH_NAME}:1.0.${BUILD_NUMBER}"
            }
            }
            }

        stage('Test  with katalon') {
            when {
            	branch 'master'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'sleep 1'
                // archiveArtifacts artifacts: 'vnchain_katalon/Reports/**/*.html', allowEmptyArchive: true
                // junit 'vnchain_katalon/Reports/**/*.xml'
                }
            }
            }


        stage('push nexus') {
            when {
            	branch 'master'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'sleep 1'

            }
        }
        }

        stage('run jmeter ') {
            when {
            	branch 'master'
            }
            steps {
             script {
                FAILED_STAGE=env.STAGE_NAME
                sh 'sleep 1'

        }
        }
        }

    }




    post {
        success {
            sh """
    curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"chat_id": "${USERID}", "text": " \ud83d\udc4d \ud83d\udc4d \ud83d\udc4d \nJobname: ${JOB_NAME} \nBuild number: ${BUILD_NUMBER} \nStatus: SUCCESS \nCommit: ${GIT_COMMIT} ", "disable_notification": true}' \
     ${WEBHOOK_URL}
            """
    }

        failure {
        sh """
    curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"chat_id": "${USERID}", "text": " \ud83d\ude21 \ud83d\ude21 \ud83d\ude21 \nJobname: ${JOB_NAME} \nBuild number: ${BUILD_NUMBER} \nStatus: FAILURE \nStage: ${FAILED_STAGE} \nCommit: ${GIT_COMMIT} ", "disable_notification": true}' \
     ${WEBHOOK_URL}
        """
        }

        aborted {
        sh """
    curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"chat_id": "${USERID}", "text": " \u2620\ufe0f \u2620\ufe0f \u2620\ufe0f \nJobname: ${JOB_NAME} \nBuild number: ${BUILD_NUMBER} \nStatus: ABORTED \nStage: ${FAILED_STAGE} \nCommit: ${GIT_COMMIT} ", "disable_notification": true}' \
     ${WEBHOOK_URL}
        """
        }

        unstable {
        sh """
    curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"chat_id": "${USERID}", "text": " \ud83d\ude4a \ud83d\ude4a \ud83d\ude4a \nJobname: ${JOB_NAME} \nBuild number: ${BUILD_NUMBER} \nStatus: UNSTABLE \nStage: ${FAILED_STAGE} \nCommit: ${GIT_COMMIT} ", "disable_notification": true}' \
     ${WEBHOOK_URL}
        """
        }

        always {
            deleteDir()
        }


}
}
