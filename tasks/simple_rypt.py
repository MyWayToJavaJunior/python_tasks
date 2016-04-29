from simplecrypt import encrypt, decrypt, DecryptionException


PASSWORDS = ['9XB8nsIqRfYeswC',
             '4sEhUGLEZti9BiN',
             'bDjmT0NcIW8nzhb',
             'ZN6QQoMOO1ZQLUY',
             'RVrF2qdMpoq6Lib',
             'tnnX7HH3vJ9Hiji',
             'C24TJYYkqekv40l',
             'B2ropluPaMAitzE',
             'DRezNUVnr2zC0CP',
             'XCNmpTvvZb1n3mX']

FILENAME = "encrypted.bin"


def main():
    with open(FILENAME, "rb") as inp:
        encrypted = inp.read()

    flag = True
    info = ''
    while flag:
        try:
            for i in reversed(range(len(PASSWORDS))):
                # print(info, PASSWORDS[i])
                info = decrypt(PASSWORDS[i].strip(), encrypted)
                print(info.decode('utf8'))
                flag = False

        except DecryptionException:
            PASSWORDS.pop()

if __name__ == '__main__':
    main()

