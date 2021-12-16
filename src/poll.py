from hierarchy import Theme_Context
from invert_array import invert_count
from likes_dislikes import Student_Preferences

"""
    themes -> {cocina: [dulce, salado],
                dulce: [postre, chocolate],
                salado: [carnes, cereales, jamon],
                deporte: [futboll, boleivol],
                futboll: [mundial],
                boleivol: [olimpiadas],
                olimpiadas: [Tokio, Beijing]}

    polls['Ivan'] -> {postres : [donnas, flan, torticas], 
              jamon: [serrano, baicon, ahumado], 
              queso: [gouda, blanco],
              cereales: [arroz, maiz],
              Tokio: [morenas del Caribe, Rusia],
              mundial: [2008, Espanna,  Alemania]}
    
    si esta no es la entrada adaptarlo al mismo
"""
def analize(themes, polls):
    theme_context = Theme_Context()
    students = []
    
    for item in themes:
        theme_context.create_theme(item, themes[item])

    for item in polls:
        students.append(Student_Preferences(item, polls[item]))
    
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            # se analizan los students sin repetir tuplas 
            invert_count(students[i], students[j])
    
    theme_context.stadistics_result(students)



p = {'Ivan': {'postres' : ['donnas', 'flan', 'torticas', 'cake'], 
              'jamon': ['serrano', 'baicon', 'ahumado'], 
              'queso': ['gouda', 'blanco'],
              'cereales': ['arroz', 'maiz'],
              'Tokio': ['morenas del Caribe', 'Rusia'],
              'mundial': ['2008',  'Alemania'],
              'Beijing': [],
              'chocolate': ['negro', 'blanco', 'leche']},
    'Juan': {'postres' : ['donnas', 'flan', 'torticas', 'cake'], 
              'jamon': ['serrano', 'baicon', 'ahumado'], 
              'queso': ['gouda', 'blanco'],
              'cereales': ['arroz', 'maiz'],
              'Tokio': [],
              'Beijing': [],
              'mundial': ['2008', 'Espanna',  'Alemania'],
              'chocolate': ['negro', 'blanco', 'leche']},
    'Ana': {'postres' : ['donnas'], 
              'jamon': ['serrano', 'baicon', 'ahumado'], 
              'queso': ['gouda', 'blanco'],
              'cereales': [],
              'Tokio': ['morenas del Caribe', 'Rusia'],
              'mundial': ['2008', 'Espanna',  'Alemania'],
              'Beijing': [],
              'chocolate': ['negro', 'blanco', 'leche']},
    'Manuel': {'postres' : ['donnas', 'flan', 'torticas', 'cake'], 
              'jamon': [], 
              'queso': ['gouda', 'blanco'],
              'cereales': ['arroz', 'maiz'],
              'Tokio': ['chinos', 'Rusia', 'coreanas'],
              'mundial': ['2008', 'Espanna',  'Alemania'],
              'Beijing': [],
              'chocolate': ['negro', 'blanco', 'leche']},
    'Rosa': {'postres' : ['donnas', 'flan', 'cake'], 
              'jamon': ['serrano', 'baicon', 'ahumado'], 
              'queso': [],
              'Beijing': [],
              'cereales': ['arroz', 'maiz'],
              'Tokio': ['morenas del Caribe', 'Rusia'],
              'mundial': [],
              'chocolate': ['negro', 'blanco', 'leche']} }
t = {
    'boleivol': ['olimpiadas'],
    'dulce': ['postres', 'chocolate'],
    'salado': ['cereales', 'jamon', 'queso'],
    'futboll': ['mundial'],
    'cocina': ['dulce', 'salado'],
    'deporte': ['futboll', 'boleivol'],
    'olimpiadas': ['Tokio', 'Beijing'],
    'Poll': ['cocina', 'deporte']}

    #tener siempre como padre del poll a la llave Poll con los subthemas q no tienen padre

analize(t, p)
