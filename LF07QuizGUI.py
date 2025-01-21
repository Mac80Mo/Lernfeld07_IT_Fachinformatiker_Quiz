import tkinter as tk
from tkinter import messagebox
import random

# Beispiel-Fragenpool
fragen_pool = [
{"frage": "Generationenwechsel in der Technisierung:\nCyber-physische Systeme (IoT, Netzwerke, Smart Factory, ab ca. 2017)?", "antworten": ["Generation 3.0", "Generation 4.0"], "richtige_antwort": "Generation 4.0"},
    {"frage": "Generationenwechsel in der Technisierung:\nAutomatisierung (Elektronik, E-Steuerung, IT-Systeme, ab ca. 1970)?", "antworten": ["Generation 3.0", "Generation 4.0"], "richtige_antwort": "Generation 3.0"},
    {"frage": "Ein Verbund aus informatischen und softwaretechnischen Komponenten mit mechanischen\nwie auch elektrischen Teilen, die mit IT-Systemen vernetzt kommunizieren?", "antworten": ["CPS", "CPPC"], "richtige_antwort": "CPS"},
    {"frage": "Entsprechende cyber-physische Systeme, die im Industriellen Umfeld in modernen Produktionsmaschinen\nund -anlagen zum Einsatz kommen?", "antworten": ["CPS", "CPPC"], "richtige_antwort": "CPPC"},
    {"frage": "Ein Sammelbegriff für die Unterschiedlichsten Technologien einer global vernetzten Infrastruktur,\ndie sowohl physische als auch virtuelle Objekte über das Internet verbindet?", "antworten": ["IoT", "IIoT"], "richtige_antwort": "IoT"},
    {"frage": "Es beschreibt Industrielle Anwendungen im Internet of Things.\nHierbei steht besonders die Vernetzung mit Maschinen und Anlagen mittels intelligenter Sensorik im Vordergrund?", "antworten": ["IoT", "IIoT"], "richtige_antwort": "IIoT"},
    {"frage": "Es bezeichnet eine sich selbst organisierende und optimierende Produktionsumgebung,\nin der mittels cyber-physischen Systemen Maschinen und Anlagen miteinander vernetzt sind?", "antworten": ["Smart Factory", "Smart Home"], "richtige_antwort": "Smart Factory"},
    {"frage": "Der Oberbegriff für den Einsatz von cyber-physischen Systemen in Wohn- und Bürogebäuden\nzur Erhöhung der Wohn- und Lebensqualität und zum intelligenten Energiemanagement?", "antworten": ["Smart Factory", "Smart Home"], "richtige_antwort": "Smart Home"},
    {"frage": "Energieversorgung, Sicherheit, Haushaltsgeräte und Komfort?", "antworten": ["Smart Factory", "Smart Home"], "richtige_antwort": "Smart Home"},
    {"frage": "Produktionsplanung, Produktionssteuerung, Vorhersage und Analyse?", "antworten": ["Smart Factory", "Smart Home"], "richtige_antwort": "Smart Factory"},
    {"frage": "Einsatz von cyber-physischen Systemen:\nEffizienzsteigerung, Erhöhung der Flexibilität, Entlastung und Informationstechnische Unterstützung, Wettbewerbsvorteile?", "antworten": ["Chancen", "Risiko"], "richtige_antwort": "Chancen"},
    {"frage": "Einsatz von cyber-physischen Systemen:\nErhöhte Komplexität, Erheblicher Veränderungsprozess, Datensicherheit und hohe Anforderungen an die IT-Kompetenz?", "antworten": ["Chancen", "Risiko"], "richtige_antwort": "Risiko"},
    {"frage": "Ein cyber-physisches System besteht aus mechanischen, elektrischen und informationstechnischen Komponenten.\nEine Steuerung ist über das Internet in Echtzeit möglich. Kann Daten austauschen, kontrollieren und gesteuert werden.\nEs süielt in der Industrie 4.0 eine wichtige Rolle.", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Ein cyber-physisches System besteht hauptsächlich aus Prozessoren, Sensorik, Kommunikation und Aktorik um\nmit seiner Umwelt zu kommunizieren?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Cyber-physische Systeme können ??? (antriebstechnische Baueinheiten wie Motoren, Ventile oder Zylinder) besitzen?", "antworten": ["Sensorik", "Aktorik"], "richtige_antwort": "Aktorik"},
    {"frage": "Einplatinencomputer (SBC)?", "antworten": ["Raspberry Pi", "Arduino"], "richtige_antwort": "Raspberry Pi"},
    {"frage": "Mikrocontroller (MCU)?", "antworten": ["Raspberry Pi", "Arduino"], "richtige_antwort": "Arduino"},
    {"frage": "Es handelt sich bei einem ??? um einen voll funktionsfähigen Computer, der alle wesentlichen Komponenten\nwie Prozessor und Arbeitsspeicher auf einer Platine vereint. Zusätzlich kann der ??? Aus- und Eingabe-Schnittstellen\nbesitzen, um Monitor, Tastatur, Maus sowie weitere Sensoren und Aktoren anzuschließen?", "antworten": ["SBC", "MCU"], "richtige_antwort": "SBC"},
    {"frage": "Ein ??? ist ein Chip, in dem neben dem Prozessor oftmals auch der Arbeitsspeicher integriert ist.\nIm Chip arbeitet ein einzelnes Programm, das zyklisch ausgeführt wird. Eine solche Einheit eignet sich sehr gut zur Automatisierung\nvon sich wiederholenden Aufgaben?", "antworten": ["SBC", "MCU"], "richtige_antwort": "MCU"},
    {"frage": "Sie ermöglichen es dem System, physische Aktionen auszuführen?", "antworten": ["Sensoren", "Aktoren"], "richtige_antwort": "Aktoren"},
    {"frage": "Sie können physikalische Parameter wie Temperatur, Druck, Geschwindigkeit und Position erfassen?", "antworten": ["Aktoren", "Sensoren"], "richtige_antwort": "Sensoren"},
    {"frage": "Benutzerinteraktionen in einem ??? erfolgen in der Regel über mobile Apps oder Sprachsteuerung,\num den Wohnkomfort zu steigern?", "antworten": ["Smart Home", "Smart Factory"], "richtige_antwort": "Smart Home"},
    {"frage": "in einer ??? ist Automatisierung und Maschinensteuerung wichtiger als die Benutzerinteraktion?", "antworten": ["Smart Home", "Smart Factory"], "richtige_antwort": "Smart Factory"},
    {"frage": "Sicherheitsanforderungen in ??? sind sehr komplex, da die Integrität der Produktionsdaten, der Schutz\nvor Cyberangriffen und die Gewährleistung der Arbeitssicherheit von größter Bedeutung sind?", "antworten": ["Smart Home", "Smart Factory"], "richtige_antwort": "Smart Factory"},
    {"frage": "Ein Ventil oder ein Motor?", "antworten": ["Aktor", "Sensor"], "richtige_antwort": "Aktor"},
    {"frage": "Ein Schalter oder ein Thermometer?", "antworten": ["Aktor", "Sensor"], "richtige_antwort": "Sensor"},
    {"frage": "... bezeichnet eine Überkompensation, durch den ein mögliches Einsparpotenzial durch das Verhalten der\nder Verbraucher wieder teilweise oder sogar komplett eliminiert wird?", "antworten": ["Rebound Effekt", "VUCA Effekt"], "richtige_antwort": "Rebound Effekt"},
    {"frage": "Das IIoT beschreibt industrielle Anwendungen im IoT. Hierbei steht besonders die Vernetzung mit Maschinen\nund Anlagen mittels intelligenter Sensoren im Vordergrund?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Indurstrie 4.0 löst weitestgehend die Fachbezeichnung ??? ab?", "antworten": ["CPS", "Industrie 3.0"], "richtige_antwort": "CPS"},
    {"frage": "Ein Ventil oder ein Motor?", "antworten": ["Aktor", "Sensor"], "richtige_antwort": "Aktor"},
    {"frage": "Bei einer intelligenten Produktion steuert sich die ???-Einheit selbst und kann\nanhand einzelner Prozessparamter Entscheidungen treffen?", "antworten": ["CPS", "CPPS"], "richtige_antwort": "CPPS"},
    {"frage": "So werden Softwarelösungen bezeichnet, mit denen Geschäftsprozesse wie etwa Beschaffung, Produktion,\nControlling und Vertrieb zentral gesteuert werden?", "antworten": ["ERP", "CRP"], "richtige_antwort": "ERP"},
    {"frage": "Es bezeichnet die weitgehend automatisierte Kommunikation zwischen Endgeräten, wie z.Bsp. Maschinen,\nAutomaten, Fahrzeugen und Messwerken?", "antworten": ["H2M", "M2M"], "richtige_antwort": "M2M"},
    {"frage": "Manufacturing Execution System (MES / Fertigungsmanagementsystem) steht für Produktionsleitsysteme,\ndie eine Produktionssteuerung und Produktionskontrolle in Echtzeit ermöglichen?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Es handelt sich um ein standardisiertes Modell, das beschreibt, wie unterschiedliche Netzwerkkomponenten\nmiteinander kommunizieren?", "antworten": ["ISO", "OSI"], "richtige_antwort": "OSI"},
    {"frage": "RAMI 4.0 ist ein dreidimensionales Strukturmodell, das alle Ebenen und Teilnehmer der Industrie 4.0 (CPS)\nerfassbar darstellt?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "In dieser Architektur werden Prozesse in überschaubare Pakete eingeteilt:\nSo gibt es eine Achse für die netzartige Hierarchiestruktur innerhalb einer modernen Fabrik,\neine Achse für den Aufbau der Architektur (Funktionen, Prozesse, Daten) und eine dritte Achse,\ndie den Produktlebenszyklus beschreibt?", "antworten": ["RFID", "RAMI 4.0"], "richtige_antwort": "RAMI 4.0"},
    {"frage": "Bei Radio Frequency Identification (RFID / Automatische Objektidentifizierung) handelt es sich um Chips,\ndie über ein elektromagnetisches Feld mit einem Lesegerät kommunizieren?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Ähnlich einem Barcode oder Magnetstreifen enthalten die Chips Informationen, die durch einen Scanner abgerufen\nwerden können. Welche Technik?", "antworten": ["WLAN", "RFID"], "richtige_antwort": "RFID"},
    {"frage": "Bei der Entwicklung welcher Produkte sind folgende Dinge zu beachten:\nDatenmenge & Datenübertragungsrate, für den geforderten Anwendungsfall, Energieeffizienz bzw. Energiebedarf des CPS,\ndie Relevanz einer Verzögerung der Datenübertragung?", "antworten": ["Aktor", "Sensor", "IoT"], "richtige_antwort": "IoT"},
    {"frage": "Gibt es z.Zt. einen einheitlichen Standard bei IoT-Geräten und deren verwendeten Protokollen?", "antworten": ["Ja", "Nein"], "richtige_antwort": "Nein"},
    {"frage": "MQTT ist weiter verbreitet als das in Deutschland übliche OPC UA?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "GSM / GPRS / EDGE(2G) / UMTS oder HSPA(3G) / LTE(4G) / 5G / LTE-M?", "antworten": ["Nahfeldkommunikation", "Mobilfunk", "LPWAN"], "richtige_antwort": "Mobilfunk"},
    {"frage": "RFID / NFC?", "antworten": ["Nahfeldkommunikation", "Mobilfunk", "LPWAN"], "richtige_antwort": "Nahfeldkommunikation"},
    {"frage": "LoRaWAN / NB-IoT / Sigfox / 4G LTE IoT / 5G IoT?", "antworten": ["Nahfeldkommunikation", "Mobilfunk", "LPWAN"], "richtige_antwort": "LPWAN"},
    {"frage": "Drahtlose Kommunikation mit geringer Reichweite: Wi-Fi / Bluetooth / BLE / ZigBee / Z-Wave?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Wofür steht die Abkürzung SBC?", "antworten": ["Micro-Controller-Unit", "Single-Board-Computer"], "richtige_antwort": "Single-Board-Computer"},
    {"frage": "Message Queue Telemetry Transport?", "antworten": ["MOTT", "MQTT"], "richtige_antwort": "MQTT"},
    {"frage": "Ein Kurznachrichtenprotokoll, das vorrangig für Verbindungen mit geringer Bandbreite in\nentlegenen Standorten verwendet wird?", "antworten": ["WLAN", "MQTT"], "richtige_antwort": "MQTT"},
    {"frage": "Das MQTT-Protokoll ist ein sehr schlankes Übertragungsprotokoll für die M2M Kommunikation,\ndas Datenpakete trotz hoher Verzügerung in Form von Nachrichten zwischen Geräten ermöglicht?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "MQTT nutzt ein Publisher-Subscriber-Muster (Daten veröffentlichen und abonnieren) und ist daher\nfür die einfache Kommunikation zwischen kleinen IoT-Geräten geeignet?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "MQTT besitzt keinen Sicherheitsmechanismus. Deshalb sollte es nicht unabhängig für die automatisierte\nSteuerung von Maschinen genutzt werden?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Falsch"},
    {"frage": "Sender (Temp.-Sensor) übermittelt seine Nachrichten an einen Broker.\nEmpfänger 'abonnieren' bestimmte Themen (Temperatur).\nBroker übermittelt an Empfänger Nachrichten zu den Themen.\nEine Nachricht kann somit von vielen Empfängern genutzt werden.", "antworten": ["Client-Server-(Broker)-Prinzip", "Machine 2 Machine"], "richtige_antwort": "Client-Server-(Broker)-Prinzip"},
    {"frage": "Was versteht man unter 'Retained Messages'?", "antworten": ["zurückgehaltene Nachricht", "dauerhafte Nachricht"], "richtige_antwort": "zurückgehaltene Nachricht"},
    {"frage": "Was versteht man unter 'Persistent Messages'?", "antworten": ["zurückgehaltene Nachricht", "dauerhafte Nachricht"], "richtige_antwort": "dauerhafte Nachricht"},
    {"frage": "Message Persistence => Beharrlichkeit einer Nachricht?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Eigenschaften von MQTT: Performance, Skalierbarkeit und Sicherheit?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Falsch"},
    {"frage": "Performance, Skalierbarkeit und Sicherheit sind Eigenschaften von?", "antworten": ["LGBQ", "MQTT", "MOTT"], "richtige_antwort": "MQTT"},
    {"frage": "Der automatisierte Informationsaustausch zwischen Maschinen, Anlagen, Automaten, Fahrzeugen und Containern?", "antworten": ["H2M", "B2B", "M2M"], "richtige_antwort": "M2M"},
    {"frage": "Open Platform Communications Unified Architecture ist ein Industriestandard für die Kommunikation\nzwischen Maschinen und Computersystemen?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Es handelt sich um einen offenen Schnittstellenstandard.\nDer Standard ist herstellerunabhängig und kann mit zahlreichen Entwicklungsumgebungen programmiert werden?", "antworten": ["OPC", "OPC UA"], "richtige_antwort": "OPC UA"},
    {"frage": "Industrie 4.0-Anforderungen, die der OPC UA Standard erfüllt:\n- Herstellerunabhängig, offen und frei von Mitgliedschaften\n- Skalierbar\n- Sicher\n- Serviceorientiert\n- Prüfbar (nachvollziehbar)", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Herstellerunabhängig, offen und frei von Mitgliedschaften, Skalierbar, Sicher, Serviceorientiert, Prüfbar (Nachvollziehabr)?", "antworten": ["OPC", "OPC UA", "MQTT"], "richtige_antwort": "OPC UA"},
    {"frage": "Die OPC-UA-Architektur:\n- TCP-basierendes Protokoll\n- Client-Server-Prinzip\n- Adressierung per IP oder Gerätenamen\n- Es werden stets die neusten Sicherheitstechnologien implementiert?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "GPIO, UART, I2C und SPI sind Schnittstellenarten von?", "antworten": ["MC(U)", "SBC", "MC(U) & SBC"], "richtige_antwort": "MC(U) & SBC"},
    {"frage": "Ein Microcontrollerboard ist ein vollständiger Computer?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Falsch"},
    {"frage": "Was betrifft die Nahfeldkommunikation?", "antworten": ["LTE (4G & 5G)", "RFID / NFC"], "richtige_antwort": "RFID / NFC"},
    {"frage": "Drahtlose Kommunikation mit geringer Reichweite?", "antworten": ["RFID / NFC", "Wi-Fi & Bluetooth"], "richtige_antwort": "Wi-Fi & Bluetooth"},
    {"frage": "Die englische Abkürzung für einen Einplatinencomputer lautet?", "antworten": ["SBC", "MCU"], "richtige_antwort": "SBC"},
    {"frage": "Auf welcher OSI-Schicht läuft das MQTT Kurznachrichtenprotokoll?", "antworten": ["Anwendungsschicht", "Transportschicht"], "richtige_antwort": "Anwendungsschicht"},
    {"frage": "Auf welcher OSI-Schicht läuft das TCP & UDP -protokoll?", "antworten": ["Anwendungsschicht", "Transportschicht"], "richtige_antwort": "Transportschicht"},
    {"frage": "Ein ??? erhält Nachrichten von Sendern und leitet diese an die Empfänger weiter?", "antworten": ["MQTT-Broker", "MQTT-Client"], "richtige_antwort": "MQTT-Broker"},
    {"frage": "Ein ??? kann beides sein, ein Publisher und ein Subscriber, je nachdem ob er gerade Nachrichten sendet oder empfängt?", "antworten": ["MQTT-Broker", "MQTT-Client"], "richtige_antwort": "MQTT-Client"},
    {"frage": "Das ??? wird vom Broker genutzt, um Nachrichten der Clients zu filtern?", "antworten": ["MQTT-Broker", "MQTT-Client", "MQTT-Topic"], "richtige_antwort": "MQTT-Topic"},
    {"frage": "QoS heisst Quality of Service?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Qos 0, At most once - höchstens einmal (Fire and Forget)?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "QoS 1, At least once - mindestens einmal?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "QoS 2, Exactly once - genau einmal?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Message Persistence (Beharrlichkeit einer Nachricht):\n- Retained Messages - eine zurückgehaltene Nachricht\n- Persistent Sessions - eine dauerhafte Verbindung\n- Keep Alive\n- Web Sockets Transport?", "antworten": ["Verstanden"], "richtige_antwort": "Verstanden"},
    {"frage": "At most once?", "antworten": ["QoS 0", "QoS 1", "QoS 2"], "richtige_antwort": "QoS 0"},
    {"frage": "At least once?", "antworten": ["QoS 0", "QoS 1", "QoS 2"], "richtige_antwort": "QoS 1"},
    {"frage": "Exactly once?", "antworten": ["QoS 0", "QoS 1", "QoS 2"], "richtige_antwort": "QoS 2"},
    {"frage": "MQTT Architektur:\nEin Sensor (Temp.) fällt unter welchen Begriff?", "antworten": ["Publisher", "Broker", "Subscriber"], "richtige_antwort": "Publisher"},
    {"frage": "MQTT Architektur:\nDer Publisher sendet das 'Topic' (Temp.-Daten) an d.. ???", "antworten": ["Publisher", "Broker", "Subscriber"], "richtige_antwort": "Broker"},
    {"frage": "MQTT Architektur:\nDer Broker sendet das 'Topic' (Temp.-Daten) an d.. ???", "antworten": ["Publisher", "Broker", "Subscriber"], "richtige_antwort": "Subscriber"},
    {"frage": "Für was steht das 'A' im Kürzel VUCA?", "antworten": ["Agility", "Ambiguity"], "richtige_antwort": "Ambiguity"},
    {"frage": "Für was steht das 'V' im Kürzel VUCA?", "antworten": ["Vision", "Volatility"], "richtige_antwort": "Volatility"},
    {"frage": "Für was steht Ambiguity in VUCA?", "antworten": ["Volatilität", "Unsicherheit", "Komplexität", "Mehrdeutigkeit"], "richtige_antwort": "Mehrdeutigkeit"},
    {"frage": "Für was steht Volatility in VUCA?", "antworten": ["Volatilität", "Unsicherheit", "Komplexität", "Mehrdeutigkeit"], "richtige_antwort": "Volatilität"},
    {"frage": "Für was steht Uncertainty in VUCA?", "antworten": ["Volatilität", "Unsicherheit", "Komplexität", "Mehrdeutigkeit"], "richtige_antwort": "Unsicherheit"},
    {"frage": "Für was steht Complexity in VUCA?", "antworten": ["Volatilität", "Unsicherheit", "Komplexität", "Mehrdeutigkeit"], "richtige_antwort": "Komplexität"},
    {"frage": "Unter dem Begriff 'Prototyping, versteht man in der IT den 'Erstellungsprozess' eines voll funktionsfähigen,\nteilweise vereinfachten?", "antworten": ["Endproduktes", "Modells"], "richtige_antwort": "Modells"},
    {"frage": "Um elektronische 'Versuchsaufbauten' schnell zu realisieren und jederzeit abändern zu können, werden sehr gerne 'Breadboards' verwendet.\nDarauf können Sensoren und Aktoren mit Verbindungsleitungen an den Anschlüssen von ??? verdrahtet werden?", "antworten": ["Modellen", "Mikrokontrollern"], "richtige_antwort": "Mikrokontrollern"},
    {"frage": "Eine aktuelle Bestandsaufnahme der schon vorhandenen Komponenten und räumlichen Gegebenheiten?", "antworten": ["IST", "SOLL"], "richtige_antwort": "IST"},
    {"frage": "Zur vermeidung von Unfällen werden Daten wie Geschwindigkeit oder Bremsen ausgetauscht.\nSo können Rettungs- und Einsatzkräfte schneller durch den Verkehr geleitet werden?", "antworten": ["Vehicle-to-Pedestrian", "Vehicle-to-Vehicle"], "richtige_antwort": "Vehicle-to-Vehicle"},
    {"frage": "DevOps: Dev umfasst => Plan, Code, Build & Test?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "DevOps: Ops umfasst => Release, Deploy, Operate & Monitor?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Neue Einplatinencomputer und Mikrocontroller ermöglichen neue IoT-Anwendungen weil 'Kosten und Größe der Hardware sinken'?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Der Energiebedarf für den Betrieb einzelner IoT-Komponenten wird trotz höherer Rechenleistung geringer.\nD.h. die Rechenleistung steigt stetig?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Die Netzabdeckung durch unterschiedliche Funktechnologien hat sich deutlich gesteigert.\nD.h. die Konnektivität wird flächendeckender?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "In einem Arduino Programm, auch 'Sketch' genannt, gibt es mindestens zwei Abschnitte, auch 'Methode' genannt.\nBitte wählen Sie die richtige Eigenschaft für folgende Methoden: Wird einmal ausgeführt / Festlegung der Eigenschaften von Ein- und Ausgängen?", "antworten": ["void setup()", "void loop()"], "richtige_antwort": "void setup()"},
    {"frage": "In einem Arduino Programm, auch 'Sketch' genannt, gibt es mindestens zwei Abschnitte, auch 'Methode' genannt.\nBitte wählen Sie die richtige Eigenschaft für folgende Methoden: Programmierte Befehle, Anweisungen / Wird mehrfach ausgeführt?", "antworten": ["void setup()", "void loop()"], "richtige_antwort": "void loop()"},
    {"frage": "Culture, Automation, Lean, Measurement und Sharing?", "antworten": ["SMART", "VUCA", "CALMS"], "richtige_antwort": "CALMS"},
    {"frage": "Für was steht 'C' in dem Kürzel 'CALMS'?", "antworten": ["Clean", "Culture"], "richtige_antwort": "Culture"},
    {"frage": "Für was steht 'L' in dem Kürzel 'CALMS'?", "antworten": ["Learn", "Lean"], "richtige_antwort": "Lean"},
    {"frage": "Für was steht die Abkürzung IDE?", "antworten": ["Intelligent Device Management", "Integrated Developement Environment"], "richtige_antwort": "Integrated Developement Environment"},
    {"frage": "Für was steht das Kürzel MES?", "antworten": ["Machine Execution System", "Manufacturing Execution System"], "richtige_antwort": "Manufacturing Execution System"},
    {"frage": "Die Massenproduktion fällt unter die Generation?", "antworten": ["1.0", "2.0", "3.0", "4.0"], "richtige_antwort": "2.0"},
    {"frage": "Die Mechanisierung fällt unter die Generation?", "antworten": ["1.0", "2.0", "3.0", "4.0"], "richtige_antwort": "1.0"},
    {"frage": "Prozessablauf einer FMEA:\n(1) Vorbereitung\n(2) FMEA-Team bilden\n(3) Strukturanalyse\n(4) Funktionsanalyse\n(5) Fehleranalyse\n(6) Risikobewertung\n(7) Optimierung", "antworten": ["Verstanden", "Lese es nochmal!"], "richtige_antwort": "Verstanden"},
    {"frage": "Es bezeichnet universelle Ein- und Ausgänge, die durch die Programmierung frei bestimmbar sind?", "antworten": ["UART", "GPIO"], "richtige_antwort": "GPIO"},
    {"frage": "Eine recht einfache Schnittstelle, weswegen man nur zwei Datenleitungen benötigt (TX/RX)?", "antworten": ["UART", "GPIO"], "richtige_antwort": "UART"},
    {"frage": "Transmit Data TX -> Receive Data RX?", "antworten": ["UART", "GPIO"], "richtige_antwort": "UART"},
    {"frage": "Im Gegensatz zu UART erfolgt die Kommunikation 'synchron' durch die SCL-Leitung.\nHat ebenfalls nur zwei Leitungen, eine davon ist die SDA-Leitung (Serial Data Line) / Mehrere Master und mehrere Slave?", "antworten": ["UART", "I2C"], "richtige_antwort": "I2C"},
    {"frage": "Ist voll duplexfähig, kann nur einen Master im Netzwerk einsetzen und für die Kommunikation über die Schnittstelle werden 'vier' Leitungen benötigt?", "antworten": ["i2C", "SPI"], "richtige_antwort": "SPI"},
    {"frage": "Jeder Pin kann individuell durch das Programm als Eingang oder Ausgang benutzt werden?", "antworten": ["GPIO", "UART"], "richtige_antwort": "GPIO"},
    {"frage": "Zwei Leitungen, eine davon ist die SDA-Leitung (Serial Data Line), um Daten zu übertragen.\nDie andere ist die SCL-Leitung (Serial Clock Line), um einen Takt-Impuls zu übertragen?", "antworten": ["I2C", "UART"], "richtige_antwort": "I2C"},
    {"frage": "Bei einer SPI-Schnittstelle werden vier Leitungen benötigt:\n- SCL (Serial Clock Leitung) Der Takt wird vom Master ausgegeben.\n- MOSI (Master Output/Slave Input) Leitung für Daten vom Master zum Slave.\n- MISO (Master Input/Slave Output) Leitung für Daten vom Slave zum Master.\n- CS (Chip Select) Auf dieser Leitung gibt der Master ein LOW-Signal aus, um mit dem entsprechenden Slave zu kommunizieren", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Eine Technologie, die mithilfe elektromagnetischer Felder Objekte oder Tags identifiziert,\ndie bestimmte gespeicherte Informationen enthalten?", "antworten": ["RFID", "NFC"], "richtige_antwort": "RFID"},
    {"frage": "Ein Protokoll für einfache und sichere Interaktion zwischen elektronischen Geräten.\nDie generell Anwendung vor allem bei Smartphones findet?", "antworten": ["RFID", "NFC"], "richtige_antwort": "NFC"},
    {"frage": "Die Eigenschaften sind vergleichbar mit den der Bluetooth-Technologie.\nEs folgt jedoch dem IEEE 802.15.4-Standard und ist ein erweitertes Kommunikationsprotokoll?", "antworten": ["RFID", "ZigBee"], "richtige_antwort": "ZigBee"},
    {"frage": "MQTT wurde für Netzwerke mit großer Verzögerungszeit und kleiner Bandbreite entwickelt?", "antworten": ["Performance", "Skalierbarkeit", "Sicherheit"], "richtige_antwort": "Performance"},
    {"frage": "MQTT wurde dafür entwickelt, die wachsende Anzahl von Sensoren und Geräten mit nur einem Server zu vernetzen?", "antworten": ["Perfomance", "Skalierbarkeit", "Sicherheit"], "richtige_antwort": "Skalierbarkeit"},
    {"frage": "MQTT selbst unterstützt nur eine Absicherung über Benutzername und Passwort.\nMit SSL bzw. TLS kann die Kommunikation auf Transportebene verschlüsselt werden?", "antworten": ["Perfomance", "Skalierbarkeit", "Sicherheit"], "richtige_antwort": "Sicherheit"},
    {"frage": "DevOps (-ziele) soll die Zusammenarbeit zwischen Stakeholder und dem Projektteam von der Planung bis zur Bereitstellung des Produkts verbessern?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Das Kunstwort für 'developement' (Entwicklung) und 'operations' (Betrieb)?", "antworten": ["SpecOps", "DevOps"], "richtige_antwort": "DevOps"},
    {"frage": "Das DevOps-Konzept folgt mehreren Prinzipien, die sich stetig verändern.\nJedoch folgen alle Prinzipien einem ganzheitlichen DevOps-Ansatz, zu diesen Prinzipien gehören:\n- Lösungen entwickeln und in produktionsähnlichen Umgebungen testen\n- wiederholbar und sicher implementieren\n- operative Qualität überwachen und validieren\n- Feedbackschleifen erweitern.", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "DevOps-Kultur:\nAuf der einen Seite möchten die Entwickler mehr Features in die Software integrieren.\nAuf der anderen Seite möchte das Operations-Team ein stabiles System.\nDevOps kann aus diesem Grund nur dann erfolgreich sein, wenn beide Teams miteinander arbeiten.", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Hier werden Konfigurationsmanagement-Tools eingesetzt und mit Tools der Entwicklung und dem Testen kombiniert,\num bei Codeproblemen sehr schnell Rückmeldung zu erhalten?", "antworten": ["Continuous Integration (CI)", "Continuous Delivery (CD)"], "richtige_antwort": "Continuous Integration (CI)"},
    {"frage": "Dieser Ansatz automatisiert die Bereitstellung von Codeänderungen nach dem Testen in einer Vorproduktions- oder Staging-Umgebung.\nDanach kann ein Mitarbeiter über die finale Freigabe in die Produktionsumgebung entscheiden?", "antworten": ["Continuous Integration (CI)", "Continuous Delivery (CD)"], "richtige_antwort": "Continuous Delivery (CD)"},
    {"frage": "Die eigentlichen Endkunden aber auch Kunden innerhalb der Wertschöpfungskette?", "antworten": ["Steakholder", "Stakeholder"], "richtige_antwort": "Stakeholder"},
    {"frage": "Kategorisierung von Anforderungen:\n- Business Requirements:\n- Stakeholder Requirements\n- Solution Requirements\n- Transition Requirements?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Sie beschreiben die Ziele, Ergebnisse und Merkmale eines neuen Produkts oder einer neuen Dienstleistung\nfür den Endbenutzer oder das Unternehmen?", "antworten": ["Business Requirements", "Stakeholder Requirements"], "richtige_antwort": "Business Requirements"},
    {"frage": "Die Bedürfnisse aller Stakeholder, welche berücksichtigt werden müssen, um die Business Requirements zu erfüllen,\nwerden von den Stakeholder Requirements zusammengefasst?", "antworten": ["Stakeholder Requirements", "Solution Requirements"], "richtige_antwort": "Stakeholder Requirements"},
    {"frage": "Sie legen die Leistungsfähigkeit und Qualität einer Lösung dar, die das Ziel hat, die Stakeholder Requirements zu erfüllen.\nSie werden unterteilt in funktionale und nicht-funktionale Anforderungen?", "antworten": ["Solution Requirements", "Transition Requirements"], "richtige_antwort": "Solution Requirements"},
    {"frage": "Sie beschreiben die Leistungsfähigkeit einer Lösung, um die Transition vom Ist-Zustand\nzum Soll-Zustand zu ermöglichen?", "antworten": ["Transition Requirements", "Solution Requirements"], "richtige_antwort": "Transition Requirements"},
    {"frage": "Die Eigenschaften sind vergleichbar mit denen der Bluetooth-Technologie. Es folgt jedoch dem IEEE 802.15.4-Standard\nund ist ein erweitertes Kommunikationsprotokoll. Der geringe Stromverbrauch, die Robustheit, hohe Sicherheit\nund hohe Skalierbarkeit sind analoge Vorteile. Reichweite: 10-100m & Datenübertragungsrate max. 250 Kbit/s?", "antworten": ["ZigBee", "Bluetooth"], "richtige_antwort": "ZigBee"},
    {"frage": "DevOps:\nIn dieser Phase werden die geschäftlichen Anforderungen festgelegt. Tools wie Jira oder Git unterstützen dabei das Projektmanagment?", "antworten": ["Planen (Plan)", "Codieren (Code)"], "richtige_antwort": "Planen (Plan)"},
    {"frage": "DevOps:\nUm präzise und effizient in der Softwareentwicklung arbeiten zu können, ist es wichtig, dass die Teams auf eine Versionskontrolle achten.\nVersionskontrollsysteme wie 'Git' machen von allen Dateien Momentaugnahmen. Der Vorteil besteht darin,\nzu jeder Zeit und dauerhaft ältere Versionen wiederherstellen zu können?", "antworten": ["Planen (Plan)", "Codieren (Code)"], "richtige_antwort": "Codieren (Code)"},
    {"frage": "DevOps:\nIn der dritten Phase gilt es, die Builds zu verwalten. Automatisierte Tools, z.Bsp. 'Docker' unterstützen das kompilieren und Packen von Codes\nfür die anstehenden Produktionsfreigaben?", "antworten": ["Codieren (Code)", "Erstellung (Build)"], "richtige_antwort": "Erstellung (Build)"},
    {"frage": "DevOps:\nIn dieser Phase wird durch kontinuierliches Testen, das sowohl automatisiert als auch manuell durchgeführt werden kann,\ndie Qualität des Codes geprüft. Desweiteren werden Benutzerakzeptanz-, Sicherheits-, Leistungs- und Lasttests durchgeführt.?", "antworten": ["Erstellung (Build)", "Testen (Test)"], "richtige_antwort": "Testen (Test)"},
    {"frage": "DevOps:\nFreigabe eines Software-Releases?", "antworten": ["Testen (Test)", "Freigabe (Release)"], "richtige_antwort": "Freigabe (Release)"},
    {"frage": "DevOps:\nErreicht ein Build die Bereitstellungsphase, ist die Software so weit, in die Produktion übertragen werden zu können?", "antworten": ["Freigabe (Release)", "Bereitstellung (Deploy)"], "richtige_antwort": "Bereitstellung (Deploy)"},
    {"frage": "DevOps:\nIn dieser Phase geht es um das permanente Management der Software im laufenden Betrieb?", "antworten": ["Bereitstellung (Deploy)", "Betrieb (Operate)"], "richtige_antwort": "Betrieb (Operate)"},
    {"frage": "DevOps:\nIn dieser Phase werden Informationen über Probleme in der Produktion erkannt und zurückgemeldet?", "antworten": ["Überwachen (Monitor)", "Testen (Test)"], "richtige_antwort": "Überwachen (Monitor)"},
    {"frage": "Eine gängige Lösung zur Versionsverwaltung ist das Lizensfreie 'Tool' ???.\nDieses Tool besitzt zwei Vorteile, die zu dessen Beliebtheit beitragen:\n- Es ist kostenlos nutzbar &\n- Sehr einfach zu erlernen?", "antworten": ["Windows", "Git"], "richtige_antwort": "Git"},
    {"frage": "Unter einem ??? versteht man in der IT ein voll funktionsfähiges, vereinfachtes Modell eines geplanten Produktes, eines Bauteils oder einer Software?", "antworten": ["Dummy", "Prototyp"], "richtige_antwort": "Prototyp"},
    {"frage": "Grundstruktur eines 'Arduino'-Sketch:\n- Bereich 1 für Bibliotheken, Variablen, Konstanten und zur Initialisierung von Komponenten\n- Bereich 2 für das 'Setup' - Aufruf der Methode 'void setup()'\n- Bereich 3 für die Ablaufsteuerung - Aufruf der Methode 'void loop()'?", "antworten": ["Richtig", "Falsch"], "richtige_antwort": "Richtig"},
    {"frage": "Grundstruktur eines 'Arduino'-Sketch:\nIn diesem Bereich werden die Elemente des Programms benannt, die global verfügbar sind.\nGlobal verfügbar bedeutet, dass diese Werte in allen folgenden Methoden und Funktionen zur Verfügung stehen?", "antworten": ["Bereich 1", "Bereich 2", "Bereich 3"], "richtige_antwort": "Bereich 1"},
    {"frage": "Grundstruktur eines 'Arduino'-Sketch:\nIn diesem Bereich werden Befehle und Anweisungen aufgerufen, die zu Beginn der Ausführung einmal ausgeführt werden.\nDort wird u.a. festgelegt, an welche Pins eines MC-Boards eine Komponente angeschlossen wird und ob sich dabei um Ein- oder Ausgang handelt?", "antworten": ["Bereich 1", "Bereich 2", "Bereich 3"], "richtige_antwort": "Bereich 2"},
    {"frage": "Grundstruktur eines 'Arduino'-Sketch:\nIn diesem Bereich werden die programmierten Befehle, Anweisungen und Funktionen in einem kontinuirlichen Kreislauf wiederholt.\nDeswegen wird dieser Bestandteil, auch als Hauptelemnt eines 'Sketches' bezeichnet. Der Loop-Teil bearbeitet einen Sketch\nvollständig und startet danach automatisch wieder am Anfang des Bereichs.?", "antworten": ["Bereich 1", "Bereich 2", "Bereich 3"], "richtige_antwort": "Bereich 3"}
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lernfeld 7, Quiz von mac80mo")

        self.label_info = tk.Label(root, text="In diesem Fragenpool sind ca. 150 Fragen")
        self.label_info.pack()

        self.label_fragen = tk.Label(root, text="Wieviele Fragen möchten Sie 'random' gestellt bekommen:")
        self.label_fragen.pack()

        self.entry_fragen = tk.Entry(root)
        self.entry_fragen.pack()

        self.button_start = tk.Button(root, text="Start", command=self.start_quiz)
        self.button_start.pack()

        self.label_frage = tk.Label(root, text="")
        self.label_frage.pack()

        self.frame_antworten = tk.Frame(root)
        self.frame_antworten.pack()

        self.var_antwort = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(self.frame_antworten, variable=self.var_antwort, value=i + 1)
            rb.pack(anchor='w')
            self.radio_buttons.append(rb)

        self.button_antwort = tk.Button(root, text="Antworten", command=self.check_antwort)
        self.button_antwort.pack()

        self.label_ergebnis = tk.Label(root, text="")
        self.label_ergebnis.pack()

        self.ausgewaehlte_fragen = []
        self.punkte = 0
        self.aktuelle_frage_index = 0

    def start_quiz(self):
        try:
            anzahl_fragen = int(self.entry_fragen.get())
            self.ausgewaehlte_fragen = random.sample(fragen_pool, min(anzahl_fragen, len(fragen_pool)))
            self.punkte = 0
            self.aktuelle_frage_index = 0
            self.label_ergebnis.config(text="")
            self.next_question()

            self.label_fragen.pack_forget()
            self.entry_fragen.pack_forget()
            self.button_start.pack_forget()
        except ValueError:
            messagebox.showerror("Ungültige Eingabe", "Bitte geben Sie eine gültige Anzahl von Fragen ein.")

    def next_question(self):
        if self.aktuelle_frage_index < len(self.ausgewaehlte_fragen):
            frage = self.ausgewaehlte_fragen[self.aktuelle_frage_index]
            self.label_frage.config(text=frage["frage"])

            for i, rb in enumerate(self.radio_buttons):
                if i < len(frage["antworten"]):  
                    rb.config(text=frage["antworten"][i], state="normal")
                    rb.pack(anchor='w')  
                else:  
                    rb.pack_forget()  

            self.var_antwort.set(0) 
        else:
            self.show_result()

    def check_antwort(self):
        frage = self.ausgewaehlte_fragen[self.aktuelle_frage_index]
        user_antwort_index = self.var_antwort.get() - 1

        if user_antwort_index < 0 or user_antwort_index >= len(frage["antworten"]):
            messagebox.showwarning("Keine Auswahl", "Bitte wählen Sie eine Antwort aus, bevor Sie fortfahren.")
            return

        if frage["antworten"][user_antwort_index] == frage["richtige_antwort"]:
            self.punkte += 5
            messagebox.showinfo("Richtige Antwort!", "Das war korrekt!")
        else:
            messagebox.showinfo("Falsch", f"Das war leider falsch. Die richtige Antwort war: {frage['richtige_antwort']}")

        self.aktuelle_frage_index += 1
        self.next_question()

    def show_result(self):
        max_punkte = len(self.ausgewaehlte_fragen) * 5
        prozentsatz = (self.punkte / max_punkte) * 100

        if prozentsatz >= 92:
            note = "1"
        elif prozentsatz >= 81:
            note = "2"
        elif prozentsatz >= 67:
            note = "3"
        elif prozentsatz >= 50:
            note = "4"
        elif prozentsatz >= 30:
            note = "5"
        else:
            note = "6"

        self.label_ergebnis.config(
            text=f"Ihr Punktestand: {self.punkte} von {max_punkte} möglichen Punkten.\nIhre Note: {note}")

        self.button_beenden = tk.Button(self.root, text="Beenden", command=self.root.quit)
        self.button_beenden.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
