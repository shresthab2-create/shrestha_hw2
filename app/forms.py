from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CitySearchForm(FlaskForm):
    city_name = StringField('City Name', validators=[ DataRequired()]) 
    submit = SubmitField('Search')

class CountrySearchForm(FlaskForm):
    country_name = StringField('Country Name', validators=[DataRequired()]) 
    submit = SubmitField('Search')

class CountryCodeSearchForm(FlaskForm): 
    country_code = StringField('Country Code', validators=[DataRequired()]) 
    submit = SubmitField('Search')

class CountryFilterForm(FlaskForm):
    db_country_name = StringField('DB Search Country') 
    submit = SubmitField('Search')
