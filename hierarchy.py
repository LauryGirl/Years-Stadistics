from stadistics import Stadistics_Op

#como se acomodan los temas y los subtemas
class Theme_Scope:
    def __init__(self, name, parent = None):
        self.name = name
        self.subthemes = []
        self.parent = parent
        self.index = 0 if parent is None else len(parent)
    
    def __len__(self):
        return len(self.subthemes)
    
    def create_subtheme(self, name):
        sub = Theme_Scope(name, self)
        self.subthemes.append(sub)
        return sub
    
    def add_subtheme(self, sub):
        self.subthemes.append(sub)
        return sub

    def find_subtheme(self, name):
        for i in range(len(self.subthemes)):
            if self.subthemes[i].name == name:
                return self.subthemes[i]
        
        s = None
        for i in range(len(self.subthemes)):
            s = self.subthemes[i].find_subtheme(name)
            if s != None:
                return s
        return s

    def __str__(self):
        return str(self.name) + ' --------> ' + str([str(x.name) for x in self.subthemes])

class Theme_Context:
    def __init__(self):
        self.themes = {}
        self.hierarchy = {}
        self.stadistics = {}
        self.sort = []

    
    def create_theme(self, parent, childrens):
        if not (parent in self.themes):
            #no he sido hijo
            self.themes[parent] = Theme_Scope(parent)
        
        for child in childrens:
            if child in self.themes:
                #ya fui padre y encontre a mi padre
                self.themes[child].parent = self.themes[parent]
                self.themes[parent].add_subtheme(self.themes[child])
            else:
                self.themes[child] = self.themes[parent].create_subtheme(child)
            
            if not self.hierarchy.__contains__(child):
                self.hierarchy[child] = []
            if self.hierarchy.__contains__(parent):
                self.hierarchy[parent].append(child)
            else:
                self.hierarchy[parent] = [child]
        


    def get_theme(self, name):
        try:
            return self.themes[name]
        except KeyError:
            return ' '

    def __str__(self):
        return '{\n\t' + '\n\t'.join(y for x in self.themes.values() for y in str(x).split('\n')) + '\n}'

    def __repr__(self):
        return str(self)

    def topological_sort(self):
        self.sort = []  # topologic sort for types
        self.topological_sort__()  
        return self.sort 

    def topological_sort__(self):
        indeg = {key : 0 for key in self.hierarchy.keys()} 

        for u in self.hierarchy.keys():
            for v in self.hierarchy[u]:
                indeg[v] += 1


        roots = [key for key in indeg.keys() if indeg[key] == 0]   

        for u in roots:
            self.dfs(u)

    def dfs(self, v):
        self.sort.append(v)
        for child in self.hierarchy[v]:
            self.dfs(child)

    def stadistics_result(self, students):
        self.topological_sort()

        #realizar analisis con el sort

        """
        print(self.sort)
        for s in self.sort:
            print(str(self.themes[s]))
        """

        #pensar bien como hacer el analisis estadistico

        
        for student in students:
            student.update_likes(self.themes)
            #print(student.likes_count.items())
        
        self.sort.reverse()
        #analizar de hijos a padres
        #print(self.sort)

        for s in self.sort:
            #si no eres hoja te evaluas 
            if s in self.hierarchy.keys() and len(self.hierarchy[s]) > 0:
                self.stadistics[s] = Stadistics_Op(self.themes[s], students)
                self.stadistics[s].solve()