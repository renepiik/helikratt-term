# Helikratt-term

## Mida see teeb

Kratt küsib sinult küsimuse, mille saadab OpenAI gpt-3.5-turbo mudelile vastamiseks.
Saadud vastus suunatakse edasi TartuNLP kõnesünteesimudelile, kus loeb Mari vastuse ilmekalt .wav faili ja saadab selle sulle tagasi.
Viimasena saadud vastus salvestatakse nii teksti kui ka helifaili kujul repo kausta (vastavalt `vastus.txt` ja `vastus.wav`).

## Kuidas töötab

Krati tööks on vajalik enda registreerimine OpenAI lehel maksvaks kasutajaks ja oma API võtme lisamine `.env` faili.
Õnneks ei maksa antud boti tehtud päringud eriti palju: koodi kirjutamise, testimise ja selle teistele näitamise peale kulus mul kokku 2 dollari senti.

Koodi testisin Fedora 37 peal. 
Installitud peab olema lisaks Python 3-le ka VLC (audio mängimiseks) ja paar paketti.
Teoorias võiks kood töötada ka Windowsil, kui kõik eeldused on täidetud, kuid eraldi ma seda üle kontrollinud pole.
Kui helifaili automaatse mängimisega tekib probleeme, siis võib vastava osa koodist lihtsalt välja kommenteerida.
Fail ise on juba kaustas olemas ja seda saab ka mistahes muu programmiga järele kuulata.
