import random
import string

try:
    length = int(input("Masukkan jumlah panjang password : "))
    formula = string.ascii_letters + string.digits + string.punctuation
    print('Your password: ' + "".join(random.sample(formula, length)))
except KeyboardInterrupt:
    print("\nyou quit to generate password")
except Exception as e:
    print("Gagal memasukkan data")

