<img src="https://andeweg-festival-zvl.s3.amazonaws.com/media/FestivalZVL_logo.png" style="margin: 0;">

# Festival-zvl (Festival van Zeeuwsch-Vlaanderen)

For over 30 years the Festival van Zeeuwsch-Vlaanderen has been the biggest festival for classical music in Zeeuwsch-Vlaanderen (Zealand's Flanders). This is the Dutch part of Flanders, disconnected from The Netherlands by the River Scheldt. A quiet, rural, but culturally rich area. This is where different venues form the stage for the festival. 
Over ten years I've had the privilege to create the program brochures, different printed material and the website. However, the ticket sale has always been outsourced to a local theater. This has meant an extra step for the visitor to buy tickets on a secondary website, away from the main site. The festival manager wants one-stop-shop. Having the tools now to build e-commerce sites will make it possible to have all the elements for one-stop-shopping on the main site.

 
## UX
 
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_1.jpg?raw=true" style="margin: 0;">
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_3.jpg?raw=true" style="margin: 0;">
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_4.jpg?raw=true" style="margin: 0;">
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_5.jpg?raw=true" style="margin: 0;">


## Features

 
### Existing Features

##### Navbar:
Provides the festival logo, and links to the 'concerts', additional 'ticket information', the 'locations' of concerts, 
the 'previous' editions/years of the festival, a page with 'sponsoring' information and 'media' which holds some footage
from previous years, interviews and previews. 
On small screens the navigation collapses into a hamburger menu (MDBootstrap).

##### MDBootstrap Caroussel
On some pages a caroussel with a selection of images is shown. This is a MDBootstrap addon by Marta Szymanska using css and JavaScript.

##### Selection options:
'Concerts' shows all concerts, under 'locations' you can view the concerts per location (the nature of the festival is that
mostly local people visit and like to see what's the nearest concert available), under 'previous' the concerts per year or
edition can be filtered.

##### Concert presentation:
The results are shown on the concert page as tweaked MDBootstrap cards with, when populated, the fields available for the concert,
edition and location. 

##### Ticket information:
The original website has more information here, since the ticket sales are outsourced, but some information on returning tickets
and buying at the location is given here if someone would wish not to buy online.

##### Locations:
Concerts per location can be shown here.

##### Previous:
We're about to start the 32nd edition of the festival and a lot of digital material and information is still available. So here
the previous editions can be populated to serve as a catalogue and impression of what the festival stands for.

##### Sponsoring:
This years' sponsors are presented and the main sponsor presents an editorial on it's cultural plans and involvement.

##### Media
A page with footage of previous editions, interviews and previews for the current edition.

##### Profile
Non-authorized users can create a profile, login when they have a profile, see their profile with purchase history and logout.
The site owner (superuser) can also add, delete and edit concerts. 

##### Shopping cart 
As the shopper is buying tickets, the total price gets updated. Clicking the cart shows the contents with the possibility to
in/decrease the amount of tickets, delete a concert from the basket and go to the checkout to pay and enter or edit personal
and delivery details.
Payments are handled with [Stripe](http://www.strip.com).

##### Toasts
Toasts provide messages when the user interacts with the system. Success messages, warnings, error messages; they give the
user a lot of clarity about how their action work out.


### Features Left to Implement
- Locations in the database can be used to implement Google Maps functionality: creating directions and showing the location on the map.
- For more easily populating the database a time/date picker can be implemented.
- Counter for the amount of tickets sold


## Technologies and API's used

### Front-end
* [HTML5](https://en.wikipedia.org/wiki/HTML5) for the HTML structure.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) for styling and editing existing (MD)Bootstrap css-code
* [FontAwesome]() version 5.8.2. used for icons
* [Google Fonts](https://fonts.google.com/) for using the fonts Raleway and Satisfy
* [MDBootstrap](https://mdbootstrap.com/) framework version 4.19.1 is used for the navbar, forms, cards and much of the css code.  
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) version 3.2.1 is used to work with JQuery, Bootstrap, 
    small snippets of code to make the user scroll back to the top, the Caroussel.
* [JQuery](https://jquery.com) which manipulates the DOM

### Back-end
* [Python](https://www.python.org/) (version 3.8.2) for running the python app
* [Django](https://www.djangoproject.com/) The Python based framework that binds the
Python apps and makes development a very quick and reasonably easy project.
* [Jinja](https://palletsprojects.com/p/jinja) for templating
* [GitHub](https://github.com) for version control and storing the repositories
* [GitPod](https://www.gitpod.io) the online IDE for coding, testing and debugging
* [Heroku](https://www.heroku.com) the cloud application platform used to deploy the Python application
* [Postgres](https://www.postgresql.org/) an open source relational database running on Heroku
* [Amazon Cloud Services](https://aws.amazon.com/) the static files are served on S3
* [Stripe](https://www.stripe.com) A complete payment system with webhook handler as a safety net implemented


## Testing

### testing code
The Python code was checked with [Pep8](http://pep8online.com) and lots of linting, indentation and minor issues were caught with that.
The HTML and CSS was validated with the [W3 validator](https://validator.w3.org/) and after making some minor changes very few errors were found.
The errors left in the HTML were inside the Caroussel code which I rather left untouched since everything works.
Throughout the development I kept a close eye on the inspect in Chrome to detect any errors in js code, css or html or any paths not working correctly.
Also the debugging in GitPod give a lot of clues when stuck on a bug. Printing in the console is a good method to check the process and flow of data.

During the process and especially after finishing the coding the following was tested on 
* desktop
* mobile
as 
* authorised user
* unauthorized user
* and site owner

#### Styling
- responsiveness: The choice was to make this a desktop first site and it definitely looks best on desktop, but on mobile everything works and looks good too.
- navigation: All links work well, no surprises going forth and back through the site and it's clear everywhere what action to take (next).
- use of colour and typography: At all times text is well readable and has good contrast. Rollovers have been made more subtle here and there and the the blue
with some yellow here and there look pleasant and have a style that suit the site.

#### CRUD functionality
- Site owner on the database: The site owner can add, delete and edit concerts. This is all working well. Unused fields do not show and the presentation of the data looks good.
- Shopper in the order process: In the shopping cart the user can increase or decrease the amount of tickets or delete the concert from the order. No issues there.

#### Order process
No issues when ordering. Payments are done with Stripe (webhooks show successfully in Stripe dashboard).
After submitting the payment with the test creditcartnumber, the order is shown and confirmation email is sent to the correct address. 
Orders are stored in the user profile and can be seen in the profile view afterwards. 
 

## DEPLOYMENT

### The process:
* In GitHub a repository with full template by the CodeInstitute is generated for use with GitPod.
* In GitPod a site is built with [Django](https://www.djangoproject.com/)
* packages installed for this project are:
    - asgiref==3.2.10
    - boto3==1.14.51
    - botocore==1.17.51
    - dj-database-url==0.5.0
    - Django==3.1
    - django-allauth==0.42.0
    - django-countries==6.1.3
    - django-crispy-forms==1.9.2
    - django-heroku==0.3.1
    - django-storages==1.10
    - docutils==0.15.2
    - gunicorn==20.0.4
    - jmespath==0.10.0
    - oauthlib==3.1.0
    - Pillow==7.2.0
    - psycopg2==2.8.5
    - psycopg2-binary==2.8.5
    - python-dateutil==2.8.1
    - python3-openid==3.2.0
    - pytz==2020.1
    - requests-oauthlib==1.3.0
    - vs3transfer==0.3.3
    - sqlparse==0.3.1
    - stripe==2.50.0
    - unicorn==1.0.1
    - whitenoise==5.2.0
 
    These are stored in the file requirements.txt by using the command: `pip3 freeze --local > requirements.txt`
    So these requirements can easily be loaded again by typing `pip3 install -r requirements.txt`

* In Heroku the app has to be created to be able to run later. 
* It's important to have the following variables in Heroku set:
    - AWS_ACCESS_KEY_ID (connect to AWS)
    - AWS_SECRET_ACCESS_KEY
    - DATABASE_URL (Postgres)
    - EMAIL_HOST_PASS (for email functionality)
    - EMAIL_HOST_USER
    - SECRET_KEY (Heroku)
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
    - STRIPE_WH_SECRET (for the webhooks)
    - USE_AWS

These variables are called in the settings.py file in our Django project so they stay hidden in production.

* In GitPod for this project I have not used the env.py file for environment variables, but the settings in the GitPod environment. This worked well.
* A Procfile is created to show that the app will be handled by the package `gunicorn` when deployed.
* In GitPod login to Heroku by typing `heroku login` and pressing the spacebar. In the preview screen the login can be done.
This failed lately and with `heroku login -i` the credentials could be entered manually.
* In GitPod the remote app is selected by typing `heroku git:remote -a myappname`
* The app has to start running on Heroku by typing `heroku ps:scale web=1`
* The normal process to push files to remote server can be used: `git add .` and `git commit . -m "comments"` and then `git push heroku master` 
to push to the master branch of our Heroku app.
* In Heroku the app can be linked to GitHub with automatic deployment, so that the step `git push Heroku master` is no longer needed.

To run the app.py locally we have to run `python3 manage.py runserver`.
You can now either open a browser on port 8000 after having that port made public.

The database in development is sqlite3. Models are created in the Django project and they are migrated to Heroku where they are used in
a Postgres database. This process works really well once set up properly. I did have some trouble because at some point I thought it
would be good to have the django package installed in GitPod. This however was not the case. It caused conflicts in packages versions
and failed to deploy on Heroku. Uninstalling Heroku solved the problem.

The static files of the project (images and css) cannot be hosted on Heroku. AWS is used for that.
S3 holds buckets where after setting all the variables right and policies on the process and folders
the static files of the whole project are automatically collected and stored in a S3 bucket.


## Credits

### Content
- The majority of the content, including images and video footage is taken from the original 
[Festival van Zeeuwsch-Vlaanderen](https://festival-zvl.nl) website and translated
into English, since the Festival is based in The Netherlands.
- A few concerts for previous years are created as a test and to show how the 'previous' 
section will work. The content in there is fictional.


### Acknowledgements

- I would like to thank the CodeInstitute for their support in the process. Most of what I've
created is based on the Boutique Ado project and molding that into this Festival website has 
helped me a lot to make more sense of the whole process of programming and developing. 
I have stayed pretty close to the processes and structures of the Boutique Ado project and had
hoped to add some more features. The size of the project and limited time however resulted in 
the project the way it now is. So a lot of credit to Chris and the other CodeInstitute developers.
- A big thank you to Rinus Meesen, director of the Festival, who has continuously granted me 
the job of building a website for years and years, even though I lacked the skill of webdevelopment
until now.
- My main sources for the project have been the CodeInstitute course material, 
[StackOverflow](https://stackoverflow.com/), the Django and Bootstrap/MDBootstrap documentation
and some sleepless nights that occasionally give one some great insights.
