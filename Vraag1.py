from random import randint, choice

def openFile():
        """
        Opent een bestand en doet deze in een lijst
        """
        o_infile = open("leerlingen.csv", "r")
        o_lines = o_infile.read().split("\n")
        o_infile.close()
        return o_lines

def makeStudentDict(m_lines):
        """
        Maakt een dictionary aan,
        Split de line in secties,
        de student staat op positie 0.
        de cijfers staan vanaf positie 1.
        van de cijfers worden floats gemaakt
        aan de dictionary, met de key van de student wordt
                een lijst van cijfers toegevoegd
        """
        m_studenten_cijfers = {}
        for m_line in m_lines:
                m_line = m_line.split(",")
                m_studenten_cijfers[m_line[0]] = []
                for m_cijfer in m_line[1:]:
                        m_cijfer = float(m_cijfer)
                        m_studenten_cijfers[m_line[0]].append(m_cijfer)
        return m_studenten_cijfers

def takeRandomStudentGrade(t_studenten_cijfers):
        """
        Er wordt een random student gekozen
                van de lijst van studenten door choice()
        Er wordt een random cijfer gekozen
                uit de lijst door randint
        
        De dictionary werkt met de studentennummers,
                en de lijst met indexen
        """
        t_studenten = []
        for t_studentnummer in t_studenten_cijfers.keys():
                t_studenten.append(t_studentnummer)

        t_randcijfer = randint(0, 2)
        t_randstudent = choice(t_studenten)

        return t_studenten_cijfers[t_randstudent][t_randcijfer]

def calculateAverageStudent(c_studenten_cijfers):
        """
        Voor elke student wordt de som en de lengte
        van alle cijfers genomen om het gemiddelde te berekenen
        Deze worden afgerond op 2 getallen achter de komma door round()
        De gemiddelde cijfers worden toegevoegd aan een lijst
        """
        c_gemiddelde_cijfers = []
        for c_student in c_studenten_cijfers.keys():
                c_som = sum(c_studenten_cijfers[c_student])
                c_lengte = len(c_studenten_cijfers[c_student])

                c_gemiddelde = round(c_som / c_lengte, 2)

                c_gemiddelde_cijfers.append(c_gemiddelde)
        return c_gemiddelde_cijfers

def calculateAverageCourse(c_studenten_cijfers):
        """
        Per kolom-waarde van alle studenten worden
                de gemiddelde cijfers per vak berekend
        deze worden afgerond op 2 cijfers achter de komma door round()
        """
        c_som_vak = [0, 0, 0]
        c_lengte = len(c_studenten_cijfers)
        for c_student in c_studenten_cijfers:
                c_som_vak[0] += c_studenten_cijfers[c_student][0]
                c_som_vak[1] += c_studenten_cijfers[c_student][1]
                c_som_vak[2] += c_studenten_cijfers[c_student][2]
        
        c_gemiddelde_vak = [0, 0, 0]
        for i in range(len(c_som_vak)):
                c_gemiddelde_vak[i] = round(c_som_vak[i] / c_lengte, 2)

        return c_gemiddelde_vak

def showData(s_studenten_cijfers, 
             s_gemiddelde_student,
             s_gemiddelde_vak,
             s_random_cijfer):
        """
        De data wordt op een zichtbare manier uitgeprint
        indien het gemiddelde meer dan een 8 is
                wordt dat aangegeven met Cum Laude!
        
        """
        print("Per vak is het gemiddelde: ", end="")
        for s_cijfer in s_gemiddelde_vak:
                print(s_cijfer, end=", ")
        print()
        
        s_count = 0
        for student in s_studenten_cijfers.keys():
                if s_gemiddelde_student[s_count] > 8.0:
                        print(f"Student: {student} had als gemiddelde: " +\
                              f"{s_gemiddelde_student[s_count]}. " +\
                               "Tot nu toe Cum Laude!")
                else:
                        print(f"Student: {student} had als gemiddelde: " +\
                              f"{s_gemiddelde_student[s_count]}. ")
                s_count += 1

        print(f"Het random cijfer is: {s_random_cijfer}")


def main():
        lines = openFile()
        studenten_cijfers = makeStudentDict(lines)
        random_cijfer = takeRandomStudentGrade(studenten_cijfers)
        gemiddelde_student = calculateAverageStudent(studenten_cijfers)
        gemiddelde_vak = calculateAverageCourse(studenten_cijfers)
        showData(studenten_cijfers,
                 gemiddelde_student,
                 gemiddelde_vak,
                 random_cijfer)
main()
"""
Nakijkmodel:
Indien er geen sprake is van gebruik van functies worden punten niet geteld.

45pt totaal.
        5pt file juist inlezen
        5pt dictionary juist aanmaken
        5pt random student kiezen uit de data
        10pt gemiddelde cijfer per student berekenen
        15pt gemiddelde cijfer per vak berekend
        5pt print functie juist gemaakt (output op de juiste manier laten zien)
"""
