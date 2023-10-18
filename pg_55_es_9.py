#dati due punti del piano cartesiano calcolare la loro distanza
import math
def main():
    a = (3, 6)
    b = (3, 7)
    distanza = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
    print(distanza)

if __name__ == "__main__":
    main()