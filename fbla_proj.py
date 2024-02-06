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
new_p_pathway = tk.StringVar()
p_delete = tk.StringVar()
product_var = tk.StringVar()
service_var = tk.StringVar()
hardware_var = tk.StringVar()
financial_var = tk.StringVar()
info_var = tk.StringVar()
mechatronics_var = tk.StringVar()
computer_science_var = tk.StringVar()
cybersecurity_var = tk.StringVar()
healthcare_var = tk.StringVar()
aerospace_var = tk.StringVar()
first_responders_var = tk.StringVar()
business_var = tk.StringVar()
graphic_design_var = tk.StringVar()
search_var = tk.StringVar()
filter_image = tk.PhotoImage(file="filter.png")
plus_image = tk.PhotoImage(file="plus.png")
logout_image = tk.PhotoImage(file="logout.png")
####
microsoft_image = tk.PhotoImage(file="partner_images/microsoft.png")
seimens_image = tk.PhotoImage(file="partner_images/seimens.png")
northside_image = tk.PhotoImage(file="partner_images/northside.png")
automation_image = tk.PhotoImage(file="partner_images/automation.png")
gp_image = tk.PhotoImage(file="partner_images/ga_power.png")
ung_image = tk.PhotoImage(file="partner_images/ung.png")
honda_image = tk.PhotoImage(file="partner_images/honda.png")
epps_image = tk.PhotoImage(file="partner_images/epps.png")
arc_image = tk.PhotoImage(file="partner_images/amr.png")
ibm_image = tk.PhotoImage(file="partner_images/ibm.png")
brandy_wine_image = tk.PhotoImage(file="partner_images/brandy_wine.png")
lanier_image = tk.PhotoImage(file="partner_images/lanier.png")
adobe_image = tk.PhotoImage(file="partner_images/adobe.png")
MMM_image = tk.PhotoImage(file="partner_images/3M.png")
amazon_image = tk.PhotoImage(file="partner_images/amazon.png")
epa_image = tk.PhotoImage(file="partner_images/epa.png")
jp_morgan_image = tk.PhotoImage(file="partner_images/JP_morgan.png")
united_airlines_image = tk.PhotoImage(file="partner_images/united_airlines.png")
chevron_image = tk.PhotoImage(file="partner_images/chevron.png")
coke_image = tk.PhotoImage(file="partner_images/coke.png")
natgeo_image = tk.PhotoImage(file="partner_images/nat_geo.png")
walmart_image = tk.PhotoImage(file="partner_images/walmart.png")
ge_image = tk.PhotoImage(file="partner_images/ge.png")
nike_image = tk.PhotoImage(file="partner_images/nike.png")
dell_image = tk.PhotoImage(file="partner_images/dell.png")
google_image = tk.PhotoImage(file="partner_images/google.png")
walgreens_image = tk.PhotoImage(file="partner_images/walgreens.png")
lm_image = tk.PhotoImage(file="partner_images/lm.png")
chick_image = tk.PhotoImage(file="partner_images/chick.png")
home_depot_image = tk.PhotoImage(file="partner_images/home_depot.png")
filter_ps_list = ['product', 'service']
filter_ps_dict = {'product':product_var, 'service':service_var}
filter_purpose_list = ['hardware', 'financial', 'info']
filter_purpose_dict = {'hardware':hardware_var, 'financial':financial_var, 'info':info_var}
filter_pathway_list = ['mechatronics', 'computer science', 'cybersecurity', 'healthcare', 'aerospace', 'first responders', 'business', 'graphic design']
filter_pathway_dict = {'mechatronics':mechatronics_var, 'computer science':computer_science_var, 'cybersecurity':cybersecurity_var, 'healthcare':healthcare_var, 'aerospace':aerospace_var, 'first responders':first_responders_var, 'business':business_var, 'graphic design':graphic_design_var}
partner_image_dict = {
                      "Microsoft":microsoft_image, 
                      "Seimens":seimens_image, 
                      "Northside Hospital":northside_image, 
                      "Automation Direct":automation_image, 
                      "Georgia Power":gp_image, 
                      "UNG":ung_image, 
                      "Honda":honda_image, 
                      "EPPS Aviation":epps_image, 
                      "American Red Cross":arc_image, 
                      "IBM":ibm_image, 
                      "BrandyWine Printing":brandy_wine_image, 
                      "Lanier Flight Center":lanier_image, 
                      "Adobe":adobe_image,
                      "3M":MMM_image,
                      "Amazon":amazon_image,
                      "EPA":epa_image,
                      "JP Morgan":jp_morgan_image,
                      "United Airlines":united_airlines_image,
                      "Chevron":chevron_image,
                      "Coca-Cola":coke_image,
                      "National Geographic":natgeo_image,
                      "Walmart":walmart_image,
                      "General Electric":ge_image,
                      "Nike":nike_image,
                      "Dell":dell_image,
                      "Google":google_image,
                      "Walgreens":walgreens_image,
                      "Lockheed Martin":lm_image,
                      "Chick-fil-a":chick_image,
                      "Home Depot":home_depot_image
                      }
partner_info_dict = {
                     "Microsoft":"Microsoft is a software as a service company that provides AAI students with technology knowledge, but mainly financial support through grants.",
                     "Seimens":"Seimens is a tech and engineering company that focuses on automating processes. Seimens provides mechatronics students with products for training the students.",
                     "Northside Hospital":"Northside is one of the leading hospitals in the US and provides AAI\'s healthcare students with residential hospital knowlegde, as well as training for on site situations",
                     "Automation Direct":"Automation Direct is a manufacturing company that mainly provides AAI students with materials, especially for their developing FRC robotics team.",
                     "Georgia Power":"Georgia Power is the leading power company in Georgia. With their extensive knowledge, Georgia Power provides energy and mechatroncis students with knowledge concerning the pathway and help out with internships for work based learning.",
                     "UNG":"University of North Georgia is an amazing georgia college to attend to especially for the field of cybersecurity. UNG provides AAI\'s cybersecurity students with great experiences and opportuunities to those trying to enter the cybersecurity field.",
                     "Honda":"Honda is one of the leaders in the automotive industry and provides the AAI FRC robotics team with the ability to advance on their robot by providing financial grants to the team.",
                     "EPPS Aviation": "EPPS Aviation is a parts manufacturer for small airliners and personal planes. EPPS Aviation provides support to the aerospace students at AAI, by proving pathway information, and by teaching manufacturing techniques for planes and other aerospace tech.",
                     "American Red Cross":"The American Red Cross is a national foundation used to help people in the US on a daily basis. The ARC helps the healthcare and first responder students at AAI, by providing financial support, and by providing internship opportunities for students.",
                     "IBM":"IBM is a data and security company that helps companies with their technical needs. IBM helps AAI cybersecurity and computer science students financially by providing money and grants for certifictaions and courses for students.",
                     "Brandywine Printing":"Brandywine Printing is a small graphic design shop that prints designs onto textiles. Brandywine Printing helps AAI graphic design students by providing them with special tools and materials used for creating and making designs on textiles for students in the student shop and other events.",
                     "Lanier Flight Center":"Lanier Flight Center is a organiztaion that helps with the flight eductaion of students. Laneir Flight Center helps AAI aerospace atudents by providing for them learning opportunities in flying and other extensive knwoledge about flying.",
                     "Adobe":"Adobe is a software as a service company and provides AAI students with Adobe software for free instead of for purchase.",
                     "3M":"3M is a manufacturing company that manufactures parts for businesses. 3M helps the AAI FRC robotics team by provifing parts and electronics to the team.",
                     "Amazon":"Amazon is a shipping and data company that provides services for people worldwide.\n They help AAI students by providing internship opportunities for students.",
                     "EPA":"The EPA is a government agency dealing with environmental protection. EPA works with mechatronics and energy students to try and come up with environmental solutions to problems in the community.",
                     "JP Morgan":"JP Morgan is a financial company that provides banking help to people. JP Morgan helps the AAI business students with knowledge of finance and business.",
                     "United Airlines":"United Airlines is a airliner company that provides a travel service for people.\n United Airlines works with aerospace studetns to try and provide internship opporutnities for students.",
                     "Chevron":"Chevron is a oil company and provides AAI first responder students with information on specific fire situations such as oil fires and how to deal with them.",
                     "Coca-Cola":"Coca-Cola is one of the leading beverage companies in the world; supporting financially the AAI FRC team.",
                     "National Geographic":"National Geographic is a nature organization, bring value to the natural world\n and also value to the graphic design students by helping them gain internship opportunities through images and competitions.",
                     "Walmart":"Walmart is a leader in the shopping industry, provding financial support through grants for the AAI FRC team.",
                     "General Electric":"General Electric is an appliance company specializing in household appliances and also helps the mechatronics students by providing parts for the classroom.",
                     "Nike":"Nike is a leader in the shoe company that also provides the AAI graphic design students with insite on how Nike does their designs and provides the students with opportunities in internships.",
                     "Dell":"Dell is a tech company that produces computers for people. Dell also provides a majority of the computer science students\' desktops and laptops.",
                     "Google":"Google is a data company that focuses on providing the user with a good service. Google also provides the cybersecurity students with a good amount of internship positions and opportunities.",
                     "Walgreens":"Walgreens is a mini store and pharmaceutical company. They provide AAI healthcare students with knowledge about the pharmaceutical business and provides students with internship opportunities.",
                     "Lockheed Martin":"Lockheed Martin is an aerospace company specializing in combat planes. they provide the AAI aerospace students with internship and work basd learning opportunities.",
                     "Chick-fil-a":"Chick-fil-a is a major fast food company and the provide the AAI FRC robotics team with money and financial support.",
                     "Home Depot":"Home Depot is a hardware warehouse store that provides people with hardware they need. Home Depot also supports the AAI FRC team with hardware for the robot."
                     }
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

  


#=# Creates Sign Up Window and includes all related functions #=#
def sign_up():

  sign_up_window = tk.Toplevel()
  sign_up_window.title("Sign Up")
  sign_up_window.geometry("300x150")
  sign_up_window.configure(bg='powderblue')



  #=# Sees if passwords are the same when asked to re-enter the password #=#
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


#=# Clears login entry boxes #=#
def clear_login_entry():
  user_var_login.set("")
  pass_var_login.set("")


#=# Creates a list of all usernames in the system and returns it #=#
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



#=# tests the signed in users role #=#
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
  
  # provides a small blurb about the company chosen #
  def info_box_window():
    selected_partner = []
    final_partner = []
    info_window = tk.Toplevel()
    info_window.title("Partner Info")
    info_window.geometry("400x300")
    info_window.configure(bg='powderblue')
    
    text_box = tk.Text(info_window, width=40, height=6, wrap=tk.WORD)
    text_box.place(relx=0.5, rely=0.73, anchor=tk.CENTER)
    
    
    #appends all selected users to a list #
    for i in listbox.curselection():
      selected_partner.append(listbox.get(i))
      selected_partner = (selected_partner[0]).split()    
    i = 0
    while "-" not in selected_partner[i]:
      final_partner.append(selected_partner[i])
      i += 1
      
    final_partner = ' '.join(final_partner)
    
    text_box.insert(tk.END, partner_info_dict[final_partner])

    info_win_query = """
                     SELECT *
                     FROM FBLA_PROJECT.dbo.partners
                     WHERE partner_name = (?)
                     """
    cursor.execute(info_win_query, (final_partner,))
    info_win_result = list(cursor.fetchone())
    
    
    image_label = tk.Label(info_window, image=(partner_image_dict[final_partner]))
    image_label.place(relx=0.2, rely=0.25, anchor=tk.CENTER)
    purpose_label = tk.Label(info_window, text = "Business Type:", bg="powderblue")
    purpose_label.place(relx=0.49, rely=0.1, anchor=tk.CENTER)
    purpose_label_var = tk.Label(info_window, text=info_win_result[1], bg="powderblue")
    purpose_label_var.place(relx=0.49, rely=0.18, anchor=tk.CENTER)
    ps_label = tk.Label(info_window, text = "Provides a:", bg="powderblue")
    ps_label.place(relx=0.75, rely=0.1, anchor=tk.CENTER)
    ps_label_var = tk.Label(info_window, text=info_win_result[2], bg="powderblue")
    ps_label_var.place(relx=0.75, rely=0.17, anchor=tk.CENTER)
    relation_label = tk.Label(info_window, text = "Provides for \nthe school: ", bg="powderblue")
    relation_label.place(relx=0.48, rely=0.29, anchor=tk.CENTER)
    relation_label_var = tk.Label(info_window, text=info_win_result[3], bg="powderblue")
    relation_label_var.place(relx=0.47, rely=0.37, anchor=tk.CENTER)
    pathway_label = tk.Label(info_window, text = "Main pathway:", bg="powderblue")
    pathway_label.place(relx=0.78, rely=0.25, anchor=tk.CENTER)
    pathway_label_var = tk.Label(info_window, text=info_win_result[4], bg="powderblue")
    pathway_label_var.place(relx=0.78, rely=0.34, anchor=tk.CENTER)
    contact_label = tk.Label(info_window, text="Contact:", bg="powderblue")
    contact_label.place(relx=0.46, rely = 0.45, anchor=tk.CENTER)
    contact_label_var = tk.Label(info_window, text=info_win_result[5], bg="powderblue")
    contact_label_var.place(relx=0.5, rely=0.51, anchor=tk.CENTER)
  # function puts listbox items in alphabetical order #
  def alphabetical_listbox():
    list_box_var = (list(listbox.get(0, tk.END)))
    list_box_var = sorted(list_box_var)
    listbox.delete(0, tk.END)
    for i in list_box_var:
      listbox.insert(tk.END, i)
  
  
  # function puts listbox items in reverse alphabetical order #
  def realphabetical_listbox():
    list_box_var = (list(listbox.get(0, tk.END)))
    list_box_var = (sorted(list_box_var))[::-1]
    listbox.delete(0, tk.END)
    for i in list_box_var:
      listbox.insert(tk.END, i)
    
  
  # pops out a window that shows all users and their roles #
  def view_users():


    
    # defines a function that lets admin select users from pending list #
    def user_accept():
      selected_users = []
      
      # appends all selected users from the pending list into user list #
      for i in user_listbox2.curselection():
        selected_users.append(user_listbox2.get(i).split())
      
      # selects the password from users in pending list to append to user database #
      for i in selected_users:
        user_pass_recovery_query = """
                                   SELECT pword
                                   FROM FBLA_PROJECT.dbo.pending_users
                                   WHERE Username = (?)
                                   """
        cursor.execute(user_pass_recovery_query, (i[0],))
        user_temp_pass_recover = list(cursor.fetchone())
        
        # removes the accepted user from the pending database #
        accept_user_remove_query = """
                                   DELETE FROM FBLA_PROJECT.dbo.pending_users
                                   WHERE Username = (?)
                                   """
        cursor.execute(accept_user_remove_query, (i[0],))
        cursor.commit()
        
        # adds the new user to the user database #
        accept_user_add_query = """
                                INSERT INTO users
                                VALUES (?,?,?)
                                """     
        cursor.execute(accept_user_add_query, (i[0],user_temp_pass_recover[0], "user"))
        cursor.commit()
    
    # defines a function that changes the users role #
    def role_change():
      selected_users = []
      
      # appends all selected users to a list #
      for i in user_listbox1.curselection():
        selected_users.append((user_listbox1.get(i)).split())
      
      # loops through every selected user #
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
    
    
    # defines a function that removes 
    def remove_user_func():
      selected_users = []
      
      # appends all selected users to a list #
      for i in user_listbox1.curselection():
        selected_users.append((user_listbox1.get(i)).split())
      
      # SQL statement that removes user from the users database #
      delete_query = """
                     DELETE FROM FBLA_PROJECT.dbo.users 
                     WHERE Username = (?)
                     """
      # runs the query for all selected users #
      for i in selected_users:
        i = i[0]
        cursor.execute(delete_query, ((i),))
        cursor.commit()
    
    # defines a function that denies a user in the pending box #
    def deny_user_func():
      selected_users = []
      
      #appends all selected users to a list #
      for i in user_listbox2.curselection():
        selected_users.append((user_listbox2.get(i)).split())
      
      # query removes selected user from pending list database #
      delete_query = """
                     DELETE FROM FBLA_PROJECT.dbo.pending_users 
                     WHERE Username = (?)
                     """
      
      # runs the query for all selected users in the list #
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
      user2_result = list(cursor.fetchall())
      user3_result = user1_result + user2_result
      
      # recieves and appends the updated list of users to tkinter listbox #
      for i in range(len(user3_result)):
        j = (list(user3_result))[i]
        user_info = (j[0] + " | " + j[2])
        user_listbox1.insert(tk.END, user_info)
    
    # defines a functiont that updates the listbox for the pending users #
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
    # users listbox #
    user_scrollbar1 = tk.Scrollbar(user_window)
    user_listbox1 = tk.Listbox(user_window, width=30, height=10, selectmode=tk.MULTIPLE)
    user_scrollbar1.place(relx=0.3, rely=0.5, anchor=tk.CENTER)
    user_listbox1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)
    user_listbox1.config(yscrollcommand = scrollbar.set)
    user_scrollbar1.config(command = listbox.yview)
    # pending listbox #
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
    role_change_tip = ToolTip(role_change1, msg="Changes the role \n of selected user", delay = 1.5)


    # button to remove user #
    remove_user_b1 = tk.Button(user_window, text="Remove User", command=lambda: [remove_user_func(), user_list_update()])
    remove_user_b1.place(relx=0.4, rely=0.8, anchor=tk.CENTER)
    remove_user_tip = ToolTip(remove_user_b1, msg="Removes user \n from system", delay = 1.5)

    # button to accept user #
    accept_user_b1 = tk.Button(user_window, text="Accept User", command=lambda: [user_accept(), update_pending_list(), user_list_update()])
    accept_user_b1.place(relx=0.6, rely=0.8, anchor=tk.CENTER)
    accept_user_tip = ToolTip(accept_user_b1, msg="Accpets user from \n request list", delay = 1.5)
    # button to deny user #
    deny_user_b1 = tk.Button(user_window, text="Deny User", command=lambda: [deny_user_func(), update_pending_list()])
    deny_user_b1.place(relx=0.8, rely=0.8, anchor=tk.CENTER)
    deny_user_tip = ToolTip(deny_user_b1, msg="Denies user from \n request list", delay = 1.5)

  
  
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
      info121 = (j[0] + " " + ("-"*(30-(len(j[0])))) + " " + j[5])
      listbox.insert(tk.END, info121)
  # function that adds partners into the listbox of partners #
  def add_partner():

    # checks whether the partner is in the list already #
    if new_p_name.get() not in partner_list():

      # inserts partner into database with SQL query #
      add_query = """
                  INSERT 
                  INTO partners 
                  VALUES (?,?,?,?,?,?)
                  """
      cursor.execute(add_query, 
        (new_p_name.get(), new_p_purpose.get(), 
        new_p_ps.get(), new_p_relation.get(),
        new_p_pathway.get(), new_p_contact.get()))
      conn.commit()

      # resets the entries for partner info #
      new_p_name.set("")
      new_p_purpose.set("")
      new_p_ps.set("")
      new_p_relation.set("")
      new_p_pathway.set("")
      new_p_contact.set("")
      # shows success message #
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
    p_name1 = tk.Label(add_window, text="Partner Name", bg="powderblue")
    p_name1.place(relx=0.2, rely=0.1, anchor=tk.CENTER)
    p_purpose1 = tk.Label(add_window, text="Partner Purpose", bg="powderblue")
    p_purpose1.place(relx=0.2, rely=0.2, anchor=tk.CENTER)
    p_ps1 = tk.Label(add_window, text="Product/Service", bg="powderblue")
    p_ps1.place(relx=0.2, rely=0.3, anchor=tk.CENTER)
    p_relation1 = tk.Label(add_window, text="Partner Relation", bg="powderblue")
    p_relation1.place(relx=0.2, rely=0.4, anchor=tk.CENTER)
    p_pathway1 = tk.Label(add_window, text='Pathway', bg="powderblue")
    p_pathway1.place(relx=0.2, rely=0.5 , anchor=tk.CENTER)
    p_contact1 = tk.Label(add_window, text="Partner Contact", bg="powderblue")
    p_contact1.place(relx=0.2, rely=0.6, anchor=tk.CENTER)
    p_name = tk.Entry(add_window, textvariable=new_p_name)
    p_name.place(relx=0.7, rely=0.1, anchor=tk.CENTER)
    p_purpose = tk.Entry(add_window, textvariable=new_p_purpose)
    p_purpose.place(relx=0.7, rely=0.2, anchor=tk.CENTER)
    p_ps= tk.Entry(add_window, textvariable=new_p_ps)
    p_ps.place(relx=0.7, rely=0.3, anchor=tk.CENTER)
    p_relation = tk.Entry(add_window, textvariable=new_p_relation)
    p_relation.place(relx=0.7, rely=0.4, anchor=tk.CENTER)
    p_pathway = tk.Entry(add_window, textvariable=new_p_pathway)
    p_pathway.place(relx=0.7, rely=0.5, anchor=tk.CENTER)
    p_contact = tk.Entry(add_window, textvariable=new_p_contact)
    p_contact.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

    # partner submit button that closes the window, adds the partner, and updates the listbox #
    new_p_submit = tk.Button(add_window, text="Add Partner", command = lambda: [add_partner(),add_window.withdraw(), update_listbox()])
    new_p_submit.place(relx=0.5, rely=0.8, anchor=S)
    new_p_submit_tip = ToolTip(new_p_submit, msg="Adds new partner \n to the list", delay = 1.5)

 
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
    p_del_button_tip = ToolTip(p_del_button, msg="Removes partner \n from list", delay = 1.5)
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
          filter_listbox_result = (h[0] + " | " + h[1] + " | " + h[2] + " | " + h[3] + " | " + h[4] + " | " + h[5])
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
      # sees which buttons are selected in the filter dropdown #
      if (filter_purpose_dict[i]).get() == 'True':
        temp_filter_list.append(i)
    
    # runs query that selects all partners with the filters applied #
    filter_query = """
                   SELECT * 
                   FROM FBLA_PROJECT.dbo.partners 
                   WHERE available_resource = (?)
                   """
    
    # runs query based on all of the filters appended to a list #
    for i in temp_filter_list:
      cursor.execute(filter_query, (str(i),))
      temp_filter_result.append(cursor.fetchall())
    
    # updates listbox based on filtered output #
    listbox.delete(0,tk.END)
    for i in temp_filter_result:
      for j in i:
        if j != []:
          h = list(j)
          filter_listbox_result = (h[0] + " | " + h[1] + " | " + h[2] + " | " + h[3] + " | " + h[4] + " | " + h[5])
          final_list.append(filter_listbox_result)
    # returns all of the partners that are refernced by the filter in a list #
    return final_list

  def apply_pathway_filter():
    temp_filter_list = []
    temp_filter_result = []
    final_list = []

    # sees whether the checkbox is selected for filtering and appends the filter to a list #
    for i in filter_pathway_list:
      # sees which buttons are selected in the filter dropdown #
      if (filter_pathway_dict[i]).get() == 'True':
        temp_filter_list.append(i)
    
    # runs query that selects all partners with the filters applied #
    filter_query = """
                   SELECT * 
                   FROM FBLA_PROJECT.dbo.partners 
                   WHERE pathway = (?)
                   """
    
    # runs query based on all of the filters appended to a list #
    for i in temp_filter_list:
      cursor.execute(filter_query, (str(i),))
      temp_filter_result.append(cursor.fetchall())
    
    # updates listbox based on filtered output #
    listbox.delete(0,tk.END)
    for i in temp_filter_result:
      for j in i:
        if j != []:
          h = list(j)
          filter_listbox_result = (h[0] + " | " + h[1] + " | " + h[2] + " | " + h[3] + " | " + h[4] + " | " + h[5])
          final_list.append(filter_listbox_result)
    # returns all of the partners that are refernced by the filter in a list #
    return final_list
  # combines the two filter sets to compare and see which partners are in both lists #
  def combine_filter():
    # redo comments later #
    if apply_ps_filter() != [] and apply_purpose_filter() != [] and apply_pathway_filter() != []:
        full_list = set(apply_ps_filter()) & set(apply_purpose_filter()) & set(apply_pathway_filter())
        listbox.delete(0, tk.END)
        for i in full_list:
          listbox.insert(tk.END, i)
    # redo comments later #
    elif apply_ps_filter() != [] and apply_purpose_filter() == [] and apply_pathway_filter() != []:
      full_list = set(apply_ps_filter()) & set(apply_pathway_filter())
      listbox.delete(0, tk.END)
      for i in full_list:
        listbox.insert(tk.END, i)
    # redo comments later #
    elif apply_purpose_filter() == [] and apply_ps_filter() != [] and apply_pathway_filter() != []:
      full_list = set(apply_ps_filter()) & set(apply_pathway_filter())
      listbox.delete(0, tk.END)
      for i in full_list:
        listbox.insert(tk.END, i)
    
    # redo comments later #
    elif apply_purpose_filter() != [] and apply_ps_filter() != [] and apply_pathway_filter() == []:
      full_list = set(apply_ps_filter()) & set(apply_purpose_filter())
      listbox.delete(0, tk.END)

      for i in full_list:
        listbox.insert(tk.END, i) 

    elif apply_purpose_filter() != [] and apply_ps_filter() == [] and apply_pathway_filter() == []:
      full_list = apply_purpose_filter()
      listbox.delete(0, tk.END)
      for i in full_list:
        listbox.insert(tk.END, i) 
    elif apply_purpose_filter() == [] and apply_ps_filter() != [] and apply_pathway_filter() == []:
      full_list = apply_ps_filter()
      listbox.delete(0, tk.END)
      for i in full_list:
        listbox.insert(tk.END, i)
    elif apply_purpose_filter() == [] and apply_ps_filter() == [] and apply_pathway_filter() != []:
      full_list = apply_pathway_filter()
      listbox.delete(0, tk.END)
      for i in full_list:
        listbox.insert(tk.END, i) 
    else:
      listbox.delete(0, tk.END)

    
  # function is used to clear the filter checkboxes when the 'clear filter' button is used #
  def clear_checkbox():
    product_var.set("False")
    service_var.set("False")
    hardware_var.set("False")
    financial_var.set("False")
    info_var.set("False")
    mechatronics_var.set("False")
    computer_science_var.set("False")
    cybersecurity_var.set("False")
    healthcare_var.set("False")
    aerospace_var.set("False")
    first_responders_var.set("False")
    business_var.set("False")
    graphic_design_var.set("False")
  
  def search_for_organization():
    searchquery = ("""
                   SELECT *
                   FROM FBLA_PROJECT.dbo.partners
                   WHERE partner_name =(?)
                   """)
    cursor.execute(searchquery, (search_var.get(),))
    search_result = cursor.fetchall()
    if search_result == []:
      update_listbox()
    else:
      listbox.delete(0, tk.END)
      j = list(search_result[0])
      insert_listbox = (j[0] + " | " + j[5])
      listbox.insert(tk.END, insert_listbox)
  
  try:
    
    # Gets the password from username in database and compares the result to the password given by user #
    query = ("""
             SELECT * 
             FROM FBLA_PROJECT.dbo.users 
             WHERE Username =(?)
             """)
    cursor.execute(query, (user_var_login.get(),))
    result = cursor.fetchone()

    if (list(result))[1] == pass_var_login.get(): 



      # withdraws login window and sets the geometry for the data window #
      main.withdraw()
      data_window = tk.Toplevel()
      data_window.title("Main Page")
      data_window.geometry("400x500")
      data_window.configure(bg="steelblue")
      
      # Menu Bar #
      menu_bar = tk.Menu(data_window)
      menu_1 = tk.Menu(menu_bar, tearoff=0)
      menu_2 = tk.Menu(menu_bar, tearoff=0)
      menu_4 = tk.Menu(menu_bar, tearoff=0)
      # If the user is an admin, an extra menu bar item named 'admin' is added with admin abilites #
      if str(user_perm.get()) == "admin":
        
        # sets the cascade onto the menu bar #
        menu_3 = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Admin", menu=menu_3)
        
        # runs function that lets you add partners #
        menu_3.add_command(label="Add Item", command=lambda:[add_window()], image=plus_image, compound='left')
        
        # runs function that lets you remove partners #
        menu_3.add_command(label="Remove Item", command=lambda:[delete_window()])
        
        # lets you view all users and pending users #
        menu_3.add_command(label="All Users", command=view_users)

        # configures cascade to menu bar #
        data_window.config(menu=menu_bar)

      # button logs user out and brings back the login page #
      menu_1.add_command(label="Log Out", command=lambda:[data_window.withdraw(),main.deiconify()], image=logout_image, compound="left")

      # button sorts list from A-Z #
      menu_4.add_command(label="A-Z", command=lambda: [alphabetical_listbox()])
      
      # button sorts from Z-A #
      menu_4.add_command(label="Z-A", command=lambda: [realphabetical_listbox()])
      # configures the filter casecade #
      filter_menu = tk.Menu(menu_2, tearoff=0)

      # sections of the filter menu #
      ps_menu = tk.Menu(filter_menu, tearoff=0)
      purpose_menu = tk.Menu(filter_menu, tearoff=0)
      pathway_menu = tk.Menu(filter_menu, tearoff=0)

      # adds check buttons for product/service cascade #
      ps_menu.add_checkbutton(label='Product', 
        variable=product_var, onvalue='True', offvalue='False')
      ps_menu.add_checkbutton(label='Service', 
        variable=service_var, onvalue='True', offvalue='False')
      
      # adds check buttons for purpose cascade #
      purpose_menu.add_checkbutton(label='Hardware', 
        variable=hardware_var, onvalue='True', offvalue='False')
      purpose_menu.add_checkbutton(label='Financial', 
        variable=financial_var, onvalue='True', offvalue='False')
      purpose_menu.add_checkbutton(label="Info", 
        variable = info_var, onvalue='True', offvalue="False")
      
      # adds check buttons for pathways #

      pathway_menu.add_checkbutton(label='Mechatronics', 
        variable=mechatronics_var, onvalue='True', offvalue='False')
      pathway_menu.add_checkbutton(label='Computer Science', 
        variable=computer_science_var, onvalue='True', offvalue='False')
      pathway_menu.add_checkbutton(label='Cybersecurity', 
        variable=cybersecurity_var, onvalue='True', offvalue='False')
      pathway_menu.add_checkbutton(label='Healthcare', 
        variable=healthcare_var, onvalue='True', offvalue='False')     
      pathway_menu.add_checkbutton(label='Aerospace', 
        variable=aerospace_var, onvalue='True', offvalue='False')
      pathway_menu.add_checkbutton(label='First Responders', 
        variable=first_responders_var, onvalue='True', offvalue='False')
      pathway_menu.add_checkbutton(label='Business', 
        variable=business_var, onvalue='True', offvalue='False')
      pathway_menu.add_checkbutton(label='Graphic Design', 
        variable=graphic_design_var, onvalue='True', offvalue='False')
      #configures cascades #
      filter_menu.add_cascade(label='Product/Service', menu=ps_menu)
      filter_menu.add_cascade(label='Relation', menu=purpose_menu)
      filter_menu.add_cascade(label='Pathway',menu = pathway_menu )


      # adds cascades onto menu bar #
      menu_2.add_cascade(label="Filter", menu=filter_menu, image=filter_image, compound="left")
      menu_bar.add_cascade(label="Account", menu=menu_1)
      menu_bar.add_cascade(label="Options", menu=menu_2)
      menu_bar.add_cascade(label="Sort", menu = menu_4)
      # applies the filters that were selected #
      menu_bar.add_command(label="Apply Filter", command =lambda: [combine_filter()])

      # clears the filters selected #      
      menu_bar.add_command(label="Clear Filter", command = lambda: [update_listbox(), clear_checkbox()])
      data_window.config(menu=menu_bar)
      

      # creates search bar and search button #
      search = tk.Entry(data_window, textvariable=search_var)
      search.place(width=180, relx=0.12, rely=0.1)
      searchbutton = tk.Button(data_window, command=lambda: [search_for_organization()], text='Search')
      searchbutton.place(width=60, height=25, relx=0.6, rely=0.095)

      # creates more-info button #
      info_button = tk.Button(data_window, command=lambda: [info_box_window()], text="More Info")
      info_button.place(width=70, height=25, relx=0.8, rely=0.095)

      # configures the listbox for data as well as the scrollbar for it #
      scrollbar = tk.Scrollbar(data_window)
      listbox = tk.Listbox(data_window, width=60, height=20, selectmode=tk.SINGLE, justify="left")
      scrollbar.place(relx=0.45, rely=0.5, anchor=tk.CENTER)
      listbox.place(relx=0.50, rely=0.5, anchor=tk.CENTER)
      listbox.config(yscrollcommand = scrollbar.set)
      scrollbar.config(command = listbox.yview)
      
      # gets data for partner listbox #
      cursor.execute("""
                     SELECT * 
                     FROM FBLA_PROJECT.dbo.partners
                     """)
      result2 = list(cursor.fetchall())
      
      for i in range(len(result2)):
        j = list(result2[i])
        
        info12 = (j[0] + " " + ("-"*(30-(len(j[0])))) + " " + j[5])
        listbox.insert(tk.END, info12)


    else:
      # shows error messagebox saying that the password for the user is incorrect #
      messagebox.showerror("Error","Password is incorrect!") 
  except TypeError:
    
    # shows error messagebox saying that the username for the user does not exist #
    user_var_login.set("")
    pass_var_login.set("")
    messagebox.showerror("Error", "Username doesn't exist!")  
  
main.mainloop()