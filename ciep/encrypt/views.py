from django.shortcuts import render


def home(request):
    boards = [
        {'name': '对称加密', 'link': '/encrypt/secretkey'},
        {'name': '非对称加密', 'link': '/encrypt/publickey'}
    ]
    return render(request, 'encrypt/home.html', {'boards': boards})


def secretKey_home(request):
    boards = [
        {'name': 'AES', 'link': 'encrypt/secretkey/aes'},
        {'name': 'DES', 'link': 'encrypt/secretkey/des'},
        {'name': 'RC4', 'link': 'encrypt/secretkey/rc4'},
    ]
    return render(request, 'encrypt/secretKey/home.html', {'boards': boards})


def publicKey_home(request):
    boards = [
        {'name': 'RSA', 'link': 'encrypt/publickey/rsa'},
        {'name': 'ElGamal', 'link': 'encrypt/publickey/elgamal'}
    ]
    return render(request, 'encrypt/publicKey/home.html', {'boards': boards})
