from flask_wtf import FlaskForm
from wtforms import IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,NumberRange
states=[('kerala','Kerala'),('bihar','Bihar'),('tamil_nadu','Tamil nadu'),('assam_and_meghalaya','Assam & Meghalaya'),
        ('nagaland_manipur_mizoram_tripura','Nagaland,Manipur,Mizoram & Tripura'),('orissa','Orissa'),('jharkhand','Jharkhand'),
        ('east_UP','Eastern Uttar Pradesh'),('west_UP','Western Uttar Pradesh'),('uttarakhand','Uttarakhand'),('haryana_delhi_chandigarh','Haryana,Delhi & Chandigarh'),
        ('punjab','Punjab'),('himachal_pradesh','Himachal Pradesh'),('jammu_and_kashmir','Jammu & Kashmir'),('costal_karnataka','Costal Karnataka'),
        ('north_interior_karnataka','North Interior Karnataka'),('south_interior_karnataka','South Interior Karnataka'),('telangana','Telangana'),
        ('costal_andhra_pradesh','Costal Andhra Pradesh'),('Chhattisgarh','Chhattisgarh'),('goa_and_konkan','Goa & Konkan'),
        ('madhya_maharashtra','Madhya Maharashtra'),('gujrat','Gujrat'),('west_rajasthan','West Rajasthan'),('east_rajasthan','East Rajasthan'),
        ('west_madhya_pradesh','West Madhya Pradesh'),('east_madhya_pradesh','East Madhya Pradesh')]

class askForm(FlaskForm):

    year = IntegerField('Enter Year',validators=[DataRequired(),NumberRange(min=1850,max=2050)])
    state = SelectField('Select State', choices=states)
    submit = SubmitField('Submit')