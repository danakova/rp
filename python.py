from browser import document

def changeLabel(event):
            button = document['myButton']
            if button.text == "Nauč sa":
                button.text = "Otestuj sa"
            else:
                button.text = "Nauč sa"

document['myButton'].bind('click', changeLabel)

def toggle_state(button):
    button.classList.toggle('active')
    

