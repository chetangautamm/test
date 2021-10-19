pipeline {

  environment {
    registry = "chetangautamm/repo"
    registryCredential = '58881f31-29bb-48a8-9da9-fc254654146d' 
    dockerImage = ""

    OSM_HOSTNAME = "20.204.6.188"
    OSM_USERNAME = "osm-8"

    K8S_HOSTNAME = "52.172.221.4"
    K8S_USERNAME = "k8suser"
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
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q cleanup_osm_env.sh $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
              sh 'ssh $OSM_USERNAME@$OSM_HOSTNAME ./cleanup_osm_env.sh'
               }                   
             }
           }
         }    

    stage('Adding Kubespray Cluster to OSM') {
      steps {
        sh "chmod +x osm-k8s-add.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q kubespray-config.yaml $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-add.sh $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
              sh "ssh $OSM_USERNAME@$OSM_HOSTNAME ./osm-k8s-add.sh"
          }
        }              
      }
    }

    stage('Validating Kubespray Cluster Addition') {
      steps {
        sh "chmod +x osm-k8s-validate.sh"        
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-validate.sh $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
              sh "ssh $OSM_USERNAME@$OSM_HOSTNAME ./osm-k8s-validate.sh" 
          }
        }
      }
    }

   
    stage('Adding Kubeadm Cluster to OSM') {
      steps {
        sh "chmod +x kubeadm-add.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-config.yaml $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-add.sh $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
              sh "ssh $OSM_USERNAME@$OSM_HOSTNAME ./kubeadm-add.sh"
          }
        }
      }
    }


    stage('Validating Kubeadm Cluster Addition') {
      steps {
        sh "chmod +x kubeadm-validate.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q kubeadm-validate.sh $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
              sh "ssh $OSM_USERNAME@$OSM_HOSTNAME ./kubeadm-validate.sh"
          }
        }
      }
    }
    
    
    stage('Adding Helm Repository to OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm repo-add --type helm-chart  helm-osm https://chetangautamm.github.io/osm-helm/ && sleep 10"
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME helm repo update && sleep 10"
          }
        }
      }
    }
    stage('Validating Helm Repo Addition') {
      steps {
        sh "chmod +x osm-helm-validate.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-helm-validate.sh $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
              sh "ssh $OSM_USERNAME@$OSM_HOSTNAME ./osm-helm-validate.sh"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for Opensips') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q opensips-knf.tar.gz $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q opensips-kns.tar.gz $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm nfpkg-create opensips-knf.tar.gz && sleep 10"
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm nspkg-create opensips-kns.tar.gz && sleep 10"
          }
        }
      }
    }
     stage('Creating nfpkg & nspkg in OSM for UAS') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q uas-knf.tar.gz $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q uas-kns.tar.gz $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm nfpkg-create uas-knf.tar.gz && sleep 10"
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm nspkg-create uas-kns.tar.gz && sleep 10"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for UAC') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q uac-knf.tar.gz $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q uac-kns.tar.gz $OSM_USERNAME@$OSM_HOSTNAME:/home/osm-9/"
          script {
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm nfpkg-create uac-knf.tar.gz && sleep 10"
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm nspkg-create uac-kns.tar.gz && sleep 10"
          }
        }
      }
    }

    stage('Creating nsd in OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm ns-create --ns_name opensips --nsd_name jenkins_opensips-7_ns --vim_account OpenstackR-1 && sleep 10"
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm ns-create --ns_name uas --nsd_name jenkins_uas-7_ns --vim_account OpenstackR-1 && sleep 10"
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm ns-create --ns_name uac --nsd_name jenkins_uac-7_ns --vim_account OpenstackR-1 && sleep 10"
          }
        }
      }
    }
    stage('Testing Opensips Server by SIPp') {
      steps {
        sh "chmod +x configure-osm.sh"
        sshagent(['k8suser']) {
          sh "scp -o StrictHostKeyChecking=no -q configure-osm.sh $K8S_USERNAME@$K8S_HOSTNAME:/home/k8suser"
          script {
            sh "ssh $K8S_USERNAME@$K8S_HOSTNAME ./configure-osm.sh"
          }
        }
      }
    }
    
     stage('Deploying Opensips IN Production-Kubeadm') {
      steps {
        sshagent(['osm-9']) {
          script { 
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm ns-create --ns_name opensips-prod --nsd_name jenkins_opensips-7_ns --vim_account OpenstackR-2 && sleep 10"
             sh "ssh $OSM_USERNAME@$OSM_HOSTNAME osm ns-list"
          }
        }
      }
    }
  }
}
