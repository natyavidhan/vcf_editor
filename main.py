import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("VCF Editor")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open VCF", command=self.open_vcf)
        self.file_menu.add_command(label="Save VCF", command=self.open_vcf)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Open CSV", command=self.open_csv)
        self.file_menu.add_command(label="Save CSV", command=self.open_csv)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.contact_list = tk.Listbox(self.root, width=40, height=10)
        self.contact_list.place(x=10, y=15, width=90, height=165)

        tk.Label(self.root, text="Name", anchor="e").place(x=115, y=15, width=60, height=15)
        self.name = tk.Entry(self.root)
        self.name.place(x=190, y=15, width=100, height=15)

        tk.Label(self.root, text="Nickname", anchor="e").place(x=115, y=40, width=60, height=15)
        self.nickname = tk.Entry(self.root)
        self.nickname.place(x=190, y=40, width=100, height=15)

        tk.Label(self.root, text="Phone", anchor="e").place(x=115, y=65, width=60, height=15)
        self.phone = tk.Entry(self.root)
        self.phone.place(x=190, y=65, width=100, height=15)

        tk.Label(self.root, text="Email", anchor="e").place(x=115, y=90, width=60, height=15)
        self.email = tk.Entry(self.root)
        self.email.place(x=190, y=90, width=100, height=15)

        tk.Label(self.root, text="Address", anchor="e").place(x=115, y=115, width=60, height=15)
        self.address = tk.Text(self.root)
        self.address.place(x=190, y=115, width=100, height=55)

    def open_vcf(self):
        pass

    def save_vcf(self):
        pass

    def open_csv(self):
        pass

    def save_csv(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()