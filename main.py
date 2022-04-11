from fastapi import FastAPI
import json
from Crypto.Cipher import AES
from base64 import b64decode

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/lotuspay")
async def lotus_pay_webhook():
    msg = json.loads('DvaraWebHook')['serialized_response']
    iv = msg[:16].encode('utf-8')
    decipher = AES.new('whk_:PqnYy_VUz7Z', AES.MODE_CBC, iv=iv)
    cipher_text = b64decode(msg[16:].encode('utf-8'))
    data = decipher.decrypt(cipher_text)
    event = json.loads(data[:data.rfind('}')+1])
    return event