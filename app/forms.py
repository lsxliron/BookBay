from flask_wtf import Form
from wtforms import TextField, BooleanField, TextAreaField, SubmitField, PasswordField,SelectField, validators, ValidationError
from app.models import User
from flask import flash

class SignUpForm(Form):
    username = TextField('Username', validators=[validators.Required()])
    first_name = TextField('First name', validators=[validators.Required()])
    last_name = TextField('Last Name', validators=[validators.Required()])
    email = TextField('Email', validators=[validators.Required()])
    password = PasswordField('Password', validators=[validators.Required()])
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        '''custom validators method. this method is referenced everytime
        form.validate_on_submit() is called. when returned False, will
        prompt the client as error'''
        if not Form.validate(self):
            return False
        # check if email is taken and if password is correct
        email = User.query.filter_by(email = self.email.data.lower()).first()
        username = User.query.filter_by(username = self.username.data.lower()).first()
        if email:
            self.email.errors.append("That email is already taken")
        if username:
            self.username.errors.append("This username is already taken")
        else:
            return True

class LoginForm(Form):
    username = TextField('Username', validators=[validators.Required()])
    password = PasswordField('Password',validators=[validators.Required("Please enter a password.")])
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        user = User.query.filter_by(username = self.username.data.lower()).first()
        if user and user.check_password(self.password.data):
            return True
        else:
            self.password.errors.append("invalid password")


class ChangePassword(Form):
    oldPassword = TextField('Old Password:', validators=[validators.Required()])
    newPassword = TextField('New Password:', validators=[validators.Required("Please enter a password")])
    newPassword2 = TextField('New Password:', validators=[validators.Required("Passwords does not match")])
    submit = SubmitField("Change Password")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        if not Form.validate(self):
            return False
        if user and user.check_password(self.oldPassword.data):
            if (self.newPassword == newPassword2):
                return True
        return False



class ChangePersonalDetails(Form):

    first_name = TextField('First Name:', validators=[validators.Required()])
    last_name = TextField('Last Name:', validators=[validators.Required()])
    updateDatails = SubmitField("Change Details")

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)



class SearchForm(Form):
    search_field = TextField(u'Search:')
    search_type = SelectField(u'Type of Search', choices=[('books','Books'), ('users', 'People')])
    submit = SubmitField("Submit")



class sellForm(Form):



    title = TextField('Title:', validators=[validators.Required()])
    author = TextField('Author', validators=[validators.Required()])
    isbn = TextField('ISBN', validators=[validators.Required()])
    price = TextField('Price:', validators=[validators.Required()])
    saleDuration = TextField('Sale duration (days):', validators=[validators.Required()])
    publisher = TextField('Publisher:', validators=[validators.Required()])
    numOfPages = TextField('No. of Pages:', validators=[validators.Required()])
    lang = TextField('Language:', validators=[validators.Required()])
    genre = TextField('Genre:', validators=[validators.Required()])
    edition = TextField('Edition:', validators=[validators.Required()])
    condition = SelectField('Condition', choices=[('new','New'),('used','Used')])
    bookType = SelectField('Type:', choices=[('paperBack','Paper back'),('hardCover','Hard Cover')])
    information = TextAreaField('Book Information')
    submit = SubmitField("Post For Sale!")
    buyable = BooleanField("Enable Buy Now")
    buynowPrice = TextField("Buy Now Price:")



    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)

    def validate(self):
        
        if not Form.validate(self):
            return False
        if (self.data.get('buyable') == True):
            if self.data.get('buynowPrice') == '':
                return False
        
        else:
            return True

    




