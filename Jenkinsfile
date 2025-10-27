pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "sasivakulrithwik/devops-assignment-2"
        K8S_NAMESPACE = "default"
        DOCKER_TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "🔄 Checking out source code..."
                checkout scm
            }
        }

        stage('Build Docker') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-id-cred', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                    echo Logging into Docker Hub...
                    echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin

                    echo Building Docker image...
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }

        stage('Test Application') {
            steps {
                script {
                    echo "⚡ Testing Docker container..."

                    // Remove old container
                    bat "docker rm -f test-app || echo No existing container"

                    // Run container on port 5000
                    bat "docker run -d --name test-app -p 8001:8000 ${DOCKER_IMAGE}:${DOCKER_TAG}"

                    // Wait for app startup using ping (10 seconds)
                    bat "ping -n 10 127.0.0.1 > nul"

                    // Health check
                    def healthCheck = bat(
                        script: 'powershell -Command "try { $response = Invoke-WebRequest -Uri http://localhost:8001/ -TimeoutSec 10 -UseBasicParsing; Write-Host \\\"SUCCESS: Status \\\" + $response.StatusCode; exit 0 } catch { Write-Host \\\"FAILED: \\\" + $_.Exception.Message; exit 1 }"',
                        returnStatus: true
                    )
                    
                    // Debug: Check container logs if health check fails
                    if (healthCheck != 0) {
                        echo "❌ Health check failed! Checking container logs..."
                        bat "docker logs test-app"
                        error("❌ Health check failed!")
                    } else {
                        echo "✅ Health check passed!"
                    }

                    // Stop and remove container
                    bat "docker stop test-app && docker rm test-app || echo Container already removed"
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-id-cred', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    bat """
                    echo Pushing Docker images...
                    docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                    docker push ${DOCKER_IMAGE}:latest
                    """
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'kube-config', variable: 'KUBECONFIG_FILE')]) {
                    bat '''
                    echo Setting up kubeconfig...
                    if not exist "%USERPROFILE%\\.kube" mkdir "%USERPROFILE%\\.kube"
                    copy /Y "%KUBECONFIG_FILE%" "%USERPROFILE%\\.kube\\config"
                    '''

                    bat """
                    echo Deploying to Kubernetes...
                    kubectl apply -f deployment.yaml --namespace ${K8S_NAMESPACE}
                    kubectl apply -f service.yaml --namespace ${K8S_NAMESPACE}

                    echo Updating image in deployment...
                    kubectl set image deployment/devops-assignment-2 devops-assignment-2-app=${DOCKER_IMAGE}:${DOCKER_TAG} --namespace ${K8S_NAMESPACE}
                    
                    echo Waiting for rollout to complete...
                    kubectl rollout status deployment/devops-assignment-2 --namespace ${K8S_NAMESPACE} --timeout=180s
                    
                    echo Deployment status:
                    kubectl get deployments,pods,services --namespace ${K8S_NAMESPACE}
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ SUCCESS: Build ${env.BUILD_NUMBER} completed."
        }
        failure {
            echo "❌ FAILED: Build ${env.BUILD_NUMBER}."
        }
        always {
            echo "🧹 Cleaning up Docker images..."
            bat "docker image prune -f"
        }
    }
}