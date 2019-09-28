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


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///static/data/db/CA_County_Crime.sqlite"
db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(db.engine, reflect=True)

# save references to each table
total_data = Base.classes.total_data
county_data = Base.classes.county_data
city_data = Base.classes.city_data


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


@app.route("/total")
def total():
    # Use Pandas to perform the sql query
    sel = [
        total_data.County,
        total_data.County_Type,
        total_data.Violent_Crime,
        total_data.Murder_And_Nonnegligent_Manslaughter,
        total_data.Forcible_Rape,
        total_data.Robbery,
        total_data.Aggravated_Assault,
        total_data.Property_Crime,
        total_data.Burglary,
        total_data.Larceny_Theft,
        total_data.Motor_Vehicle_Theft,
        total_data.Total_Officers,
        total_data.Population,
        total_data.Land_Area
    ]

    results = db.session.query(*sel).all()

    # Create a dictionary entry for each row of metadata information
    dict_list = []
    for result in results:

        total_dict = {}

        total_dict["County"] = result[0]
        total_dict["County_Type"] = result[1]
        total_dict["Violent_Crime"] = result[2]
        total_dict["Murder_And_Nonnegligent_Manslaughter"] = result[3]
        total_dict["Forcible_Rape"] = result[4]
        total_dict["Robbery"] = result[5]
        total_dict["Aggravated_Assault"] = result[6]
        total_dict["Property_Crime"] = result[7]
        total_dict["Burglary"] = result[8]
        total_dict["Larceny_Theft"] = result[9]
        total_dict["Motor_Vehicle_Theft"] = result[10]
        total_dict["Total_Officers"] = result[11]
        total_dict["Population"] = result[12]
        total_dict["Land_Area"] = result[13]
        
        dict_list.append(total_dict)

    return jsonify(dict_list)


@app.route("/county")
def county():
    # Use Pandas to perform the sql query
    sel = [
        county_data.County,
        county_data.County_Type,
        county_data.Lat,
        county_data.Lng,
        county_data.Violent_Crime,
        county_data.Murder_And_Nonnegligent_Manslaughter,
        county_data.Forcible_Rape,
        county_data.Robbery,
        county_data.Aggravated_Assault,
        county_data.Property_Crime,
        county_data.Burglary,
        county_data.Larceny_Theft,
        county_data.Motor_Vehicle_Theft
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
        county_dict["Violent_Crime"] = result[4]
        county_dict["Murder_And_Nonnegligent_Manslaughter"] = result[5]
        county_dict["Forcible_Rape"] = result[6]
        county_dict["Robbery"] = result[7]
        county_dict["Aggravated_Assault"] = result[8]
        county_dict["Property_Crime"] = result[9]
        county_dict["Burglary"] = result[10]
        county_dict["Larceny_Theft"] = result[11]
        county_dict["Motor_Vehicle_Theft"] = result[12]
        
        dict_list.append(county_dict)

    return jsonify(dict_list)


@app.route("/city")
def city():
    # Use Pandas to perform the sql query
    sel = [
        city_data.City,
        city_data.Lat,
        city_data.Lng,
        city_data.County,
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
        city_dict["Violent_Crime"] = result[4]
        city_dict["Murder_And_Nonnegligent_Manslaughter"] = result[5]
        city_dict["Forcible_Rape"] = result[6]
        city_dict["Robbery"] = result[7]
        city_dict["Aggravated_Assault"] = result[8]
        city_dict["Property_Crime"] = result[9]
        city_dict["Burglary"] = result[10]
        city_dict["Larceny_Theft"] = result[11]
        city_dict["Motor_Vehicle_Theft"] = result[12]
        city_dict["Total_Officers"] = result[13]
        
        dict_list.append(city_dict)

    return jsonify(dict_list)


# run the app
if __name__ == "__main__":
    app.run()
