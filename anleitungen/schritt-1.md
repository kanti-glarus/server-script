# Schritt 1: Einfachster Python-Server

Auf einem `Raspberry Pi` kann ein simpler Python-Server mit dem folgenden Befehl gestartet werden:

    python3 -m http.server

## Zugriff

Mit der IP-Adresse vom `Raspberry Pi` kann von Geräten aus dem gleichen Netzwerk auf den Webserver zugegriffen werden:

    http://192.168.1.xx:8000

Die Ausgabe im Browser müsste nun ein Verzeichnis aller Dateien auf dem Raspberry Pi sein.

[Schritt 2: Einfacher Python Server](schritt-2.md)