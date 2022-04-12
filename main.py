from fastapi import FastAPI, status, Request, Body
import json
from Crypto.Cipher import AES
from base64 import b64decode
import uvicorn
from typing import Dict

app = FastAPI()


def response_to_dict(response):
    """Converting bytes response to python dictionary"""
    # response_content = response.content
    # response_decode = response.decode("UTF-8")
    # json_acceptable_string = response.replace("'", "\"")
    convert_to_json = json.loads(response)
    response_dict = dict(convert_to_json)
    return response_dict


@app.post("/")
async def root(payload: Dict = Body(...)):
    print('hello coming here', payload)
    return {"message": "Hello World"}


@app.post("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/lotuspay")
async def lotus_pay_webhook(payload: Dict = Body(...), status_code=status.HTTP_200_OK):
    #msg = json.loads('sk_test_5kCfPu3Wx6VBNZsbc6a6TibS')
    #payload_response = {"serialized_response":"5kCfPu3Wx6VBNZsbc6a6TibS"}
    #msg = json.loads(payload_response)
    #msg =
    msg = payload['serialized_response']
    print('printing serialized response - ', msg)
    #msg = json.loads(payload)['serialized_response']
    #iv = msg[:16].encode('utf-8')
    iv = msg[:16].encode('utf-8')
    decipher = AES.new('whk_:PqnYy_VUz7Z'.encode('utf-8'), AES.MODE_CBC, iv=iv)
    cipher_text = b64decode(msg[16:].encode('utf-8'))
    #cipher_text = b64decode(msg[16:].encode('utf-8'))
    data = decipher.decrypt(cipher_text)
    print('printing data - ', data)
    # event = json.loads(data[:data.rfind('}')+1])
    # event = json.loads(data)
    event = json.loads(data[:data.rfind('}')])

    print('printing event - ', event)
    # data_dict = response_to_dict(data)
    # return event
    # return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)