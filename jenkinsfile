node {
    stage('Checkout') {
        checkout scm
    }

    stage('Python Dependencies') {
        // Only needed once if already installed on agent; for safety, we install in a venv
        bat 'python -m venv venv'
        bat '.\\venv\\Scripts\\activate && pip install selenium'
    }

    stage('Run Headless Selenium Test') {
        // Run the script
        bat '.\\venv\\Scripts\\activate && python headless_test.py'
    }
}
