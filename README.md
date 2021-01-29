# **Αλγόριθμοι και Πολυπλοκότητα**
## **"Χρονοπρογραμματισμός Εξετάσεων Πανεπιστημίου"**
## Του Μεταπτυχιακού προγράμματος Πληροφορικής και Δικτύων του Πανεπιστημίου Ιωαννίων 
## Μαυρογιώργος Δημήτριος ΑΜ00104


## Εισαγωγή
Είναι μια εργασία που ασχολείται με τον Χρονοπρογραμματισμό  Εξετάσεων Πανεπιστημίου.
Πρόκειται για την δημιουργία προγράμματος εξετάσεων σε Πανεπιστήμια, 
από μια απλοποιημένη μορφή αυτού του προβλήματος έχει προταθεί 
από τους Carter, Laporte και Lee το 1996 οι οποίοι διέθεσαν στο κοινό 13 προβλήματα 
χρονοπρογραμματισμού εξετάσεων  τα οποία στην συνέχεια χρησιμοποιήθηκαν από πολλά Πανεπιστήμια 
ανά τον κόσμο για να βρεθεί η βέλτιστη λύση στο πρόβλημα Χρονοπρογραμματισμού Εξετάσεων Πανεπιστημίων.

## Περιγραφή προβλήματος

Το πρόβλημα αφορά εξετάσεις, σπουδαστές και συνεχόμενες περιόδους σε κάθε μια από
τις οποίες μπορούν να διεξαχθούν μια ή περισσότερες εξετάσεις. Κάθε εξέταση διαθέτει μια 
λίστα από σπουδαστές και κάθε σπουδαστής μπορεί να είναι εγγεγραμμένος σε μια ή 
περισσότερες εξετάσεις. Η λύση του προβλήματος συνίσταται στην ανάθεση εξετάσεων σε περιόδους έτσι
ώστε να μην υπάρχουν συγκρούσεις, δηλαδή να μην υπάρχουν σπουδαστές που θα έπρεπε να
συμμετάσχουν σε εξετάσεις σε περισσότερα του ενός μαθήματα στην ίδια περίοδο. Καθώς είναι
ενδεχόμενο να υπάρχουν πολλά εναλλακτικά προγράμματα που ικανοποιούν τον ανωτέρω 
περιορισμό, προτιμότερο θεωρείται εκείνο το πρόγραμμα που διαθέτει επαρκή διαστήματα 
προετοιμασίας ανάμεσα σε διαδοχικές εξετάσεις για όλους τους φοιτητές συνολικά. Ειδικότερα,
ορίζονται τιμές ποινής που είναι 16, 8, 4, 2 ή 1 σε κάθε περίπτωση που ένας φοιτητής συμμετέχει
σε δύο εξετάσεις που απέχουν 1, 2, 3, 4 ή 5 περιόδους αντίστοιχα. Η συνολική ποινή για όλους
τους φοιτητές, διαιρεμένη με το πλήθος των φοιτητών αποτελεί το κόστος της λύσης.

## Τεχνολογίες που χρησιμοποιήθηκαν 
Για να  δημιουργηθεί η λύση για το  Πρόβλημα Χρονοπρογραμματισμού  Εξετάσεων Πανεπιστημίου
δημιουργήθηκε κώδικας στην Python και η βιβλιοθήκη NetworkX.

## Οδηγίες εγκατάστασης-εκτέλεσης για τον κώδικα που εχει υλοποιήθει στην Python 

* Download γλώσσα προγραμματισμού Python την τελευταία έκδοση: 
https://www.python.org/downloads/
* Ενδικτηκό πρόγραμμα για την εκτλέση της Python:
https://www.jetbrains.com/pycharm/download/#section=windows
* Εγκατάσταση της βιβλιόθήκης NetworkX της Python
    1) Επιλογή Preferences> Project:<<όνομα Project>> 
    2) Εντοπισμοός συμβόλου <<+>> κατω αριστερά ή πάνω δεξιά στο παράθυρο που έχετε μπροστά σας
    3) Αναζήτηση της βιβλιόθήκης NetworkX  και Install Package
* Download  το συμπιεσμένο αρχείο με κατάληξη .zip και αποσυμπίεση σε έναν φάκελο 
* Άνοιγμα του προγράμματος που εκτελείται η Python και επιλογή του φακέλου που εχει τα αρχεία 
* Επιλογή αρχείου με την κατάληξη .py και Run
* Άνοιγμα του terminal  που εκτελείται ο κώδικας 


