// Selecting elements from the HTML
const cityInput = document.getElementById('cityInput');
const checkAqiBtn = document.getElementById('checkAqiBtn');
const airQualityResult = document.getElementById('airQualityResult');
const cityNameElement = document.getElementById('cityName');
const airQualityIndexElement = document.getElementById('airQualityIndex');
const airQualityDescriptionElement = document.getElementById('airQualityDescription');


// Store your API token
const apiToken = '51c33981f292424b1a99b49430800170e8999a45'; // Replace with your actual API token

// Function to get AQI description based on AQI value
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

// Function to fetch air quality data
async function fetchAirQuality(city) {
        const apiUrl = `https://api.waqi.info/feed/${city}/?token=${apiToken}`;
        const response = await fetch(apiUrl);

        // Check if the response is ok
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Check if data exists for the city
        if (data.status === 'ok') {
            const aqi = data.data.aqi;
            const aqiInfo = getAqiDescription(aqi);

            // Display the air quality data
            cityNameElement.innerText = city.charAt(0).toUpperCase() + city.slice(1); // Capitalize the first letter
            airQualityIndexElement.innerText = aqi;
            airQualityDescriptionElement.innerText = aqiInfo.description;
        } else {
            alert("Air quality data not available for this city.");
        }
}


// Adding event listener to the button
checkAqiBtn.addEventListener('click', () => {
    const city = cityInput.value.trim().toLowerCase(); // Make it lowercase to match API requirements
    if (city) {
        fetchAirQuality(city);
    } else {
        alert('Please enter a city name.');
    }
});