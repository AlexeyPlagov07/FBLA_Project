# FBLA Project
A search engine that allows users to sift through various organizations based on varying aspects (what the organization offers, what pathway it relates to, etc.) and sort by alphabetical order to find an organization that aligns with what the user is looking for

## Objective
The main objective of this project is to facilitate the search for organizations by allowing users to filter the results based on different attributes. Users can use the given filters to sort through what does and doesn't align with what they are looking for, such as the type of organization, location, industry, size, etc., and the search engine will return relevant results matching those criteria.

## Features
Search Functionality: Users can input keywords to search for specific organizations, and can apply filters to narrow down search results based on their needs.
User Signup: Users can create accounts (pending until an admin approves the request.)
Administration: Admins can manage user roles within the system, approve/deny user sign-up requests, and add/delete/edit partner organizations in the database.

## Technologies Used
Python: The backend logic and search algorithms are implemented using Python.
Tkinter: GUI is developed using Tkinter, a Python library for creating desktop applications.
SQL: For data storage and management, SQL (Structured Query Language) is utilized along with SSMS (SQL Server Management Studio).

## Usage
If an account does not exist: Sign up (input username and password/password confirmation.)
With account (non-admin): Login, then use the filters to narrow the organizations you are looking for, which you can sort from either A-Z or Z-A.
With account (admin): On top of being able to use the search engine, you can add/remove organization entries and either promote(give an account admin permissions) or demote(remove an account's admin permissions) other accounts. 

## Installation
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

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow the standard GitHub flow:
Fork the repository.
Create a new branch (git checkout -b feature/new-feature).
Make your changes.
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature/new-feature).
Create a new Pull Request.

## License
This project is licensed under the MIT License - see [the LICENSE file](https://choosealicense.com/licenses/mit/) for details.
