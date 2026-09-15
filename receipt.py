# Receipt Generator
from pyscript import document, display

def getting_total(e):
    selected_coffee = document.querySelector(
        "input[name='coffee']:checked"
    )
    subtotal = float(selected_coffee.value)
    vat = subtotal * 0.12
    total = subtotal + vat

    document.querySelector("#result").innerHTML = ""
    display(f"Subtotal: Php {subtotal}", target="result")
    display(f"Tax (12%): Php {vat}", target="result")
    display(f"Total payment: Php {total}", target="result")