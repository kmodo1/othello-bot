import sys; args = sys.argv[1:]
from final_bot import *
from time import process_time
args = [int(j) for j in args]
p = process_time()
from multiprocessing import Value; va = Value("d")

try:
    def main():
        global stuff, cached
        stuff = [(34628173824, 68853694464)]
        cached = {}
        i = 0
        global LIMIT_MG, trt, evaltrt
        LIMIT_MG = args[1]
        while i < args[0]:
            me, en = stuff[i]
            i += 1
            if int((hx:=hex(int(str(int(bin(me)[2:]) + int((bin(en).replace("1", "2"))[2:])), 3))), 16) not in ob:
                if not hx in cached:
                    mv = MTDF(me, en, LIMIT_MG + 1, va)
                    cached[hx] = mv
                    evaltrt = {}
                    trt = {}

            else: cached[hx] = ob[int(hx, 16)]
            if len(stuff) < args[0]:
                for loc in smth(getmoves(me, en)):
                    nbm, nbe = place(me, en, loc)
                    if bin(nbm).count("1") + bin(nbe).count("1") > 9: 
                        print(len(stuff))
                        exit()
                    stuff.append((nbe, nbm))
            print(i)
            open("book.txt", "w").write(str(cached).replace("'", ""))

    if __name__ == "__main__": main()

except:
    print(stuff)
    print(cached)
    open("book.txt", "w").write(str(cached).replace("'", ""))
    print(f"Time: {process_time()-p}s")
    exit()

def printb(b): print("\n".join(("0"*64 + bin(b)[2:])[-64:][i:i+8] for i in range(0, 64, 8)))
