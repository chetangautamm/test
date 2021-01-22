pipeline{
    agent any 
    stages{
        stage("Git Checkout"){
            steps{
                git credentialsId: '0280c339-f1a8-48bc-b303-3ec7a661b546', url: 'https://github.com/chetangautamm/test'
            }
        }
    }
}
