var allBoldItems;

function getBoldItems() {
  const paragraph = document.querySelector('p');
  allBoldItems = paragraph.querySelectorAll('strong');
}

function highlight() {
  allBoldItems.forEach(item => {
    item.style.color = 'blue';
  });
}
function returnItemsToDefault() {
    allBoldItems.forEach(item => {
      item.style.color = 'black';
    });
  }

document.addEventListener('DOMContentLoaded', function() {
  getBoldItems();
  const paragraph = document.querySelector('p');
  paragraph.addEventListener('mouseover', highlight);
  paragraph.addEventListener('mouseout', returnItemsToDefault);
});
