function GetValue()
{
    var myarray= new Array("On average, the busiest air-travel month in the US is July!",
    "In 2019, the top 10 airports scheduled over 300M flights combined.",
    "From 2019 to 2020, the top 10 airports reported a 66% decline in scheduled flights.",
    "Los Angeles and Chicago O'Hare International airports have the highest number of scheduled flights in the country, averaging approximately 2.8 million flights per month!",
    "Boston, Chicago, New York, Los Angeles, San Francisco, and Seattle are all popular air travel destinations in the Summer.",
    "Las Vegas's busiest air travel month is October.",
    "Orlando's busiest air travel month is March.",
    "Washington DC Dulles International Airport's busiest air travel month is July. Ronald Reagan Washington National Airport's busiest air travel month is October. These airports are only 30 miles apart!");
    var random = myarray[Math.floor(Math.random() * myarray.length)];
    //alert(random);
    document.getElementById("message").innerHTML=random;
}