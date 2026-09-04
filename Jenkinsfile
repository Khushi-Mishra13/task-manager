pipeline{
  agent any
	stages{
		stage('checkout scm'){
			steps{
				checkout scm
				}
			}
		stage('Build Image'){
			steps{
				sh 'docker compose build'
				}
			}
		stage('Run the image'){
			steps{
				sh 'docker compose up -d'
				}
			}
		}
	}
