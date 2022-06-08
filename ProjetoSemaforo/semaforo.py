import json
import threading
import tkinter
  
root = tkinter.Tk()
root.title("Projeto Semaforo")
root.geometry('700x500')
options_list = ["Sem Semaforo", "Com Semaforo"]
value_inside = tkinter.StringVar(root)
value_inside.set("Selecione a Opção")
question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
question_menu.pack()

f = open('ProjetoSemaforo/data.json')
  
sem = threading.Semaphore()
  
data = json.load(f)

def show_songs_with_semaphore():
    sem.acquire()
    for i in data['songs']:
        print('Nome da musica: ' + i['title'])
    sem.release()

def show_artists_with_semaphore():
    sem.acquire()
    for i in data['songs']:
        print('Nome do artista: ' + i['artist'])
    sem.release()

def show_songs():
    for i in data['songs']:
        print('Nome da musica: ' + i['title'])

def show_artists():
    for i in data['songs']:
        print('Nome do artista: ' + i['artist'])

def without_semaphore():
    threading.Thread(target=show_songs).start()
    threading.Thread(target=show_artists).start()

def with_semaphore():
    threading.Thread(target=show_songs_with_semaphore).start()
    threading.Thread(target=show_artists_with_semaphore).start()

def submitButton():
    if value_inside.get() == "Sem Semaforo":
        without_semaphore()
    else:
        with_semaphore()

def clearTerminal():
    print("\n" * 100)
  
submit_button = tkinter.Button(root, text='Enviar', command=submitButton)
clear_button = tkinter.Button(root, text='Limpar', command=clearTerminal)
submit_button.pack()
clear_button.pack()
  
root.mainloop()

f.close()