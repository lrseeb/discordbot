from random import choice, randint
from urheilu import kysymykset
from tiede import kysymykset

    
def question_handler(category_choice: int) -> tuple:

    if category_choice == 1:
        try:
            urheiluK = list(kysymykset.keys())
            for ui in urheiluK:
                ukysymys = ui
            uvastaus = kysymykset.get(ui)
            return (ukysymys, uvastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error')  # Placeholder values for error
    
    elif category_choice == 2:
        try:
            tiedeK = list(kysymykset.keys())
            for i in tiedeK:
                kysymys = i
            vastaus = kysymykset.get(i)
            return (kysymys, vastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error') 
    elif '3':
        return 'get question'
    elif '4':
        return 'get question'
    elif '5':
        return 'get question'
    elif '6':
        return 'get question'
    else:
        return ('get question', 'get answer')