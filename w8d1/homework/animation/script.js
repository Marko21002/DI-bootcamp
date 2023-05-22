var intervalId;
// function alertHelloWorld() {
//     alert("Hello World");
//   }
  
//   setTimeout(alertHelloWorld, 2000);

  function adding() {
    const container = document.getElementById("container");
    const newpar = document.createElement("p");
    newpar.textContent = "Hello World";
    container.appendChild(newpar);

    if(container.childElementCount ===5){
        clearInterval(intervalId);
    }


  }
intervalId = setInterval(adding, 2000);