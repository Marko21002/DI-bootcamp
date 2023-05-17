const planets = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune"
  ];


  planets.forEach((planet, index) => {
    const div = document.createElement("div");
    div.className = "planet planet-" + index;
    div.textContent = planet;
  
   
    const colors = ["#ff8080", "#ffcc80", "#ffff80", "#b3ff80", "#80ffbf", "#80ffd4", "#80e5ff", "#80b3ff"];
    div.style.backgroundColor = colors[index];
  
    document.body.appendChild(div);
  });
  