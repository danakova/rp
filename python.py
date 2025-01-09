from browser import document

def changeLabel(event):
            button = document['myButton']
            moznosti = document["moznosti"]
            if button.text == "Nauč sa":
                button.text = "Otestuj sa"
                moznosti.style.visibility = "visible"

            else:
                button.text = "Nauč sa"
                moznosti.style.visibility = "hidden"

document['myButton'].bind('click', changeLabel)

def toggle_state(button):
    button.classList.toggle('active')
    

