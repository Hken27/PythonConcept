def jumlahan(arr):
    jumlah = 0
    for num in arr:
        jumlah += num
    return jumlah
listku = [2, 5, 6, 7, 12]
hasil_sum = jumlahan(listku)
print(hasil_sum)