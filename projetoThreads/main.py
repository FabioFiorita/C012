from threading import Thread
from playsound import playsound
import time
from os import chdir
import subprocess

chdir("/Users/fabiofiorita/Repositórios/C012/projetoThreads/")

def playSong():
    playsound('song.wav', True)

def showLyrics():
    lyrics = '''
Nobody wanna see us together
But it don't matter no
'Cause I got you babe
Nobody wanna see us together
But it don't matter no
'Cause I got you babe
'Cause we gonna fight
Oh yes we gonna fight
Believe we gonna fight
(We gonna fight)
Fight for our right to love yeah
Nobody wanna see us together
But it don't matter no
'Cause I got you

Nobody wanna see us together
Nobody thought we'd last forever
I feel I'm hopin' and prayin'
Things between us gonna get better
Men steady comin' after you
Women steady comin' after me
Seems like everybody wanna go for self
And don't wanna respect boundaries
Tellin' you all those lies
Just to get on your side
But I must admit there was a couple secrets
I held inside
But just know that I try
To always apologize
And I'ma have you first always in my heart
To keep you satisfied

Nobody wanna see us together
But it don't matter no
'Cause I got you babe
Nobody wanna see us together
But it don't matter no
'Cause I got you babe
'Cause we gonna fight
Oh yes we gonna fight
Believe we gonna fight
(We gonna fight)
Fight for our right to love yeah
Nobody wanna see us together
But it don't matter no
'Cause I got you, babe

Got every right to wanna leave
Got every right to wanna go
Got every right to hit the road
And never talk to me no more
You don't even have to call
Even check for me at all
Because the way I've been actin' lately
Has been off the wall
Especially towards you
Puttin' girls before you
And they watchin' everything I been doin'
Just to hurt you
Most of it just ain't true
Ain't true
And they won't show you
How much of a queen you are to me
And why I love you baby


Oh oh oh oh oh
'Cause I got you
'Cause I got you
Oh
'Cause I got you babe
'Cause I got you

Nobody wanna see us together
But it don't matter no
'Cause I got you babe
Nobody wanna see us together
But it don't matter no
'Cause I got you babe
'Cause we gonna fight
Oh yes we gonna fight
Believe we gonna fight
We gonna fight
Fight for our right to love yeah
Nobody wanna see us together
But it don't matter no
'Cause I got you
Nobody wanna see us together
But it don't matter no
'Cause I got you babe
Nobody wanna see us together
But it don't matter no
'Cause I got you babe
'Cause we gonna fight
Oh yes we gonna fight
Believe we gonna fight
We gonna fight
Fight for our right to love yeah
Nobody wanna see us together
But it don't matter no
'Cause I got you
    
    '''
    lyricsArray = lyrics.split('\n')
    time.sleep(35)
    for line in lyricsArray:
        print(line)
        time.sleep(2)

def showVideo():
    time.sleep(35)
    subprocess.Popen(["open", '/Users/fabiofiorita/Repositórios/C012/projetoThreads/dance.mp4'])
    
        
t1 = Thread(target=playSong)
t2 = Thread(target=showLyrics)
t3 = Thread(target=showVideo)
t2.start()
t1.start()
t3.start()
