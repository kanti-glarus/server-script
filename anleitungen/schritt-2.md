# Schritt 2: Einfacher Python-Server

Mihilfe der Python Library `http.server` kann ein einfacher Python Server erstellt werden.

    import http.server

    webServer = HTTPServer(('localhost', 8000), EinfacherServer)

Ein einfaches Beispiel findet sich bei den [python scripts](../python): [simple-server.py](../python/simple-server.py).

## Aufgabe

Fangen sie verschiedene Pfade ab und ändern sie beispielsweise den Statuscode von `200` zu `400`, sobald eine Datei nicht existiert.

    if self.path == '/favicon.ico':
        self.send_response(400)

Erarbeiten sie den Fall, dass ihr Server bei fehlenden Dateien den korrekten Status `400 Bad Request` oder `404 Not Found` zurückschickt.

Mehr Informationen zu den HTTP-Status-Codes findet sich beispielsweise hier: [developer.mozilla.org/de/docs/Web/HTTP/Status/404](https://developer.mozilla.org/de/docs/Web/HTTP/Status/404)

## Zugriff

Mit der IP-Adresse vom `Raspberry Pi` kann von Geräten aus dem gleichen Netzwerk auf den Webserver zugegriffen werden:

    http://192.168.1.xx:8080/favicon.ico

Die Ausgabe im Browser müsste nun den Status 400 zurückmelden.

[Schritt 3: HTTP-Header](schritt-3.md)