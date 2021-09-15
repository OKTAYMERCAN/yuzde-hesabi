#Yüzde hesaplama
i = 0
while i <= 1:
    print("X sayisinin %Y si kac?. (Cikmak için q yazin)")
    print("örn: X = 100 ve %Y = 10 ise SONUC: 10 dir.")
    value = float(input("X : "))
    yuzde = float(input("%Y : "))
    total = value / 100 * yuzde
    print("Sonuc: ", total)