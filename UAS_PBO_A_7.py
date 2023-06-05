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
        self.root.configure(bg="sienna")  
        # mengatur warna latar belakang window
        self.textarea = tk.Text(root, undo=True, bg="ivory", fg="saddlebrown")
        # membuat area kosong yang dapat diisi dengan teks
        # dan mengatur warna latar belakang textarea dan warna teks)
        self.textarea.pack(expand=True, fill='both')
        # menentukan tata letak area text dengan tata letak pack
        self.create_buttons()
        # digunakan untuk memanggil def create_buttons

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="sienna")  
        # untuk membuat frame yang berisi tombol dan mengatur warna latar belakang button_frame dengan warna "sienna"
        button_frame.pack()
        # mengatur tata letak frame
        button_width = 10  
        # untuk mengatur lebar tombol menjadi 10
        new_button = tk.Button(button_frame, text="New", command=self.new_file, width=button_width, bg="burlywood", fg="white")  
        # menambah tombal "New" dan mengatur warna latar belakang menjadi "burlywood" dan warna teks tombol menjadi "white"
        new_button.pack(side=tk.LEFT, padx=5, pady=5)
        # untuk mengatur tata letak tombol "new"
        open_button = tk.Button(button_frame, text="Open", command=self.open_file, width=button_width, bg="burlywood", fg="white")  
        # menambah tombal "Open" dan mengatur warna latar belakang menjadi "burlywood" dan warna teks tombol menjadi "white"
        open_button.pack(side=tk.LEFT, padx=5, pady=5)
        # untuk mengatur tata letak tombol "open"
        save_button = tk.Button(button_frame, text="Save", command=self.save_file, width=button_width, bg="burlywood", fg="white")  
        # menambah tombal "Save" dan mengatur warna latar belakang menjadi "burlywood" dan warna teks tombol menjadi "white"
        save_button.pack(side=tk.LEFT, padx=5, pady=5)
        # untuk mengatur tata letak tombol "save"
        save_as_button = tk.Button(button_frame, text="Save As", command=self.save_file_as, width=button_width, bg="burlywood", fg="white")  
        # menambah tombal "Save As" dan mengatur warna latar belakang menjadi "burlywood" dan warna teks tombol menjadi "white"
        save_as_button.pack(side=tk.LEFT, padx=5, pady=5)
        # untuk mengatur tata letak tombol "save as"

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

