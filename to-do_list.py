todo_list = []

def show_tasks():
    if not todo_list:
        print("Belum ada tugas.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task(task):
    todo_list.append(task)
    print("Tugas berhasil ditambahkan.")

def delete_task(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index - 1)
        print(f"Tugas dihapus: {removed}")
    else:
        print("Nomor tugas tidak valid.")

while True:
    print("\n=== To-Do List ===")
    print("1. Lihat Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    choice = input("Pilih opsi (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Masukkan tugas: ")
        add_task(task)
    elif choice == '3':
        show_tasks()
        try:
            idx = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            delete_task(idx)
        except ValueError:
            print("Harap masukkan angka yang valid.")
    elif choice == '4':
        print("Sampai jumpa!")
        break
    else:
        print("Opsi tidak valid.")
