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
          sh "scp -o StrictHostKeyChecking=no -q kubespray-config.yaml osm-9@13.71.29.238:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-add.sh osm-9@13.71.29.238:/home/osm-9/"
          script {
              sh "ssh osm-9@13.71.29.238 ./osm-k8s-add.sh"
          }
        }              
      }
    }

    stage('Validating Cluster Addition') {
      steps {
        sh "chmod +x osm-k8s-validate.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-k8s-validate.sh osm-9@13.71.29.238:/home/osm-9/"
          script {
              sh "ssh osm-9@13.71.29.238 ./osm-k8s-validate.sh"
          }
        }
      }
    }
    stage('Adding Helm Repository to OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
             sh "ssh osm-9@13.71.29.238 osm repo-add helm-repo https://chetangautamm.github.io/osm-helm/"
          }
        }
      }
    }
    stage('Validating Helm Repo Addition') {
      steps {
        sh "chmod +x osm-helm-validate.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q osm-helm-validate.sh osm-9@13.71.29.238:/home/osm-9/"
          script {
              sh "ssh osm-9@13.71.29.238 ./osm-helm-validate.sh"
          }
        }
      }
    }
    stage('Creating nfpkg & nspkg in OSM for Opensips') {
      steps {
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q opensips-nf.tar.gz osm-9@13.71.29.238:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q opensips-ns.tar.gz osm-9@13.71.29.238:/home/osm-9/"
          script {
             sh "ssh osm-9@13.71.29.238 ls"
             sh "ssh osm-9@13.71.29.238 pwd"
          }
        }
      }
    }
     stage('Creating nfpkg & nspkg in OSM for Sipp') {
      steps {
        sh "chmod +x test-sipp.sh"
        sshagent(['osm-9']) {
          sh "scp -o StrictHostKeyChecking=no -q sipp-nf.tar.gz osm-9@13.71.29.238:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q test-sipp.sh osm-9@13.71.29.238:/home/osm-9/"
          sh "scp -o StrictHostKeyChecking=no -q sipp-ns.tar.gz osm-9@13.71.29.238:/home/osm-9/"
          script {
             sleep "10"
             sh "ssh osm-9@13.71.29.238 osm nfpkg-create sipp-nf.tar.gz"
             sleep "10"
             sh "ssh osm-9@13.71.29.238 osm nspkg-create sipp-ns.tar.gz"
          }
        }
      }
    }
    stage('Creating nsd in OSM') {
      steps {
        sshagent(['osm-9']) {
          script {
             sh "ssh osm-9@13.71.29.238 ls"
             sh "ssh osm-9@13.71.29.238 osm ns-create --ns_name uas-sipp --nsd_name cicd_sipp_uas-30_ns --vim_account OpenstackR"
          }
        }
      }
    }
  }
}
