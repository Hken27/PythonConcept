# data list campuran
random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

int_dict = {}  # Untuk menyimpan data int dalam bentuk dictionary
float_tuple = ()  # Untuk menyimpan data float dalam bentuk tuple
string_list = []  # Untuk menyimpan data string dalam bentuk list

for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100

        # Menyimpan data int dalam dictionary
        int_dict[item] = {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}
    elif isinstance(item, float):
        # Menyimpan data float dalam tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Menyimpan data string dalam list
        string_list.append(item)

# Mencetak hasil
print("Data int: ")
print(int_dict)
print("\nData float: ")
print(float_tuple)
print("\nData string: ")
print(string_list)


