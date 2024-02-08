# FBLA 2024 SLC Coding and Programming project submission
### Alexey Plagov, Nitish Kaluvakolli, and Yashas Herunde  

# Project Description
The use of this project revolves around being able to filter and sort through school and/or academic partners/sponsors. In this project, 30 partners are listed, 
but code is made for custom use. This project uses an outside SQL server and must be downloaded seperate from the code provided. In our code, SSMS was used as the SQL server
manager and used microsoft azure as the server host. Server log-on is included at the beggining of the code. Tkinter was used for the project GUI, since python was the main
language used in the script. Also outside png images were used in the code for asthetic purposes so downloading the two image folders in the repository branch are 
vital for the code and images can be replaced with ones that are needed for the specific case. Features used in the project include filtering through copmany resource, 
pathway, and whether they provide a product or service. Also includes a A-Z and Z-A sorting feature and advanced security concerning logins and sign-ups. 
Future features might include timed-logout and editing partner info.

# Project Installation and Setup
For this project, a few libraries are needed to run the software. Before installing libraries, place the python script into a folder and 
```
cd *Folder Name*
```
to go into your folder.
Then, an outside SQL server will be needed to run the software and setup of server connection will have to 
be done in the code. For python to be able to connect to the SQL server, the **pypyodbc** library was used to install:
```
pip install pypyodbc
```
To run in Visual Studio Code, the library file will have to be placed inside the [python script](https://github.com/AlexeyPlagov07/FBLA_Project/blob/Master/pypyodbc.py) folder when run. Otherwise, if running in CMD or another method, the file isn't 
needed. When setting up your SQL server, make sure your database has three tables: *users*, *partners*, and *pending_users*. For the table *users*, the columns in the table 
include *Username*, *pword*, and *role1*. Same setup for the *pending users* table. For the *partners* table, the columns include *partner_name*, *organization*,
*product/service*, *available_resource*, *pathway*, and *contact*.
Also to run the code, the tkinter module "tool tip" will be needed to be able to use the tool tip module which adds comments on buttons. To install:
```
pip install ToolTip
```
To run in Visual Studio Code, the library file will have to be placed inside the [python script](https://github.com/AlexeyPlagov07/FBLA_Project/blob/Master/tooltip.py) folder when run. Otherwise, if running in CMD or another method, the file isn't 
needed.
For all the images to load the two image folders ([partner_images](https://github.com/AlexeyPlagov07/FBLA_Project/tree/Master/partner_images) and [icons](https://github.com/AlexeyPlagov07/FBLA_Project/tree/Master/icons))
will be needed to display images in the tkinter windows. Once all the files are in the folder with the project, the project is ready to run, in Visual Studio Code, or in command line.
To run on command line, make sure you're in the project directory and type:
```
python fbla_proj.py
```
to run the code. If done correctly, a blue window should open up with login  and signup buttons.

# Project Use 
## Login and Sign Up Process 
When the code is run, a window should appear that has two entry boxes and two buttons labeled: *Log in* and *Sign up*. For you to be able to log in, you would already have to
be part of the users table in the database. If already in database as user or admin, type into the entryboxes your username and password and select **login**. If not a user, 
click the sign up button and fill out the form. Enter username, password, and re-enter to add to security measures. If username already exists, then you won't be able to create 
an account. Same goes with not matching passwords. If username is unique and passwords identical, press sign up and your data will be placed into the pending_users table in the database.
When logged in, to sign out, press the section **Account** in the menu bar, and press *logout*.
## Using Filter and Sort Features
Main part of the project was the filter and sort features. At the top of the window when logged in, there will be menu bar which will display *Options*, *Apply Filter*, and 
*Clear FIlter*. To select filters, navigate to *Options* and then to *Filters*, where then, based on *Product/Service*, *Relation*, and *Pathway*, you'll get to choose whcih filter to apply.
When filters are selected, click the *Apply Filter* button to apply filter and only partners that apply to the chosen filters will be shown. **When using filters, stackable filters 
are based in each category.** When filtered, it will only show partners that fit all the filters. To sort, navigate to *Options*, and *Sort*, and select **A-Z**, which is alphabetical,
and **Z-A** which is reverse-alphabetical. To clear filter and sorting, click the **Clear Filter** button to return the listbox to original state.
## Using Search Feature
To search, enter partner name into the bar and click the **Search** button. If enetered correctly, the only partner in the listbox will be the one searched for, otherwise
code will return error stating *Partner is not in table*.
## Using *More Info* Feature
When browsing through partners, you can select one in the listbox. The partner you clicked on should turn blue, and you can select to **More Info** button. When selected, a 
window will open up displaying the partner logo, the business type, whether a product or service is provided, what resource it gives to the school, the main pathway it affects,
and their contact. ALso at the bottom, there will be a short paragraph explaining the company and describing how the partner further helps the school and/or pathway.
## Using Administrator Tools
Administrator tools consist of 
1. Adding partners
2. Deleting Partners
3. Managing Users
### Adding partners
When adding partners, navigate to the *admin* menubar cascade, and select *Add Item*. When selected, a window will open with entry boxes to fill. Fill out accordingly, and
click **Add Partner**. A confirmation window will open if this is a unique partner, and error if this is a reoccuring one.
### Deleteing partners
Navigate to the *admin* meunbar cascade, and select *Remove Item*. When selected, a window will open and to delete partner, enter the partner name in the box, and select 
**Delete Partner**. if partner is system, it will be deleted, if not, error will pop up.
### Managing Users
When managing users you can accept and deny pending users, and change roles of and delete current users. To navigate to the page, go to the *admin* menubar cascade, and select
the *All Users* button. It will open a window with two textboxes: Left one is for current users and right one is for pending users. Under the current users listbox, there are two buttons.
To change the role of a user, select the user in the listbox on the left, and click **Change Role**, this will change the role from Admin --> User, or User --> Admin. Then the
listbox will update. To Delete user, select user in listbox to the left, and click **Remove User**. This will remove user from database and update the listbox. To accept pending users,
select the user in the right listbox and click button **Accept User**, and the user will be switched over from *pending users* --> *users*. To deny, select user in the right listbox,
and click the button **Deny User**, and the pending user is deleted.
# Credits
This project was done as a result of the Future Business Leaders of America Coding and Programming challenge and was built and managed by Alexey Plagov, Nitish Kaluvakolli, and Yashas Herunde.
