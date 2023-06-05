import tkinter as tk                                                                    # UAS PBO 
# untuk mengimport modul tkinter                                                        # Kelompok 8
# pemanggilan modul menggunakan alias tk                                                # Nama Anggota :
from tkinter import filedialog                                                          # 1. Sophina Shafa Salsabila    (G1A022021)
# memanggil fungsi filediolog dari modul tkinter                                        # 2. Hanif Abdullah Zuhdi       (G1A022041)
                                                                                        # 3. Arief Setiawan             (G1A022055) 
class Notepad:
# membuat kelas Nodepad
    def __init__(self, root):
    # konstruktor yang dipanggil saat objek kelas dibuat dengan parameter root
        self.root = root 
        # membuat atribut root dari parameter root
        self.root.title("Notepad")
        # membuat judul window
        self.textarea = tk.Text(root, undo=True)
        # membuat area kosong yang dapat diisi dengan teks
        self.textarea.pack(expand=True, fill='both')
        # menentukan tata letak area text dengan tata letak pack
        self.create_menu()
        # digunakan untuk memanggil def create_menu

    def create_menu(self):
    # fungsi yang digunakan untuk membuat menu utama pada aplikasi
        menubar = tk.Menu(self.root)
        # untuk membuat objek menu pada tampilan
        file_menu = tk.Menu(menubar, tearoff=0)
        # untuk membuat objek menubar dengan nama file_menu pada tampilan
        file_menu.add_command(label="New", command=self.new_file)
        # membuat menu 'new' pada objek file_menu yang akan mengarah pada fungsi new_file
        file_menu.add_command(label="Open", command=self.open_file)
        # membuat menu 'open' pada objek file_menu yang akan mengarah pada fungsi open_file
        file_menu.add_command(label="Save", command=self.save_file)
        # membuat menu 'save' pada objek file_menu yang akan mengarah pada fungsi save_file
        file_menu.add_command(label="Save As", command=self.save_file_as)
        # membuat menu 'save as' pada objek file_menu yang akan mengarah pada fungsi save_file_as
        file_menu.add_separator()
        # untuk memisahkan objek selanjutnya dengan objek sebelumnya
        file_menu.add_command(label="Exit", command=self.root.quit)
        # membuat menu 'exit' pada objek file_menu yang akan menghentikan program
        menubar.add_cascade(label="File", menu=file_menu)
        # menambah sub objek menu pada menubar

        edit_menu = tk.Menu(menubar, tearoff=0)
        # untuk membuat objek menubar baru dengan nama edit_menu
        edit_menu.add_command(label="Undo", command=self.textarea.edit_undo)
        # membuat menu 'undo' pada objek edit_menu yang akan menjalankan undo pada textarea
        menubar.add_cascade(label="Edit", menu=edit_menu)
        # menambah sub objek menu pada menubar

        self.root.config(menu=menubar)
        # mengkonfigurasi objek menubar sebagai menu utama pada objek root

    def new_file(self):
    # fungsi yang digunakan untuk menampilkan textarea baru
        self.textarea.delete("1.0", tk.END)
        # menghapus isi pada textarea dengan '1.0' menunjukan posisi awal dan tk.END menunjukkan posisi akhir

    def open_file(self):
    # fungsi yang digunakan untuk membuka file note
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        # akan diarahkan pada file explorer dengan menampilkan pilihan Open untuk data yang sesuai format
        if file_path:
        # kondisi yang memeriksa apakah terdapat nilai yang sesuai pada file_path
            with open(file_path, "r") as file:
            # untuk membaca file text. Parameter "r"  menunjukkan bahwa file akan dibuka dalam mode baca
                content = file.read()
                # untuk membaca seluruh isi file dan menyimpannya ke dalam variabel 'content'
            self.textarea.delete("1.0", tk.END)
            # untuk menghapus semua teks yang ada di dalam self.textarea sebelum mengisinya dengan isi file yang baru
            self.textarea.insert(tk.END, content)
            # untuk memasukkan teks baru ke dalam textarea

    def save_file(self):
    # fungsi yang digunakan untuk menyimpan file note
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        # akan diarahkan pada file explorer dengan menampilkan pilihan Save untuk menyimpan data dengan format .txt
        if file_path:
        # kondisi yang memeriksa apakah terdapat nilai yang sesuai pada file_path
            content = self.textarea.get("1.0", tk.END)
            # untuk menggambil seluruh teks pada textarea dari baris pertama(1.0) hingga akhir(tk.END)
            with open(file_path, "w") as file:
            # untuk membuka file yang dipilih dalam metode "write"
            # penggunaan with digunakan untuk memastikan bahwa file akan ditutup dengan benar setelah selesai digunakan
                file.write(content)
                # untuk meenulis isi teks yang disimpan dalam variabel content ke dalam file yang telah dibuka
                # isi teks akan ditulis ke dalam file

    def save_file_as(self):
    #fungsi yang digunakan untuk menyimpan file note
        file_path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        # akan diarahkan pada file explorer dengan menampilkan pilihan Save untuk menyimpan data dengan format yang diminta.
        if file_path:
        # kondisi yang memeriksa apakah terdapat nilai yang sesuai pada file_path
            content = self.textarea.get("1.0", tk.END)
            # untuk menggambil seluruh teks pada textarea dari baris pertama(1.0) hingga akhir(tk.END)
            with open(file_path, "w") as file:
            # untuk membuka file yang dipilih dalam metode "write"
            # penggunaan with digunakan untuk memastikan bahwa file akan ditutup dengan benar setelah selesai digunakan
                file.write(content)
                # untuk meenulis isi teks yang disimpan dalam variabel content ke dalam file yang telah dibuka
                # isi teks akan ditulis ke dalam file

root = tk.Tk()
# membuat objek Tkinter root sebagai window utama aplikasi
notepad = Notepad(root)
# membuat objek notepad untuk menjalankan kelas Notepad
root.mainloop()
# untuk memulai siklus utama program yang dijalankan

