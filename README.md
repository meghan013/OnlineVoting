Django Online Voting System

Introduction

This project is an Online Voting System developed using Django, a high-level Python web framework. The system allows users to vote for candidates in various polls conducted online.

Features

User authentication: Users can register, login, and manage their accounts. Poll creation: Admin users can create polls with a list of candidates. Voting: Registered users can vote for their preferred candidates in each poll. Results display: After voting ends, the system displays the results of each poll.

Project Structure

.idea: Contains IDE-specific configuration files (e.g., for PyCharm). Online_Voting_System: Django project directory. media: Directory for storing uploaded files (e.g., candidate images). candidates: Directory for storing candidate-related files. onlineVotingSystem: Django app directory. poll: Django app responsible for managing polls. migrations: Database migrations for the poll app. templates: HTML templates for rendering poll-related views. admin.py: Admin configurations for poll models. forms.py: Forms for poll-related data input. models.py: Database models for polls and candidates. tests.py: Test cases for poll-related functionality. tokens.py: Token generation for poll-related operations. validators.py: Custom validators for poll data. views.py: Views for handling poll-related HTTP requests. manage.py: Django's command-line utility for various project tasks.

Installation

Clone the repository: git clone <repository_url> Navigate to the project directory: cd Django_Online_Voting_System Install dependencies: pip install -r requirements.txt Run migrations: python manage.py migrate Create a superuser (admin): python manage.py createsuperuser Start the development server: python manage.py runserver

Usage

Access the admin panel by visiting http://localhost:8000/admin (login with superuser credentials). Create polls and add candidates through the admin interface. Users can register and log in to vote for candidates in polls.

Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository Create your feature branch (git checkout -b feature/YourFeature) Commit your changes (git commit -am 'Add some feature') Push to the branch (git push origin feature/YourFeature) Create a new Pull Request

OUTPUT:


![image](https://github.com/kesavaTDP/Online_Voting_System/assets/141147408/913d2575-232f-4232-b098-4c118540c1ea)

![image](https://github.com/kesavaTDP/Online_Voting_System/assets/141147408/3f03ec1f-64c0-4b4e-a0c4-29294217b869)

![image](https://github.com/kesavaTDP/Online_Voting_System/assets/141147408/c486a5d2-79b4-42ac-adf9-6ff7753e435a)

![image](https://github.com/kesavaTDP/Online_Voting_System/assets/141147408/33ce4023-8ced-48f0-a608-66210f5100b9)

![image](https://github.com/kesavaTDP/Online_Voting_System/assets/141147408/7a4855b3-70b6-43ab-afd5-62f6d48678c0)

![image](https://github.com/kesavaTDP/Online_Voting_System/assets/141147408/595ee189-af19-495b-b0c0-92452a568f78)

![image](https://github.com/kesavaTDP/Online_Voting_System/assets/141147408/0579daa4-0b4e-4f89-89cd-0c1f9fc1a219)

![image](https://github.com/kesavaTDP/Online_Voting_System/assets/141147408/96e79b3b-1ff9-4ea4-a8b2-b099a1bb5702)

