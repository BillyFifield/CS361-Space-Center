'use strict'

window.onload = function() {
    document.getElementById("expressLink").addEventListener("click", getData)

}


async function getData(){

    try{
        const response = await fetch('https://api.nasa.gov/planetary/apod?api_key=4uHXJ6jK0bbHUzaAF70DaEfG6mq9uCuLpMNEIt76');
        const data = await response.json()
        let title = data['title']
        let description = data['explanation']
        let imageURL = data['url']
        let copyright = data['copyright']
        let img = document.getElementById('potdImage')
        // let potd = document.querySelector('#potdImage');
        let potd;
        if (imageURL.slice(0,24) == 'https://www.youtube.com/'){
            potd = document.createElement('video');
            potd.src = imageURL;
            potd.controls = true;
        }
        else{
            potd = new Image();
            potd.src = imageURL;
        }
        console.log(imageURL);
        copyright = '©' + copyright;
        // return()


        let titleChild = document.createTextNode(title)
        let copyrightChild = document.createTextNode(copyright)
        let descChild = document.createTextNode(description)
        console.log(title)
        console.log(descChild)
        
        const lineBreak = document.createElement("br")

        document.getElementById("potdTitle").appendChild(titleChild)
        document.getElementById("potdImage").appendChild(potd)
        document.getElementById("potdCR").append(copyrightChild)
        document.getElementById("potdCR").append(lineBreak)
        document.getElementById("potdDesc").appendChild(descChild)



  
    } catch(error){
        console.error(error)
    }
}