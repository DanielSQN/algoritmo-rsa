import rsa
# (key_pub, key_priv) = rsa.newkeys(512)
(key_pub, key_priv) = rsa.newkeys(1024)

with open('public.pem', 'wb') as f:
    f.write(key_pub.save_pkcs1('PEM'))

with open('private.pem', 'wb') as f:
    f.write(key_priv.save_pkcs1('PEM'))