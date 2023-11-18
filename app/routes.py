from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import City, Country
from app.forms import CitySearchForm, CountrySearchForm, CountryCodeSearchForm, CountryFilterForm
import requests
from flask import flash
def call_geodb_api(endpoint, params):
    headers = {
        'x rapidapi key': 'ab5f69c994mshb3231d7b0316beap18425ajsn04e70eb16061', # Replace with your actual API key
        'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com'

    }
    base_url='https://wft-geo-db.p.rapidapi.com/v1/geo'
     
    url=f"{base_url}/{endpoint}"

    response= requests.get(url, headers=headers, params=params)
    return response.json()

#Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/city_search', methods=['GET', 'POST'])
def city_search():
    return render_template('index.html')
    # Your code here

@app.route('/search_country', methods=['GET', 'POST'])
def search_country():
    form =  CountrySearchForm()
    if form.validate_on_submit():
        country_name= form.country_name.data
        params = {'namePrefix': country_name}
        country_data = call_geodb_api('countries', params)

        if 'data' in country_data and country_data['data']:
            country_info =  country_data['data'][0] #Assuming data is a list containing country Info
            code =  country_info.get('code')
            currency_code =  country_info.get('currencyCodes', [''])[0] #Access first currency code if available
            name = country_info.get('name')
            wiki_data_id = country_info.get('wikiDataId')


            if code and name:
                #Create a Country object and add it to the database
                country = Country(
                    code = code,
                    currency_code=currency_code,
                    name=name,
                    wiki_data_id=wiki_data_id
                )
                db.session.add(country)
                db.session.commit()
                flash('Country data added successfully!', 'success')
                return redirect(url_for('display_countries')) #Redirect to display the added countries
            else:
                flash('Required country info not found in API response.', 'error')
        else:
            flash ('No country data found in the API response.', 'error')
 

    return render_template('country_search.html', form=form)


@app.route('/display_countries')
def  display_countries():
    countries = Country.query.all()
    return render_template('country_results.html', countries=countries)


@app.route('/search_cities_by_name', methods=['GET', 'POST'])
def search_cities_by_name():
    form =  CitySearchForm()
    if form.validate_on_submit():
        city_name=  form.city_name.data
        params = {'namePrefix': city_name}
        city_data = call_geodb_api('cities', parass)

        if 'data' in city_data and city_data['data']:
            cities_info = city_data['data']
            for city_info in cities_info:
                # Extract relevant fields from city info
                wikiDataId =  city_info.get('wikiDataId')
                city_type =  city_info.get('type')
                city_name = city_info.get('name')
                country = city_info.get('country')
                countryCode = city_info.get('countrycode')
                latitude = city_info.get('latitude')
                longitude =  city_info.get('longitude')
                #Check if the city already exists in the database
                existing_city =  City.query.filter_by(name=city_name).first()

                if existing_city:
                    flash("The city (city_name} already exists in the database", "info")
                else:
                    # Create and store city information in the database.
                    city = City(
                        wikiDataId=wikiDataId,
                        ctype=city_type,
                        name=city_name,
                        country=country,
                        countryCode=countryCode,
                        latitude=latitude,
                        longitude=longitude
                      
                    )
                    db.sesson.add(city)
                    db.session.commit()
                    return redirect(url_for('display_cities'))

            else:
                flash('No cities found for the entered name.', 'error')
                    
    return render_template('city_search.html', form=form)

            
@app.route('/display_cities', methods=['GET'])
def display_cities():
    cities=City.query.all()# Retrieve all cities from the database
    return render_template('city_results.html', cities=cities)

@app.route('/filter_cities_by_country', methods=['GET', 'POST'])
def filter_cities_by_country():
    form= CountryCodeSearchForm()

    if form.validate_on_submit():
        country_code= form.country_code.data
        #Query the database for cities based on the provided country code 
        cities=City.query.filter_by(countryCode=country_code).all()
        if cities:

            return render_template('filtered_cities.html', cities=cities, country_code=country_code)

        else:
            flash('No cities found for the selected country code.', 'error')
    return render_template('city_filter_by_country.html', form-form)

@app.route('/db_search_countries', methods=['GET', 'POST'])
def db_search_countries():
    form = CountryFilterForm()
    if form.validate_on_submit():
        db_country_name = form.db_country_name.data
        countries = Country.query.filter(
            Country.name.ilike(f'%[db_country_name]%')
        ).all()

        if countries:
            return render_template('filtered_countries.html', countries=countries, db_country_name=db_country_name)
        else:
            flash('No countries found for the selected criteria.', 'error')
    return render_template('country_filter.html', form=form)
