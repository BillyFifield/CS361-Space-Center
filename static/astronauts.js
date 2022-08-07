'use strict'

window.onload = function() {
    people();

}

async function people(){
    try{
        const API_URL = 'http://api.open-notify.org/astros.json';
        const response = await fetch(API_URL);
        const data = await response.json();
        console.log(`Table Data Source: ${API_URL}`);
        let astronautList = data['people'];
        let count = parseInt(data['number']);

        let keys = ['Name', 'Craft'];

        let tableData;
        
        let myTable = document.querySelector('#astronautTable');

        let table = document.createElement('table');
        let headerRow = document.createElement('tr');
        let header = document.createElement('th');

        keys.forEach(headerText => {
            let header = document.createElement('th');
            let textNode = document.createTextNode(headerText);
            header.appendChild(textNode);
            headerRow.appendChild(header);
        });

        table.appendChild(headerRow);

        for (let i = 0; i < count; i++){
            // Get data for each cell
            let name = astronautList[i]['name'];
            let craft = astronautList[i]['craft'];

            // Create an array containing the cell variables
            let tableData = [name, craft];

            let row = document.createElement('tr');
            
            tableData.forEach(spaceData => {
                let cell = document.createElement('td');
                let textNode = document.createTextNode(spaceData);
                cell.appendChild(textNode);
                // console.log(cell);
                row.appendChild(cell);
            });

            // console.log(row);
            table.appendChild(row);

            // myTable.appendChild(table);
        }
        // console.log(myTable);
        myTable.appendChild(table);





    } catch(error){
        console.error(error);
    }

};