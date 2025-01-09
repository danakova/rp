from browser import document

def podstrankajedna(event):
    button = document['myButton']
    op1 = document["option1"]
    op2 = document["option2"]
    op3 = document["option3"]
    op4 = document["option4"]
    op5 = document["option5"]
    op6 = document["option6"]
    op7 = document["option7"]
    op8 = document["option8"]
    op9 = document["option9"]
    op10 = document["option10"]
    op11 = document["option11"]
    op12 = document["option12"]
    op13 = document["option13"]
    op14 = document["option14"]

if button.text == "Nauč sa":
    
    if op1.checked:
        op8.event.checked

document['enter'].bind('click', podstrankajedna)