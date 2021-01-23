import logging
import pytesseract
from PIL import Image
import azure.functions as func
import os
# defining a main fuction , it need one arg func.HttpRequest and we will store it in variable req.(req: func.HttpRequest)
# and output of this function is func.HttpResponse (-> func.HttpResponse: )
def main(req: func.HttpRequest) -> func.HttpResponse: 
    
    # Log the information when function trigger.
    logging.info('Python HTTP trigger function processed a request.')
 
    # test code for OCR
    try:
        # ('file') this file is argument passed by http request coming via browser or postman .
        file = req.files.get('file')
        file.save('/tmp/1.jpg')
    except ValueError:
        pass

    text = ''
    if file: # if file is present then extract text from it.
        text = str(pytesseract.image_to_string(Image.open('/tmp/1.jpg')))
    
    # return the extracted text via http response. (func.HttpResponse)
    return func.HttpResponse('text Extracted from Image: {}'.format(text))