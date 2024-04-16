from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy here
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email
import random
from config import Config

import random
app = Flask(__name__)
app.config.from_object(Config)



# List of headlines
headlines = [
    "Breaking News: New Study Shows Benefits of Exercise",
    "Tech Giant Launches Revolutionary Product",
    "World Leaders Gather for Historic Summit",
    "Local Community Comes Together to Support Charity Event",
    "Scientists Make Breakthrough in Cancer Research"
]

@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', headlines=headlines)


# Secret key for CSRF protection
app.config['SECRET_KEY'] = 'your-secret-key'
# Initialize the database
db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        # Handle the form submission by adding data to the database
        new_contact = Contact(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data
        )

        db.session.add(new_contact)
        db.session.commit()

        # You can redirect to a thank you page or home page after submission
        return render_template('thankyou.html')

    return render_template('contact.html', form=form)


@app.route('/products/')
def products():
    return render_template('products.html')



@app.route('/about')
def about():
    return render_template('about.html')




@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/moreinfo')
def moreinfo():
    return render_template('moreinfo.html')

@app.route('/semi_automatic_rifle')
def semi_automatic_rifle():
    # Your view logic goes here
    return render_template('semi_automatic_rifle.html')    

@app.route('/pistols_history')
def pistols_history():
    return render_template('pistols_history.html')


@app.route('/guns_history')
def guns_history():
    return render_template('guns_history.html')    

@app.route('/moreabout')
def moreabout():
    return render_template('moreabout.html')   



@app.route('/moreabout_web')
def moreabout_web():
    return render_template('moreabout_web.html')

@app.route('/moreaboutAli')
def moreaboutAli():
    return render_template('moreaboutAli.html')    

@app.route('/moreaboutSchool')
def moreaboutSchool():
    return render_template('moreaboutSchool.html') 

@app.route('/moreaboutData')
def moreaboutData():
    return render_template('moreaboutData.html')         


@app.route('/bore30_pistols')
def bore30_pistols():
    products30bor = [
        {'name': '30 Bore Pistol A', 'description': 'High-quality 30 bore pistol with precision engineering. Russian Interchange.', 'price': 25000, 'image': '30bore1.jpg'},
        {'name': '30 Bore Pistol B', 'description': 'Durable and reliable 30 bore pistol spare parts for long life.', 'price': 15000, 'image': '30bore2.jpg'},
        {'name': '30 Bore Pistol C', 'description': 'Versatile and accurate 30 bore pistol suitable for professionals made by our experts.', 'price': 22000, 'image': '30bore3.jpg'},
        {'name': '30 Bore Pistol D', 'description': 'Ergonomically designed 30 bore pistol for comfortable handling and orignal barrel.', 'price': 30000, 'image': '30bore4.jpg'},
        {'name': '30 Bore Pistol E', 'description': 'Precision barrel and effective stopping power in this 30 bore zistawa pistol.', 'price': 30000, 'image': '30bore5.jpg'},
        {'name': '30 Bore Pistol F', 'description': 'Made by Order pistol 7 short and 14 shorts see more design.', 'price': 35000, 'image': '30bore.jpg'},

        
    ]
    return render_template('bore30_pistols.html', products30bor=products30bor)  

@app.route('/mm9_pistols')
def mm9_pistols():
    products9mm = [
        {'name': '9mm Pistol A', 'description': 'Glock17 9mm pistol with weightless engineering.', 'price':  35000, 'image': 'Glock9mm.webp'},
        {'name': '9mm Pistol B', 'description': 'Glock19 9mm pistol for various shooting applications.', 'price': 40000, 'image': 'glock2.png'},
        {'name': '9mm Pistol C', 'description': 'Versatile and accurate 9mm pistol suitable for professionals.', 'price': 30000, 'image': 'images.jpeg'},
        {'name': '9mm Pistol D', 'description': 'Ergonomically designed 9mm pistol for comfortable handling.', 'price': 30000, 'image': 'images (1).jpeg'},
        {'name': '9mm Pistol E', 'description': 'Precision barrel and effective stopping power in this 9mm pistol.', 'price': 35000, 'image': '9mm_.38_pistol.jpg'},
        {'name': '9mm Pistol F', 'description': 'Reliable and durable 9mm pistol for self-defense and sport shooting.', 'price': 45000, 'image': 'glock12.jpg'},
        {'name': '9mm Pistol G', 'description': 'Compact design and safety features in this 9mm Glock34 pistol.', 'price': 25000, 'image': 'glock11.jpg'},
        {'name': '9mm Pistol H', 'description': 'Balanced combination of power and accuracy in this 9mm Glock26 pistol.', 'price': 30000, 'image': 'glock26.jpg'},
        {'name': '9mm Pistol H', 'description': 'Balanced combination of power and accuracy in this 9mm Glock17 pistol.', 'price': 25000, 'image': 'glock17.jpg'},
        
    ]    
    return render_template('mm9_pistols.html', products9mm=products9mm)  

@app.route('/bore12_short_guns')
def bore12_short_guns():
    products12bor = [
        {'name': '12Bore A', 'description': 'High-quality 12 bore with precision engineering.', 'price': 35000, 'image': '12bore_semiauto_bikal.jpg'},
        {'name': '12Bore B', 'description': 'Durable and reliable 12 bore for various shooting applications.', 'price': 30000, 'image': '12bore_semiauto1.jpg'},
        {'name': '12Bore C', 'description': 'Precision barrel and effective stopping power in this 9mm pistol.', 'price': 40000, 'image': '12bore_semiauto.jpg'},
        {'name': '12Bore D', 'description': 'Reliable and durable 9mm pistol for self-defense and sport shooting.', 'price': 35000, 'image': '12bore_turky.jpg'},
        {'name': '12Bore D', 'description': 'Compact design and safety features in this 9mm pistol.', 'price': 30000, 'image': '12boresiga.jpg'},
        {'name': '12Bore E', 'description': 'High-performance 9mm pistol suitable for various shooting scenarios.', 'price': 35000, 'image': '12bore_repeator.jpg'},

        
    ]    
    return render_template('bore12_short_guns.html', products12bor=products12bor) 

@app.route('/Guns')
def Guns():
    guns = [
        {'name': 'Gun AK47 70', 'description': 'High-quality Russian Design with precision engineering.', 'price': 50000, 'image': 'automatic_gun.jpg'},
        {'name': 'Gun M16 ', 'description': 'Durable and reliable for various shooting applications.', 'price': 60000, 'image': 'breechloadingA.png'},
        {'name': 'Gun M4', 'description': 'Versatile and accurate suitable for professionals.', 'price': 70000, 'image': 'm4.jpg'},
        {'name': 'Gun AK47 75', 'description': 'Ergonomically designed gun for comfortable handling.', 'price': 10000, 'image': 'ak47_model75.jpg'},
        {'name': 'Gun AK47 75', 'description': 'Ergonomically designed gun for comfortable handling.', 'price': 10000, 'image': 'machine_gun.jpg'},
        {'name': 'Gun AK47 75', 'description': 'Ergonomically designed gun for comfortable handling.', 'price': 10000, 'image': 'semiAuto.png'},
        

        
    ]    
    return render_template('Guns.html', guns=guns)    

@app.route('/ammunition')
def ammunition():

    ammunition = [
        {'name': '30 Bore Ammunition A', 'description': 'High-quality 30 bore pistol with precision engineering.', 'price': 500, 'image': 'ammu1.png'},
        {'name': '30 Bore Ammunition B', 'description': 'Durable and reliable 30 bore pistol for various shooting applications.', 'price': 600, 'image': 'ammum16.jpeg'},
        {'name': '30 Bore Ammunition C', 'description': 'Versatile and accurate 30 bore pistol suitable for professionals.', 'price': 700, 'image': 'ammu30.png'},
        {'name': '30 Bore Ammunition D', 'description': 'Ergonomically designed 30 bore pistol for comfortable handling.', 'price': 800, 'image': 'ammunition_image1.jpg'},
        {'name': '30 Bore Amunition E', 'description': 'Precision barrel and effective stopping power in this 30 bore pistol.', 'price': 900, 'image': '30borepistol_5.png'},
        {'name': '30 Bore Pistol F', 'description': 'Reliable and durable 30 bore pistol for self-defense and sport shooting.', 'price': 1000, 'image': '30borepistol_6.png'},
        {'name': '30 Bore Pistol G', 'description': 'Compact design and safety features in this 30 bore pistol.', 'price': 1100, 'image': '30borepistol_7.png'},
        {'name': '30 Bore Pistol H', 'description': 'Balanced combination of power and accuracy in this 30 bore pistol.', 'price': 1200, 'image': '30borepistol_8.png'},
        {'name': '30 Bore Pistol I', 'description': 'High-performance 30 bore pistol suitable for various shooting scenarios.', 'price': 1300, 'image': '30borepistol_9.png'},
        
    ]    
    return render_template('ammunition.html', products=ammunition)     
     

@app.route('/Accesories')
def Accesories():

    accesories = [
        {'name': '30 Bore Pistol A', 'description': 'High-quality 30 bore pistol with precision engineering.', 'price': 500, 'image': 'kaash1.jpeg'},
        {'name': '30 Bore Pistol B', 'description': 'Durable and reliable 30 bore pistol for various shooting applications.', 'price': 600, 'image': 'kaash2.jpeg'},
        {'name': '30 Bore Pistol C', 'description': 'Versatile and accurate 30 bore pistol suitable for professionals.', 'price': 700, 'image': 'kaash3.jpeg'},

        
    ]    
    return render_template('Accesories.html', products=accesories)    
 

if __name__ == '__main__':
    with app.app_context():
       db.create_all()
    app.run(debug=False)
