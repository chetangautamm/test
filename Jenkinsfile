pipeline {

  agent any

  stages {

    stage('Checkout Source Code') {
      steps {
        git 'https://github.com/chetangautamm/test.git'
      }
    }
    
    stage('Executing Commands on OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
            sh "pwd"
            sh "ssh osm-9@20.198.76.9 osm ns-list"
          }
        }              
      }
    }
  }
}
