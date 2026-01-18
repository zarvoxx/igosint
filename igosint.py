import os
import instaloader
from colorama import Fore, Style, init
from datetime import datetime

# Renkleri başlat
init(autoreset=True)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def osint_banner():
    print(
        Fore.CYAN
        + Style.BRIGHT
        + """
     ZARVOX INSTAGRAM OSINT v1.0
    [───────────────────────────]"""
    )


def get_instagram_data():
    clear()
    osint_banner()

    target = input(Fore.YELLOW + "\n[?] Hedef Kullanıcı Adı: " + Fore.WHITE)
    L = instaloader.Instaloader()

    try:
        print(Fore.CYAN + "[*] Bilgiler toplanıyor, lütfen bekleyin...\n")
        profile = instaloader.Profile.from_username(L.context, target)

        # Temel Bilgiler
        print(f"{Fore.GREEN}[+] Kullanıcı Adı  : {profile.username}")
        print(f"{Fore.GREEN}[+] Kullanıcı ID   : {profile.userid}")
        print(f"{Fore.GREEN}[+] Tam Ad         : {profile.full_name}")
        print(f"{Fore.GREEN}[+] Biyografi      : {profile.biography}")
        print(
            f"{Fore.GREEN}[+] Profil Linki   : https://instagram.com/{profile.username}"
        )

        print(Fore.WHITE + "─" * 40)

        # İstatistikler
        print(f"{Fore.BLUE}[>] Takipçi Sayısı : {profile.followers}")
        print(f"{Fore.BLUE}[>] Takip Edilen   : {profile.followees}")
        print(f"{Fore.BLUE}[>] Gönderi Sayısı : {profile.mediacount}")

        print(Fore.WHITE + "─" * 40)

        # Detaylı Durum Analizi
        print(
            f"{Fore.YELLOW}[!] Gizli Hesap mı : {'Evet' if profile.is_private else 'Hayır'}"
        )
        print(
            f"{Fore.YELLOW}[!] Onaylı Hesap   : {'Evet' if profile.is_verified else 'Hayır'}"
        )
        print(
            f"{Fore.YELLOW}[!] İşletme Hesabı : {'Evet' if profile.is_business_account else 'Hayır'}"
        )
        if profile.is_business_account:
            print(f"{Fore.YELLOW}[!] Kategori       : {profile.business_category_name}")

        print(
            f"{Fore.YELLOW}[!] Dış Bağlantı   : {profile.external_url if profile.external_url else 'Yok'}"
        )

        # Profil Fotoğrafı
        print(f"{Fore.CYAN}[#] HD Profil Foto : {profile.profile_pic_url}")

        # Veriyi Dosyaya Kaydetme
        save = input(
            Fore.WHITE + "\n[?] Bu bilgileri rapora kaydetmek ister misin? (e/h): "
        )
        if save.lower() == "e":
            filename = f"{target}_osint_report.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"ZARVOX OSINT RAPORU - {datetime.now()}\n")
                f.write(
                    f"Kullanıcı: {profile.username}\nID: {profile.userid}\nBio: {profile.biography}\n"
                )
                f.write(
                    f"Takipçi: {profile.followers}\nTakip Edilen: {profile.followees}\n"
                )
                f.write(f"HD Foto Link: {profile.profile_pic_url}\n")
            print(Fore.GREEN + f"\n[✓] Rapor oluşturuldu: {filename}")

    except instaloader.exceptions.ProfileNotExistsException:
        print(Fore.RED + "\n[!] HATA: Kullanıcı bulunamadı!")
    except Exception as e:
        print(Fore.RED + f"\n[!] BEKLENMEDİK HATA: {e}")


if __name__ == "__main__":
    get_instagram_data()
    input(Fore.GRAY + "\nÇıkmak için Enter'a bas...")
