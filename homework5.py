birinchi_yol = float(input("1-sidan 1 kunda necha kilo metir yugurganini kiritin: "))
ikkinchi_yol = float(input("2-sidan 1 kunda necha kilo metir yugurganini kiritin: "))

# Birinchi yo'lin 10% ga qo'shilgan masofani hisoblash
birinchi_yol += birinchi_yol * 0.1

# Nechi kunda yetib borishini hisoblash
kunlar_soni = 0
while birinchi_yol < ikkinchi_yol:
    birinchi_yol += birinchi_yol * 0.1
    kunlar_soni += 1

# Natijani chiqarish
print(f"{kunlar_soni} kunda birinchi yo'l ikkinchi yo'lni {ikkinchi_yol} kilo metrga yetib borgan.")

