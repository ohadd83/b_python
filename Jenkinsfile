pipeline {

    agent any


    environment {

        IMAGE_NAME = "ohadd306/fastapi-app"
        IMAGE_TAG  = "${IMAGE_TAG}"

    }


    stages {
	
//	stage('show image tag')  {
  //          steps {
//		sh " echo ${IMAGE_TAG} "	
//		
//		}
//
//	}
        


//        stage('Checkout') {
//
//            steps {
//
  //              git branch: 'main',
    //                url: 'https://github.com/your-user/python-fastapi-app.git'

      //      }
        //}



        stage('Install Dependencies') {

            steps {

                sh '''
                python3 -m pip install -r requirements.txt
                '''

            }
        }



        stage('Run Tests') {

            steps {

                sh '''
                pytest -v
                '''

            }
        }



 //       stage('Build Docker Image') {

   //         steps {

     //           sh '''
       //         docker build \
         //       -t ${IMAGE_NAME}:${IMAGE_TAG} .
           //     '''

    //        }
      //  }



//        stage('Login Docker Hub') {

  //          steps {

    //            withCredentials([
      //              usernamePassword(
        //            credentialsId: 'dockerhub-creds',
          //          usernameVariable: 'DOCKER_USER',
            //        passwordVariable: 'DOCKER_PASS'
              //      )
             //   ]) {

               //     sh '''
                 //   echo $DOCKER_PASS | docker login \
                   // -u $DOCKER_USER \
             //       --password-stdin
               //     '''

              //  }

          //  }

      //  }

        stage('Build Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    sh """
                        echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                        docker push ${IMAGE_NAME}:${IMAGE_TAG}
                    """
                }
            }
        }

        stage('Push Docker Image') {

            steps {

                sh '''

                docker push \
                ${IMAGE_NAME}:${IMAGE_TAG}

                '''

            }

        }



        stage('Deploy Container') {

            steps {

                sh '''

                docker rm -f fastapi-container || true


                docker run -d \
                --name fastapi-container \
                -p 8000:8000 \
                ${IMAGE_NAME}:${IMAGE_TAG}

                '''

            }

        }



        stage('Health Check') {

            steps {

                sh '''

                sleep 5

                curl http://localhost:8000/health

                '''

            }

        }


    }


    post {


        success {

            echo "FastAPI deployment completed successfully"

        }


        failure {

            echo "Pipeline failed"

        }


    }

}
