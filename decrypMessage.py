import rsa

with open('private.pem', 'rb') as f:
    key_priv = rsa.PrivateKey.load_pkcs1(f.read())

with open('message.txt', 'rb') as f:
    crypto = f.read()

try:
    message = rsa.decrypt(crypto, key_priv).decode()
    print('message descripted:', message)
    print('El mensaje se ha desencriptado correctamente')
except:
    print('Error: The message could not be decrypted')
