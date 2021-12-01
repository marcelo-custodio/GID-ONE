from os import close
from cryptography.hazmat.primitives import hashes
import base64 as b64
f = open("test.txt", 'rb')
digest = hashes.Hash(hashes.SHA256())
digest.update(f.read())
summary = digest.finalize()
print(summary)
print(len(summary))
print(b64.encodebytes(summary))
print(len(b64.encodebytes(summary)))
print(type(summary))
f.close()