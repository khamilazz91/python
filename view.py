
import tkinter as tk
from tkinter import ttk

class View(tk.Tk):

    PAD = 15


    def __init__(self, controller):
        super().__init__()

        self.title('Tkinter CRUD')
        self.controller = controller
        #self.protocol("WM_DELETE_WINDOW", self.controller.on_click_btn_x)
        self._make_main_frame()
        self._make_tab_create() 
        self._make_tab_update()
        self.protocol("WM_DELETE_WINDOW", self.controller.on_click_btn_x)
        
    def main(self):
        self.mainloop()      

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
    
    def _make_tab_create(self):
        self.notebook = ttk.Notebook(self)
        self.tab_create = tk.Frame(self.notebook)
        self.notebook.add(self.tab_create, text="Create") 
        self.notebook.pack(expand=1, fill="both")
        
        self.label_id_create = tk.Label(self.tab_create ,text = 'ID: ')
        self.label_id_create.pack()
        self.entry_id_create = tk.Entry(self.tab_create)
        self.entry_id_create.pack()

        self.label_name_create = tk.Label(self.tab_create ,text = 'Name: ')
        self.label_name_create.pack()
        self.entry_name_create = tk.Entry(self.tab_create)
        self.entry_name_create.pack()

        self.label_lastname_create = tk.Label(self.tab_create ,text = 'Lastname: ')
        self.label_lastname_create.pack()
        self.entry_lastname_create = tk.Entry(self.tab_create)
        self.entry_lastname_create.pack()

        self.label_phone_create = tk.Label(self.tab_create ,text = 'Phone: ')
        self.label_phone_create.pack()
        self.entry_phone_create = tk.Entry(self.tab_create)
        self.entry_phone_create.pack()

        self.label_adress_create = tk.Label(self.tab_create ,text = 'Adress: ')
        self.label_adress_create.pack()
        self.entry_adress_create = tk.Entry(self.tab_create)
        self.entry_adress_create.pack()

        self.btnAdd_create = ttk.Button(self.tab_create, text = 'Add Person', command = self.controller.on_click_create)
        self.btnAdd_create.pack()

        self.btnPrinting = ttk.Button(self.tab_create, text = 'Printing', command = self.controller.on_click_btn_printing)
        self.btnPrinting.pack()

        ################################## TAB UPDATE #######################################
    def _make_tab_update(self):
        self.tab_update = tk.Frame(self.notebook)
        self.notebook.add(self.tab_update, text="Modify")
        self.notebook.bind('<Button-1>', self.controller.on_click_tab_update)
        self.notebook.pack(expand=1, fill="both")
        self.label_id_update = tk.Label(self.tab_update ,text = 'ID: ')
        self.label_id_update.pack()
        self.entry_id_update = tk.Entry(self.tab_update, text = '')
        self.entry_id_update.config(state = 'disable')
        self.entry_id_update.pack()

        self.label_name_update = tk.Label(self.tab_update ,text = 'Name: ')
        self.label_name_update.pack()
        self.entry_name_update = tk.Entry(self.tab_update)
        self.entry_name_update.pack()

        self.label_lastname_update = tk.Label(self.tab_update ,text = 'Lastname: ')
        self.label_lastname_update.pack()
        self.entry_lastname_update = tk.Entry(self.tab_update)
        self.entry_lastname_update.pack()

        self.label_phone_update = tk.Label(self.tab_update ,text = 'Phone: ')
        self.label_phone_update.pack()
        self.entry_phone_update = tk.Entry(self.tab_update)
        self.entry_phone_update.pack()

        self.label_adress_update = tk.Label(self.tab_update ,text = 'Adress: ')
        self.label_adress_update.pack()
        self.entry_adress_update = tk.Entry(self.tab_update)
        self.entry_adress_update.pack()

        self.btnUpdate = ttk.Button(self.tab_update, text = 'Update', command = self.controller.on_click_btn_update_person)
        self.btnUpdate.pack()

        self.btnDelete = ttk.Button(self.tab_update, text = 'Delete Person', command = self.controller.on_click_btn_delete_person)
        self.btnDelete.pack()

        # Treeview Update
        self.tree_update = ttk.Treeview(self.tab_update, height = 10, columns=1)
        self.tree_update['columns'] = ('name', 'lastname', 'phone', 'adress')
        self.tree_update.heading('#0', text='ID')
        self.tree_update.column('#0')
        self.tree_update.heading('#1', text='Name')
        self.tree_update.heading('#2', text='Lastname')
        self.tree_update.heading('#3', text='Phone')
        self.tree_update.heading('#4', text='Adress')
        self.tree_update.bind("<Double-1>", self.controller.double_click_treeview) # Double_Click Event Function
        self.tree_update.pack()

