from hissi import Hissi

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lukumaara):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lukumaara)]

    def aja_hissia(self, hissin_numero, tavoite_kerros):
        if 0 <= hissin_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissin_numero}.")
            self.hissit[hissin_numero].siirry_kerrokseen(tavoite_kerros)
        else:
            print(f"Virhe: Hissi {hissin_numero} ei ole olemassa.")

    def palohalytys(self):
        print("Palohälytys! Kaikki hissit siirtyvät pohjakerrokseen.")
        for i, hissi in enumerate(self.hissit):
            print(f"Siirretään hissi {i} pohjakerrokseen.")
            hissi.siirry_kerrokseen(self.hissit[0].alin_kerros)
