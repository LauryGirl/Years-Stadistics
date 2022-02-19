from .hierarchy import Theme_Context
from .invert_array import invert_count
from .likes_dislikes import Student_Preferences
import os

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
def analize(themes, p):
    theme_context = Theme_Context()
    students = []
    
    dicts_ = {}
    themes = themes_modify(themes, dicts_)
    polls = polls_modify(p, themes)

    for item in themes:
        theme_context.create_theme(item, themes[item])

    for item in polls:
        students.append(Student_Preferences(item, polls[item]))
    
    for i in range(len(students)):
        for j in range(i + 1, len(students)):
            # se analizan los students sin repetir tuplas 
            invert_count(students[i], students[j])
    
    theme_context.stadistics_result(students)

    for (key, value) in theme_context.stadistics.items():
        print(key)
        print(value.mode_text)
        print(value.median_text)
        print(value.variance_coef_text)
        
        for (k,v) in value.percent.items():
            print("Tema: " + str(k) + " representa un " + str(v) + " porciento")
        
        print("---------------------------------")    
    
    countf = 1
    while True:
        filePath = 'poll_' + str(countf) + ".txt"
        if checkFileExistance(filePath):
            countf += 1
        else:
            f = open(filePath, 'w')
            break
            
    text_ = ""
    for std in students:
        text_ += "////////////////////////////////////////////////////////////////////////////////////////////////\r\n"
        text_ += "Id del encuestado: " + str(std.name) + "\r\n"

        mark = False
        s = ""
        for a in std.preferences:
            if a[1] == 0:
                break
            mark = True
            s += str(a[0]) + " , "
        
        if mark:
            text_ += "Respuestas a la encuesta: " + "\r\n"
            text_ += s + "\r\n"

        text_ += "Gustos semejantes: " + "\r\n"

        for std1 in std.likes.keys():
            text_ += str(std1.name) + ":\r\r"
            for value in std.likes[std1]:
                if value[0][1] > 0:
                    text_ += str(value[0][0]) + " , "
            text_ += "\r\n"    
        
        text_ += "Gustos alejados: " + "\r\n"

        for std1 in std.dislikes.keys():
            text_ += str(std1.name) + ":\r\r"
            for value in std.dislikes[std1]:
                if value[0][1] > 0:
                    text_ += str(value[0][0]) + " , "
            text_ += "\r\n"    

    f.write(text_)
    f.close()


def checkFileExistance(filePath):
    try:
        with open(filePath, 'r'):
            return True
    except FileNotFoundError:
        return False
    except IOError:
        return False

def themes_modify(t, dict_):
    t0 = {}
    nones_count = 0

    for key, values in t.items():
        for value in values:
            if value == "none":
                dict_[key] = nones_count
                nones_count += 1

    for (theme, subthemes) in t.items():
        add = []
        for sub in subthemes:
            if sub == "none":
                add.append("none" + str(dict_[theme]))
            else:
                add.append(sub)
        t0[theme] = add
    return t0

def polls_modify(p, t):
    polls = {}

    for (student, poll) in p.items():
        p = {}
        for values in poll.values():
            for value in values:
                p[value] = ["1"]
        
        for values in t.values():
            for value in values:
                if (not (value in t.keys())) and (not (value in p.keys())):
                    p[value] = []

        polls[student] = p
    
    return polls
