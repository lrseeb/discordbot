from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if '/trivia' in lowered:
        return 'Halutko pelata trivia peliä ? :DD (y/e)'
    elif 'y' in lowered:
        return 'Valitse kategoria: 1. Kirjallisuus\n2. Tiede\n3. Maantieto\n4. Vapaa-aika ja urheilu\n6. Historia'
    elif 'e' in lowered:
        return 'Eipä sitte mitään :\'(('
    elif 'bye' in lowered:
        return 'See you!'
    elif '1' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(['I do not understand...',
                       'What are you talking about?',
                       'Do you mind rephrasing that?'])