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

        self.map_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color=self.bg_color)
        self.map_frame.grid(row=0, column=0, sticky='nsew')
        self.map_widget = tkmapview.TkinterMapView(self.map_frame, corner_radius=30)
        self.map_widget.pack(fill='both', expand=True)
        self.map_widget.set_position(52.2, 21.0)
        self.map_widget.set_zoom(10)

        self.side_bar_frame = ctk.CTkFrame(self.root, fg_color=self.bg_color)
        self.side_bar_frame.grid(row=0, column=1, sticky='nsew')
        self.side_bar_frame.grid_rowconfigure(0, weight=0)
        self.side_bar_frame.grid_rowconfigure(1, weight=0)
        self.side_bar_frame.grid_rowconfigure(2, weight=1)
        self.side_bar_frame.grid_propagate(False)
        self.side_bar_frame.grid_columnconfigure(0, weight=1)

        self.bank_frame=ctk.CTkFrame(self.side_bar_frame, corner_radius=20, fg_color="#2F3A40", border_width=3,border_color="#4B5A5E")
        self.bank_frame.grid(row=0,column=0, padx=15,pady=(40,20), sticky='ew')
        self.bank_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.build_bank_list_frame()

        self.worker_frame = ctk.CTkFrame(self.side_bar_frame, corner_radius=20, fg_color="#2F3A40", border_width=3,border_color="#4B5A5E")
        self.worker_frame.grid(row=1, column=0, padx=15, pady=(20,0), sticky='ew')
        self.worker_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.build_workers_list_frame()

        self.user_window_button_frame= ctk.CTkFrame(self.side_bar_frame)
        self.user_window_button_frame.grid(row=2, column=0, padx=15, pady=20, sticky='ew')
        self.user_window_button_frame.grid_propagate(False)
        self.user_window_button_frame.configure(height=80)
        self.user_window_button_frame.grid_rowconfigure(0, weight=1)
        self.user_window_button_frame.grid_columnconfigure(0, weight=1)
        self.user_window_button_frame.configure(fg_color="transparent")

        self.build_user_window_button_frame()

    def build_bank_list_frame(self):
        self.bank_header=ctk.CTkFrame(self.bank_frame, fg_color="transparent")
        self.bank_header.grid(row=0, column=0, columnspan=5, padx=5, pady=20)
        self.bank_label=ctk.CTkLabel(self.bank_header, text='Bank List', font=('Montserrat', 24, 'bold'), fg_color="#2F3A40")
        self.bank_label.grid(row=0, column=0, padx=10)
        self.bank_search=ctk.CTkEntry(self.bank_header, placeholder_text="Search Bank", font=("Montserrat", 14, "bold"))
        self.bank_search.grid(row=0, column=1, padx=(30,2))
        self.bank_search_btn=ctk.CTkButton(self.bank_header, text='Go', width=25,height=25, font=('Montserrat', 18, 'bold'), fg_color="#0EA5A4", hover_color="#14B8A6")
        self.bank_search_btn.grid(row=0, column=2, padx=10)

        self.bank_listbox=ctk.CTkScrollableFrame(self.bank_frame, width=400, corner_radius=20, fg_color='#37474F')
        self.bank_listbox.grid(row=1,column=0, columnspan=5, padx=20)

        self.bank_add_btn=ctk.CTkButton(self.bank_frame, text="Add Bank", font=("Montserrat", 14, "bold"), width=130, fg_color="#2563EB",hover_color="#3B82F6", command=lambda: self.build_bank_form_window())
        self.bank_add_btn.grid(row=2, column=0, padx=10, pady=15)
        self.bank_details_btn=ctk.CTkButton(self.bank_frame, text="Details",font=("Montserrat", 14, "bold"),width=140, fg_color='#37474F', hover_color="#455A64")
        self.bank_details_btn.grid(row=2, column=1, padx=10, pady=15)
        self.bank_edit_btn=ctk.CTkButton(self.bank_frame, text="Edit",font=("Montserrat", 14, "bold"),width=140,fg_color='#D97706', hover_color="#F59E0B")
        self.bank_edit_btn.grid(row=2, column=2, padx=10,pady=15)

    def build_workers_list_frame(self):
        self.worker_label= ctk.CTkLabel(self.worker_frame, text="Worker List", font=('Montserrat', 24, 'bold'), fg_color="#2F3A40" )
        self.worker_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        self.worker_listbox=ctk.CTkScrollableFrame(self.worker_frame, width=400, corner_radius=20, fg_color='#37474F')
        self.worker_listbox.grid(row=1,column=0, columnspan=5, padx=20)

        self.worker_add_btn=ctk.CTkButton(self.worker_frame, text="Add Worker", font=("Montserrat", 14, "bold"), width=130, fg_color="#2563EB",hover_color="#3B82F6", command=lambda:self.build_worker_form())
        self.worker_add_btn.grid(row=2, column=0, padx=10, pady=15)
        self.worker_details_btn = ctk.CTkButton(self.worker_frame, text="Details",font=("Montserrat", 14, "bold"),width=140, fg_color='#37474F', hover_color="#455A64")
        self.worker_details_btn.grid(row=2, column=1, padx=10, pady=15)
        self.worker_edit_btn=ctk.CTkButton(self.worker_frame,text="Edit",font=("Montserrat", 14, "bold"),width=140,fg_color='#D97706', hover_color="#F59E0B")
        self.worker_edit_btn.grid(row=2, column=2, padx=10, pady=15)

    def build_user_window_button_frame(self):
        self.user_window_button=ctk.CTkButton(self.user_window_button_frame,text="Bank Users",font=("Montserrat", 18, "bold"),width=140,fg_color="#6366F1",hover_color = "#818CF8",corner_radius=50)
        self.user_window_button.grid(row=0, column=0, columnspan=5, padx=40, pady=15, sticky='nsew')

    #     self.user_label= ctk.CTkLabel(self.user_frame, text="User List", font=('Montserrat', 24, 'bold'), fg_color="#2F3A40" )
    #     self.user_label.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
    #
    #     self.user_listbox=ctk.CTkScrollableFrame(self.user_frame, width=400, corner_radius=20, fg_color='#37474F')
    #     self.user_listbox.grid(row=1,column=0, columnspan=5, padx=20)
    #
    #     self.user_add_btn=ctk.CTkButton(self.user_frame, text="Add User", font=("Montserrat", 14, "bold"), width=130, fg_color="#2563EB")
    #     self.user_add_btn.grid(row=2, column=0, padx=10, pady=15)
    #     self.user_details_btn = ctk.CTkButton(self.user_frame, text="Details",font=("Montserrat", 14, "bold"),width=140, fg_color='#37474F')
    #     self.user_details_btn.grid(row=2, column=1, padx=10, pady=15)
    #     self.user_edit_btn=ctk.CTkButton(self.user_frame,text="Edit",font=("Montserrat", 14, "bold"),width=140,fg_color='#D97706')
    #     self.user_edit_btn.grid(row=2, column=2, padx=10, pady=15)


    def build_bank_form_window(self):
        self.w_root = ctk.CTkToplevel(self.root)
        self.w_root.transient(self.root)
        self.w_root.grab_set()
        self.w_root.title("Add")
        self.w_root.configure(fg_color="#69797D")
        self.w_root.geometry("400x400")
        self.w_root.grid_rowconfigure(0, weight=1)
        self.w_root.grid_columnconfigure(0, weight=1)

        self.window_form_frame=ctk.CTkFrame(self.w_root, corner_radius=12)
        self.window_form_frame.grid(row=0, column=0, padx=15,pady=15, sticky='nsew')
        self.window_form_frame.grid_columnconfigure(1, weight=1)

        self.head= ctk.CTkLabel(self.window_form_frame, text="Add Bank", font=('Montserrat', 25, "bold")).grid(row=0, column=0, columnspan=2, pady=(10, 15))
        labels = ["Bank Name", "Bank Town", "Bank Street", "Bank Number", "Bank Logo"]
        for i, text in enumerate(labels, start=1):
            ctk.CTkLabel(self.window_form_frame,text=text,font=('Montserrat', 18, "bold"),anchor="w").grid(row=i, column=0, padx=(15,5), pady=5, sticky='w')

        self.entry_bank_name = ctk.CTkEntry(self.window_form_frame)
        self.entry_bank_town = ctk.CTkEntry(self.window_form_frame)
        self.entry_bank_street = ctk.CTkEntry(self.window_form_frame)
        self.entry_bank_number = ctk.CTkEntry(self.window_form_frame)
        self.entry_bank_logo = ctk.CTkEntry(self.window_form_frame)

        entries = [
            self.entry_bank_name,
            self.entry_bank_town,
            self.entry_bank_street,
            self.entry_bank_number,
            self.entry_bank_logo
        ]

        for i, entry in enumerate(entries, start=1):
            entry.grid(row=i, column=1, padx=15, pady=5, sticky='nsew')

        self.button_bank_save = ctk.CTkButton(self.window_form_frame,text="Save",font=('Montserrat', 20, "bold"),width=120,height=35)
        self.button_bank_save.grid(row=6, column=0, columnspan=2,padx=30,pady=25, sticky="nsew")



    def build_bank_details(self):
        self.fr_label(self.frame_bank_details, 'Bank Details',0,0,self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 0)

    def build_worker_list(self):
        self.fr_label(self.frame_worker_list, 'Worker List', 0,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 0)
        self.listbox_workers = Listbox(self.frame_worker_list)
        self.listbox_workers.grid(row=1, column=0)

    def build_worker_form(self):
        self.w_root = ctk.CTkToplevel(self.root)
        self.w_root.transient(self.root)
        self.w_root.grab_set()
        self.w_root.title("Add")
        self.w_root.configure(fg_color="#69797D")
        self.w_root.geometry("500x500")
        self.w_root.grid_rowconfigure(0, weight=1)
        self.w_root.grid_columnconfigure(0, weight=1)

        self.window_form_frame = ctk.CTkFrame(self.w_root, corner_radius=12)
        self.window_form_frame.grid(row=0, column=0, padx=15, pady=15, sticky='nsew')
        self.window_form_frame.grid_columnconfigure(1, weight=1)

        self.head = ctk.CTkLabel(self.window_form_frame, text="Add Worker", font=('Montserrat', 25, "bold")).grid(row=0,column=0,columnspan=2,pady=(10,15))
        labels = ["Name", "Surname", "Bank ID", "Town", "Street", "Number", "Photo"]
        for i, text in enumerate(labels, start=1):
            ctk.CTkLabel(self.window_form_frame, text=text, font=('Montserrat', 18, "bold"), anchor="w").grid(row=i,column=0,padx=(15,5),pady=5,sticky='w')

        self.entry_worker_name = ctk.CTkEntry(self.window_form_frame)
        self.entry_worker_surname = ctk.CTkEntry(self.window_form_frame)
        self.entry_worker_bank = ctk.CTkEntry(self.window_form_frame)
        self.entry_worker_town = ctk.CTkEntry(self.window_form_frame)
        self.entry_worker_role = ctk.CTkEntry(self.window_form_frame)
        self.entry_worker_street = ctk.CTkEntry(self.window_form_frame)
        self.entry_worker_number = ctk.CTkEntry(self.window_form_frame)
        self.entry_worker_photo = ctk.CTkEntry(self.window_form_frame)

        entries = [
            self.entry_worker_name,
            self.entry_worker_surname,
            self.entry_worker_bank,
            self.entry_worker_role,
            self.entry_worker_town,
            self.entry_worker_street,
            self.entry_worker_number,
            self.entry_worker_photo
        ]

        for i, entry in enumerate(entries, start=1):
            entry.grid(row=i, column=1, padx=15, pady=5, sticky='nsew')

        self.button_bank_save = ctk.CTkButton(self.window_form_frame, text="Save", font=('Montserrat', 20, "bold"),width=120, height=35)
        self.button_bank_save.grid(row=8, column=0, columnspan=2, padx=30, pady=25, sticky="nsew")

    def build_worker_details(self):
        self.fr_label(self.frame_worker_details, 'Worker Details', 0,0, self.f_name, self.f_size, 'bold', 1, 1, self.f_anch, 0)

    def build_user_window(self):
        self.w_root = ctk.CTkToplevel(self.root)
        self.w_root.transient(self.root)
        self.w_root.grab_set()
        self.w_root.title("Add")
        self.w_root.configure(fg_color="#69797D")
        self.w_root.geometry("500x500")

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