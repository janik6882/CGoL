## Du willst Mitarbeiten?

1. Schick mir deinen GitHub nutzernamen, sonst wird das hochladen nicht funktionieren.
2. Du wirst eine E-Mail bekommen, in der du über die Einladung benachrichtigt wirst.

## Ordner herunterladen (clonen)

1. bei dem grünen knopf "code" auf github.com/janik6882/cgol den Link kopieren
2. in dem ordner auf eurem PC wo die datein hin sollen, eine Eingabeaufforderung öffnen
3. in der Eingabeaufforderung git clone und die kopierte url einfügen
4. Fertig


## Eine auf eurem PC veränderte Datei hochladen (zum ersten mal)

1. git add .
(alternativ statt dem Punkt einen Datei namen, der Punkt würde alle datein im Ordner hochladen)
2. git config --global user.email "eure@email.endung"
3. git config --global user.name "euer github nutzername"
4. git commit -m "irgendeinen sinnvollen Kommentar, der moeglichst kurz ist"
5. git push (beim ersten mal wird sich ein Fenster öffnen, welches euch auffordert euch in eurem Browser anzumelden. Dies machen und danach zur Eingabeaufforderung zurück.)
Fertig.


## Eine auf eurem PC veränderte Datei hochladen (wenn ihr es bereits mindestens einmal gemacht habt)

1. git add . (statt . kann hier eine spezielle Datei hin)
2. git commit -m "sinnvoller Kommentar hier"
3. git push


## Ordner auf den neusten Stand mit der Cloud bringen

1. git pull
Das war's


## Eine neue Funktion hinzufügen:
Für jede neue Funktion die ihr einfügt, erstellt ihr bitte einen neuen sogenannten Branch.

1. git branch sinnvoller_name
2. git checkout sinnvoller_name

### Wenn ihr hier einen push durchführen wollt, wird euch git auffordern etwas einzugeben. Entweder ihr kopiert das oder ihr nehmt das, was ich euch hinschreibe:
git push --set-upstream origin neuer_name

## Eine neue Funktion implementieren bzw. in den branch main übernehmen:

Wir werden noch besprechen, wie genau wir das machen werden aber bitte macht kein Merge von eurem branch in den main branch, das könnte sehr aufwändig werden.
