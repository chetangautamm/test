pipeline {

  environment {
    registry = "chetangautamm/repo"
    registryCredential = '58881f31-29bb-48a8-9da9-fc254654146d' 
    dockerImage = ""
  }

  agent any

  stages {

    stage('Checkout Source Code') {
      steps {
        git 'https://github.com/chetangautamm/test.git'
      }
    }
    
    
    stage('Adding Kubespray Cluster to OSM') {
      steps {
        sh "chmod +x osm-k8s-add.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q kubespray-config.yaml osm-9@104.211.79.50:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-add.sh osm-9@104.211.79.50:/home/osm-9/"
          script {
              sh "ssh osm-9@104.211.79.50 ./osm-k8s-add.sh"
          }
        }              
      }
    }

    stage('Validating Cluster Addition') {
      steps {
        sh "chmod +x osm-k8s-validate.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-validate.sh osm-9@104.211.79.50:/home/osm-9/"
          script {
              sh "ssh osm-9@104.211.79.50 ./osm-k8s-validate.sh"
          }
        }
      }
    }
    stage('Adding Helm Repository to OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
             sh "ssh osm-9@104.211.79.50 osm repo-add --type helm-chart  helm-osm https://chetangautamm.github.io/osm-helm/"
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 helm repo update"
             sh "ssh osm-9@104.211.79.50 sleep 10"
          }
        }
      }
    }
    stage('Validating Helm Repo Addition') {
      steps {
        sh "chmod +x osm-helm-validate.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-helm-validate.sh osm-9@104.211.79.50:/home/osm-9/"
          script {
              sh "ssh osm-9@104.211.79.50 ./osm-helm-validate.sh"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for Opensips') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q opensips-knf.tar.gz osm-9@104.211.79.50:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q opensips-kns.tar.gz osm-9@104.211.79.50:/home/osm-9/"
          script {
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm nfpkg-create opensips-knf.tar.gz"
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm nspkg-create opensips-kns.tar.gz"
             sh "ssh osm-9@104.211.79.50 sleep 10"
          }
        }
      }
    }
     stage('Creating nfpkg & nspkg in OSM for UAS') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q uas-knf.tar.gz osm-9@104.211.79.50:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q uas-kns.tar.gz osm-9@104.211.79.50:/home/osm-9/"
          script {
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm nfpkg-create uas-knf.tar.gz"
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm nspkg-create uas-kns.tar.gz"
             sh "ssh osm-9@104.211.79.50 sleep 10"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for UAC') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q uac-knf.tar.gz osm-9@104.211.79.50:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q uac-kns.tar.gz osm-9@104.211.79.50:/home/osm-9/"
          script {
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm nfpkg-create uac-knf.tar.gz"
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm nspkg-create uac-kns.tar.gz"
             sh "ssh osm-9@104.211.79.50 sleep 10"
          }
        }
      }
    }
    stage('Creating nsd in OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm ns-create --ns_name opensips --nsd_name jenkins_opensips-7_ns --vim_account OpenstackR"
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm ns-create --ns_name uas --nsd_name jenkins_uas-7_ns --vim_account OpenstackR"
             sh "ssh osm-9@104.211.79.50 sleep 10"
             sh "ssh osm-9@104.211.79.50 osm ns-create --ns_name uac --nsd_name jenkins_uac-7_ns --vim_account OpenstackR"
             sh "ssh osm-9@104.211.79.50 sleep 10"
          }
        }
      }
    }
    stage('Testing Opesnips Server by SIPp') {
      steps {
        sh "chmod +x configure-osm.sh"
        sshagent(['k8suser']) {
          sh "scp -o StrictHostKeyChecking=no -q configure-osm.sh k8suser@52.172.221.4:/home/k8suser"
          script {
            sh "ssh k8suser@52.172.221.4 sleep 30"
            sh "ssh k8suser@52.172.221.4 ./configure-osm.sh"
          }
        }
      }
    }
  }
}
