pipeline {

  agent any
  environment {
		DOCKERHUB_CREDENTIALS=credentials('dockerhub-cred')
	}


  stages {
    
    

    stage('Checkout Source') {
      steps {
        git url:'https://github.com/JahanzebKhan98/simple-python-program.git', branch:'main'
      }
    }
    
    
    stage('Build') {

			steps {
				sh 'docker build -t jahanzebpythonapp:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push jahanzebpythonapp:latest'
			}
		}
    


    stage('Deploy App') {
      steps {
        script {
          kubernetesDeploy(configs: "deployment.yaml", kubeconfigId: "mykubeconfig1")
        }
      }
    }

  }
}
