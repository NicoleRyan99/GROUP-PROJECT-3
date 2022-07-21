import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import psycopg2
from flask import Flask, jsonify
import config

engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(config.username, config.password, 'localhost', 5432, 'city_weather_db'))
#engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(config.user, config.Password, 'localhost', 5432, 'movie_db'))

# reflect an existing database into a new model use autoamp
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)


# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
monthly_arrivals = Base.classes.monthly_arrivals
total_arrivals = Base.classes.total_arrivals
monthly_summary = Base.classes.monthly_summary


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
        f"/api/v1.0/monthlyarrivals <br/>"
        f"/api/v1.0/totalarrivals <br/>"
        f"/api/v1.0/monthlysummary <br/>"
       
    )


#Convert the query results to a dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.

@app.route("/api/v1.0/monthlyarrivals")
def monthlyarrivals():
   
    monthly_arrivals_result = session.query(monthly_arrivals.Airport, monthly_arrivals.Airport_Code, monthly_arrivals.Year, monthly_arrivals.Month, monthly_arrivals.TOTAL, monthly_arrivals.City ).all()
    monthly_arrivals_list = []

    for Airport, Airport_Code, Year, Month, TOTAL,City    in monthly_arrivals_result:
        row = {}
        row["Airport"] = Airport
        row["Airport_Code"] = Airport_Code
        row["Year"] = Year
        row["Month"] = Month
        row["TOTAL"] = TOTAL
        row["City"] = City
      
        monthly_arrivals_list.append(row)
    return jsonify(monthly_arrivals_list)

@app.route("/api/v1.0/totalarrivals")
def totalarrivals():
   
    total_arrivals_result = session.query(total_arrivals.Airport, total_arrivals.Airport_Code, total_arrivals.Year, total_arrivals.Month, total_arrivals.TOTAL, total_arrivals.City ).all()
    total_arrival_list = []

    for Airport, Airport_Code, Year, Month, TOTAL,City    in total_arrivals_result:
        row = {}
        row["Airport"] = Airport
        row["Airport_Code"] = Airport_Code
        row["Year"] = Year
        row["Month"] = Month
        row["TOTAL"] = TOTAL
        row["City"] = City
      
        total_arrival_list.append(row)
    return jsonify(total_arrival_list)


@app.route("/api/v1.0/monthlysummary")
def monthlysummary():
   
    monthly_summary_result = session.query(monthly_summary.DATE, monthly_summary.AIRPORT_CODE, monthly_summary.AIRPORT, monthly_summary.LATITUDE, monthly_summary.LONGITUDE, monthly_summary.ELEVATION,monthly_summary.Average_Wind_Speed, monthly_summary.Max_Gust_Speed, monthly_summary.Precipitation, monthly_summary.Snow_Accumulation, monthly_summary.Average_Temperature, monthly_summary.Max_Temperature,monthly_summary.Min_Temperature ).all()
    
    monthly_summary_list = []

    for DATE, AIRPORT_CODE, AIRPORT, LATITUDE, LONGITUDE, ELEVATION, Average_Wind_Speed, Max_Gust_Speed, Precipitation , Snow_Accumulation , Average_Temperature, Max_Temperature, Min_Temperature    in monthly_summary:
        row = {}
        row["DATE"] = DATE
        row["AIRPORT_CODE"] = AIRPORT_CODE
        row["AIRPORT"] = AIRPORT
        row["LATITUDE"] = LATITUDE
        row["LONGITUDE"] = LONGITUDE
        row["ELEVATION"] = ELEVATION
        row["Average_Wind_Speed"] = Average_Wind_Speed
        row["Max_Gust_Speed"] = Max_Gust_Speed
        row["Precipitation"] = Precipitation
        row["Snow_Accumulation"] = Snow_Accumulation
        row["Average_Temperature"] = Average_Temperature
        row["Max_Temperature"] = Max_Temperature
        row["Min_Temperature"] = Min_Temperature
      
        monthly_summary_list.append(row)
    return jsonify(monthly_summary_list)

    

if __name__ == "__main__":
    app.run(debug=True)