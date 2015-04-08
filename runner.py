import win32api, win32con
import time
import winsound
import win32com.client
#import focus

def click(x,y): #FUNZIONE CLICK PER SPOSTARE IL CURSORE SULLO SCHERMO, nella posizione x,y
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def registra_pos(z):
    print("Posiziona il cursore per click numero: ",z)
    time.sleep(4) # sleep di 4 secondi
    (x,y) = win32api.GetCursorPos() #posizione cursore
    Freq = 2500 # Set Frequency To 2500 Hertz
    Dur = 1000 # Set Duration To 1000 ms == 1 second
    winsound.Beep(Freq,Dur)
    click(x,y)
    return (x,y)


# REGISTRIAMO LA POSIZIONE DEI VARI CLICK

sec = int(input("Inserisci quanti secondi fra 1 click e l'altro: "))

n_click = int(input("Inserisci il numero di click in totale: "))

lista = list() # conterra' le coordinate del cursore
for i in range(n_click):
    lista.append(registra_pos(i))

print("\n\n Configurazione TERMINATA, bot in partenza.. attiva la finestra bersaglio.")
time.sleep(4)
#focus.shell.AppActivate('AddMeFast.com - YouTube Views - Google Chrome') #arbitrariamente attiviamo la finestra bersaglio

# IL BOT ESEGUE I CLICK NELLE POSIZIONI REGISTRATE:

i = 0
while True:
    x,y = lista[i]
    click(x,y)
    print("click numero",i,"su",x,y)
    time.sleep(sec)
    i = (i + 1) % len(lista)
    










