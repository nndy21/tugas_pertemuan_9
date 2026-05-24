# Program Array Sederhana

data = ["durian", "apel", "rambutan", "melon", "jeruk"]

print("Data awal:", data)

# tambahkan elemen
data.append("durian")
print("Setelah append:", data)

# hapus elemen
data.remove("apel")
print("Setelah remove apel:", data)

# akses index
print("Index ke-1:", data[1])
print("Index terakhir:", data[-1])

# panjang array
print("Jumlah elemen:", len(data))

# looping
print("\nIsi array:")
for i, item in enumerate(data):
    print(f"  {i}. {item}")

# sorting
data.sort()
print("\nSetelah di-sort:", data)

# slicing
print("Slice [1:3]:", data[1:3])
