async function fetchData(){
    try{
    const response = await fetch('https://api.giphy.com/v1/gifs/search?q=sun&limit=10&offset=2&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My')
    const jsondata = await response.json()
    console.log(jsondata)
    }catch (error) {
        // Handle any errors that occurred during the fetch request
        console.error('Error:', error);
      }
    
    
}
//3
async function starwars(){
    try{
        const response = await fetch('https://www.swapi.tech/api/starships/9/')
        const jsresponse = await response.json()
        console.log(jsresponse)

    }catch(error){
        console.error('Error:', error);
    }
}