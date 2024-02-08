Organization Search Engine
This project is a search engine designed to filter organizations based on specified criteria. It provides users with the ability to search for organizations and apply various filters to refine their search results.

Objective
The main objective of this project is to facilitate the search for organizations by allowing users to filter the results based on different attributes. Users can specify the criteria they are interested in, such as the type of organization, location, industry, size, etc., and the search engine will return relevant results matching those criteria.

Features
Search Functionality: Users can input keywords to search for specific organizations.
Filtering: Users can apply filters to narrow down search results based on various attributes such as organization type, location, industry, size, etc.
Dynamic Results: The search engine dynamically updates the results based on the applied filters and search queries.
User-Friendly Interface: The interface is designed to be user-friendly and intuitive, enabling users to quickly find the information they are looking for.
User Signup: Users can sign up, becoming pending until admin approval.
Admin Approval: Administrators can accept or deny pending user requests.
Role Administration: Admins can manage user roles within the system.
Partner Management: Users can add and delete partner organizations.

Technologies Used
Python: The backend logic and search algorithms are implemented using Python.
Tkinter: GUI is developed using Tkinter, a Python library for creating desktop applications.
SQL: For data storage and management, SQL (Structured Query Language) is utilized along with SSMS (SQL Server Management Studio).

Usage
If an account does not exist: Sign up (input username and password/password confirmation.)
With account (non-admin): Login, then use the filters to narrow the organizations you are looking for, which you can sort from either A-Z or Z-A.
With account (admin): On top of being able to use the search engine, you can add/remove organization entries and either promote(give an account admin permissions) or demote(remove an account's admin permissions) other accounts. 

Installation
Clone the repository to your local machine:
git clone https://github.com/AlexeyPlagov07/FBLA_Project.git

Navigate to the project directory:
cd FBLA_Project

Run the application:
python main.py

Use the search bar to enter keywords for organizations you want to search for.
Apply filters to narrow down the search results based on specific criteria.
View the dynamically updated search results.
Explore the details of each organization and use the information as needed.

Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow the standard GitHub flow:
Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Create a new Pull Request.

License
This project is licensed under the MIT License - see [the LICENSE file](https://choosealicense.com/licenses/mit/) for details.
