# List of dictionary
items = [
    {'namapemain': 'joao pedro', 'stok': 1, 'harga': 70000000},
    {'namapemain': 'palmer', 'stok': 1, 'harga': 230000000},
    {'namapemain': 'felix', 'stok': 1, 'harga': 50000000},
    {'namapemain': 'sanchez', 'stok': 1, 'harga': 30000000},
    {'namapemain': 'malo gusto', 'stok': 1, 'harga': 40000000}
]

# Fungsi untuk menambahkan item ke list of dictionary
def create(namapemain, stok, harga):
    new_item = {'namapemain': namapemain, 'stok': stok, 'harga': harga}
    items.append(new_item)

# Menampilkan isi dari list of dictionary
def display_items():
    for item in items:
        print(f"NamaPemain: {item['namapemain']}, Stok: {item['stok']}, Harga: {item['harga']}")

# Menambahkan item baru
create('enzo', 1, 120000000)

# Menampilkan semua item
display_items()
