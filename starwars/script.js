document.addEventListener('DOMContentLoaded', () => {
    const getRandomFactButton = document.getElementById('button');
    const loading = document.getElementById('loading');
    const fact = document.getElementById('container');
  
    getRandomFactButton.addEventListener('click', async () => {
      loading.style.display = 'block';
      fact.style.display = 'none';
  
      await fetchData();
  
      loading.style.display = 'none';
      fact.style.display = 'block';
    });
  
    // Rest of your code...
  });
 
async function fetchData(){
    const index =  Math.floor(Math.random() * 83);
    const fetched = await fetch('https://www.swapi.tech/api/people/' + index)
    const data = await fetched.json()
    displayFact(data.result.properties,index);
    
}

async function displayFact(character,index) {
    home = await fetch("https://www.swapi.tech/api/planets/" + index)
    homeworld = await home.json()
    console.log('Fetching', character)
    document.getElementById('name').textContent = character.name;
    document.getElementById('height').textContent = character.height;
    document.getElementById('gender').textContent = character.gender;
    document.getElementById('home').textContent = homeworld.result.properties.name;
    
    
}  