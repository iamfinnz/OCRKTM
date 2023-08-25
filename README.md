# OCRKTM
Source code to extract NIM of KTM with Tesseract OCR

## Prerequisites
1. Server/Virtual Machine with this minimum spesification
   - 1 vCPU
   - 2 GB of Memory
   - 20 GB of Disk
2. Operating System: Linux Ubuntu 22.04
3. Python v3.10.x (built-in Ubuntu OS)
4. Tesseract-ocr for Ubuntu OS
5. Python Flask
6. Docker and docker compose <br/>
   https://docs.docker.com/engine/install/ubuntu/

## How to run on local
1. Update the apt package manager
   
   ```bash
   sudo apt update -y
   ```
   
2. Check the python version and install pip3 for the python package manager and it’s dependencies
   
   ```bash
   python3 --version
   sudo apt install python3-pip python3-flask tesseract-ocr -y
   pip3 install --user -r requirements.txt
   ```
   
3. Run the app in development mode
   ```bash
   git clone https://github.com/iamfinnz/OCRKTM.git
   cd OCRKTM
   export FLASK_APP=app.py
   flask run --host=0.0.0.0
   ```

## How to run on local / Update Flask OCR with Docker on Server
1. Run this command to update current docker image with the new ones based on git repository
   
   ```bash
   cd ~/OCRKTM
   git pull
   docker-compose up -d
   ```
   
## Result
[Home](http://103.193.176.122:5000/) (Request GET) <br/>
[Predict](http://103.193.176.122:5000/predict) (Request POST)
