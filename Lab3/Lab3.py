import numpy as np

import csv
import matplotlib
import matplotlib.pyplot as plt

class BAYES():

    def __init__(self):
        self.promien=float(input('Podaj promien:'))
        [self.X1, self.Y1] = self.wczytaj('data1.csv')
        [self.X2, self.Y2] = self.wczytaj('data2.csv')
        self.drukuj(self.X1, self.X2, self.Y1, self.Y2, 0, 0)
        self.Petla();

        self.Centrox = 0
        self.Centroy = 0


        return

    def zwroc_liczbe_otaczajacych(self,wybor,px,py):

        if(wybor==0):
            tempx=self.X1
            tempy=self.Y1
        else:
            tempx = self.X2
            tempy = self.Y2

        Liczba=0;
        for i in range(len(tempx)):
            if( np.power((tempx[i]-px)**2 + (tempy[i]-py)**2 , 0.5) <= self.promien ):
                Liczba+=1

        return Liczba

    def zwroc_prawdopodobienstwa(self,px,py):
        C=len(self.X1) / (len(self.X1)+len(self.X2))
        B=len(self.X2) / (len(self.X1)+len(self.X2))

        C2 = self.zwroc_liczbe_otaczajacych(0, px, py) / len(self.X1)
        B2 = self.zwroc_liczbe_otaczajacych(1, px, py) / len(self.X2)

        Z="Liczba niebieskich:"+str(len(self.X2))+" Liczba czerwonych:"+str(len(self.X1))
        Z1="Otaczajace niebieskie:"+str(B2)+" Otaczajace czerwone:"+str(C2)
        print(Z)
        print(Z1)
        CK=C*C2
        BK=B*B2
        Z2 = "Prawdopodobienstwo niebieskie:" + str(BK) + " Prawdopodobienstwo czerwone:" + str(CK)
        print(Z2)

        return CK,BK

    def srednia(self):
        tx = 0
        ty = 0

        for i in range(len(self.X1)):
            tx += self.X1[i]
            tx += self.X2[i]
            ty += self.Y1[i]
            ty += self.Y2[i]
        tx /= len(self.X1)
        ty /= len(self.X1)

        self.Centrox = tx
        self.Centroy = ty 

        return

    def Petla(self):

        Dzialaj = True
        Powtorz = False
        tempx = self.promien
        while Dzialaj:

         if Powtorz == False:
            Temp=input('Dodac punkt ? (T - Tak / N- nie):')
         if(Temp is "T" or "t"):
             if (Powtorz == False):
                x=float(input('Podaj wsp x punktu:'))
                y=float(input('Podaj wsp y punktu:'))
                [Ck,Bk]=self.zwroc_prawdopodobienstwa(x,y)
                self.drukuj(self.X1, self.X2, self.Y1, self.Y2, x, y)

             Powtorz = False

             if Ck > Bk:
                 self.X1.append(x)
                 self.Y1.append(y)
             elif Ck < Bk :
                 self.X2.append(x)
                 self.Y2.append(y)
             else:
                 Powtorz=True
                 if(self.promien>0.05):
                     self.promien -= 0.05
                 continue

             self.promien = tempx

             self.drukuj(self.X1, self.X2, self.Y1, self.Y2, 0, 0)

         else:
             Dzialaj=False

        return

    def wczytaj(self,Nazwa):
        Q=[]
        with open(Nazwa, 'r') as csvfile:
           cos = csv.reader(csvfile, delimiter='|', quotechar='|')
           for wiersz in cos:
               Q.append(wiersz)

        X=[]
        Y=[]
        for i in range(len(Q)):
            X.append(Q[i][0])
            Y.append(Q[i][1])

        X=[i.replace(',', '.') for i in X]
        Y=[i.replace(',', '.') for i in Y]
        for i in range(len(X)):
            X[i]=float(X[i])
            Y[i]=float(Y[i])

        return X,Y


    def drukuj(self,X1,X2,Y1,Y2,x,y):

        if(x!=0 and y !=0):
            plt.plot(x,y,'go')
            obwod= plt.Circle((x, y), self.promien, color='g', fill=False)
            plt.gcf().gca().add_artist(obwod)
        plt.plot(X1, Y1, 'ro')
        plt.plot(X2, Y2, 'bo')
        plt.legend('GRB')
        plt.title('Pokaz przynaleznosci')
        plt.show()
        return



Zadanie=BAYES()

