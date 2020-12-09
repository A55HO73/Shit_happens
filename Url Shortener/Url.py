import pyautogui as pg
import pyshorteners as ps

link = pg.prompt("Enter Your Url :")

shortener = ps.Shortener()

try :
    x = shortener.tinyurl.short(link)
    ps.alert(x)
except :
    pg.alert("Please  Check Your Internet Connection")


