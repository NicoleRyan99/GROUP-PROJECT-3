import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import psycopg2
from flask import Flask, jsonify
import config

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(config.user, config.Password, 'localhost', 5432, 'city_weather_db'))
#engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(config.user, config.Password, 'localhost', 5432, 'movie_db'))

# reflect an existing database into a new model use autoamp
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
city_weather = Base.classes.city_weather
fit_weather_data = Base.classes.fit_weather_data
hotel = Base.classes.hotel


# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

# 2. Create an app, being sure to pass __name__

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def Welcome():
    print("List all available api routes")
    return(
        "Welcome: <br/>"
        f"Here are the Availeble Routs: <br/>"
        f"/api/v1.0/hotels <br/>"
        f"/api/v1.0/stations <br/>"
        f"/api/v1.0/tobs <br/>"
        f"/api/v1.0/start <br/>"
        f"/api/v1.0/start/end <br/>"
    )


#Convert the query results to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.

@app.route("/api/v1.0/hotels")
def hotels():
   
    Hotel_result = session.query(hotel.city, hotel.population ,hotel.lat,hotel.lng,hotel.Humidity,hotel.Country,hotel.Date).all()
    Hotel_list = []

    for city, population, lat, lng, Humidity, Country, Date  in Hotel_result:
        row = {}
        row["city"] = city
        row["population"] = population
        row["lat"] = lat
        row["lng"] = lng
        row["Humidity"] = Humidity
        row["Country"] = Country
        row["Date"] = Date
     
       
        Hotel_list.append(row)
    return jsonify(Hotel_list)

#Return a JSON list of stations from the dataset. 
    


if __name__ == "__main__":
    app.run(debug=True)