from os import close
from cryptography.hazmat.primitives import hashes

f = open("test.txt", 'rb')
digest = hashes.Hash(hashes.SHA256())
digest.update(f.read())
summary = digest.finalize()
print(summary)
print(type(summary))
f.close()