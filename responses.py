import random
from maantieto import maaKysymykset
from viihde import viihdeKysymykset
from historia import historiaKysymykset
from kirjallisuus import kirjaKysymykset
from tiede import tiedeKysymykset
from urheilu import urheiluKysymykset
    
def question_handler(category_choice: int) -> tuple:

    if category_choice == 1:
        try:
            maaK = list(maaKysymykset.keys())
            random.shuffle(maaK)
            for i in maaK:
                kysymys = i
            vastaus = maaKysymykset.get(i)
            maaKysymykset.pop(i)
            if not maaKysymykset:
                return ('Ei enää kysymyksiä tästä kategoriasta, valitse uusi', 'Ei enää kysymyksiä tästä kategoriasta, valitse uusi')
            else:
                return (kysymys, vastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error') 
    
    elif category_choice == 2:
        try:
            viihdeK = list(viihdeKysymykset.keys())
            random.shuffle(viihdeK)
            for i in viihdeK:
                kysymys = i
            vastaus = viihdeKysymykset.get(i)
            viihdeKysymykset.pop(i)
            if not viihdeKysymykset:
                return ('Ei enää kysymyksiä tästä kategoriasta, valitse uusi', 'Ei enää kysymyksiä tästä kategoriasta, valitse uusi')
            else:
                return (kysymys, vastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error') 

    elif category_choice == 3:
        try:
            historiaK = list(historiaKysymykset.keys())
            random.shuffle(historiaK)
            for i in historiaK:
                kysymys = i
            vastaus = historiaKysymykset.get(i)
            historiaKysymykset.pop(i)
            if not historiaKysymykset:
                return ('Ei enää kysymyksiä tästä kategoriasta, valitse uusi', 'Ei enää kysymyksiä tästä kategoriasta, valitse uusi')
            else:
                return (kysymys, vastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error') 
    
    elif category_choice == 4:
        try:
            kirjaK = list(kirjaKysymykset.keys())
            random.shuffle(kirjaK)
            for i in kirjaK:
                kysymys = i
            vastaus = kirjaKysymykset.get(i)
            kirjaKysymykset.pop(i)
            if not kirjaKysymykset:
                return ('Ei enää kysymyksiä tästä kategoriasta, valitse uusi', 'Ei enää kysymyksiä tästä kategoriasta, valitse uusi')
            else:
                return (kysymys, vastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error') 
    
    elif category_choice == 5:
        try:
            tiedeK = list(tiedeKysymykset.keys())
            random.shuffle(tiedeK)
            for i in tiedeK:
                kysymys = i
            vastaus = tiedeKysymykset.get(i)
            tiedeKysymykset.pop(i)
            if not tiedeKysymykset:
                return ('Ei enää kysymyksiä tästä kategoriasta, valitse uusi', 'Ei enää kysymyksiä tästä kategoriasta, valitse uusi')
            else:
                return (kysymys, vastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error') 
        
    elif category_choice == 6:
        try:
            urheiluK = list(urheiluKysymykset.keys())
            random.shuffle(urheiluK)
            for i in urheiluK:
                kysymys = i
            vastaus = urheiluKysymykset.get(i)
            urheiluKysymykset.pop(i)
            if not urheiluKysymykset:
                return ('Ei enää kysymyksiä tästä kategoriasta, valitse uusi', 'Ei enää kysymyksiä tästä kategoriasta, valitse uusi')
            else:
                return (kysymys, vastaus)
        except Exception as e:
            print("Error reading or parsing JSON file:", e)
            return ('Error', 'Error')
        
    else:
        return ('get question', 'get answer')