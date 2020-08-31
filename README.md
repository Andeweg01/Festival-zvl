<img src="https://andeweg-festival-zvl.s3.amazonaws.com/media/FestivalZVL_logo.png" style="margin: 0;">

# Festival-zvl (Festival van Zeeuwsch-Vlaanderen)

For over 30 years the Festival van Zeeuwsch-Vlaanderen has been the biggest festival for classical music in Zeeuwsch-Vlaanderen (Zealand's Flanders). This is the Dutch part of Flanders, disconnected from The Netherlands by the River Scheldt. A quiet, rural, but culturally rich area. This is where different venues form the stage for the festival. 
Over ten years I've had the privilege to create the program brochures, different printed material and the website. However, the ticket sale has always been outsourced to a local theater. This has meant an extra step for the visitor to buy tickets on a secondary website, away from the main site. The festival manager wants one-stop-shop. Having the tools now to build e-commerce sites will make it possible to have all the elements for one-stop-shopping on the main site.

 
## UX
 
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_1.jpg?raw=true" style="margin: 0;">
<img src="https://github.com/Andeweg01/Festival-zvl/blob/master/img/Festival-zvl_project_Page_2.jpg?raw=true" style="margin: 0;">
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


## Technologies Used

### Front-end
* [HTML5](https://en.wikipedia.org/wiki/HTML5) for the HTML structure.
* [CSS3](https://www.w3.org/Style/CSS/Overview.en.html) for styling and editing existing (MD)Bootstrap css-code
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
- site owner on the database: The site owner can add, delete and edit concerts. This is all working well. Unused fields do not show and the presentation of the data looks good.
- users ordering: 




## DEPLOYMENT
In the design phase [Adobe Dreamweaver](https://www.adobe.com/ie/products/dreamweaver.html) was used to speed up the 
design process and make good use of the handy live view. 
The HTML/CSS design during this process was also deployed and tested on a live server (Strato - domain Tradtracker.com). 

In the process I found issues with combining Bootstrap and Materialize. In their css they use the same naming in the CSS 
code for several navigation elements. Inspecting with Google Chrome on the live server proved to be very usefull to find 
the issues and create workarounds in my own code. After finding more and more issues that seemed impossible to overcome I decided
to stop using Bootstrap en continue with Materialize only.

I used the GitPod IDE for testing in the required environment for the CodeInstitute courses. The HTML/CSS files 
are pushed to the GitHub repository to handle the version control.

The Flask/Python part of the project is built within the GitPod IDE and once linked to the MongoDB database, 
deployment is done on Heroku.

### The process:
* In GitHub a repository with full template by the CodeInstitute is generated for use with GitPod.
* In GitPod a site structure is built with a static folder, as required for Flask project, a templates folder and
* files to load and set the libraries, environment variables, configuration files:
   dnspython==1.16.0  
   Flask==1.1.2  
   Flask-PyMongo==2.3.0  
   heroku==0.1.4  
   pymongo==3.10.1  
   python-dateutil==1.5  
   Werkzeug==1.0.1  

   These are stored in the file requirements.txt by using the command: `pip3 freeze --local > requirements.txt`
   So these requirements can easily be loaded again by typing `pip3 install -r requirements.txt`
* In Heroku the app has to be created to be able to run later. 
* It's important to have the variables 'IP' and 'HOST' set and also the Mongo URI key to be able to use the database with Heroku
* In GitPod an env.py file is created to store that same Mongo URI variable. The env.py is stored in the .gitignore so that it doesn't push to the remote servers.
* A Procfile is created to show that app.py will be the Python file to run and we're good to go. Type `echo web: python app.py > Procfile`
* In GitPod login to Heroku by typing `heroku login` and pressing the spacebar. In the preview screen the login can be done.
* In GitPod the remote app is selected by typing `heroku git:remote -a myappname`
* The app has to start running on Heroku by typing `heroku ps:scale web=1`
* The normal process to push files to remote server can be used: `git add .` and `git commit . -m "comments"` and then `git push heroku master` to push to the master branch of our Heroku app.

To run the app.py locally we have to run the Python server `python3 -m http.server` and run `python3 app.py`.
You can now either open a browser or the preview in GitPod.




## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X
