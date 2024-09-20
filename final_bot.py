from sys import argv; args = argv[1:]
from time import process_time
from multiprocessing import Value
LIMIT_AB = 15
LIMIT_MG = 9
CRN = 0x8100000000000081
LRMASK = 0x7e7e7e7e7e7e7e7e
ALLFILL = 0xffffffffffffffff
MIDDLE = 0x7e7e7e7e7e7e00
bot = 0xFF
right =	0x101010101010101
left = 0x8080808080808080
top = 0xFF00000000000000
bt = bot | top
rl = right | left
bord = bt | rl
nr = ~right
nl = ~left
evaltrt = {}
pmtrt = {}
def rbc(b):
    b -= (b >> 1) & 0x5555555555555555
    b = (b & 0x3333333333333333) + ((b >> 2) & 0x3333333333333333)
    b = (b + (b >> 4)) & 0x0f0f0f0f0f0f0f0f
    b += b >> 8
    b += b >> 16
    return (b + (b >> 32)) & 0x7f
BCOUNTL = []
for k in range(1 << 16): BCOUNTL.append(rbc(k))
ob = {0x4dc5ea74d79a3e4: 19, 0x378f49c90bc5b95: 29, 0x378f93bac33f3b1: 43, 0x120da19a5e23e3db: 20, 0x6aca7047f11eea1fd7: 34, 0x4dc5ea7c0ef7a51: 37, 0x4dc6c8824778e57: 34, 0x60496c2d909d4b1: 19, 0x4dc60f74eab465f: 44, 0x4dc6ed7b2335a65: 18, 0x604991266c5a0bf: 20, 0x9076cd9523aabdd: 43, 0x23a0aea3f5ea88c017: 45, 0x14059c26d7502c1a6fd: 19, 0x356538c004b29dc9db: 45, 0x58fcdff7214aebde15: 29, 0x175b5f3c0a06324c4fb: 26, 0x378edad554909f2: 43, 0x378f93c4dd8ecb0: 43, 0x120da19affc8dcda: 43, 0x6aca7047f1c08f18d6: 52, 0x378dfcfc57ebb2c: 37, 0x378f4a30f5d381d: 29, 0x3797173e317724c: 41, 0x120da88b318ce6dd: 45, 0x1405434720f939e6d6c: 37, 0x3f791eeba946b99d2: 42, 0xbe0b0e232680ae070: 43, 0x239aaa3dc030878514: 43, 0x6ac9f9cf433c5ea236: 52, 0x14053be073f48c06bfa: 43, 0x378f24c615d63da: 29, 0x120da63a1b4074f6: 38, 0x6aca704c90dc06b0f2: 29, 0x378e46ee0f65348: 21, 0x378f9415b00b4a8: 29, 0x3797612fe8f0a68: 29, 0x120d985be1edffc8: 38, 0x140543476aeaf160588: 19, 0x3f791f359afe331ee: 44, 0xbe0ec26a07692ab15: 43, 0x239aaa425f4bff1d30: 13, 0x6acaab934f3106d1ed: 45, 0x14053be0bde64380416: 44, 0x120dd226db87848a: 19, 0x120de6f5a2fc48df: 18, 0x120de0073f0f9890: 50, 0x120e1e75bfa38467: 20, 0x120e09b1127e5002: 19, 0x11dcd6edc782876a08: 44, 0x11dcd6f266fa5d4748: 25, 0x11ddff25e29aa1c468: 34, 0x1dba85540b98bfb1a8: 34, 0x1302e5033a1e1d2ea0ac8: 42, 0xa0374b9440df705bce: 34, 0xa0374b98dffae7f3ea: 25, 0x10afe42e7956d9e2010: 20, 0x201260136cf363e672d816: 34, 0x6aca70787d9c4dc086: 20, 0x6aca70787df8ac05aa: 11, 0x6aca70865dffd5d48c: 20, 0x6aca7086613f2642d0: 20, 0x6aca70b007d3448bfe: 21, 0x7c9539941e434da604: 26, 0x7c95eb582a94541adf: 18, 0x7c9661cc395b680064: 22, 0x9a3e62ff0cafe3691f: 34, 0x130990896483893b046c4: 26, 0x10aefae3a97a03697ca: 11, 0x10aefae3f36bbae2fe6: 20, 0x56c02f45992dda3139e: 20, 0x4dc5ea7c8a299da: 37, 0x4dc5ea7f6d68a9c: 26, 0x4dc7377bc49251e: 42, 0x4dcf04c9f27e922: 26, 0x6049db270db6b78: 37, 0x239c8427693775fd5c: 37, 0x4dc6ed86aefe4ad: 34, 0x6049b62ad3df715: 20, 0x906db351d5f23c4: 37, 0x906db36bd01f2f0: 37, 0x9076cd9c5b0824a: 43, 0x23a0aea3f65dfe9684: 29, 0x14059c26d7576377d6a: 37, 0x3565382e607dc241c2: 37, 0x3565382e621d6510ee: 52, 0x356538c0052613a048: 26, 0x58fcdff721be61b482: 29, 0x175b5f3c0a0d69a9b68: 37, 0x4dc6c879a0447c6: 42, 0x4dc6c8824a01a0c: 42, 0x4dc7376fbf268e6: 19, 0x4dc781673c84626: 26, 0x604ab92140cc346: 26, 0xbe28ad9bb122ab086: 34, 0x4dc6c8a940418ec: 34, 0x4dc5eab003fe895: 29, 0x60496c6185a42f5: 19, 0x4dc9d14e721e2e1: 26, 0x4dcd49ed8d1fa7e: 33, 0x604dc1f32fd0921: 42, 0x2a5b35860c2804fe: 33, 0x906d44743fa7335: 53, 0x97d5ad42fac8195: 45, 0x6acffe4359cd5dc7ac: 34, 0xa02a1a583ee777a006: 42, 0xa02a1a583f15a4f546: 42, 0xa02a1a63cdc13b9e66: 42, 0xa02a90decc015703a6: 26, 0xac07c8c5725f9e08c6: 34, 0x10af111b28333f1ca8c: 26, 0x1fff37ada1facf617: 19, 0x1fff37ada088ffcd8: 43, 0x1fff388ba6c1810de: 26, 0x1fff388bdab687f22: 20, 0x200563398a11f041a: 18, 0x5f3d13529192f088c: 37, 0x5f3d149f8f5be9c4d: 37, 0x130168a313b7c855356fa: 19, 0x11d0cde2effd6d5ade: 37, 0x11d0cdf7bfd9fcee9f: 34, 0x1302e442a970a4dcffb9e: 26, 0xab08383384a0757ae382e: 30, 0x3566606d6b0ee41bdd: 21, 0x3566606d6c6940372e: 20, 0x3566607b4e9a9fa4e8: 43, 0x3574f51a69218cf008: 18, 0x20118a7d9fb09054f6ff28: 11, 0xa02b428969151500bf: 53, 0xa02b42896a6f711c10: 45, 0xa02b42974ca0d089ca: 43, 0xa039d7366727bdd4ea: 19, 0x4dc60f74eacc6ce: 44, 0x4dc75c742535212: 44, 0x4dc64d1974370ee: 19, 0x4dcf29c25321616: 44, 0x604a001f6e5986c: 21, 0x239c8429b8bd802a50: 19, 0x906e15ec57da930: 44, 0x9076f29536c4e58: 43, 0x97d5f721ef1b8fc: 38, 0x23a0aea645ebba6292: 19, 0x14059c26fc503f34978: 44, 0x356538348a25e0c72e: 44, 0x356538c254b3cf6c56: 43, 0x3565aeb29d7f54d6fa: 44, 0x58fcdff9714c1d8090: 29, 0x175b5f3c2f064566776: 44, 0x4dc6ed7b25be61a: 18, 0x4dc75c689ae34f4: 29, 0x4dc79a0bb2de791: 26, 0x604ade1a1c88f54: 19, 0xbe28adc0a9fe67c94: 34, 0x4dc60fb5dcfd034: 44, 0x4dc5a1cc2ff70cc: 26, 0x604a005eef1aa4f: 44, 0x4dc9f642f96fb14: 44, 0x4dcd6ee668dc68c: 19, 0x604de6ec0b8d52f: 20, 0x2a5b37d599e3d10c: 19, 0x906f62ea20d3cf1: 42, 0x97d71f2287eccd4: 34, 0xbe6b5589886c5d1f4: 29, 0x6acffe45a95b1993ba: 18, 0x3c0fb39a226a3c4486c: 25, 0xa02a1a655808a13fd1: 46, 0xa02a90e11b8f12cfb4: 45, 0xac07c8c7c1ed59d4d4: 29, 0x10af111b4d2c1ad969a: 26, 0x1fff37889d17cb208: 21, 0x1fff37d29964bc8e6: 26, 0x1fff37d29f2aa0e0a: 19, 0x1fff38b09f9d3dcec: 19, 0x1fff38b0d39244b30: 20, 0x2005635e82edad028: 21, 0x5f395f7a9b3daa211: 43, 0x5f396058a1762b617: 26, 0x5f4aa6fd5259a40ee: 20, 0x11d0cde78f5e2ba6d5: 19, 0x11d0cdfa0f67b8baad: 21, 0x1302e442a9959db8bc7ac: 12, 0xab08383384c56e56a043c: 12, 0x3565aeabae064d573f: 46, 0x3565aeb04f1dcb6ba1: 45, 0x3574f51cb8af48bc16: 20, 0xa02b428718c6e4bcb0: 21, 0xa02b428718e5aed3bc: 21, 0xa02b428bb8e81218b2: 21, 0xa02b428bb9fd2ce81e: 19, 0xa02b42999c2e8c55d8: 20, 0xa039d738b6b579a0f8: 19, 0x90771790f573cf8: 44, 0xbe6b5d31dadb9a758: 44, 0x23a212ad8528977b32: 44, 0x6acffec02e820d691e: 42, 0x1405ded74b7a592c084: 42, 0x3c0fb3a1cabcab81dd0: 42, 0x90771793d865f8a: 43, 0x23a21298b6ebb01e93: 18, 0x1405ded5fe968ab63e5: 17, 0x907580c86d1cbc4: 51, 0x907580c86fd0b74: 51, 0x23a2c45f13c8759d9f: 42, 0x1406002a51ff7d21227: 44, 0x908e35f494bf002: 43, 0x23a0aee2639b48905d: 45, 0x14059c2abe2b3817743: 20, 0x908e36428449568: 42, 0xbe6b59ba91cdb1050: 43, 0x23a0aef736e557b4f4: 44, 0x6acffe88b9f12ed216: 44, 0x14059c2c0b5fd909bda: 37, 0x3c0fb39e53739d986c8: 42, 0x23a0aea3f68c2db916: 37, 0x23a0aeb1d9d2a7f63c: 34, 0x23a2c4582396b1939c: 18, 0x23ce81f716871fe79b: 17, 0x23a0aea1a626eb4bb4: 38, 0x23a0aea6464818a7b6: 45, 0x23a0aeb4298e92e4dc: 34, 0x23a2c45a73529c823c: 29, 0x23ce81f966430ad63b: 21, 0x23a07365b18424e2d4: 44, 0x23a24df4437d979c2d: 43, 0x2794c79e13ee37fe54: 44, 0x163f0f3b698a28cd07c: 19, 0x2990910b57fca692cd: 19}

def main():
    board = args[0]
    player = args[1]
    best_move = Value('d')
    if (hx:=int((dr:=board.replace(".", "0")).replace(player, "1").replace("xo"[player == "x"], "2"), 3)) in ob: 
        best_move.value = ob[hx]
        return
    bx = int(dr.replace("o", "0").replace("x", "1"), 2)
    bo = int(dr.replace("o", "1").replace("x", "0"), 2)
    me, en = (bx, bo) if player == "x" else (bo, bx)
    if (dc:=board.count(".")) < LIMIT_AB:
        print(MTDF(me, en, 64 + LIMIT_MG//2 + 2, best_move))
    elif dc < LIMIT_AB + 2: print(MTDF(me, en, LIMIT_MG, best_move))
    else: print(MTDF(me, en, LIMIT_MG + 1, best_move))

def MTDF(me, en, maxd, best_move):
    tim = process_time()
    f = -1000000
    m = None
    global trt
    if maxd > 64: r = [*range(1, maxd-64)] + [64]
    else: r = range(1, maxd)
    for depth in r:
        f = -1000000
        trt = {}
        upb = 100000000
        lwb = -100000000
        while lwb < upb:
            if f == lwb: beta = f + 1 
            else: beta = f
            f, m = abmlvl1(me, en, beta - 1, beta, depth, m)
            if f < beta: upb = f 
            else: lwb = f
        best_move.value = (mov := 64 - m.bit_length())
        print(f"Time: {round(process_time()-tim, 3)}, Move: {mov}, Weight: {round(f, 3)}, Depth: {depth}")
    return 64 - m.bit_length()

def abmlvl1(me, en, a, beta, d, gm):
    g = (-100000000, 0)
    if gm != None:
        bm, be = place(me, en, gm)
        g = (abm(be, bm, False, a, beta, d - 1), gm)
        a = max(a, g[0])
        if g[0] >= beta: return g
    for loc in smth(getmoves(me, en)):
        if loc == gm: continue
        bm, be = place(me, en, loc)
        t = (abm(be, bm, False, a, beta, d - 1), loc)
        if t[0] > g[0]: g = t
        a = max(a, g[0])
        if g[0] >= beta: return g
    return g

#m = if maximizing player or not
def abm(me, en, m, alpha, beta, d):
    if (k:=(me, en, m)) in trt:
        if (j:=trt[k])[0] and j[0] >= beta: return j[0]
        if j[1] and j[1] <= alpha: return j[1]
        if j[0]: alpha = max(alpha, j[0])
        if j[1]: beta = min(beta, j[1])
    if d == 0: 
        if m: return evalb(me, en)
        else: return evalb(en, me)
    elif not (pm := getmoves(me, en)): 
        if not getmoves(en, me): #change this to a diff method to just look for one move and return true
            if m: g = (((fsc:=(bcount(me) - bcount(en))) > 0)*2 - 1) * 99934 + fsc
            else: g = (((fsc:=(bcount(en) - bcount(me))) > 0)*2 - 1) * 99934 + fsc
        else: g = abm(en, me, not m, alpha, beta, d)
    elif m:
        mvs = smth(pm)
        g = -100000000
        a = alpha
        for loc in mvs:
            bm, be = place(me, en, loc)
            g = max(g, abm(be, bm, not m, a, beta, d - 1))
            a = max(a, g)
            if g >= beta: break
    else:
        mvs = smth(pm)
        g = 100000000
        b = beta
        for loc in mvs:
            bm, be = place(me, en, loc)
            g = min(g, abm(be, bm, not m, alpha, b, d - 1))
            b = min(b, g)
            if g <= alpha: break
    if g <= alpha:
        if k in trt: trt[k] = (trt[k][0], g)
        else: trt[k] = (None, g)
    if g > alpha and g < beta: trt[k] = (g, g)
    if g >= beta:
        if k in trt: trt[k] = (g, trt[k][1])
        else: trt[k] = (g, None)
    return g

def getmoves(me, en): #could combine a lot of these
    if (k:=(me, en)) in pmtrt: return pmtrt[k]
    ten = en & LRMASK
    t = (me >> 1 | me << 1) & ten
    for i in range(5): t |= (t >> 1 | t << 1) & ten
    mvs = (t >> 1 | t << 1)
    t = (me >> 7 | me << 7) & ten
    for i in range(5): t |= (t >> 7 | t << 7) & ten
    mvs |= (t >> 7 | t << 7)
    t = (me >> 8 | me << 8) & en
    for i in range(5): t |= (t >> 8 | t << 8) & en
    mvs |= (t >> 8 | t << 8)
    t = (me >> 9 | me << 9) & ten
    for i in range(5): t |= (t >> 9 | t << 9) & ten
    mvs |= (t >> 9 | t << 9)
    pmtrt[k] = mvs & ~(me | en) & ALLFILL
    return pmtrt[k]

def place(me, en, loc):
    flips = 0
    ten = en & LRMASK
    t = (loc >> 1) & ten
    for i in range(5): t |= (t >> 1) & ten
    if (t >> 1) & me: flips |= t
    t = (loc << 1) & ten
    for i in range(5): t |= (t << 1) & ten
    if (t << 1) & me: flips |= t
    t = (loc >> 7) & ten
    for i in range(5): t |= (t >> 7) & ten
    if (t >> 7) & me: flips |= t
    t = (loc << 7) & ten
    for i in range(5): t |= (t << 7) & ten
    if (t << 7) & me: flips |= t
    t = (loc >> 8) & en
    for i in range(5): t |= (t >> 8) & en
    if (t >> 8) & me: flips |= t
    t = (loc << 8) & en
    for i in range(5): t |= (t << 8) & en
    if (t << 8) & me: flips |= t
    t = (loc >> 9) & ten
    for i in range(5): t |= (t >> 9) & ten
    if (t >> 9) & me: flips |= t
    t = (loc << 9) & ten
    for i in range(5): t |= (t << 9) & ten
    if (t << 9) & me: flips |= t
    return ((me | flips | loc) & ALLFILL, (en & ~flips) & ALLFILL)

def bcount(b): return BCOUNTL[b & 0xffff] + BCOUNTL[(b >> 16) & 0xffff] + BCOUNTL[(b >> 32) & 0xffff] + BCOUNTL[(b >> 48) & 0xffff]

def smth(pm):
    mvs = []
    while pm:
        mvs.append(pm & -pm)
        pm &= (pm - 1)
    return mvs

def crnasc(b):
    sc = 0
    if not b & 1: 
        if b & 1 << 1: sc -= 1
        if b & 1 << 8: sc -= 1
        if b & 1 << 9: sc -= 1.75
    if not b & 1 << 7:
        if b & 1 << 6: sc -= 1
        if b & 1 << 15: sc -= 1
        if b & 1 << 14: sc -= 1.75
    if not b & 1 << 56:
        if b & 1 << 48: sc -= 1
        if b & 1 << 57: sc -= 1
        if b & 1 << 49: sc -= 1.75
    if not b & 1 << 63:
        if b & 1 << 55: sc -= 1
        if b & 1 << 62: sc -= 1
        if b & 1 << 54: sc -= 1.75
    return sc

def front(me, en):
    brd = me | en
    emp = ~ brd
    front = brd & (emp >> 8 | emp << 8 | (emp & nl) << 1 | (emp & nr) >> 1 | (emp & nr) >> 9 | (emp & nl) >> 7 | (emp & nl) << 9 | (emp & nr) << 7)
    return front & MIDDLE

def newstable(me, en, brd):
    mstab = 0
    trow, tcol = top << 8, left << 1
    trl, tbt = rl, bt
    while (trow := (trow >> 8)): trl |= ((brd & trow) == trow) * trow
    while ((tcol := (tcol >> 1)) != (right >> 1)): tbt |= ((brd & tcol) == tcol) * tcol
    while True:
        table = mstab | (me & ((mstab >> 8 | mstab << 8 | tbt) & (mstab >> 1 | mstab << 1 | trl) & (mstab >> 7 | mstab << 7 | bord) & (mstab >> 9 | mstab << 9 | bord)))
        if not (table ^ mstab): break
        mstab |= table
    estab = 0
    while True:
        table = estab | (en & ((estab >> 8 | estab << 8 | tbt) & (estab >> 1 | estab << 1 | trl) & (estab >> 7 | estab << 7 | bord) & (estab >> 9 | estab << 9 | bord)))
        if not (table ^ estab): break
        estab |= table
    return bcount(mstab) - bcount(estab)

def evalb(me, en):
    if (k:=(me, en)) in evaltrt: return evaltrt[k]
    hl = 60 - bcount(ALLFILL & ~(me | en))
    crns = bcount(me & CRN) - bcount(en & CRN)
    crnsc = crnasc(me) - crnasc(en)
    mob = bcount(getmoves(me, en)) - bcount(getmoves(en, me))
    if me & CRN or en & CRN: stab = newstable(me, en, me|en)
    else: stab = 0
    frsc = bcount((fr:=front(me, en))&en) - bcount(fr&me)
    dsc = bcount(me) - bcount(en)
    evaltrt[k] = (1700 * crns) + ((300-hl) * stab) + ((90+(hl/2)) * (mob*1.25 + frsc)) + (125 * crnsc) + ((-12 + hl/2) * dsc)
    return evaltrt[k]

if __name__ == "__main__": main()