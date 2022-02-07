---
hide:
  - navigation
---
# {{ cookiecutter.project_name }}
---
Baserad på [DIGG förtroendemodell](https://www.digg.se/publicerat/publikationer/2020/testa-ny-teknik-for-automatisering-inom-offentlig-forvaltning)
## Översiktlig sammanfattning
En sammanfattning av innehållet i övriga kortet. Ska gå att förstå av en "okunnig".

|Typ                   | Process, Modell eller Algoritm |
|--------------------- | ------------------------------ |
|In                    |                                |
|Ut                    |                                |
|Ingår i               |                                |
|Arkitektur            |                                |
|Dokument Version      |                                |
|Algoritm Version      |                                |

### Tänkt användning
Varför har det utvecklats? Vad har målen varit? Användningsområden?

### Prestanda
Hur väl fungerar det? (beskrivet i enkla termer)

### Begränsningar
När fungerar det mindre bra (ska innehålla konkreta exempel, bilder om möjligt), antingen p.g.a. avsiktliga avgränsningar eller oavsiktliga biverkningar.

### Processöversikt
Gäller enbart för beskrivning av Processen.

En enkel processkiss med indata, underprocesser/modeller/algoritmer, och utdata

## Modellinformation
Person eller organisation som utvecklat processen/modell/algoritmen. När processen/modellen/algoritmen utvecklats och dess version.

### Arkitektur
Gäller enbart för modeller & algoritmer.

Grundläggande om modellens/algoritmens arkitektur. Vid en välkänd modell/algoritm kan det räcka att ange dess namn och konfiguration samt länk till
artikel med mer information, annars behövs även en kort sammanfattning. M: Ska ge personer med kunskap om AI förståelse för begränsningar och betänkanden
inbyggda i själva modellarkitekturen.

### Teknisk plattform
Gäller enbart för processer.

Beskriv i ord eller bild vald teknisk plattform, ta särskilt hänseende till och uppmärksamma ev. molnlösningar

### Träning
Vilka parametrar som använts vid träning, t.ex. antal epoker, batchstorlek, lossfunktion, learning rate, etc.

### Begränsningar
Mer ingående information om begränsningar och avgränsningar.

### Implementationsdetaljer
T.ex. användning av ramverk, programvara, m.m.

### Artiklar eller andra resurser för mer information
Länkar till externa resurser, t.ex. artikel där processen/modellen/algoritmen introduceras, eller andra som haft liknande användning eller som av annan
anledning är relevant.

### Licens
Hur är processen/modellen/algoritmen licenserad? Vad krävs för att få använda den?

### Kontaktperson
Vem ska man kontakta för mer information

### Avsedd användning
Primära avsedda användningar och användare.

### Användningsfall utanför tillämpningsområdet
Alternativa tänkbara eller faktiska användningsfall, eventuellt med specifika
betänkanden eller kommentarer.

## Faktorer
### Relevanta faktorer
De faktorer som kan påverka processen/modellen/algoritmen. Det kan handla om 3 huvudsakliga typer av faktorer: Olika grupper av objekt, t.ex. ålder och kön
i en modell för ansiktsigenkänning, byggnadsändamål och byggnadsstorlek i en modell för att hitta byggnader eller olika längd på meningar i en NLP-modell.
Påverkan av olika instrument, t.ex. kameramodell och bearbetningsmetoder. Miljön, t.ex. belysning, plats, m.m.

### Utvärderingsfaktorer
De faktorer (av dem som nämns i 4.1.) som har utvärderats. Varför har de utvärderats eller inte (t.ex. för att det inte fanns tillgängligt eller ansetts vara
relevant)?

## Utvärdering av modellen
Kort (1-2meningar) beskrivning om vilka mått som använts.

### Resultat
Processens/modellens/algoritmens prestanda beskriven med siffror och grafer för helheten.

### Användarresultat
Gäller enbart för processer.

Resultat från användning i verkligheten. Kan vara under en testperiod eller i produktion (vilket det är ska anges). Ska ge en indikation om processens
prestanda, exempel på mätvärden: Användarbetyg, antal omprövningar och andel som ändrade resultatet, stickprovskontroller

### Unitära resultat
Vad är modellens prestanda för de enskilda faktorerna (t.ex. olika kön, byggnadsändamål eller meningslängder) beskriven med siffror och grafer för
helheten?

### Trösklar och jämförelser
Trösklar för när processen/modellen/algoritmen (enligt oss) är tillämpbar (t.ex. ett krav på precision/recall från "högre instans"), jämförelser med andra
processer/modeller/algoritmer och metoder, m.m.

### Utvärderingsmetod
Hur har utvärderingsvärdena (t.ex. precision/recall) räknats fram? Kan hänvisa till extern information om oförändrade standardmetoder används och en egen
beskrivning inte tillför något.

## Data
### Utvärderingsdata
Information om det data som använts för att genomföra utvärderingen (källa, utbredning, förbehandling, m.m.). uppmärksamma särskilt om det finns
personuppgifter eller skyddsvärd information i utvärderingsdata.

### Träningsdata
Information om det data som använts för att träna modellen (källa, utbredning, förbehandling, m.m.). uppmärksamma särskilt om det finns personuppgifter eller
skyddsvärd information i utvärderingsdata.

## Övervakning, loggning och profilering
Beskriv om systemet genererar loggar samt någon form av övervakning. Ta särskild hänsyn till mänsklig interaktion med dessa loggar eller övervakning

## Etiska aspekter
EU-kommissionens Etiska riktlinjer för tillförlitlig AI ställer upp tre komponenter i sitt ramverk för tillförlitlig AI: Inkluderar, men är inte begränsat
till: Laglig AI, Etisk AI och Robust AI. Etisk AI omfattar i sin tur fyra principer:
- Respekt för människans autonomi
- Förebyggande av skada
- Rättvisa
- Förklarbarhet.
Dessa principer finns förklarade i detalj i riktlinjerna. De kan med fördel vara vägledande för den redovisning som görs under denna rubrik.

## Juridiska aspekter
Krav som ställs på processen/modellen/algoritmen utifrån gällande lagar och förordningar.Kan ha delvis överlapp med Etiska aspekter, t.ex. gällande
personuppgifter. Uppdelningen som gäller är att kapitlet Etiska ställningstaganden ska hantera den etiska sidan ("bör man") och Juridiska
aspekterska hantera den juridiska sidan ("får man").

### Integritetslagstiftning
Uppmärksamma särskilt den data som används och då i förhållande till t.ex. GDPR

### Sekretess eller annan skyddslagstiftning
Överväg vilken information gällande sekretess som är relevant att uppmärksamma

### Omprövning och överklagande
Enbart för processer.
Kan man få beslutet omprövat (av en mänsklig handläggare) eller överklagat? Hur?

### Tillsyn
Finns det någon som har tillsyn? Externt eller internt? Myndighet, företag eller annan?

## Betänkanden och rekommendationer
Finns det några ytterligare aspekter att ta hänsyn till, som inte hanterats i någon annan rubrik? Indikerar t.ex. resultaten på att det behövs mer tester? Fanns det
några faktorer/grupper som inte täckts av det använda data? Finns det några andra betänkanden eller rekommendationer som en användare eller vidareutvecklare av
modellen bör tänka på?
