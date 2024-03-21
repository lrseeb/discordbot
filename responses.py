from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if '-trivia' in lowered:
        return 'Halutko pelata trivia peliä ? :DD (y/e)'
    else:
        return choice(['I do not understand...',
                        'What are you talking about?',
                        'Do you mind rephrasing that?'])
    
def got_response(user_input: str) -> str:        
    lowered: str = user_input.lower()

    if 'y' in lowered:
        return 'Valitse kategoria:\n1. Kirjallisuus\n2. Tiede\n3. Maantieto\n4. Vapaa-aika ja urheilu\n5. Historia\n6. viihde'
    elif '1' in lowered:
        return 'get question'
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