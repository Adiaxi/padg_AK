from tkinter import *
import tkintermapview as tkmapview

#OSMNX BIBLIOTEKA SPRAWDZIĆ
#ROBIC COMMITY! ! !

class Login:
    def __init__(self):

        self.root = Tk()
        self.root.configure(background="#69797D")
        self.root.title("Logowanie")
        self.root.geometry("400x400")

        self.log_frame = Frame(self.root)
        self.log_frame.grid(column=0, row=0)

        self.build_login()
    #     self.log(str(input("Login: ")),str(input("Password: ")))
    #
    # def log(self,log:str,psswd:str):
    #     if  psswd == 'admin' and log == 'admin':
    #         app=AppView()
    #         app.run()
    #         self.run()

    def build_login(self):
        self.log_name=Label(self.log_frame,text="Login")
        self.log_psswd=Label(self.log_frame,text="Password")
        self.entry_name=Entry(self.log_frame)
        self.entry_psswd=Entry(self.log_frame)

        self.log_name.grid(column=0,row=0,padx=5,pady=5)
        self.log_psswd.grid(column=1,row=0,padx=5,pady=5)
        self.entry_name.grid(column=0,row=1)
        self.entry_psswd.grid(column=1,row=1)
        self.log_psswd.focus()

    def run(self):
         self.root.mainloop()



class AppView:
    def __init__(self):

        self.root = Tk()
        self.root.configure(background="#69797D")
        self.root.title("PADG Projekt")
        self.root.geometry("1920x1080")

        self.root.rowconfigure(1, weight=0)
        self.root.columnconfigure(3, weight=0)

        self.f_size: int = 10
        self.f_name: str = 'Segoe UI'
        self.f_anch: str = 'center'



    # BANK FRAMES
        self.frame_bank_list = Frame(self.root,borderwidth=3, relief="solid")
        self.frame_bank_details = Frame(self.root, bg="lightblue",borderwidth=3, relief="solid")
        self.frame_bank_form = Frame(self.root, borderwidth=3, relief="solid")

        self.frame_bank_list.grid(row=0, column=0, padx=(15,0), pady=(15,5), sticky='W')
        self.frame_bank_form.grid(row=0, column=1, sticky='W')
        self.frame_bank_details.grid(row=1, column=0, sticky='W', padx=(15,0))

        self.build_bank_list_frame()
        self.build_bank_form()
        self.build_bank_details()



    # WORKER FRAMES
        self.frame_worker_list = Frame(self.root, borderwidth=3, relief="solid")
        self.frame_worker_details = Frame(self.root, bg="lightblue", borderwidth=3, relief="solid")
        self.frame_worker_form = Frame(self.root, borderwidth=3, relief="solid")

        self.frame_worker_list.grid(row=0, column=2, padx=(100,0), pady=(15,0), sticky='W')
        self.frame_worker_form.grid(row=0, column=3, sticky='W')
        self.frame_worker_details.grid(row=1, column=2, padx=(100,15), sticky='W')

        self.build_worker_list()
        self.build_worker_form()
        self.build_worker_details()


        # ZROBIC TAK ABY FORMULARZ DODAWNIA SIE WYSWIETLAL JAKO DODATKOWE OKIENKO A NIE WSZYSTKO W JEDNYM ! ! ! !


        # MAP FRAME
        self.map_frame=Frame(self.root, borderwidth=10, relief="sunken")
        self.map_frame.grid(row=2,column=0, pady=(20,0), columnspan=5)
        self.map_widget=tkmapview.TkinterMapView(self.map_frame, width=1506, height=455, corner_radius=0)
        self.map_widget.grid(row=0, column=0, sticky="")
        self.map_widget.set_position(deg_x=52.2, deg_y=21.0)
        self.map_widget.set_zoom(14)

        self.build_map()

    def fr_label(self,fr, t: str, r: int, col: int, f1:str, f2:int, f3:str, x:int, y:int, anch:str, en:int):
        from tkinter import Label
        import os
        temp = Label(fr, text=t, font=(f1,f2,f3), padx=x, pady=y, anchor=anch)
        if en == 0:
            temp.grid(row=r, column=col)
        else:
            temp.grid(row=r, column=col, sticky='W')

        return temp

    def f_b(self, f, t:str, wid:int,h:int):
        temp=Button(f, text=t, width=wid, height=h)
        return temp


    def build_bank_list_frame(self):
        self.fr_label(self.frame_bank_list, 'Bank List',0,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 0)
        self.listbox_banks = Listbox(self.frame_bank_list)
        self.listbox_banks.grid(row=1, column=0)

        self.button_bank_details= self.f_b(self.frame_bank_list, 'Show details', 10, 1)
        self.button_bank_edit= self.f_b(self.frame_bank_list, 'Edit', 10, 1)
        self.button_bank_details.grid(row=2, column=0, pady=10, sticky='W')
        self.button_bank_edit.grid(row=2, column=1, pady=10, sticky='W')

    def build_bank_form(self):
        self.fr_label(self.frame_bank_form, 'Bank Name',1,0, self.f_name, self.f_size,  'bold', 1, 1, self.f_anch,1)
        self.fr_label(self.frame_bank_form, 'Bank Town',2,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch,1)
        self.fr_label(self.frame_bank_form, 'Bank Street',3,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch,1)
        self.fr_label(self.frame_bank_form, 'Bank Number',4,0, self.f_name, self.f_size,'bold', 1, 1, self.f_anch,1)
        self.fr_label(self.frame_bank_form, 'Bank Logo',5,0, self.f_name, self.f_size,'bold', 1, 1, self.f_anch,1)

        self.entry_bank_name=Entry(self.frame_bank_form)
        self.entry_bank_town=Entry(self.frame_bank_form)
        self.entry_bank_street=Entry(self.frame_bank_form)
        self.entry_bank_number=Entry(self.frame_bank_form)
        self.entry_bank_logo=Entry(self.frame_bank_form)

        self.entry_bank_name.grid(row=1, column=1)
        self.entry_bank_town.grid(row=2, column=1)
        self.entry_bank_street.grid(row=3, column=1)
        self.entry_bank_number.grid(row=4, column=1)
        self.entry_bank_logo.grid(row=5, column=1)

        self.button_bank_save= self.f_b(self.frame_bank_form, 'Save', 15, 2)
        self.button_bank_save.grid(row=6, column=1,pady=10, sticky='W')


    def build_bank_details(self):
        self.fr_label(self.frame_bank_details, 'Bank Details',0,0,self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 0)

    def build_worker_list(self):
        self.fr_label(self.frame_worker_list, 'Worker List', 0,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 0)
        self.listbox_workers = Listbox(self.frame_worker_list)
        self.listbox_workers.grid(row=1, column=0)

    def build_worker_form(self):
        self.fr_label(self.frame_worker_form, 'Worker Name',1,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1 )
        self.fr_label(self.frame_worker_form, 'Worker Surname', 2,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)
        self.fr_label(self.frame_worker_form, 'Worker Town', 3,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)
        self.fr_label(self.frame_worker_form, 'Worker Street', 4,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)
        self.fr_label(self.frame_worker_form, 'Worker Home Numb', 5,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)
        self.fr_label(self.frame_worker_form, 'Worker IMG', 6,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)

        self.entry_worker_name = Entry(self.frame_worker_form)
        self.entry_worker_surname = Entry(self.frame_worker_form)
        self.entry_worker_town = Entry(self.frame_worker_form)
        self.entry_worker_street = Entry(self.frame_worker_form)
        self.entry_worker_home_number = Entry(self.frame_worker_form)
        self.entry_worker_img = Entry(self.frame_worker_form)

        self.entry_worker_name.grid(row=1, column=1)
        self.entry_worker_surname.grid(row=2, column=1)
        self.entry_worker_town.grid(row=3, column=1)
        self.entry_worker_street.grid(row=4, column=1)
        self.entry_worker_home_number.grid(row=5, column=1)
        self.entry_worker_img.grid(row=6, column=1)

    def build_worker_details(self):
        self.fr_label(self.frame_worker_details, 'Worker Details', 0,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 0)

    def build_map(self):
        self.map_menu=Label(self.map_frame, text='MENU')
        self.map_menu.grid(row=0, column=0, columnspan=5, sticky='N')

        self.map_find_button=self.f_b(self.map_menu, 'Find Bank', 10,2)
        self.map_find_button.grid(row=0,column=0)
        self.map_search_button=self.f_b(self.map_menu, 'Search Address', 14,2)
        self.map_search_button.grid(row=0,column=1)
        self.map_dark_button=self.f_b(self.map_menu, 'Dark Mode', 10,2)
        self.map_dark_button.grid(row=0,column=2)


    def run(self):
        self.root.mainloop()