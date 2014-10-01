# BookBay #

## About This Project##
This web application was created as a final project in software engineering course together with another 2 classmates.  
It is a book sale site (eBay style) written in *python* and using the [Flask](http://flask.pocoo.org) framework.

#### Project Ourline####
You can find detailed information about this project in the SRS document in the docs folder. 

There are 3 kinds of users:

* Guest user
* Registered user
* Superuser


***Guest User -*** can sign up, browse books and search for other users.  
***Registered User -*** has privileges as the *guest user* but in addition can post books for sale, buy books,rate books, complain about other users or books and send messages to *superusers* and look in his profile statistics.  
*** Superuser -*** has all the privileges of the *registered user* and in addition:  

* User management - approving and suspending users. 
* Books management - remove books from sale.
* Watch bid history of each book.
* Watch transaction history of every user.

---
###General Idea ###
* Each registered user have a personal hompage which suggests the best sellers in case that there is no information about the user or *books you may like* in case we collected information about the user. 
* Everyone can sign up to the websits but need to be approved by the admin.
* After signing up, the user gets a temporary password the needs to be changed after admin approval.
* Each registered user starts with a balance of 100$ in his account. For every day of sale the user will pay 5$.
* A seller can decide to use the **Buy Now** feature which requires a special price (normally higher) to buy the book before the auction is over.

###Rules###
* Books with no bidder will be removed automatically after the auction is over.
* After a transaction has been made, the buyer must evaluate the book. 
* A registered user with 3 complaints will be suspended automatically. Only a *superuser* can reverse the suspension. 
* A book with 3 complaints will be suspended automatically. Only a *superuser* can reverse the suspension. 
* After a transaction has been made the seller will pay 5% of the sale price to the system.


## Requirements ##
[MySQL](http://www.mysql.com/downloads/) installed on the machine.

##Libraries in use##
* Flask
* Flask-Login
* Flask-Mail
* Flask-SQLAlchemy
* Flask-WTF
* Jinja2
* MarkupSafe
* MySQL-python
* SQLAlchemy
* Tempita
* WTForms
* Werkzeug
* argparse
* blinker
* decorator
* itsdangerous
* sqlalchemy-migrate
* stevedore
* virtualenv
* virtualenv-clone
* virtualenvwrapper
* wsgiref




## Installation #
Clone Repository And Install Libraries.

After cloneining this repository, open terminal and type:
```
cd /path/to/repository

virtualenv --no-site-packages .bookbay && source .bookbay/bin/activate && pip install -r requirements.txt && source .bookbay/bin/activate
```
###Setup MySQL Database###

Access your mysql database:
```
$ mysql -u root -p
```

Create database:
```
mysql> create database softeng character set utf8 collate utf8_bin;
```

Create a username and password:
```
mysql> create user 'softeng'@'localhost' identified by 'softeng';
```

Grant privieges to the user you just created:

```
mysql> grant all privileges on softeng.* to 'softeng'@'localhost';
```

```
mysql> flush privileges;
```

Create the database:
```
python db_create.py
```

Start the app by typing:
```
python runserver.py
```


### Usage ###
The first time you will user the app you need to create an admin account. To do that open your browser and navigate to [localhost:5000/get_admin_account](localhost:5000/get_admin_account).  
You will be redirected to the homepage.  

**Admin account:**  

* Username: admin
* Password: admin  



