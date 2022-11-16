import rsa

(key_pub, key_priv) = rsa.newkeys(512)

with open('public.pem', 'rb') as f:
    key_pub = rsa.PublicKey.load_pkcs1(f.read())

message = input('Enter a message: ')

crypto = rsa.encrypt(message.encode(), key_pub)

with open('message.txt', 'wb') as f:
    f.write(crypto)

print('El mensaje se ha encriptado correctamente')