// Create the tile layer that will be the background of our map
var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.light",
  accessToken: API_KEY
});

// Create a baseMaps object to hold the lightmap layer
var baseMaps = {
  "Light Map": lightmap
};

// Create the map object with options
var map = L.map("map-id", {
  center: [36.7783, -119.4179],
  zoom: 6,
  layers: [lightmap]
});

// Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
// L.control.layers(baseMaps, {
//   collapsed: false
// }).addTo(map);

var link = 'https://opendata.arcgis.com/datasets/f26ff0ccda6e48a8b923927cfdb2a451_0.geojson'

var geoJson;

// Grabbing our GeoJSON data..
d3.json(link, function(data) {
  console.log(data)
    // Creating a geoJSON layer with the retrieved data
    geoJson = L.geoJson(data, {
        // Style for each feature (in this case a neighborhood)
        style: function(feature) {
            return {
                color: "lightgrey",
                // Call the chooseColor function to decide which color to color our neighborhood (color based on borough)
                fillColor: "green",
                fillOpacity: 0.5,
                weight: 1
            };
        },
        // Called on each feature
        onEachFeature: function(feature, layer) {
        // Setting various mouse events to change style when different events occur
            layer.on({
                // On mouse over, make the feature (neighborhood) more visible
                mouseover: function(event) {
                    layer = event.target;
                    layer.setStyle({
                        fillOpacity: 0.9
                    });
                },
                // Set the features style back to the way it was
                mouseout: function(event) {
                    geoJson.resetStyle(event.target);
                },
                // When a feature (neighborhood) is clicked, fit that feature to the screen
                click: function(event) {
                    map.fitBounds(event.target.getBounds());
                }
            });
        // Giving each feature a pop-up with information about that specific feature
        layer.bindPopup("<h1>" + feature.properties.COUNTY_NAME + "</h1>");
        }
    }).addTo(map);
});
