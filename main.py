import tkinter as tk
from tkinter import filedialog

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
        self.csv_menu.add_command(label="Save CSV", command=self.save_csv)

        self.contact_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Contact", menu=self.contact_menu)
        self.contact_menu.add_command(label="Add Contact", command=self.add_contact)
        self.contact_menu.add_command(label="Save Contact", command=self.save_contact)
        self.contact_menu.add_command(label="Delete Contact", command=self.delete_contact)

        self.contact_list = tk.Listbox(self.root, width=40, height=10)
        self.contact_list.place(x=10, y=15, width=90, height=165)
        self.contact_list.bind("<<ListboxSelect>>", self.select_contact)

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

        self.contacts = []
        self.last_opened = None
    
    def parse_vcf(self, contact:str):
        contact = contact.split("\n")
        c = {}
        for line in contact:
            if line.startswith("N:") or line.startswith("FN:"):
                c['name'] = "".join(line.split(":")[1])
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
        c = f"BEGIN:VCARD\nVERSION:3.0\nN:{contact['name']}\nFN:{contact['name']}\nTITLE:{contact['nickname']}\nTEL;TYPE=CELL:{contact['phone']}\nEMAIL:{contact['email']}\nADR;TYPE#WORK,PREF:;;{contact['address']}\nEND:VCARD\n"
        return c

    def open_vcf(self):
        file = filedialog.askopenfilename(filetypes=[("VCF Files", "*.vcf")])
        if file:
            with open(file, "r") as f:
                contacts = f.read().split("BEGIN:VCARD")
            self.contacts = []
            for contact in contacts:
                if contact:
                    self.contacts.append(self.parse_vcf(contact))
            self.load_contacts()

    def save_vcf(self):
        file = filedialog.asksaveasfilename(filetypes=[("VCF Files", "*.vcf")])
        if file:
            with open(file, "w") as f:
                for contact in self.contacts:
                    f.write(self.gen_vcf(contact))

    def open_csv(self):
        file = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file:
            with open(file, "r") as f:
                contacts = f.read().split("\n")
            self.contacts = []
            for contact in contacts:
                if contact:
                    try:
                        name, phone, nickname, email, address = contact.split(",")
                        self.contacts.append({"name":name, "nickname":nickname, "phone":phone, "email":email, "address":address})
                    except:
                        try:
                            name, phone, nickname, email = contact.split(",")
                            self.contacts.append({"name":name, "nickname":nickname, "phone":phone, "email":email})
                        except:
                            try:
                                name, phone, nickname = contact.split(",")
                                self.contacts.append({"name":name, "nickname":nickname, "phone":phone})
                            except:
                                try:
                                    name, phone = contact.split(",")
                                    self.contacts.append({"name":name, "phone":phone})
                                except:
                                    pass
            self.load_contacts()

    def save_csv(self):
        file = filedialog.asksaveasfilename(filetypes=[("CSV Files", "*.csv")])
        if file:
            with open(file, "w") as f:
                for contact in self.contacts:
                    s = ""
                    s+=contact['name']+","
                    s+=contact['phone']+","
                    try:
                        s+=contact['nickname']+","
                    except:
                        s+=","
                    try:
                        s+=contact['email']+","
                    except:
                        s+=","
                    try:
                        s+=contact['address']
                    except:
                        pass
                    f.write(s+"\n")

    def add_contact(self):
        self.contacts.append({"name":"","nickname":"","phone":"","email":"","address":""})
        self.load_contacts()
    
    def save_contact(self):
        index = self.last_opened
        self.contacts[index]["name"] = self.name.get()
        self.contacts[index]["nickname"] = self.nickname.get()
        self.contacts[index]["phone"] = self.phone.get()
        self.contacts[index]["email"] = self.email.get()
        self.contacts[index]["address"] = self.address.get("1.0", "end-1c")
    
    def select_contact(self, event):
        index = self.contact_list.curselection()[0]
        self.last_opened = index
        self.name.delete(0, "end")
        self.name.insert(0, self.contacts[index]["name"])
        try:
            self.nickname.delete(0, "end")
            self.nickname.insert(0, self.contacts[index]["nickname"])
        except:
            pass
        self.phone.delete(0, "end")
        self.phone.insert(0, self.contacts[index]["phone"])
        try:
            self.email.delete(0, "end")
            self.email.insert(0, self.contacts[index]["email"])
        except:
            pass
        try:
            self.address.delete("1.0", "end")
            self.address.insert("1.0", self.contacts[index]["address"])
        except:
            pass

    def delete_contact(self):
        self.contacts.pop(self.last_opened)
        self.load_contacts()

    def load_contacts(self):
        self.contact_list.delete(0, tk.END)
        for contact in self.contacts:
            self.contact_list.insert(tk.END, contact["name"])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()