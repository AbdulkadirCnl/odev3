class Personel:
     def __init__(self, adi, departmani, calisma_yili, maasi):
        self.adi = adi
        self.departmani = departmani
        self.calisma_yili = calisma_yili
        self.maasi = maasi

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self, personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        print("Firma Personelleri:")
        for personel in self.personel_listesi:
            print(f"Adi: {personel.adi}, Departmani: {personel.departmani}, Çalişma Yili: {personel.calisma_yili}, Maaşi: {personel.maasi}")

    def maas_zammi(self, personel, zam_orani):
        personel.maasi *= (1 + zam_orani / 100)
        print(f"{personel.adi} adli personelin maaşi {zam_orani}% oraninda artirildi. Yeni maaşi: {personel.maasi}")

    def personel_cikart(self, personel):
        if personel in self.personel_listesi:
            self.personel_listesi.remove(personel)
            print(f"{personel.adi} adli personel listeden çikartildi.")
        else:
            print("Belirtilen personel listede bulunamadi.")

if __name__ == "__main__":
    personel1 = Personel("Ahmet", "İnsan Kaynaklari", 5, 5000)
    personel2 = Personel("Mehmet", "Muhasebe", 3, 4500)
    personel3 = Personel("Ayşe", "Satiş", 7, 6000)

    firma = Firma()

    firma.personel_ekle(personel1)
    firma.personel_ekle(personel2)
    firma.personel_ekle(personel3)

    firma.personel_listele()

    firma.maas_zammi(personel1, 10)

    firma.personel_cikart(personel2)

    firma.personel_listele()
