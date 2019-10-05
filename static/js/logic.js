
var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});


var baseMaps = {
  "Light Map": lightmap
};


var map = L.map("map-id", {
  center: [36.7783, -119.4179],
  zoom: 6,
  layers: [lightmap]
});



var link = 'https://opendata.arcgis.com/datasets/f26ff0ccda6e48a8b923927cfdb2a451_0.geojson'
var geoJson;

d3.json(link, function(data) {

    d3.json("/county_rates", function(county) {

        geoJson = L.geoJson(data, {

            style: function(feature) {
                return {
                    color: "lightgrey",
                    fillColor: "green",
                    fillOpacity: .2,
                    weight: 1
                };
            },

            onEachFeature: function(feature, layer) {

                layer.on({

                    mouseover: function(event) {
                        layer = event.target;
                        layer.setStyle({
                            fillOpacity: 0.7
                        });
                    },

                    mouseout: function(event) {
                        geoJson.resetStyle(event.target);
                    },

                    click: function(event) {
                        map.fitBounds(event.target.getBounds());
                    }
                });

                layer.bindPopup(
                    "<h2>" + county.County + " Crime Rates</h2>" +
                    "<h3>Per 10,000 People</h3>" +
                    "<strong>Total Crime: " + county.Total_Crime
                );
            }
        }).addTo(map);
    });
});



var markers = L.layerGroup();

d3.json("/city", function(response) {
    console.log(response);

    for (var i = 0; i < response.length; i++) {
        
        var lat = response[i].Lat
        var lng = response[i].Lng

        markers.addLayer(L.marker([lat,lng])
            .bindPopup(
                "<strong>City: </strong>" + response[i].City + "<br>" +
                "<strong>County: </strong>" + response[i].County + "<br><br>" +
                "<strong>Violent Crime: </strong>" + response[i].Violent_Crime + "<br>" +
                "<strong>Murder/Manslaughter: </strong>" + response[i].Murder_And_Nonnegligent_Manslaughter + "<br>" +
                "<strong>Forcible Rape: </strong>" + response[i].Forcible_Rape + "<br>" +
                "<strong>Robbery: </strong>" + response[i].Robbery + "<br>" +
                "<strong>Aggravated Assault: </strong>" + response[i].Aggravated_Assault + "<br><br>" +
                "<strong>Property Crime: </strong>" + response[i].Property_Crime + "<br>" +
                "<strong>Burglary: </strong>" + response[i].Burglary + "<br>" +
                "<strong>Larceny-Theft: </strong>" + response[i].Larceny_Theft + "<br>" +
                "<strong>Motor Vehicle Theft: </strong>" + response[i].Motor_Vehicle_Theft + "<br><br>" +
                "<strong>Total Officers: </strong>" + response[i].Total_Officers + "<br>"
            )
        );
    }
});

map.on('zoomend', function() {
    if (map.getZoom() <9){
            map.removeLayer(markers);
    }
    else {
            map.addLayer(markers);
    }
});