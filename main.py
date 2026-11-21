import json,os,urllib.request as u
E=os.getenv("MAKEFUN_ENV_URL")
V=[0,100,320,330,500,900,0]
PS=["KKKKLMMGLJIKKKKOLLMPMMOQUUUUKKKK","ACEECGKLELMNEKNOELNOEKMNCGKKACEE","GIIIILKKIMMMIKMMILLMIKLMIKKKGIII","KKKLJ"+"KKKJ"*4+"KKKLMMMKKKK","GIIJIKLKILLLKKLLJKLLIKLLIKKKGIIJ","OQMKOOKKIGGGGEEC"+"ECCA"*4]
KN=[-33,-31,-18,-14,14,18,31,33]
BI=[-17,-15,15,17]
RI=[-16,-1,1,16]
KI=sorted(BI+RI)
CK={0:13,7:14,4:12,112:7,119:11,116:3}
NB=60000
I=10**9
B=[0]*128
sd=1;cr=15;ep=-1;K=[4,116]
nd=0
class X(Exception):pass
def atk(s,w):
 for O,t in(((-15,-17) if w else(15,17),1),(KN,2),(KI,6)):
  for o in O:
   g=s+o
   if not g&136 and B[g]==(t if w else-t):return 1
 for o in BI+RI:
  g=s
  while 1:
   g+=o
   if g&136:break
   q=B[g]
   if q:
    a=abs(q)
    if(q>0)==w and a in(5,3+(o in RI)):return 1
    break
 return 0
def ev():
 s=0
 for q in range(128):
  if q&136:continue
  p=B[q]
  if not p:continue
  t=abs(p)
  r=q>>4
  v=V[t]+5*(ord(PS[t-1][(r if p>0 else 7-r)*4+min(q&7,7-(q&7))])-75)
  s+=v if p>0 else-v
 return s if sd>0 else-s
def gen():
 ms=[]
 for s in range(128):
  if s&136:continue
  p=B[s]
  if not p or(p>0)!=(sd>0):continue
  t=abs(p)
  if t==1:
   d=16*sd
   w=7*(sd>0)
   f=s+d
   if not B[f]:
    ms.append(s|f<<7|((5<<14)if f>>4==w else 0))
    if(s>>4)==1+5*(sd<0)and not B[s+2*d]:ms.append(s|(s+2*d)<<7)
   for o in(-1,1):
    g=s+d+o
    if not g&136 and((B[g]and(B[g]>0)!=(sd>0))or g==ep):ms.append(s|g<<7|((5<<14)if g>>4==w else 0))
  else:
   for o in(0,0,KN,BI,RI,BI+RI,KI)[t]:
    g=s
    while 1:
     g+=o
     if g&136:break
     q=B[g]
     if q:
      if(q>0)!=(sd>0):ms.append(s|g<<7)
      break
     ms.append(s|g<<7)
     if t in(2,6):break
 for k,r,c,a,b in((4,7,1,6,5),(4,0,2,2,3))if sd>0 else((116,119,4,118,117),(116,112,8,114,115)):
  if cr&c and B[r]==4*sd and not B[a]and not B[b]and(c&10==0 or not B[k-3])and not any(atk(x,sd<0)for x in(k,a,b)):ms.append(k|a<<7)
 return ms
def make(m):
 global cr,ep,sd
 f=m&127;t=m>>7&127;q=m>>14&7
 pc=B[f];c=B[t]
 B[f]=0
 if abs(pc)==1:
  e=t-sd*16
  if t==ep and not c:
   c=B[e];B[e]=0
  ep=e if abs(t-f)==32 else-1
  if q:pc=q*sd
 else:ep=-1
 if abs(pc)==6:
  K[sd<0]=t
  if abs(t-f)==2:
   rf=t+1 if t>f else t-2
   rt=t-1 if t>f else t+1
   B[rt]=B[rf];B[rf]=0
 B[t]=pc
 cr&=CK.get(f,15)&CK.get(t,15)
 sd=-sd
def srch(a,b,d,pl):
 global nd,B,cr,ep,sd,K
 nd+=1
 if nd>NB:raise X
 ck=atk(K[sd<0],sd<0)
 d+=ck*(pl<40)
 if d<=0:
  if pl<2:return ev()
  if not ck:
   st=ev()
   if st>=b:return b
   a=max(a,st)
  ms=[m for m in gen() if m>>14 or((B[m>>7&127]or(m>>7&127)==ep)and st+V[abs(B[m>>7&127])]+200>=a)]if not ck else gen()
 else:ms=gen()
 ms.sort(key=lambda m:-(abs(B[m>>7&127])*9+H[m&4095]//256))
 bs=-I
 for m in ms:
  Z=(B[:],cr,ep,sd,K[:])
  make(m)
  if atk(K[sd>0],sd>0):
   B,cr,ep,sd,K=Z;continue
  s=-srch(-b,-a,d-1,pl+1)
  B,cr,ep,sd,K=Z
  bs=max(bs,s)
  a=max(a,s)
  H[m&4095]+=d*d*(a>=b)
  if a>=b:return b if d<=0 else a
 if bs==-I:return pl-10**5 if ck else a*(d<=0)
 return bs if d>0 else a
def root():
 global nd,B,cr,ep,sd,K,H
 nd=0;H=[0]*4096
 ms=gen()
 sc={}
 bm=ms[0]
 try:
  for d in range(33):
   ms.sort(key=lambda m:-sc.get(m,0))
   bs=-I
   for m in ms:
    Z=(B[:],cr,ep,sd,K[:])
    make(m)
    if atk(K[sd>0],sd>0):
     B,cr,ep,sd,K=Z;sc[m]=-I;continue
    s=-srch(-I,I,d-1,1)
    if P.get(tuple(B),0)>1:s+=150-400*(s>=0)
    B,cr,ep,sd,K=Z
    sc[m]=s
    if s>bs:bs=s;bm=m
 except X:pass
 return bm
def uci(m):
 return chr(97+(m&7))+str(1+(m>>4&7))+chr(97+(m>>7&7))+str(1+(m>>11&7))+"q"*(m>>14>0)
def post(p,b):
 return json.load(u.urlopen(u.Request(E+p,data=json.dumps(b).encode())))
while(g:=post("/game",{}))["status"]>"done":
 while g["status"]=="your_move":
  B=[0]*128
  for i,p in enumerate([4,2,3,5,6,3,2,4]):B[i]=p;B[i+112]=-p;B[i+16]=1;B[i+96]=-1
  sd=1;cr=15;ep=-1;K=[4,116];P={}
  for mv in g["moves"]:
   f,t=[(int(mv[i+1])-1)*16+ord(mv[i])-97 for i in(0,2)]
   q="nbrq".find(mv[4])+2 if len(mv)>4 else 0
   make(f|t<<7|q<<14);P[tuple(B)]=P.get(tuple(B),0)+1
  z=uci(root())
  L=g["legal_moves"]
  g=post("/move",{"game":g["game"],"move":z if z in L else L[0]})
