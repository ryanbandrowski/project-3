import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Database Setup
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///static/data/db/CA_County_Crime.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# save references to each table
county_data = Base.classes.county_data
county_rates = Base.classes.county_rates
city_data = Base.classes.city_data

# Define Routes

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/county")
def county():
    # Use Pandas to perform the sql query
    sel = [
        county_data.County,
        county_data.County_Type,
        county_data.Lat,
        county_data.Lng,
        county_data.Total_Crime,
        county_data.Violent_Crime,
        county_data.Murder_And_Nonnegligent_Manslaughter,
        county_data.Forcible_Rape,
        county_data.Robbery,
        county_data.Aggravated_Assault,
        county_data.Property_Crime,
        county_data.Burglary,
        county_data.Larceny_Theft,
        county_data.Motor_Vehicle_Theft,
        county_data.Total_Officers,
        county_data.Population,
        county_data.Land_Area
    ]

    results = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information
    dict_list = []
    for result in results:

        county_dict = {}

        county_dict["County"] = result[0]
        county_dict["County_Type"] = result[1]
        county_dict["Lat"] = result[2]
        county_dict["Lng"] = result[3]
        county_dict["Total_Crime"] = result[4]
        county_dict["Violent_Crime"] = result[5]
        county_dict["Murder_And_Nonnegligent_Manslaughter"] = result[6]
        county_dict["Forcible_Rape"] = result[7]
        county_dict["Robbery"] = result[8]
        county_dict["Aggravated_Assault"] = result[9]
        county_dict["Property_Crime"] = result[10]
        county_dict["Burglary"] = result[11]
        county_dict["Larceny_Theft"] = result[12]
        county_dict["Motor_Vehicle_Theft"] = result[13]
        county_dict["Total_Officers"] = result[14]
        county_dict["Population"] = result[15]
        county_dict["Land_Area"] = result[16]
        
        dict_list.append(county_dict)

    return jsonify(dict_list)


@app.route("/county_rates")
def countyRates():
    # Use Pandas to perform the sql query
    sel = [
        county_rates.County,
        county_rates.County_Type,
        county_rates.Lat,
        county_rates.Lng,
        county_rates.Total_Crime,
        county_rates.Violent_Crime,
        county_rates.Murder_And_Nonnegligent_Manslaughter,
        county_rates.Forcible_Rape,
        county_rates.Robbery,
        county_rates.Aggravated_Assault,
        county_rates.Property_Crime,
        county_rates.Burglary,
        county_rates.Larceny_Theft,
        county_rates.Motor_Vehicle_Theft,
        county_rates.Total_Officers,
        county_rates.Population,
        county_rates.Land_Area
    ]

    results = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information
    dict_list = []
    for result in results:

        county_rates_dict = {}

        county_rates_dict["County"] = result[0]
        county_rates_dict["County_Type"] = result[1]
        county_rates_dict["Lat"] = result[2]
        county_rates_dict["Lng"] = result[3]
        county_rates_dict["Total_Crime"] = result[4]
        county_rates_dict["Violent_Crime"] = result[5]
        county_rates_dict["Murder_And_Nonnegligent_Manslaughter"] = result[6]
        county_rates_dict["Forcible_Rape"] = result[7]
        county_rates_dict["Robbery"] = result[8]
        county_rates_dict["Aggravated_Assault"] = result[9]
        county_rates_dict["Property_Crime"] = result[10]
        county_rates_dict["Burglary"] = result[11]
        county_rates_dict["Larceny_Theft"] = result[12]
        county_rates_dict["Motor_Vehicle_Theft"] = result[13]
        county_rates_dict["Total_Officers"] = result[14]
        county_rates_dict["Population"] = result[15]
        county_rates_dict["Land_Area"] = result[16]
        
        dict_list.append(county_rates_dict)

    return jsonify(dict_list)


@app.route("/city")
def city():
    # Use Pandas to perform the sql query
    sel = [
        city_data.City,
        city_data.Lat,
        city_data.Lng,
        city_data.County,
        city_data.Total_Crime,
        city_data.Violent_Crime,
        city_data.Murder_And_Nonnegligent_Manslaughter,
        city_data.Forcible_Rape,
        city_data.Robbery,
        city_data.Aggravated_Assault,
        city_data.Property_Crime,
        city_data.Burglary,
        city_data.Larceny_Theft,
        city_data.Motor_Vehicle_Theft,
        city_data.Total_Officers,
    ]

    results = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information
    dict_list = []
    for result in results:

        city_dict = {}

        city_dict["City"] = result[0]
        city_dict["Lat"] = result[1]
        city_dict["Lng"] = result[2]
        city_dict["County"] = result[3]
        city_dict['Total_Crime'] = result[4]
        city_dict["Violent_Crime"] = result[5]
        city_dict["Murder_And_Nonnegligent_Manslaughter"] = result[6]
        city_dict["Forcible_Rape"] = result[7]
        city_dict["Robbery"] = result[8]
        city_dict["Aggravated_Assault"] = result[9]
        city_dict["Property_Crime"] = result[10]
        city_dict["Burglary"] = result[11]
        city_dict["Larceny_Theft"] = result[12]
        city_dict["Motor_Vehicle_Theft"] = result[13]
        city_dict["Total_Officers"] = result[14]
        
        dict_list.append(city_dict)

    return jsonify(dict_list)


# run the app
if __name__ == "__main__":
    app.run()
