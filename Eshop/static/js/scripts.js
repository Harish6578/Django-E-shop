// Cart handling


// Add to cart
const products_container=document.getElementById('products-container');

let count_cart = document.getElementById('count_cart')

const csrfToken =document.querySelector("[name=csrfmiddlewaretoken").value

alert(csrfToken)