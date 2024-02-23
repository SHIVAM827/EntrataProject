
# Project Title: Entrata 

## Getting Started
### 1.Prerequisites
#### a.Python 3.12.2
#### b.Pycharm
#### c.Pytest 8.0.1
#### d.pip


### 2.Download browser specific drivers using below links..(using chrome and window)

Chrome: https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.57/win64/chromedriver-win64.zip

Note: 1.Use chrome version 115 or newer.
##### 2.once you downloaded,extract .zip files then you will see .exe files(they are drivers)
Official website to download webdrivers: https://www.selenium.dev/downloads/


### 3.setup selenium webdriver
#### Approach 1:
##### a.pip install selenium
##### b.pip install pytest
##### c.pip install webdriver-manager

#### Approach 2
##### Pycharm Project settings-->interpreter -->add add selenium,pytest,webdriver-manager,chromedrivermanager,options,package_name,pip,service,servicemanager

### Important steps before running project:
##### Step1-Open PyCharm.
##### Step2-Navigate to your project.
##### Step3-In the bottom right corner, you'll see a 'Terminal' tab. Click on it to open a terminal within PyCharm.
##### Step4-Inside the terminal, run the following command:
##### 1.pip install --upgrade pytest
##### 2.pip install --upgrade pip
pip freeze | grep -v "^-e" | cut -d = -f 1  | xargs -n1 pip install -U
##### 3.pip install --upgrade package_name
##### 4.pip install --upgrade selenium
##### 5.pytest --version
##### python --version
