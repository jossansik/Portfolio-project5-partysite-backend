# Portfolio Project 5 PartyDimension social community and inspirational website
 
PartyDimension social community and inspirational website
 
## Table of contents
 
* [About this project](https://github.com/jossansik/Portfolio-project5-partysite-backend#About-this-project)
* [Technology](https://github.com/jossansik/Portfolio-project5-partysite-backend#Technology)
* [Setup project locally](https://github.com/jossansik/Portfolio-project5-partysite-backend#Setup-project-locally)
* [Features & site goals](https://github.com/jossansik/Portfolio-project5-partysite-backend#Features-&-site-goals)
* [Site experience](https://github.com/jossansik/Portfolio-project5-partysite-backend#Site-experience)
* [Testing](https://github.com/jossansik/Portfolio-project5-partysite-backend#Testing)
* [Issues](https://github.com/jossansik/Portfolio-project5-partysite-backend#Issues)
* [Validator testing](https://github.com/jossansik/Portfolio-project5-partysite-backend#Validator-testing)
* [Deployment](https://github.com/jossansik/Portfolio-project5-partysite-backend#Deployment)
* [Credits](https://github.com/jossansik/Portfolio-project5-partysite-backend#Credits)
 
## About this project
 
This project is a a content-sharing web application with React and an API (Django Rest Framework) Back-End. This allows the users to browse and comment/like each other's content as well as add and delete their own. The users can also bookmark content.

The basic concept of this website is: user built, user driven. Meaning that the main asset of the site will be the users' own contributed material and that the interactions between the users and the integrated technologies should be meaningful, informative and results driven.

Party themed, having different choices of themes for parties is the main concept.

Features and functionalities include Sharing and collecting. Sharing your own ideas and thoughts, collecting and saving others ideas for the future.

Because of the wide span of the subject, the target group is very broad and multifaceted in terms of age and other demographics.

This site is for everyone who is looking for creative ideas or tips about everything concearning parties and other social events. A user can be anybody thinking of throwing parties or just looking for inspiration for the future. Guiding principles for the website will be family-friendly, fun, creative & inspiring.

Goal - The goal for this project was To build a community that make it easy and fun for party planners and guest to organize and find ideas, to inspire creativity and make the process more fun and exciting.

The project is divided into two repositories, this one for the back-end (this) and one for the front-end, found [here](https://github.com/jossansik/Portfolio-project5-partysite-frontend).
As Agile methodology during the development process of planning and designing this project Github Issues was used for user stories and Github Projects for kanban board.
 
The project board is found [here](https://github.com/users/jossansik/projects/7). 
The project board consists of both frontend and backend user stories to make the project objective coherent.

![image](https://user-images.githubusercontent.com/92020968/204350921-8f701e9c-33dd-4b66-b3be-1b05701aeb34.png)
 
The project is deployed through [Heroku](https://heroku.com) and accessed at https://partysite-api.herokuapp.com/.
 
## Technology
 
This project is built with Python+Django, using [Heroku Postgres](https://www.heroku.com/postgres) as relational database. The application is run, operated and deployed through Heroku.
 
Images and media are uploaded and stored through [Cloudinary](https://cloudinary.com).
 
### Data schema
 
The chart below fully describes the data scema:
 
![database_schema](https://user-images.githubusercontent.com/92020968/198819865-52865466-7b14-4fc3-b386-5956d54e4cf4.png)

All data models except for Bookmark, Category, Comment, Like, Post, Profile and Tag is default generated by django.
 
## Setup project locally
 
### Pre-requirements:
 
VS Code, Python.
 
env.py with following properties:
- import os
- os.environ["DATABASE_URL"]
- os.environ["SECRET_KEY"]
- os.environ["CLOUDINARY_URL"]
- os.environ["DEV"]
- os.environ["CLIENT_ORIGIN"]
 
### Installation
 
- Git clone - To get all code to your computer locally
- cmd: 'python3 -m venv venv' - To get a local python environment
- cmd: 'source venv/bin/activate' - To activate the new python environment
- cmd: 'pip3 install -r requirements.txt' - To get all python dependencies installed
- (cmd: 'python3 manage.py migrate' - To get all tables generated in database) Only if no database exists.
- cmd: 'python3 manage.py runserver' - To start a local instance

### Business Vision:
 
Description: The vision is to create an inspiring, user-driven web community for everyone who is looking for creative ideas or tips about everything concearning parties and other social events. A user can be anybody thinking of throwing parties or just looking for inspiration for the future. Guiding principles for the website will be family-friendly, fun, creative and inspiring.
 
Target Groups: Because of the wide span of the subject, the target group is very broad and multifaceted in terms of age and other demographics.
 
Needs: User need to find a site where the can find the party content fast and in a easy way
 
Business goals: A goal could be make the site to a place where differents venues and other businesses would like to advertise.
 
Product: An inspirational party themed DIY web site/content-sharing platform.

## Features & site goals
 
### Super admin goals
 
- Admin can log in 
- Admin can log out
- Admin can administrate all features

### Site admin goals
Features for (staff) adminwebsite

- Can manage categories
- Can manage tags

## Site experience

### Features for (superadmin) adminwebsite

![image](https://user-images.githubusercontent.com/92020968/198821024-292392e7-3c4a-48c0-a754-ab25c5102ea1.png)

### Features for (site admin) adminwebsite

![image](https://user-images.githubusercontent.com/92020968/198821046-39faa425-cd12-401a-87bd-78c8b6751ba6.png)

## Postman
Postmas is able to verify and use features directly against the api. It is included in the project.

To login use 'Login' rest availability in Postman. When used you will get a cookie, check the 'Cookies' section and verify:

![image](https://user-images.githubusercontent.com/92020968/198820263-b138c212-190a-4995-9507-e8dd32ea4957.png)
![image](https://user-images.githubusercontent.com/92020968/198820276-8708d234-99e1-4943-a8c5-bd59dc14c271.png)

To acces content postman will automatically use the created cookie. BUT you will need to add X-CSRFToken as a header, it is found in one of the cookies, just copy and insert, see image:

![image](https://user-images.githubusercontent.com/92020968/198820373-ed4a8f4d-9c9c-47dc-93e1-197ae01dc876.png)
![image](https://user-images.githubusercontent.com/92020968/198820338-f83a4e49-fbeb-4627-a5ce-29fdb6cc1d1f.png)

## Testing
 
### Python tests
 
To run tests, run the following command: coverage run manage.py test posts -v 2
 
Located in posts/tests.py and tests only functions in services.py.
 
#### Tests for adding tags to post is located in: AddTagsToPostTest.
 
1. test_can_add_tag_to_post:
 
When there are one tag submitted to a post, it should be connected. Then we should find the post by tag submitted.

2. test_when_no_tags_submitted_expect_no_tags_on_post:

When there are no tag submitted to a post, it should not be connected to any tags. Then we should not find any post for the tag.

3. test_when_two_tags_submitted_expect_match_on_both_tags:

When there are two tags submitted to a post, it should be connected to both tags. Then we should be able to find post by both tags.

## Issues

### Third-Party Cookies on different Web/Mobile Browsers
Due to project requirements with website in separate domains the cookie cannot be shared and therefore it is a problem in Safari and mobile which does not allow cross-site tracking. It is however possible to turn it of in mobile, here is how you do it:
![image](https://user-images.githubusercontent.com/92020968/198820423-ff5a080f-0b00-4e5f-ab5c-0fe6358f2e40.png)

If the task did not require multiple projects I would have used an approach where I had put the website in the same domain with a proxy.

### Admin web and website cookie
A known issue is that if a administrator log in to admin web and then visits website the cookie is not valid so the admin has to log out before using website.

## Validator testing
 
### Python validation
All the python files pass validator testing pep8online without issues, except for the settings.py file in startsite which is auto-generated by django. This file gets 'E501 line too long' on AUTH_PASSWORD_VALIDATORS. I do not like to change this since it is auto-generated.
 
![pep8_validation](https://user-images.githubusercontent.com/92020968/181763626-c7229c1e-ba16-4e0f-867a-b63333f0998e.png)

## Deployment
 
Initial step for creating a app in Heroku:
 
- Created an account on Heroku.com (from the Heroku dashboard clicked the “Create new app” button).
- Named the app "partysite-api"
- Selected region (Europe), then clicked “Create app”.

Using Heroku for deployment, here is the overview:
![image](https://user-images.githubusercontent.com/92020968/198820638-dd0f4cf5-7604-49da-8bea-e53d2cb703ae.png)

The settings in Heroku for my app:
![image](https://user-images.githubusercontent.com/92020968/198820672-98cb8376-ab60-4214-80be-37805ba1534c.png)

## Credits
Wireframes and mockups, as well as images and vectors used on the website were made using [Figma](https://figma.com/)

Data schema is created with [graphviz](https://graphviz.org/)

Alot of code is based on this project [drf-api](https://github.com/Code-Institute-Solutions/drf-api)
