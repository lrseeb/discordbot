from random import choice, randint
from urheilu import kysymykset
#from urheilu_v import vaihtoehot


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if '-t' in lowered:
        return 'Halutko pelata trivia peliä ? :DD (y/e)'
    else:
        pass
    
def got_response(user_input: str) -> str:        
    lowered: str = user_input.lower()

    if 'y' in lowered:
        return 'Valitse kategoria:\n1. Kirjallisuus\n2. Tiede\n3. Maantieto\n4. Vapaa-aika ja urheilu\n5. Historia\n6. viihde'
    elif '1' in lowered:
        try:
            #kysymys = 1

            urheiluK = list(kysymykset.keys())
            for i in urheiluK:
                kysymys = i
            
            vastaus = kysymykset.get(i)

            return (kysymys, vastaus)
            
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
        
    elif '2' in lowered:
        return 'get question'
    elif '3' in lowered:
        return 'get question'
    elif '4' in lowered:
        return 'get question'
    elif '5' in lowered:
        return 'get question'
    elif '6' in lowered:
        return 'get question'
    elif 'juu' in lowered:
        return 'kategoriaa ei ole :P'
    elif 'e' in lowered:
        return 'Eipä sitte mitään :\'(('
    elif 'bye' in lowered:
        return 'Heipä hei! D:'