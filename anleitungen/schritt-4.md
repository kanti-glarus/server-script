# Schritt 4: GET und POST Parameter

Mit Hilfe von `GET` und `POST` Parametern können vom Browser Daten an den Server geschickt und dort verarbeitet werden.

GET-Parameter:

    https://192.168.1.xx:8080?name=kanti-glarus

    todo: POST-Parameter einfügen

Ein fertiges Beispiel findet sich bei den [python scripts](../python): [get-post-server.py](../python/get-post-server.py).

## Aufgabe: GET-Parameter

GET-Parameter können direkt über die URL ausgelesen werden

    from urllib.parse import urlparse

    def get_parameters(self):
        parameter_string = urlparse(self.path).query
        parameters = dict(qc.split("=") for qc in parameter_string.split("&"))
        return parameters

Achtung: der Vergleich `if self.path == '/get':` funktioniert nicht mehr einfach so, da die GET-Parameter ein Teil vom Pfad sind. Der folgende Python-Befehl
gibt den aktuellen Pfad aus - ohne die GET-Parameter.

    urlparse(self.path).path

## Aufgabe: POST-Parameter

POST-Parameter werden als Teil vom HTTP-Header mitgeschickt. Sie sind nicht in der URL sichtbar. Ausgelesen werden können sie wie folgt:

    def post_parameters(self):
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        return form

Normale Anfragen via Browser sind immer via `GET`-Methode. Die `POST`-Methode kann zum Beispiel mit Formularen explizit aufgerufen werden.
Dazu hier ein Beispiel: [w3schools.com/tags/tryit.asp?filename=tryhtml_form_method_post](https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_form_method_post)

## Zugriff

Mit der IP-Adresse vom `Raspberry Pi` kann von Geräten aus dem gleichen Netzwerk auf den Webserver zugegriffen werden:

    http://192.168.1.xx:8080/get?name=kanti-glarus
    http://192.168.1.xx:8080/post

Auf dem Server können die übermittelten Daten verarbeitet werden.
