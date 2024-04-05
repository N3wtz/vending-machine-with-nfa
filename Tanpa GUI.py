class VendingMachine:
    def __init__(self):
        self.state = 'q0'
        self.balance = 0
        self.output = 0

    def input_transition(self, input):
        if self.state == 'q0':
            if input == 'b':
                self.state = 'q2'
                self.balance = 5000
            elif input == 'c':
                self.state = 'q3'
                self.balance = 10000
            elif input == 'd':
                self.state = 'q5'
                self.balance = 20000
            elif input == 't':
                self.state = 'q7'
                self.balance = 50000
            elif input == 'e':
                self.state = 'q6'

        elif self.state == 'q2':
            if input == 'b':
                self.state = 'q3'
                self.balance += 5000
            elif input == 'c':
                self.state = 'q4'
                self.balance += 10000
            elif input == 'e':
                self.state = 'q6'

        elif self.state == 'q3':
            if input == 'b':
                self.state = 'q4'
                self.balance += 5000
            elif input == 'c':
                self.state = 'q5'
                self.balance += 10000
            elif input == 'e':
                self.state = 'q6'

        elif self.state == 'q4':
            if input == 'b':
                self.state = 'q5'
                self.balance += 5000
            elif input == 'i':
                self.state = 'q9'
                self.output = 4
            elif input == 'h':
                self.state = 'q10'
                self.output = 6
            elif input == 'e':
                self.state = 'q6'

        elif self.state == 'q5':
            if input == 'e':
                self.state = 'q6'
            elif input == 'f':
                self.state = 'q8'
                self.output = 0
            elif input == 'i':
                self.state = 'q23'
            elif input == 'h':
                self.state = 'q23'

        elif self.state == 'q7':
            if input == 'e':
                self.state = 'q6'
            elif input == 'f':
                self.state = 'q21'
                self.output = 0
            elif input == 'i' or input == 'h':
                self.state = 'q22'
                self.output = 0

        elif self.state == 'q21':
            if input == 'f':
                self.state = 'q8'
                self.output = 0

        elif self.state == 'q22':
            if input == 'i':
                self.state = 'q9'
                self.output = 0
            elif input == 'h':
                self.state = 'q10'
                self.output = 0

        elif self.state == 'q6':
            if input == 'a':
                self.state = 'q1'
                self.output = 0
        
        elif self.state == 'q8':
            if input == 'j':
                self.state = 'q11'
                self.output = 1  # Nasi Ayam Kecap
            elif input == 'k':
                self.state = 'q12'
                self.output = 2  # Nasi Kari
            elif input == 'l':
                self.state = 'q13'
                self.output = 3  # Nasi Rendang

        elif self.state == 'q9':
            if input == 'm':
                self.state = 'q14'
                self.output = 4  # Onigiri Ayam
            elif input == 'n':
                self.state = 'q15'
                self.output = 5  # Onigiri Tuna

        elif self.state == 'q10':
            if input == 'o':
                self.state = 'q16'
                self.output = 6  # Burger Ayam
            elif input == 'p':
                self.state = 'q17'
                self.output = 7  # Burger Sapi
            elif input == 'q':
                self.state = 'q18'
                self.output = 8  # Burger Babi
                
        elif self.state in ['q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18']:
            if input in 'g':
                self.state = 'q19'
            if input in 'r':
                self.state = 'q20'

        elif self.state == 'q19':
            if input == 'a':
                self.state = 'q20'
                self.output = self.output

        elif self.state == 'q20':
            if input == 'a':
                self.state = 'q1'
                self.output = self.output

    def display(self):
        if self.state == 'q0':
            print("Vending Machine")
            print(f"Saldo {self.balance}")
            print("Masukkan Uang 5000 > b")
            print("Masukkan Uang 10000 > c")
            print("Masukkan Uang 20000 > d")
            print("Masukkan Uang 50000 > t")
            print("Batalkan > e")

        elif self.state == 'q2':
            print("Vending Machine")
            print(f"Saldo {self.balance}")
            print("Masukkan Uang 5000 > b")
            print("Masukkan Uang 10000 > c")
            print("Batalkan > e")

        elif self.state == 'q3':
            print("Vending Machine")
            print(f"Saldo {self.balance}")
            print("Masukkan Uang 5000 > b")
            print("Masukkan Uang 10000 > c")
            print("Batalkan > e")

        elif self.state == 'q4':
            print("Vending Machine")
            print(f"Saldo {self.balance}")
            print("Masukkan Uang 5000 > b")
            print("Pilih Menu")
            print("Onigiri > i")
            print("Burger > h")
            print("Batalkan > e")

        elif self.state == 'q5':
            print("Vending Machine")
            print(f"Saldo {self.balance}")
            print("Pilih Menu")
            print("Nasi Kotak > f")
            print("Onigiri > i")
            print("Burger > h")
            print("Batalkan > e")

        elif self.state == 'q6':
            print("Vending Machine")
            print("Pembayaran Dibatalkan")
            print("Silahkan Ambil Uang Kembali")
            print("Terima Kasih Telah Menggunakan Kami")

        elif self.state == 'q7':
            print("Vending Machine")
            print(f"Saldo {self.balance}")
            print("Pilih Menu")
            print("Nasi Kotak > f")
            print("Onigiri > i")
            print("Burger > h")
            print("Batalkan > e")
            
        elif self.state == 'q21':
            print("Vending Machine")
            print("Silahkan Ambil Kembalian 30000")
            print("Pilih Menu")
            print("Nasi Kotak > f")
        
        elif self.state == 'q22':
            print("Vending Machine")
            print("Silahkan Ambil Kembalian 35000")
            print("Pilih Menu")
            print("Onigiri > i")
            print("Burger > h")
            
        elif self.state == 'q23':
            print("Vending Machine")
            print("Silahkan Ambil Kembalian 5000")
            print("Pilih Menu")
            print("Onigiri > i")
            print("Burger > h")

        elif self.state == 'q8':
            print("Vending Machine")
            print("Nasi Kotak")
            print("Pilih Menu")
            print("Nasi Ayam Kecap > j")
            print("Nasi Kari > k")
            print("Nasi Rendang > l")

        elif self.state == 'q9':
            print("Vending Machine")
            print("Onigiri Ayam")
            print("Pilih Menu")
            print("Onigiri Ayam > m")
            print("Onigiri Tuna > n")

        elif self.state == 'q10':
            print("Vending Machine")
            print("Burger")
            print("Pilih Menu")
            print("Burger Ayam > o")
            print("Burger Sapi > p")
            print("Burger Babi > q")

        elif self.state in ['q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18']:
            print("Vending Machine")
            if self.output == 1:
                print("Nasi Ayam Kecap")
            elif self.output == 2:
                print("Nasi Kari")
            elif self.output == 3:
                print("Nasi Rendang")
            elif self.output == 4:
                print("Onigiri Ayam")
            elif self.output == 5:
                print("Onigiri Tuna")
            elif self.output == 6:
                print("Burger Ayam")
            elif self.output == 7:
                print("Burger Sapi")
            elif self.output == 8:
                print("Burger Babi")
            print("Hangatkan > g")
            print("Tidak > r")

        elif self.state == 'q19':
            print("Vending Machine")
            if self.output == 1:
                print("Nasi Ayam Kecap")
            elif self.output == 2:
                print("Nasi Kari")
            elif self.output == 3:
                print("Nasi Rendang")
            elif self.output == 4:
                print("Onigiri Ayam")
            elif self.output == 5:
                print("Onigiri Tuna")
            elif self.output == 6:
                print("Burger Ayam")
            elif self.output == 7:
                print("Burger Sapi")
            elif self.output == 8:
                print("Burger Babi")
            print("mu sedang Dihangatkan")
            print("Lanjut > a")

        elif self.state == 'q20':
            print("Vending Machine")
            if self.output == 1:
                print("Silahkan ambil Nasi Ayam Kecap mu")
            elif self.output == 2:
                print("Silahkan ambil Nasi Kari mu")
            elif self.output == 3:
                print("Silahkan ambil Nasi Rendang mu")
            elif self.output == 4:
                print("Silahkan ambil Onigiri Ayam mu")
            elif self.output == 5:
                print("Silahkan ambil Onigiri Tuna mu")
            elif self.output == 6:
                print("Silahkan ambil Burger Ayam mu")
            elif self.output == 7:
                print("Silahkan ambil Burger Sapi mu")
            elif self.output == 8:
                print("Silahkan ambil Burger Babi mu")
            print("Terima Kasih Telah Menggunakan Kami")

    def run(self):
        while self.state != 'q1':
            self.display()
            user_input = input()
            self.input_transition(user_input)


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
