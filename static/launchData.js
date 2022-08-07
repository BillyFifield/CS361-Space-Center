'use strict'

window.onload = function() {
    launch();

}

async function launch(){
    try {
        // Fetch launch data from the API to fill the table
        const API_URL = 'https://fdo.rocketlaunch.live/json/launches/next/5';
        const response = await fetch(API_URL);
        const data = await response.json();
        console.log(`Table Data Source: ${API_URL}`);

        let keys = ['Provider', 'Vehicle', 'Mission Name', 'Mission Description & Time', 'Weather', 'Location', 'State', 'Country', ' '];
        let tableData;
        
        let myTable = document.querySelector('#table');

        let table = document.createElement('table');
        let headerRow = document.createElement('tr');
        let header = document.createElement('th');

        // Create the header row of the table
        keys.forEach(headerText => {
            let header = document.createElement('th');
            let textNode = document.createTextNode(headerText);
            header.appendChild(textNode);
            headerRow.appendChild(header);
        });

        table.appendChild(headerRow);
        // Fill the table with the data that was received from the API
        for (let i = 0; i < 5; i++){
            // Get data for each cell
            let provider = data['result'][i]['provider']['name'];
            let vehicleName = data['result'][i]['vehicle']['name'];
            let vehicle = document.createElement('a');
            let linkNode = document.createTextNode(vehicleName);
            vehicle.appendChild(linkNode);
            vehicle.title = vehicleName;
            vehicle.href = `/launch_craft/${provider} ${vehicleName}`;
            let missionName = data['result'][i]['missions'][0]['name'];
            let missionDesc = data['result'][i]['launch_description'];
            let weather = data['result'][i]['weather_summary'];
            if (weather === null){
                weather = 'Weather is not yet known.'
            }
            let location = data['result'][i]['pad']['location']['name'];
            let state = data['result'][i]['pad']['location']['statename'];
            if (state === null){
                state = 'N/A';
            }
            let country = data['result'][i]['pad']['location']['country'];
            
            // Call the flag microservice to get the source for the image
            const response = await fetch(`http://localhost:5353/country/${country}`);
            let flag_image = await response.text();
            console.log(`Country flag image source: ${flag_image}`);

            // Create an array containing the cell variables
            let tableData = [provider, vehicle, missionName, missionDesc, weather, location, state, country, flag_image];

            let row = document.createElement('tr');
            let textNode;
            
            // Fill each cell with the space data
            tableData.forEach(spaceData => {
                let cell = document.createElement('td');
                // If the data is the source of the country flag, first create an image element 
                if (spaceData === flag_image){
                    textNode = new Image(120,60);
                    textNode.src = spaceData;
                }
                else if (spaceData === vehicle){
                    textNode = vehicle;
                }
                else{
                    textNode = document.createTextNode(spaceData);
                }

                // Append the cells to the row
                cell.appendChild(textNode);
                row.appendChild(cell);
            });

            table.appendChild(row);   // Append the row to the table

        }

        myTable.appendChild(table);   // Append the created table to the myTable tag

    } catch(error){
        console.error(error);
    }
}
