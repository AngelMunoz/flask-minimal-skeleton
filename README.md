#### NOTE:
I made this when I was starting web development overall if there are old patterns and stuff you see it's a bad practice please raise an issue or make a pr :) I'd gladly accept it thanks

# Hello everyone!
This is a flask application using blueprints.
Blueprints are really good when one of the concerns is scalable apps.
each "blueprint" is what we could call a module, the application here is composed of two modules
`auth` and `admin` as the names suggest, auth is the module in charge of authentication and user session and allowing
where can users go or can not.

admin is a module that emulates a very simple administration website

the website is composed of a user who has a company and said company may have many subsidiaries, each subsidiary may have several employees.

while is not such a complex scenario, it shows you some concepts of the modern web development.

the application logic is a MVC workflow structure
where each module has its own controller and its own views, however the models work for the whole application.
each module will contain its own readme file explaining what is done there.

Have a nice day! oh by the way! this app is hosted in Heroku (thank you continuous deployment!)
which picks the files in github and serves them and updates as soon as the repository is updated.


## UPDATE 10/10/2017
Added new Files
- `.env`
- `Pipfile/Pipfile.lock`

You aren't likely to put `.env` into source control but I put it here for completeness.

Added Pipfile/Pipfile.lock these is an amazing way to keep your python dependencies management under control.
(it even loads .env files!) check more about it [here](https://github.com/kennethreitz/pipenv)
### Misc.
- Fixed Sign up form
- Updated dependencies
- Fixed some warning deprecation messages
