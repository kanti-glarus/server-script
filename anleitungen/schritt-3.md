# Schritt 3: HTTP Header anpassen

Je nach Abfrage können wir andere HTTP-Antworten an den Browser zurücksenden. Wir erarbeiten nun 2 Beispiele, wie wir
JSON-Requests oder Bild-Requests verarbeiten können.


    if self.path == '/data.json':
        self.handle_json_request()

    elif self.path == '/image.png':
        self.handle_image_request()

Ein fertiges Beispiel findet sich bei den [python scripts](../python): [image-json-server.py](../python/image-json-server.py).

## Aufgabe: JSON

JSON-Dateien können als JSON-Output zurückgeschickt werden. So erkennt der Browser, dass hier Daten im JSON-Format ausgegeben werden können.

    self.send_header("Content-type", "application/json")

Daten können als Daten-Objekt (`dict`) verarbeitet und zurückgeschickt werden:

    self.wfile.write(json.dumps(data).encode('utf-8'))

## Aufgabe: Bild

Bilder werden nicht als Datenobjekt sondern als Byte-Abfolge zurückgeschickt. Dazu muss ein Bild zuerst in Python korrekt eingelesen werden:

    def load_binary(self, filename):
        with open(filename, 'rb') as file_handle:
            return file_handle.read()

Das Bild kann nun auf Abruf eingelesen werden und zurückgeschickt werden:

    file_read = self.load_binary('../images/flag_glarus.png')
    self.wfile.write(file_read)

Erarbeiten sie die beiden Fälle *Bild* und *JSON*, so dass ihr Python-Server beide Formate ausgeben kann.

## Zugriff

Mit der IP-Adresse vom `Raspberry Pi` kann von Geräten aus dem gleichen Netzwerk auf den Webserver zugegriffen werden:

    http://192.168.1.xx:8080/image
    http://192.168.1.xx:8080/data

Die Ausgabe im Browser müsste nun entweder ein Bild oder Daten im JSON-Format sein.
