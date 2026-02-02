// Cart handling


// Add to cart
const products_container=document.getElementById('products-container');

let count_cart = document.getElementById('count_cart')

const csrfToken =document.querySelector("[name=csrfmiddlewaretoken").value

// add to cart url 
const addUrl=products_container.dataset.addUrl


// adding event listener onto product cards through  their parent container 

products_container.addEventListener('chick',async function (event) {
    return;
})