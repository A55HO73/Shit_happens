
import pyshorteners as ps

def main():
    link = input("Enter the Link :")
    shortener = ps.Shortener()
    x = shortener.tinyurl.short(link)
    print(x)



main()