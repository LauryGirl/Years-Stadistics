def invert_count(student1, student2, rang = 0):
    
    order = student1.preferences
    to_order = student2.preferences

    #print(order)
    #print(to_order)

    #adoptar order y to_order a un criterio de comp con numeros
    dict_ = {}
    for i in range(len(order)):
        dict_[order[i][0]] = i

    #a -> array a analizar
    a = []
    for item in to_order:
        a.append(dict_[item[0]])
    
    #print(a)

    for i in range(len(a)):
        #buscar aqui nivel de coincidencia (exacto o con un por ciento de desplazamiento en las posiciones)
        if abs(i - a[i]) <= rang:
            try:
                #tuple -> ((tema, count), diferencia de posiciones)
                student1.likes[student2].append((to_order[i], abs(i - a[i])))
            except KeyError:
                student1.likes[student2] = [(to_order[i], abs(i - a[i]))]
            try:
                student2.likes[student1].append((to_order[i], abs(i - a[i])))
            except KeyError:
                student2.likes[student1] = [(to_order[i], abs(i - a[i]))]
        else:
            try:
                #tuple -> ((tema, count), diferencia de posiciones)
                student1.dislikes[student2].append((to_order[i], abs(i - a[i])))
            except KeyError:
                student1.dislikes[student2] = [(to_order[i], abs(i - a[i]))]
            try:
                student2.dislikes[student1].append((to_order[i], abs(i - a[i])))
            except KeyError:
                student2.dislikes[student1] = [(to_order[i], abs(i - a[i]))]