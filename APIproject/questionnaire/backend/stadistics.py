class Stadistics_Op:
    #datos cualitativos

    def __init__(self, theme, students):
        self.theme = theme
        self.students = students

        #guardar resultados por estudiantes en la clase student -> creo que ya estan en answers y likes y dislikes
        """
            table[i] : [ni, Ni, fi, Fi] -> para datos agrupados
        """
        self.table = {}
        """
            list[i] : count -> para datos simples
        """
        self.list = []

        self.n = 0
        self.mean = 0
        self.mean_classe = None
        self.mode_classes = []
        self.mode_value = 0
        self.median_classe = None
        self.variance_ = 0
        self.typical_deviation_ = 0
        self.variance_coef = 0


        #Interpretacion de los resultados
        self.mean_text = ''
        self.mode_text = ''
        self.median_text = ''
        self.variance_coef_text = ''
 
        self.values_i = {}
        self.i_values = {}
        i = 1
        for sub in self.theme.subthemes:
            self.values_i[sub.name] = i
            self.i_values[i] = sub.name
            i += 1
    

    #tabla de distribucion empirica de frecuencia
    def empiric_distribution_table(self):
        self.n = len(self.students)

        ni = [0] * (len(self.theme.subthemes) + 1)
        Ni = [0] * (len(self.theme.subthemes) + 1)
        fi = [0] * (len(self.theme.subthemes) + 1)
        Fi = [0] * (len(self.theme.subthemes) + 1)

        for student in self.students:
            max_count = -1
            max_sub = ''

            for sub in self.theme.subthemes:
                if student.likes_count[sub.name] > max_count:
                    max_count = student.likes_count[sub.name]
                    max_sub = sub.name
            
            ni[self.values_i[max_sub]] += 1
            if self.n <= 15:
                self.list.append(self.values_i[max_sub])
    
        if self.n <= 15:
            return    
        
        accumulate_ni = 0
        accumulate_fi = 0
        for sub in self.theme.subthemes:
            fi[self.values_i[sub.name]] = ni[self.values_i[sub.name]] / self.n

            accumulate_ni += ni[self.values_i[sub.name]]
            accumulate_fi += fi[self.values_i[sub.name]]

            Ni[self.values_i[sub.name]] = accumulate_ni
            Fi[self.values_i[sub.name]] = accumulate_fi

        
        for sub in self.theme.subthemes:
            self.table[sub.name] = [ni[self.values_i[sub.name]], Ni[self.values_i[sub.name]], fi[self.values_i[sub.name]], Fi[self.values_i[sub.name]]]
                
        #print(self.table.items())

    #medidas de tendencia central
    def arithmetic_mean(self):
        if self.n > 15:
            add = 0
            for key in self.table.keys():
                add += self.table[key][0] * self.values_i[key]
            self.mean = round(add / self.n)
        else:
            add = 0
            for item in self.list:
                add += item
            self.mean = round(add / self.n)
        
        self.mean_classe =  self.i_values[self.mean]
        self.mean_text = "En el tema: " + str(self.theme.name) + ", los estudiantes tienen como gusto promedio a " + str(self.mean_classe) + "."
        #print(self.mean_text)
    

    def mode(self):
        value_count = {}

        if self.n <= 15:
            for i in range(len(self.list)):
                try:
                    value_count[self.i_values[self.list[i]]] += 1
                except KeyError:
                    value_count[self.i_values[self.list[i]]] = 1

            max_count = max(value_count.values())
            self.mode_value = max_count

            for key, value in value_count.items():
                if value == max_count:
                    self.mode_classes.append(key)

        else:
            max_count = max([t[0] for t in self.table.values()])
            self.mode_value = max_count

            for key in self.table.keys():
                if self.table[key][0] == max_count:
                    self.mode_classes.append(key)
        
        self.mode_text = "En el tema: " + str(self.theme.name) + ", la mayoria de estudiantes prefieren "
        if len(self.mode_classes) > 1:
            self.mode_text += "los topicos: "
            for classe in self.mode_classes:
                self.mode_text += classe + ", "
        else:
            self.mode_text += "el topico " + self.mode_classes[0] + ", "
        self.mode_text += "con una cantidad de " + str(self.mode_value) + " estudiantes."

        #print(self.mode_text)
        """
        print(self.mode_value)
        print(self.mode_classes)
        """

    def median(self):
        if self.n <= 15:
            self.list.sort()
            middle = int(self.n / 2)
            self.median_classe = self.i_values[self.list[middle]]
        else:
            for key, value in self.table.items():
                if value[1] >= int(self.n / 2):
                    self.median_classe = key
                    break
        
        self.median_text = "En el tema: " + str(self.theme.name) + ", el 50 porciento de los estudiantes prefieren el topico: " + str(self.median_classe) + "."
        #print(self.median_text)
        #print(self.median_classe)


    #medidas de dispersion
    def variance(self):
        add = 0
        if self.n <= 15:
            for item in self.list:
                add += (item - self.mean) ** 2
            self.variance_ = add / (self.n - 1) if self.n > 1 else add
        else:
            for key in self.table.keys():
                add += self.table[key][0] * (self.values_i[self.table[key]] - self.mean) ** 2
            self.variance_ = add / (self.n - 1) if self.n > 1 else add
        #print(self.variance_)

    def typical_deviation(self):
        self.typical_deviation_ = self.variance_ ** 0.5
        #print(self.typical_deviation_)
    
    def variance_coefficient(self):
        self.variance_coef = self.variance_ / self.mean
        #print(self.variance_coef)
        self.variance_coef_text = "En el tema: " + str(self.theme.name)
        if self.variance_coef >= 0 and self.variance_coef < 0.11:
            self.variance_coef_text += " se consideran los datos muy homogeneos, lo que supone que se este analizando al mismo individuo muchas veces."
        elif self.variance_coef >= 0.11 and self.variance_coef < 0.16:
            self.variance_coef_text += " se consideran los datos homogeneos, lo que supone que no tiene sentido su analisis."
        elif self.variance_coef >= 0.16 and self.variance_coef < 0.26:
            self.variance_coef_text += " se consideran los datos heterogeneos, lo que supone que existen muchos datos a analizar, lo cual es factible."
        else:
            self.variance_coef_text += " se consideran los datos muy heterogeneos, lo que supone que se esten analizando individuos tan distintos que no se podria encontrar un patron de comportamiento."
        #print(self.variance_coef_text)        

    def solve(self):
        #calculate
        self.empiric_distribution_table()
        self.arithmetic_mean()
        self.mode()
        self.median()
        self.variance()
        self.typical_deviation()
        self.variance_coefficient()