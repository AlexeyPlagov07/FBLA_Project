import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
import base64
import pypyodbc as odbc
#Initalizing Login Page#
main = tk.Tk()
main.title("Login Page")
main.geometry("500x500")
main.configure(bg="cornflowerblue")
#Initializing Variables#
user_var_login = tk.StringVar()
pass_var_login = tk.StringVar()
pass1_signup = tk.StringVar()
pass2_signup = tk.StringVar()
user_signup = tk.StringVar()
user_perm = tk.StringVar()
selected = tk.StringVar()
new_p_name = tk.StringVar()
new_p_purpose = tk.StringVar()
new_p_ps = tk.StringVar()
new_p_relation = tk.StringVar()
new_p_contact = tk.StringVar()
p_delete = tk.StringVar()
product_var = tk.StringVar()
service_var = tk.StringVar()
hardware_var = tk.StringVar()
financial_var = tk.StringVar()
info_var = tk.StringVar()
filter_ps_list = ['product', 'service']
filter_ps_dict = {'product':product_var, 'service':service_var}
filter_purpose_list = ['hardware', 'financial', 'info']
filter_purpose_dict = {'hardware':hardware_var, 'financial':financial_var, 'info':info_var}
############################


#cursor.execute("CREATE TABLE partner_info (Name TEXT, organization_type TEXT, product_service TEXT, available_resource TEXT, contact_info TEXT)")
#cursor.execute("CREATE TABLE users (Username TEXT, Password TEXT, role TEXT)")

#cursor.execute("INSERT INTO partner_info VALUES ('Automation Direct', 'product provider', 'product', 'hardware', '770-844-4200')")
#conn.commit()

DRIVER_NAME = 'SQL SERVER'

SERVER_NAME = 'DESKTOP-GGC1QRG\SQL_SERVER'

DATABASE_NAME = 'FBLA_PROJECT'

connection_string = f"""
  DRIVER={{{DRIVER_NAME}}};
  SERVER={{{SERVER_NAME}}};
  DATABASE={{{DATABASE_NAME}}};
  Trust_Connection=yes;
"""

conn = odbc.connect(connection_string)
cursor = conn.cursor()



def base64_encode_return(x):
  b64set = (x).encode("ascii")
  base64_bytes = base64.b64encode(b64set) 
  base64_string = base64_bytes.decode("ascii") 
  return base64_string

def base64_decode_return(x):
  decoded_string = base64.b64decode(x).decode('utf-8')
  return decoded_string
#role_update_query = ("UPDATE FBLA_PROJECT.odb.users SET role='admin' WHERE Username = (?)")
#cursor.execute(role_update_query, (base64_encode_return("Alexey"),))
#conn.commit()

def base64_encode(x):
  b64set = (x.get()).encode("ascii")
  base64_bytes = base64.b64encode(b64set) 
  base64_string = base64_bytes.decode("ascii") 
  x.set(base64_string)
#Creates Sign Up Window and includes all related functions#
def sign_up():
  
  sign_up_window = tk.Toplevel()
  sign_up_window.title("Sign Up")
  sign_up_window.geometry("300x150")
  sign_up_window.configure(bg='powderblue')
  #Sees if passwords are the same when asked to re-enter the password#
  def sign_up_check():
    
    
    if pass1_signup.get() == pass2_signup.get():
      base64_encode(user_signup)
      base64_encode(pass1_signup)
      name_list = []
      cursor.execute("SELECT Username FROM FBLA_PROJECT.odb.users")
      result1 = cursor.fetchall()
      #returns all created usernames in a list#
      for i in result1:
        name_list.append(list(i)[0])
      #checks if attempted username is in list.
      if user_signup.get() not in name_list:
        
        sign_up_window.withdraw()
        messagebox.showinfo("Sign Up", "Sign Up Successful!")
        info111 = "INSERT INTO users VALUES (?,?,?)"
        
        
        cursor.execute(info111, (user_signup.get(),pass1_signup.get(),"user"))
        conn.commit()
      
        user_signup.set("")
        pass1_signup.set("")
        pass2_signup.set("")
      else:
        messagebox.showerror("Sign Up", "Username Already Exists!")
        user_signup.set("")
        pass1_signup.set("")
        pass2_signup.set("")
    else:
      messagebox.showerror("Sign Up", "Passwords Don't Match!")
      user_signup.set("")
      pass1_signup.set("")
      pass2_signup.set("")
  #Labels, Entries, and Buttons for the Sign Up Page#
  user_label2 = tk.Label(sign_up_window, text="Username", bg="powderblue").place(relx=0.2, rely=0.2, anchor=CENTER)
  password_label2 = tk.Label(sign_up_window, text="Password", bg="powderblue").place(relx=0.2, rely=0.38, anchor=CENTER)
  password_label3 = tk.Label(sign_up_window, text="Re-Enter", bg="powderblue").place(relx=0.2, rely=0.56, anchor=CENTER)
  ue2 = tk.Entry(sign_up_window, textvariable=user_signup).place(relx=0.6, rely=0.2, anchor=CENTER)
  pe2 = tk.Entry(sign_up_window, textvariable=(pass1_signup)).place(relx=0.6, rely=0.38, anchor=CENTER)
  pe3 = tk.Entry(sign_up_window, textvariable=pass2_signup).place(relx=0.6, rely=0.56, anchor=CENTER)
  sub2 = tk.Button(sign_up_window, text="Sign Up", command=lambda: [sign_up_check()]).place(relx=0.6, rely=0.80, anchor=CENTER)

#Clears Login entry-so when they logout, the data inputed doesn't save#
def clear_login_entry():
  user_var_login.set("")
  pass_var_login.set("")
def user_list():
  user_list = []
  cursor.execute("SELECT Username FROM FBLA_PROJECT.odb.users")
  user_result = cursor.fetchall()
  for i in user_result:
    user_list.append(list(i)[0])
  return user_list
def admin_test():
  
  if base64_encode_return(user_var_login.get()) in user_list():
  
    query3 = ("SELECT * FROM FBLA_PROJECT.odb.users WHERE Username =(?)")
    cursor.execute(query3, (base64_encode_return(user_var_login.get()),))
    login_result = cursor.fetchone()
    user_perm.set(str((list(login_result))[2]))

#Login Labels#
user_label = tk.Label(main, text="Username", bg='cornflowerblue').place(relx=0.26, rely=0.3, anchor=CENTER)
pass_label = tk.Label(main, text="Password", bg='cornflowerblue').place(relx=0.26, rely=0.35, anchor=CENTER)
#Login Page Entries and Button#
ue1 = tk.Entry(main, textvariable=user_var_login).place(relx=0.5, rely=0.3, anchor=CENTER)
pe1 = tk.Entry(main, textvariable=pass_var_login).place(relx=0.5, rely=0.35, anchor=CENTER)
lib1 = tk.Button(main, text='Login', command=lambda: [admin_test(), data_window(), clear_login_entry()]).place(relx=0.435, rely=0.4)
sub1 = tk.Button(main, text="Sign Up", command=sign_up).place(relx=0.421, rely=0.47)
#Window with data and sorting options#




def partner_list():
  partner_list = []
  cursor.execute("SELECT Name FROM FBLA_PROJECT.odb.partners")
  partner_result = cursor.fetchall()
  for i in partner_result:
    partner_list.append(list(i)[0])
  return partner_list

def data_window():

  
  
  def view_users():
    
    def role_change():
      selected_users = []
      for i in user_listbox.curselection():
        selected_users.append((user_listbox.get(i)).split())
      for i in selected_users:
        if i[2] == "admin":
          admin_role_change = "UPDATE FBLA_PROJECT.odb.users SET role='user' WHERE Username = (?)"
          cursor.execute(admin_role_change, (base64_encode_return(i[0]),))
          conn.commit()
        elif i[2] == "user":
          user_role_change = "UPDATE FBLA_PROJECT.odb.users SET role='admin' WHERE Username = (?)"
          cursor.execute(user_role_change, (base64_encode_return(i[0]),))
          conn.commit()
    def user_list_update():
      user_listbox.delete(0, END)
      cursor.execute("SELECT * FROM FBLA_PROJECT.odb.users WHERE role='admin'")
      user1_result = list(cursor.fetchall())
      cursor.execute("SELECT * FROM FBLA_PROJECT.odb.users WHERE role='user'")
      user2_result = list(cursor.fetchall())
      user3_result = user1_result + user2_result
      for i in range(len(user3_result)):
        j = (list(user3_result))[i]
        user_info = (base64_decode_return(j[0]) + " | " + j[2])
        user_listbox.insert(END, user_info)
        
    user_window = tk.Toplevel()
    user_window.title("Users")
    user_window.geometry("300x300")
    user_window.configure(bg='powderblue')
    tk.Label(user_window, text="User |  Role", bg='powderblue').place(relx=0.25, rely=0.1, anchor=CENTER)
    user_scrollbar = tk.Scrollbar(user_window)
    user_listbox = tk.Listbox(user_window, width=30, height=10, selectmode=MULTIPLE)
    user_scrollbar.place(relx=0.5, rely=0.5, anchor=CENTER)
    user_listbox.place(relx=0.5, rely=0.4, anchor=CENTER)
    user_listbox.config(yscrollcommand = scrollbar.set)
    user_scrollbar.config(command = listbox.yview)
    user_list_update()
    role_change1 = tk.Button(user_window, text="Change Role", command=lambda: [role_change(), user_list_update()]).place(relx=0.5, rely=0.8, anchor=CENTER)
    
  
  def update_listbox():
    listbox.delete(0,END)
    cursor.execute("SELECT * FROM FBLA_PROJECT.odb.partners")
    result21 = list(cursor.fetchall())
    for i in range(len(result21)):
      j = list(result21[i])
      info121 = (j[0] + " | " + j[1] + " | " + j[2] + " | " + j[3] + " | " + j[4])
      listbox.insert(END, info121)
  def add_partner():

    if new_p_name.get() not in partner_list():
      add_query = "INSERT INTO partners VALUES (?,?,?,?,?)"
      cursor.execute(add_query, (new_p_name.get(), new_p_purpose.get(), new_p_ps.get(), new_p_relation.get(), new_p_contact.get()))
      conn.commit()
      new_p_name.set("")
      new_p_purpose.set("")
      new_p_ps.set("")
      new_p_relation.set("")
      new_p_contact.set("")

      messagebox.showinfo("Success!", "Your New Partner Has Been Saved!")
    else:
      messagebox.showerror("Error", "Partner Already In System!")
  def add_window():
    add_window = tk.Toplevel()
    add_window.title("Add To List")
    add_window.geometry("300x250")
    add_window.configure(bg="powderblue")
    p_name1 = tk.Label(add_window, text="Partner Name", bg="powderblue").place(relx=0.2, rely=0.1, anchor=CENTER)
    p_purpose1 = tk.Label(add_window, text="Partner Purpose", bg="powderblue").place(relx=0.2, rely=0.2, anchor=CENTER)
    p_ps1 = tk.Label(add_window, text="Product/Service", bg="powderblue").place(relx=0.2, rely=0.3, anchor=CENTER)
    p_relation1 = tk.Label(add_window, text="Partner Relation", bg="powderblue").place(relx=0.2, rely=0.4, anchor=CENTER)
    p_contact1 = tk.Label(add_window, text="Partner Contact", bg="powderblue").place(relx=0.2, rely=0.5, anchor=CENTER)
    p_name = tk.Entry(add_window, textvariable=new_p_name).place(relx=0.7, rely=0.1, anchor=CENTER)
    p_purpose = tk.Entry(add_window, textvariable=new_p_purpose).place(relx=0.7, rely=0.2, anchor=CENTER)
    p_ps= tk.Entry(add_window, textvariable=new_p_ps).place(relx=0.7, rely=0.3, anchor=CENTER)
    p_relation = tk.Entry(add_window, textvariable=new_p_relation).place(relx=0.7, rely=0.4, anchor=CENTER)
    p_contact = tk.Entry(add_window, textvariable=new_p_contact).place(relx=0.7, rely=0.5, anchor=CENTER)
    new_p_submit = tk.Button(add_window, text="Add Partner", command = lambda: [add_partner(),add_window.withdraw(), update_listbox()]).place(relx=0.5, rely=0.7, anchor=S)




  def delete_partner():
    if p_delete.get() in partner_list():
      delete_query = ("DELETE FROM FBLA_PROJECT.odb.partners WHERE Name=(?)")
      cursor.execute(delete_query, (p_delete.get(),))
      conn.commit()
      p_delete.set("")
    else:
      messagebox.showerror("Error", "Partner is not in system!")
  def delete_window():
    delete_window = tk.Toplevel()
    delete_window.title("Delete From List")
    delete_window.geometry("300x100")
    delete_window.configure(bg="powderblue")
    p_del = tk.Label(delete_window, text="Enter Partner Name to Delete", bg="powderblue").place(relx=0.5, rely=0.2, anchor=CENTER)
    p_delete1 = tk.Entry(delete_window, textvariable=p_delete).place(relx=0.5, rely=0.5, anchor=CENTER)
    p_del_button = tk.Button(delete_window, text="Delete Partner", command =lambda: [delete_partner(), delete_window.withdraw(), update_listbox()]).place(relx=0.5, rely=0.8, anchor=CENTER)
  
    
  def apply_ps_filter():
    temp_filter_list = []
    final_list = []
    temp_filter_result = []
    for i in filter_ps_list:
      if (filter_ps_dict[i]).get() == 'True':
        temp_filter_list.append(i)

    filter_query = "SELECT * FROM FBLA_PROJECT.odb.partners WHERE product_service = (?)"
    for i in temp_filter_list:
      cursor.execute(filter_query, (str(i),))
      temp_filter_result.append(cursor.fetchall())
    listbox.delete(0,END)
    for i in temp_filter_result:
      for j in i:
        if j != []:
  
          h = list(j)
          filter_listbox_result = (h[0] + " | " + h[1] + " | " + h[2] + " | " + h[3] + " | " + h[4])
          final_list.append(filter_listbox_result)
    return final_list
  
  
  
  def apply_purpose_filter():
    temp_filter_list = []
    temp_filter_result = []
    final_list = []
    for i in filter_purpose_list:
      
      if (filter_purpose_dict[i]).get() == 'True':
        temp_filter_list.append(i)
    filter_query = "SELECT * FROM FBLA_PROJECT.odb.partners WHERE available_resource = (?)"
    for i in temp_filter_list:
      cursor.execute(filter_query, (str(i),))
      temp_filter_result.append(cursor.fetchall())
    listbox.delete(0,END)
    for i in temp_filter_result:
      for j in i:
        if j != []:

          h = list(j)
          filter_listbox_result = (h[0] + " | " + h[1] + " | " + h[2] + " | " + h[3] + " | " + h[4])
          final_list.append(filter_listbox_result)
    return final_list
    
  
  
  def combine_filter():
    if apply_ps_filter() != [] and apply_purpose_filter() != []:
        full_list = set(apply_ps_filter()) & set(apply_purpose_filter())
        listbox.delete(0, END)
        for i in full_list:
          listbox.insert(END, i)
    elif apply_ps_filter() != [] and apply_purpose_filter() == []:
      full_list = apply_ps_filter()
      listbox.delete(0, END)
      for i in full_list:
        listbox.insert(END, i)
    elif apply_purpose_filter() != [] and apply_ps_filter() == []:
      full_list = apply_purpose_filter()
      listbox.delete(0, END)
      for i in full_list:
        listbox.insert(END, i)
    else:
      listbox.delete(0, END)
  
  def clear_checkbox():
    product_var.set("False")
    service_var.set("False")
    hardware_var.set("False")
    financial_var.set("False")
    info_var.set("False")
  try:
    base64_encode(user_var_login)
    base64_encode(pass_var_login)
    query = ("SELECT * FROM FBLA_PROJECT.odb.users WHERE Username =(?)")
    cursor.execute(query, (user_var_login.get(),))
    result = cursor.fetchone()
    
    if (list(result))[1] == pass_var_login.get():
    
    
    
    
      main.withdraw()
      data_window = tk.Toplevel()
      data_window.title("Main Page")
      data_window.geometry("500x500")
      data_window.configure(bg="steelblue")
      #Menu Bar
      menu_bar = tk.Menu(data_window)
      menu_1 = tk.Menu(menu_bar, tearoff=0)
      menu_2 = tk.Menu(menu_bar, tearoff=0)
      
      
      if str(user_perm.get()) == "admin":
        menu_3 = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Admin", menu=menu_3)
        menu_3.add_command(label="Add Item", command=lambda: [add_window()])
        menu_3.add_command(label="Remove Item", command=lambda: [delete_window()])
        menu_3.add_command(label="All Users", command=view_users)

        data_window.config(menu=menu_bar)
      menu_1.add_command(label="Log Out", command=lambda: [data_window.withdraw(), main.deiconify()])

      
      
      filter_menu = tk.Menu(menu_2, tearoff=0)
      
      
      product_menu = tk.Menu(filter_menu, tearoff=0)
      relation_menu = tk.Menu(filter_menu, tearoff=0)

      product_menu.add_checkbutton(label='Product', variable=product_var, onvalue='True', offvalue='False')
      product_menu.add_checkbutton(label='Service', variable=service_var, onvalue='True', offvalue='False')
      relation_menu.add_checkbutton(label='Hardware', variable=hardware_var, onvalue='True', offvalue='False')
      relation_menu.add_checkbutton(label='Financial', variable=financial_var, onvalue='True', offvalue='False')
      relation_menu.add_checkbutton(label="Info", variable = info_var, onvalue='True', offvalue="False")

      filter_menu.add_cascade(label='Product/Service', menu=product_menu)
      filter_menu.add_cascade(label='Relation', menu=relation_menu)
      
      
      
      
      menu_2.add_cascade(label="Filter", menu=filter_menu)
      menu_bar.add_cascade(label="Account", menu=menu_1)
      menu_bar.add_cascade(label="Options", menu=menu_2)
      menu_bar.add_command(label="Apply Filter", command =lambda: [combine_filter()])
      menu_bar.add_command(label="Clear Filter", command =lambda: [update_listbox(), clear_checkbox()])
      data_window.config(menu=menu_bar)
      scrollbar = tk.Scrollbar(data_window)
      listbox = tk.Listbox(data_window, width=60, height=20)
      scrollbar.place(relx=0.5, rely=0.5, anchor=CENTER)
      listbox.place(relx=0.5, rely=0.5, anchor=CENTER)
      listbox.config(yscrollcommand = scrollbar.set)
      scrollbar.config(command = listbox.yview)
      cursor.execute("SELECT * FROM FBLA_PROJECT.odb.partners")
      result2 = list(cursor.fetchall())
      for i in range(len(result2)):
        j = list(result2[i])
        info12 = (j[0] + " | " + j[1] + " | " + j[2] + " | " + j[3] + " | " + j[4])
        listbox.insert(tk.END, info12)
      
       
  except TypeError:
    user_var_login.set("")
    pass_var_login.set("")
    messagebox.showerror("Error", "Username doesn't exist!")  

main.mainloop()