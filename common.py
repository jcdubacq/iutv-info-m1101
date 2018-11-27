from __future__ import print_function
import math
import random
from IPython.display import display, Markdown, Latex, HTML, Image
import ipywidgets as widgets
import datetime
import os


interactif = False

class utils(object):
    def __init__(self, inter, seed = None):
        self.switch(inter)
        self.widgets = widgets
        self.blank = '`_____________________________________________________`'
        mode='Ce cours a été régénéré le {0}.'.format(datetime.datetime.now())
        if self.answers:
            mode = mode + ' Mode avec corrigé.'
        else:
            mode = mode + ' Mode sans corrigé.'
        if self.interactif:
            mode = mode + ' Mode interactif.'
        else:
            mode = mode + ' Mode statique.'
        if seed != None:
            mode = mode + ' Modèle numéro {}.'.format(seed)
            random.seed(seed)
        print(mode)
        tikzmode = True
        try:
            get_ipython().run_line_magic('reload_ext', 'tikzmagic')
        except(ModuleNotFoundError):
            tikzmode = False
        try:
            os.stat("/usr/bin/pdflatex")
        except:
            tikzmode = False
        self.tikzmode = tikzmode
    def switch(self,inter):
        self.interactif = False
        self.answers = False
        if inter == "PDF+SOL":
            self.interactif = False
            self.answers = True
        if inter == "INTER":
            self.interactif = True
            self.answers = False
        if inter == "PROF":
            self.interactif = True
            self.answers = True
    def __str__(self):
        return "{} ".format(self.__class__.__name__)

    def tikz(self,tikzfile,tikzargs,tikzstring):
        tikzpath="tikz/{0}.png".format(tikzfile)
        if self.tikzmode:
            try:
                os.stat("tikz")
            except:
                os.mkdir("tikz")
            try:
                display(Markdown('Figure `{0}*`.'.format(tikzfile)))
                a=get_ipython().run_cell_magic("tikz","-S "+tikzpath+' '+tikzargs,tikzstring)
            except(FileNotFoundError):
                try:
                    os.stat(tikzpath)
                    display(Markdown('Figure `{0}`.'.format(tikzfile)))
                    display(Image(filename=tikzpath))
                except(FileNotFoundError):
                    display(Markdown('La figure `{0}` est introuvable.'.format(tikzfile)))
        else:
            try:
                os.stat(tikzpath)
                display(Image(filename=tikzpath))
            except(FileNotFoundError):
                display(Markdown('La figure `{0}` est introuvable.'.format(tikzfile)))

    def mark(self,m):
        display(Markdown(m))

    def xtoggle(self):
        if self.interactif:
            print("Mode automatique")
            self.interactif = False
        else:
            print("Mode interactif")
            self.interactif = True
    def soltoggle(self):
        if self.answers:
            print("Mode sans correction")
            self.answers = False
        else:
            print("Mode corrigé")
            self.answers = True

    def activite(self,title):
        display(Markdown('#### Activité : '+title))

    def yes_no(self,question,default=False):
        rep=''
        print('', end='', flush=True)
        if len(question)>0:
            question=question+' '
        if default:
            question=question+'[o/N]> '
        else:
            question=question+'[O/n]> '
        if not (self.interactif):
            if default:
                print(question+'o',flush=True)
            else:
                print(question+'n',flush=True)
            return default
        while rep!='o' and rep!='n':
            rep=input(question)
        return rep == 'o'
    
    def question(self,markdown):
        print('', end='', flush=True)
        display(Markdown(markdown))
        if (self.interactif):
            rep=input('Votre proposition > ')
        else:
            display(Markdown(self.blank))
    def solcomment(self,markdown):
        if self.answers:
            display(Markdown(markdown))
    
    def questionint(self,markdown,rangelow,rangehigh):
        print('', end='', flush=True)
        display(Markdown(markdown))
        if (self.interactif):
            rep=input('Un entier > ')
            return(int(rep))
        else:
            rep=random.randint(rangelow,rangehigh)
            display(Markdown('Un entier > `{0}`'.format(rep)))
            return(rep)
    
    def solution(self,markdown):
        print('', end='', flush=True)
        if (self.interactif):
            rep=input('Votre proposition > ')
        else:
            display(Markdown('Votre proposition > '+self.blank))
        if self.answers:
            display(Markdown('**Solution:** '+markdown))
    
    def solutioncheck(self,question, answer, feedback_yes, feedback_no):
        print('', end='', flush=True)
        ret=False
        if (self.interactif):
            rep=input(question+' > ')
            display(Markdown('Vous avez répondu : '+rep))        
            if rep==answer:
                display(Markdown(feedback_yes))
                ret=True
            else:
                display(Markdown(feedback_no))
        else:
            display(Markdown(question+' > '+self.blank))
            if self.answers:
                display(Markdown('**Solution :** '+answer))
        return ret
    
    def reasonablenumbertostr(self,f):
        sign=True
        if f<0:
            sign=False
            f=-f
        a=math.floor(f)
        b=f-a
        if b<0.000001:
            b=0.0
        if b > 0.999999:
            b=0.0
            a=a+1
        s=''
        e=0
        while(a>0):
            e=e+1
            if e>3 and e%3 == 1:
                s='~'+s
            s=str(a%10)+s
            a=a//10
        if b>0:
            if s=='':
                s='0,'
            else:
                s=s+','
            e=0
            while(b>0):
                e=e+1
                if e>3 and e%3 == 1:
                    s=s+'~'
                b=b*10
                if b-math.floor(b)>.999999:
                    b=math.floor(b)+1
                s=s+str(int(math.floor(b)))
                b=b-math.floor(b)
                if b<0.000001:
                    b=0.0
        if s=='':
            return '0'
        if sign:
            return s
        return '-'+s
    
    def numbertostr(self,f,dollar=True):
        e=0
        d=''
        if dollar:
            d='$'
        if (abs(f))<0.01 and f>0:
            while abs(f)<0.999999 and f>0:
                f=10*f
                e=e-1
        x=self.reasonablenumbertostr(f)
        if e<0 or e>0:
            if x!='1':
                return d+x+'×10^{'+str(e)+'}'+d
            else:
                return d+'10^{'+str(e)+'}'+d
        else:
            return d+x+d
        
    def n2s(self,f):
        return self.numbertostr(f,dollar=False)
    
    def twobyten(self,lead,two,ten,final):
        # if final, eliminate small powers of two and all powers of ten
        if final:
            if two<-8 or two>8:
                lead=lead*math.pow(10,ten)
                ten=0
            else:
                lead=lead*math.pow(2,two)*math.pow(10,ten)
                two=0
                ten=0
            if lead == 0:
                two=0
                ten=0
    
        root=self.numbertostr(lead)
        root=root.replace('$','') # remove math markers
        if two!=0:
            if root != '1':
                root = root+'×2^{'+str(two)+'}'
            else:
                root = '2^{'+str(two)+'}'
        if ten!=0:
            if root != '1':
                root = root+'×10^{'+str(ten)+'}'
            else:
                root = '10^{'+str(ten)+'}'
        return '$'+root+'$'

    def basicmachine(self,mem,memi,outputratio = 4):
        next=0
        step=0

        r=[0,0,0,0]
        pc=0

        inst=['—']
        val1=0
        val2=0
        result=0

        phase="Booting"

        header='| Étape | Phase | R0 | R1 | R2 | R3 | INST | VAL1 | VAL2 | RESULT | MEM |'
        headel='|-------|-------|----|----|----|----|------|------|------|--------|-----|'

        out=[header,headel]
        olda=[]

        def output(olda):
            a=[]
            a.append(str(step))
            a.append(str(phase))
            a=a+[c for c in map(str,r)]
            a.append(' '.join(inst))
            a.append(str(val1))
            a.append(str(val2))
            a.append(str(result))
            lastnz=0
            for i in range(0,len(mem)):
                if mem[i]!=0:
                    lastnz=i
            if lastnz+1==len(mem):
                a.append(','.join(mem))
            else:
                a.append(','.join(map(str,mem[:lastnz+1]))+'...')
            b=a.copy()
            for x in range(0,len(a)):
                if (len(olda)>0):
                    if (olda[x]!=a[x]):
                        b[x]='**'+a[x]+'**'
            olda=a.copy()
            l="|"+(" | ".join(b))+"|"
            out.append(l)
        outputratio=4
        output(olda)

        # LOAD PUT STORE ADD MUL SUB CMP0 GOTO
        # LOAD charge depuis la mémoire dans un registre
        # PUT met un entier dans un registre
        # STORE met depuis un registre dans la mémoire
        # ADD MUL et SUB font des opérations entre deux registres et mettent le résultat dans un registre
        # CMP0 va à une adresse si deux registres sont égaux
        # GOTO va a une adresse
        # STOP arrête la machine

        while True:
            step = step + 1
            phase="Instruction"
            inst=memi[pc]
            codeop=inst[0]
            if len(inst)>1:
                argone=inst[1]
            if len(inst)>2:
                argtwo=inst[2]
            if len(inst)>3:
                argthree=inst[3]
            else:
                argthree="-"
            if outputratio==4:
                output(olda)
            phase="Preparation"
            if codeop=="LOAD":
                val1=mem[int(argone)]
            if codeop=="STORE":
                val1=r[int(argtwo)]
            if codeop=="ADD" or codeop=="SUB" or codeop=="MUL":
                val1=r[int(argone)]
                val2=r[int(argtwo)]
            if codeop=="PUT":
                val1=int(argone)
            if codeop=="GOTO":
                val1=int(argone)
            if codeop=="CMP0":
                val1=int(argone)
                val2=r[int(argtwo)]
            if codeop=="STOP":
                break
            if outputratio==4:
                output(olda)
            phase="Execution"
            next=pc+1
            if codeop=="ADD":
                result=val1+val2
            if codeop=="SUB":
                result=val1-val2
            if codeop=="MUL":
                result=val1*val2
            if codeop=="LOAD" or codeop=="STORE" or codeop=="PUT":
                result=val1
            if codeop=="GOTO":
                next=val1
            if codeop=="CMP0":
                if val2==0:
                    next=val1

            if outputratio==4:
                output(olda)
            phase="Store"
            if codeop=="LOAD" or codeop=="PUT":
                r[int(argtwo)]=result
            if codeop=="STORE":
                mem[int(argone)]=result
            if codeop=="ADD" or codeop=="MUL" or codeop=="SUB":
                r[int(argthree)]=result
            pc=next
            output(olda)
        phase="Stop"
        output(olda)

        def outputn(Step):
            self.mark('\n'.join(out[:(outputratio*Step+3)]))

        if self.interactif:
            w=self.widgets.interactive(outputn, Step=(0,(len(out)-1)//outputratio))
            w.children[0].value=w.children[0].max
            w.children[0].description='Étape'
            display(w)
        else:
            outputn((len(out)-1)//outputratio)
                

