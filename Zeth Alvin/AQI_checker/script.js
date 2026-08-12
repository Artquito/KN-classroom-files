// Selecting elements from the HTML
const cityInput = document.getElementById('cityInput');
const checkAqiBtn = document.getElementById('checkAqiBtn')
const airQualityResult = document.getElementById('airQualityResult');
const cityNameElement = document.getElementById('cityName');
const airQualityIndexElement = document.getElementById('airQualityIndex');
const airQualityDescriptionElement = document.getElementById('airQualityDescription');


// Store your API token
const apiToken = '51c33981f292424b1a99b49430800170e8999a45'; // Replace with your actual API token

// Function to get AQI description based on AQI value
// This function is based on the AQI categories defined by the US EPA
// Don't change this following aqi description function
function getAqiDescription(aqi) {
    if (aqi <= 50) {
        return { description: "Good", color: "#fafa3c" };
    } else if (aqi <= 100) {
        return { description: "Moderate", color: "#ffff00" };
    } else if (aqi <= 150) {
        return { description: "Unhealthy for Sensitive Groups", color: "#ff7e00" };
    } else if (aqi <= 200) {
        return { description: "Unhealthy", color: "#ff0000" };
    } else if (aqi <= 300) {
        return { description: "Very Unhealthy", color: "#8f3f97" };
    } else {
        return { description: "Hazardous", color: "#7e0023" };
    }
}

// async function to fetch air quality data
async function fetchAirQuality(city) {
        const apiUrl = `https://api.waqi.info/feed/${city}/?token=${apiToken}`;
        const response = await fetch(apiUrl);

        // Check if the response is ok
   


        // Check if data exists for the city
        

        
}

// Adding event listener to the button
checkAqiBtn.addEventListener('click', () => {

});

