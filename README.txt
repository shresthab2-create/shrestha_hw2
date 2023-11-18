This application  uses the GeoDB API.
The user can search for a country or city by name and retrieve information from this API.
It accesses the following endpoints:
/v1/geo/countries
/v1/geo/cities
It has the following routes:
homepage
'search_country'
'search_cities_by_name'
'filter_cities_by_country"
'db_search_countries'
-accesses API, displays response, stores data in DB
-accesses API, displays response, stores data in DB -queries DB for cities with provided country code i.e.'us'
-queries database for countries with provided name
After searching the API and getting a response, the program will save and display the city or country data in the database
