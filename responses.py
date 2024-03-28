import random
from urheilu import urheiluKysymykset
from tiede import tiedeKysymykset

    
def question_handler(category_choice: int) -> tuple:

    if category_choice == 1:
        try:
            urheiluK = list(urheiluKysymykset.keys())
            random.shuffle(urheiluK)
            for ui in urheiluK:
                ukysymys = ui
            uvastaus = urheiluKysymykset.get(ui)
            return (ukysymys, uvastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error')
    
    elif category_choice == 2:
        try:
            tiedeK = list(tiedeKysymykset.keys())
            for i in tiedeK:
                kysymys = i
            vastaus = tiedeKysymykset.get(i)
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