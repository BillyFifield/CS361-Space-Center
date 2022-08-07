'use strict'

window.onload = function() {
    launch();

}

async function spaceCraft(){
    try{
        const amqp = require('amqplib/allback_api');

        const messageQueueURL = 
                "amqps://bzwlgfru:nSPek3rNzDaKr_OrsM0rmBUGDHf7HROz@beaver.rmq.cloudamqp.com/bzwlgfru";


        amqp.connect(messageQueueURL, function (error0, connection) {

            if (error0) {
                throw error0;
            }

            connection.createChannel(function (error1, channel) {
                if (error1){
                    throw error1;
                }

                const queue = 'wikiscraperQuery';

                channel.assertQueue(queue, {
                    durable: false,
                });

                let fh = channel.sendToQueue(queue, Buffer.from('Falcon Heavy'));
                console.log(fh);
            });
        });

        let spaceImg = document.querySelector('#spacePhoto');
        
        let craftImg = new Image(120,60);
        craftImg.src = fh['img'];

        spaceImg.appendChild(img);
        




    } catch(error){
        console.error(error);
    }
}