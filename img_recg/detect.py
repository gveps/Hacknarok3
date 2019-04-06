import io
from google.cloud import vision
from google.oauth2 import service_account


def recognize(path):
    credentials = service_account.Credentials.from_service_account_file('key.json')
    client = vision.ImageAnnotatorClient(credentials=credentials)
    with io.open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.types.Image(content=content)
    response=client.label_detection(image=image)
    labels=response.label_annotations
    names=[]
    for label in labels:
        names.append(label.description)
    return names

#HOW TO USE
print(recognize("hantel.jpg"))
