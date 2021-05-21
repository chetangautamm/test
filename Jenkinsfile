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
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q cleanup_osm_env.sh Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
              sh "ssh Osm9-17m@20.198.70.83 ./cleanup_osm_env.sh"            
          }
        }
      }
    }    

    stage('Adding Kubespray Cluster to OSM') {
      steps {
        sh "chmod +x osm-k8s-add.sh"
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q kubespray-config.yaml Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-add.sh Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
              sh "ssh Osm9-17m@20.198.70.83 ./osm-k8s-add.sh"
          }
        }              
      }
    }

    stage('Validating Kubespray Cluster Addition') {
      steps {
        sh "chmod +x osm-k8s-validate.sh"        
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-validate.sh Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
              sh "ssh Osm9-17m@20.198.70.83 ./osm-k8s-validate.sh" 
          }
        }
      }
    }

   
    stage('Adding Kubeadm Cluster to OSM') {
      steps {
        sh "chmod +x kubeadm-add.sh"
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-config.yaml Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-add.sh Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
              sh "ssh Osm9-17m@20.198.70.83 ./kubeadm-add.sh"
          }
        }
      }
    }


    stage('Validating Kubeadm Cluster Addition') {
      steps {
        sh "chmod +x kubeadm-validate.sh"
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-validate.sh Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
              sh "ssh Osm9-17m@20.198.70.83 ./kubeadm-validate.sh"
          }
        }
      }
    }
    
    
    stage('Adding Helm Repository to OSM') {
      steps {
        sshagent(['Osm9-17m']) {
          script {
             sh "ssh Osm9-17m@20.198.70.83 osm repo-add --type helm-chart  helm-osm https://chetangautamm.github.io/osm-helm/ && sleep 10"
             sh "ssh Osm9-17m@20.198.70.83 helm repo update && sleep 10"
          }
        }
      }
    }
    stage('Validating Helm Repo Addition') {
      steps {
        sh "chmod +x osm-helm-validate.sh"
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-helm-validate.sh Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
              sh "ssh Osm9-17m@20.198.70.83 ./osm-helm-validate.sh"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for Opensips') {
      steps {
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q opensips-knf.tar.gz Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          sh "scp -o StrictHostKeyChecking=no -q opensips-kns.tar.gz Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
             sh "ssh Osm9-17m@20.198.70.83 osm nfpkg-create opensips-knf.tar.gz && sleep 10"
             sh "ssh Osm9-17m@20.198.70.83 osm nspkg-create opensips-kns.tar.gz && sleep 10"
          }
        }
      }
    }
     stage('Creating nfpkg & nspkg in OSM for UAS') {
      steps {
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q uas-knf.tar.gz Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          sh "scp -o StrictHostKeyChecking=no -q uas-kns.tar.gz Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
             sh "ssh Osm9-17m@20.198.70.83 osm nfpkg-create uas-knf.tar.gz && sleep 10"
             sh "ssh Osm9-17m@20.198.70.83 osm nspkg-create uas-kns.tar.gz && sleep 10"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for UAC') {
      steps {
        sshagent(['Osm9-17m']) {
          sh "scp -o StrictHostKeyChecking=no -q uac-knf.tar.gz Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          sh "scp -o StrictHostKeyChecking=no -q uac-kns.tar.gz Osm9-17m@20.198.70.83:/home/Osm9-17m/"
          script {
             sh "ssh Osm9-17m@20.198.70.83 osm nfpkg-create uac-knf.tar.gz && sleep 10"
             sh "ssh Osm9-17m@20.198.70.83 osm nspkg-create uac-kns.tar.gz && sleep 10"
          }
        }
      }
    }

    stage('Creating nsd in OSM') {
      steps {
        sshagent(['Osm9-17m']) {
          script {
             sh "ssh Osm9-17m@20.198.70.83 osm ns-create --ns_name opensips --nsd_name jenkins_opensips-7_ns --vim_account OpenstackR-1 && sleep 10"
             sh "ssh Osm9-17m@20.198.70.83 osm ns-create --ns_name uas --nsd_name jenkins_uas-7_ns --vim_account OpenstackR-1 && sleep 10"
             sh "ssh Osm9-17m@20.198.70.83 osm ns-create --ns_name uac --nsd_name jenkins_uac-7_ns --vim_account OpenstackR-1 && sleep 10"
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
            sh "ssh k8suser@52.172.221.4 ./configure-osm.sh"
          }
        }
      }
    }
    
     stage('Deploying Opensips IN Production-Kubeadm') {
      steps {
        sshagent(['Osm9-17m']) {
          script { 
             sh "ssh Osm9-17m@20.198.70.83 osm ns-create --ns_name opensips-prod --nsd_name jenkins_opensips-7_ns --vim_account OpenstackR-2 && sleep 10"
             sh "ssh Osm9-17m@20.198.70.83 osm ns-list"
          }
        }
      }
    }
  }
}
