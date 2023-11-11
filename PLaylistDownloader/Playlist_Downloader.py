from pytube import*
import customtkinter
import os
import threading

#création de la fenetre
app = customtkinter.CTk()
app.title("Youtube playlist downloader")
app.geometry("900x450")
app.iconbitmap("icone.ico")


progressbar = customtkinter.CTkProgressBar(app,width=800,height=50)
champerreur = customtkinter.CTkLabel(app, text="", text_color="red")
champerreur.grid(row=7,column=0)


def telecharger_playlist(origine,arrivee):
    """
        telecharger_playlist(str,str,str(facultatif)) --> None(str si le chemin d'arrivée est incorrect))
        origine : link of the youtube playlist you want to download
        arrivee : chemin du dossier dans lequel les vidéos seront telechargées
    """
    compteur=0        
    if os.path.exists(arrivee):
        playlist = Playlist(origine)
        listeplaylists = playlist.video_urls
        nbvideo = len(listeplaylists)
        for url in listeplaylists:
            video = YouTube(url)
            video.streams.get_by_itag(139).download(arrivee)
            compteur +=1
            progressbar.set(compteur/nbvideo)
    else:
        champerreur.configure(text="le chemin d'arrivée est incorrect")
        return "le chemin d'arrivée est incorrect"

# création des elements de la fenetre
descchampytb = customtkinter.CTkLabel(app, text = "Entrer le lien de la playlist Youtube : ",width=800,height=50)
descchampytb.grid(row=1,column=0,padx=50)

champytb = customtkinter.CTkEntry(app, placeholder_text="Lien de la playlist Youtube",width=800,height=50)
champytb.grid(row=2,column=0,padx=50)

descchamparrivee = customtkinter.CTkLabel(app, text = "Entrer le chemin de la playlist d'arrivee : ",width=800,height=50)
descchamparrivee.grid(row=3,column=0,padx=50)

champarrivee = customtkinter.CTkEntry(app, placeholder_text="Chemin de la playlist d'arrivee",width=800,height=50)
champarrivee.grid(row=4,column=0,padx=50)

def valider():
    """
    recupere les valeurs entrées dans les champs et applemme la fonction Telecharger_Playlist() avec ceux-ci
    """
    champerreur.configure(text="")
    progressbar.set(0)
    v_champytb = champytb.get()
    v_champarrivee = champarrivee.get()
    
    telecharger_playlist(v_champytb,v_champarrivee)
        
def start_valider():
    """
    appelle la fonction valider avec threading pour actualiser la barre de chargement pendant que la fonction
    Telecharger_Playlist continue d'etre executée"
    """
    threading.Thread(target=valider).start()

btnvalider = customtkinter.CTkButton(app, text="Valider",command=start_valider,width=100,height=50)
btnvalider.grid(row=8,column=0,padx=50,pady=30)

progressbar.grid(row=9,column=0,padx=50)
progressbar.set(0)

app.mainloop()


