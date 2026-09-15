# Sku Generator
from pyscript import document


def generate_sku(e):
    category = document.querySelector("#category").value
    product_name = document.querySelector("#product-name").value
    stock_quantity = document.querySelector("#stock-quantity").value

    product_name = product_name.upper()
    product_name = product_name.replace(" ", "")
    product_code = product_name[:2]
    stock_code = stock_quantity[-2:]
    sku = category[:3] + product_code + stock_code

    document.querySelector("#sku-result").innerText = sku
    document.querySelector("#sku-details").innerText = (
        "Category: " + category +
        " | Product: " + product_name +
        " | Stock: " + stock_quantity
    )
button = document.querySelector("#generate-sku")
button.addEventListener("click", generate_sku)


