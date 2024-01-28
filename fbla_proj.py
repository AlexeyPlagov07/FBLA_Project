import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showwarning
import pypyodbc as odbc
from tooltip import ToolTip
import time
#Initalizing Login Page#
main = tk.Tk()
main.title("Login Page")
main.geometry("500x500")
main.configure(bg="cornflowerblue")
#==Initializing Variables==#
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



#==# MSSQL AZURE server connection #==#
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
#=====================================#

  


# Creates Sign Up Window and includes all related functions #
def sign_up():

  sign_up_window = tk.Toplevel()
  sign_up_window.title("Sign Up")
  sign_up_window.geometry("300x150")
  sign_up_window.configure(bg='powderblue')



  # Sees if passwords are the same when asked to re-enter the password #
  def sign_up_check():

    # compares signup passwords when signup is attempted #
    if pass1_signup.get() == pass2_signup.get():

      # creates empty list for all usernames when checking availability #
      name_list = []

      # selects and fetches all stored usernames from database #
      cursor.execute("""
                      SELECT Username 
                      FROM FBLA_PROJECT.dbo.users
                      """)
      result1 = cursor.fetchall()


      # appends to name_list all created usernames in a list #
      for i in result1:
        name_list.append(list(i)[0])


      # checks if attempted username is in list #
      if user_signup.get() not in name_list:

        # clears window and shows 'signup' was successful #
        sign_up_window.withdraw()
        messagebox.showinfo("Sign Up", "Sign Up Successful!")


        # inserts signed up user into 'users' database #
        info111 = """
                  INSERT 
                  INTO pending_users
                  VALUES (?,?,?)
                  """
        cursor.execute(info111,(user_signup.get(),pass1_signup.get(),"user"))
        conn.commit()


        # clears signup entry box #
        user_signup.set("")
        pass1_signup.set("")
        pass2_signup.set("")


      # tells user username is in use and clears entry box #
      else:
        messagebox.showerror("Sign Up", "Username Already Exists!")
        user_signup.set("")
        pass1_signup.set("")
        pass2_signup.set("")

    # tells user that attempted account passwords don't match #
    else:
      messagebox.showerror("Sign Up", "Passwords Don't Match!")
      user_signup.set("")
      pass1_signup.set("")
      pass2_signup.set("")


  # Labels, Entries, and Buttons for the Sign Up Page #
  user_label2 = tk.Label(sign_up_window, text="Username", bg="powderblue")
  user_label2.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
  password_label2 = tk.Label(sign_up_window, text="Password", bg="powderblue")
  password_label2.place(relx=0.2, rely=0.38, anchor=tk.CENTER)
  password_label3 = tk.Label(sign_up_window, text="Re-Enter", bg="powderblue")
  password_label3.place(relx=0.2, rely=0.56, anchor=tk.CENTER)
  user_entry2 = tk.Entry(sign_up_window, textvariable=user_signup)
  user_entry2.place(relx=0.6, rely=0.2, anchor=tk.CENTER)

  pe2 = tk.Entry(sign_up_window, textvariable=(pass1_signup))
  pe2.place(relx=0.6, rely=0.38, anchor=tk.CENTER)
  pe3 = tk.Entry(sign_up_window, textvariable=pass2_signup)
  pe3.place(relx=0.6, rely=0.56, anchor=tk.CENTER)

  sub2 = tk.Button(sign_up_window, text="Sign Up", command=lambda:[sign_up_check()])
  sub2.place(relx=0.6, rely=0.80, anchor=tk.CENTER)
  sub2_tip = ToolTip(sub2, msg="Click to sign up", delay = 1.5)
  sign_up_window.mainloop()


# Clears login entry boxes #
def clear_login_entry():
  user_var_login.set("")
  pass_var_login.set("")


# Creates a list of all usernames in the system and returns it #
def user_list():
  user_list = []
  cursor.execute("""
                 SELECT Username 
                 FROM FBLA_PROJECT.dbo.users
                 """)
  user_result = cursor.fetchall()
  for i in user_result:
    user_list.append(list(i)[0])
  return user_list



# tests the signed in users role #
def admin_test():

  # checks if user exists #
  if user_var_login.get() in user_list():


    # runs a query to find role of user after logging in #
    query3 =  """
              SELECT * 
              FROM users 
              WHERE Username =(?)
              """
    cursor.execute(query3,(user_var_login.get(),))
    login_result = cursor.fetchone()
    # sets the role of the user in the user_perm variable when logging in #
    user_perm.set((list(login_result))[2])


# login labels #
user_label = tk.Label(main, text="Username", bg='cornflowerblue')
user_label.place(relx=0.26, rely=0.3, anchor=tk.CENTER)
pass_label = tk.Label(main, text="Password", bg='cornflowerblue')
pass_label.place(relx=0.26, rely=0.35, anchor=tk.CENTER)


# login page entries and sign-in button #
ue1 = tk.Entry(main, textvariable=user_var_login)
ue1.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
pe1 = tk.Entry(main, textvariable=pass_var_login)
pe1.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

# login button #
lib1 = tk.Button(main, text='Login', command=lambda: [admin_test(), data_window(), clear_login_entry()])
lib1.place(relx=0.435, rely=0.4)
lib1_tip = ToolTip(lib1, msg="Logs User In", delay = 1.5)
# sign-up button #
sub1 = tk.Button(main, text="Sign Up", command=sign_up)
sub1.place(relx=0.421, rely=0.47)
sub1_tip = ToolTip(sub1, msg="opens signup \n window", delay = 1.5)


# runs a query that locates the names of all the school partners and returns a list #
def partner_list():
  partner_list = []
  cursor.execute("""
                  SELECT partner_name 
                  FROM FBLA_PROJECT.dbo.partners
                 """)
  partner_result = cursor.fetchall()
  for i in partner_result:
    partner_list.append(list(i)[0])
  return partner_list



# window with data and sorting options #
def data_window():
  
  
  
    
    
  # pops out a window that shows all users and their roles #
  def view_users():


    # defines a function that changes the users role #
    
    def user_accept():
      selected_users = []
      for i in user_listbox2.curselection():
        selected_users.append(user_listbox2.get(i).split())
      for i in selected_users:
        user_pass_recovery_query = """
                                   SELECT pword
                                   FROM FBLA_PROJECT.dbo.pending_users
                                   WHERE Username = (?)
                                   """
        cursor.execute(user_pass_recovery_query, (i[0],))
        user_temp_pass_recover = list(cursor.fetchone())
        accept_user_remove_query = """
                                   DELETE FROM FBLA_PROJECT.dbo.pending_users
                                   WHERE Username = (?)
                                   """
        cursor.execute(accept_user_remove_query, (i[0],))
        cursor.commit()
        accept_user_add_query = """
                                INSERT INTO users
                                VALUES (?,?,?)
                                """
        
        cursor.execute(accept_user_add_query, (i[0],user_temp_pass_recover[0], "user"))
        cursor.commit()
    def role_change():
      selected_users = []
      for i in user_listbox1.curselection():
        selected_users.append((user_listbox1.get(i)).split())
      for i in selected_users:

        # changes role from 'admin' to 'user' #
        if i[2] == "admin":
          admin_role_change = """
                              UPDATE FBLA_PROJECT.dbo.users 
                              SET role1='user' 
                              WHERE Username = (?)
                              """



          cursor.execute(admin_role_change, (i[0],))
          conn.commit()

        # changes role from 'user' to 'admin' #
        if i[2] == "user":
          user_role_change = """
                             UPDATE FBLA_PROJECT.dbo.users 
                             SET role1='admin' 
                             WHERE Username = (?)
                             """
          cursor.execute(user_role_change, (i[0],))
          conn.commit()

    def remove_user12():
      selected_users = []
      for i in user_listbox1.curselection():
        selected_users.append((user_listbox1.get(i)).split())
      delete_query = """
                     DELETE FROM FBLA_PROJECT.dbo.users 
                     WHERE Username = (?)
                     """
      for i in selected_users:
        i = i[0]
        cursor.execute(delete_query, ((i),))
        cursor.commit()
    def deny_user1():
      selected_users = []
      for i in user_listbox2.curselection():
        selected_users.append((user_listbox2.get(i)).split())
      delete_query = """
                     DELETE FROM FBLA_PROJECT.dbo.pending_users 
                     WHERE Username = (?)
                     """
      for i in selected_users:
        i = i[0]
        cursor.execute(delete_query, ((i),))
        cursor.commit()
    # updates the gui textbox list of users #
    def user_list_update():

      # clears listbox #
      user_listbox1.delete(0, tk.END)

      #selects all users, starting with admin, so admin appear before regular users #
      cursor.execute("""
                     SELECT * 
                     FROM FBLA_PROJECT.dbo.users 
                     WHERE role1='admin'
                     """)


      user1_result = list(cursor.fetchall())
      cursor.execute("""
                     SELECT * 
                     FROM FBLA_PROJECT.dbo.users 
                     WHERE role1='user'
                     """)

      # recieves and appends the updated list of users to tkinter listbox #
      user2_result = list(cursor.fetchall())
      user3_result = user1_result + user2_result
      for i in range(len(user3_result)):
        j = (list(user3_result))[i]
        user_info = (j[0] + " | " + j[2])
        user_listbox1.insert(tk.END, user_info)
    def update_pending_list():
      # clears listbox #
      user_listbox2.delete(0, tk.END)

      #selects all users, starting with admin, so admin appear before regular users #
      cursor.execute("""
                     SELECT * 
                     FROM FBLA_PROJECT.dbo.pending_users
                     """)


      user1_result = list(cursor.fetchall())

      # recieves and appends the updated list of users to tkinter listbox #    
      for i in range(len(user1_result)):
        j = (list(user1_result))[i]
        user_info = (j[0] + " | " + j[2])
        user_listbox2.insert(tk.END, user_info)
    # Defines the 'users' window #
    user_window = tk.Toplevel()
    user_window.title("Users")
    user_window.geometry("600x300")
    user_window.configure(bg='powderblue')
    u_r_label = tk.Label(user_window, text="User |  Role", bg='powderblue')
    u_r_label.place(relx=0.25, rely=0.1, anchor=tk.CENTER)
    user_scrollbar1 = tk.Scrollbar(user_window)
    user_listbox1 = tk.Listbox(user_window, width=30, height=10, selectmode=tk.MULTIPLE)
    user_scrollbar1.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    user_listbox1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
    user_listbox1.config(yscrollcommand = scrollbar.set)
    user_scrollbar1.config(command = listbox.yview)
    
    user_scrollbar2 = tk.Scrollbar(user_window)
    user_listbox2 = tk.Listbox(user_window, width=30, height=10, selectmode=tk.MULTIPLE)
    user_scrollbar1.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
    user_listbox2.place(relx=0.7, rely=0.4, anchor=tk.CENTER)
    user_listbox2.config(yscrollcommand = scrollbar.set)
    user_scrollbar2.config(command = listbox.yview)

    # update both user list #
    user_list_update()
    update_pending_list()
    
    # button to change role of selected user #
    role_change1 = tk.Button(user_window, text="Change Role", command=lambda: [role_change(),user_list_update()])
    role_change1.place(relx=0.2, rely=0.8, anchor=tk.CENTER)


    # button to remove user #
    remove_user_b1 = tk.Button(user_window, text="Remove User", command=lambda: [remove_user12(), user_list_update()])
    remove_user_b1.place(relx=0.4, rely=0.8, anchor=tk.CENTER)

    # button to accept user #
    accept_user_b1 = tk.Button(user_window, text="Accept User", command=lambda: [user_accept(), update_pending_list(), user_list_update()])
    accept_user_b1.place(relx=0.6, rely=0.8, anchor=tk.CENTER)

    # button to deny user #
    deny_user_b1 = tk.Button(user_window, text="Deny User", command=lambda: [deny_user1(), update_pending_list()])
    deny_user_b1.place(relx=0.8, rely=0.8, anchor=tk.CENTER)
  
  
  
  # updates the listbox of partners #
  def update_listbox():

    # clears listbox #
    listbox.delete(0,tk.END)

    # selects all partners in database #
    cursor.execute("""
                   SELECT * 
                   FROM FBLA_PROJECT.dbo.partners
                   """)

    # appends all partners into the listbox #
    result21 = list(cursor.fetchall())
    for i in range(len(result21)):
      j = list(result21[i])
      info121 = (j[0] + " | " + j[1] + " | " + j[2] + " | " + j[3] + " | " + j[4])
      listbox.insert(tk.END, info121)

  # function that adds partners into the listbox of partners #
  def add_partner():

    # checks whether the partner is in the list already #
    if new_p_name.get() not in partner_list():

      # inserts partner into database with SQL query #
      add_query = """
                  INSERT 
                  INTO partners 
                  VALUES (?,?,?,?,?)
                  """
      cursor.execute(add_query, 
        (new_p_name.get(), new_p_purpose.get(), 
        new_p_ps.get(), new_p_relation.get(), 
        new_p_contact.get()))
      conn.commit()

      # resets the entries for partner info #
      new_p_name.set("")
      new_p_purpose.set("")
      new_p_ps.set("")
      new_p_relation.set("")
      new_p_contact.set("")

      messagebox.showinfo("Success!", "Your New Partner Has Been Saved!")
    else:
      messagebox.showerror("Error", "Partner Already In System!")

  # window that pops up whenever adding a partner #
  def add_window():

    # window geometry #
    add_window = tk.Toplevel()
    add_window.title("Add To List")
    add_window.geometry("300x250")
    add_window.configure(bg="powderblue")

    # all patrner info entries and labels #
    p_name1 = tk.Label(add_window, text="Partner partner_name", bg="powderblue")
    p_name1.place(relx=0.2, rely=0.1, anchor=tk.CENTER)
    p_purpose1 = tk.Label(add_window, text="Partner Purpose", bg="powderblue")
    p_purpose1.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
    p_ps1 = tk.Label(add_window, text="Product/Service", bg="powderblue")
    p_ps1.place(relx=0.2, rely=0.3, anchor=tk.CENTER)
    p_relation1 = tk.Label(add_window, text="Partner Relation", bg="powderblue")
    p_relation1.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    p_contact1 = tk.Label(add_window, text="Partner Contact", bg="powderblue")
    p_contact1.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
    p_name = tk.Entry(add_window, textvariable=new_p_name)
    p_name.place(relx=0.7, rely=0.1, anchor=tk.CENTER)
    p_purpose = tk.Entry(add_window, textvariable=new_p_purpose)
    p_purpose.place(relx=0.7, rely=0.2, anchor=tk.CENTER)
    p_ps= tk.Entry(add_window, textvariable=new_p_ps)
    p_ps.place(relx=0.7, rely=0.3, anchor=tk.CENTER)
    p_relation = tk.Entry(add_window, textvariable=new_p_relation)
    p_relation.place(relx=0.7, rely=0.4, anchor=tk.CENTER)
    p_contact = tk.Entry(add_window, textvariable=new_p_contact)
    p_contact.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

    # partner submit button that closes the window, adds the partner, and updates the listbox #
    new_p_submit = tk.Button(add_window, text="Add Partner", command = lambda: [add_partner(),add_window.withdraw(), update_listbox()])
    new_p_submit.place(relx=0.5, rely=0.7, anchor=S)



  # delets partner from listbox #
  def delete_partner():

    # checks if the partner is in the list #
    if p_delete.get() in partner_list():

      # removes the partner from database using SQL query #
      delete_query = ("""
                      DELETE 
                      FROM FBLA_PROJECT.dbo.partners 
                      WHERE partner_name=(?)
                      """)
      cursor.execute(delete_query, (p_delete.get(),))
      conn.commit()

      # clears delete entry #
      p_delete.set("")
    else:
      messagebox.showerror("Error", "Partner is not in system!")

  # window where user deletes partners from the database #
  def delete_window():
    delete_window = tk.Toplevel()
    delete_window.title("Delete From List")
    delete_window.geometry("300x100")
    delete_window.configure(bg="powderblue")
    p_del = tk.Label(delete_window, text="Enter Partner partner_name to Delete", bg="powderblue")
    p_del.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
    p_delete1 = tk.Entry(delete_window, textvariable=p_delete)
    p_delete1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # button deletes the entered partner, closes window, and updates the listbox #
    p_del_button = tk.Button(delete_window, text="Delete Partner", command =lambda:[delete_partner(), delete_window.withdraw(),update_listbox()])
    p_del_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

  # applies the filter on the data whether it is product or service relation #
  def apply_ps_filter():
    temp_filter_list = []
    final_list = []
    temp_filter_result = []


    # sees whether the checkbox is selected for filtering and appends the filter to a list #
    for i in filter_ps_list:
      if (filter_ps_dict[i]).get() == 'True':
        temp_filter_list.append(i)

    filter_query = """
                   SELECT * 
                   FROM FBLA_PROJECT.dbo.partners 
                   WHERE product_service = (?)
                   """

    # gets all the partner info from database depending on the list of filters #
    for i in temp_filter_list:
      cursor.execute(filter_query, (str(i),))
      # appends partner_info query to a list #
      temp_filter_result.append(cursor.fetchall())


    # clears listbox #
    listbox.delete(0,tk.END)

    # puts all the partner info into a string to input into the listbox #
    for i in temp_filter_result:
      for j in i:
        if j != []:

          h = list(j)
          filter_listbox_result = (h[0] + " | " + h[1] + " | " + h[2] + " | " + h[3] + " | " + h[4])
          final_list.append(filter_listbox_result)


    # returns list of partners with the filter applied #
    return final_list


  # applies filter on partner list based on their purpose to the school #
  def apply_purpose_filter():
    temp_filter_list = []
    temp_filter_result = []
    final_list = []

    # sees whether the checkbox is selected for filtering and appends the filter to a list #
    for i in filter_purpose_list:

      if (filter_purpose_dict[i]).get() == 'True':
        temp_filter_list.append(i)
    filter_query = """
                   SELECT * 
                   FROM FBLA_PROJECT.dbo.partners 
                   WHERE available_resource = (?)
                   """
    for i in temp_filter_list:
      cursor.execute(filter_query, (str(i),))
      temp_filter_result.append(cursor.fetchall())
    listbox.delete(0,tk.END)
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
        listbox.delete(0, tk.END)
        for i in full_list:
          listbox.insert(tk.END, i)


    elif apply_ps_filter() != [] and apply_purpose_filter() == []:
      full_list = apply_ps_filter()
      listbox.delete(0, tk.END)
      for i in full_list:
        listbox.insert(tk.END, i)


    elif apply_purpose_filter() != [] and apply_ps_filter() == []:
      full_list = apply_purpose_filter()
      listbox.delete(0, tk.END)
      for i in full_list:
        listbox.insert(tk.END, i)
    else:
      listbox.delete(0, tk.END)

  def clear_checkbox():
    product_var.set("False")
    service_var.set("False")
    hardware_var.set("False")
    financial_var.set("False")
    info_var.set("False")
  try:
    query = ("""
             SELECT * 
             FROM FBLA_PROJECT.dbo.users 
             WHERE Username =(?)
             """)
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
        menu_3.add_command(label="Add Item", command=lambda:[add_window()])
        menu_3.add_command(label="Remove Item", command=lambda:[delete_window()])
        menu_3.add_command(label="All Users", command=view_users)

        data_window.config(menu=menu_bar)

      menu_1.add_command(label="Log Out", command=lambda:[data_window.withdraw(),main.deiconify()])



      filter_menu = tk.Menu(menu_2, tearoff=0)


      product_menu = tk.Menu(filter_menu, tearoff=0)
      relation_menu = tk.Menu(filter_menu, tearoff=0)

      product_menu.add_checkbutton(label='Product', 
        variable=product_var, onvalue='True', offvalue='False')
      product_menu.add_checkbutton(label='Service', 
        variable=service_var, onvalue='True', offvalue='False')
      relation_menu.add_checkbutton(label='Hardware', 
        variable=hardware_var, onvalue='True', offvalue='False')
      relation_menu.add_checkbutton(label='Financial', 
        variable=financial_var, onvalue='True', offvalue='False')
      relation_menu.add_checkbutton(label="Info", 
        variable = info_var, onvalue='True', offvalue="False")
      filter_menu.add_cascade(label='Product/Service', menu=product_menu)
      filter_menu.add_cascade(label='Relation', menu=relation_menu)




      menu_2.add_cascade(label="Filter", menu=filter_menu)
      menu_bar.add_cascade(label="Account", menu=menu_1)
      menu_bar.add_cascade(label="Options", menu=menu_2)
      menu_bar.add_command(label="Apply Filter", command =lambda: [combine_filter()])
      menu_bar.add_command(label="Clear Filter", command = lambda: [update_listbox(), clear_checkbox()])
      data_window.config(menu=menu_bar)
      scrollbar = tk.Scrollbar(data_window)
      listbox = tk.Listbox(data_window, width=60, height=20)
      scrollbar.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
      listbox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
      listbox.config(yscrollcommand = scrollbar.set)
      scrollbar.config(command = listbox.yview)
      cursor.execute("""
                     SELECT * 
                     FROM FBLA_PROJECT.dbo.partners
                     """)
      result2 = list(cursor.fetchall())
      for i in range(len(result2)):
        j = list(result2[i])
        info12 = (j[0] + " | " + j[1] + " | " + j[2] + " | " + j[3] + " | " + j[4])
        listbox.insert(tk.END, info12)


    else:
      messagebox.showerror("Error","Password is incorrect!") 
  except TypeError:
    user_var_login.set("")
    pass_var_login.set("")
    messagebox.showerror("Error", "Username doesn't exist!")  
  
main.mainloop()