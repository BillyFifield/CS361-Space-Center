# CS361-Space-Center

The Space Center is a space themed application that allows the user to get up to date information on everything space. This includes information
on the next 5 launches from around the world, information on the space craft being launched, the location of the Internationial Space Station - including a
Google map link to the exact location, as well as data on who is currently in space.

The application in Flask and uses APIs from NASA, RocketLive, and a countryflag API. The application also features two different microservices. The first
microservice returns the image source of the flag of the country where the launch is taking place. The second microservice is a Wikipedia scraper
that gets a image and information about the space craft being launched.

To run this application, the following will need to be installed:
      pip install flask flask-cors
