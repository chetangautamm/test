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
        git 'https://github.com/chetangautamm/helm-k8s-deployment.git'
      }
    }
    
    
    stage('Adding Kubespray Cluster to OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
              sh "ssh osm-9@20.198.96.248 osm k8scluster-add --creds kubespray-config.yaml --version '1.20.2' --vim devstack --description "Kubespray Cluster" --k8s-nets '{"net1": "external"}' kubespray-cluster"
          }
        }              
      }
    }

    stage('Validating Cluster Addition') {
      steps {
        sh "chmod +x osm-k8s-validate.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-validate.sh osm-9@20.198.96.248:/home/osm-9"
          script {
              sh "ssh osm-9@20.198.96.248 ./osm-k8s-validate.sh"
          }
        }
      }
    }
    stage('Adding Helm Repository to OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
             sh "ssh osm-9@20.198.96.248 osm repo-add helm-repo https://chetangautamm.github.io/osm-helm/"
          }
        }
      }
    }
    stage('Validating Helm Repo Addition') {
      steps {
        sh "chmod +x osm-helm-validate.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-helm-validate.sh osm-9@20.198.96.248:/home/osm-9"
          script {
              sh "ssh osm-9@20.198.96.248 ./osm-helm-validate.sh"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for Opensips') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q opensips-nf.tar.gz osm-9@20.198.96.248:/home/osm-9"
          sh "scp -o StrictHostKeyChecking=no -q opensips-ns.tar.gz osm-9@20.198.96.248:/home/osm-9"
          script {
             sh "ssh osm-9@20.198.96.248 osm nfpkg-create opensips-nf.tar.gz"
             sh "ssh osm-9@20.198.96.248 osm nspkg-create opensips-ns.tar.gz"
          }
        }
      }
    }
     stage('Creating nfpkg & nspkg in OSM for Sipp') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q sipp-nf.tar.gz osm-9@20.198.96.248:/home/osm-9"
          sh "scp -o StrictHostKeyChecking=no -q sipp-ns.tar.gz osm-9@20.198.96.248:/home/osm-9"
          script {
             sh "ssh osm-9@20.198.96.248 osm nfpkg-create sipp-nf.tar.gz"
             sh "ssh osm-9@20.198.96.248 osm nspkg-create sipp-ns.tar.gz"
          }
        }
      }
    }
    stage('Creating nsd in OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
             sh "ssh osm-9@20.198.96.248 osm ns-create --ns_name opensips --nsd_name cicd_opensips-7_ns --vim_account OpenstackR"
             sh "ssh osm-9@20.198.96.248 osm ns-create --ns_name sipp --nsd_name cicd_opensips-7_ns --vim_account OpenstackR"
          }
        }
      }
    }
    stage('Validating Opensips Using SIPp') {
      steps {
        sh "chmod +x configure-osm.sh"
        sshagent(['k8suser']) {
          sh "scp -o StrictHostKeyChecking=no -q configure-osm.sh k8suser@52.172.221.4:/home/k8suser"
          script {
            sh "sleep 10"
            sh "ssh k8suser@52.172.221.4 ./configure-osm.sh"
          }
        }
      }
    }
  }
}
