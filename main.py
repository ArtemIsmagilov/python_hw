from tkinter import *
from tkinter import filedialog
import shelve, sys, os, time, _tkinter


def importing():
    pass


def exporting():
    pass


class App():
    frames = list()

    def __init__(self):
        self.flag = True
        self.db = shelve.open('students')
        print(list(self.db.items()))
        self.root = Tk()
        self.root.geometry('600x400')

        self.f = Frame()
        self.f.pack()

        self.btn1 = Button(self.f, text='Add', command=self.adding)
        self.btn2 = Button(self.f, text='Change', command=self.changing)
        self.btn3 = Button(self.f, text='Delete', command=self.deleting)

        self.btn4 = Button(self.f, text='Import', command=self.importing)
        self.btn5 = Button(self.f, text='Export', command=self.exporting)

        [b.pack(side=LEFT) for b in (self.btn1, self.btn2, self.btn3, self.btn4, self.btn5)]

        self.root.iconbitmap(r'open-book.ico')
        self.root.mainloop()
        self.root.mainloop()

    def create_window(self):
        [f.destroy() for f in App.frames]
        self.f1 = Frame()
        self.f2 = Frame()
        self.f3 = Frame()
        self.f4 = Frame()

        [f.pack() for f in (self.f1, self.f2, self.f3, self.f4)]

        App.frames = [self.f1, self.f2, self.f3, self.f4]

    def adding(self, text="Add new user and number"):
        def add_db():
            name, number = self.entry_name.get(), self.entry_number.get()
            if name and number and name not in self.db:
                self.db[name] = number
                self.get_messange('Success. You add new number phone and name', 'spring green')
            elif name in self.db:
                self.get_messange(
                    'This name already exists. Please add a new name or change the phone number by clicking `change`',
                    'tan1')
            else:
                self.get_messange('You add empty number phone or name', 'tan1')

        self.create_window()

        self.lbl_name = Label(self.f1, text="Name: ", font='Times 13')
        self.entry_name = Entry(self.f1, font='Times 13')
        self.lbl_number = Label(self.f2, text="Number phone: ", font='Times 13')
        self.entry_number = Entry(self.f2, font='Times 13')

        self.lbl_name.pack(side=LEFT)
        self.entry_name.pack(side=RIGHT)
        self.lbl_number.pack(side=LEFT)
        self.entry_number.pack(side=RIGHT)

        self.btn_enter = Button(self.f3, text=text, command=add_db)
        self.btn_enter.pack()

    def changing(self, text="Replace user and number"):
        def change_db():
            name, number = self.entry_name.get(), self.entry_number.get()
            if name and number and name in self.db:
                self.db[name] = number
                self.get_messange('Success. This user exists. You change number phone and name', 'spring green')
            else:
                self.get_messange('There is no such user. Please click `add` and insert new user', 'tan1')

        self.create_window()

        self.lbl_name = Label(self.f1, text="Name: ", font='Times 13')
        self.entry_name = Entry(self.f1, font='Times 13')
        self.lbl_number = Label(self.f2, text="Number phone: ", font='Times 13')
        self.entry_number = Entry(self.f2, font='Times 13')

        self.lbl_name.pack(side=LEFT)
        self.entry_name.pack(side=RIGHT)
        self.lbl_number.pack(side=LEFT)
        self.entry_number.pack(side=RIGHT)

        self.btn_enter = Button(self.f3, text=text, command=change_db)
        self.btn_enter.pack()

    def deleting(self):

        def delete_db():
            nonlocal del_nums
            old_del_nums = del_nums.copy()
            if not del_nums:
                self.get_messange('Empty database. Nothing to delete', 'tan1')
            else:
                for key, d, ch in del_nums:
                    if d.get():
                        ch.destroy()
                        old_del_nums.remove((key, d, ch))
                        self.db.pop(str(key))

                if old_del_nums == del_nums:
                    self.get_messange('You have not selected the entries to delete', 'yellow')
                else:
                    self.get_messange('Success. You delete names and numbers phone', 'spring green')
            del_nums = old_del_nums

        self.create_window()

        del_nums = list()
        for i, k in enumerate(self.db):
            var1 = IntVar()
            ch = Checkbutton(self.f1, text=f'{i}) {k} - {self.db[str(k)]}', font='Times 15', variable=var1)
            ch.pack(anchor=W)
            del_nums.append((k, var1, ch))

        self.btn_enter = Button(self.f2, text="Delete selected users and numbers", font='Times 13', command=delete_db)

        self.btn_enter.pack()

    def importing(self):
        self.create_window()

        filename = filedialog.askopenfilename()
        ext = os.path.splitext(filename)[-1]
        print(filename)
        if ext == '.txt':
            with open(filename) as f:
                self.db.clear()
                result = str()
                count = 0
                for line in f:
                    count += 1
                try:
                    usr, phone = line.split(' ', 1)
                    phone = phone.rstrip()
                    if usr and phone:
                        result += f'{count}) {usr} - {phone}\n'
                        self.db[usr] = phone.rstrip()
                    else:
                        return self.get_messange(self.f4, 'Empty values name or phone. Try to fix the file.')
                except:
                    self.get_messange(self.f4, 'Mistake format text.')
                Message(self.f1, text=result, width=400, font='Times 15').pack()
                self.get_messange('Success. Import completed', 'spring green')
        elif ext:
            return self.get_messange(
                f'Not correct extention for GUI. Please, use extention - `.txt`. Your extetion - `{ext}`', 'yellow')
        else:
            return self.get_messange('Exit from Import mode', 'orange')

    def exporting(self):
        self.create_window()

        result = str()
        for k in self.db:
            u, n = k, self.db[k]
            result += '%s %s\n' % (u, n)

        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if f is None:
            return self.get_messange('Exit from Export mode.', 'orange')
        else:
            f.write(result)
            f.close()
        return self.get_messange(f'To end of file export - {f.name}', 'spring green')

    def get_messange(self, text, color):
        Message(self.f4, text=text, width=400, font='Times 15', bg=color).pack(side=TOP)
        self.f4.after(2000, self.f4.destroy)
        self.f4 = Frame()
        self.f4.pack()


if __name__ == '__main__':
    App()







