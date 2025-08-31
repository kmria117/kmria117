class kalkulator():
    def __init__(self,angka1,angka2):
        self.angka1=angka1
        self.angka2=angka2
    def add(self):
        return self.angka1 + self.angka2

    def subtract(self):
        return self.angka1 - self.angka2
    
    def multiply (self): 
        return self.angka1 * self.angka2
    
    def divide (self):
        if self.angka1 ==0:
            return "error:pembagi dengan 0"
        return self.angka1 / self.angka2

while True:
    print("\n === Kalkulator sederhana ===",
          "\n Pilih operasi",
          "\n 1. +",
          "\n 2. -",
          "\n 3. *",
          "\n 4. /")
    op = input( "Masukkan pilihan anda:" )
    a=float(input("masukan angka pertama:"))
    b=float(input("masukan angka kedua:"))
    mask=kalkulator(a, b)  
    if  op == "+":
        hasil=mask.add()
    elif  op == "-":
        hasil=mask.subtract()
    elif  op == "*":
        hasil=mask.multiply()
    elif  op == "/":
        hasil=mask.divide()
    else: 
        print("operasi tidak valid")
    print("hasil", hasil)
          
          
          

