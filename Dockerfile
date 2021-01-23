FROM mcr.microsoft.com/azure-functions/python:3.0-python3.7

ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
AzureFunctionsJobHost__Logging__Console__IsEnabled=true

COPY requirements.txt /

RUN pip install -r /requirements.txt

RUN apt-get update && apt-get install -y tesseract-ocr

# this will copy there files inside the docker image(Dockerfile  HttpOcrFunc  host.json  requirements.txt)
COPY . /home/site/wwwroot