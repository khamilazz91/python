import psycopg2 
import psycopg2.extras
import pprint
import sys
from tkinter import BOTH, END, LEFT
from tkinter import messagebox as msbox



#connect to database
try:
    conn = psycopg2.connect(host = "localhost",
                                database="person", 
                                user = "postgres", 
                                password = "postgresql")

    cursor = conn.cursor()

    class Model:

        def __init__(self):
            '''Constructor'''

        def run_query(query, parameters = ()):
            with psycopg2.connect(database="person", user = "postgres", password = "postgresql") as conn:
                cursor = conn.cursor()
                result = cursor.execute(query, parameters)
                conn.commit()
            return result

        ################################### CREATE FUNCTION ############################################

        def create_person(self):               
            query = 'INSERT INTO person VALUES(%s, %s, %s, %s, %s)'
            parameters = self.view.entry_id_create.get(), str(self.view.entry_name_create.get()), str(self.view.entry_lastname_create.get()), str(self.view.entry_phone_create.get()), str(self.view.entry_adress_create.get())
            self.model.run_query(query, parameters)
            msbox.showinfo('Information',"""The record {} added Successfully""".format(str(self.view.entry_name_create.get()))) 
            self.view.entry_id_create.delete(0, END)
            self.view.entry_name_create.delete(0, END)
            self.view.entry_lastname_create.delete(0, END)
            self.view.entry_phone_create.delete(0, END)
            self.view.entry_adress_create.delete(0, END) 

        ############################ LIST FUNCTION TREEVIEW CREATE FUNCTION #############################

        def list_person(self):
            #Cleaning table
            records = self.view.tree_update.get_children()
            for element in records:
                self.view.tree_update.delete(element)

            #Quering data
            with psycopg2.connect(database="person", user = "postgres", password = "postgresql") as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM person ORDER BY id ASC')
                rows = cursor.fetchall()

                cont = 1  # Counter representing the ID of your code.
                for row in rows:
                    self.view.tree_update.insert('', 'end', text=str(cont), values=(row[1], row[2], row[3], row[4]))
                    cont += 1 # Increment the ID

        ############################## LOAD EVENT DATA IN TREEVIEW  UPDATE AUTOMATICALLY ###########################

        def on_click_tab_update(self, event):
            self.list_person()

        ############################## DOUBLE CLICK EVENT FUNCTION LOAD DATA IN A ENTRIES #################################  

        def double_click(self):
            #Cleaning duplicate information
            self.view.entry_id_update.config(state = 'normal')
            self.view.entry_id_update.delete(0, END)
            self.view.entry_id_update.config(state = 'disable')
            self.view.entry_name_update.delete(0, END)
            self.view.entry_lastname_update.delete(0, END)
            self.view.entry_phone_update.delete(0, END)
            self.view.entry_adress_update.delete(0, END)

            #Updating onformation
            self.view.entry_id_update.config(state = 'normal')
            self.view.entry_id_update.pack()
            self.view.entry_id_update.insert("end", self.view.tree_update.item(self.view.tree_update.selection())['text'])
            self.view.entry_name_update.insert("1", self.view.tree_update.item(self.view.tree_update.selection())['values'][0])   
            self.view.entry_lastname_update.insert("2", self.view.tree_update.item(self.view.tree_update.selection())['values'][1])   
            self.view.entry_phone_update.insert("3", self.view.tree_update.item(self.view.tree_update.selection())['values'][2])   
            self.view.entry_adress_update.insert("4", self.view.tree_update.item(self.view.tree_update.selection())['values'][3]) 
            self.view.entry_id_update.config(state = 'disable')
            self.view.entry_id_update.pack()

        ################################### UPDATE FUNCTION #########################################
            
        def update_person(self):
            query_update = """UPDATE person SET name = %s, lastname = %s, phone = %s, adress = %s where id = %s"""
            id = 0
            name = self.view.entry_name_update.get()
            lastname = self.view.entry_lastname_update.get()
            phone = self.view.entry_phone_update.get()
            adress = self.view.entry_adress_update.get()
            id = self.view.entry_id_update.get()
            self.model.run_query(query_update, (name, lastname, phone, adress, id))
            self.view.entry_id_update.config(state = 'normal')
            self.view.entry_id_update.delete(0, END)
            self.view.entry_id_update.config(state = 'disable')
            self.view.entry_name_update.delete(0, END)
            self.view.entry_lastname_update.delete(0, END)
            self.view.entry_phone_update.delete(0, END)
            self.view.entry_adress_update.delete(0, END)
            msbox.showinfo('Information', """The record {} has been Update Successfully""".format(str(name))) 
            self.model.list_person(self)

        ################################### DELETE FUNCTION #########################################

        def delete_person(self):             
            record = self.view.tree_update.item(self.view.tree_update.selection())['values'][0]
            query_delete = 'DELETE FROM person WHERE name = %s'
            self.model.run_query(query_delete, (record,))
            msbox.showinfo('Information','Person {} as deleted Successfully'.format(record))
            self.model.list_person(self)
            self.view.entry_id_update.config(state = 'normal')
            self.view.entry_id_update.delete(0, END)
            self.view.entry_id_update.config(state = 'disable')
            self.view.entry_name_update.delete(0, END)
            self.view.entry_lastname_update.delete(0, END)
            self.view.entry_phone_update.delete(0, END)
            self.view.entry_adress_update.delete(0, END)

        ################################## EXIT TKINTER FUNCTION #####################################

        def exit(self):
            if msbox.askokcancel("Quit", "Do you really wish to quit?"):
                self.view.destroy()

        ################################## LOAD ID AUTOMATICALLY #####################################
        
        def load_id(self):
            with psycopg2.connect(database="person", user = "postgres", password = "postgresql") as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT id FROM person ORDER BY id DESC LIMIT 1')
                datas = cursor.fetchone()
                data = int(datas[0])
                self.view.entry_id_create.insert(0, data+1)
                self.view.entry_id_create.config(state = 'disable')

                
            



except (Exception, psycopg2.Error) as error:
    print("Error in Query ", error)
    conn = psycopg2.connect(host = "localhost",
                                database="person", 
                                user = "postgres", 
                                password = "postgresql")

    cursor = conn.cursor()
    
finally:
    # Closing database connection.
    if (conn):
        cursor.close()
        conn.close()
        print("Your code compiled successfully")