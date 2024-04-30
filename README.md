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

![Screenshot (587)](https://github.com/meghan013/OnlineVoting/assets/128183027/9dce0b9a-bd6a-4631-85b5-c8c7d8f388ac)

![Screenshot (588)](https://github.com/meghan013/OnlineVoting/assets/128183027/7a2f4d50-531a-4973-b6a5-82c36f7ff45c)

![Screenshot (589)](https://github.com/meghan013/OnlineVoting/assets/128183027/0820992c-1ea0-4e9f-b305-b3e8b54d6b80)

![Screenshot (590)](https://github.com/meghan013/OnlineVoting/assets/128183027/7e08e05c-d660-454d-93fe-ee9f16cc4dc0)

![Screenshot (591)](https://github.com/meghan013/OnlineVoting/assets/128183027/6ef3d45a-828e-438f-bfa5-e0f9a252c603)

![Screenshot (592)](https://github.com/meghan013/OnlineVoting/assets/128183027/1ef71265-54c3-4726-aad0-c757575bc8c0)

![Screenshot (593)](https://github.com/meghan013/OnlineVoting/assets/128183027/bb1970b8-d553-4a8c-bd2b-29ff6495b37b)

![Screenshot (594)](https://github.com/meghan013/OnlineVoting/assets/128183027/be8b296f-c675-43ba-b000-33547b1ac68f)

![Screenshot (595)](https://github.com/meghan013/OnlineVoting/assets/128183027/3638ed3d-7875-425d-8a4b-5a3fc28e851f)

![Screenshot (595)](https://github.com/meghan013/OnlineVoting/assets/128183027/e02dbae8-e162-4778-8952-aba43e036584)















