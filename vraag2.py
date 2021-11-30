def calcNewBox(box, ans, extra):
        grootte = len(box)
        print()
        for i in range(len(box)):
                for j in range(len(box[i])):
                        pos = i*grootte + j
                        if (pos%grootte) == (ans%grootte):
                                box[i][j] += extra
                        elif pos == ans:
                                box[i][j] += extra
                        elif (pos//grootte) == (ans//grootte):
                                box[i][j] += extra

def printBox(box, grootte):
        c = grootte - 1
        for i in box:
                print(f"{grootte-c}|", end="")
                for j in i:
                        print(f"{j:>5}", end="")
                print()
                c -= 1
        print("-"*6*grootte)
        print("  ", end="")
        for i in range(grootte):
                print(f"{i+1:>5}", end="")
        print()


def vulBox(box, grootte):
        gebruikt = set()
        while len(gebruikt) < grootte**2:
                new_num = len(gebruikt) + 1
                printBox(box, grootte)
                ans = int(input(f"Waar wil je het nummer {new_num} invoegen?\n"))
                if ans not in gebruikt and ans < grootte**2 and ans > -1:
                        calcNewBox(box, ans, new_num)
                        gebruikt.add(ans)
        return box

def maakBox(grootte):
        box = []
        for i in range(grootte):
                minibox = []
                for j in range(grootte):
                        minibox.append(0)
                box.append(minibox)
        return box

def main():
        grootte = 3
        box = maakBox(grootte)
        box = vulBox(box, grootte)
        printBox(box, grootte)
main()
"""
Nakijkmodel:
Indien er geen sprake is van gebruik van functies worden punten niet geteld.

55pt totaal.
        10pt een box wordt op de juiste manier aangemaakt
                ([[],[],[]])

        10pt cijfers worden op de juiste manier gevraagd
                en ook niet meer gevraagd (stoppend bij 9 (unieke) getallen in de set / lijst)

        10pt alleen geldige cijfers kunnen worden ingevoerd door de user
                (getal > -1, getal < 9, getal niet al reeds gebruikt)

        15pt de juiste cijfers worden opgeteld met het juiste getal
                - 5pt kolomwaarden worden opgeteld
                - 5pt rijwaarden worden opgeteld
                - 5pt het juiste getal wordt opgeteld

        10pt de outputbox wordt op een overzichtelijke manier geprint naar het scherm
"""
