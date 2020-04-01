from google.cloud import vision
from google.protobuf.json_format import MessageToJson
import base64
import json

def dniverification(request):
    request_json = request.get_json()
    if request_json and 'img' in request_json:
        data = document_ocr(request_json['img'])
        print('----------------')
        print(json.loads(data)['textAnnotations'][0]['description'])
        print('----------------')
        return data
    else:
        return f'Error!'

def document_ocr(image):
    client = vision.ImageAnnotatorClient()
    response = client.annotate_image({'image': {'content': base64.b64decode(image)}, 'features': [{'type': vision.enums.Feature.Type.DOCUMENT_TEXT_DETECTION}],})
    return MessageToJson(response)
