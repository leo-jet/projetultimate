from sympy import *
import random

#Genere un entier non nul entre -5 et 5
def entier():
    n = 0 
    while(n==0):
        n = random.randint(-5, 5)
    return n

#Genere une racine carre entre racine de 2, racine de 3 et racine de 5
def racine_carre():
    a = random.choice([2,3])
    return sqrt(a)
    

#Operation de la forme a(x+yi)+b(x1+y1i)
def addition_dans_C():
    z = entier()+I*entier()
    z1 = entier()+I*entier()
    a = entier()
    b = entier()
    #Pour cette operation je dois generer l'ecriture de l'operation sinon il sera directement calcule par sympy
    if b<0:
        op = str(a)+'('+latex(z)+')'+str(b)+'('+latex(z1)+')'
    else:
        op = str(a)+'('+latex(z)+')+'+str(b)+'('+latex(z1)+')'
    sol = a*z+b*z1
    prop1 = a*z+a*z1
    prop2 = -a*z+b*z1
    prop3 = b*z-b*z1
    question = {
        "q": "Ecrire sous forme algebrique le nombre complexe suivant "+"$$$"+latex(op)+"$$$",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false},
            {"option": "$$"+latex(prop2)+"$$",      "correct": false},
            {"option": "$$"+latex(prop3)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result
    
    
    #operation de la forme (a+bi)^3
    #operation avec les racines carrées
    
    
#operation de la forme (a+bi)(x+yi)   
def multiplication_dans_C():
    z = entier()+I*entier()
    z1 = entier()+I*entier()
    op = z*z1
    sol = simplify(op)
    prop1 = z + z1
    prop2 = -z + z1
    prop3 = 2*z-z1
    question = {
        "q": "Ecrire sous forme algebrique le nombre complexe suivant "+"$$$"+latex(op)+"$$$",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false},
            {"option": "$$"+latex(prop2)+"$$",      "correct": false},
            {"option": "$$"+latex(prop3)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    
    return result


#operation de la forme (a+bi)/(x+yi)
def division_dans_C():
    z = entier()+I*entier()
    z1 = entier()+I*entier()
    op = z/z1
    sol = simplify(op)
    prop1 = simplify((z-2*z1)/z1)
    prop2 = simplify((z1+z)/z1)
    prop3 = simplify((z1-z)/z1)
    question = {
        "q": "Ecrire sous forme algebrique le nombre complexe suivant "+"$$$"+latex(op)+"$$$",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false},
            {"option": "$$"+latex(prop2)+"$$",      "correct": false},
            {"option": "$$"+latex(prop3)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result

#operation de la forme (a+bi)(x+yi)   
def multiplication_dans_C_avec_racine_carree():
    z = entier()*racine_carre()+I*racine_carre()
    z1 = entier()*racine_carre()+I*racine_carre()
    op = z*z1
    sol = collect(simplify(op), I)
    prop1 = collect(simplify(z*conjugate(z1)), I)
    prop2 = collect(simplify(conjugate(z)*z1), I)
    prop3 = collect(simplify(conjugate(z)*conjugate(z1)), I)
    question = {
        "q": "Ecrire sous forme algebrique le nombre complexe suivant "+"$$$"+latex(op)+"$$$",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false},
            {"option": "$$"+latex(prop2)+"$$",      "correct": false},
            {"option": "$$"+latex(prop3)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result


#operation de la forme (a+bi)/(x+yi)
def division_dans_C_avec_racine_carree():
    z = entier()*racine_carre()+I*racine_carre()
    x = racine_carre()
    y = racine_carre()
    a = entier()
    z1 = x+a*I*y
    z1_conjugue = x-a*I*y
    op = z/z1
    sol = collect(simplify(simplify(z*z1_conjugue)/simplify(z1*z1_conjugue)), I)
    prop1 = collect(simplify((z-2*z1)*z1_conjugue)/simplify(z1*z1_conjugue), I)
    prop2 = collect(simplify((z-z1)*z1_conjugue)/simplify(z1*z1_conjugue), I)
    prop3 = collect(simplify((z+z1)*z1_conjugue)/simplify(z1*z1_conjugue), I)
    question = {
        "q": "Ecrire sous forme algebrique le nombre complexe suivant "+"$$$"+latex(op)+"$$$",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false},
            {"option": "$$"+latex(prop2)+"$$",      "correct": false},
            {"option": "$$"+latex(prop3)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result

def affixe_point():
    a = entier()
    b = entier()
    repere = "Quel est l affixe du point A <div id=\"jxgbox\" class=\"jxgbox\" style=\"width:500px; height:500px;\"></div>"
    repere += "<script type=\"text/javascript\">"
    repere += "var board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox: [-6, 6, 6, -6], axis: true, showcopyright: false, shownavigation: false});"
    repere += "var p = board.create('point',["+str(a)+","+str(b)+"], {face:'+', size:1});"
    repere += "</script>"
    question = {
        "q": repere,
        "a": [
            {"option": "$$"+latex(a+b*I)+"$$",      "correct": true},
            {"option": "$$"+latex(b+a*I)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result

def affixe_vecteur():
    a = entier()
    b = entier()
    x = entier()
    y = entier()
    z = a+b*I
    z1 = x+y*I
    repere = "Quel est l affixe du vecteur AB <div id=\"jxgbox\" class=\"jxgbox\" style=\"width:500px; height:500px;\"></div>"
    repere += "<script type=\"text/javascript\">"
    repere += "var board = JXG.JSXGraph.initBoard('jxgbox', {boundingbox: [-6, 6, 6, -6], axis: true, showcopyright: false, shownavigation: false});"
    repere += "var p = board.create('point',["+str(a)+","+str(b)+"], {face:'+', size:1});"
    repere += "var q = board.create('point',["+str(x)+","+str(y)+"], {face:'+', size:1});"
    repere += "var v = board.create('arrow', [p, q]);"
    repere += "</script>"
    question = {
        "q": repere,
        "a": [
            {"option": "$$"+latex(z1-z)+"$$",      "correct": true},
            {"option": "$$"+latex(z-z1)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result

def affixe_vecteur_2():
    z = entier()+I*entier()
    z1 = entier()+I*entier()
    z2 = entier()+I*entier()
    x = entier()
    y = entier()
    sol = x*(z1-z)+y*(z2-z)
    prop1 = x*(z1+z)+y*(z2-z)
    prop2 = x*(z1-z)+y*(z2+z)
    prop3 = x*(z1+z)+y*(z2+z)
    question = {
        "q": "On considere les point A, B et C d affixes respectives"+"$$$"+latex(z)+","+ latex(z1)+","+ latex(z2)+ "$$$. Determiner l affixe de "+latex(x)+"AB+"+latex(y)+"AC",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false},
            {"option": "$$"+latex(prop2)+"$$",      "correct": false},
            {"option": "$$"+latex(prop3)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result

def conjugue():
    z = entier()+I*entier()
    z1 = entier()+I*entier()
    x = entier()
    y = entier()
    sol = conjugate(x*z+y*z1)
    prop1 = conjugate(x*z)+conjugate(y*z1)
    prop2 = conjugate(x*z-y*z1)
    question = {
        "q": "Soient les nombres complexes suivants"+"$$$"+latex(z)+","+ latex(z1) + "$$$. Ecrire sous forme algebrique le nombre complexe ... ",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false},
            {"option": "$$"+latex(prop2)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result
 
def module_complex():
    z = entier()+I*entier()
    sol = sqrt(simplify(conjugate(z)*z))
    prop1 = sqrt(simplify(conjugate(z*z)*z*z))
    question = {
        "q": "Calculer le module du nombre complexe suivant "+"$$$"+ latex(z) + "$$$",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result

def argument_complex():
    z = entier()+I*entier()
    sol = arg(z)
    prop1 = arg(conjugate(z))
    question = {
        "q": "Determiner l argument du nombre complexe suivant "+"$$$"+ latex(z) + "$$$",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result

#racine nieme d un nombre complexe
def calcul_racine_nieme(z, n):
    argument_c = arg(z)
    module_c = z*conjugate(z)
def racine_nieme():
    z = entier()+I*entier()
    sol = simplify(z**(1/2))
    prop1 = simplify((conjugate(z)))
    question = {
        "q": "Determiner la racine nieme du nombre complexe suivant "+"$$$"+ latex(z) + "$$$",
        "a": [
            {"option": "$$"+latex(sol)+"$$",      "correct": true},
            {"option": "$$"+latex(prop1)+"$$",      "correct": false}
        ],
        "correct": "Bonne reponse",
        "incorrect": "mauvaise reponse"# no comma here
    }
    result = str(question)
    result = result.replace("True", "true")
    result = result.replace("False", "false")
    return result

class PointGraphe(object):
    
    def __init__(self):
        self._x=0
        self._y=0
        
    def _set_x(self, a):
        self._x=a
        
    def _set_y(self, b):
        self._y=b 
    
    def _get_x(self):
        return self._x
    
    def _get_y(self):
        return self._y

class Graphe(object):
    plan = []
    def __init__(self, minX, maxX, minY, maxY):
        self._plan.append("var board = JXG.JSXGraph.initBoard('box', {boundingbox: ["+minX+","+maxX+","+maxY+","+minY+"], axis:true});")
        
    def _set_plan(self, elt, type):
        #ajouter un point 
        if type==0:
            self.plan.append("var p = board.create('point',["+elt.x+","+elt.y+"]);")
    
    def _get_plan(self):
        return self._plan
            
        
def exercice_37(type_triangle):
    zA = entier()+I*entier()
    zB = entier()+I*entier()
    zC = 0
    triangle = ""
    #triangle equilateral
    if type_triangle == 1:
        z1 = cos(pi/3)+I*sin(pi/3)
        z2 = zB-zA
        z = expand(z1*z2)
        zC += z+zA 
        triangle += "equilateral"
    #triangle isocele
    if type_triangle == 2:
        angle_liste = {pi/6,pi/4,-pi/6,-pi/4}
        angle = random.sample(angle_liste, 1)
        z1 = cos(angle[0])+I*sin(angle[0])
        z2 = zB-zA
        z = expand(z1*z2)
        zC += z+zA
        triangle += "isocele"
    #triangle rectangle isocele
    if type_triangle == 3:
        angle_liste = {pi/2,-pi/2}
        angle = random.sample(angle_liste, 1)
        z1 = cos(angle[0])+I*sin(angle[0])
        z2 = zB-zA
        z = expand(z1*z2)
        zC += z+zA
        triangle += "rectangle isocele"
     #triangle rectangle 
    if type_triangle == 4:
        angle_liste = {pi/2,-pi/2}
        angle = random.sample(angle_liste, 1)
        z1 = entier()*(cos(angle[0])+I*sin(angle[0]))
        z2 = zB-zA
        z = expand(z1*z2)
        zC += z+zA
        triangle += "rectangle"
    zC = collect(simplify(zC),I)
    enonce = "Soit A(${{"+latex(zA)+"}}$), B(${{"+latex(zB)+"}}$), C(${{"+latex(zC)+"}}$)."
    question = []
    question.append("Placer les points A, B et C.")
    question.append("Demontrer que le triangle ABC est "+triangle+".")
    question.append("Determiner l affixe du point D tel que ABCD soit un parallelogramme.")
    question.append("Determiner l affixe du point E symetrique de A par rapport au milieu de [BC].")
    
    titre = "Exercice 37"
    
    #CORRECTION
    zD = -zB+zA+zC
    zE = -zA+zB+zC
    minX = min(re(zA),re(zB),re(zC),re(zD))
    minY = min(im(zA),im(zB),im(zC),im(zD))
    maxX = max(re(zA),re(zB),re(zC),re(zD))
    maxY = max(im(zA),im(zB),im(zC),im(zD))
    solution = Graphe(minX, maxX, maxY, minX)
    solution.plan()
    p = Point()
    p.x= re(zA)
    correction = []
    correction.append(solution)
    content = {
               "zA": latex(zA), 
               "zB": latex(zB), 
               "zC": latex(zC),
               "enonce": enonce,
               "titre": titre,
               "question":question,
               }
    return content

def exercice_28(type):
    z = symbols("z")
    a = entier()+I*entier()
    b = entier()+I*entier()
    c = entier()
    d = I*entier()
    #une solution reelle
    if type == 1:
        P = (z-a)*(z-b)*(z-c)
    else:
        P = (z-d)*(z-b)*(z-c)
    
    P = collect(expand(P), z)
    enonce = "\\section{{Exercice 28}}"
    enonce += "Soit P le polynome defini par : \\\\ $" + latex(P)+"$.\\\\"
    if type == 1:
        enonce += "Demontrer qu il existe un nombre reel $\\alpha$ solution de l equation : P(z)=0\\\\"
    else:
        enonce += "Demontrer qu il existe un imaginaire pur $i\\beta$ solution de l equation : P(z)=0\\\\"
        
    enonce += "Determiner un polynome Q du second degre  tel que: P(z)=(z-alpha)Q(z)\\\\"
    enonce += "Resoudre dans C lequation : P(z) = 0\\\\"
     #CORRECTION
   
    content = {
               "enonce": enonce,
               }
    return content
    

