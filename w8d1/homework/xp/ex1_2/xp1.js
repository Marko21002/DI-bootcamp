var h1 = document.querySelector("h1");
    console.log(h1);

var article = document.querySelector("article");
var paragraphs = article.querySelectorAll("p");
var lastParagraph = paragraphs[paragraphs.length - 1];
lastParagraph.remove();

var h2 = document.querySelector("h2")
var h3 = document.querySelector("h3")
h2.addEventListener("click", RespondClick);
function RespondClick() { 
    h2.style.backgroundColor = "red";
} 


h3.addEventListener("click", RespondClickHide);
function RespondClickHide() { 
    h3.style.display = "none";
} 

var boldButton = document.getElementById("boldButton");
var allParagraphs = document.querySelectorAll("p");
boldButton.addEventListener("click",RespondClickBold);
function RespondClickBold(){
    allParagraphs.forEach(function(paragraph) {
        paragraph.style.fontWeight = "bold";
      });
}