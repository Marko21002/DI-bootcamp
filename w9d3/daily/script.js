const form = document.querySelector('#gifForm');
const categoryInput = document.querySelector('#categoryInput');
const gifContainer = document.querySelector('#gifContainer');
const deleteAllButton = document.querySelector('#deleteAllButton');
const apiKey = 'hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My';

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const category = categoryInput.value;

    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/random?api_key=${apiKey}&tag=${encodeURIComponent(category)}`);
        const data = await response.json();

        const gifUrl = data.data.images.original.url;

        // Create a div element for the GIF and the delete button
        const gifDiv = document.createElement('div');
        const gifImage = document.createElement('img');
        gifImage.src = gifUrl;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Delete';

        // Append the GIF image and delete button to the GIF div
        gifDiv.appendChild(gifImage);
        gifDiv.appendChild(deleteButton);

        // Append the GIF div to the container
        gifContainer.appendChild(gifDiv);

        // Add click event listener to the delete button
        deleteButton.addEventListener('click', () => {
            gifDiv.remove();
        });
    } catch (error) {
        console.error('Error:', error);
    }
});

deleteAllButton.addEventListener('click', () => {
    gifContainer.innerHTML = '';
});
