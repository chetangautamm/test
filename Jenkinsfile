pipeline {

  agent any

  stages {

    stage('Checkout Source Code') {
      steps {
        git 'https://github.com/chetangautamm/k8s-deployment.git'
      }
    }
    
    
    stage('Deploying Opensips CNF') {
      steps {
        sshagent(['k8suser']) {
          sh "scp -o StrictHostKeyChecking=no -q opensips.yaml k8suser@52.172.221.4:/home/k8suser"
          script {
            try {
              sh "ssh k8suser@52.172.221.4 kubectl apply -f opensips.yaml"
            }catch(error){
              sh "ssh k8suser@52.172.221.4 kubectl apply -f opensips.yaml"
            } 
          }
        }              
      }
    }
    stage('Validating Opensips Using SIPp') {
      steps {
        sh "chmod +x configure.sh"
        sshagent(['k8suser']) {
          sh "scp -o StrictHostKeyChecking=no -q configure.sh k8suser@52.172.221.4:/home/k8suser"
          script {
            sh "sleep 10"
            sh "ssh k8suser@52.172.221.4 ./configure.sh"
          }
        }              
      }
    }
  }
}
