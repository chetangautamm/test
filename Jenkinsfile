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
    stage('Cleanup OSM Environment') {
      steps {
        sh "chmod +x cleanup_osm_env.sh"
        sshagent(['Osm9-12m']) {
          sh "scp -o StrictHostKeyChecking=no -q cleanup_osm_env.sh Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          script {
              sh "ssh Osm9-12m@20.198.121.127 ./cleanup_osm_env.sh"
              sh "ssh Osm9-12m@20.198.121.127 sleep 10"
          }
        }
      }
    }

    stage('Adding Kubespray Cluster to OSM') {
      steps {
        sh "chmod +x osm-k8s-add.sh"
        sshagent(['Osm9-12m']) {
          sh "scp -o StrictHostKeyChecking=no -q kubespray-config.yaml Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-add.sh Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          script {
              sh "ssh Osm9-12m@20.198.121.127 ./osm-k8s-add.sh"
          }
        }              
      }
    }
   
    stage('Adding Kubeadm Cluster to OSM') {
      steps {
        sh "chmod +x kubeadm-add.sh"
        sshagent(['kubeadm']) {
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-config.yaml kubeadm@20.193.238.113:/home/Osm9-12m/"
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-add.sh kubeadm@20.193.238.113:/home/Osm9-12m/"
          script {
              sh "ssh Osm9-12m@20.198.121.127 ./kubeadm-add.sh"
          }
        }
      }
    }


    stage('Validating Cluster Addition') {
      steps {
        sh "chmod +x osm-k8s-validate.sh"
        sh "chmod +x kubeadm-validate.sh"
        sshagent(['Osm9-12m']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-validate.sh Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          script {
              sh "ssh Osm9-12m@20.198.121.127 ./osm-k8s-validate.sh"
              sh "ssh Osm9-12m@20.198.121.127 sleep 5"
          }
        }
        sshagent(['kubeadm']) {
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-validate.sh kubeadm@20.193.238.113:/home/Osm9-12m/"
          script {
              sh "ssh kubeadm@20.193.238.113 ./kubeadm-validate.sh"
          }
        }
      }
    }
    
    
    stage('Adding Helm Repository to OSM') {
      steps {
        sshagent(['Osm9-12m']) {
          script {
             sh "ssh Osm9-12m@20.198.121.127 osm repo-add --type helm-chart  helm-osm https://chetangautamm.github.io/osm-helm/"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 helm repo update"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
          }
        }
      }
    }
    stage('Validating Helm Repo Addition') {
      steps {
        sh "chmod +x osm-helm-validate.sh"
        sshagent(['Osm9-12m']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-helm-validate.sh Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          script {
              sh "ssh Osm9-12m@20.198.121.127 ./osm-helm-validate.sh"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for Opensips') {
      steps {
        sshagent(['Osm9-12m']) {
          sh "scp -o StrictHostKeyChecking=no -q opensips-knf.tar.gz Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          sh "scp -o StrictHostKeyChecking=no -q opensips-kns.tar.gz Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          script {
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm nfpkg-create opensips-knf.tar.gz"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm nspkg-create opensips-kns.tar.gz"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
          }
        }
      }
    }
     stage('Creating nfpkg & nspkg in OSM for UAS') {
      steps {
        sshagent(['Osm9-12m']) {
          sh "scp -o StrictHostKeyChecking=no -q uas-knf.tar.gz Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          sh "scp -o StrictHostKeyChecking=no -q uas-kns.tar.gz Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          script {
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm nfpkg-create uas-knf.tar.gz"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm nspkg-create uas-kns.tar.gz"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for UAC') {
      steps {
        sshagent(['Osm9-12m']) {
          sh "scp -o StrictHostKeyChecking=no -q uac-knf.tar.gz Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          sh "scp -o StrictHostKeyChecking=no -q uac-kns.tar.gz Osm9-12m@20.198.121.127:/home/Osm9-12m/"
          script {
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm nfpkg-create uac-knf.tar.gz"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm nspkg-create uac-kns.tar.gz"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
          }
        }
      }
    }
     stage('Cleanup Kubernetes') {
      steps {
        sh "chmod +x k8s-cleanup.sh"
        sshagent(['k8suser']) {
          sh "scp -o StrictHostKeyChecking=no -q k8s-cleanup.sh k8suser@52.172.221.4:/home/k8suser"
          script {
            sh "ssh k8suser@52.172.221.4 ./k8s-cleanup.sh"
            sh "ssh k8suser@52.172.221.4 sleep 30"
          }
        }
      }
    }
    
     stage('Cleanup Kubeadm') {
      steps {
        sh "chmod +x kubeadm-cleanup.sh"
        sshagent(['kubeadm']) {
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-cleanup.sh kubeadm@20.193.238.113:/home/k8suser"
          script {
            sh "ssh kubeadm@20.193.238.113 ./kubeadm-cleanup.sh"
            sh "ssh kubeadm@20.193.238.113 sleep 30"
          }
        }
      }
    }


    stage('Creating nsd in OSM') {
      steps {
        sshagent(['Osm9-12m']) {
          script {
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm ns-create --ns_name opensips --nsd_name jenkins_opensips-7_ns --vim_account OpenstackR"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm ns-create --ns_name uas --nsd_name jenkins_uas-7_ns --vim_account OpenstackR"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm ns-create --ns_name uac --nsd_name jenkins_uac-7_ns --vim_account OpenstackR"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
          }
        }
      }
    }
    stage('Testing Opensips Server by SIPp') {
      steps {
        sh "chmod +x configure-osm.sh"
        sshagent(['k8suser']) {
          sh "scp -o StrictHostKeyChecking=no -q configure-osm.sh k8suser@52.172.221.4:/home/k8suser"
          script {
            sh "ssh k8suser@52.172.221.4 sleep 120"
            sh "ssh k8suser@52.172.221.4 ./configure-osm.sh"
          }
        }
      }
    }
    
     stage('Creating nsd in OSM for Kubeadm') {
      steps {
        sshagent(['Osm9-12m']) {
          script {
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm ns-create --ns_name opensips-prod --nsd_name jenkins_opensips-7_ns --vim_account OpenstackR"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm ns-create --ns_name uas-prod --nsd_name jenkins_uas-7_ns --vim_account OpenstackR"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
             sh "ssh Osm9-12m@20.198.121.127 osm ns-create --ns_name uac-prod --nsd_name jenkins_uac-7_ns --vim_account OpenstackR"
             sh "ssh Osm9-12m@20.198.121.127 sleep 10"
          }
        }
      }
    }
    stage('Testing Opensips Server by SIPp on Kubeadm') {
      steps {
        sh "chmod +x configure-osm.sh"
        sshagent(['kubeadm']) {
          sh "scp -o StrictHostKeyChecking=no -q configure-osm.sh kubeadm@20.193.238.113:/home/k8suser"
          script {
            sh "ssh kubeadm@20.193.238.113 sleep 120"
            sh "ssh kubeadm@20.193.238.113 ./configure-osm.sh"
          }
        }
      }
    }
  }
}
