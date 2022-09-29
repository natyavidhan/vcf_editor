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
        self.file_menu.add_command(label="Open", command=self.open_vcf)
        self.file_menu.add_command(label="Save", command=self.save_vcf)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        self.csv_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="CSV", menu=self.csv_menu)
        self.csv_menu.add_command(label="Open CSV", command=self.open_csv)
        self.csv_menu.add_command(label="Save CSV", command=self.open_csv)

        self.contact_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Contact", menu=self.contact_menu)
        self.contact_menu.add_command(label="Add Contact", command=self.add_contact)
        self.contact_menu.add_command(label="Delete Contact", command=self.delete_contact)

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
    
    def parse_vcf(self, contact:str):
        contact = contact.split("\n")
        c = {}
        for line in contact:
            if line.startswith("N:") or line.startswith("FN:"):
                c["name"] = line.replace("N:", "")
            elif line.startswith("TITLE:"):
                c["nickname"] = line.replace("TITLE:", "")
            elif line.startswith("TEL;TYPE=CELL:"):
                c["phone"] = line.replace("TEL;TYPE=CELL:", "")
            elif line.startswith("EMAIL:"):
                c["email"] = line.replace("EMAIL:", "")
            elif line.startswith("ADR;TYPE#WORK,PREF:;;"):
                c["address"] = line.replace("ADR;TYPE#WORK,PREF:;;", "")
        return c
    
    def gen_vcf(self, contact:dict):
        contact['address'] = contact['address'].replace("\n", "\\n")
        c = f"BEGIN:VCARD\nVERSION:3.0\nN:{contact['name']}\nFN:{contact['name']}\nTITLE:{contact['nickname']}\nTEL;TYPE=CELL:{contact['phone']}\nEMAIL:{contact['email']}\nADR;TYPE#WORK,PREF:;;{contact['address']}\nEND:VCARD"
        return c

    def open_vcf(self):
        pass

    def save_vcf(self):
        pass

    def open_csv(self):
        pass

    def save_csv(self):
        pass

    def add_contact(self):
        pass

    def delete_contact(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()