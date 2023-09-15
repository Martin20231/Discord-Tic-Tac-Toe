# Discord Tic-Tac-Toe Bot

Dies ist ein einfacher Discord-Bot, mit dem du Tic-Tac-Toe (Drei gewinnt) mit Freunden auf deinem Discord-Server spielen kannst.

## Funktionen

- Starte ein neues Tic-Tac-Toe-Spiel auf deinem Discord-Server.
- Tritt dem Spiel bei und mache nacheinander Züge.
- Der Bot überprüft, ob es einen Gewinner gibt, und gibt das Ergebnis des Spiels bekannt.

## Installation

Bevor du diesen Bot ausführen kannst, musst du die folgenden Abhängigkeiten installieren:

- [Python 3](https://www.python.org/downloads/): Stelle sicher, dass du Python 3 installiert hast.

Als nächstes musst du die erforderlichen Python-Pakete installieren. Das kannst du mit `pip`, dem Python-Paketmanager, erledigen.

Öffne deine Eingabeaufforderung oder dein Terminal und navigiere zum Verzeichnis, in dem sich dein Bot-Skript befindet. Führe dann den folgenden Befehl aus, um die notwendigen Pakete zu installieren:

```bash
pip install discord.py

## Konfiguration
Bevor du den Bot ausführst, musst du einige Einstellungen im Skript vornehmen:

Setze den Token deines Bots:

Ersetze 'DEIN_BOT_TOKEN' im Skript durch den tatsächlichen Token deines Bots.

Setze das Präfix deines Bots:

Du kannst das prefix-Variable auf dein bevorzugtes Befehlspräfix ändern (z.B. '!', '?', '/', usw.).

Setze die Zielkanal-ID:

In der on_message-Funktion ersetzt du 'DEINE_CHANNEL_ID' durch die tatsächliche ID des Kanals, in dem du möchtest, dass der Bot auf Befehle reagiert.

# Ausführen des Bots
Nachdem du den Bot konfiguriert und die erforderlichen Pakete installiert hast, kannst du den Bot ausführen, indem du das Python-Skript ausführst. In deinem Terminal oder der Eingabeaufforderung navigiere zum Verzeichnis mit deinem Skript und führe aus:

- python bot_script.py

Der Bot sollte nun auf deinem Discord-Server aktiv sein.


# Verwendung
Um ein neues Spiel zu starten, verwende den !neu-Befehl:

Um einen Zug zu machen, verwende den !zug-Befehl gefolgt von der Position, an der du dein Zeichen platzieren möchtest (1-9):

Vergiss nicht, den Bot auf deinen Discord-Server einzuladen und sicherzustellen, dass er die erforderlichen Berechtigungen zum Lesen von Nachrichten, Senden von Nachrichten und Verwalten von Nachrichten in den gewünschten Kanälen hat.

Viel Spaß beim Spielen von Tic-Tac-Toe mit deinen Freunden auf Discord!
