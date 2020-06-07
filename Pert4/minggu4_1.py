# ====================================================================================================================
# CLASS (Object Oriented Programming/OOP)

# Class = Cetakan 

# Contoh 'Cetakan Hewan'
# class hewan:
    
#     # class attribute
#     spesies = 'kambing'

#     #instance attribute
#     def __init__(self,asal,bobot,usia):
#         self.asal = asal
#         self.bobot = bobot
#         self.usia = usia

# gaga = hewan('Garut', 40, 8)
# tutul = hewan('Tulungagung', 45, 7)

# mengakses 'class atribute'
# print(f'gaga adalah seekor {gaga.__class__.spesies}')
# print(f'tutul adalah seekor {tutul.__class__.spesies}')

# Cerita
# print('Gaga adalah seekor {g.spesies}. Tutul juga seekor {t.spesies}. Gaga berasal dari {g.asal}. Sedangkan Tutul berasal dari {t.asal}.'.format(g=gaga, t=tutul))

# print('Tahun ini, Tutul menginjak usia {t.usia} tahun. Lebih muda setahun dari usia Gaga ({g.usia} tahun'.format(g=gaga, t=tutul))

# print('Meskipun lebih muda, Tutul memiliki bobot lebih tinggi ({t.bobot} kg) daripada Gaga ({g.bobot} kg).'.format(g=gaga, t=tutul))

# ====================================================================================================================
# METHOD = function in class

# class hewan:
    
#     # class attribute
#     spesies = 'kambing'

#     #instance attribute
#     def __init__(self, nama, asal, bobot, usia):
#         self.name = nama
#         self.asal = asal
#         self.bobot = bobot
#         self.usia = usia

#     # instance METHOD/function
#     def makan(self, makanan):
#         return f'{self.name} sedang menikmati {makanan}.'

#     def sate(self):
#         tusuk_sate = self.bobot * 20
#         return f'{self.name} bisa diolah menjadi {tusuk_sate} tusuk sate'


# # Mengisi cetakan 'class'
# kambing_baru = hewan('Etawa', 'Garut', 45, 9)

# #uji coba methods
# print(kambing_baru.makan('Daun Pisang'))
# print(kambing_baru.sate())


#=========================================================================================================
# LATIHAN MEMBUAT CLASS CALCULATOR

# class calculator:
#     def tambah(self, x, y):
#         return x + y
#     def kurang(self, x, y):
#         return x - y
#     def kali (self,x ,y):
#         return x * y
#     def bagi(self, x, y):
#         return x / y
#     def pangkat(self, x, y):
#         return x ** y

# print(calculator().tambah(4,5))
# print(calculator().kurang(40,5))
# print(calculator().kali(2,7))
# print(calculator().bagi(40,8))
# print(calculator().pangkat(4,3))




#=========================================================================================================
# LATIHAN BUAT CALCULATOR STATISTIK
# BUATLAH CLASS YANG BERISI METHOD DENGAN FITUR:
# 1. MENGHITUNG NILAI MINIMUM DALAM LIST (tidak boleh pake built-in function spt min())
# 2. MENGHITUNG NILAI MAKSIMUM DALAM LIST (tidak boleh pake built-in function spt max())
# 3. MENGHITUNG PANJANG ANGGOTA DALAM LIST (tidak boleh pake built-in function spt len())
# 4. Mean
# 5. Standar Deviasi

data = [2, 3, 4, 5, 6, 7, 8, 8, 9, 21, 3, 2, 5, 4, 1, 5, 12]

import math

class statistik:

    def minimum(self, list):
        a = list[0]
        for i in list:
            if i < a:
                a=i
        return a
    

    def maksimum(self, list):
        a= list[0]
        for i in list:
            if i > a:
                a=i
        return a


    def panjang(self, list):
        a = 0
        for i in list:
            a += 1
        return a
    
    def mean(self, list):
        jumlah = 0
        n = 0
        for i in list:
            jumlah += i
        
        for i in list:
            n += 1
        return jumlah/n
    
    def SD(self, list):
        jumlah = 0
        n = 0
        for i in list:
            jumlah += i
        
        for i in list:
            n += 1

        list2 = []
        for i in list:
            list2.append(i-(jumlah/n))
        
        list_kuadrat = []
        for i in list2:
            list_kuadrat.append(i**2)
        
        sigma=0
        for i in list_kuadrat:
            sigma += i
        
        return math.sqrt(sigma/n)
        
    def std(self, list):  #Caranya mas kim
        jumlah = 0
        n = 0
        for i in list:
            jumlah += i
            n += 1
        ratarata = jumlah/n

        total = 0
        for i in list:
            total += (i-ratarata)**2

        return (total/n)**0.5



print(statistik().minimum(data))
print(statistik().maksimum(data))
print(statistik().panjang(data))
print(statistik().mean(data))
print(statistik().SD(data))
print(statistik().std(data))


