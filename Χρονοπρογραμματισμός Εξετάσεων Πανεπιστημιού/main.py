from itertools import combinations
import networkx

def readSTU(filename):
    # Μεταβλητές
    # koinoispudastes dictionary που έχει τους κοινούς σπουδαστές ανάμεσα σε δύο περιόδους
    koinoispoudastes= dict()
    # Ο αριθμός των μαθητών
    spoudastes = 0
    # Το μεγαλύτερο μάθημα = Συνολικός αριθμός μαθημάτων
    megalyteroMathima = 0
    # Ο πίνακας συγκρούσεων
    koinaSet = set()


    # Ανάγωνση του αρχείου
    file1 = open(filename, 'r')
    # Ανάγωνση των γραμμών
    Lines = file1.readlines()

    #  Έλεγχος για κάθε γραμμή
    for line in Lines:
        # Κάθε γραμμή είναι και ένας σπουδαστής
        spoudastes += 1
        # Αφαιρούνται τα κενά
        line = line.strip()

        # Διαχωρίζονται οι γραμμές
        grammh = line.split(" ")

        # Μετατρέπεται  απο string σε int
        for i in range(0, len(grammh)):
            # Ελέγέται ότι έχέι διαβάστεί σωστά και δεν έχω κενό
            if (isinstance(grammh[i], str)and (grammh[i] != '')):
                grammh[i]=grammh[i].strip()
                # Μετατρέπέται σε Int
                grammh[i] = int(grammh[i])
                # Ελέγχεται μήπως είναι το μεγαλύτερο μάθημα
                if grammh[i] > megalyteroMathima:
                    megalyteroMathima = grammh[i]

        # Αναζήτηση για πιθανούς συνδιασμούς με μέγεθος 2 δηλαδή για το {12,23,34) θα βγούν {12,23},{12,34},{23,34}
        comb = combinations(grammh, 2)

        # Για κάθε δυάδα από το comb
        for i in list(comb):
            # Προστήθεται ο συνδιασμό στον πίνακα συγκρούσεων
            koinaSet.add(i)
            # Προστήθεται ο συνδιασμό στο dictionary
            key = (i[0], i[1])
            # ΈλέγχΟς στο dictionary koinoimathites εάν υπάρχει το κλειδί, δλδ αν έχει ξαναπεραστεί  ο συνδιασμός και αυξάνω κατά 1 κονό μαθητή
            if key in koinoispoudastes:
                koinoispoudastes[key] = koinoispoudastes[key] + 1
            else:
                # αλλιώς το εκινώ με τον πρώτο μαθητή
                koinoispoudastes[key] = 1

    # Αναφορές
    # Όνομα προβλήματος
    print("Όνομα αρχείου:", filename)
    # αριθμός μαθητών
    print("Αριθμός μαθητών: ", spoudastes)
    # αριθμός μαθημάτων
    print("Τα μαθήματα είναι: ", megalyteroMathima)
    # Υπολογίζω την πυκνότητα για όλων τον πίνακα
    maxpinakas = megalyteroMathima * megalyteroMathima
    pyknothta = (len(koinaSet) * 2) / maxpinakas
    print("Η πυκνότητα είναι ", pyknothta)

    # Δημιουργία Γραφήματος
    grafhma = networkx.Graph()

    # Εισαγώγη των μαθήματων στο γράφημα
    for i in range(megalyteroMathima):
        grafhma.add_node(i + 1)

    # Εισαγωγή των συγκρούσεων στο γράφημα
    for koino in koinaSet:
        grafhma.add_edge(koino[0], koino[1])

    # Graph Coloring
    minXrwmata = 500
    straghgikh_pou_xrhsimopoihthke = ""
    strategikes = ["largest_first","smallest_last","DSATUR"] # Οι στρατηγικές που χρησιμοποιόυνται
    for straghgikh in strategikes:                           # Δοκιμή και των τριών στρατηγικών για το πρόβλημα
        xrwmatismos = networkx.coloring.greedy_color(grafhma, strategy=straghgikh)
        maxXrwmata = 0
        #βρίσκω τον αριθμό των χρωμάτων (περιόδων) που χρησιμοποιήθηκαν
        for mathima in xrwmatismos:
            if xrwmatismos[mathima] > maxXrwmata:
                maxXrwmata = xrwmatismos[mathima]
        #Εάν έχουν χρησιμοποιηθεί λιγότερες περίοδοι κρατάω αυτήν την στρατηγική και τον χρωματισμό
        if minXrwmata > maxXrwmata:
            d = xrwmatismos
            minXrwmata = maxXrwmata
            straghgikh_pou_xrhsimopoihthke = straghgikh


    print("Στατιγική που χρησιμοποιήθηκε", straghgikh_pou_xrhsimopoihthke)
    # Βαθμολόγηση των σπουδαστων για κάθε μάθημα
    bathmologia = 0
    # Ελέχω όλους τους συνδιασμούς μαθημάτων πχ (1,2), (1,3) ... (2,3) από μία φορά
    for i in range(1, megalyteroMathima + 1):
        for j in range(i + 1, megalyteroMathima + 1):
            # Για να μην πετάει error
            # Επιλογή  ποινής μαθημάτων  ανάλαγα με τις  περιόδους
            if key in koinoispoudastes.keys():
                # Βρίσκεται η  διαφορά των περιόδων των δύο εξετάσεων
                diafora = abs(d[i] - d[j])
                # Βρίσκέται με βάσει το dictionary τους κοινούς μαθητές
                koinoi_mathtes = koinoispoudastes[key]
                # Προστήθεται στην βαθμολογία τις ποινές ανάλογα με την απόσταση των περιόδων
                if diafora == 1:
                    bathmologia = bathmologia + koinoi_mathtes * 16
                if diafora == 2:
                    bathmologia = bathmologia + koinoi_mathtes * 8
                if diafora == 3:
                    bathmologia = bathmologia + koinoi_mathtes * 4
                if diafora == 4:
                    bathmologia = bathmologia + koinoi_mathtes * 2
                if diafora == 5:
                    bathmologia = bathmologia + koinoi_mathtes * 1
    # Υπολογισμός βαθμολογίας Τελική = Συνολική / Αριθμός Σπουδαστών
    telikhBathmologia = bathmologia / spoudastes
    print(telikhBathmologia)
    print("Χρησιμοποιήθηκαν ", minXrwmata + 1, " περίοδοι")


    # Αποθηκεύεται σε ένα αρχείο με τίτλο το πρόβλημα και την βαθμολογία και την κατάληξη sol
    f = open(filename + str(telikhBathmologia) + ".sol", "w")
    for mathima in d:
        f.write(str(mathima) + "\t" + str(d[mathima]) + "\n")
    f.close()

# Μενόυ επιλογής προβήματος  απο τον χρήστη
if __name__ == '__main__':
    # Εισαγωγη προβλημάτων σε έναν πίνακα
    stus =["car-f-92.stu","car-s-91.stu","ear-f-83.stu","hec-s-92.stu","kfu-s-93.stu","lse-f-91.stu","pur-s-93.stu","rye-s-93.stu","sta-f-83.stu","tre-s-92.stu","uta-s-92.stu","ute-s-92.stu","yor-f-83.stu"]
    while True:
        print("Δώσε αριθμό πίνακα:")
        # Έλεγχος επιλογής απο τον χρήστης για την φόρτοση του προβλήματος
        # Mε επιλογή απο το 1 εώς το 14 για επιλογή ενός προβλήματος ή με 0 να τα εκτελέσει όλα τα προβλήματα μαζι
        for i in range(1,len(stus)+1):
            print(i, ". ", stus[i-1])
        print("0. Επιλογή όλων")
        pinakas= input()
        pinakas = int(pinakas)
        if pinakas in range(1,len(stus)+1):
            readSTU(stus[pinakas-1])
        elif pinakas == 0:
            for i in range(0,len(stus)):
                readSTU(stus[i])