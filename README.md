<h1 align="center">
    <img align="center" src="https://user-images.githubusercontent.com/118578799/212907888-9bf45f71-8707-44e2-b536-64a46c9a7764.png" />
    <p> CryptoKo </p>
</h1>

###### This app made in python with [kivy framework](https://kivy.org), works with [cryptography](https://cryptography.io/en/latest/fernet/#cryptography.fernet.Fernet) library
###### Features
+ Encrypt messages and generate key
+ Decrypt messages with key
+ Simple and beautiful UI

# Fernet (symmetric encryption)[¶](https://cryptography.io/en/latest/fernet/#fernet-symmetric-encryption)

Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. [Fernet](https://github.com/fernet/spec/) is an implementation of symmetric (also known as “secret key”) authenticated cryptography.<br> Fernet also has support for implementing key rotation via `MultiFernet`.
<br><br>
This app generates a fresh fernet key for **each message (each time you press `Encrypt` button)**. Keep this some place safe! If you lose it you’ll no longer be able to decrypt messages; if anyone else gains access to it, they’ll be able to **decrypt your messages**, and they’ll also be able forge arbitrary messages that will be authenticated and decrypted.

### Implementation [¶](https://cryptography.io/en/latest/fernet/#implementation)
Fernet is built on top of a number of standard cryptographic primitives. Specifically it uses:
+ `AES` in `CBC` mode with a 128-bit key for encryption; using `PKCS7` padding.
+ `HMAC` using `SHA256` for authentication.
+ nitialization vectors are generated using `os.urandom()`.

### Encrypt
Encrypts data passed. The result of this encryption is known as a “Fernet token” and has strong privacy and authenticity guarantes. you will receive both the encrypted plaintext and decryption key as the result copied to clipboard
```
Encrypted Message: 
gAAAAABjyikCuDrKLCNF3f-W8mYjrQYiBNU5ggIoDutXMP6yikWewN3XIq0NGhE5OkR30hpSpnR21ZucRcGQ7-2yQZC4JaFhrA==

Decryption Key: 
fKf3iOMfUQ-UrIddfvFPrEDWEGPQDnUzS4wKIXrzZYQ=
```

### Decrypt
If successfully decrypted you will receive the original plaintext as the result copied to clipboard, otherwise an exception will be raised
```
Decrypted Message: 
hi
```
### Note
So... I'm new in Kivy and trying to learn more and more. in future, I may add more features.
+ resize main kivy window when soft keyboard appears
+ encrypt_at_time
+ decrypt_at_time 
+ extract_timestamp
+ more screens

> Hope you enjoy it.

# Installation
+ clone
```bash
git clone https://github.com/Kourva/CryptoKo && cd CryptoKo
```
+ requirements
```bash
pip install kivy cryptography
```
+ run
```bash
python3 main.py
```
 ###### use [google colab](https://colab.research.google.com/) and convert your kivy app to apk easily.


# Preview
<p align="center">
    <img align="left" src="https://user-images.githubusercontent.com/118578799/212908630-4b5c9eb1-d30c-421d-a15e-3946b8cad426.png" width=180 height=400 />
    <img align="center" src="https://user-images.githubusercontent.com/118578799/212908637-27649336-3472-48df-9a6f-28c6eda59277.jpg" width=180 height=400 />
    <img align="right" src="https://user-images.githubusercontent.com/118578799/212908645-29117a2c-022d-4531-82de-bdb469ab964f.jpg" width=180 height=400 />
</p>
