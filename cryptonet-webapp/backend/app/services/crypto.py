import os, hashlib, secrets, json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hmac, hashes
from cryptography.hazmat.backends import default_backend

def generate_file_id(filepath: str) -> str:
    sha = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()

def encrypt_file(filepath: str, remove_original: bool = False):
    file_id = generate_file_id(filepath)
    key = secrets.token_bytes(32)
    iv = secrets.token_bytes(16)
    hmac_key = secrets.token_bytes(32)

    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    h = hmac.HMAC(hmac_key, hashes.SHA256(), backend=default_backend())

    out_path = filepath + '.enc'
    with open(filepath, 'rb') as fin, open(out_path, 'wb') as fout:
        fout.write(iv)
        for chunk in iter(lambda: fin.read(4096), b""):
            ct = encryptor.update(chunk)
            fout.write(ct)
            h.update(ct)
        fout.write(encryptor.finalize())
    with open(out_path + '.hmac', 'wb') as hfile:
        hfile.write(h.finalize())
    keyfile = filepath + '.key'
    with open(keyfile, 'w') as kf:
        json.dump({'file_id': file_id, 'aes_key': key.hex(), 'hmac_key': hmac_key.hex()}, kf)

    if remove_original:
        os.remove(filepath)
    return out_path

def decrypt_file(enc_path: str, remove_original: bool = False):
    keyfile = enc_path.replace('.enc', '.key')
    with open(keyfile) as kf:
        data = json.load(kf)
    key = bytes.fromhex(data['aes_key'])
    hmac_key = bytes.fromhex(data['hmac_key'])

    with open(enc_path, 'rb') as fin:
        iv = fin.read(16)
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        h = hmac.HMAC(hmac_key, hashes.SHA256(), backend=default_backend())
        ciphertext = fin.read()
        h.update(ciphertext)
        h.verify()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    orig_path = enc_path.replace('.enc', '.dec')
    with open(orig_path, 'wb') as fout:
        fout.write(plaintext)

    if remove_original:
        os.remove(enc_path)
        os.remove(keyfile)
        os.remove(enc_path + '.hmac')
    return orig_path
