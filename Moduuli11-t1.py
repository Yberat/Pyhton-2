from julkaisu import Julkaisu

if __name__ == "__main__":
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti_nro_6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    aku_ankka.tulosta_tiedot()
    print()
    hytti_nro_6.tulosta_tiedot()
