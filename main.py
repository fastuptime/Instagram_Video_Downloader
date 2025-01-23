import instaloader

def download_reels(username):
    loader = instaloader.Instaloader()

    print("Opsiyonel: Instagram hesabınıza giriş yapabilirsiniz.")
    user_login = input("Giriş yapacak mısınız? (evet/hayır): ").strip().lower()
    if user_login == "evet":
        username_login = input("Kullanıcı adınız: ")
        password = input("Şifreniz: ")
        try:
            loader.login(username_login, password)
            print("Başarıyla giriş yapıldı.")
        except Exception as e:
            print(f"Giriş yapılamadı: {e}")
            return

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        
        print(f"{username} kullanıcısının tüm Reels'lerini indiriliyor...")
        for post in profile.get_posts():
            if post.is_video and post.typename == "GraphVideo":
                loader.download_post(post, target=f"{username}_reels")
        
        print(f"{username} kullanıcısının tüm Reels'leri başarıyla indirildi!")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    target_username = input("Reels'lerini indirmek istediğiniz hesabın kullanıcı adını girin: ")
    download_reels(target_username)
