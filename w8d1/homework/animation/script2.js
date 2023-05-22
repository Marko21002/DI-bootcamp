function myMove() {
    var container = document.getElementById("container");
    var animate = document.getElementById("animate");
    var position = 0;
    var intervalId = setInterval(moveRight, 1);
  
    function moveRight() {
      if (position === container.offsetWidth - animate.offsetWidth) {
        clearInterval(intervalId);
      } else {
        position+=1;
        animate.style.left = position + "px";
      }
    }
  }
  