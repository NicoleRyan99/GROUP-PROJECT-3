console.log(data);
console.log(info);
console.log(value);

//Create a function to build the charts
function graphBuilder(place, time){
  
  //let cityName = place

  //Create a function that filters for specific place
  function chooseCity(location) {
    return location.City == place
  };

  let thisCity = data.filter(chooseCity);
  console.log(thisCity);

  //create a function that filters for specific time i.e., year
  function chooseYear(object) {
    return object.Year == time
  };

  let thisYear = thisCity.filter(chooseYear);
  console.log(thisYear);

  //obtain info for graphs
  let monthList = thisYear.map(function(unit) {
    return unit.Month;
  });

  console.log(monthList);

  let valueList = thisYear.map(function(item) {
    return item.TOTAL;
  });

  console.log(valueList);

  let trace1 = {
    x: thisYear.map(row => row.Month),
    y: thisYear.map(row => row.TOTAL),
    type: "bar",
    //text: average temperature for that month 
  };

  let setUp = [trace1];

  let barLayout = {
    title: "Passenger Arrivals Throughout the Year",
    xaxis: { title: "Month" },
    yaxis: { title: "Number Of Arrivals" }
  };

  //plot graph
  Plotly.newPlot("plot", setUp, barLayout);

  //Second Graph 
  //Total arrivals per year for 10 years

  //Use the chooseCity function created above to filter for specific city

  let thatCity = info.filter(chooseCity);
  console.log(thatCity);

  //create bar graph
  let trace2 = [{
    x: thatCity.map(row => row.Year),
    y: thatCity.map(row => row.TOTAL),
    type: "bar",
  }];

  let barLayout2 = {
    title: "Passenger Arrivals Throughout the Decade",
    xaxis: { title: "Year" },
    yaxis: { title: "Number Of Arrivals" }
  };

  Plotly.newPlot("bar", trace2, barLayout2);

};



//Build init funciton
function init() {
  // Grab a reference to the dropdown select element
  let selector = d3.select("#selDataset");
  let selector2 = d3.select("#yearDataset");

  // Use the list of cities names to populate the select options
  // add Miami once its been add to df -> database -> api -> json-> js
  let cityNames = ["Boston", "Chicago", "Las Vegas", "Los Angeles", "New York", "Orlando", "San Francisco", "Seattle", "Washington DC"];
  let cityYear = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022];

  cityNames.forEach((object) => {
    selector
        .append("option")
        .text(object)
        .property("value", object);
  });

  cityYear.forEach((object) => {
    selector2
        .append("option")
        .text(object)
        .property("value", object);
  });

  // Use the first sample from the list to build the initial plots
  let firstCity = cityNames[0];
  let firstYear = cityYear[0];
  graphBuilder(firstCity, firstYear);
  console.log("new city was choosen");
  //buildMetadata(firstCity);
}

function optionChanged(newCity, newYear) {
  // Fetch new data each time a new sample is selected
  graphBuilder(newCity, newYear);
  //buildMetadata(newCity);
};

// Initialize the dashboard
init();