from tkinter import *
import tkintermapview as tkmapview
import customtkinter as ctk


#OSMNX BIBLIOTEKA SPRAWDZIĆ
#ROBIC COMMITY! ! !

class Login:
    def __init__(self):

        self.root = ctk.CTk()
        self.root.configure(background="#69797D")
        self.root.title("Login")
        self.root.geometry("400x350")

        self.log_frame = Frame(self.root)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.log_frame.grid(column=0, row=0)


        self.build_login()

    def log(self,log:str,psswd:str):
        if  psswd == 'admin' and log == 'admin':
            self.root.destroy()
            app=AppView()
            app.run()

    def build_login(self):
        self.log_name=Label(self.log_frame,text="Login", font=("Segoe UI", 14, 'bold'))
        self.log_psswd=Label(self.log_frame,text="Password",font=("Segoe UI", 14, 'bold'))
        self.entry_name=Entry(self.log_frame)

        self.pswd_button = Button(self.log_frame, text="See", command=lambda: self.pswd())
        self.pswd_button.grid(column=2,row=1, padx=5, pady=5)
        self.entry_pswd=Entry(self.log_frame, show='*')

        self.log_name.grid(column=0,row=0,padx=10,pady=10,sticky='W')
        self.log_psswd.grid(column=1,row=0,padx=10,pady=10,sticky="W")
        self.entry_name.grid(column=0,row=1,padx=10,pady=10)
        self.entry_pswd.grid(column=1,row=1,padx=10,pady=10)

        self.log_button=Button(self.log_frame,text='Login', command=lambda: self.log(self.entry_name.get(),self.entry_pswd.get()))
        self.log_button.grid(column=0,row=2,padx=10,pady=10,sticky='W')

    def pswd(self):
        if self.entry_pswd.cget("show")=='*':
            self.entry_pswd.config(show='')

        elif self.entry_pswd.cget("show")=='':
            self.entry_pswd.config(show='*')
    def run(self):
         self.root.mainloop()



class AppView:
    def __init__(self):

        self.bg_color: str = "#1F2933"

        self.root = ctk.CTk()
        self.root.configure(fg_color=self.bg_color)
        self.root.title("PADG Projekt")
        self.root.geometry("1600x900")


        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=7)
        self.root.grid_columnconfigure(1, weight=3)


    # MAP FRAME
        self.map_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color=self.bg_color)
        self.map_frame.grid(row=0, column=0, sticky='nsew')
        self.map_widget = tkmapview.TkinterMapView(self.map_frame, corner_radius=30)
        self.map_widget.pack(fill='both', expand=True)
        self.map_widget.set_position(52.2, 21.0)
        self.map_widget.set_zoom(10)



    # BANK FRAMES

        self.side_bar_frame = ctk.CTkFrame(self.root, fg_color=self.bg_color)
        self.side_bar_frame.grid(row=0, column=1, sticky='nsew')
        self.side_bar_frame.grid_propagate(False)
        self.side_bar_frame.grid_columnconfigure(0, weight=1)

        self.bank_frame=ctk.CTkFrame(self.side_bar_frame, corner_radius=20, fg_color="#2F3A40", border_width=3,border_color="#4B5A5E")
        self.bank_frame.grid(row=0,column=0, padx=15,pady=15, sticky='ew')
        self.bank_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.build_bank_list_frame()

        self.worker_frame = ctk.CTkFrame(self.side_bar_frame, corner_radius=20, fg_color="#2F3A40", border_width=3,border_color="#4B5A5E")
        self.worker_frame.grid(row=1, column=0, padx=15, pady=15, sticky='ew')
        self.worker_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.build_workers_list_frame()



        # self.frame_bank_list = Frame(self.root,borderwidth=3, relief="solid")
        # self.frame_bank_details = Frame(self.root, bg="lightblue",borderwidth=3, relief="solid")
        # self.frame_bank_form = Frame(self.root, borderwidth=3, relief="solid")
        # self.frame_button_list = Frame(self.frame_bank_list)
        #
        # self.frame_bank_list.grid(row=0, column=0, padx=(50,0), pady=(15,5), sticky='W')
        # self.frame_bank_form.grid(row=0, column=1, sticky='W')
        # self.frame_bank_details.grid(row=1, column=0, sticky='W', padx=(15,0))
        # self.frame_button_list.grid(row=1, column=1, sticky='W')
        #
        # self.build_bank_list_frame()
        # self.build_bank_details()



    # # WORKER FRAMES
    #     self.frame_worker_list = Frame(self.root, borderwidth=3, relief="solid")
    #     self.frame_worker_details = Frame(self.root, bg="lightblue", borderwidth=3, relief="solid")
    #     self.frame_worker_form = Frame(self.root, borderwidth=3, relief="solid")
    #
    #     self.frame_worker_list.grid(row=0, column=2, padx=(100,0), pady=(15,0), sticky='W')
    #     self.frame_worker_form.grid(row=0, column=3, sticky='W')
    #     self.frame_worker_details.grid(row=1, column=2, padx=(100,15), sticky='W')
    #
    #     self.build_worker_list()
    #     self.build_worker_form()
    #     self.build_worker_details()





       # self.build_map()

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
        self.bank_label=ctk.CTkLabel(self.bank_frame, text='Bank List', font=('Montserrat', 24, 'bold'), fg_color="#2F3A40")
        self.bank_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.bank_listbox=ctk.CTkScrollableFrame(self.bank_frame, width=400, corner_radius=20, fg_color='#37474F')
        self.bank_listbox.grid(row=1,column=0, columnspan=5, padx=20)

        self.bank_add_btn=ctk.CTkButton(self.bank_frame, text="Add Bank", font=("Montserrat", 14, "bold"), width=130, fg_color="#2563EB")
        self.bank_add_btn.grid(row=2, column=0, padx=10, pady=15)
        self.bank_details_btn=ctk.CTkButton(self.bank_frame, text="Details",font=("Montserrat", 14, "bold"),width=140, fg_color='#37474F')
        self.bank_details_btn.grid(row=2, column=1, padx=10, pady=15)
        self.bank_edit_btn=ctk.CTkButton(self.bank_frame, text="Edit",font=("Montserrat", 14, "bold"),width=140,fg_color='#D97706')
        self.bank_edit_btn.grid(row=2, column=2, padx=10,pady=15)

    def build_workers_list_frame(self):
        self.worker_frame= ctk.CTkLabel(self.worker_frame, text="Worker List", font=('Montserrat', 24, 'bold'), fg_color="#2F3A40" )
        self.worker_frame.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.worker_listbox=ctk.CTkScrollableFrame(self.worker_frame, width=400, corner_radius=20, fg_color='#37474F')
        self.worker_listbox.grid(row=1,column=0, columnspan=5, padx=20)

        self.worker_add_btn=ctk.CTkButton(self.worker_frame, text="Add Worker", font=("Montserrat", 14, "bold"), width=130, fg_color="#2563EB")
        self.worker_add_btn.grid(row=2, column=0, padx=10, pady=15)
        self.worker_details_btn = ctk.CTkButton(self.worker_frame, text="Details",font=("Montserrat", 14, "bold"),width=140, fg_color='#37474F')
        self.worker_details_btn.grid(row=2, column=1, padx=10, pady=15)
        self.worker_edit_btn=ctk.CTkButton(self.worker_frame,text="Edit",font=("Montserrat", 14, "bold"),width=140,fg_color='#D97706')
        self.worker_edit_btn.grid(row=2, column=2, padx=10, pady=15)

    def new_window(self):
        self.new_root = ctk.CTk()
        self.new_root.title("BANK APP")
        self.new_root.geometry("400x400")

        self.new_root.mainloop()

    def build_form_window(self):
        self.w_root = Toplevel(self.root)
        self.w_root.configure(background="#69797D")
        self.w_root.title("Add")
        self.w_root.geometry("400x400")

        self.w_root.grid_rowconfigure(0, weight=1)
        self.w_root.grid_columnconfigure(0, weight=1)

        self.window_form_frame=Frame(self.w_root, borderwidth=3, relief="solid")
        self.window_form_frame.grid(row=0, column=0, padx=15,pady=15)

        self.head=self.fr_label(self.window_form_frame, 'Add Bank', 0, 0, self.f_name, 15, 'bold', 60, 1, 'center', 1)
        self.fr_label(self.window_form_frame, 'Bank Name', 1, 0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)
        self.fr_label(self.window_form_frame, 'Bank Town', 2, 0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)
        self.fr_label(self.window_form_frame, 'Bank Street', 3, 0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)
        self.fr_label(self.window_form_frame, 'Bank Number', 4, 0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)
        self.fr_label(self.window_form_frame, 'Bank Logo', 5, 0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 1)

        self.entry_bank_name = Entry(self.window_form_frame)
        self.entry_bank_town = Entry(self.window_form_frame)
        self.entry_bank_street = Entry(self.window_form_frame)
        self.entry_bank_number = Entry(self.window_form_frame)
        self.entry_bank_logo = Entry(self.window_form_frame)

        self.entry_bank_name.grid(row=1, column=1)
        self.entry_bank_town.grid(row=2, column=1)
        self.entry_bank_street.grid(row=3, column=1)
        self.entry_bank_number.grid(row=4, column=1)
        self.entry_bank_logo.grid(row=5, column=1)

        self.button_bank_save = self.f_b(self.window_form_frame, 'Save', 15, 2)
        self.button_bank_save.grid(row=6, column=1, pady=10, sticky='W')



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
        self.map_menu = Frame(self.map_frame)
        Label(self.map_menu, text="MENU").grid(row=0, column=0)
        self.map_menu.grid(row=0, column=0, sticky='N')

        self.map_find_button=self.f_b(self.map_menu, 'Find Bank', 10,2)
        self.map_find_button.grid(row=0,column=0)
        self.map_search_button=self.f_b(self.map_menu, 'Search Address', 14,2)
        self.map_search_button.grid(row=0,column=1)
        self.map_dark_button=self.f_b(self.map_menu, 'Dark Mode', 10,2)
        self.map_dark_button.grid(row=0,column=2)


    def run(self):
        self.root.mainloop()