#Tugas-1 No. 3
a = float(input("Nilai Ujian Teori:"))
b = float(input("Nilai Ujian Praktek:"))
if a >= 70 and b >= 70:
      print("Selamat, anda lulus!")
if a >= 70 and b < 70:
      print("Anda harus mengulang ujian praktek.")
if a < 70 and b >= 70:
      print("Anda harus mengulang ujian teori.")
if a < 70 and b < 70:
      print("Anda harus mengulang ujian teori dan praktek.")