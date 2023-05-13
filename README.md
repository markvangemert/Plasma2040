# Plasma2040
Code en handleiding bij de Wireless Plasma Kit van Pimoroni

# Dit hoef je niet te doen, de Plasma stick 2040 bevat al de nodige programmatuur

kopieer een gecompileerd programma of MicroPython naar de Raspberry Pico:
* Houd knop BOOTSEL ingedrukt en druk op RESET.

In Windows Explorer verschijnt RPI-RP2
* Sleep (kopieer) het programma naar RPI-RP2.
-> RPI-RP2 verdwijnt uit Windows Explorer

Micropython vind je op:
https://micropython.org/download/rp2-pico-w/

# Dit moet je altijd doen

Voor programma's in MicroPython heb je Thonny nodig:
Met Thonny kun je programma's schrijven, testen en van en naar je Raspberry Pico kopieren
* Download Thonny van https://thonny.org/
* Verbind de Raspberry Pico via USB met je computer en start Thonny
Rechtsonder staat dan iets als: "MicroPython (Raspberry Pi Pico) COMx". Als dit niet het geval is dubbelklik dan rechtsonder en kies je Raspberry Pico
In de onderste helft van Thonny kun je MicroPython uitvoeren op je Raspberry Pico. Op de regel met >>> kun je code uitvoeren.
* Typ daar: print("hallo") en ENTER
Dit wordt nu door MicroPython op je Raspberry Pico uitgevoerd en in Thonny geprint

Staat er al code op je Raspberry Pico?
* Verbind de Raspberry Pico via USB met je computer en start Thonny
* Kies "File", dan "Open...", dan: "Raspberry Pi Pico"
De code is ook te vinden op: https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/examples/plasma_stick 

Het LED-je op de Raspberry Pico laten knipperen:
* Verbind de Raspberry Pico via USB met je computer en start Thonny
* Open "Pico Blink.py" in Thonny (File - Open ...)
Je kunt het programma vauit Thonny op je Raspberry Pico uitvoeren:
* Kies "Run", dan "Run current script"
     of
* Klik op het Run-icoontje (groen met wit driehoekje)
     of
* Toets F5
Onderin zie je dat het programma wordt uitgevoerd en eventuele informatie die vanuit het programma wordt geprint
Je kunt het uitvoeren van het programma afbreken met o.a. het Stop-icoontje, of de RESET-knop op de Raspberry Pico


De code naar de Raspberry Pico kopieren:
* Verbind de Raspberry Pico via USB met je computer en start Thonny
* Open "Pico Blink.py" in Thonny (File - Open ...)
Kopeer de code
* Kies "File", dan "Save Copy...", dan "Raspberry Pi Pico"
Als er al een main.py op de Raspberry Pico staat, overschrijf deze alleen als je er ergens een kopie van hebt (zie volgende blok)
* Save de file als "main.py" 
* Druk op de RESET-knop op de Raspberry Pico om het programma te starten
De Raspberry Pico voert altijd maar één programma uit. Of het programma main.py dat op de Raspberry Pico staat, of een programma vanuit Thonny
