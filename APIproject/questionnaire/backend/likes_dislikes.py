from .avl import AVLSearchBinaryTree_Insert

class Student_Preferences:
    def __init__(self, name, answers):
        self.name = name
        self.answers = answers

        #gustos similares y distintos con los otros estudiantes
        self.likes = {}
        self.dislikes = {}
 
        self.avl = None
        self.preferences = []
        self.likes_count = {}
        self.preferences_take()

    
    def preferences_take(self):
        temp = []
        for item in self.answers:
            temp.append((item, len(self.answers[item])))
        
        self.avl = AVLSearchBinaryTree_Insert(temp[0], None, None, None)
        for i in range(1, len(temp)):
            self.avl.insert(temp[i])

        t = self.avl.in_order()
        for i in range(len(t) - 1, -1, -1):
            self.preferences.append(t[i])
    

    def parent_update_likes(self, themes, current_theme, add):
        try:
            self.likes_count[themes[current_theme.name].name] += add
        except KeyError:
            self.likes_count[themes[current_theme.name].name] = add
        
        if not (current_theme.parent is None):
            self.parent_update_likes(themes, current_theme.parent, add)


    def update_likes(self, themes):
        for pref in self.preferences:
            self.likes_count[themes[pref[0]].name] = pref[1]

            #parent_update
            if themes[pref[0]].parent is None:
                continue

            self.parent_update_likes(themes, themes[pref[0]].parent, pref[1])


    def __str__(self):
        s = self.name + ' -------> '
        s += ' Answers: '
        for a in self.answers:
            s += str(a) + '->' + str(self.answers[a]) + ' , '
        return s