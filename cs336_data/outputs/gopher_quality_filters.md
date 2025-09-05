# Problem (gopher_quality_filters): 3 points

Main code file: [gopher_quality_filters.py](../gopher_quality_filters.py)

## Question (a)

Implement (at least) the subset of the Gopher quality filters as described above. For tokenizing
text into words, you might find the NLTK package useful (specifically nltk.word_tokenize),
though you’re not required to use it.
Deliverable: A function that takes a string as its only argument and returns a boolean indi-
cating whether the text passes the Gopher quality filters. Implement the adapter
[run_gopher_quality_filter]. Then, make sure your filters pass the tests in uv run pytest
-k test_gopher.

**Answer:** Passed

How to run: 
```bash
uv run pytest -k test_gopher
```

## Question (b)

Run your rule-based quality filter on text extracted from the WARC files (via your previously-
implemented text extraction function). Look through 20 random examples and compare the filter
predictions to your own judgment. Comment on any cases where the quality filters differ from
your judgments.
Deliverable: A 2-5 sentence response.

**Answer:** 8/50 examples were classified as low quality.

Quality filter differ from my judgement: 

### Example 1
```
LABEL: True
text: Greenbets – Seu principal destino de apostas esportivas e cassino online

Captains of the Coast

Captains of the Coast

Home » Captains of the Coast
Rate Game
(0 Votes)
Captains of the Coast Jogar de Verdade Powered by Slots Launch

Play Captains of the Coast for real money

Captains of the Coast Jogar de Verdade

Having issues with Captains of the Coast ?

Try Our Featured Games
Release the Kraken Megaways
Try Demo
Vampy Party
Try Demo
Barbarossa Revenge
Try Demo

Deixe um comentário Cancelar resposta

O seu endereço de e-mail não será publicado. Campos obrigatórios são marcados com *

Recent Posts

  • Hello world!

Recent Comments

  1. A WordPress Commenter em Hello world!
© Copyright 2024 | Greenbets
Greenbets – Seu principal destino de apostas esportivas e cassino online
© Copyright 2024 | Greenbets
```

### Example 2

```
LABEL: True
text:   • Home
  • what's PoS
  • for organizers
  • for chairpersons
  • for authors
  • for readers
  • staff
Volume 481 - 9th Symposium on Prospects in the Physics of Discrete Symmetries (DISCRETE2024) - Flavour and CP violation 2
The n2EDM experiment, a high-sensitivity search for the neutron electric dipole moment
V. Kletzl
Full text: Not available
How to cite

Metadata are provided both in article format (very similar to INSPIRE) as this helps creating very compact bibliographies which can be beneficial to authors and readers, and in proceeding format which is more detailed and complete.

Open Access
Creative Commons LicenseCopyright owned by the author(s) under the term of the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.

Communicate with the PoS editorial office | Cookie policy | Privacy policy

Published by Sissa Medialab srl Partita IVA: IT01097780322
```

### Example 3

```
ABEL: True
text:  Zum Inhalt springen
cd kopierer Deutschland Logo
  • ADR cdkopierer
  • EPSON cdkopierer
  • Rimage cdkopierer
  • Primera cdkopierer
  • ADR cdkopierer
  • EPSON cdkopierer
  • Rimage cdkopierer
  • Primera cdkopierer
cd-kopierer.deRPM-ADMIN2020-08-11T00:25:05+02:00

Wegen Wartungsarbeiten zur Zeit offline! Besuchen Sie cd-kopierer.com

MENÜ

  • cd-kopierer.de
  • Datenschutzerklärung
  • Impressum

RSS ADR News

  • Der BOTLR – Die nächste Generation der Flaschenetikettierung
  • Messetermine 2025 – ADR AG auf drei internationalen Messen
  • ADR in Hamburg beim Epson Launch Event
  • Wieslochs Bürgermeister besuchte ADR

Get Social

Contact Info

Ludwig Wagner Str. 19 - D-69168 Wiesloch

Telefon: +49 (0)6222-9388-0

E-Mail: info@adr-ag.com

Website: https://adr-ag.de

CD DVD Blu-ray

CD Rohlinge

DVD Rohlinge

Blu-ray Rohlinge

Mini Disc CD/DVD-R (8cm)

CD / DVD Visitenkarten Rohlinge

M-Disc Blu-ray Rohlinge

CD SlimCases

CD Jewel Cases

DVD Boxen

Shell Boxen für Disc Speichermedien

CD / DVD / BD Papierstecktaschen

Cake-Boxen für Disc Speichermedien

Polybags für Disk & Mini-Disk-Medien

Flip & Grip Case Disk Verpackungen

CD / DVD / BD Disk Versandtaschen

CD / DVD /BD Disk Transport, Aufbewahrung

ADR KOPIERER

usb-stick kopierer

flashcard kopierer

sd-karten kopierer

cf-karten kopierer

festplattenkopierer

cd-kopierer

cd-kopierturm

dvd-kopierturm

cd-kopiertower

dvd-kopiertower

blu-ray kopierroboter

dvd drucker

JMV Packaging Produkte

Verpacker für CDs

Etikettierer für CDs

Cellophanierer für CDs

automatisch etikettieren

flaschen etikettierer

beutel etikettierer

karton etikettierer

jmv-packaging.com

ADR INTERNETSHOP

Shop für CD-Kopierer uvm.
www.adr-shop.com

Im ADR-Vertrieb

EPSON Etikettendrucker

EPSON Colorworks Drucker

ureach.eu

dicom-disc.de

Deutscher Hersteller von CD-Kopierern | ADR AG

Deutscher Hersteller von CD-Kopierern | ADR AG

Made in Germany

Made in Germany

Copyright 2019 ADR AG | All Rights Reserved | Powered by AGENTUR RPM!
Page load link
Nach oben
--------------------------------
--------------------------------
LABEL: True
text: Greenbets – Seu principal destino de apostas esportivas e cassino online

Captains of the Coast

Captains of the Coast

Home » Captains of the Coast
Rate Game
(0 Votes)
Captains of the Coast Jogar de Verdade Powered by Slots Launch

Play Captains of the Coast for real money

Captains of the Coast Jogar de Verdade

Having issues with Captains of the Coast ?

Try Our Featured Games
Release the Kraken Megaways
Try Demo
Vampy Party
Try Demo
Barbarossa Revenge
Try Demo

Deixe um comentário Cancelar resposta

O seu endereço de e-mail não será publicado. Campos obrigatórios são marcados com *

Recent Posts

  • Hello world!

Recent Comments

  1. A WordPress Commenter em Hello world!
© Copyright 2024 | Greenbets
Greenbets – Seu principal destino de apostas esportivas e cassino online
© Copyright 2024 | Greenbets
```