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
				sh 'docker build -t 03022086691/jahanzebpythonapp:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push 03022086691/jahanzebpythonapp:latest'
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
