# M1TR4M_Mat.py - M1TR4M: edicao de reserva "M1TR4M Mat" num so ficheiro
# (gerada pelo build; nao editar). Usa-se so se importar modulos entre
# programas nao funcionar no aparelho. Leva: 12 temas (n7 a7 g7 d7 n8 a8 g8 d8 n9 a9 g9 d9), 35 calculadoras.



_F = {}
_L = {}
_ED = 'Mat'


class _NS:
 pass


def _ns(n, *v):
 m = _NS()
 i = 0
 for k in n.split():
  setattr(m, k, v[i])
  i += 1
 return m


def _imp(n):
 m = _L.get(n)
 if m is None:
  f = _F.get(n)
  if f is None:
   raise ImportError("no module named '" + n + "'")
  m = f()
  _L[n] = m
 return m


_W = None


def _dz(s):
 global _W
 if _W is None:
  _W = _T.split('`')
 a = '`~$&#*Y'
 b = "!%'()+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXZ[]^_abcdefghijklmnopqrstuvwxyz{|}"
 k = len(b)
 n = len(a) * k
 for i in range(len(_W) - 1, -1, -1):
  if i < n:
   t = a[i // k] + b[i % k]
  else:
   j = i - n
   t = a[j // n] + a[j // k % len(a)] + b[j % k]
  s = s.replace(t, _W[i])
 return s



_T = "\xe2ngulo`\n\
Verifica\xe7\xe3o:`\xe3`\xe9`\xe7`\u221a`\xd7`\xb2`\n\
Erros a evitar:`Matem\xe1tica`n\xfamero`\n\
Objetivo:`\xe1`\n\
- Calcular`\n\
Resultado:`\n\
Interpreta`\n\
Enunciado:`\xf5es`\xb0`\u03b1`\u2248`\xed`\n\
Dados:`probabilidade`\u03c0`\n\
@F`expoente`de um`\xea`\n\
Resolu`\n\
@X`\n\
@S`\n\
@P`\n\
@D`multiplica`quadrado`com`\xba`o de`ncia`\u2713`dos`mediana`racionais`\n\
2.`\n\
1.`\u207b`\n\
Qual`para`\u20ac`\xf3`valor`semelhantes`\n\
3.`amplitude`\xfa`cleo|||AE`hipotenusa`altura`proporcionalidade`\xc2ngulo`circunfer`\u2223`\u21d4`diferen`\xb3`pontos`\n\
- Resolver`Quanto`reta`\n\
- Reconhecer`diagrama`ano,`\n\
@R`\n\
@L`\n\
@J`\n\
@C`\n\
@A`\u2074`constante`maior`percentagem`Multiplica`x =`uma`por`centro`soma`inscrito`duas`denominador`\u221e`.\
 Qual`casas decimais?`ou seja,`casos`que`dois`equa`intervalo`simplificar`inteiros`tri`m.m.c.`relativa`tem`Calcula`\n\
@E`\n\
- Escrever`adjacente`\u2264`\u2081`\n\
- Usar`dist\xe2`internos`A \u2229`primento`\n\
@T \xc1lgebra`o cient`lado`angulo`sen`logo`\u2260`\u2082`cerca de`solu`s de`rea`metro`resolver`mente\
 pro`mede`diagonal`= 2`produto`cateto`termo`base`coordenadas`quadrada`cos`meros`\u2265`\u2075`\n\
@O`u(n) =`sem reposi`oposto`peri`\n\
- Construir`est`inicial`entre`dividir`ano)`fatores`o sinal`externo`calcular`Probabilidades`tabela`m.d.c.`zima`\n\
>`gono`infinita`@V 1`\n\
@N`cada`dia`frequ`Teorema de Pit`cionalidade`\n\
- Aplicar`= 12`ponto`\n\
-`mesma`express`s e`classe`cm de`/ 2`fator`\u0394`anulamento do`acontecimento`o mesmo`a\
 partir`primeiro`substitui`a de`vetor`sempre`a e Medida`\n\
@T Geome`transla`|c_mgeo.ang`inversa`m-se os`divide`figuras`fra`\n\
Um`\n\
Falso:`mais`negativo`ordem`alternos`desconto`A \u222a`rtice`vale`per`pelo`imposs`fico`volume`semelhan`x +`o\
 resultado`ordena`Metade de`num`iguais`inteiro`e a`das`cao`aproximada`Resolve`pot`= 4`= 10`=\
 1`regular`\u2192`reflex`metade`Simplifica`\xe0`Escreve`\n\
4.`am-se`x \u2208`segmento`radicais`passa`em nota`rmula`raio`problemas`interno`na\
 origem`\u221b`conjunto-`Soma`(podes responder`Amplitude`(x -`par`C.S. =`correspondentes`imagem`finita`agudo|`\n\
Num`|c_m`prb.freq`terreno`|7|n`menor`igual`\xe2`Quadrado do bin`qual`ret`rvore`A\
 =`pol.pol`\u2077`\xc1`pendicular`menos`grau`medida`gera`escreve-se`de\
 extremo`cionais.`Relacionar`favor`outros`os da`do\
 1.`arco`turma`custa`conjun`circular`poss`mantissa`cilindro`verticalmente`\n\
@T`= a`= 360`grandezas`\u2076`= 3`rota`indeterminada`discriminante`a m`regras`= 9`=\
 5`consecutivos`Diferen`raiz`inverso`sombra`sforos`amplia`quartis`pol`resulta`veis.`o\
 se`geo.a`eixo`interquartil`gtr.iso`cm.`exp.eq1`escreve`equidistante`coes`fica.`de\
 da`centual`caixa`bolas`aumenta`Para`tangente`subtrair`Express`forma`f(x)`de sa`5 cm`cionais:`caminhos`Equa`B\
 =`0,15`\u2228`total`suplementar`\u207f`\u2070`rculo`\xb9`plementares`letra`lelas`sime`gnita`quando`e o`no\
 interior: semis`contr`concavidade`calcu`Distinguir`raz`12,"


def _m_c_mate():
 import math
 N=_imp('m1_nucleo')
 MS='\xb7'
 def nums(t,nm):
  out=[]
  for p in N.lst(t):
   out.append(N.num(p)[0])
  N.need(out,'Escreve '+nm+' separados por espa\xe7os')
  return out
 def lista(xs):
  return ' '.join([N.fmt(x)for x in xs])
 def med(xs):
  n=len(xs)
  h=n//2
  return xs[h]if n%2 else(xs[h-1]+xs[h])/2
 def quartis(xs):
  n=len(xs)
  h=n//2
  return(med(xs[:h]),med(xs[n-h:]))
 def percentil(xs,k):
  n=len(xs)
  p=k*n/100
  i=int(p+1e-09)
  if abs(p-i)<1e-09:
   return((xs[i-1]+xs[min(i,n-1)])/2 if i>0 else xs[0],p)
  return(xs[i],p)
 def modas(xs):
  vs=[]
  fs=[]
  for x in xs:
   if vs and vs[-1]==x:
    fs[-1]+=1
   else:
    vs.append(x)
    fs.append(1)
  m=max(fs)
  if len(vs)>1 and min(fs)==m:
   return([],m)
  return([vs[i]for i in range(len(vs))if fs[i]==m],m)
 def uni():
  return('Estat\xedstica de uma vari\xe1vel',[N.fld('Dados (ou valores, se h\xe1 frequ\xeancias)','','2 4 4 5 7 8 9 9 9 25','l'),N.fld('Frequ\xeancias absolutas (opcional)','','','t'),N.fld('Percentil k (opcional, 0 < k < 100)',
'','','o'),N.fld('Transforma\xe7\xe3o y = a x + b: a (opcional)','','','o'),N.fld('b (opcional)','','','o')],_uni)
 def _uni(v):
  xs=[p[0]for p in v[0]]
  if v[1]:
   fs=nums(v[1],'as frequ\xeancias')
   N.need(len(fs)==len(xs),'H\xe1 '+str(len(xs))+' valores e '+str(len(fs))+' frequ\xeancias')
   ys=[]
   for i in range(len(xs)):
    N.need(fs[i]>=0 and fs[i]==int(fs[i]),'As frequ\xeancias t\xeam de ser inteiros n\xe3o negativos')
    ys+=[xs[i]]*int(fs[i])
    N.need(len(ys)<=2000,'No m\xe1ximo 2000 dados')
   xs=ys
  xs.sort()
  n=len(xs)
  N.need(n>=2,'S\xe3o precisos pelo menos 2 dados')
  m=sum(xs)/n
  s2=sum([(x-m)**2 for x in xs])/(n-1)
  s=math.sqrt(s2)
  me=med(xs)
  q1,q3=quartis(xs)
  aiq=q3-q1
  mo,fm=modas(xs)
  o=['n = '+str(n)+(': '+lista(xs)if n<=30 else ' (ordenados: '+lista(xs[:5])+' ...)')]
  o+=['= M\xe9dia = soma / n = '+N.fmt(sum(xs))+' / '+str(n),'> M\xe9dia '+N.eq(m),'Moda: '+('n\xe3o h\xe1 (todos os valores com a mesma frequ\xeancia)'if not mo else lista(mo[:4])+(' ...'if len(mo)>4 else '')+' (frequ\xeancia '+str(fm)+')'),
'> Mediana '+N.eq(me),'> Q1 '+N.eq(q1)+' '+MS+' Q3 '+N.eq(q3)+' (medianas das metades'+(', sem a mediana)'if n%2 else ')'),'M\xednimo '+N.fmt(xs[0])+' '+MS+' m\xe1ximo '+N.fmt(xs[-1])+' '+MS+' amplitude '+N.fmt(xs[-1]-xs[0]),
'> AIQ = Q3 - Q1 '+N.eq(aiq),'= s\xb2 = soma dos (x - m\xe9dia)\xb2 / (n - 1)','> Vari\xe2ncia '+N.eq(s2)+' '+MS+' desvio padr\xe3o s '+N.eq(s)]
  lo,hi=(q1-1.5*aiq,q3+1.5*aiq)
  out=[x for x in xs if x<lo or x>hi]
  o.append('Barreiras: Q1 - 1,5 AIQ = '+N.fmt(lo)+' e Q3 + 1,5 AIQ = '+N.fmt(hi))
  o.append('Outliers: '+lista(out[:8])+(' ...'if len(out)>8 else '')if out else 'Sem outliers.')
  if out:
   ok=[x for x in xs if lo<=x<=hi]
   m2=sum(ok)/len(ok)
   o.append('Sem os outliers: m\xe9dia '+N.eq(m2)+', mediana '+N.eq(med(ok))+' (a mediana \xe9 mais resistente).')
  if v[2]is not None:
   k=v[2][0]
   N.need(0<k<100,'O percentil k tem de estar entre 0 e 100')
   pk,p=percentil(xs,k)
   o.append('P'+N.fmt(k)+': '+N.fmt(k)+'% de '+str(n)+' = '+N.fmt(p)+(' (inteiro: m\xe9dia de 2 dados)'if abs(p-round(p))<1e-09 else ' (posi\xe7\xe3o seguinte)')+'; P'+N.fmt(k)+' '+N.eq(pk))
   if k in(25,75)and abs(pk-(q1 if k==25 else q3))>1e-12:
    o.append('(Aqui P'+N.fmt(k)+' \u2260 Q'+('1'if k==25 else '3')+': as duas regras podem dar valores diferentes.)')
  if v[3]is not None or v[4]is not None:
   a=v[3][0]if v[3]is not None else 1.0
   b=v[4][0]if v[4]is not None else 0.0
   o+=['Com y = '+N.fmt(a)+'x + '+N.fmt(b)+':',' m\xe9dia '+N.eq(a*m+b)+'; mediana '+N.eq(a*me+b),' s '+N.eq(abs(a)*s)+'; AIQ '+N.eq(abs(a)*aiq)+' (o b n\xe3o muda a dispers\xe3o)']
  wl=min([x for x in xs if x>=lo])
  wh=max([x for x in xs if x<=hi])
  d=(xs[-1]-xs[0])*0.1 or 1.0
  sg=[(q1,0.7,q3,0.7),(q1,1.3,q3,1.3),(q1,0.7,q1,1.3),(q3,0.7,q3,1.3),(me,0.7,me,1.3),(wl,1,q1,1),(q3,1,wh,1),(wl,0.85,wl,1.15),(wh,0.85,wh,1.15)]
  its=[('s',sg,2)]
  if out:
   its.append(('p',[(x,1)for x in out],5))
  gr=('Diagrama de extremos e quartis',its,xs[0]-d,xs[-1]+d,0,2,'Q1 '+N.fmt(q1)+' '+MS+' Me '+N.fmt(me)+' '+MS+' Q3 '+N.fmt(q3)+(' '+MS+' pontos: outliers'if out else ''))
  st=('Mediana: valor do meio dos dados ordenados (m\xe9dia dos dois do meio, se n for par).\nQ1 e Q3: medianas das metades de baixo e de cima.\nPk: k% de n; n\xe3o inteiro: posi\xe7\xe3o seguinte; inteiro: '
'm\xe9dia desse dado e do seguinte.\nOutliers: abaixo de Q1 - 1,5 AIQ ou acima de Q3 + 1,5 AIQ (confirma a regra do teu manual).\nDesvio padr\xe3o amostral: divide-se por n - 1.')
  return('\n'.join(o),st,m,'',gr)
 def cls():
  return('Dados em classes e histograma',[N.fld('Limites das classes','','0 10 20 30 40','l'),N.fld('Frequ\xeancias das classes (ou vazio)','','3 7 8 2','t'),N.fld('Dados brutos (se n\xe3o h\xe1 frequ\xeancias)',
'','','t')],_cls)
 def _cls(v):
  L=[p[0]for p in v[0]]
  k=len(L)-1
  N.need(k>=1,'Escreve pelo menos 2 limites (ex.: 0 10 20)')
  for i in range(k):
   N.need(L[i+1]>L[i],'Os limites t\xeam de estar por ordem crescente')
  if v[1]:
   N.need(not v[2],'Escreve as frequ\xeancias ou os dados brutos, n\xe3o os dois')
   fs=nums(v[1],'as frequ\xeancias')
   N.need(len(fs)==k,'H\xe1 '+str(k)+' classes e '+str(len(fs))+' frequ\xeancias')
   for f in fs:
    N.need(f>=0 and f==int(f),'As frequ\xeancias t\xeam de ser inteiros n\xe3o negativos')
  else:
   N.need(v[2],'Escreve as frequ\xeancias ou os dados brutos')
   xs=nums(v[2],'os dados')
   fs=[0]*k
   for x in xs:
    N.need(L[0]<=x<=L[-1],'O dado '+N.fmt(x)+' est\xe1 fora das classes')
    i=0
    while i<k-1 and x>=L[i+1]:
     i+=1
    fs[i]+=1
  n=sum(fs)
  N.need(n>0,'N\xe3o h\xe1 dados')
  hs=[L[i+1]-L[i]for i in range(k)]
  iguais=max(hs)-min(hs)<1e-09*max(hs)
  pm=[(L[i]+L[i+1])/2 for i in range(k)]
  o=['Classe: ponto m\xe9dio; ni; fi; Ni; Fi']
  F=0
  for i in range(k):
   F+=fs[i]
   o.append('['+N.fmt(L[i])+', '+N.fmt(L[i+1])+(']'if i==k-1 else '[')+': '+N.fmt(pm[i])+'; '+str(int(fs[i]))+'; '+N.fmt(100*fs[i]/n,0,1)+'%; '+str(int(F))+'; '+N.fmt(100*F/n,0,1)+'%')
  m=sum([pm[i]*fs[i]for i in range(k)])/n
  o+=['n = '+str(int(n)),'> M\xe9dia (com os pontos m\xe9dios) '+N.eq(m)]
  if n>1:
   s=math.sqrt(sum([fs[i]*(pm[i]-m)**2 for i in range(k)])/(n-1))
   o.append('> Desvio padr\xe3o (aproximado) '+N.eq(s))
  dens=[fs[i]/hs[i]for i in range(k)]
  dm=max(dens)
  o.append('Classe modal: '+', '.join(['['+N.fmt(L[i])+', '+N.fmt(L[i+1])+'['for i in range(k)if dens[i]==dm]))
  F=0
  for i in range(k):
   F+=fs[i]
   if 2*F==n and i<k-1:
    o.append('A frequ\xeancia acumulada \xe9 50% no fim de ['+N.fmt(L[i])+', '+N.fmt(L[i+1])+'[: a mediana fica no limite '+N.fmt(L[i+1])+'.')
    break
   if 2*F>n:
    o.append('Classe mediana: ['+N.fmt(L[i])+', '+N.fmt(L[i+1])+('['if i<k-1 else ']')+' (a frequ\xeancia acumulada passa os 50%)')
    break
  if not iguais:
   o.append('Classes com amplitudes diferentes: no histograma, a altura \xe9 ni / amplitude.')
  ys=fs if iguais else dens
  sg=[]
  for i in range(k):
   sg+=[(L[i],0,L[i],ys[i]),(L[i],ys[i],L[i+1],ys[i]),(L[i+1],ys[i],L[i+1],0)]
  d=(L[-1]-L[0])*0.08
  rs=[(L[i],ys[i],str(int(fs[i])))for i in range(k)]
  gr=('Histograma',[('s',sg,4),('t',rs,0)],L[0]-d,L[-1]+d,0,max(ys)*1.25,'limites '+' '.join([N.fmt(x)for x in L])+'; '+'n\xfameros: ni'+(''if iguais else ' (altura: ni / amplitude)'))
  st=('ni: frequ\xeancia absoluta; fi = ni / n; Ni e Fi: acumuladas.\nClasses [a, b[: o limite de cima fica na classe seguinte (a \xfaltima \xe9 fechada).\nM\xe9dia de dados agrupados: usa os pontos m\xe9dio'
's (\xe9 um valor aproximado).')
  return('\n'.join(o),st,m,'',gr)
 def cauleset(t,dec,nm):
  xs=nums(t,nm)
  out=[]
  for x in xs:
   N.need(x>=0,'O caule-e-folhas desta calculadora s\xf3 aceita valores n\xe3o negativos')
   y=x*10 if dec else x
   N.need(abs(y-round(y))<1e-09,'Os dados t\xeam de ter '+('no m\xe1ximo uma casa decimal'if dec else 'ser inteiros (usa as d\xe9cimas como folhas)'))
   y=int(round(y))
   out.append((y//10,y%10))
  out.sort()
  return(xs,out)
 def caule():
  return('Caule-e-folhas',[N.fld('Dados A','','12 15 21 23 23 30 38 41','t'),N.fld('Dados B (opcional, diagrama duplo)','','','t'),N.fld('Folhas','','','c',['unidades (caule: dezenas)','d\xe9cimas (caule: unidades)'])],
_caule)
 def _caule(v):
  ta,tb,dec=v
  xa,a=cauleset(ta,dec,'os dados A')
  xb,b=cauleset(tb,dec,'os dados B')if tb else([],[])
  cs=[c for c,f in a+b]
  lo,hi=(min(cs),max(cs))
  N.need(hi-lo<=40,'Demasiados caules: usa outra unidade para as folhas')
  o=[]
  if b:
   rows=[]
   for c in range(lo,hi+1):
    fa=[str(f)for cc,f in a if cc==c]
    fa.reverse()
    rows.append((' '.join(fa),str(c),' '.join([str(f)for cc,f in b if cc==c])))
   w=max([len(r[0])for r in rows])
   wc=max([len(r[1])for r in rows])
   for r in rows:
    o.append(' '*(w-len(r[0]))+r[0]+' | '+' '*(wc-len(r[1]))+r[1]+' | '+r[2])
   o.append('Folhas de A \xe0 esquerda, de B \xe0 direita.')
  else:
   wc=len(str(hi))
   for c in range(lo,hi+1):
    s=str(c)
    o.append(' '*(wc-len(s))+s+' | '+' '.join([str(f)for cc,f in a if cc==c]))
  c0,f0=(a+b)[0]
  o.append('Legenda: '+str(c0)+' | '+str(f0)+' = '+(str(c0)+','+str(f0)if dec else str(c0*10+f0)))
  for nm,xs in(('A',xa),('B',xb)):
   if xs:
    ys=sorted(xs)
    o.append(nm+': n = '+str(len(ys))+', m\xednimo '+N.fmt(ys[0])+', mediana '+N.fmt(med(ys))+', m\xe1ximo '+N.fmt(ys[-1]))
  st='Caule: os algarismos da esquerda; folha: o \xfaltimo algarismo.\nAs folhas escrevem-se por ordem crescente a partir do caule.\nO diagrama mostra a forma da distribui\xe7\xe3o sem perder os dados.'
  return('\n'.join(o),st,None,'')
 return _ns('N quartis percentil uni cls caule',N,quartis,percentil,uni,cls,caule)


_F['c_mate'] = _m_c_mate


def _m_c_matf():
 import math
 N=_imp('m1_nucleo')
 X=N.X
 INF='+\u221e'
 MINF='-\u221e'
 UN=' \u222a '
 def ex(v):
  s,ok=N.fmt2(v,0,-1)
  if ok:
   return s
  e=N.exact(v)
  return e if e is not None else s
 def lista(xs):
  ts=[ex(x)for x in xs]
  return sep(*ts).join(ts)
 def sep(*ts):
  for t in ts:
   if ','in t:
    return '; '
  return ', '
 def iv(a,b,ca=0,cb=0):
  sa=MINF if a is None else ex(a)
  sb=INF if b is None else ex(b)
  return('['if ca and a is not None else ']')+sa+sep(sa,sb)+sb+(']'if cb and b is not None else '[')
 def lin(m,b):
  if m==0:
   return ex(b)
  c=ex(abs(m))
  if '/'in c:
   c='('+c+')'
  s=(''if m>0 else '-')+(''if abs(m)==1 else c)+'x'
  if b>0:
   s+=' + '+ex(b)
  elif b<0:
   s+=' - '+ex(-b)
  return s
 def safe(f,x):
  try:
   y=f(x)
   if y!=y or abs(y)>1e+300:
    return None
   return y
  except Exception:
   return None
 def zeros(f,a,b,n=400):
  h=(b-a)/n
  xs=[a+i*h for i in range(n+1)]
  ys=[safe(f,x)for x in xs]
  vs=[abs(y)for y in ys if y is not None]
  if not vs:
   return([],0)
  sc=max(vs)or 1.0
  zs=[]
  for i in range(n+1):
   y=ys[i]
   if y is None:
    continue
   if abs(y)<=1e-12*max(1.0,sc):
    zs.append(xs[i])
    continue
   if i<n and ys[i+1]is not None and(y*ys[i+1]<0):
    lo,hi=(xs[i],xs[i+1])
    for k in range(60):
     m=(lo+hi)/2
     fm=safe(f,m)
     if fm is None:
      break
     if(fm<0)==(y<0):
      lo=m
     else:
      hi=m
    zs.append((lo+hi)/2)
   elif 0<i<n and ys[i-1]is not None and(ys[i+1]is not None)and(abs(y)<=abs(ys[i-1]))and(abs(y)<=abs(ys[i+1]))and(abs(y)<0.001*sc):
    lo,hi=(xs[i-1],xs[i+1])
    for k in range(80):
     m1=lo+(hi-lo)/3
     m2=hi-(hi-lo)/3
     if abs(safe(f,m1)or 0)<abs(safe(f,m2)or 0):
      hi=m2
     else:
      lo=m1
    xm=(lo+hi)/2
    if abs(safe(f,xm)or 1)<1e-09*max(1.0,sc):
     zs.append(xm)
  out=[]
  for z in sorted(zs):
   if not out or abs(z-out[-1])>1e-06*(b-a):
    out.append(z)
  return([limpa(z)for z in out],len(vs)<n+1)
 def limpa(z):
  r=round(z*1000000.0)/1000000.0
  return r if abs(r-z)<1e-09 else z
 def extremos(f,a,b,n=400):
  h=(b-a)/n
  xs=[a+i*h for i in range(n+1)]
  ys=[safe(f,x)for x in xs]
  out=[]
  for i in range(1,n):
   y0,y1,y2=(ys[i-1],ys[i],ys[i+1])
   if y0 is None or y1 is None or y2 is None:
    continue
   mx=y1>y0 and y1>=y2
   mn=y1<y0 and y1<=y2
   if not(mx or mn):
    continue
   lo,hi=(xs[i-1],xs[i+1])
   for k in range(60):
    m1=lo+(hi-lo)/3
    m2=hi-(hi-lo)/3
    f1,f2=(safe(f,m1),safe(f,m2))
    if f1 is None or f2 is None:
     break
    if(f1>f2)==mx:
     hi=m2
    else:
     lo=m1
   xm=(lo+hi)/2
   ym=safe(f,xm)
   xr=round(xm*1000000.0)/1000000.0
   yr=safe(f,xr)
   if yr is not None and ym is not None and(abs(xr-xm)<1e-06)and((yr-ym)*(1 if mx else-1)>=-1e-12*max(1.0,abs(ym))):
    xm,ym=(xr,yr)
   out.append((mx,xm,ym))
  return out
 def janela(f,a,b):
  ys=[safe(f,a+(b-a)*i/80)for i in range(81)]
  ys=sorted([y for y in ys if y is not None])
  N.need(ys,'A fun\xe7\xe3o n\xe3o tem valores neste intervalo')
  lo,hi=(ys[len(ys)//20],ys[len(ys)*19//20])
  d=(hi-lo)*0.15 or 1.0
  return(min(lo,0.0)-d,max(hi,0.0)+d)
 def fx():
  return('Fun\xe7\xe3o escrita por ti',[N.fld('f(x) =','','x^2 - 4','t'),N.fld('Intervalo: de','','-5'),N.fld('at\xe9','','5'),N.fld('Calcular f em x = (opcional)','','','o')],_fx)
 def _fx(v):
  s,a,b,x0=v
  code=N.comp(s)
  a,b=(a[0],b[0])
  N.need(b>a,'O intervalo tem de ter a < b')
  def f(x):
   return N.ev(code,x)
  o=['f(x) = '+s]
  r=None
  if x0 is not None:
   y=safe(f,x0[0])
   N.need(y is not None,'f n\xe3o est\xe1 definida em x = '+ex(x0[0]))
   o.append('> f('+ex(x0[0])+') '+N.rhs(y))
   r=y
  o.append('Tabela:')
  for i in range(5):
   x=a+(b-a)*i/4
   y=safe(f,x)
   o.append('x = '+ex(x)+': '+('sem valor'if y is None else 'f(x) '+N.rhs(y)))
  zs,falha=zeros(f,a,b)
  if falha:
   o.append('! f n\xe3o est\xe1 definida em parte do intervalo.')
  o.append('Zeros em '+iv(a,b,1,1)+': '+(lista(zs)if zs else 'nenhum'))
  if not falha:
   cs=[a]+zs+[b]
   pos,neg=([],[])
   for i in range(len(cs)-1):
    if cs[i+1]-cs[i]<1e-12:
     continue
    y=safe(f,(cs[i]+cs[i+1])/2)
    if y is None:
     continue
    (pos if y>0 else neg).append(iv(cs[i],cs[i+1]))
   o.append('f > 0 em '+(UN.join(pos)if pos else '\u2205')+'; f < 0 em '+(UN.join(neg)if neg else '\u2205'))
  for mx,xm,ym in extremos(f,a,b):
   o.append(('M\xe1ximo'if mx else 'M\xednimo')+' relativo '+N.rhs(ym)+' em x '+N.rhs(xm))
  lo,hi=janela(f,a,b)
  g=('f(x) = '+s,[('f',f,4)],a,b,lo,hi,'f(x) = '+s)
  st='Zeros e extremos procurados numericamente no intervalo escolhido (aproximados; a forma exata aparece quando \xe9 reconhecida).\nMuda o intervalo para ver mais do gr\xe1fico.'
  return('\n'.join(o),st,r,'',g)
 def afim():
  return('Fun\xe7\xe3o afim',[N.fld('Declive m (opcional)','','','o'),N.fld('Ordenada na origem b (opcional)','','','o'),N.fld('Ponto A (x y), opcional','','1 3','t'),N.fld('Ponto B (x y), opcional','',
'3 7','t')],_afim)
 def ponto(t,nm):
  ps=N.lst(t)
  N.need(len(ps)==2,'Escreve as duas coordenadas de '+nm+', por exemplo 2 3')
  return(N.num(ps[0])[0],N.num(ps[1])[0])
 def _afim(v):
  m,b,ta,tb=v
  A=ponto(ta,'A')if ta else None
  B=ponto(tb,'B')if tb else None
  o=[]
  if A and B:
   N.need(m is None and b is None,'Com dois pontos, deixa m e b vazios')
   N.need(A[0]!=B[0],'Os pontos t\xeam a mesma abcissa: a reta \xe9 vertical (x = '+ex(A[0])+') e n\xe3o \xe9 uma fun\xe7\xe3o')
   m=(B[1]-A[1])/(B[0]-A[0])
   b=A[1]-m*A[0]
   o+=['= m = (yB - yA) / (xB - xA)','m '+N.rhs(m),'b = yA - m xA '+N.rhs(b)]
  elif m is not None and A and(b is None):
   m=m[0]
   b=A[1]-m*A[0]
   o+=['= b = yA - m xA','b '+N.rhs(b)]
  elif b is not None and A and(m is None):
   b=b[0]
   N.need(A[0]!=0,'Com b e um ponto de abcissa 0 n\xe3o d\xe1 para saber o declive')
   m=(A[1]-b)/A[0]
   o+=['= m = (yA - b) / xA','m '+N.rhs(m)]
  elif m is not None and b is not None and(not A):
   m,b=(m[0],b[0])
  else:
   N.need(0,'D\xe1 m e b, ou m e um ponto, ou b e um ponto, ou dois pontos')
  o.append('> f(x) = '+lin(m,b))
  if m==0:
   o+=['Fun\xe7\xe3o constante: D\u2032f = {'+ex(b)+'}.','Zeros: '+('todos os x'if b==0 else 'nenhum')+'.']
  else:
   z=-b/m
   o+=['Zero: x = -b / m '+N.rhs(z),'f > 0 em '+(iv(z,None)if m>0 else iv(None,z))+'; f < 0 em '+(iv(None,z)if m>0 else iv(z,None)),('Crescente'if m>0 else 'Decrescente')+' em \u211d (m '+('> 0'if m>0 else '< 0')+'); D\u2032f = \u211d']
  c=0.0 if m==0 else-b/m
  w=max(5.0,abs(c)*1.5,abs(b)/max(abs(m),0.1))
  g=('f(x) = '+lin(m,b),[('f',lambda x:m*x+b,4),('p',[p for p in(A,B)if p],5)],c-w,c+w,min(-w,b-w),max(w,b+w),'y = '+lin(m,b))
  st='Declive: m = (y2 - y1) / (x2 - x1); ordenada na origem: b = f(0).\nm > 0: crescente; m < 0: decrescente; m = 0: constante.'
  return('\n'.join(o),st,m,'',g)
 def ramos():
  return('Fun\xe7\xe3o definida por ramos',[N.fld('Ramo 1: f(x) =','','-x','t'),N.fld('Fronteira a','','0'),N.fld('Ramo 2: f(x) =','','x^2','t'),N.fld('Fronteira c (s\xf3 com 3 ramos)','','','o'),N.fld('Ramo 3: f(x) = (opcional)',
'','','t'),N.fld('Cada fronteira pertence ao ramo','','','c',['da direita (x \u2265 a)','da esquerda (x \u2264 a)']),N.fld('Calcular f em x = (opcional)','','','o')],_ramos)
 def _ramos(v):
  r1,a,r2,c,r3,k,x0=v
  N.need(r1 and r2,'Escreve pelo menos os dois primeiros ramos')
  a=a[0]
  cs=[N.comp(r1),N.comp(r2)]
  fs=[a]
  nm=[r1,r2]
  if c is not None or r3:
   N.need(c is not None and r3,'Com 3 ramos, escreve a fronteira c e o 3.\xba ramo')
   N.need(c[0]>a,'A fronteira c tem de ser maior do que a')
   fs.append(c[0])
   cs.append(N.comp(r3))
   nm.append(r3)
  esq=k==1
  def qual(x):
   for i in range(len(fs)):
    if x<fs[i]or(esq and x==fs[i]):
     return i
   return len(fs)
  def f(x):
   return N.ev(cs[qual(x)],x)
  lt,le,ge,gt=(' < ',' \u2264 ',' \u2265 ',' > ')
  o=['f(x) =']
  for i in range(len(cs)):
   if i==0:
    cond='x'+(le if esq else lt)+ex(fs[0])
   elif i==len(cs)-1:
    cond='x'+(gt if esq else ge)+ex(fs[-1])
   else:
    cond=ex(fs[i-1])+(lt if esq else le)+'x'+(le if esq else lt)+ex(fs[i])
   o.append('  '+nm[i]+', se '+cond)
  r=None
  if x0 is not None:
   y=safe(f,x0[0])
   N.need(y is not None,'f n\xe3o est\xe1 definida em x = '+ex(x0[0]))
   o.append('> f('+ex(x0[0])+') '+N.rhs(y)+' (ramo '+str(qual(x0[0])+1)+')')
   r=y
  for i in range(len(fs)):
   e=safe(lambda x:N.ev(cs[i],x),fs[i])
   d=safe(lambda x:N.ev(cs[i+1],x),fs[i])
   if e is None or d is None:
    continue
   o.append('Em x = '+ex(fs[i])+': ramo '+str(i+1)+' d\xe1 '+ex(e)+', ramo '+str(i+2)+' d\xe1 '+ex(d)+(' (cont\xednua)'if abs(e-d)<1e-12 else ' (salto)'))
  lo_x,hi_x=(fs[0]-10,fs[-1]+10)
  zs,fa=zeros(f,lo_x,hi_x,800)
  o.append('Zeros em '+iv(lo_x,hi_x,1,1)+': '+(lista(zs)if zs else 'nenhum'))
  its=[]
  bs=[lo_x]+fs+[hi_x]
  for i in range(len(cs)):
   def g(x,i=i):
    N.need(bs[i]<=x<=bs[i+1],'')
    return N.ev(cs[i],x)
   its.append(('f',g,(4,5,6)[i]))
  y0,y1=janela(f,lo_x,hi_x)
  gr=('Fun\xe7\xe3o por ramos',its,lo_x,hi_x,y0,y1,'cada cor \xe9 um ramo')
  st='Para calcular f(x), escolhe-se primeiro o ramo a que x pertence.\nEqua\xe7\xf5es: resolve-se ramo a ramo e s\xf3 se ficam as solu\xe7\xf5es que est\xe3o no intervalo desse ramo.'
  return('\n'.join(o),st,r,'',gr)
 return _ns('N X ex zeros limpa extremos fx afim ponto ramos',N,X,ex,zeros,limpa,extremos,fx,afim,ponto,ramos)


_F['c_matf'] = _m_c_matf


def _m_c_matq():
 import math
 N=_imp('m1_nucleo')
 X=N.X
 INF='+\u221e'
 MINF='-\u221e'
 def nr(n,d):
  g=N.gcd(n,d)or 1
  if d<0:
   n,d=(-n,-d)
  return(n//g,d//g)
 def rat(x):
  return N.frac(x,100000)
 def radd(a,b):
  return nr(a[0]*b[1]+b[0]*a[1],a[1]*b[1])
 def rmul(a,b):
  return nr(a[0]*b[0],a[1]*b[1])
 def rs(a):
  return N.fstr(a[0],a[1])
 def rv(a):
  return 1.0*a[0]/a[1]
 def num(x,ex=None):
  if ex is not None:
   return ex
  return N.fmt(x)
 def coef(c,first=0,var='x\xb2'):
  v=rv(c)if isinstance(c,tuple)else c
  if v==0:
   return ''
  s=rs((abs(c[0]),c[1]))if isinstance(c,tuple)else N.fmt(abs(v))
  if '/'in s and var:
   s='('+s+')'
  if s=='1'and var:
   s=''
  sg='-'if v<0 else ''if first else '+'
  return(sg+(''if first else ' ')if not first else sg)+s+var
 def poly(a,b,c):
  t=[x for x in(coef(a,1,'x\xb2'),coef(b,0,'x'),coef(c,0,''))if x]
  s=t[0]
  for x in t[1:]:
   s=s+' '+x
  return s.replace('+ -','- ')
 def roots(a,b,c,ra,rb,rc):
  d=b*b-4*a*c
  ex=ra is not None and rb is not None and(rc is not None)
  dt=rs(radd(rmul(rb,rb),rmul((-4,1),rmul(ra,rc))))if ex else N.fmt(d)
  if ex:
   D=radd(rmul(rb,rb),rmul((-4,1),rmul(ra,rc)))
   d=rv(D)
  if d<0:
   return([],d,dt)
  if not ex:
   if d==0:
    return([(-b/(2*a),None)],d,dt)
   s=math.sqrt(d)
   r=sorted([(-b-s)/(2*a),(-b+s)/(2*a)])
   return([(r[0],None),(r[1],None)],d,dt)
  P=nr(-rb[0]*ra[1],2*rb[1]*ra[0])
  if D[0]==0:
   return([(rv(P),rs(P))],0.0,dt)
  k,m=N.rad(D[0]*D[1])
  Q=nr(k*ra[1],D[1]*2*abs(ra[0]))
  Q=(abs(Q[0]),Q[1])
  if m==1:
   r1=radd(P,(-Q[0],Q[1]))
   r2=radd(P,Q)
   return([(rv(r1),rs(r1)),(rv(r2),rs(r2))],d,dt)
  L=P[1]*Q[1]//N.gcd(P[1],Q[1])
  A=P[0]*L//P[1]
  B=Q[0]*L//Q[1]
  g=N.gcd(N.gcd(A,B),L)
  A,B,L=(A//g,B//g,L//g)
  sq=(''if B==1 else str(B))+'\u221a'+str(m)
  out=[]
  for sg in(-1,1):
   if A==0:
    t=('-'if sg<0 else '')+sq
   else:
    t=str(A)+(' - 'if sg<0 else ' + ')+sq
   if L!=1:
    t='('+t+')/'+str(L)if A!=0 else t+'/'+str(L)
   out.append(((A+sg*B*math.sqrt(m))/L,t))
  out.sort(key=lambda x:x[0])
  return(out,d,dt)
 def sep(*ts):
  for t in ts:
   if ','in t:
    return '; '
  return ', '
 def pt(a,b):
  return '('+a+sep(a,b)+b+')'
 def iv(a,b,ca,cb):
  sa=MINF if a is None else a
  sb=INF if b is None else b
  return('['if ca and a is not None else ']')+sa+sep(sa,sb)+sb+(']'if cb and b is not None else '[')
 def reads(v):
  a,b,c=(v[0][0],v[1][0],v[2][0])
  ra=rat(a)
  rb=rat(b)
  rc=rat(c)
  return(a,b,c,ra,rb,rc)
 def fields():
  return[N.fld('a (coeficiente de x\xb2)','','1'),N.fld('b (coeficiente de x)','','0'),N.fld('c (termo independente)','','0')]
 def window(a,b,c,zs):
  h=-b/(2*a)if a else 0
  k=c-b*b/(4*a)if a else c
  if zs:
   s=max([abs(z[0]-h)for z in zs])
  else:
   s=math.sqrt(abs(k/a))if a else 1.0
  w=max(1.0,1.6*s)
  x0=h-w
  x1=h+w
  ys=[a*x*x+b*x+c for x in(x0,x1,h)]
  y0=min(ys+[0])
  y1=max(ys+[0])
  dy=(y1-y0)*0.1 or 1.0
  return(x0,x1,y0-dy,y1+dy)
 def q2():
  return('Equa\xe7\xe3o do 2.\xba grau',fields(),_q2)
 def lin(b,c,rb,rc):
  if b==0:
   return 'a = 0 e b = 0: n\xe3o \xe9 uma equa\xe7\xe3o do 1.\xba nem do 2.\xba grau ('+('imposs\xedvel'if c!=0 else 'poss\xedvel e '+'indeterminada')+').'
  x=-c/b
  ex=rs(nr(-rc[0]*rb[1],rc[1]*rb[0]))if rb and rc else None
  r=N.rhs(x)
  if ex is not None and '= '+ex not in r:
   r='= '+ex+' '+r
  return 'a = 0: a equa\xe7\xe3o \xe9 do 1.\xba grau.\n= x = -c / b\n> x '+r
 def _q2(v):
  a,b,c,ra,rb,rc=reads(v)
  if a==0:
   return(lin(b,c,rb,rc),'',None,'')
  zs,d,dt=roots(a,b,c,ra,rb,rc)
  o=['f(x) = '+poly(ra or a,rb or b,rc or c),'= \u0394 = b\xb2 - 4ac = '+dt]
  if d>0:
   o.append('\u0394 > 0: dois zeros')
  elif d==0:
   o.append('\u0394 = 0: um zero (duplo)')
  else:
   o.append('\u0394 < 0: n\xe3o h\xe1 zeros (a equa\xe7\xe3o \xe9 imposs\xedvel em \u211d)')
  if zs:
   o.append('= x = (-b \xb1 \u221a\u0394) / (2a)')
   o.append('> '+' \u2228 '.join(['x = '+z[1]if z[1]is not None else 'x '+N.eq(z[0])for z in zs]))
   if zs[0][1]is not None and '\u221a'in zs[0][1]:
    o.append('  ('+' \u2228 '.join(['x '+N.AP+' '+N.fmt(z[0])for z in zs])+')')
   ts=[num(z[0],z[1])for z in zs]
   o.append('C.S. = {'+sep(*ts).join(ts)+'}')
  else:
   o.append('C.S. = \u2205')
  h=-b/(2*a)
  k=c-b*b/(4*a)
  hx=kx=None
  if ra and rb and rc:
   H=nr(-rb[0]*ra[1],2*rb[1]*ra[0])
   K=radd(rc,rmul((-1,1),rmul(rmul(rb,rb),nr(ra[1],4*ra[0]))))
   hx,kx=(rs(H),rs(K))
   h,k=(rv(H),rv(K))
  sh=num(h,hx)
  sk=num(k,kx)
  up=a>0
  o+=['V\xe9rtice: V'+pt(sh,sk),'Eixo de simetria: x = '+sh,'Concavidade voltada para '+('cima'if up else 'baixo')+' (a '+('>'if up else '<')+' 0)',('M\xednimo'if up else 'M\xe1ximo')+': '+sk+' (em x = '+sh+')',
'D\u2032f = '+(iv(sk,None,1,0)if up else iv(None,sk,0,1)),('Decrescente'if up else 'Crescente')+' em '+iv(None,sh,0,1)+'; '+('crescente'if up else 'decrescente')+' em '+iv(sh,None,1,0)]
  if hx is not None:
   sa=''if ra==(1,1)else '-'if ra==(-1,1)else rs(ra)if ra[1]==1 else '('+rs(ra)+')'
   if H[0]==0:
    fc=sa+'x\xb2'
   else:
    fc=sa+'(x '+('- '+rs(H)if H[0]>0 else '+ '+rs((-H[0],H[1])))+')\xb2'
   if K[0]!=0:
    fc=fc+(' + 'if K[0]>0 else ' - ')+rs((abs(K[0]),K[1]))
   o.append('Forma can\xf3nica: f(x) = '+fc)
  o.append(sign(a,zs))
  x0,x1,y0,y1=window(a,b,c,zs)
  g=('f(x) = '+poly(ra or a,rb or b,rc or c),[('f',lambda x:a*x*x+b*x+c,2),('p',[(z[0],0)for z in zs]+[(h,k)],5)],x0,x1,y0,y1,'pontos: zeros e v\xe9rtice')
  st='F\xf3rmula resolvente: x = (-b \xb1 \u221a(b\xb2 - 4ac)) / (2a).\nV\xe9rtice: x = -b/(2a) e y = f(-b/(2a)).\nNa forma a(x - h)\xb2 + k, o v\xe9rtice \xe9 (h; k).'
  return('\n'.join(o),st,zs[0][0]if zs else None,'',g)
 def sign(a,zs):
  up=a>0
  p,n=('positiva','negativa')if up else('negativa','positiva')
  t=[num(z[0],z[1])for z in zs]
  if len(zs)==2:
   return 'Sinal: '+p+' em '+iv(None,t[0],0,0)+' \u222a '+iv(t[1],None,0,0)+'; '+n+' em '+iv(t[0],t[1],0,0)+'; nula em '+t[0]+' e '+t[1]
  if len(zs)==1:
   return 'Sinal: '+p+' em \u211d \\ {'+t[0]+'}; nula em '+t[0]
  return 'Sinal: '+p+' em \u211d (sem zeros)'
 TT=('g(x) = f(x - a)','g(x) = f(x) + b','g(x) = c '+X+' f(x)','g(x) = f(x - a) + b')
 return _ns('N X num poly q2 TT',N,X,num,poly,q2,TT)


_F['c_matq'] = _m_c_matq


def _m_c_matr():
 import math
 N=_imp('m1_nucleo')
 X=N.X
 MS='\xb7'
 G=math.pi/180
 NOT={0:('0','1','0'),30:('1/2','\u221a3/2','\u221a3/3'),45:('\u221a2/2','\u221a2/2','1'),60:('\u221a3/2','1/2','\u221a3'),90:('1','0',None)}
 def ex(v):
  s,ok=N.fmt2(v,0,-1)
  if ok:
   return s
  e=N.exact(v)
  return e if e is not None else s
 def gr(v):
  s,ok=N.fmt2(v,0,1)
  return('= 'if ok else N.AP+' ')+s+'\xb0'
 def janela(ps):
  xs=[p[0]for p in ps]
  ys=[p[1]for p in ps]
  x0,x1,y0,y1=(min(xs),max(xs),min(ys),max(ys))
  w=max(x1-x0,2.1*(y1-y0))*1.3 or 1.0
  cx,cy=((x0+x1)/2,(y0+y1)/2)
  return(cx-w/2,cx+w/2,cy-w/4.2,cy+w/4.2)
 def desenho(t,A,B,C,nomes,leg):
  x0,x1,y0,y1=janela([A,B,C])
  sg=[(A[0],A[1],B[0],B[1]),(B[0],B[1],C[0],C[1]),(C[0],C[1],A[0],A[1])]
  return(t,[('s',sg,4),('t',[(A[0],A[1],nomes[0]),(B[0],B[1],nomes[1]),(C[0],C[1],nomes[2])],0)],x0,x1,y0,y1,leg)
 def tri():
  return('Tri\xe2ngulo ret\xe2ngulo',[N.fld('Cateto oposto a \u03b1 (a)','','3','o'),N.fld('Cateto adjacente a \u03b1 (b)','','4','o'),N.fld('Hipotenusa (c)','','','o'),N.fld('\xc2ngulo \u03b1 (graus)',
'','','o')],_tri)
 def _tri(v):
  a,b,c,al=[None if x is None else x[0]for x in v]
  N.need(len([x for x in v if x is not None])==2,'Preenche exatamente dois dados (pelo menos um lado)')
  for x,nm in((a,'O cateto a'),(b,'O cateto b'),(c,'A hipotenusa')):
   if x is not None:
    N.pos(x,nm)
  o=[]
  if al is not None:
   N.need(0<al<90,'O \xe2ngulo agudo tem de estar entre 0\xb0 e 90\xb0')
   r=al*G
   if a is not None:
    b,c=(a/math.tan(r),a/math.sin(r))
    o+=['= tg \u03b1 = a / b, logo b = a / tg \u03b1','= sen \u03b1 = a / c, logo c = a / sen \u03b1']
   elif b is not None:
    a,c=(b*math.tan(r),b/math.cos(r))
    o+=['= tg \u03b1 = a / b, logo a = b '+X+' tg \u03b1','= cos \u03b1 = b / c, logo c = b / cos \u03b1']
   else:
    a,b=(c*math.sin(r),c*math.cos(r))
    o+=['= a = c '+X+' sen \u03b1','= b = c '+X+' cos \u03b1']
  elif c is None:
   c=math.sqrt(a*a+b*b)
   o.append('= c\xb2 = a\xb2 + b\xb2 (Pit\xe1goras)')
   al=math.atan(a/b)/G
   o.append('= tg \u03b1 = a / b = '+ex(a/b))
  elif a is not None:
   N.need(c>a,'A hipotenusa tem de ser maior do que os catetos')
   b=math.sqrt(c*c-a*a)
   al=math.asin(a/c)/G
   o+=['= b\xb2 = c\xb2 - a\xb2','= sen \u03b1 = a / c = '+ex(a/c)]
  else:
   N.need(c>b,'A hipotenusa tem de ser maior do que os catetos')
   a=math.sqrt(c*c-b*b)
   al=math.acos(b/c)/G
   o+=['= a\xb2 = c\xb2 - b\xb2','= cos \u03b1 = b / c = '+ex(b/c)]
  o+=['> a '+N.rhs(a)+' '+MS+' b '+N.rhs(b)+' '+MS+' c '+N.rhs(c),'> \u03b1 '+gr(al)+' e \u03b2 = 90\xb0 - \u03b1 '+gr(90-al),'sen \u03b1 = a / c '+N.rhs(a/c)+'; cos \u03b1 = b / c '+N.rhs(b/c)+'; tg \u03b1 = a / b '+N.rhs(a/b),
'\xc1rea = a b / 2 '+N.rhs(a*b/2)+'; per\xedmetro '+N.rhs(a+b+c)]
  g=desenho('Tri\xe2ngulo ret\xe2ngulo',(0,0),(b,0),(b,a),('\u03b1','90\xb0','\u03b2'),'a: vertical; b: horizontal; c: hipotenusa')
  st=('SOH-CAH-TOA: sen = oposto / hipotenusa; cos = adjacente / hipotenusa; tg = oposto / adjacente.\n\u03b1 + \u03b2 = 90\xb0 e a\xb2 + b\xb2 = c\xb2.\nNa calculadora, o \xe2ngulo a partir de uma raz\xe3o:'
' sen\u207b\xb9, cos\u207b\xb9 ou tg\u207b\xb9 (em graus).')
  return('\n'.join(o),st,al,'\xb0',g)
 def rad():
  return('Graus, radianos e valores exatos',[N.fld('\xc2ngulo','','60','n'),N.fld('Unidade','','','c',['graus','radianos (extens\xe3o)'])],_rad)
 def _rad(v):
  x,u=(v[0][0],v[1])
  if u==0:
   d=x
   r=x*G
   o=['= rad = graus '+X+' \u03c0 / 180','> '+N.fmt(d)+'\xb0 = '+pi_txt(d)+' rad '+N.AP+' '+N.fmt(r,0,4)+' rad']
  else:
   r=x
   d=x/G
   o=['= graus = rad '+X+' 180 / \u03c0','> '+N.fmt(r)+' rad '+gr(d)]
  k=round(d)
  if abs(d-k)<1e-09 and k in NOT:
   s,c,t=NOT[k]
   o.append('Valores exatos: sen = '+s+', cos = '+c+', tg = '+(t if t else 'n\xe3o existe'))
  o.append('sen '+N.rhs(math.sin(r))+'; cos '+N.rhs(math.cos(r))+('; tg '+N.rhs(math.tan(r))if abs(math.cos(r))>1e-12 else '; tg n\xe3o existe'))
  if not 0<=d<=90:
   o.append('(\xc2ngulos fora de 0\xb0 a 90\xb0: trigonometria do 11.\xba ano.)')
  st=('180\xb0 = \u03c0 rad (os radianos s\xe3o do 11.\xba ano: extens\xe3o).\nValores exatos: sen 30\xb0 = cos 60\xb0 = 1/2; sen 45\xb0 = cos 45\xb0 = \u221a2/2; sen 60\xb0 = cos 30\xb0 = \u221a3/2.\nsen'
'\xb2 \u03b1 + cos\xb2 \u03b1 = 1 e tg \u03b1 = sen \u03b1 / cos \u03b1.')
  return('\n'.join(o),st,r if u==0 else d,'rad'if u==0 else '\xb0')
 def pi_txt(d):
  for q in range(1,181):
   p=d*q/180
   if abs(p-round(p))<1e-09:
    p=int(round(p))
    if p==0:
     return '0'
    s=(''if abs(p)==1 else str(abs(p)))+'\u03c0'
    return('-'if p<0 else '')+s+(''if q==1 else '/'+str(q))
  return N.fmt(d/180,0,4)+'\u03c0'
 def ang(a,b,c):
  return math.acos(max(-1.0,min(1.0,(b*b+c*c-a*a)/(2*b*c))))/G
 return _ns('N X ex gr desenho tri rad ang',N,X,ex,gr,desenho,tri,rad,ang)


_F['c_matr'] = _m_c_matr


def _m_c_matt():
 import math
 N=_imp('m1_nucleo')
 X=N.X
 def ok3(v):
  for x in v:
   if x is not None:
    N.pos(x[0],'Cada medida')
 def um(v,nome):
  f=[i for i in range(len(v))if v[i]is None]
  N.need(len(f)==1,'Deixa vazio s\xf3 o campo que queres calcular ('+nome+')')
  return f[0]
 def fx(v):
  e=N.exact(v)
  return e if e is not None else N.fmt(v,0,-1)
 def dist(p,q):
  return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)
 def lado(nm,v):
  return nm+' '+N.rhs(v)
 def onde(p,a,b,c,e):
  for q in(a,b,c):
   if dist(p,q)<e:
    return 'v'
  s=[]
  for u,w in((a,b),(b,c),(c,a)):
   s.append((w[0]-u[0])*(p[1]-u[1])-(w[1]-u[1])*(p[0]-u[0]))
  k=max([abs(x)for x in s])*1e-09+1e-12
  if min(s)>k or max(s)<-k:
   return 'i'
  if min(s)>=-k or max(s)<=k:
   return 'f'
  return 'e'
 def pit():
  return('Teorema de Pit\xe1goras',[N.fld('Cateto a','','','o'),N.fld('Cateto b','','','o'),N.fld('Hipotenusa c (3 lados: rec\xedproco)','','','o')],_pit)
 def q2(x):
  return N.fmt(x)+'\xb2'
 def raiz(s):
  r=math.sqrt(s)
  t,ex=N.fmt2(r,0,2)
  if ex:
   return '\u221a'+N.fmt(s)+' = '+t
  e=N.exact(r)
  return '\u221a'+N.fmt(s)+(' = '+e if e and e!='\u221a'+N.fmt(s)else '')+' '+N.AP+' '+t
 def _pit(v):
  a,b,c=v
  ok3(v)
  st=('S\xf3 vale em tri\xe2ngulos ret\xe2ngulos; a hipotenusa \xe9 o lado oposto ao \xe2ngulo reto (o maior).\nRec\xedproco: se o quadrado do maior lado \xe9 igual \xe0 soma dos quadrados dos outros dois, o'
' tri\xe2ngulo \xe9 ret\xe2ngulo.')
  if a is not None and b is not None and(c is not None):
   return reciproco(a[0],b[0],c[0],st)
  k=um(v,'a, b ou c')
  o=['= c\xb2 = a\xb2 + b\xb2']
  if k==2:
   s2=a[0]**2+b[0]**2
   o+=['c\xb2 = '+q2(a[0])+' + '+q2(b[0])+' = '+N.fmt(a[0]**2)+' + '+N.fmt(b[0]**2)+' = '+N.fmt(s2),'> c = '+raiz(s2)]
  else:
   o2=b if k==0 else a
   N.need(c[0]>o2[0],'A hipotenusa tem de ser maior do que cada cateto')
   s2=c[0]**2-o2[0]**2
   x='a'if k==0 else 'b'
   o+=[x+'\xb2 = c\xb2 - '+('b'if k==0 else 'a')+'\xb2 = '+q2(c[0])+' - '+q2(o2[0])+' = '+N.fmt(c[0]**2)+' - '+N.fmt(o2[0]**2)+' = '+N.fmt(s2),'> '+x+' = '+raiz(s2)]
  return('\n'.join(o),st,math.sqrt(s2),'')
 def reciproco(a,b,c,st):
  p,q,h=sorted([a,b,c])
  N.need(h<p+q,'Com estas medidas n\xe3o h\xe1 tri\xe2ngulo: o maior lado tem de ser menor do que a soma dos outros dois')
  s1=p*p+q*q
  s2=h*h
  o=['Rec\xedproco do teorema de Pit\xe1goras: compara-se o quadrado do maior lado com a soma dos quadrados dos outros dois.',q2(h)+' = '+N.fmt(s2),q2(p)+' + '+q2(q)+' = '+N.fmt(p*p)+' + '+N.fmt(q*q)+' = '+N.fmt(s1)]
  if abs(s1-s2)<=1e-09*s2:
   o.append('> S\xe3o iguais: o tri\xe2ngulo \xe9 ret\xe2ngulo (o \xe2ngulo reto op\xf5e-se ao lado '+N.fmt(h)+').')
  else:
   o.append('> '+N.fmt(s2)+(' > 'if s2>s1 else ' < ')+N.fmt(s1)+': n\xe3o \xe9 ret\xe2ngulo; \xe9 '+('obtus\xe2ngulo'if s2>s1 else 'acut\xe2ngulo')+'.')
  return('\n'.join(o),st,None,'')
 def sem():
  return('Semelhan\xe7a',[N.fld('Lado da figura original','',''),N.fld('Lado correspondente na nova figura','',''),N.fld('Outro comprimento da original (opcional)','','','o'),N.fld('\xc1rea da original (opcional)',
'','','o')],_sem)
 def _sem(v):
  a,b,x,s=v
  ok3(v)
  k=b[0]/a[0]
  o=['= k = lado novo / lado original','> k '+N.rhs(k),'k > 1: amplia\xe7\xe3o.'if k>1 else 'k < 1: redu\xe7\xe3o.'if k<1 else 'k = 1: figuras congruentes.']
  if x is not None:
   o.append('Comprimento correspondente: k '+X+' '+N.fmt(x[0])+' '+N.rhs(k*x[0]))
  if s is not None:
   o.append('\xc1rea da nova figura: k\xb2 '+X+' '+N.fmt(s[0])+' '+N.rhs(k*k*s[0]))
  st='Em figuras semelhantes, os comprimentos multiplicam-se por k e as \xe1reas por k\xb2.\nCrit\xe9rio AA: dois \xe2ngulos iguais bastam para dois tri\xe2ngulos serem semelhantes.'
  return('\n'.join(o),st,k,'')
 return _ns('N X um fx lado onde pit q2 raiz sem',N,X,um,fx,lado,onde,pit,q2,raiz,sem)


_F['c_matt'] = _m_c_matt


def _m_c_mexp():
 N=_imp('m1_nucleo')
 Q=_imp('m1_q')
 RELS=(('<=','\u2264'),('>=','\u2265'),('\u2264','\u2264'),('\u2265','\u2265'),('<','<'),('>','>'),('=','='))
 INV={'<':'>','>':'<','\u2264':'\u2265','\u2265':'\u2264'}
 MENOS=(-1,1)
 def partes(s):
  s=s.replace('=<','<=').replace('=>','>=')
  ps,rs=([],[])
  i=0
  ini=0
  while i<len(s):
   for t,r in RELS:
    if s.startswith(t,i):
     ps.append(s[ini:i])
     rs.append(r)
     i+=len(t)
     ini=i
     break
   else:
    i+=1
  ps.append(s[ini:])
  for p in ps:
   N.need(p.strip(),'Falta um membro da '+('equa\xe7\xe3o'if '='in rs else 'inequa\xe7\xe3o'))
  return(ps,rs)
 def lado(s):
  t=Q.arvore(s)
  return(Q.poli(t),Q.letras(t))
 def soma(ps):
  o=''
  for p in ps:
   t=Q.pstr(p)
   if t=='0':
    continue
   if not o:
    o=t
   elif t.startswith('-'):
    o+=' - '+t[1:]
   else:
    o+=' + '+t
  return o or '0'
 def separa(A,x):
  a=dict([(m,A[m])for m in A if dict(m).get(x)])
  b=dict([(m,A[m])for m in A if not dict(m).get(x)])
  return(a,b)
 def termos(A):
  return[{m:A[m]}for m in Q.ordem(A)]
 def coef(A,x):
  C={}
  for m in A:
   if dict(m).get(x):
    C[tuple([(v,e)for v,e in m if v!=x])]=A[m]
  return C
 def mx(A,x):
  c=Q.cte(A)
  if c is not None:
   return Q.pstr(Q.pmul(A,{((x,1),):Q.UM}))if c[0]else '0'+x
  if len(A)==1:
   return Q.pstr(Q.pmul(A,{((x,1),):Q.UM}))
  return '('+Q.pstr(A)+')'+x
 INV={'<':'>','>':'<','\u2264':'\u2265','\u2265':'\u2264'}
 def resolve1(L,R,x,o,rel,txt):
  if '('in txt or '/'in txt:
   o.append(('Sem par\xeanteses: 'if '('in txt else 'Simplificando: ')+Q.pstr(L)+' '+rel+' '+Q.pstr(R))
  k=Q.mmc(Q.denl(L),Q.denl(R))
  if k>1:
   L=Q.pesc(L,(k,1))
   R=Q.pesc(R,(k,1))
   o.append('\xd7 '+str(k)+' (m.m.c. dos denominadores): '+Q.pstr(L)+' '+rel+' '+Q.pstr(R))
  Lx,L0=separa(L,x)
  Rx,R0=separa(R,x)
  if Rx and(not Lx):
   L,R,Lx,L0,Rx,R0=(R,L,Rx,R0,Lx,L0)
   rel=INV.get(rel,rel)
   o.append('Trocando os membros: '+Q.pstr(L)+' '+rel+' '+Q.pstr(R))
  if Rx or L0:
   o.append('Termos com '+x+' no 1.\xba membro: '+soma(termos(Lx)+[Q.pesc(t,MENOS)for t in termos(Rx)])+' '+rel+' '+soma(termos(R0)+[Q.pesc(t,MENOS)for t in termos(L0)]))
  A=coef(Q.padd(Lx,Rx,-1),x)
  B=Q.padd(R0,L0,-1)
  t=mx(A,x)+' '+rel+' '+Q.pstr(B)
  if not o or not o[-1].endswith(': '+t):
   o.append('Reduzindo: '+t)
  return(A,B,rel)
 def incognita(vs,tx,nm):
  if tx:
   x=tx.strip()
   if x not in vs:
    c=[v for v in vs if v.lower()==x.lower()]
    N.need(len(c)==1,'A inc\xf3gnita '+x+' n\xe3o est\xe1 na '+nm)
    x=c[0]
   return x
  N.need(vs,'A '+nm+' n\xe3o tem inc\xf3gnita (nenhuma letra)')
  N.need(len(vs)==1,'A '+nm+' tem as letras '+', '.join(vs)+': escreve qual \xe9 a inc\xf3gnita')
  return vs[0]
 def grau_aviso(D,x):
  g=Q.grau(D,x)
  if g==2 and len(set([v for m in D for v,e in m]))==1:
   cs=Q.coefs(D,x)
   N.err('\xc9 uma equa\xe7\xe3o do 2.\xba grau: '+Q.pstr(D)+' = 0 (a = '+Q.qs(cs[2])+', b = '+Q.qs(cs[1])+', c = '+Q.qs(cs[0])+'); usa a calculadora do 2.\xba grau')
  N.need(g<=1,'N\xe3o \xe9 do 1.\xba grau em '+x+' (grau '+str(g)+'); usa a fatoriza\xe7\xe3o')
 def negativo(A):
  return A[Q.ordem(A)[0]][0]<0 if A else False
 def eq1():
  return('Equa\xe7\xe3o do 1.\xba grau',[N.fld('Equa\xe7\xe3o','','3(x - 2) + 4 = 2x - 1','t'),N.fld('Inc\xf3gnita (se houver outras letras)','','','t')],_eq1)
 def _eq1(v):
  s,tx=v
  N.need(s,'Escreve a equa\xe7\xe3o, por exemplo 2x + 3 = 7')
  ps,rs=partes(s)
  N.need(rs==['='],'Escreve uma equa\xe7\xe3o com um s\xf3 sinal =')
  L,l1=lado(ps[0])
  R,l2=lado(ps[1])
  vs=sorted(set(l1+l2))
  x=incognita(vs,tx,'equa\xe7\xe3o')
  grau_aviso(Q.padd(L,R,-1),x)
  o=[]
  A,B,r=resolve1(L,R,x,o,'=',s)
  c=Q.cte(A)
  r=None
  if c is None:
   if negativo(A):
    A,B=(Q.pesc(A,MENOS),Q.pesc(B,MENOS))
    o.append('Multiplicando por -1: '+mx(A,x)+' = '+Q.pstr(B))
   o.append('> '+x+' = '+frac_txt(B,A)+' (se '+Q.pstr(A)+' \u2260 0)')
  elif c[0]==0:
   if not B:
    o.append('> 0'+x+' = 0: equa\xe7\xe3o poss\xedvel e indeterminada; C.S. = \u211d')
   else:
    o.append('> 0'+x+' = '+Q.pstr(B)+': equa\xe7\xe3o imposs\xedvel; C.S. = \u2205')
  else:
   b=Q.cte(B)
   if b is not None:
    r=Q.div(b,c)
    if c!=Q.UM:
     o.append('Dividindo por '+Q.qp(c)+': '+x+' = '+Q.qs(b)+' : '+Q.qp(c))
    o.append('> '+x+' = '+Q.qs(r)+' ; C.S. = {'+Q.vstr(r)+'}')
    v1=Q.valor(L,{x:r})
    v2=Q.valor(R,{x:r})
    o.append('Verifica\xe7\xe3o: 1.\xba membro = '+Q.qs(v1)+' e 2.\xba membro = '+Q.qs(v2)+(' \u2713'if v1==v2 else ' \u2717'))
   else:
    o.append('> '+x+' = '+frac_txt(B,A))
  st=('Resolver: tirar os par\xeanteses; tirar os denominadores (multiplicar tudo pelo m.m.c.); passar os termos com a inc\xf3gnita para um membro (trocando o sinal); reduzir; dividir pelo coeficiente.\n0x ='
' 0: poss\xedvel e indeterminada; 0x = b (b \u2260 0): imposs\xedvel.')
  return('\n'.join(o),st,Q.qf(r)if r else None,'')
 def frac_txt(B,A):
  c=Q.cte(A)
  if c is not None:
   return Q.pstr(Q.pesc(B,Q.div(Q.UM,c)))
  b=Q.pstr(B)
  return('('+b+')'if len(B)>1 else b)+' / '+('('+Q.pstr(A)+')'if len(A)>1 else Q.pstr(A))
 def ineq():
  return('Inequa\xe7\xe3o do 1.\xba grau',[N.fld('Inequa\xe7\xe3o (ex.: 3 - 2x >= 7)','','3 - 2x >= 7','t'),N.fld('2.\xaa inequa\xe7\xe3o (opcional)','','','t'),N.fld('Liga\xe7\xe3o das duas','','','c',
['e (\u2227, interse\xe7\xe3o)','ou (\u2228, reuni\xe3o)'])],_ineq)
 def uma(s,o,x=None):
  ps,rs=partes(s)
  N.need(rs and '='not in rs and(len(rs)<=2),'Escreve uma inequa\xe7\xe3o com <, >, <= ou >= (por exemplo 2x + 1 < 7)')
  if len(rs)==2:
   o.append('Inequa\xe7\xe3o dupla: '+ps[0].strip()+' '+rs[0]+' '+ps[1].strip()+' e '+ps[1].strip()+' '+rs[1]+' '+ps[2].strip())
   I1,x=uma(ps[0]+rs[0]+ps[1],o,x)
   I2,x=uma(ps[1]+rs[1]+ps[2],o,x)
   return(Q.inter(I1,I2)if I1 and I2 else None,x)
  L,l1=lado(ps[0])
  R,l2=lado(ps[1])
  vs=sorted(set(l1+l2))
  x=x or incognita(vs,'','inequa\xe7\xe3o')
  N.need(vs==[x]or not vs,'Usa s\xf3 a inc\xf3gnita '+x)
  grau_aviso(Q.padd(L,R,-1),x)
  A,B,rel=resolve1(L,R,x,o,rs[0],s)
  a=Q.cte(A)
  b=Q.cte(B)or Q.Z
  if a[0]==0:
   ok={'<':0<b[0],'>':0>b[0],'\u2264':0<=b[0],'\u2265':0>=b[0]}[rel]
   o.append('0 '+rel+' '+Q.qs(b)+' \xe9 '+('sempre verdade: C.S. = \u211d'if ok else 'falso: C.S. = \u2205'))
   return((None,False,None,False)if ok else None,x)
  r=Q.div(b,a)
  if a[0]<0:
   rel=INV[rel]
   o.append('Dividindo por '+Q.qp(a)+' (negativo), o sinal inverte-se: '+x+' '+rel+' '+Q.qs(r))
  elif a!=Q.UM:
   o.append('Dividindo por '+Q.qp(a)+': '+x+' '+rel+' '+Q.qs(r))
  if rel in('<','\u2264'):
   I=(None,False,r,rel=='\u2264')
  else:
   I=(r,rel=='\u2265',None,False)
  o.append('C.S. = '+Q.istr(I))
  return(I,x)
 def _ineq(v):
  s1,s2,lig=v
  N.need(s1,'Escreve a inequa\xe7\xe3o')
  o=[]
  I1,x=uma(s1,o)
  res=[I1]if I1 else[]
  if s2:
   o.append('2.\xaa inequa\xe7\xe3o:')
   I2,x=uma(s2,o,x)
   if lig==0:
    C=Q.inter(I1,I2)if I1 and I2 else None
    res=[C]if C else[]
    o.append('Interse\xe7\xe3o (e):')
   else:
    res=Q.uniao(I1,I2)if I1 and I2 else[I for I in(I1,I2)if I]
    o.append('Reuni\xe3o (ou):')
  if not s2 and o and o[-1].startswith('C.S. = '):
   o.pop()
  o.append('> C.S. = '+(' \u222a '.join([Q.istr(I)for I in res])if res else '\u2205'))
  st=('Resolve-se como uma equa\xe7\xe3o, mas ao multiplicar ou dividir por um n\xfamero negativo o sinal da desigualdade inverte-se.\nO conjunto-solu\xe7\xe3o escreve-se com intervalos; e (\u2227): interse'
'\xe7\xe3o; ou (\u2228): reuni\xe3o.')
  return('\n'.join(o),st,None,'')
 def forma(D,vs,k):
  N.need(Q.grau(D)<=1,'A '+str(k)+'.\xaa equa\xe7\xe3o n\xe3o \xe9 do 1.\xba grau')
  D=Q.pesc(D,(Q.denl(D),1))
  a=D.get(((vs[0],1),),Q.Z)
  b=D.get(((vs[1],1),),Q.Z)
  return(a,b,Q.neg(D.get((),Q.Z)))
 def lin(ts):
  o=''
  for c,t in ts:
   if c[0]==0:
    continue
   a=(abs(c[0]),c[1])
   if t:
    p=(''if a==Q.UM else '('+Q.qs(a)+')'if a[1]>1 else Q.qs(a))+t
   else:
    p=Q.qs(a)
   if not o:
    o=('-'if c[0]<0 else '')+p
   else:
    o+=(' - 'if c[0]<0 else ' + ')+p
  return o or '0'
 def sis():
  return('Sistema de duas equa\xe7\xf5es',[N.fld('1.\xaa equa\xe7\xe3o','','x + y = 5','t'),N.fld('2.\xaa equa\xe7\xe3o','','2x - y = 1','t')],_sis)
 def subs(c1,c0,y):
  if not c1[0]:
   return Q.qs(c0)
  v=Q.qp(y)
  t=v if c1==Q.UM else '-'+v if c1==MENOS else('('+Q.qs(c1)+')'if c1[1]>1 else Q.qs(c1))+' \xd7 '+v
  if c0[0]:
   t+=(' + 'if c0[0]>0 else ' - ')+Q.qs((abs(c0[0]),c0[1]))
  return t
 def _sis(v):
  eqs=[]
  vs=[]
  for k in range(2):
   N.need(v[k],'Escreve a '+str(k+1)+'.\xaa equa\xe7\xe3o')
   ps,rs=partes(v[k])
   N.need(rs==['='],'A '+str(k+1)+'.\xaa equa\xe7\xe3o tem de ter um s\xf3 sinal =')
   L,l1=lado(ps[0])
   R,l2=lado(ps[1])
   eqs.append(Q.padd(L,R,-1))
   vs=sorted(set(vs+l1+l2))
  N.need(len(vs)==2,'O sistema tem de ter duas inc\xf3gnitas (encontrei '+(', '.join(vs)or 'nenhuma')+')')
  E=[forma(eqs[k],vs,k+1)for k in range(2)]
  for k in range(2):
   N.need(E[k][0][0]or E[k][1][0],'A '+str(k+1)+'.\xaa equa\xe7\xe3o n\xe3o tem inc\xf3gnitas')
  o=['Forma reduzida:']
  for k in range(2):
   o.append(' '+str(k+1)+'.\xaa: '+lin([(E[k][0],vs[0]),(E[k][1],vs[1])])+' = '+Q.qs(E[k][2]))
  esc=None
  for i,j in((0,0),(0,1),(1,0),(1,1)):
   if abs(E[i][j][0])==1 and E[i][j][1]==1:
    esc=(i,j)
    break
  if esc is None:
   esc=(0,0)if E[0][0][0]else(0,1)
  i,j=esc
  u,w=(vs[j],vs[1-j])
  al,be,ga=(E[i][j],E[i][1-j],E[i][2])
  c0=Q.div(ga,al)
  c1=Q.neg(Q.div(be,al))
  ex=lin([(c1,w),(c0,'')])
  o.append('Da '+str(i+1)+'.\xaa equa\xe7\xe3o: '+u+' = '+ex)
  k=1-i
  al2,be2,ga2=(E[k][j],E[k][1-j],E[k][2])
  sub=lin([(be2,w)])if not al2[0]else('-'if al2==(-1,1)else ''if al2==Q.UM else Q.qs(al2))+'('+ex+')'+(''if not be2[0]else(' - 'if be2[0]<0 else ' + ')+lin([((abs(be2[0]),be2[1]),w)]))
  o.append('Substituindo na '+str(k+1)+'.\xaa: '+sub+' = '+Q.qs(ga2))
  K=Q.add(be2,Q.mul(al2,c1))
  M=Q.sub(ga2,Q.mul(al2,c0))
  o.append('Reduzindo: '+lin([(K,w)])+' = '+Q.qs(M))
  r=None
  if K[0]==0:
   if M[0]==0:
    o.append('> 0'+w+' = 0: sistema poss\xedvel e indeterminado (infinitas solu\xe7\xf5es; as retas s\xe3o coincidentes)')
   else:
    o.append('> 0'+w+' = '+Q.qs(M)+': sistema imposs\xedvel (as retas s\xe3o paralelas)')
  else:
   yw=Q.div(M,K)
   xu=Q.add(c0,Q.mul(c1,yw))
   if K!=Q.UM:
    o.append(w+' = '+Q.qs(M)+' : '+Q.qp(K)+' = '+Q.qs(yw))
   o.append(u+' = '+subs(c1,c0,yw)+' = '+Q.qs(xu))
   sol={u:xu,w:yw}
   r=sol
   par='('+Q.vstr(sol[vs[0]])+Q.sepr(sol[vs[0]],sol[vs[1]])+Q.vstr(sol[vs[1]])+')'
   o.append('> ('+vs[0]+', '+vs[1]+') = '+par+'; poss\xedvel e determinado')
   ok=[Q.valor(eqs[q],sol)[0]==0 for q in range(2)]
   o.append('Verifica\xe7\xe3o nas duas equa\xe7\xf5es: '+' e '.join(['\u2713'if b else '\u2717'for b in ok]))
   o.append('As duas retas intersetam-se no ponto '+par+'.')
  its=[]
  cx,cy=(Q.qf(r[vs[0]]),Q.qf(r[vs[1]]))if r else(0.0,0.0)
  sg=[]
  for q in range(2):
   a,b,c=[Q.qf(z)for z in E[q]]
   if b:
    def f(t,a=a,b=b,c=c):
     return(c-a*t)/b
    its.append(('f',f,4+q))
   elif a:
    sg.append((c/a,cy-100,c/a,cy+100))
  if sg:
   its.append(('s',sg,6))
  if r:
   its.append(('p',[(cx,cy)],2))
  gr=('Sistema: as duas retas',its,cx-8,cx+8,cy-4.5,cy+4.5,vs[0]+' na horizontal, '+vs[1]+' na vertical; ponto: a solu\xe7\xe3o')
  st=('M\xe9todo de substitui\xe7\xe3o: resolve-se uma equa\xe7\xe3o em ordem a uma inc\xf3gnita e substitui-se na outra.\nCada equa\xe7\xe3o \xe9 uma reta; a solu\xe7\xe3o \xe9 o ponto de interse\xe7\xe3o ('
'se as retas forem paralelas, n\xe3o h\xe1 solu\xe7\xe3o; se coincidirem, h\xe1 infinitas).')
  return('\n'.join(o),st,None,'',gr)
 return _ns('N Q lado soma separa termos mx negativo eq1 ineq uma forma sis',N,Q,lado,soma,separa,termos,mx,negativo,eq1,ineq,uma,forma,sis)


_F['c_mexp'] = _m_c_mexp


def _m_c_mgeo():
 import math
 N=_imp('m1_nucleo')
 G='\xb0'
 X=N.X
 def nv(x):
  s,ex=N.fmt2(x,0,-1)
  if ex:
   return s
  e=N.exact(x)
  return e if e is not None else s
 def eq(a,b):
  return abs(a-b)<1e-09*max(1.0,abs(a),abs(b))
 def gms(x):
  if eq(x,round(x)):
   return ''
  t=abs(x)*3600
  s=int(round(t))
  d,m,r=(s//3600,s//60%60,s%60)
  return ' ('+('= 'if abs(t-s)<1e-06 else N.AP+' ')+str(d)+G+' '+str(m)+"'"+(' '+str(r)+'"'if r else '')+')'
 def ga(x):
  return N.rhs(x,2)+G+gms(x)
 OPA=['Complementar e suplementar','Tri\xe2ngulo: 3.\xba \xe2ngulo','Pol\xedgono de n lados','n pelo \xe2ngulo interno (regular)','n pelo \xe2ngulo externo (regular)','n pela soma dos \xe2ngulos internos',
'Paralelas e secante (desenho)']
 NOMES={3:'tri\xe2ngulo',4:'quadril\xe1tero',5:'pent\xe1gono',6:'hex\xe1gono',7:'hept\xe1gono',8:'oct\xf3gono',9:'ene\xe1gono',10:'dec\xe1gono',11:'undec\xe1gono',12:'dodec\xe1gono',15:'pentadec\xe1gono',
20:'icos\xe1gono'}
 def ang():
  return('\xc2ngulos e pol\xedgonos',[N.fld('Calcular','','','c',OPA),N.fld('Dado: \xe2ngulo (graus), n ou soma','','35','o'),N.fld('2.\xba \xe2ngulo (s\xf3 no tri\xe2ngulo)','','','o')],_ang)
 def _ang(v):
  k,a,b=v
  N.need(a is not None,'Escreve o dado (\xe2ngulo, n ou soma)')
  a=a[0]
  if k==0:
   return compl(a)
  if k==1:
   N.need(b is not None,'Escreve o 2.\xba \xe2ngulo do tri\xe2ngulo')
   return triang(a,b[0])
  if k==6:
   return paralelas(a)
  o=[]
  if k==2:
   N.need(eq(a,round(a)),'O n\xfamero de lados n tem de ser inteiro')
   n=int(round(a))
  else:
   N.pos(a,'O dado')
   if k==3:
    N.need(a<180,'O \xe2ngulo interno de um pol\xedgono convexo \xe9 menor do que 180\xb0')
    e=180-a
    o+=['= \xe2ngulo externo = 180\xb0 - \xe2ngulo interno','180\xb0 - '+nv(a)+'\xb0 '+ga(e)]
   else:
    e=a
   if k==5:
    x=a/180+2
    o+=['= S = (n - 2) '+X+' 180\xb0  \u21d4  n = S : 180\xb0 + 2','n = '+nv(a)+' : 180 + 2 '+N.rhs(x,2)]
   else:
    N.need(e<=120,'O \xe2ngulo externo de um pol\xedgono regular \xe9 no m\xe1ximo 120\xb0 (tri\xe2ngulo)')
    x=360/e
    o+=['= n = 360\xb0 : \xe2ngulo externo','n = 360\xb0 : '+nv(e)+'\xb0 '+N.rhs(x,2)]
   n=int(round(x))
   if not eq(x,n):
    if abs(x-n)<0.01 and n>=3:
     o.append('n '+N.AP+' '+str(n)+': o dado parece arredondado; uso n = '+str(n)+'.')
    else:
     o.append('> N\xe3o h\xe1 pol\xedgono '+(''if k==5 else 'regular ')+'assim: n tem de ser um n\xfamero inteiro.')
     return('\n'.join(o),ST_POL,None,'')
  N.need(3<=n<=10**6,'Um pol\xedgono tem pelo menos 3 lados')
  poligono(n,o)
  return('\n'.join(o),ST_POL,(n-2)*180,'')
 def poligono(n,o):
  nm=NOMES.get(n)
  s=(n-2)*180
  o+=['Pol\xedgono de '+str(n)+' lados'+(' ('+nm+')'if nm else '')+'.','= Soma dos \xe2ngulos internos: S = (n - 2) '+X+' 180\xb0','> S = ('+str(n)+' - 2) '+X+' 180\xb0 = '+str(s)+G,'Soma dos \xe2ngulos externos: 360\xb0 (em qualquer pol\xedgono convexo).',
'Se for regular: \xe2ngulo interno = '+str(s)+'\xb0 : '+str(n)+' '+ga(s/n),'\xe2ngulo externo = 360\xb0 : '+str(n)+' '+ga(360/n)]
  if n==3:
   o.append('O tri\xe2ngulo n\xe3o tem diagonais.')
  else:
   o+=['= Diagonais: d = n(n - 3) / 2','> d = '+str(n)+' '+X+' '+str(n-3)+' / 2 = '+str(n*(n-3)//2),'De cada v\xe9rtice saem '+str(n-3)+' diagonais; dividem o pol\xedgono em '+str(n-2)+' tri\xe2ngulos.']
  o.append('Regular: '+str(n)+' eixos de simetria e simetria de rota\xe7\xe3o de ordem '+str(n)+'.')
 ST_POL='S = (n - 2) '+X+' 180\xb0: o pol\xedgono divide-se em n - 2 tri\xe2ngulos.\nNum pol\xedgono regular, \xe2ngulo interno + \xe2ngulo externo = 180\xb0 e \xe2ngulo externo = 360\xb0 : n.'
 def compl(a):
  N.need(0<a<180,'O \xe2ngulo tem de estar entre 0\xb0 e 180\xb0')
  t='agudo'if a<90 else 'reto'if eq(a,90)else 'obtuso'
  o=['\u03b1 = '+nv(a)+'\xb0: \xe2ngulo '+t+'.']
  r=None
  if a<90 and(not eq(a,90)):
   r=90-a
   o+=['= Complementar: 90\xb0 - \u03b1','> 90\xb0 - '+nv(a)+'\xb0 '+ga(r)]
  else:
   o.append('N\xe3o tem complementar (s\xf3 os \xe2ngulos agudos t\xeam).')
  o+=['= Suplementar: 180\xb0 - \u03b1','> 180\xb0 - '+nv(a)+'\xb0 '+ga(180-a),'O verticalmente oposto tamb\xe9m mede '+nv(a)+'\xb0.']
  st='Complementares: somam 90\xb0. Suplementares: somam 180\xb0.\n\xc2ngulos verticalmente opostos s\xe3o iguais.'
  return('\n'.join(o),st,180-a if r is None else r,'')
 def triang(a,b):
  N.need(a>0 and b>0,'Os \xe2ngulos t\xeam de ser positivos')
  N.need(a+b<180 and(not eq(a+b,180)),'A soma dos dois \xe2ngulos tem de ser menor do que 180\xb0')
  c=180-a-b
  o=['= \u03b1 + \u03b2 + \u03b3 = 180\xb0','> \u03b3 = 180\xb0 - '+nv(a)+'\xb0 - '+nv(b)+'\xb0 '+ga(c)]
  m=max(a,b,c)
  t='ret\xe2ngulo'if eq(m,90)else 'obtus\xe2ngulo'if m>90 else 'acut\xe2ngulo'
  k=eq(a,b)+eq(b,c)+eq(a,c)
  o+=['Tri\xe2ngulo '+t+' e '+('equil\xe1tero'if k==3 else 'is\xf3sceles'if k else 'escaleno')+' (\xe2ngulos iguais \u2194 lados iguais).','\xc2ngulos externos: '+', '.join([nv(180-x)+G for x in(a,b,c)])+' (soma 360\xb0).',
'Cada \xe2ngulo externo = soma dos dois internos n\xe3o adjacentes.','Ao maior \xe2ngulo ('+nv(m)+'\xb0) op\xf5e-se o maior lado.']
  st='A soma dos \xe2ngulos internos de um tri\xe2ngulo \xe9 180\xb0.\nNum tri\xe2ngulo, ao maior \xe2ngulo op\xf5e-se o maior lado.'
  return('\n'.join(o),st,c,'')
 def paralelas(a):
  N.need(0<a<180,'O \xe2ngulo tem de estar entre 0\xb0 e 180\xb0')
  s1=nv(a)+G
  s2=nv(180-a)+G
  o=['\xc2ngulos 1 a 4 na reta de cima e 5 a 8 na de baixo (ver o desenho).','> 1 = 3 = 5 = 7 = '+s1,'> 2 = 4 = 6 = 8 = '+s2,'Verticalmente opostos (iguais): 1 e 3, 2 e 4, 5 e 7, 6 e 8.','Correspondentes (iguais): 1 e 5, 2 e 6, 3 e 7, 4 e 8.',
'Alternos internos (iguais): 3 e 5, 4 e 6.','Alternos externos (iguais): 1 e 7, 2 e 8.','Internos do mesmo lado (somam 180\xb0): 3 e 6, 4 e 5.']
  if eq(a,90):
   o.append('Secante perpendicular: os 8 \xe2ngulos s\xe3o retos.')
  st='Duas retas paralelas cortadas por uma secante: \xe2ngulos correspondentes, alternos internos e alternos externos s\xe3o iguais; internos do mesmo lado s\xe3o suplementares.'
  gr=None
  if 12<=a<=168:
   t=a*math.pi/180
   ux,uy=(math.cos(t),math.sin(t))
   B=(20.0,11.0)
   T=(20.0+2*ux/uy,13.0)
   p0=(B[0]-ux/uy,10.0)
   p1=(T[0]+ux/uy,14.0)
   x0=min(p0[0],p1[0])-1.5
   x1=max(p0[0],p1[0])+1.5
   w=max(x1-x0,2.1*4.6)
   h=w/2.1
   cx=(x0+x1)/2
   X0,X1=(cx-w/2,cx+w/2)
   d=h/130
   rot=[]
   for P,j0 in((T,1),(B,5)):
    for j in range(4):
     b=(a/2+90*j)*math.pi/180
     rot.append((P[0]+0.55*math.cos(b)-6*d,P[1]+0.55*math.sin(b)+6*d,str(j0+j)))
   gr=('Paralelas cortadas por uma secante',[('s',[(X0,11.0,X1,11.0),(X0,13.0,X1,13.0)],0),('s',[(p0[0],p0[1],p1[0],p1[1])],6),('t',rot[:4],2),('t',rot[4:],5)],X0,X1,12-h/2,12+h/2,'1=3=5=7: '+s1+'; 2=4=6=8: '+s2)
  return('\n'.join(o),st,a,'',gr)if gr else('\n'.join(o),st,a,'')
 UN=['u.c.','cm','m','mm','dm','km']
 def ue(u,k):
  if u=='u.c.':
   return('u.c.','u.a.','u.v.')[k-1]
  return u+('','\xb2','\xb3')[k-1]
 def lermed(v,nms,conh,livre=-1):
  k=len(nms)
  for i in range(k,len(v)):
   N.need(v[i]is None,'Esta figura s\xf3 usa '+str(k)+' medida'+('s ('+', '.join(nms)+')'if k>1 else ' ('+nms[0]+')'))
  m=[None if x is None else N.pos(x[0],nms[i]+' ('+str(i+1)+'.\xaa medida)')for i,x in enumerate(v[:k])]
  f=[i for i in range(k)if m[i]is None]
  dados=[c for c in conh if c is not None]
  if not f:
   N.need(not dados,'J\xe1 deste todas as medidas: deixa vazia a \xe1rea, o per\xedmetro ou o volume conhecido')
   return(m,-1)
  N.need(len(f)==1,'Falta mais do que uma medida ('+', '.join([nms[i]for i in f])+')')
  if f[0]==livre and(not dados):
   return(m,f[0])
  N.need(len(dados)==1,'Para calcular '+nms[f[0]]+', escreve '+'um valor conhecido (\xe1rea, per\xedmetro ou volume)')
  return(m,f[0])
 def subst(tp,m,nms):
  return tp.format(*[nms[i]if m[i]is None else nv(m[i])for i in range(len(nms))])
 def resolve(m,i,nms,val,nm,tp,inv,o):
  N.need(i in inv,'Com '+nm+' n\xe3o sei calcular '+nms[i]+'; escreve outra medida')
  o+=[nv(val)+' = '+subst(tp,m,nms),'\u21d4 '+nms[i]+' = '+inv[i][0]]
  try:
   r=inv[i][1](m,val)
  except(ValueError,ZeroDivisionError):
   r=-1
  N.need(r>1e-12,'Os dados n\xe3o s\xe3o compat\xedveis: '+nms[i]+' daria um valor n\xe3o positivo')
  m[i]=r
 FIG=['Quadrado (lado l)','Ret\xe2ngulo (c, l)','Paralelogramo (b, h)','Tri\xe2ngulo (b, h)','Losango (D, d)','Trap\xe9zio (B, b, h)','Pol\xedgono regular (n, l, ap)','C\xedrculo (raio r)','Setor circular (r, \u03b1)',
'Coroa circular (R, r)']
 sq=math.sqrt
 PI=math.pi
 FA=(('l',('A = l\xb2','{0}\xb2',lambda m:m[0]**2),('P = 4 '+X+' l','4 '+X+' {0}',lambda m:4*m[0]),{0:('\u221aA',lambda m,A:sq(A))},{0:('P / 4',lambda m,P:P/4)}),('c l',('A = c '+X+' l','{0} '+X+' {1}',
lambda m:m[0]*m[1]),('P = 2 '+X+' c + 2 '+X+' l','2 '+X+' {0} + 2 '+X+' {1}',lambda m:2*m[0]+2*m[1]),{0:('A / l',lambda m,A:A/m[1]),1:('A / c',lambda m,A:A/m[0])},{0:('P / 2 - l',lambda m,P:P/2-m[1]),1:('P / 2 - c',
lambda m,P:P/2-m[0])}),('b h',('A = b '+X+' h','{0} '+X+' {1}',lambda m:m[0]*m[1]),None,{0:('A / h',lambda m,A:A/m[1]),1:('A / b',lambda m,A:A/m[0])},{}),('b h',('A = b '+X+' h / 2','{0} '+X+' {1} / 2',
lambda m:m[0]*m[1]/2),None,{0:('2 '+X+' A / h',lambda m,A:2*A/m[1]),1:('2 '+X+' A / b',lambda m,A:2*A/m[0])},{}),('D d',('A = D '+X+' d / 2','{0} '+X+' {1} / 2',lambda m:m[0]*m[1]/2),('P = 4 '+X+' \u221a((D/2)\xb2 + (d/2)\xb2)',
'4 '+X+' \u221a(({0}/2)\xb2 + ({1}/2)\xb2)',lambda m:4*sq((m[0]/2)**2+(m[1]/2)**2)),{0:('2 '+X+' A / d',lambda m,A:2*A/m[1]),1:('2 '+X+' A / D',lambda m,A:2*A/m[0])},{0:('2\u221a((P/4)\xb2 - (d/2)\xb2)',
lambda m,P:2*sq((P/4)**2-(m[1]/2)**2)),1:('2\u221a((P/4)\xb2 - (D/2)\xb2)',lambda m,P:2*sq((P/4)**2-(m[0]/2)**2))}),('B b h',('A = (B + b) / 2 '+X+' h','({0} + {1}) / 2 '+X+' {2}',lambda m:(m[0]+m[1])/2*m[2]),
None,{0:('2 '+X+' A / h - b',lambda m,A:2*A/m[2]-m[1]),1:('2 '+X+' A / h - B',lambda m,A:2*A/m[2]-m[0]),2:('2 '+X+' A / (B + b)',lambda m,A:2*A/(m[0]+m[1]))},{}),('n l ap',('A = P / 2 '+X+' ap = n '+X+' l '+X+' ap / 2',
'{0} '+X+' {1} '+X+' {2} / 2',lambda m:m[0]*m[1]*m[2]/2),('P = n '+X+' l','{0} '+X+' {1}',lambda m:m[0]*m[1]),{0:('2 '+X+' A / (l '+X+' ap)',lambda m,A:2*A/m[1]/m[2]),1:('2 '+X+' A / (n '+X+' ap)',lambda m,
A:2*A/m[0]/m[2]),2:('2 '+X+' A / (n '+X+' l)',lambda m,A:2*A/m[0]/m[1])},{0:('P / l',lambda m,P:P/m[1]),1:('P / n',lambda m,P:P/m[0])}),('r',('A = \u03c0 '+X+' r\xb2','\u03c0 '+X+' {0}\xb2',lambda m:PI*m[0]**2),
('P = 2 '+X+' \u03c0 '+X+' r','2 '+X+' \u03c0 '+X+' {0}',lambda m:2*PI*m[0]),{0:('\u221a(A / \u03c0)',lambda m,A:sq(A/PI))},{0:('P / (2\u03c0)',lambda m,P:P/2/PI)}),('r \u03b1',('A = \u03b1/360 '+X+' \u03c0 '+X+' r\xb2',
'{1}/360 '+X+' \u03c0 '+X+' {0}\xb2',lambda m:m[1]/360*PI*m[0]**2),('P = 2r + \u03b1/360 '+X+' 2\u03c0r','2 '+X+' {0} + {1}/360 '+X+' 2\u03c0 '+X+' {0}',lambda m:2*m[0]+m[1]/180*PI*m[0]),{0:('\u221a(360A / (\u03b1\u03c0))',
lambda m,A:sq(360*A/m[1]/PI)),1:('360A / (\u03c0r\xb2)',lambda m,A:360*A/PI/m[0]**2)},{0:('P / (2 + \u03b1\u03c0/180)',lambda m,P:P/(2+m[1]*PI/180)),1:('(P - 2r) '+X+' 180 / (\u03c0r)',lambda m,P:(P-2*m[0])*180/PI/m[0])}),
('R r',('A = \u03c0R\xb2 - \u03c0r\xb2','\u03c0 '+X+' {0}\xb2 - \u03c0 '+X+' {1}\xb2',lambda m:PI*(m[0]**2-m[1]**2)),('P = 2\u03c0R + 2\u03c0r','2\u03c0 '+X+' {0} + 2\u03c0 '+X+' {1}',lambda m:2*PI*(m[0]+m[1])),
{0:('\u221a(A/\u03c0 + r\xb2)',lambda m,A:sq(A/PI+m[1]**2)),1:('\u221a(R\xb2 - A/\u03c0)',lambda m,A:sq(m[0]**2-A/PI))},{0:('P / (2\u03c0) - r',lambda m,P:P/2/PI-m[1]),1:('P / (2\u03c0) - R',lambda m,P:P/2/PI-m[0])}))
 def area():
  return('\xc1reas e per\xedmetros',[N.fld('Figura','','','c',FIG),N.fld('1.\xaa medida','','5','o'),N.fld('2.\xaa medida','','','o'),N.fld('3.\xaa medida','','','o'),N.fld('\xc1rea conhecida (opcional)',
'','','o'),N.fld('Per\xedmetro conhecido (opcional)','','','o'),N.fld('Unidade de comprimento','','','c',UN)],_area)
 def _area(v):
  k=v[0]
  u=UN[v[6]]
  nms=FA[k][0].split()
  fa,fp,ia,ip=FA[k][1:]
  Ak=None if v[4]is None else N.pos(v[4][0],'A \xe1rea')
  Pk=None if v[5]is None else N.pos(v[5][0],'O per\xedmetro')
  m,i=lermed(v[1:4],nms,(Ak,Pk),2 if k==6 else-1)
  o=[]
  if k==6 and i==2 and(Ak is None)and(Pk is None):
   n=m[0]
   N.need(eq(n,round(n))and n>=3,'O n\xfamero de lados n tem de ser um inteiro maior ou igual a 3')
   m[2]=m[1]/2/math.tan(PI/n)
   o.append('ap = l / (2 tan(180\xb0/n)) '+N.rhs(m[2],2)+' (trigonometria, 9.\xba ano)')
  elif i>=0:
   if Ak is not None:
    o.append('= '+fa[0])
    resolve(m,i,nms,Ak,'a \xe1rea',fa[1],ia,o)
   else:
    N.need(fp is not None,'Esta figura n\xe3o tem f\xf3rmula do per\xedmetro s\xf3 com estas medidas; usa a \xe1rea')
    o.append('= '+fp[0])
    resolve(m,i,nms,Pk,'o per\xedmetro',fp[1],ip,o)
   o.append('> '+nms[i]+' '+N.rhs(m[i],2)+{'n':'','\u03b1':G}.get(nms[i],' '+ue(u,1)))
  if k==6:
   N.need(eq(m[0],round(m[0]))and m[0]>=3,'O n\xfamero de lados n tem de ser um inteiro maior ou igual a 3')
  if k==8:
   N.need(m[1]<=360 or eq(m[1],360),'A amplitude do setor \xe9 no m\xe1ximo 360\xb0')
  if k==9:
   N.need(m[0]>m[1],'O raio exterior R tem de ser maior do que r')
  o.append(FIG[k].split(' (')[0]+': '+', '.join([nms[j]+' = '+nv(m[j])+(G if j==1 and k==8 else '')for j in range(len(nms))]))
  A=fa[2](m)
  if i<0 or Ak is None:
   o+=['= '+fa[0],'A = '+subst(fa[1],m,nms),'> A '+N.rhs(A,2)+' '+ue(u,2)]
  if fp is not None:
   P=fp[2](m)
   if i<0 or Pk is None:
    o+=['= '+fp[0],'P = '+subst(fp[1],m,nms),'> P '+N.rhs(P,2)+' '+ue(u,1)]
  else:
   o.append('Per\xedmetro: s\xe3o precisos os comprimentos de todos os lados.')
  if k==0:
   o.append('Diagonal: l\u221a2 '+N.rhs(m[0]*sq(2),2))
  elif k==1:
   o.append('Diagonal (Pit\xe1goras): \u221a(c\xb2 + l\xb2) '+N.rhs(sq(m[0]**2+m[1]**2),2))
  elif k==7:
   o.append('Di\xe2metro: 2r = '+nv(2*m[0]))
  elif k==8:
   o.append('Arco: \u03b1/360 '+X+' 2\u03c0r '+N.rhs(m[1]/180*PI*m[0],2))
  st='\xc1reas em unidades quadradas (cm\xb2, m\xb2...); per\xedmetros em unidades de comprimento.\nPara descobrir uma medida: escreve a \xe1rea ou o per\xedmetro e deixa essa medida vazia.'
  return('\n'.join(o),st,A,ue(u,2))
 return _ns('N X eq ang paralelas resolve area',N,X,eq,ang,paralelas,resolve,area)


_F['c_mgeo'] = _m_c_mgeo


def _m_c_mgtr():
 import math
 N=_imp('m1_nucleo')
 Q=_imp('m1_q')
 G='\xb0'
 OPI=['Transla\xe7\xe3o (vetor a b)','Reflex\xe3o no eixo Ox','Reflex\xe3o no eixo Oy','Reflex\xe3o na reta x = k','Reflex\xe3o na reta y = k','Reflex\xe3o na reta y = x','Reflex\xe3o na reta y = -x','Rota\xe7\xe3o de 90\xb0 (sentido +)',
'Rota\xe7\xe3o de 180\xb0 (meia-volta)','Rota\xe7\xe3o de 90\xb0 (sentido -)']
 def iso():
  return('Isometrias',[N.fld('V\xe9rtices (ex.: 1 1; 4 1; 2 3)','','1 1; 4 1; 2 3','t'),N.fld('Isometria','','','c',OPI),N.fld('Vetor (a b), centro (x y) ou k','','3 2','t')],_iso)
 def qn(t,nm):
  c=Q.cte(Q.poli(Q.arvore(t)))
  N.need(c is not None,nm+': s\xf3 n\xfameros')
  return c
 def nums(t,nm):
  return[qn(p,nm)for p in t.replace(';',' ').split()]
 def lin(a,b,c):
  p={}
  for k,q in(((('x',1),),a),((('y',1),),b),((),c)):
   if q[0]:
    p[k]=q
  return p
 def pts(t):
  ps=[]
  for p in t.split(';'):
   if p.strip():
    c=nums(p,'Os v\xe9rtices')
    N.need(len(c)==2,'Escreve cada v\xe9rtice com duas coordenadas, separados por ; (ex.: 1 1; 4 1; 2 3)')
    ps.append(tuple(c))
  N.need(ps,'Escreve pelo menos um ponto')
  N.need(len(ps)<=12,'No m\xe1ximo 12 v\xe9rtices')
  return ps
 def ptx(p):
  return '('+Q.vstr(p[0])+Q.sepr(p[0],p[1])+Q.vstr(p[1])+')'
 def _iso(v):
  ps=pts(v[0])
  k=v[1]
  c=nums(v[2],'O vetor, o centro ou k')if v[2].strip()else[]
  um,z=(Q.UM,Q.Z)
  m=Q.neg(um)
  cen=None
  if k==0:
   N.need(len(c)==2,'Escreve o vetor com duas coordenadas (ex.: 3 2)')
   T=(lin(um,z,c[0]),lin(z,um,c[1]))
   nm='Transla\xe7\xe3o associada ao vetor ('+Q.vstr(c[0])+Q.sepr(c[0],c[1])+Q.vstr(c[1])+')'
  elif k in(3,4):
   N.need(len(c)==1,'Escreve s\xf3 o valor de k (ex.: 2)')
   d=Q.mul((2,1),c[0])
   T=(lin(m,z,d),lin(z,um,z))if k==3 else(lin(um,z,z),lin(z,m,d))
   nm='Reflex\xe3o na reta '+('x'if k==3 else 'y')+' = '+Q.vstr(c[0])
  elif k in(1,2,5,6):
   T={1:(lin(um,z,z),lin(z,m,z)),2:(lin(m,z,z),lin(z,um,z)),5:(lin(z,um,z),lin(um,z,z)),6:(lin(z,m,z),lin(m,z,z))}[k]
   nm=OPI[k]
  else:
   N.need(len(c)in(0,2),'Escreve o centro com duas coordenadas (vazio = origem)')
   cx,cy=c if c else(z,z)
   cen=(cx,cy)
   if k==8:
    T=(lin(m,z,Q.mul((2,1),cx)),lin(z,m,Q.mul((2,1),cy)))
   elif k==7:
    T=(lin(z,m,Q.add(cx,cy)),lin(um,z,Q.sub(cy,cx)))
   else:
    T=(lin(z,um,Q.sub(cx,cy)),lin(m,z,Q.add(cy,cx)))
   nm=OPI[k].split(' (')[0]+(' (sentido '+('positivo'if k==7 else 'negativo')+')'if k!=8 else '')+' de centro '+('O'if not c else ptx(cen))
  o=[nm+':','= (x, y) \u2192 ('+Q.pstr(T[0],['x','y'])+', '+Q.pstr(T[1],['x','y'])+')']
  im=[]
  for i in range(len(ps)):
   p=ps[i]
   d={'x':p[0],'y':p[1]}
   q=(Q.valor(T[0],d),Q.valor(T[1],d))
   im.append(q)
   L=chr(65+i)
   o.append('> '+L+ptx(p)+' \u2192 '+L+"'"+ptx(q))
  if k==8:
   o.append('Rota\xe7\xe3o de 180\xb0 = simetria central (reflex\xe3o central).')
  o.append('Isometria: mant\xe9m comprimentos e amplitudes; a imagem \xe9 congruente com a figura.')
  o.append('Reflex\xe3o: troca o sentido dos v\xe9rtices.'if 1<=k<=6 else 'Mant\xe9m o sentido (a orienta\xe7\xe3o) dos v\xe9rtices.')
  st='Transla\xe7\xe3o: soma-se o vetor. Reflex\xe3o no eixo Ox: (x, -y); no eixo Oy: (-x, y).\nRota\xe7\xe3o de 90\xb0 (sentido positivo, centro O): (-y, x); de 180\xb0: (-x, -y).'
  return('\n'.join(o),st,None,'',desenho(ps,im,k,c,cen,nm))
 def desenho(ps,im,k,c,cen,nm):
  f=[(Q.qf(p[0]),Q.qf(p[1]))for p in ps]
  g=[(Q.qf(p[0]),Q.qf(p[1]))for p in im]
  xs=[p[0]for p in f+g]
  ys=[p[1]for p in f+g]
  if cen or 1<=k<=6:
   xs.append(Q.qf(cen[0])if cen else 0.0)
   ys.append(Q.qf(cen[1])if cen else 0.0)
  x0,x1,y0,y1=(min(xs),max(xs),min(ys),max(ys))
  w=max(x1-x0,2.1*(y1-y0),2.0)*1.3
  h=w/2.1
  mx,my=((x0+x1)/2,(y0+y1)/2)
  X0,X1,Y0,Y1=(mx-w/2,mx+w/2,my-h/2,my+h/2)
  def poli(q):
   if len(q)<2:
    return[]
   n=len(q)if len(q)>2 else 1
   return[(q[i][0],q[i][1],q[(i+1)%len(q)][0],q[(i+1)%len(q)][1])for i in range(n)]
  its=[('s',poli(f),0),('s',poli(g),5),('p',f,0),('p',g,5),('t',[(f[i][0],f[i][1],chr(65+i))for i in range(len(f))],0),('t',[(g[i][0],g[i][1],chr(65+i)+"'")for i in range(len(g))],5)]
  if k==0:
   its.append(('s',[(f[i][0],f[i][1],g[i][0],g[i][1])for i in range(len(f))],7))
  elif k in(1,4):
   y=0.0 if k==1 else Q.qf(c[0])
   its.append(('s',[(X0,y,X1,y)],6))
  elif k in(2,3):
   x=0.0 if k==2 else Q.qf(c[0])
   its.append(('s',[(x,Y0,x,Y1)],6))
  elif k in(5,6):
   s=1 if k==5 else-1
   a=max(abs(X0),abs(X1),abs(Y0),abs(Y1))
   its.append(('s',[(-a,-s*a,a,s*a)],6))
  else:
   q=(Q.qf(cen[0]),Q.qf(cen[1]))
   its+=[('p',[q],6),('t',[(q[0],q[1],'O'if not c else 'C')],6)]
  return(nm,its,X0,X1,Y0,Y1,'preto: figura; vermelho: imagem')
 OPC=['Dado o arco AB','Dado o \xe2ngulo inscrito','V\xe9rtice interior (arcos a, b)','V\xe9rtice exterior (arcos a, b)','Quadril\xe1tero inscrito (\u03b1, \u03b2)','Pol\xedgono regular inscrito (n)',
'Comprimento do arco (r, \u03b1)']
 def circ():
  return('\xc2ngulos na circunfer\xeancia',[N.fld('Calcular','','','c',OPC),N.fld('1.\xba dado (graus, n ou raio)','','80','o'),N.fld('2.\xba dado (graus)','','','o')],_circ)
 def gt(x):
  return N.rhs(x,2)+G
 def nv(x):
  s,ex=N.fmt2(x,0,-1)
  e=None if ex else N.exact(x)
  return(e or s)+G
 def pc(t,r=3.0):
  t=t*math.pi/180
  return(10+r*math.cos(t),10+r*math.sin(t))
 def janela(nm,its,ps,leg):
  xs=[p[0]for p in ps]+[6.5,13.5]
  ys=[p[1]for p in ps]+[6.5,13.5]
  x0,x1,y0,y1=(min(xs),max(xs),min(ys),max(ys))
  w=max(x1-x0,2.1*(y1-y0))*1.1
  h=w/2.1
  mx,my=((x0+x1)/2,(y0+y1)/2)
  cs=[pc(7.5*i)for i in range(49)]
  its=[('s',[(cs[i][0],cs[i][1],cs[i+1][0],cs[i+1][1])for i in range(48)],7)]+its
  return(nm,its,mx-w/2,mx+w/2,my-h/2,my+h/2,leg)
 def segs(*ps):
  return[(ps[i][0],ps[i][1],ps[i+1][0],ps[i+1][1])for i in range(len(ps)-1)]
 def rot(ls):
  return[(p[0],p[1],t)for p,t in ls]
 def _circ(v):
  k,a,b=v
  N.need(a is not None,'Escreve o 1.\xba dado')
  a=a[0]
  o=[]
  gr=None
  O=(10.0,10.0)
  if k in(0,1):
   N.pos(a,'O dado')
   x=a if k==0 else 2*a
   N.need(x<360,'O arco tem de ser menor do que 360\xb0'if k==0 else 'O \xe2ngulo inscrito tem de ser menor do que 180\xb0')
   if k==1:
    o+=['= arco = 2 '+N.X+' \xe2ngulo inscrito','> Arco AB = 2 '+N.X+' '+nv(a)+' '+gt(x)]
   else:
    o.append('Arco AB = '+nv(x))
   o+=['> \xc2ngulo ao centro AOB '+gt(x)+' (igual ao arco)','> \xc2ngulo inscrito AVB '+gt(x/2)+' (metade do arco)','\xc2ngulo de segmento (corda AB e tangente em A) '+gt(x/2),'Com o v\xe9rtice no pr\xf3prio arco AB: (360\xb0 - '+nv(x)+') / 2 '+gt((360-x)/2)]
   if abs(x-180)<1e-09:
    o.append('Arco de 180\xb0: o \xe2ngulo inscrito numa semicircunfer\xeancia \xe9 reto.')
   A,B,V=(pc(270-x/2),pc(270+x/2),pc(90))
   gr=janela('\xc2ngulo ao centro e inscrito',[('s',segs(A,O,B),2),('s',segs(A,V,B),5),('t',rot([(A,'A'),(B,'B'),(O,'O'),(V,'V')]),0)],[A,B,V],'azul: ao centro '+nv(x)+'; vermelho: '+'inscrito '+nv(x/2))
   r=x/2
  elif k in(2,3):
   N.need(b is not None,'Escreve os dois arcos')
   b=b[0]
   N.need(a>0 and b>=0,'Os arcos t\xeam de ser positivos')
   N.need(a+b<=360,'Os dois arcos somam no m\xe1ximo 360\xb0')
   if k==2:
    r=(a+b)/2
    o+=['= \xe2ngulo = (a + b) / 2 (semissoma dos arcos)','> ('+nv(a)+' + '+nv(b)+') / 2 '+gt(r),'a: arco entre os lados do \xe2ngulo; b: arco entre os prolongamentos dos lados.']
    x=(360-a-b)/2
    A,B=(pc(270-a/2),pc(270+a/2))
    C,D=(pc(270+a/2+x),pc(270+a/2+x+b))
    gr=janela('V\xe9rtice no interior',[('s',segs(A,C)+segs(B,D),5),('t',rot([(A,'A'),(B,'B'),(C,'C'),(D,'D')]),0)],[A,B,C,D],'arco AB = '+nv(a)+'; arco CD = '+nv(b))
   else:
    N.need(a>b,'O 1.\xba arco (o mais afastado do v\xe9rtice) tem de ser o maior')
    r=(a-b)/2
    o+=['= \xe2ngulo = (a - b) / 2 (semidiferen\xe7a dos arcos)','> ('+nv(a)+' - '+nv(b)+') / 2 '+gt(r),'a: arco mais afastado do v\xe9rtice; b: o mais pr\xf3ximo.','Vale para duas secantes, secante e tangente ou duas tangentes.']
    if a+b<359.9 and r>=8:
     A,B=(pc(90+b/2),pc(90-b/2))
     D,C=(pc(270-a/2),pc(270+a/2))
     P=corte(A,D,B,C)
     if P and abs(P[0]-10)<13 and(abs(P[1]-10)<13):
      gr=janela('V\xe9rtice no exterior',[('s',segs(P,D)+segs(P,C),5),('t',rot([(P,'P'),(A,'A'),(B,'B'),(C,'C'),(D,'D')]),0)],[A,B,C,D,P],'arco DC = '+nv(a)+'; arco AB = '+nv(b))
  elif k==4:
   N.need(b is not None,'Escreve dois \xe2ngulos consecutivos')
   b=b[0]
   N.need(0<a<180 and 0<b<180,'Os \xe2ngulos de um quadril\xe1tero inscrito est\xe3o entre 0\xb0 e 180\xb0')
   r=180-a
   o+=['Num quadril\xe1tero inscrito, os \xe2ngulos opostos s\xe3o suplementares.','> Oposto a '+nv(a)+': 180\xb0 - '+nv(a)+' '+gt(r),'> Oposto a '+nv(b)+': 180\xb0 - '+nv(b)+' '+gt(180-b),'Soma dos quatro: 360\xb0 \u2713']
  elif k==5:
   N.need(abs(a-round(a))<1e-09 and 3<=a<=1000,'n tem de ser um inteiro maior ou igual a 3')
   n=int(round(a))
   r=360/n
   o+=['= \xe2ngulo ao centro = 360\xb0 : n','> 360\xb0 : '+str(n)+' '+gt(r),'Arco correspondente a cada lado '+gt(r),'\xc2ngulo interno = \xe2ngulo inscrito que abrange n - 2 arcos: (n - 2) '+N.X+' 180\xb0 : n '+gt((n-2)*180/n),
'\xc2ngulo inscrito que abrange um lado '+gt(r/2)]
   if n<=24:
    q=[pc(90+r*i)for i in range(n+1)]
    gr=janela('Pol\xedgono regular inscrito',[('s',segs(*q),5),('s',segs(q[0],O,q[1]),2)],q,'azul: \xe2ngulo ao centro '+nv(r))
  else:
   N.need(b is not None,'Escreve o raio r e a amplitude \u03b1')
   b=b[0]
   N.pos(a,'O raio')
   N.need(0<b<=360,'A amplitude tem de estar entre 0\xb0 e 360\xb0')
   r=b/360*2*math.pi*a
   o+=['= comprimento do arco: l = \u03b1/360 '+N.X+' 2\u03c0r','> l = '+N.fmt(b)+'/360 '+N.X+' 2\u03c0 '+N.X+' '+N.fmt(a)+' '+N.rhs(r,2),'= \xe1rea do setor: A = \u03b1/360 '+N.X+' \u03c0r\xb2','> A = '+N.fmt(b)+'/360 '+N.X+' \u03c0 '+N.X+' '+N.fmt(a)+'\xb2 '+N.rhs(b/360*math.pi*a*a,
2)]
   q=[pc(270-b/2+b*i/24)for i in range(25)]
   gr=janela('Arco e setor',[('s',segs(*q),5),('s',segs(q[0],O,q[24]),2)],q,'vermelho: arco de '+nv(b))
  st='\xc2ngulo ao centro = arco; \xe2ngulo inscrito = metade do arco.\nV\xe9rtice interior: semissoma dos arcos; exterior: semidiferen\xe7a.\nQuadril\xe1tero inscrito: \xe2ngulos opostos suplementares.'
  return('\n'.join(o),st,r,'',gr)if gr else('\n'.join(o),st,r,'')
 def corte(A,D,B,C):
  d1=(D[0]-A[0],D[1]-A[1])
  d2=(C[0]-B[0],C[1]-B[1])
  den=d1[0]*d2[1]-d1[1]*d2[0]
  if abs(den)<1e-12:
   return None
  t=((B[0]-A[0])*d2[1]-(B[1]-A[1])*d2[0])/den
  return(A[0]+t*d1[0],A[1]+t*d1[1])
 return _ns('N Q iso desenho circ',N,Q,iso,desenho,circ)


_F['c_mgtr'] = _m_c_mgtr


def _m_c_mnum():
 N=_imp('m1_nucleo')
 Q=_imp('m1_q')
 SIM={'+':'+','-':'-','*':'\xd7','/':':'}
 def ler(s):
  t=Q.arvore(s)
  ls=Q.letras(t)
  N.need(not ls,'Esta calculadora \xe9 s\xf3 para n\xfameros (encontrei a letra '+(ls[0]if ls else '')+')')
  return t
 def base_txt(a):
  return '('+Q.qs(a)+')'if a[0]<0 or a[1]>1 else Q.qs(a)
 def passo_op(k,a,b,r,ps):
  if k in '+-'and(a[1]>1 or b[1]>1):
   L=Q.mmc(a[1],b[1])
   fa=str(a[0]*(L//a[1]))+'/'+str(L)
   fb=str(b[0]*(L//b[1]))+'/'+str(L)
   s=Q.qs(a)+' '+k+' '+Q.qp(b)
   if a[1]!=L or b[1]!=L:
    s+=' = '+fa+' '+k+' '+('('+fb+')'if b[0]<0 else fb)
   n=a[0]*(L//a[1])+(1 if k=='+'else-1)*b[0]*(L//b[1])
   s+=' = '+str(n)+'/'+str(L)
   if(n,L)!=r:
    s+=' = '+Q.qs(r)
   ps.append(s)
  elif k=='*'and(a[1]>1 or b[1]>1):
   s=Q.qs(a)+' \xd7 '+Q.qp(b)+' = '+str(a[0]*b[0])+'/'+str(a[1]*b[1])
   if(a[0]*b[0],a[1]*b[1])!=r:
    s+=' = '+Q.qs(r)
   ps.append(s)
  elif k=='/'and(a[1]>1 or b[1]>1 or Q.qs(r).find('/')>=0):
   inv=Q.R(b[1],b[0])
   ps.append(Q.qs(a)+' : '+Q.qp(b)+' = '+Q.qs(a)+' \xd7 '+Q.qp(inv)+' = '+Q.qs(r))
  else:
   ps.append(Q.qp(a)+' '+SIM[k]+' '+Q.qp(b)+' = '+Q.qs(r))
 def calc(t,ps):
  k=t[0]
  if k=='n':
   return t[1]
  if k=='u':
   return Q.neg(calc(t[1],ps))
  if k in '+-*/':
   a=calc(t[1],ps)
   b=calc(t[2],ps)
   r={'+':Q.add,'-':Q.sub,'*':Q.mul,'/':Q.div}[k](a,b)
   passo_op(k,a,b,r,ps)
   return r
  if k=='^':
   a=calc(t[1],ps)
   e=calc(t[2],ps)
   N.need(e[1]==1,'O expoente tem de ser um n\xfamero inteiro')
   r=Q.pw(a,e[0])
   s=base_txt(a)+N.sup(e[0])+' = '
   if e[0]<0:
    s+='('+Q.qs(Q.R(a[1],a[0]))+')'+N.sup(-e[0])+' = '
   ps.append(s+Q.qs(r))
   return r
  if k=='r':
   a=calc(t[1],ps)
   N.need(a[0]>=0,'N\xe3o h\xe1 raiz quadrada de um n\xfamero negativo')
   n,d=(isqrt(a[0]),isqrt(a[1]))
   N.need(n*n==a[0]and d*d==a[1],'\u221a'+Q.qs(a)+' n\xe3o \xe9 um n\xfamero racional: usa a calculadora de radicais')
   r=Q.R(n,d)
   ps.append('\u221a'+base_txt(a)+' = '+Q.qs(r))
   return r
  N.err('Express\xe3o inv\xe1lida')
 def isqrt(n):
  if n<2:
   return n
  x=int(n**0.5)
  while x*x>n:
   x-=1
  while(x+1)*(x+1)<=n:
   x+=1
  return x
 def mostra(r):
  o=['> = '+Q.qs(r)]
  if r[1]>1:
   o.append('Em d\xedzima: '+Q.dizima(r)+(''if fin(r[1])else ' \u2248 '+N.fmt(Q.qf(r))))
   if abs(r[0])>r[1]:
    ip=abs(r[0])//r[1]
    o.append('Numeral misto: '+('-'if r[0]<0 else '')+str(ip)+' e '+str(abs(r[0])-ip*r[1])+'/'+str(r[1]))
  return o
 def fin(d):
  for p,e in Q.fatores(d):
   if p not in(2,5):
    return False
  return True
 def frac():
  return('Fra\xe7\xf5es e n\xfameros racionais',[N.fld('Express\xe3o num\xe9rica','','1/2 + 3/4 \xd7 (2/3 - 1)','t'),N.fld('Ordenar (opcional): n\xfameros com espa\xe7os','','','t')],_frac)
 def _frac(v):
  te,to=v
  o=[]
  r=None
  if te:
   ps=[]
   r=calc(ler(te),ps)
   if ps:
    o.append('Pela ordem das opera\xe7\xf5es (par\xeanteses, pot\xeancias, \xd7 e :, + e -):')
    o+=[str(i+1)+'. '+ps[i]for i in range(len(ps))]
   o+=mostra(r)
  if to:
   xs=[]
   for p in to.replace(';',' ').split():
    r2=calc(ler(p),[])
    k=len(xs)
    while k>0 and Q.cmp(xs[k-1][0],r2)>0:
     k-=1
    xs.insert(k,(r2,p))
   N.need(len(xs)>=2,'Escreve pelo menos dois n\xfameros para ordenar')
   txt=xs[0][1]
   for i in range(1,len(xs)):
    txt+=(' = 'if Q.cmp(xs[i][0],xs[i-1][0])==0 else ' < ')+xs[i][1]
   o.append('Por ordem crescente: '+txt)
   o.append('(Valores: '+'; '.join([N.fmt(Q.qf(x))for x,p in xs])+')')
  N.need(te or to,'Escreve uma express\xe3o ou n\xfameros para ordenar')
  st=('Ordem das opera\xe7\xf5es: par\xeanteses, pot\xeancias, multiplica\xe7\xf5es e divis\xf5es, adi\xe7\xf5es e subtra\xe7\xf5es (da esquerda para a direita).\nSomar fra\xe7\xf5es: reduz-se ao mesmo denom'
'inador (m.m.c.).\nDividir por uma fra\xe7\xe3o: multiplica-se pelo inverso.\nSinais: (-) \xd7 (-) = (+); (-) \xd7 (+) = (-).')
  return('\n'.join(o),st,Q.qf(r)if r else None,'')
 def fatores_pot(t,sg,out):
  k=t[0]
  if k=='*':
   return fatores_pot(t[1],sg,out)and fatores_pot(t[2],sg,out)
  if k=='/':
   return fatores_pot(t[1],sg,out)and fatores_pot(t[2],-sg,out)
  if k=='^':
   b,e=(t[1],t[2])
   if b[0]=='^':
    pp=[]
    if not fatores_pot(b,1,pp)or len(pp)!=1:
     return False
    ee=calc(e,[])
    if ee[1]!=1:
     return False
    out.append((sg,pp[0][1],pp[0][2]*ee[0],(pp[0][2],ee[0])))
    return True
   ee=calc(e,[])
   if ee[1]!=1 or b[0]not in('n','v','u'):
    return False
   if b[0]=='u'and b[1][0]!='n':
    return False
   out.append((sg,b,ee[0],None))
   return True
  if k in('n','v'):
   out.append((sg,t,1,None))
   return True
  return False
 def btxt(b):
  if b[0]=='v':
   return b[1]
  if b[0]=='u':
   return '(-'+Q.qs(b[1][1])+')'
  return base_txt(b[1])
 def pot():
  return('Pot\xeancias e as suas regras',[N.fld('Express\xe3o com pot\xeancias','','2^3 \xd7 2^4 : 2^5','t')],_pot)
 def _pot(v):
  s=v[0]
  N.need(s,'Escreve uma express\xe3o, por exemplo 2^3 \xd7 2^4')
  t=Q.arvore(s)
  o=[]
  fs=[]
  if fatores_pot(t,1,fs)and len(fs)>=1:
   for sg,b,e,pp in fs:
    if pp:
     o.append('Pot\xeancia de pot\xeancia: ('+btxt(b)+N.sup(pp[0])+')'+N.sup(pp[1])+' = '+btxt(b)+'^('+str(pp[0])+' \xd7 '+qn(pp[1])+') = '+btxt(b)+N.sup(e))
   grupos=[]
   for sg,b,e,pp in fs:
    nm=btxt(b)
    for g in grupos:
     if g[0]==nm:
      g[2].append(sg*e)
      break
    else:
     grupos.append([nm,b,[sg*e]])
   for g in grupos:
    if len(g[2])>1:
     soma=sum(g[2])
     o.append('Mesma base '+g[0]+': somam-se ou subtraem-se os expoentes: '+g[0]+'^('+str(g[2][0])+''.join([' + '+str(x)if x>=0 else ' - '+str(-x)for x in g[2][1:]])+') = '+g[0]+N.sup(soma))
   res=[(g[0],g[1],sum(g[2]))for g in grupos]
   es=set([e for nm,b,e in res])
   if len(res)>1 and len(es)==1 and(not[1 for nm,b,e in res if b[0]=='v']):
    e=list(es)[0]
    prod=Q.UM
    for nm,b,x in res:
     prod=Q.mul(prod,calc(b,[]))
    o.append('Mesmo expoente: multiplicam-se as bases: '+' \xd7 '.join([nm+N.sup(e)for nm,b,x in res])+' = ('+' \xd7 '.join([nm for nm,b,x in res])+')'+N.sup(e)+' = '+base_txt(prod)+N.sup(e))
   if[1 for nm,b,e in res if b[0]=='v']:
    o.append('> '+' \xd7 '.join([nm+(N.sup(e)if e!=1 else '')for nm,b,e in res if e!=0])or '> 1')
    for nm,b,e in res:
     if e<0:
      o.append(nm+N.sup(e)+' = 1/'+nm+N.sup(-e)+' (expoente negativo)')
    return('\n'.join(o),ST_POT,None,'')
   for nm,b,e in res:
    if e<0:
     o.append(nm+N.sup(e)+' = 1/'+nm+N.sup(-e)+' (expoente negativo)')
    if e==0:
     o.append(nm+'\u2070 = 1 (expoente zero)')
  ps=[]
  r=calc(t,ps)
  o.append('Valor: '+(ps[-1]if ps else Q.qs(r)))
  o+=mostra(r)
  if abs(r[0])>=10**6 or(r[0]and abs(Q.qf(r))<10**(-4)):
   o.append('Em nota\xe7\xe3o cient\xedfica: usa a calculadora de nota\xe7\xe3o cient\xedfica.')
  return('\n'.join(o),ST_POT,Q.qf(r),'')
 def qn(x):
  return str(x)if x>=0 else '('+str(x)+')'
 ST_POT=('a^m \xd7 a^n = a^(m + n); a^m : a^n = a^(m - n), com a \u2260 0.\n(a^m)^n = a^(m \xd7 n); a^n \xd7 b^n = (a \xd7 b)^n.\na\u2070 = 1; a^(-n) = 1/a^n.\nBase negativa: expoente par d\xe1 positivo; expoen'
'te \xedmpar d\xe1 negativo.')
 def mdc():
  return('Fatores primos, m.d.c. e m.m.c.',[N.fld('N\xfameros inteiros (2 ou mais)','','84 120','l')],_mdc)
 def _mdc(v):
  ns=[]
  for x,sf in v[0]:
   N.need(x==int(x)and 1<=x<=10**12,'Escreve n\xfameros inteiros positivos (at\xe9 10\xb9\xb2)')
   ns.append(int(x))
  N.need(len(ns)<=6,'No m\xe1ximo 6 n\xfameros')
  o=[]
  fs=[]
  for n in ns:
   f=Q.fatores(n)
   fs.append(f)
   o.append(str(n)+' = '+Q.fstr(f)+(' (primo)'if len(f)==1 and f[0][1]==1 else ''))
  if len(ns)==1:
   n=ns[0]
   if n<=10**6:
    ds=[d for d in range(1,n+1)if n%d==0]if n<=2000 else divisores(fs[0])
    o.append('Divisores ('+str(len(ds))+'): '+', '.join([str(d)for d in ds[:40]])+(' ...'if len(ds)>40 else ''))
   st='Decomp\xf5e-se dividindo pelos primos 2, 3, 5, 7, ... por ordem.'
   return('\n'.join(o),st,None,'')
  ps=sorted(set([p for f in fs for p,e in f]))
  com=[]
  tod=[]
  g=ns[0]
  m=ns[0]
  for n in ns[1:]:
   g=Q.mdc(g,n)
   m=Q.mmc(m,n)
  for p in ps:
   es=[dict(f).get(p,0)for f in fs]
   if min(es)>0:
    com.append((p,min(es)))
   tod.append((p,max(es)))
  o.append('= m.d.c.: fatores comuns, com o menor expoente')
  o.append('> m.d.c. = '+(Q.fstr(com)+' = 'if com else '')+str(g))
  o.append('= m.m.c.: fatores comuns e n\xe3o comuns, com o maior expoente')
  o.append('> m.m.c. = '+Q.fstr(tod)+' = '+str(m))
  if g==1:
   o.append('Os n\xfameros s\xe3o primos entre si (m.d.c. = 1).')
  if len(ns)==2:
   a,b=ns
   o.append('Confirma\xe7\xe3o: m.d.c. \xd7 m.m.c. = '+str(g*m)+' = '+str(a)+' \xd7 '+str(b))
   o.append('Fra\xe7\xe3o '+str(a)+'/'+str(b)+' simplificada (: '+str(g)+'): '+Q.qs(Q.R(a,b)))
  st='m.d.c.: o maior divisor comum (serve para simplificar fra\xe7\xf5es).\nm.m.c.: o menor m\xfaltiplo comum (serve para somar fra\xe7\xf5es).'
  return('\n'.join(o),st,g,'')
 def divisores(f):
  ds=[1]
  for p,e in f:
   ds=[d*p**k for d in ds for k in range(e+1)]
  ds.sort()
  return ds
 def dec():
  return('D\xedzimas e fra\xe7\xf5es',[N.fld('Fra\xe7\xe3o ou d\xedzima (ex.: 7/12 ou 1,2(45))','','7/12','t')],_dec)
 def dez(k):
  return '10'if k==1 else '10'+N.sup(k)
 def _dec(v):
  s=v[0].replace(' ','').replace('.',',')
  N.need(s,'Escreve uma fra\xe7\xe3o (7/12) ou uma d\xedzima (0,(3) ou 1,25)')
  o=[]
  if '('in s:
   N.need(s.endswith(')')and s.count('(')==1 and(','in s),'Escreve a d\xedzima peri\xf3dica assim: 1,2(45) (per\xedodo entre par\xeanteses)')
   neg=s.startswith('-')
   s2=s.lstrip('-+')
   ip,rest=s2.split(',')
   np_,per=rest[:-1].split('(')
   N.need((ip+np_+per).isdigit()and per,'D\xedzima mal escrita')
   k,p=(len(np_),len(per))
   a=int(ip+np_+per)
   b=int(ip+np_)if ip+np_ else 0
   num,den=(a-b,10**(k+p)-10**k)
   r=Q.R(-num if neg else num,den)
   sg='-'if neg else ''
   o.append('Seja d = '+sg+(ip or '0')+','+np_+'('+per+')')
   if k:
    o.append(dez(k)+' d = '+sg+str(int(ip+np_))+',('+per+')')
   o.append(dez(k+p)+' d = '+sg+str(int(ip+np_+per))+',('+per+')')
   o.append('Subtraindo: '+str(den)+' d = '+('-'if neg else '')+str(num))
   o.append('> d = '+('-'if neg else '')+str(num)+'/'+str(den)+(' = '+Q.qs(r)if(num,den)!=(abs(r[0]),r[1])else ''))
  else:
   r=calc(ler(s.replace(',','.')if '/'not in s else s),[])
   o.append('> '+s+' = '+Q.qs(r)+(' (fra\xe7\xe3o irredut\xedvel)'if r[1]>1 else ''))
   o.append('D\xedzima: '+Q.dizima(r))
  if r[1]>1:
   f=Q.fatores(r[1])
   o.append('Denominador '+str(r[1])+' = '+Q.fstr(f))
   if fin(r[1]):
    o.append('S\xf3 tem os fatores 2 e 5: d\xedzima finita.')
   else:
    dz=Q.dizima(r)
    o.append('Tem fatores diferentes de 2 e 5: d\xedzima infinita peri\xf3dica'+(', per\xedodo '+dz[dz.find('(')+1:-1]if '('in dz else ''))
  st=('Fra\xe7\xe3o irredut\xedvel com denominador s\xf3 com fatores 2 e 5: d\xedzima finita; sen\xe3o, infinita peri\xf3dica.\nD\xedzima peri\xf3dica para fra\xe7\xe3o: multiplica-se por pot\xeancias de 10 '
'e subtrai-se para o per\xedodo desaparecer.')
  return('\n'.join(o),st,Q.qf(r),'')
 return _ns('N Q ler calc mostra frac pot mdc dec',N,Q,ler,calc,mostra,frac,pot,mdc,dec)


_F['c_mnum'] = _m_c_mnum


def _m_c_mpol():
 N=_imp('m1_nucleo')
 Q=_imp('m1_q')
 def binomio(P):
  return len(P)==2
 def caso(t,ex):
  if t[0]=='^':
   e=Q.cte(Q.poli(t[2]))
   b=Q.poli(t[1])
   if e==(2,1)and binomio(b):
    return 'quadrado do bin\xf3mio: (a \xb1 b)\xb2 = a\xb2 \xb1 2ab + b\xb2'
   if e==(3,1)and binomio(b):
    return 'cubo do bin\xf3mio'
  if t[0]=='*':
   a,b=(Q.poli(t[1]),Q.poli(t[2]))
   if binomio(a)and binomio(b)and(len(ex)==2)and(len(Q.padd(a,b))==1)and(len(Q.padd(a,b,-1))==1):
    return 'diferen\xe7a de quadrados: (a + b)(a - b) = a\xb2 - b\xb2'
   if len(a)>1 or len(b)>1:
    return 'propriedade distributiva'
  return ''
 def pol():
  return('Polin\xf3mios: desenvolver e simplificar',[N.fld('Express\xe3o','','(2x - 3)^2 - (x + 1)(x - 1)','t'),N.fld('Valor da letra (opcional)','','','o')],_pol)
 def _pol(v):
  s,x0=v
  N.need(s,'Escreve uma express\xe3o, por exemplo (x + 2)^2')
  p=Q.P(s)
  ts=p.termos()
  o=[]
  for sg,t,txt in ts:
   e=Q.poli(t)
   nm=caso(t,e)
   if nm or(t[0]in '*^/'and Q.pstr(e)!=txt.replace(' ','')):
    o.append(txt+' = '+Q.pstr(e)+('  ('+nm+')'if nm else ''))
  P={}
  for sg,t,txt in ts:
   P=Q.padd(P,Q.poli(t),sg)
  if len(ts)>1:
   o.append('Juntando os termos semelhantes:')
  o.append('> '+Q.pstr(P))
  ls=sorted(set([x for m in P for x,e in m]))
  g=Q.grau(P)
  o.append('Grau: '+(str(g)if P else 'n\xe3o tem (polin\xf3mio nulo)')+'; termo independente: '+Q.qs(P.get((),Q.Z)))
  r=None
  if x0 is not None:
   N.need(len(ls)<=1,'Para o valor num\xe9rico, o polin\xf3mio s\xf3 pode ter uma letra')
   f=N.frac(x0[0],10**6)
   q=Q.R(f[0],f[1])if f else None
   N.need(q is not None,'Escreve o valor como inteiro, decimal ou fra\xe7\xe3o')
   r=Q.valor(P,{ls[0]:q})if ls else P.get((),Q.Z)
   o.append('Valor para '+(ls[0]if ls else 'x')+' = '+Q.qs(q)+': '+Q.qs(r))
  st=('Casos not\xe1veis: (a + b)\xb2 = a\xb2 + 2ab + b\xb2; (a - b)\xb2 = a\xb2 - 2ab + b\xb2; (a + b)(a - b) = a\xb2 - b\xb2.\nMultiplicar polin\xf3mios: cada termo de um por cada termo do outro.\nTermos s'
'emelhantes: a mesma parte literal; somam-se os coeficientes.')
  return('\n'.join(o),st,Q.qf(r)if r else None,'')
 def isq(n):
  if n<0:
   return None
  k=int(n**0.5)
  while k*k>n:
   k-=1
  while(k+1)*(k+1)<=n:
   k+=1
  return k if k*k==n else None
 def lin(q,p,x):
  if p==0:
   return x
  s=(''if q==1 else str(q))+x+(' - '+str(p)if p>0 else ' + '+str(-p))
  return '('+s+')'
 def pobj(cs,x):
  return Q.pstr(Q.decoefs(cs,x))
 def divide(cs,r):
  n=len(cs)-1
  q=[Q.Z]*n
  acc=Q.Z
  for i in range(n,0,-1):
   acc=Q.add(cs[i],Q.mul(r,acc))
   q[i-1]=acc
  return(q,Q.add(cs[0],Q.mul(r,acc)))
 def fatq(cs,x,o,fs,zs):
  c,b,a=(cs[0][0],cs[1][0],cs[2][0])
  D=b*b-4*a*c
  ka,kc=(isq(a),isq(abs(c)))
  if b==0 and c<0 and ka and kc:
   o.append('Diferen\xe7a de quadrados: '+pobj(cs,x)+' = '+('('+str(ka)+x+')'if ka>1 else x)+'\xb2 - '+str(kc)+'\xb2')
   fs+=[lin(ka,kc,x),lin(ka,-kc,x)]
   zs+=[Q.R(kc,ka),Q.R(-kc,ka)]
   return
  if D==0 and ka and kc:
   sg=-1 if b*c<0 or b<0 else 1
   o.append('Quadrado do bin\xf3mio: '+pobj(cs,x)+' = '+lin(ka,-sg*kc,x)+'\xb2')
   fs+=[lin(ka,-sg*kc,x)]*2
   zs+=[Q.R(-sg*kc,ka)]
   return
  o.append('\u0394 = b\xb2 - 4ac = '+str(D))
  if D<0:
   o.append('\u0394 < 0: '+pobj(cs,x)+' n\xe3o tem zeros reais; n\xe3o se decomp\xf5e em fatores do 1.\xba grau.')
   fs.append('('+pobj(cs,x)+')')
   return
  k=isq(D)
  if k is not None:
   r1,r2=(Q.R(-b+k,2*a),Q.R(-b-k,2*a))
   o.append('Zeros (f\xf3rmula resolvente): '+Q.qs(r2)+' e '+Q.qs(r1))
   f=[lin(r1[1],r1[0],x),lin(r2[1],r2[0],x)]
   k2=Q.R(a,r1[1]*r2[1])
   if k2!=Q.UM:
    fs.append(Q.qs(k2))
   fs+=f
   zs+=[r2,r1]
   return
  kk,m=(1,D)
  for p,e in Q.fatores(D):
   kk*=p**(e//2)
   m//=p**(2*(e//2))
  g=Q.mdc(Q.mdc(b,kk),2*a)
  rr=(str(kk//g)if kk//g>1 else '')+'\u221a'+str(m)
  den='/'+str(2*a//g)if 2*a//g>1 else ''
  if b:
   z1=('('if den else '')+str(-b//g)+' + '+rr+(')'if den else '')+den
   z2=('('if den else '')+str(-b//g)+' - '+rr+(')'if den else '')+den
  else:
   z1,z2=(rr+den,'-'+rr+den)
  o.append('Zeros irracionais: '+z2+' \u2248 '+N.fmt((-b-D**0.5)/(2*a))+' e '+z1+' \u2248 '+N.fmt((-b+D**0.5)/(2*a)))
  fs.append((str(a)if a!=1 else '')+fz(z1,x)+fz(z2,x))
  zs+=[z2,z1]
 def fz(z,x):
  if z.startswith('-')and ' 'not in z:
   return '('+x+' + '+z[1:]+')'
  if ' 'in z and(not z.startswith('(')):
   return '('+x+' - ('+z+'))'
  return '('+x+' - '+z+')'
 def fat():
  return('Fatorizar e resolver por fatoriza\xe7\xe3o',[N.fld('Polin\xf3mio ou equa\xe7\xe3o (... = ...)','','x^3 - 4x','t')],_fat)
 def _fat(v):
  s=v[0]
  N.need(s,'Escreve um polin\xf3mio, por exemplo x^2 - 9')
  eq='='in s
  if eq:
   N.need(s.count('=')==1,'S\xf3 um sinal =')
   a,b=s.split('=')
   N.need(a.strip()and b.strip(),'Falta um membro da equa\xe7\xe3o')
   P=Q.padd(Q.poli(Q.arvore(a)),Q.poli(Q.arvore(b)),-1)
  else:
   P=Q.poli(Q.arvore(s))
  N.need(P,'O polin\xf3mio \xe9 nulo')
  ls=sorted(set([x for m in P for x,e in m]))
  o=[]
  if eq:
   o.append('Tudo no 1.\xba membro: '+Q.pstr(P)+' = 0')
  L=Q.denl(P)
  Pi=Q.pesc(P,(L,1))
  g=0
  for m in Pi:
   g=Q.mdc(g,Pi[m][0])
  lead=Pi[Q.ordem(Pi)[0]][0]
  c=Q.R(g if lead>0 else-g,L)
  mins={}
  for x in ls:
   mins[x]=min([dict(m).get(x,0)for m in P])
  fm=tuple([(x,mins[x])for x in ls if mins[x]])
  R={}
  for m in P:
   d=dict(m)
   m2=tuple([(x,d[x]-mins.get(x,0))for x in sorted(d)if d[x]-mins.get(x,0)])
   R[m2]=Q.div(P[m],c)
  ca=(abs(c[0]),c[1])
  fc=('-'if c[0]<0 else '')+(''if ca==Q.UM else '('+Q.qs(ca)+')'if ca[1]>1 else Q.qs(ca))+Q.mstr(fm)
  if fc=='-':
   o.append('Sinal - em evid\xeancia: '+Q.pstr(P)+' = -('+Q.pstr(R)+')')
  elif fc:
   o.append('Fator comum: '+fc+', logo '+Q.pstr(P)+' = '+fc+'('+Q.pstr(R)+')')
  fs=[]
  zs=[]
  if len(ls)>1:
   N.need(not eq,'Para resolver, a equa\xe7\xe3o s\xf3 pode ter uma letra')
   res=fc+'('+Q.pstr(R)+')'if fc else Q.pstr(P)
   o.append('> '+res)
   return('\n'.join(o),ST_FAT,None,'')
  x=ls[0]if ls else 'x'
  if fm:
   zs.append(Q.Z)
  cs=Q.coefs(R,x)if R else[Q.UM]
  while len(cs)>3:
   rs=Q.raizes_rac(cs)
   if not rs:
    o.append(pobj(cs,x)+' n\xe3o tem zeros racionais.')
    fs.append('('+pobj(cs,x)+')')
    cs=None
    break
   r=rs[0]
   qcs,resto=divide(cs,r)
   o.append(x+' = '+Q.qs(r)+' \xe9 zero (resto 0): divide-se por '+lin(r[1],r[0],x)+' [Ruffini]')
   fs.append(lin(r[1],r[0],x))
   zs.append(r)
   cs=[Q.div(y,(r[1],1))for y in qcs]
  if cs is not None:
   if len(cs)==3:
    fatq(cs,x,o,fs,zs)
   elif len(cs)==2:
    fs.append(lin(cs[1][0],-cs[0][0],x)if cs[1][0]>0 else '('+pobj(cs,x)+')')
    zs.append(Q.div(Q.neg(cs[0]),cs[1]))
  txt=junta(fc,fs)
  o.append('> '+Q.pstr(P)+' = '+txt)
  if eq:
   reais=[z for z in zs if not isinstance(z,str)]
   reais.sort(key=lambda z:Q.qf(z))
   irr=[z for z in zs if isinstance(z,str)]
   vs=[Q.vstr(z)for z in reais]+irr
   o.append('Lei do anulamento do produto: cada fator igual a zero.')
   o.append('> C.S. = '+('{'+'; '.join(vs)+'}'if vs else '\u2205'))
  return('\n'.join(o),ST_FAT,None,'')
 def junta(fc,fs):
  o=[]
  for f in fs:
   for k in range(len(o)):
    if o[k][0]==f:
     o[k][1]+=1
     break
   else:
    o.append([f,1])
  t=''.join([f+(N.sup(n)if n>1 else '')for f,n in o])
  return fc+t if fc and fc!='-'else(fc or '')+t
 ST_FAT=('Por ordem: fator comum; casos not\xe1veis (a\xb2 - b\xb2 = (a - b)(a + b); a\xb2 \xb1 2ab + b\xb2 = (a \xb1 b)\xb2); zeros (com a f\xf3rmula resolvente ou a regra de Ruffini).\nLei do anulamento do pr'
'oduto: a \xd7 b = 0 \u21d4 a = 0 \u2228 b = 0.')
 return _ns('N Q pol divide fat',N,Q,pol,divide,fat)


_F['c_mpol'] = _m_c_mpol


def _m_c_mprb():
 N=_imp('m1_nucleo')
 Q=_imp('m1_q')
 def toks(t):
  return t.replace(';',' ').split()
 def qnum(p):
  try:
   return Q.cte(Q.poli(Q.arvore(p)))
  except ValueError:
   return None
 def ap(x,d):
  s,ex=N.fmt2(x,0,d)
  return(''if ex else N.AP+' ')+s
 def pr(a,b):
  s=str(a)+'/'+str(b)
  if a==0 or a==b:
   return s+' = '+('0'if a==0 else '1')+(' = 0%'if a==0 else ' = 100%')
  q=Q.R(a,b)
  if q!=(a,b):
   s+=' = '+Q.qs(q)
  x=a/b
  d,e1=N.fmt2(x,0,2)
  p,e2=N.fmt2(100*x,0,1)
  return s+(' = 'if e1 else ' '+N.AP+' ')+d+(' = 'if e2 else ' '+N.AP+' ')+p+'%'
 def escala(a,b):
  if a==0:
   return 'imposs\xedvel'
  if a==b:
   return 'certo'
  return 'pouco prov\xe1vel'if 2*a<b else 't\xe3o prov\xe1vel como improv\xe1vel'if 2*a==b else 'muito prov\xe1vel'
 def freq():
  return('Tabela de frequ\xeancias',[N.fld('Dados (ou os valores diferentes)','','3 5 4 3 2 5 3 4 1 3','t'),N.fld('Frequ\xeancias absolutas (opcional)','','','t')],_freq)
 def _freq(v):
  ts=toks(v[0])
  N.need(ts,'Escreve os dados separados por espa\xe7os')
  if v[1].strip():
   fs=toks(v[1])
   N.need(len(fs)==len(ts),'H\xe1 '+str(len(ts))+' valores e '+str(len(fs))+' frequ\xeancias')
   cs=[]
   for f in fs:
    q=qnum(f)
    N.need(q is not None and q[1]==1 and(q[0]>=0),'As frequ\xeancias absolutas s\xe3o n\xfameros inteiros (0, 1, 2...)')
    cs.append(q[0])
   vs=ts
  else:
   vs,cs=([],[])
   for t in ts:
    if t in vs:
     cs[vs.index(t)]+=1
    else:
     vs.append(t)
     cs.append(1)
  qs=[qnum(t)for t in vs]
  num=None not in qs
  if num:
   d={}
   for i in range(len(qs)):
    d[qs[i]]=d.get(qs[i],0)+cs[i]
   ks=sorted(d.keys(),key=Q.qf)
   cs=[d[k]for k in ks]
   vs=[Q.vstr(k)for k in ks]
  else:
   N.need(len(set([N.low(x)for x in vs]))==len(vs)or not v[1].strip(),'H\xe1 valores repetidos: escreve cada valor uma s\xf3 vez')
  n=sum(cs)
  N.need(n>0,'O total das frequ\xeancias \xe9 0')
  o=['n = '+str(n)+' dados '+('quantitativos'if num else 'qualitativos')+'; '+str(len(vs))+' valores diferentes.','Valor \u2192 freq. absoluta; relativa; \xe2ngulo no gr\xe1fico circular']
  ac=0
  for i in range(len(vs)):
   ac+=cs[i]
   o.append(vs[i]+' \u2192 '+str(cs[i])+'; '+pr(cs[i],n)+'; '+ap(360*cs[i]/n,1)+'\xb0'+('; acumulada '+str(ac)if num else ''))
  o.append('Soma das frequ\xeancias relativas: 1 (100%); dos \xe2ngulos: 360\xb0.')
  m=max(cs)
  mo=[vs[i]for i in range(len(vs))if cs[i]==m]
  if len(mo)==len(vs)and len(vs)>1:
   o.append('> N\xe3o h\xe1 moda: todos os valores t\xeam a mesma frequ\xeancia.')
  else:
   o.append('> Moda: '+', '.join(mo)+' (frequ\xeancia '+str(m)+')'+(' - bimodal'if len(mo)==2 else ''))
  r=None
  if num:
   s=Q.Z
   for i in range(len(ks)):
    s=Q.add(s,Q.mul(ks[i],(cs[i],1)))
   r=Q.div(s,(n,1))
   if len(ks)<=8:
    t=' + '.join([Q.vstr(ks[i])+' '+N.X+' '+str(cs[i])for i in range(len(ks))])
    o.append('> M\xe9dia = ('+t+') / '+str(n)+' = '+Q.vstr(s)+' / '+str(n)+' '+rq(r,Q.R(s[0],s[1]*n)))
   else:
    o.append('> M\xe9dia = soma / n = '+Q.vstr(s)+' / '+str(n)+' '+rq(r,Q.R(s[0],s[1]*n)))
   def pos(k):
    a=0
    for i in range(len(ks)):
     a+=cs[i]
     if a>=k:
      return ks[i]
   if n%2:
    me=pos((n+1)//2)
    o.append('> Mediana: '+Q.vstr(me)+' (n \xedmpar: valor na posi\xe7\xe3o '+str((n+1)//2)+')')
   else:
    a,b=(pos(n//2),pos(n//2+1))
    me=Q.div(Q.add(a,b),(2,1))
    o.append('> Mediana: ('+Q.vstr(a)+' + '+Q.vstr(b)+') / 2 '+rq(me)+' (n par: posi\xe7\xf5es '+str(n//2)+' e '+str(n//2+1)+')')
   o.append('> Amplitude: '+Q.vstr(ks[-1])+' - '+Q.vstr(ks[0])+' = '+Q.vstr(Q.sub(ks[-1],ks[0])))
   r=Q.qf(r)
  else:
   o.append('Dados qualitativos: n\xe3o h\xe1 m\xe9dia nem mediana (s\xf3 moda).')
  st='Frequ\xeancia relativa = frequ\xeancia absoluta / n.\n\xc2ngulo do setor no gr\xe1fico circular = frequ\xeancia relativa '+N.X+' 360\xb0.\nMediana: ordenam-se os dados e escolhe-se o do meio (ou a m\xe9dia dos dois do meio).'
  gr=barras(vs,cs)if len(vs)<=12 else None
  return('\n'.join(o),st,r,'',gr)if gr else('\n'.join(o),st,r,'')
 def rq(q,d=None):
  s=Q.vstr(q)
  if '/'not in s:
   return '= '+s
  a=N.AP+' '+N.fmt(Q.qf(q),0,2)
  return a if q==d else '= '+s+' '+a
 def barras(vs,cs):
  k=len(vs)
  m=max(cs)
  sg=[]
  for i in range(k):
   x=i+1
   sg+=[(x-0.3,0,x-0.3,cs[i]),(x-0.3,cs[i],x+0.3,cs[i]),(x+0.3,cs[i],x+0.3,0)]
  w=4 if k<=6 else 2
  return('Gr\xe1fico de barras',[('s',sg,4),('t',[(i+0.75,cs[i]+0.02*m,str(cs[i]))for i in range(k)],0),('t',[(i+0.7,-0.2*m,vs[i][:w])for i in range(k)],2)],0.3,k+0.7,-0.26*m,1.18*m,'barras: frequ\xeancias absolutas')
 def casos(t):
  out=[]
  for p in toks(t):
   q=qnum(p)
   if q is not None:
    N.need(q[1]==1 and q[0]>=0,'O n\xfamero de casos tem de ser um inteiro: '+p)
    out.append([q[0],''])
   else:
    N.need(out,'Come\xe7a por um n\xfamero (ex.: 3 azuis 5 vermelhas)')
    out[-1][1]=(out[-1][1]+' '+p).strip()
  N.need(out,'Escreve os casos (ex.: 3 azuis 5 vermelhas)')
  return out
 def acha(w,nomes):
  w=N.low(w)
  best,bi,dup=(0,-1,0)
  for i in range(len(nomes)):
   a=N.low(nomes[i])
   k=0
   while k<min(len(a),len(w))and a[k]==w[k]:
    k+=1
   if a==w:
    return i
   if k>best:
    best,bi,dup=(k,i,0)
   elif k==best:
    dup=1
  N.need(bi>=0 and best>=min(3,len(w)),'N\xe3o conhe\xe7o "'+w+'"; usa um dos nomes: '+', '.join(nomes))
  N.need(not dup,'"'+w+'" pode ser mais do que um nome; escreve mais letras ('+', '.join(nomes)+')')
  return bi
 def prob():
  return('Probabilidade (Laplace)',[N.fld('Casos (ex.: 3 azuis 5 vermelhas)','','3 azuis 5 vermelhas 2 verdes','t'),N.fld('Acontecimento (ex.: azuis verdes)','','azuis','t')],_prob)
 def _prob(v):
  cs=casos(v[0])
  if len(cs)==2 and(not cs[0][1])and(not cs[1][1]):
   a,b=(cs[0][0],cs[1][0])
   N.need(b>0,'Os casos poss\xedveis n\xe3o podem ser 0')
   N.need(a<=b,'Os casos favor\xe1veis n\xe3o podem ser mais do que os poss\xedveis')
   o=['= P(A) = casos favor\xe1veis / casos poss\xedveis','> P(A) = '+pr(a,b)]
  else:
   nomes=[c[1]for c in cs]
   N.need(''not in nomes,'D\xe1 um nome a cada grupo (ex.: 3 azuis 5 vermelhas)')
   b=sum([c[0]for c in cs])
   N.need(b>0,'N\xe3o h\xe1 casos poss\xedveis')
   o=['Casos poss\xedveis: '+' + '.join([str(c[0])for c in cs])+' = '+str(b)+' (igualmente prov\xe1veis).']
   for c in cs:
    o.append('P('+c[1]+') = '+pr(c[0],b))
   ws=toks(v[1])
   if not ws:
    return('\n'.join(o),ST_LAP,None,'')
   neg=N.low(ws[0])in('nao','n')
   if neg:
    ws=ws[1:]
    N.need(ws,'Escreve o que vem depois de "n\xe3o"')
   ix=[]
   for w in ws:
    i=acha(w,nomes)
    if i not in ix:
     ix.append(i)
   if neg:
    ix=[i for i in range(len(cs))if i not in ix]
   a=sum([cs[i][0]for i in ix])
   nm=' ou '.join([cs[i][1]for i in ix])or 'nenhum'
   o+=['Acontecimento A: '+nm,'= P(A) = casos favor\xe1veis / casos poss\xedveis','> P(A) = '+('('+' + '.join([str(cs[i][0])for i in ix])+')/'+str(b)+' = 'if len(ix)>1 else '')+pr(a,b)]
  o+=['Contr\xe1rio: P(n\xe3o A) = 1 - P(A) = '+pr(b-a,b),'A \xe9 um acontecimento '+escala(a,b)+'.']
  return('\n'.join(o),ST_LAP,a/b,'')
 ST_LAP='Lei de Laplace (casos igualmente prov\xe1veis): P(A) = casos favor\xe1veis / casos poss\xedveis.\n0 \u2264 P(A) \u2264 1; P(n\xe3o A) = 1 - P(A).'
 OPD=['Soma de dois dados','Produto de dois dados','Diferen\xe7a de dois dados','Duas moedas (n.\xba de E)','Tr\xeas moedas (n.\xba de E)']
 def dados():
  return('Dois dados ou moedas',[N.fld('Experi\xeancia','','','c',OPD),N.fld('Acontecimento (ex.: 7, > 9, par, primo)','','7','t')],_dados)
 def primo(x):
  if x<2:
   return False
  d=2
  while d*d<=x:
   if x%d==0:
    return False
   d+=1
  return True
 def cond(t):
  s=N.low(t).replace(' ','')
  if not s:
   return None
  for a,b in(('pelomenos','>='),('nomaximo','<='),('maisde','>'),('menosde','<'),('igual','=')):
   if s.startswith(a):
    s=b+s[len(a):].lstrip('a')
  if s in('par','pares'):
   return('\xe9 par',lambda x:x%2==0)
  if s in('impar','impares'):
   return('\xe9 \xedmpar',lambda x:x%2==1)
  if s in('primo','primos'):
   return('\xe9 n\xfamero primo',primo)
  for a,nm in(('multiplode','\xe9 m\xfaltiplo de '),('divisorde','\xe9 divisor de ')):
   if s.startswith(a):
    k=qnum(s[len(a):])
    N.need(k is not None and k[1]==1 and(k[0]>0),'Escreve o n\xfamero depois de "'+nm[2:].strip()+'"')
    k=k[0]
    if a[0]=='m':
     return(nm+str(k),lambda x:x%k==0)
    return(nm+str(k),lambda x:x>0 and k%x==0)
  op='='
  for p in('>=','<=','!=','=','>','<'):
   if s.startswith(p):
    op,s=(p,s[len(p):])
    break
  j=0
  while j<len(s)and s[j]in '0123456789,./-':
   j+=1
  k=qnum(s[:j])if j and s[j:].isalpha()or j==len(s)else None
  N.need(k is not None,'N\xe3o percebi o acontecimento; exemplos: 7, > 9, <= 4, par, \xedmpar, primo, m\xfaltiplo de 3, pelo menos 1')
  x=Q.qf(k)
  f={'=':lambda y:y==x,'!=':lambda y:y!=x,'>':lambda y:y>x,'<':lambda y:y<x,'>=':lambda y:y>=x,'<=':lambda y:y<=x}
  return({'>=':'\u2265 ','<=':'\u2264 ','!=':'\u2260 '}.get(op,op+' ')+Q.vstr(k),f[op])
 def _dados(v):
  k=v[0]
  c=cond(v[1])
  if k<=2:
   fn=(lambda a,b:a+b,lambda a,b:a*b,lambda a,b:abs(a-b))[k]
   nm=('soma','produto','diferen\xe7a')[k]
   cs=[((a,b),fn(a,b))for a in range(1,7)for b in range(1,7)]
   o=['Tabela de dupla entrada ('+nm+'; 1.\xba dado nas linhas):']
   for a in range(1,7):
    o.append(str(a)+' | '+' '.join([str(fn(a,b))for b in range(1,7)]))
   def cx(p):
    return '('+str(p[0])+','+str(p[1])+')'
  else:
   m=2 if k==3 else 3
   nm='n.\xba de E'
   cs=[('',0)]
   for i in range(m):
    cs=[(s+l,e+(l=='E'))for s,e in cs for l in 'EN']
   o=['E: face europeia; N: face nacional. Casos: '+', '.join([s for s,e in cs])]
   def cx(p):
    return p
  n=len(cs)
  vs=sorted(set([x for p,x in cs]))
  o+=[str(n)+' casos poss\xedveis, todos igualmente prov\xe1veis.','Valores ('+nm+') e n\xfamero de casos: '+'; '.join([str(x)+': '+str(len([1 for p,y in cs if y==x]))for x in vs])]
  r=None
  fav=[]
  if c:
   fav=[p for p,x in cs if c[1](x)]
   a=len(fav)
   o.append('Acontecimento A: '+nm+' '+c[0])
   if fav:
    o.append('Casos favor\xe1veis: '+(' '.join([cx(p)for p in fav])+' \u2192 '+str(a)if a<=12 else str(a)+' (a vermelho na tabela)'))
   o.append('> P(A) = '+pr(a,n))
   r=a/n
  if k<=2:
   its=[('t',[(1.7+b,8,str(b))for b in range(1,7)]+[(0.7,7-a+1,str(a))for a in range(1,7)],2),('t',[(0.7,8,{0:'+',1:N.X,2:'-'}[k])],0),('s',[(0.5,7.9,8.4,7.9),(1.5,1.4,1.5,8.9)],7)]
   for f in(0,1):
    its.append(('t',[(1.7+p[1],8-p[0],str(x))for p,x in cs if(p in fav)==bool(f)],5 if f else 0))
   gr=('Tabela de dupla entrada: '+nm,its,0.4,8.4,1.2,9.0,'vermelho: casos favor\xe1veis'if fav else '')
   return('\n'.join(o),ST_DAD,r,'',gr)
  return('\n'.join(o),ST_DAD,r,'')
 ST_DAD='Experi\xeancia composta: contam-se todos os pares de resultados (tabela de dupla entrada ou diagrama em \xe1rvore).\nCom dois dados h\xe1 6 '+N.X+' 6 = 36 casos igualmente prov\xe1veis.'
 def urna():
  return('Duas extra\xe7\xf5es',[N.fld('Composi\xe7\xe3o (ex.: 3 azuis 2 brancas)','','3 azuis 2 brancas','t'),N.fld('Extra\xe7\xf5es','','','c',['Sem reposi\xe7\xe3o','Com reposi\xe7\xe3o']),N.fld('Acontecimento (ex.: azul branca)',
'','','t')],_urna)
 def _urna(v):
  cs=casos(v[0])
  nomes=[c[1]for c in cs]
  N.need(''not in nomes and len(cs)>=2,'Escreve pelo menos dois grupos com nome (ex.: 3 azuis 2 brancas)')
  N.need(len(cs)<=6,'No m\xe1ximo 6 grupos')
  sr=v[1]==0
  T=sum([c[0]for c in cs])
  N.need(T>=2 or not sr,'Sem reposi\xe7\xe3o s\xe3o precisas pelo menos 2 bolas')
  N.need(T>0,'A urna est\xe1 vazia')
  T2=T-1 if sr else T
  o=['Total: '+str(T)+'; duas extra\xe7\xf5es '+('sem'if sr else 'com')+' reposi\xe7\xe3o'+(' (2.\xaa extra\xe7\xe3o com '+str(T2)+')'if sr else '')+'.']
  P={}
  k=len(cs)
  for i in range(k):
   for j in range(k):
    a=cs[i][0]
    b=cs[j][0]-(1 if sr and i==j else 0)
    P[i,j]=(a*b,T*T2)
    o.append(nomes[i]+' \u2192 '+nomes[j]+': '+str(a)+'/'+str(T)+' '+N.X+' '+str(b)+'/'+str(T2)+' = '+Q.qs(Q.R(a*b,T*T2)))
  s=Q.Z
  for x in P.values():
   s=Q.add(s,Q.R(x[0],x[1]))
  o.append('Soma de todos os ramos: '+Q.qs(s)+' \u2713')
  ig=[P[i,i]for i in range(k)]
  a=sum([x[0]for x in ig])
  o+=['> Do mesmo tipo (ex.: mesma cor): '+pr(a,T*T2),'> De tipos diferentes: '+pr(T*T2-a,T*T2)]
  ws=toks(v[2])
  r=None
  if len(ws)==2:
   i,j=(acha(ws[0],nomes),acha(ws[1],nomes))
   x=P[i,j]
   o.append('> P(1.\xaa '+nomes[i]+' e 2.\xaa '+nomes[j]+') = '+pr(x[0],x[1]))
   r=x[0]/x[1]
   if i!=j:
    y=P[j,i]
    o.append('> P(uma '+nomes[i]+' e uma '+nomes[j]+', por qualquer ordem) = '+pr(x[0]+y[0],x[1]))
  elif len(ws)==1:
   i=acha(ws[0],nomes)
   d=P[i,i][0]
   u=sum([P[i,j][0]+P[j,i][0]for j in range(k)if j!=i])
   n=T*T2
   o+=['> P(duas '+nomes[i]+') = '+pr(d,n),'> P(exatamente uma '+nomes[i]+') = '+pr(u,n),'> P(pelo menos uma '+nomes[i]+') = 1 - P(nenhuma) = '+pr(d+u,n)]
   r=(d+u)/n
  else:
   N.need(not ws,'Escreve um ou dois nomes (ex.: azul branca)')
  st='Diagrama em \xe1rvore: multiplica-se ao longo dos ramos e somam-se os caminhos favor\xe1veis.\nSem reposi\xe7\xe3o, na 2.\xaa extra\xe7\xe3o h\xe1 menos uma bola (e menos uma da cor que saiu).'
  gr=arvore(cs,P,T,T2,sr)if k<=3 else None
  return('\n'.join(o),st,r,'',gr)if gr else('\n'.join(o),st,r,'')
 def arvore(cs,P,T,T2,sr):
  k=len(cs)
  ab=[]
  for c in cs:
   w=N.low(c[1])
   n=1
   while n<len(w)and[1 for d in cs if d is not c and N.low(d[1])[:n]==w[:n]]:
    n+=1
   ab.append(c[1][:max(n,3)])
  L=k*k
  x1,x2=(3.6,6.6)if k<=2 else(3.3,6.0)
  sg,rt,pb=([],[],[])
  r0=(0.8,(L+1)/2)
  for i in range(k):
   ys=[L-(i*k+j)for j in range(k)]
   n1=(x1,sum(ys)/k)
   sg.append((r0[0],r0[1],n1[0],n1[1]))
   rt.append((n1[0],n1[1],ab[i]))
   pb.append(((r0[0]+n1[0])/2-0.4,(r0[1]+n1[1])/2+0.15,str(cs[i][0])+'/'+str(T)))
   for j in range(k):
    n2=(x2,ys[j])
    sg.append((n1[0]+0.2+0.25*len(ab[i]),n1[1],n2[0],n2[1]))
    b=str(cs[j][0]-(1 if sr and i==j else 0))+'/'+str(T2)
    q=Q.qs(Q.R(P[i,j][0],P[i,j][1]))
    if k<=2:
     rt.append((n2[0],n2[1],ab[j]+'  '+q))
     pb.append(((n1[0]+n2[0])/2+0.3,(n1[1]+n2[1])/2+0.15,b))
    else:
     rt.append((n2[0],n2[1],ab[j]+' '+b+': '+q))
  return('Diagrama em \xe1rvore',[('s',sg,7),('t',rt,0),('t',pb,4)],0.5,10.5,0.3,L+0.7,'azul: probabilidade de cada ramo')
 return _ns('N Q ap pr escala freq barras casos prob dados primo cond urna arvore',N,Q,ap,pr,escala,freq,barras,casos,prob,dados,primo,cond,urna,arvore)


_F['c_mprb'] = _m_c_mprb


def _m_c_mprp():
 N=_imp('m1_nucleo')
 Q=_imp('m1_q')
 def numeros(t,nm,falta=False):
  out=[]
  for p in t.replace(';',' ').split():
   if falta and p=='?':
    out.append(None)
   else:
    c=Q.cte(Q.poli(Q.arvore(p)))
    N.need(c is not None,nm+': s\xf3 n\xfameros'+(' ou ?'if falta else ''))
    out.append(c)
  return out
 def sub(i):
  return ''.join([chr(8320+int(c))for c in str(i)])
 def seq():
  return('Sequ\xeancias: termo geral',[N.fld('Primeiros termos','','3 7 11 15','t'),N.fld('Termo de ordem n (opcional)','','','o'),N.fld('Este n\xfamero \xe9 termo? (opcional)','','','t')],_seq)
 def _seq(v):
  us=numeros(v[0],'Os termos')
  N.need(len(us)>=3,'Escreve pelo menos 3 termos')
  ds=[Q.sub(us[i+1],us[i])for i in range(len(us)-1)]
  o=['Diferen\xe7as entre termos seguidos: '+', '.join([Q.qs(d)for d in ds])]
  tipo=None
  if all_eq(ds):
   d=ds[0]
   G=Q.decoefs([Q.sub(us[0],d),d],'n')
   o.append('Diferen\xe7a constante '+Q.qs(d)+': sequ\xeancia aritm\xe9tica.')
   o.append('Lei de recorr\xeancia: u(n+1) = u(n) '+('+ '+Q.qs(d)if d[0]>=0 else '- '+Q.qs(Q.neg(d))))
   tipo='a'
  else:
   d2=[Q.sub(ds[i+1],ds[i])for i in range(len(ds)-1)]
   if len(us)>=4 and all_eq(d2):
    a=Q.div(d2[0],(2,1))
    b=Q.sub(Q.sub(us[1],us[0]),Q.mul((3,1),a))
    c=Q.sub(Q.sub(us[0],a),b)
    G=Q.decoefs([c,b,a],'n')
    o.append('Segundas diferen\xe7as constantes ('+Q.qs(d2[0])+'): o termo geral \xe9 do 2.\xba grau em n.')
    tipo='q'
   elif not[u for u in us if u[0]==0]:
    rs=[Q.div(us[i+1],us[i])for i in range(len(us)-1)]
    N.need(all_eq(rs),'N\xe3o encontrei uma regra simples (nem diferen\xe7as constantes, nem raz\xe3o constante)')
    r=rs[0]
    o.append('Raz\xe3o constante '+Q.qs(r)+': sequ\xeancia geom\xe9trica (aprofundamento).')
    tipo='g'
   else:
    N.err('N\xe3o encontrei uma regra simples (nem diferen\xe7as constantes, nem raz\xe3o constante)')
  if tipo=='g':
   o.append('> Termo geral: u(n) = '+Q.qp(us[0])+' \xd7 '+Q.qp(r)+'^(n - 1)')
   def termo(n):
    return Q.mul(us[0],Q.pw(r,n-1))
  else:
   o.append('> Termo geral: u(n) = '+Q.pstr(G))
   def termo(n):
    return Q.valor(G,{'n':(n,1)})
  ok=[termo(i+1)==us[i]for i in range(len(us))]
  o.append('Confirma\xe7\xe3o com os termos dados: '+('\u2713'if all(ok)else '\u2717'))
  if v[1]is not None:
   n=v[1][0]
   N.need(n==int(n)and 1<=n<=10**6,'A ordem n tem de ser um inteiro positivo')
   n=int(n)
   o.append('u'+sub(n)+' = '+Q.qs(termo(n)))
  if v[2]:
   t=numeros(v[2],'O n\xfamero')
   N.need(len(t)==1,'Escreve um s\xf3 n\xfamero para verificar')
   t=t[0]
   n=ordem(tipo,G if tipo!='g'else None,us,termo,t)
   if n:
    o.append(Q.qs(t)+' \xe9 termo: \xe9 o termo de ordem '+str(n)+'.')
   else:
    o.append(Q.qs(t)+' n\xe3o \xe9 termo da sequ\xeancia (n\xe3o h\xe1 n inteiro positivo).')
  st=('Termo geral: a express\xe3o de u(n) em fun\xe7\xe3o da ordem n.\nAritm\xe9tica (diferen\xe7a d constante): u(n) = d n + (u(1) - d).\nPara ver se um n\xfamero \xe9 termo: resolve-se u(n) = n\xfamero e '
'v\xea-se se n \xe9 inteiro positivo.')
  return('\n'.join(o),st,None,'')
 def all_eq(xs):
  for x in xs:
   if x!=xs[0]:
    return False
  return True
 def ordem(tipo,G,us,termo,t):
  if tipo=='a':
   d=G.get((('n',1),),Q.Z)
   c=G.get((),Q.Z)
   if d[0]==0:
    return 1 if c==t else 0
   n=Q.div(Q.sub(t,c),d)
   return n[0]if n[1]==1 and n[0]>=1 else 0
  for n in range(1,2001):
   u=termo(n)
   if u==t:
    return n
   if tipo=='g'and abs(u[0])>abs(t[0])*u[1]*10**6+10**6:
    break
  return 0
 def tabela(tx,ty):
  xs=numeros(tx,'Os valores de x',True)
  ys=numeros(ty,'Os valores de y',True)
  N.need(len(xs)==len(ys),'H\xe1 '+str(len(xs))+' valores de x e '+str(len(ys))+' de y')
  N.need(len(xs)>=1,'Escreve os valores')
  for i in range(len(xs)):
   N.need(xs[i]is not None or ys[i]is not None,'Na coluna '+str(i+1)+' faltam os dois valores')
  return(xs,ys)
 def prop():
  return('Proporcionalidade direta',[N.fld('Valores de x (? = em falta)','','2 3 5 ?','t'),N.fld('Valores de y (? = em falta)','','6 9 ? 21','t')],_prop)
 def _prop(v):
  xs,ys=tabela(v[0],v[1])
  ks=[]
  o=[]
  for i in range(len(xs)):
   if xs[i]is not None and ys[i]is not None:
    N.need(xs[i][0]!=0,'Com x = 0, o quociente y/x n\xe3o existe')
    k=Q.div(ys[i],xs[i])
    ks.append(k)
    o.append(Q.qs(ys[i])+' : '+Q.qp(xs[i])+' = '+Q.qs(k))
  N.need(ks,'\xc9 preciso pelo menos um par (x, y) completo')
  if not all_eq(ks):
   o.append('> Os quocientes y/x n\xe3o s\xe3o todos iguais: x e y n\xe3o s\xe3o diretamente proporcionais.')
   return('\n'.join(o),ST_PROP,None,'')
  k=ks[0]
  o.append('> Constante de proporcionalidade: k = y/x = '+Q.qs(k)+'; y = '+(Q.pstr({(('x',1),):k})if k[0]else '0'))
  for i in range(len(xs)):
   if xs[i]is None:
    N.need(k[0],'Com k = 0 n\xe3o se pode calcular x')
    xs[i]=Q.div(ys[i],k)
    o.append('x = y : k = '+Q.qs(ys[i])+' : '+Q.qp(k)+' = '+Q.qs(xs[i]))
   elif ys[i]is None:
    ys[i]=Q.mul(k,xs[i])
    o.append('y = k \xd7 x = '+Q.qs(k)+' \xd7 '+Q.qp(xs[i])+' = '+Q.qs(ys[i]))
  o.append('Tabela: '+'; '.join(['('+Q.vstr(xs[i])+Q.sepr(xs[i],ys[i])+Q.vstr(ys[i])+')'for i in range(len(xs))]))
  fx=[Q.qf(x)for x in xs]
  fy=[Q.qf(y)for y in ys]
  x1=max([abs(x)for x in fx]+[1.0])*1.2
  y1=max([abs(y)for y in fy]+[1.0])*1.2
  gr=('y = '+Q.qs(k)+'x',[('f',lambda t:Q.qf(k)*t,4),('p',list(zip(fx,fy)),5)],-x1*0.2,x1,-y1*0.2,y1,'reta que passa na origem; pontos: a tabela')
  return('\n'.join(o),ST_PROP,Q.qf(k),'',gr)
 ST_PROP='Proporcionalidade direta: y/x \xe9 sempre o mesmo n\xfamero k (constante de proporcionalidade); y = kx.\nO gr\xe1fico \xe9 uma reta que passa na origem.\nRegra de tr\xeas simples: valor em falta = k \xd7 x ou y : k.'
 def inv():
  return('Proporcionalidade inversa',[N.fld('Valores de x (? = em falta)','','2 4 5 ?','t'),N.fld('Valores de y (? = em falta)','','10 5 ? 2','t')],_inv)
 def _inv(v):
  xs,ys=tabela(v[0],v[1])
  ks=[]
  o=[]
  for i in range(len(xs)):
   if xs[i]is not None and ys[i]is not None:
    k=Q.mul(xs[i],ys[i])
    ks.append(k)
    o.append(Q.qs(xs[i])+' \xd7 '+Q.qp(ys[i])+' = '+Q.qs(k))
  N.need(ks,'\xc9 preciso pelo menos um par (x, y) completo')
  if not all_eq(ks)or ks[0][0]==0:
   o.append('> Os produtos x \xd7 y n\xe3o s\xe3o todos iguais (ou s\xe3o 0): x e y n\xe3o s\xe3o inversamente proporcionais.')
   return('\n'.join(o),ST_INV,None,'')
  k=ks[0]
  o.append('> Constante: k = x \xd7 y = '+Q.qs(k)+'; y = '+Q.qs(k)+'/x')
  for i in range(len(xs)):
   if xs[i]is None:
    N.need(ys[i][0],'y = 0 n\xe3o \xe9 poss\xedvel na proporcionalidade inversa')
    xs[i]=Q.div(k,ys[i])
    o.append('x = k : y = '+Q.qs(k)+' : '+Q.qp(ys[i])+' = '+Q.qs(xs[i]))
   elif ys[i]is None:
    N.need(xs[i][0],'x = 0 n\xe3o \xe9 poss\xedvel na proporcionalidade inversa')
    ys[i]=Q.div(k,xs[i])
    o.append('y = k : x = '+Q.qs(k)+' : '+Q.qp(xs[i])+' = '+Q.qs(ys[i]))
  o.append('Tabela: '+'; '.join(['('+Q.vstr(xs[i])+Q.sepr(xs[i],ys[i])+Q.vstr(ys[i])+')'for i in range(len(xs))]))
  fx=[Q.qf(x)for x in xs]
  fy=[Q.qf(y)for y in ys]
  kf=Q.qf(k)
  x1=max([abs(x)for x in fx]+[1.0])*1.3
  y1=max([abs(y)for y in fy]+[1.0])*1.3
  def f(t):
   N.need(abs(t)>1e-09,'')
   return kf/t
  gr=('y = '+Q.qs(k)+'/x',[('f',f,4),('p',list(zip(fx,fy)),5)],0,x1,0 if kf>0 else-y1,y1 if kf>0 else 0,'ramo de hip\xe9rbole; pontos: a tabela')
  return('\n'.join(o),ST_INV,kf,'',gr)
 ST_INV='Proporcionalidade inversa: x \xd7 y \xe9 sempre o mesmo n\xfamero k; y = k/x.\nQuando x duplica, y passa a metade.\nO gr\xe1fico (x > 0) \xe9 um ramo de hip\xe9rbole.'
 TIPOS=['p% de a','a em % de b','a com aumento de p%','a com desconto de p%','valor inicial (a j\xe1 com aumento de p%)','valor inicial (a j\xe1 com desconto de p%)','varia\xe7\xe3o percentual de a para b']
 def perc():
  return('Percentagens',[N.fld('Calcular','','','c',TIPOS),N.fld('Valor a','','80','o'),N.fld('Valor b','','','o'),N.fld('Percentagem p (%)','','15','o')],_perc)
 def qv(x,nm):
  N.need(x is not None,'Escreve '+nm)
  f=N.frac(x[0],10**6)
  return Q.R(f[0],f[1])if f else None
 def _perc(v):
  t,a,b,p=v
  o=[]
  cem=(100,1)
  if t in(0,2,3,4,5):
   a=qv(a,'o valor a')
   p=qv(p,'a percentagem p')
   N.need(a is not None and p is not None,'Valores com demasiadas casas decimais')
   f=Q.div(p,cem)
  if t==0:
   r=Q.mul(f,a)
   o+=['= p% de a = (p/100) \xd7 a','> '+Q.vstr(p)+'% de '+Q.vstr(a)+' = '+Q.vstr(f)+' \xd7 '+Q.vstr(a)+' = '+Q.vstr(r)]
  elif t==1 or t==6:
   a=qv(a,'o valor a')
   b=qv(b,'o valor b')
   N.need(a is not None and b is not None,'Valores com demasiadas casas decimais')
   if t==1:
    N.need(b[0],'b n\xe3o pode ser 0')
    r=Q.mul(Q.div(a,b),cem)
    o+=['= a/b \xd7 100','> '+Q.vstr(a)+' \xe9 '+pt(r)+' de '+Q.vstr(b)]
   else:
    N.need(a[0],'O valor inicial a n\xe3o pode ser 0')
    r=Q.mul(Q.div(Q.sub(b,a),a),cem)
    o+=['= (b - a)/a \xd7 100','> Varia\xe7\xe3o: '+('+'if r[0]>0 else '')+pt(r)+(' (aumento)'if r[0]>0 else ' (diminui\xe7\xe3o)'if r[0]<0 else '')]
  else:
   up=t in(2,4)
   N.need(up or Q.cmp(p,cem)<0,'Um desconto tem de ser menor do que 100%')
   fat=Q.add((1,1),f)if up else Q.sub((1,1),f)
   if t in(2,3):
    r=Q.mul(a,fat)
    o+=['= a \xd7 (1 '+('+'if up else '-')+' p/100)','> '+Q.vstr(a)+' \xd7 '+Q.vstr(fat)+' = '+Q.vstr(r)]
   else:
    r=Q.div(a,fat)
    o+=['= a : (1 '+('+'if up else '-')+' p/100)','> '+Q.vstr(a)+' : '+Q.vstr(fat)+' = '+Q.vstr(r)]
  if '/'in Q.vstr(r):
   o.append('Valor aproximado: '+N.fmt(Q.qf(r),0,2))
  st='p% = p/100. Aumento de p%: \xd7 (1 + p/100); desconto de p%: \xd7 (1 - p/100).\nValor inicial: divide-se pelo fator.\nVaria\xe7\xe3o percentual: (novo - antigo)/antigo \xd7 100.'
  return('\n'.join(o),st,Q.qf(r),'')
 def pt(r):
  s=Q.vstr(r)
  return(s if '/'not in s else N.AP+' '+N.fmt(Q.qf(r),0,2))+'%'
 return _ns('N Q sub seq ordem tabela prop inv perc',N,Q,sub,seq,ordem,tabela,prop,inv,perc)


_F['c_mprp'] = _m_c_mprp


def _m_c_mrea():
 import math
 N=_imp('m1_nucleo')
 Q=_imp('m1_q')
 def valor(s,nm):
  s=s.replace(' ','')
  N.need(s,'Escreve '+nm)
  t=Q.arvore(s)
  N.need(not Q.letras(t),nm[0].upper()+nm[1:]+' n\xe3o pode ter letras')
  c=Q.cte(Q.poli(t))
  return c if c is not None else Q.Z
 def expo(v):
  a=(abs(v[0]),v[1])
  n=int(math.floor(math.log10(Q.qf(a))))if Q.qf(a)>0 else 0
  while Q.cmp(a,Q.pw((10,1),n))<0:
   n-=1
  while Q.cmp(a,Q.pw((10,1),n+1))>=0:
   n+=1
  return n
 def cien(v):
  N.need(v[0]!=0,'0 n\xe3o se escreve em nota\xe7\xe3o cient\xedfica')
  n=expo(v)
  m=Q.div(v,Q.pw((10,1),n))
  return(m,n)
 def mtxt(m):
  s=Q.vstr(m)
  if '/'in s or '('in s or len(s)>12:
   return N.AP+' '+N.fsf(Q.qf(m),4)
  return s
 def ctxt(m,n):
  s=mtxt(m)
  return s+' \xd7 10'+N.sup(n)
 def ncie():
  return('Nota\xe7\xe3o cient\xedfica',[N.fld('N\xfamero A','','0,00052','t'),N.fld('N\xfamero B (opcional)','','','t'),N.fld('Opera\xe7\xe3o','','','c',['s\xf3 escrever A em nota\xe7\xe3o cient\xedfica',
'A \xd7 B','A : B','A + B','A - B'])],_ncie)
 def _ncie(v):
  ta,tb,op=v
  A=valor(ta,'o n\xfamero A')
  ma,na=cien(A)
  o=['A = '+ctxt(ma,na)]
  r=A
  if op:
   B=valor(tb,'o n\xfamero B')
   mb,nb=cien(B)
   o.append('B = '+ctxt(mb,nb))
   if op==1:
    m=Q.mul(ma,mb)
    o.append('= ('+mtxt(ma)+' \xd7 '+mtxt(mb)+') \xd7 10^('+str(na)+' + '+qn(nb)+')')
    o.append('= '+mtxt(m)+' \xd7 10'+N.sup(na+nb))
    r=Q.mul(A,B)
   elif op==2:
    m=Q.div(ma,mb)
    o.append('= ('+mtxt(ma)+' : '+mtxt(mb)+') \xd7 10^('+str(na)+' - '+qn(nb)+')')
    o.append('= '+mtxt(m)+' \xd7 10'+N.sup(na-nb))
    r=Q.div(A,B)
   else:
    k=max(na,nb)
    a2=Q.div(A,Q.pw((10,1),k))
    b2=Q.div(B,Q.pw((10,1),k))
    sg=' + 'if op==3 else ' - '
    o.append('Mesma pot\xeancia de 10: '+mtxt(a2)+' \xd7 10'+N.sup(k)+sg+mtxt(b2)+' \xd7 10'+N.sup(k))
    m=Q.add(a2,b2)if op==3 else Q.sub(a2,b2)
    o.append('= '+mtxt(m)+' \xd7 10'+N.sup(k))
    r=Q.add(A,B)if op==3 else Q.sub(A,B)
   N.need(r[0]!=0,'O resultado \xe9 0')
   mr,nr=cien(r)
   o.append('> '+ctxt(mr,nr))
  else:
   o[0]='> '+o[0]
  st=('Nota\xe7\xe3o cient\xedfica: a \xd7 10\u207f com 1 \u2264 a < 10 e n inteiro.\nMultiplicar: multiplicam-se os n\xfameros e somam-se os expoentes.\nDividir: dividem-se os n\xfameros e subtraem-se os ex'
'poentes.\nSomar: primeiro, a mesma pot\xeancia de 10.')
  return('\n'.join(o),st,Q.qf(r),'')
 def qn(x):
  return str(x)if x>=0 else '('+str(x)+')'
 def sqf(n):
  k,m=(1,1)
  for p,e in Q.fatores(n):
   k*=p**(e//2)
   m*=p**(e%2)
  return(k,m)
 def rlimpa(A):
  return dict([(m,A[m])for m in A if A[m][0]])
 def radd(A,B,s=1):
  C=dict(A)
  for m in B:
   C[m]=Q.add(C.get(m,Q.Z),B[m])if s>0 else Q.sub(C.get(m,Q.Z),B[m])
  return rlimpa(C)
 def rmul(A,B):
  C={}
  for a in A:
   for b in B:
    k,m=sqf(a*b)
    C[m]=Q.add(C.get(m,Q.Z),Q.mul(Q.mul(A[a],B[b]),(k,1)))
  return rlimpa(C)
 def rsqrt(q,ps):
  N.need(q[0]>=0,'N\xe3o h\xe1 raiz quadrada de um n\xfamero negativo')
  if q[0]==0:
   return{}
  k,m=sqf(q[0]*q[1])
  r={m:Q.R(k,q[1])}
  if k>1 or q[1]>1:
   p=['\u221a'+('('+Q.qs(q)+')'if q[1]>1 else str(q[0]))]
   if q[1]>1:
    p.append('\u221a'+str(q[0]*q[1])+'/'+str(q[1]))
   if k>1:
    p.append('\u221a('+str(k*k)+' \xd7 '+str(m)+')'+('/'+str(q[1])if q[1]>1 else ''))
   if rstr(r)!=p[-1]:
    p.append(rstr(r))
   ps.append(' = '.join(p))
  return r
 def rconj(B):
  ks=list(B.keys())
  if len(ks)==1:
   return{ks[0]:Q.UM}
  N.need(len(ks)==2,'Denominador com mais de dois termos: n\xe3o sei racionalizar')
  return{ks[0]:B[ks[0]],ks[1]:Q.neg(B[ks[1]])}
 def rdiv(A,B,ps):
  N.need(B,'Divis\xe3o por zero')
  if list(B.keys())==[1]:
   return dict([(m,Q.div(A[m],B[1]))for m in A])
  c=rconj(B)
  den=rmul(B,c)
  N.need(list(den.keys())in([1],[]),'N\xe3o sei racionalizar este denominador')
  N.need(den,'Divis\xe3o por zero')
  ps.append('Racionalizar: multiplica-se em cima e em baixo por '+rstr(c)+' (o denominador fica '+Q.vstr(den[1])+')')
  num=rmul(A,c)
  return dict([(m,Q.div(num[m],den[1]))for m in num])
 def reval(t,ps):
  k=t[0]
  if k=='n':
   return{1:t[1]}if t[1][0]else{}
  if k=='r':
   a=reval(t[1],ps)
   N.need(list(a.keys())in([1],[]),'Ra\xedzes de ra\xedzes: n\xe3o sei simplificar')
   return rsqrt(a.get(1,Q.Z),ps)
  if k=='u':
   return dict([(m,Q.neg(c))for m,c in reval(t[1],ps).items()])
  if k in '+-':
   return radd(reval(t[1],ps),reval(t[2],ps),1 if k=='+'else-1)
  if k=='*':
   return rmul(reval(t[1],ps),reval(t[2],ps))
  if k=='/':
   return rdiv(reval(t[1],ps),reval(t[2],ps),ps)
  if k=='^':
   e=reval(t[2],ps)
   N.need(list(e.keys())in([1],[])and e.get(1,Q.Z)[1]==1,'O expoente tem de ser inteiro')
   e=e.get(1,Q.Z)[0]
   b=reval(t[1],ps)
   N.need(abs(e)<=12,'Expoente demasiado grande')
   r={1:Q.UM}
   for i in range(abs(e)):
    r=rmul(r,b)
   return rdiv({1:Q.UM},r,ps)if e<0 else r
  if k=='c':
   N.err('Raiz c\xfabica s\xf3 sozinha (por exemplo \u221b54)')
  N.err('Os radicais n\xe3o podem ter letras')
 def rstr(A):
  if not A:
   return '0'
  o=''
  for m in sorted(A.keys()):
   c=A[m]
   a,d=(abs(c[0]),c[1])
   if m==1:
    t=Q.qs((a,d))
   else:
    t=(''if a==1 else str(a))+'\u221a'+str(m)+('/'+str(d)if d>1 else '')
   if not o:
    o=('-'if c[0]<0 else '')+t
   else:
    o+=(' - 'if c[0]<0 else ' + ')+t
  return o
 def rval(A):
  return sum([Q.qf(A[m])*m**0.5 for m in A])
 def rad():
  return('Ra\xedzes e radicais',[N.fld('Express\xe3o com \u221a (ex.: \u221a50 + 2\u221a8)','','\u221a50 + 2\u221a8 - \u221a18','t')],_rad)
 def _rad(v):
  s=v[0].replace('\u221b',' cbrt ')
  N.need(s.strip(),'Escreve uma express\xe3o, por exemplo \u221a50')
  if 'cbrt'in s:
   N.need(s.strip().startswith('cbrt'),'A raiz c\xfabica tem de estar sozinha (por exemplo \u221b54)')
   return cubica(s.replace('cbrt','').strip())
  t=Q.arvore(s)
  ps=[]
  A=reval(t,ps)
  o=[]
  if ps:
   o+=['Passos:']+['- '+p for p in ps]
  o.append('> '+rstr(A))
  x=rval(A)
  o.append('Valor aproximado: '+N.fmt(x))
  if list(A.keys())not in([1],[]):
   o.append('\xc9 um n\xfamero irracional (tem uma raiz que n\xe3o \xe9 exata).')
  if t[0]=='r'and len(A)==1 and(list(A.keys())!=[1]):
   q=Q.cte(Q.poli(t[1]))
   if q is not None and q[1]==1:
    k=int(q[0]**0.5)
    while k*k>q[0]:
     k-=1
    while(k+1)*(k+1)<=q[0]:
     k+=1
    o.append('Enquadramento: '+str(k)+' < \u221a'+str(q[0])+' < '+str(k+1)+' ('+str(k*k)+' < '+str(q[0])+' < '+str((k+1)**2)+')')
    lo=int(x*10)/10
    o.append('\xc0s d\xe9cimas: '+N.fix(lo,1)+' < \u221a'+str(q[0])+' < '+N.fix(lo+0.1,1)+' (por defeito e por excesso)')
  st=('\u221a(a \xd7 b) = \u221aa \xd7 \u221ab e \u221a(a/b) = \u221aa / \u221ab (a, b \u2265 0).\nSimplificar: tira-se para fora o maior quadrado perfeito: \u221a50 = \u221a(25 \xd7 2) = 5\u221a2.\nS\xf3 se'
' somam radicais iguais: 5\u221a2 + 4\u221a2 = 9\u221a2.\nRacionalizar: multiplicar pelo conjugado, (a + \u221ab)(a - \u221ab) = a\xb2 - b.')
  return('\n'.join(o),st,x,'')
 def cubica(s):
  q=Q.cte(Q.poli(Q.arvore(s)))
  N.need(q is not None,'Escreve um n\xfamero dentro da raiz c\xfabica')
  sg=-1 if q[0]<0 else 1
  o=[]
  res=[]
  for x in(abs(q[0]),q[1]):
   k,m=(1,1)
   for p,e in Q.fatores(x):
    k*=p**(e//3)
    m*=p**(e%3)
   res.append((k,m))
  (kn,mn),(kd,md)=res
  v=sg*abs(Q.qf(q))**(1/3)
  if mn==1 and md==1:
   o.append('> \u221b'+Q.vstr(q)+' = '+Q.qs(Q.R(sg*kn,kd))+' (cubo perfeito)')
  else:
   o.append('> \u221b'+Q.vstr(q)+' = '+('-'if sg<0 else '')+(str(kn)if kn>1 else '')+'\u221b'+str(mn*md*md)+('/'+str(kd*md)if kd*md>1 else ''))
   o.append('Valor aproximado: '+N.fmt(v))
  st='\u221b(a\xb3) = a; a raiz c\xfabica de um n\xfamero negativo \xe9 negativa.'
  return('\n'.join(o),st,v,'')
 def extremo(s):
  s=s.strip().lower().replace('+','')
  if s in('inf','\u221e','infinito'):
   return 'inf'
  if s in('-inf','-\u221e','-infinito'):
   return '-inf'
  return valor(s,'o extremo')
 def intervalo(s):
  s=s.strip().replace(' ','').replace('\u221e','inf')
  N.need(len(s)>=5 and s[0]in '[]'and(s[-1]in '[]'),'Escreve o intervalo assim: [-2, 5[ (ou com ; se usares v\xedrgulas decimais)')
  meio=s[1:-1]
  sep=';'if ';'in meio else ','
  N.need(meio.count(sep)==1,'Um intervalo tem dois extremos')
  a,b=meio.split(sep)
  lo,hi=(extremo(a),extremo(b))
  N.need(lo!='inf'and hi!='-inf','Extremos trocados')
  lc=s[0]=='['and lo!='-inf'
  hc=s[-1]==']'and hi!='inf'
  lo=None if lo=='-inf'else lo
  hi=None if hi=='inf'else hi
  if lo is not None and hi is not None:
   c=Q.cmp(lo,hi)
   N.need(c<0 or(c==0 and lc and hc),'O 1.\xba extremo tem de ser menor do que o 2.\xba')
  return(lo,lc,hi,hc)
 def inteiros(I):
  lo,lc,hi,hc=I
  if lo is None or hi is None:
   return None
  a=-(-lo[0]//lo[1])
  if Q.cmp((a,1),lo)==0 and(not lc):
   a+=1
  b=hi[0]//hi[1]
  if Q.cmp((b,1),hi)==0 and(not hc):
   b-=1
  return list(range(a,b+1))
 def intv():
  return('Intervalos de n\xfameros reais',[N.fld('Intervalo A','','[-2, 5[','t'),N.fld('Intervalo B (opcional)','',']3, +inf[','t')],_intv)
 def _intv(v):
  A=intervalo(v[0])
  o=['A = '+Q.istr(A)+': '+Q.cond(A)]
  its=[A]
  B=None
  if v[1]:
   B=intervalo(v[1])
   its.append(B)
   o.append('B = '+Q.istr(B)+': '+Q.cond(B))
   C=Q.inter(A,B)
   o.append('> A \u2229 B = '+Q.istr(C)+(' ('+Q.cond(C)+')'if C else ''))
   U=Q.uniao(A,B)
   o.append('> A \u222a B = '+' \u222a '.join([Q.istr(x)for x in U]))
   alvo=C
  else:
   alvo=A
  if alvo:
   zs=inteiros(alvo)
   if zs is not None:
    o.append('N\xfameros inteiros em '+('A \u2229 B'if B else 'A')+': '+(', '.join([str(z)for z in zs[:30]])+(' ...'if len(zs)>30 else '')if zs else 'nenhum')+' ('+str(len(zs))+')')
   if alvo[0]is not None and alvo[2]is not None:
    o.append('Amplitude: '+Q.vstr(Q.sub(alvo[2],alvo[0])))
  fin=[x for I in its for x in(I[0],I[2])if x is not None]
  lo=min([Q.qf(x)for x in fin])if fin else 0.0
  hi=max([Q.qf(x)for x in fin])if fin else 1.0
  d=(hi-lo)*0.25+1
  sg=[]
  tx=[]
  for j in range(len(its)):
   I=its[j]
   y=2-j
   a=lo-d if I[0]is None else Q.qf(I[0])
   b=hi+d if I[2]is None else Q.qf(I[2])
   sg.append((a,y,b,y))
   if I[0]is not None:
    tx.append((a,y,'['if I[1]else ']'))
   if I[2]is not None:
    tx.append((b,y,']'if I[3]else '['))
  gr=('Na reta real',[('s',sg,4),('t',tx,5)],lo-d,hi+d,0,3,'em cima: A'+('; em baixo: B'if B else ''))
  st=('[a, b]: a \u2264 x \u2264 b (fechado); ]a, b[: a < x < b (aberto).\nA \u2229 B: os n\xfameros que est\xe3o nos dois (e, \u2227); A \u222a B: os que est\xe3o em pelo menos um (ou, \u2228).\nNo infinito'
' o intervalo \xe9 sempre aberto.')
  return('\n'.join(o),st,None,'',gr)
 return _ns('N Q valor ncie rad extremo intervalo inteiros intv',N,Q,valor,ncie,rad,extremo,intervalo,inteiros,intv)


_F['c_mrea'] = _m_c_mrea


def _m_c_msol():
 import math
 N=_imp('m1_nucleo')
 X=N.X
 sq=math.sqrt
 PI=math.pi
 UN=['u.c.','cm','m','mm','dm','km']
 def nv(x):
  s,ex=N.fmt2(x,0,-1)
  if ex:
   return s
  e=N.exact(x)
  return e if e is not None else s
 def eq(a,b):
  return abs(a-b)<1e-09*max(1.0,abs(a),abs(b))
 def ue(u,k):
  if u=='u.c.':
   return('u.c.','u.a.','u.v.')[k-1]
  return u+('','\xb2','\xb3')[k-1]
 def lermed(v,nms,conh,livre=-1):
  k=len(nms)
  for i in range(k,len(v)):
   N.need(v[i]is None,'Este s\xf3lido s\xf3 usa '+str(k)+' medida'+('s ('+', '.join(nms)+')'if k>1 else ' ('+nms[0]+')'))
  m=[None if x is None else N.pos(x[0],nms[i]+' ('+str(i+1)+'.\xaa medida)')for i,x in enumerate(v[:k])]
  f=[i for i in range(k)if m[i]is None]
  dados=[c for c in conh if c is not None]
  if not f:
   N.need(not dados,'J\xe1 deste todas as medidas: deixa vazia a \xe1rea, o per\xedmetro ou o volume conhecido')
   return(m,-1)
  N.need(len(f)==1,'Falta mais do que uma medida ('+', '.join([nms[i]for i in f])+')')
  if f[0]==livre and(not dados):
   return(m,f[0])
  N.need(len(dados)==1,'Para calcular '+nms[f[0]]+', escreve '+'um valor conhecido (\xe1rea, per\xedmetro ou volume)')
  return(m,f[0])
 def subst(tp,m,nms):
  return tp.format(*[nms[i]if m[i]is None else nv(m[i])for i in range(len(nms))])
 def resolve(m,i,nms,val,nm,tp,inv,o):
  N.need(i in inv,'Com '+nm+' n\xe3o sei calcular '+nms[i]+'; escreve outra medida')
  o+=[nv(val)+' = '+subst(tp,m,nms),'\u21d4 '+nms[i]+' = '+inv[i][0]]
  try:
   r=inv[i][1](m,val)
  except(ValueError,ZeroDivisionError):
   r=-1
  N.need(r>1e-12,'Os dados n\xe3o s\xe3o compat\xedveis: '+nms[i]+' daria um valor n\xe3o positivo')
  m[i]=r
 SOL=['Cubo (aresta a)','Paralelep\xedpedo (c, l, h)','Prisma reto (Ab, Pb, h)','Cilindro (r, h)','Pir\xe2mide (Ab, h)','Pir\xe2mide regular (n, l, h)','Cone (r, h)','Esfera (raio r)']
 FS=(('a',('V = a\xb3','{0}\xb3',lambda m:m[0]**3),('At = 6 '+X+' a\xb2','6 '+X+' {0}\xb2',lambda m:6*m[0]**2),{0:('\u221bV',lambda m,V:V**(1/3))},{0:('\u221a(At / 6)',lambda m,A:sq(A/6))}),('c l h',('V = c '+X+' l '+X+' h',
'{0} '+X+' {1} '+X+' {2}',lambda m:m[0]*m[1]*m[2]),('At = 2 '+X+' (cl + ch + lh)','2 '+X+' ({0} '+X+' {1} + {0} '+X+' {2} + {1} '+X+' {2})',lambda m:2*(m[0]*m[1]+m[0]*m[2]+m[1]*m[2])),{0:('V / (l '+X+' h)',
lambda m,V:V/m[1]/m[2]),1:('V / (c '+X+' h)',lambda m,V:V/m[0]/m[2]),2:('V / (c '+X+' l)',lambda m,V:V/m[0]/m[1])},{2:('(At/2 - cl) / (c + l)',lambda m,A:(A/2-m[0]*m[1])/(m[0]+m[1]))}),('Ab Pb h',('V = Ab '+X+' h',
'{0} '+X+' {2}',lambda m:m[0]*m[2]),('At = Pb '+X+' h + 2 '+X+' Ab','{1} '+X+' {2} + 2 '+X+' {0}',lambda m:m[1]*m[2]+2*m[0]),{0:('V / h',lambda m,V:V/m[2]),2:('V / Ab',lambda m,V:V/m[0])},{2:('(At - 2Ab) / Pb',
lambda m,A:(A-2*m[0])/m[1])}),('r h',('V = \u03c0 '+X+' r\xb2 '+X+' h','\u03c0 '+X+' {0}\xb2 '+X+' {1}',lambda m:PI*m[0]**2*m[1]),('At = 2\u03c0r\xb2 + 2\u03c0rh','2\u03c0 '+X+' {0}\xb2 + 2\u03c0 '+X+' {0} '+X+' {1}',
lambda m:2*PI*m[0]*(m[0]+m[1])),{0:('\u221a(V / (\u03c0h))',lambda m,V:sq(V/PI/m[1])),1:('V / (\u03c0r\xb2)',lambda m,V:V/PI/m[0]**2)},{1:('(At - 2\u03c0r\xb2) / (2\u03c0r)',lambda m,A:(A-2*PI*m[0]**2)/(2*PI*m[0]))}),
('Ab h',('V = Ab '+X+' h / 3','{0} '+X+' {1} / 3',lambda m:m[0]*m[1]/3),None,{0:('3V / h',lambda m,V:3*V/m[1]),1:('3V / Ab',lambda m,V:3*V/m[0])},{}),('n l h',None,None,{},{}),('r h',('V = \u03c0 '+X+' r\xb2 '+X+' h / 3',
'\u03c0 '+X+' {0}\xb2 '+X+' {1} / 3',lambda m:PI*m[0]**2*m[1]/3),('At = \u03c0r\xb2 + \u03c0rg',None,lambda m:PI*m[0]*(m[0]+sq(m[0]**2+m[1]**2))),{0:('\u221a(3V / (\u03c0h))',lambda m,V:sq(3*V/PI/m[1])),
1:('3V / (\u03c0r\xb2)',lambda m,V:3*V/PI/m[0]**2)},{}),('r',('V = 4/3 '+X+' \u03c0 '+X+' r\xb3','4/3 '+X+' \u03c0 '+X+' {0}\xb3',lambda m:4*PI*m[0]**3/3),('A = 4\u03c0r\xb2','4\u03c0 '+X+' {0}\xb2',lambda m:4*PI*m[0]**2),
{0:('\u221b(3V / (4\u03c0))',lambda m,V:(3*V/4/PI)**(1/3))},{0:('\u221a(A / (4\u03c0))',lambda m,A:sq(A/4/PI))}))
 def sol():
  return('S\xf3lidos: \xe1reas e volumes',[N.fld('S\xf3lido','','','c',SOL),N.fld('1.\xaa medida','','3','o'),N.fld('2.\xaa medida','','','o'),N.fld('3.\xaa medida','','','o'),N.fld('Volume conhecido (opcional)',
'','','o'),N.fld('\xc1rea total conhecida (opcional)','','','o'),N.fld('Unidade de comprimento','','','c',UN)],_sol)
 def _sol(v):
  k=v[0]
  u=UN[v[6]]
  nms=FS[k][0].split()
  fv,fa,iv,ia=FS[k][1:]
  Vk=None if v[4]is None else N.pos(v[4][0],'O volume')
  Ak=None if v[5]is None else N.pos(v[5][0],'A \xe1rea')
  m,i=lermed(v[1:4],nms,(Vk,Ak))
  if k==5:
   N.need(i<0,'Na pir\xe2mide regular escreve as tr\xeas medidas (n, l, h)')
   return piramide(m,u)
  o=[]
  if i>=0:
   if Vk is not None:
    o.append('= '+fv[0])
    resolve(m,i,nms,Vk,'o volume',fv[1],iv,o)
   else:
    N.need(ia,'Com a \xe1rea total n\xe3o sei calcular esta medida; usa o volume')
    o.append('= '+fa[0])
    resolve(m,i,nms,Ak,'a \xe1rea',fa[1]or fa[0],ia,o)
   o.append('> '+nms[i]+' '+N.rhs(m[i],2)+' '+ue(u,2 if nms[i]=='Ab'else 1))
  o.append(SOL[k].split(' (')[0]+': '+', '.join([nms[j]+' = '+nv(m[j])for j in range(len(nms))]))
  V=fv[2](m)
  if i<0 or Vk is None:
   o+=['= '+fv[0],'V = '+subst(fv[1],m,nms),'> V '+N.rhs(V,2)+' '+ue(u,3)]
  if k==6:
   g=sq(m[0]**2+m[1]**2)
   o+=['Geratriz (Pit\xe1goras): g = \u221a(r\xb2 + h\xb2) '+N.rhs(g,2),'Al = \u03c0rg '+N.rhs(PI*m[0]*g,2)+' '+ue(u,2)]
  elif k==3:
   o.append('Al = 2\u03c0rh '+N.rhs(2*PI*m[0]*m[1],2)+' '+ue(u,2))
  elif k==2:
   o.append('Al = Pb '+X+' h '+N.rhs(m[1]*m[2],2)+' '+ue(u,2))
  elif k==0:
   o.append('Diagonal espacial: a\u221a3 '+N.rhs(m[0]*sq(3),2))
  elif k==1:
   o.append('Diagonal espacial: \u221a(c\xb2 + l\xb2 + h\xb2) '+N.rhs(sq(m[0]**2+m[1]**2+m[2]**2),2))
  if fa is None:
   o.append('\xc1rea: \xe9 preciso o ap\xf3tema (usa a pir\xe2mide regular).')
  elif i<0 or Ak is None:
   A=fa[2](m)
   t=fa[0].split(' =')[0]
   o+=['= '+fa[0]]+([t+' = '+subst(fa[1],m,nms)]if fa[1]else[])+['> '+t+' '+N.rhs(A,2)+' '+ue(u,2)]
  litros(V,u,o)
  return('\n'.join(o),ST_SOL,V,ue(u,3))
 ST_SOL='Prisma e cilindro: V = \xe1rea da base '+X+' altura.\nPir\xe2mide e cone: V = \xe1rea da base '+X+' altura / 3.\nEsfera: V = 4/3 \u03c0r\xb3; \xe1rea 4\u03c0r\xb2.'
 def litros(V,u,o):
  f={'mm':1e-06,'cm':0.001,'dm':1.0,'m':1000.0,'km':1000000000000.0}.get(u)
  if f:
   o.append('Capacidade: 1 dm\xb3 = 1 L, logo '+N.fmt(V)+' '+ue(u,3)+' = '+N.fmt(V*f)+' L')
 def piramide(m,u):
  n,l,h=m
  N.need(eq(n,round(n))and n>=3,'O n\xfamero de lados da base n tem de ser um inteiro maior ou igual a 3')
  n=int(round(n))
  a=l/2/math.tan(PI/n)
  Ab=n*l*a/2
  ap=sq(h*h+a*a)
  Al=n*l*ap/2
  V=Ab*h/3
  o=['Pir\xe2mide regular: base com '+str(n)+' lados de '+nv(l)+'; altura '+nv(h)+'.','Ap\xf3tema da base: a = l / (2 tan(180\xb0/n)) '+N.rhs(a,2)+(' (metade do lado)'if n==4 else ''),'Ab = n '+X+' l '+X+' a / 2 '+N.rhs(Ab,
2)+' '+ue(u,2),'= V = Ab '+X+' h / 3','> V '+N.rhs(V,2)+' '+ue(u,3),'Ap\xf3tema da pir\xe2mide (Pit\xe1goras): \u221a(h\xb2 + a\xb2) '+N.rhs(ap,2),'Al = n '+X+' l '+X+' ap / 2 '+N.rhs(Al,2)+' '+ue(u,2),
'> At = Ab + Al '+N.rhs(Ab+Al,2)+' '+ue(u,2)]
  if n not in(3,4,6):
   o.append('(O ap\xf3tema da base usa trigonometria: 9.\xba ano.)')
  litros(V,u,o)
  return('\n'.join(o),ST_SOL,V,ue(u,3))
 return _ns('N X eq resolve sol',N,X,eq,resolve,sol)


_F['c_msol'] = _m_c_msol


def _m_m1():
 MODO='edi\xe7\xe3o de reserva Mat'
 def _nome(e):
  s=str(e)
  i=s.find("'")
  j=s.find("'",i+1)
  if 0<=i<j:
   return s[i+1:j]
  return s
 def main():
  f0=-1
  try:
   import gc
   gc.collect()
   f0=gc.mem_free()
  except Exception:
   pass
  try:
   m1_app=_imp('m1_app')
  except MemoryError:
   print('M1TR4M: mem\xf3ria insuficiente para arrancar.')
   print('Fecha outros documentos e tenta de novo.')
   return
  except ImportError as e:
   n=_nome(e)
   print('M1TR4M: falta o m\xf3dulo '+n+' (instala '+n+'.tns).')
   return
  try:
   m1_app.S['imp']=MODO
   m1_app.run(f0)
  except KeyboardInterrupt:
   pass
  except MemoryError:
   print('M1TR4M: mem\xf3ria insuficiente. Volta a abrir a app.')
  except Exception as e:
   print('M1TR4M: erro fatal '+type(e).__name__+': '+str(e))
 main()
 return _ns('')


_F['m1'] = _m_m1


def _m_m1_app():
 P=_imp('m1_plat')
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 C=_imp('m1_cont')
 K=_imp('m1_cat')
 APPV='1.0'
 S={'cfg':None,'ex':None,'lic':None,'tst':None,'rev':None,'pos':None,'h':[],'vals':{},'f0':-1,'where':'arranque','gv':True,'aviso':0,'imp':'','mods':''}
 DEF=[1,4,1,6,0,1,0,2,7,17,13]
 GV=(9.8,10.0,9.80665)
 GT=('9,8 m s\u207b\xb2 (manual)','10 m s\u207b\xb2 (exame)','9,80665 m s\u207b\xb2 (padr\xe3o)')
 TOL=(0.001,0.01,0.0001)
 TT=('0,1 %','1 %','0,01 %')
 NIV=('','B\xe1sico','Interm\xe9dio','Avan\xe7ado')
 GR=(('F','q','Qu\xedmica'),('F','f','F\xedsica'),('F','a','Atividades laboratoriais'),('F','r','Revis\xf5es do 7.\xba ao 9.\xba ano'),('M','7','7.\xba ano'),('M','8','8.\xba ano'),('M','9','9.\xba ano'),
('M','t','10.\xba ano'))
 DN={'F':'F\xedsica e Qu\xedmica A','M':'Matem\xe1tica','C':'Comuns'}
 def apply_cfg():
  c=S['cfg']
  N.CF['dec']=c[1]
  N.CF['sci']=c[3]
  N.CF['ang']=c[4]
  N.CF['sfa']=c[2]
  N.CF['g']=GV[c[5]]
  P.E['sym']=c[7]
  P.metrics(c[8],c[9],c[10])
 def save(nm):
  key={'m1def':'cfg','m1prog':'ex','m1lic':'lic','m1tst':'tst','m1rev':'rev','m1pos':'pos'}[nm]
  if not P.save(nm,S[key])and(not S['aviso']):
   S['aviso']=1
   U.msg('Gravar','N\xe3o foi poss\xedvel guardar dados neste aparelho. A app funciona, mas o progresso n\xe3o fica guardado.',5)
 def wipe():
  if U.ask('Apagar o progresso','Apagar li\xe7\xf5es vistas, exerc\xedcios, testes e cart\xf5es? N\xe3o d\xe1 para desfazer.'):
   for k in('ex','lic','tst','rev','pos'):
    v=S[k]
    for j in range(1,len(v)):
     v[j]=0
   for nm in('m1prog','m1lic','m1tst','m1rev','m1pos'):
    save(nm)
   U.msg('Progresso','Progresso apagado. Grava o documento (ctrl+S).')
 def g():
  return GV[S['cfg'][5]]
 def sfa():
  return S['cfg'][2]
 def th(i):
  return K.TEMAS[i].split('|')
 def tfind(tid):
  for i in range(len(K.TEMAS)):
   if K.TEMAS[i].startswith(tid+'|'):
    return i
  return-1
 def calcs():
  return[ln.split('|')for ln in C.get('k','m1_calc').CALC.split('\n')if ln]
 def grupos(d):
  out=[]
  for x in GR:
   ts=[i for i in range(len(K.TEMAS))if th(i)[1]==d and th(i)[2]==x[1]]
   if x[0]==d and ts:
    out.append((x[1],x[2],ts))
  return out
 def cname(cid):
  for c in calcs():
   if c[0]==cid:
    return c[1]
  return cid
 def main_menu():
  it=('F\xedsica e Qu\xedmica A','Matem\xe1tica','Pesquisa global','Calculadoras','Tabela peri\xf3dica','Formul\xe1rio','Constantes e unidades','Exemplos resolvidos','Exerc\xedcios e testes','O meu progresso',
'Revis\xe3o r\xe1pida','Defini\xe7\xf5es, ajuda e Diagn\xf3stico','Sair')
  sel=0
  while True:
   S['where']='menu principal'
   r=U.menu('M1TR4M \xb7 FQ 10.\xba \xb7 Mat 7.\xba-10.\xba',it,sel)
   if r<0 or r==12:
    if U.ask('Sair','Sair da M1TR4M?',1):
     return
    continue
   sel=r
   if r==0:
    disc('F')
   elif r==1:
    disc('M')
   elif r==2:
    search()
   elif r==3:
    nav('calc_menu','')
   elif r==4:
    C.get('p','m1_tp').run()
   elif r in(5,7,8,10):
    i=nav('pick')
    if i>=0:
     if r==5:
      nav('formulas',i)
     elif r==7:
      nav('examples',i)
     elif r==8:
      nav('ex_menu',i)
     else:
      tool('m1_ex','review',i)
   elif r==6:
    nav('consts')
   elif r==9:
    tool('m1_ex','progress')
   elif r==11:
    tool('m1_cfg')
 def nav(fn,*a):
  return getattr(C.get('f','m1_nav'),fn)(*a)
 def tool(nm,fn='run',a=None):
  m=C.get('f',nm)
  f=getattr(m,fn)
  if a is None:
   f()
  else:
   f(a)
 def search():
  while True:
   t=C.get('f','m1_pesq').run()
   C.drop('f')
   C.drop('p')
   if not t:
    return
   go(t)
 def go(t):
  k=t[0]
  v=t[2:]
  if k=='L':
   goto_lesson(v)
  elif k=='C':
   calc(v)
  elif k=='T':
   C.get('p','m1_tp').sheet(int(v))
  elif k=='K':
   calc('c_comd.cte')
  else:
   tid,n=v.split(':')
   i=tfind(tid)
   if k=='F':
    nav('fshow',i,int(n))
   elif k=='E':
    nav('eshow',i,int(n))
   else:
    tool('m1_ex','one',(i,int(n)))
 def disc(d):
  gs=grupos(d)
  if not gs:
   U.msg(DN[d],'Esta edi\xe7\xe3o n\xe3o tem temas de '+DN[d]+'.')
   return
  sel=0
  while True:
   S['where']=DN[d]
   r=U.menu(DN[d],[x[1]for x in gs],sel)
   if r<0:
    return
   sel=r
   ts=gs[r][2]
   s2=0
   while True:
    q=U.menu(gs[r][1],[th(i)[3]for i in ts],s2)
    if q<0:
     break
    s2=q
    theme(ts[q])
 def theme(i):
  t=th(i)
  S['where']=t[3]
  D=C.get('p',t[4]).D
  acts=[('Li\xe7\xf5es',0)]
  if '\n@F 'in D:
   acts.append(('Formul\xe1rio do tema',1))
  if '\n@E 'in D:
   acts.append(('Exemplos',2))
  if t[5]:
   acts.append(('Exerc\xedcios',3))
   acts.append(('Teste do cap\xedtulo',4))
  if t[12]:
   acts.append(('Calculadoras do tema',5))
  if '\n@I'in D:
   acts.append(('Resumo',6))
  D=None
  sel=0
  while True:
   r=U.menu(t[3],[a[0]for a in acts],sel)
   if r<0:
    return
   sel=r
   a=acts[r][1]
   if a==0:
    lessons(i)
   elif a==1:
    nav('formulas',i)
   elif a==2:
    nav('examples',i)
   elif a==3:
    tool('m1_ex','train',i)
   elif a==4:
    tool('m1_ex','test',i)
   elif a==5:
    nav('calc_list',t[12].split(' '),t[3])
   else:
    nav('summary',i)
 def lessons(i):
  t=th(i)
  sel=0
  while True:
   D=C.get('p',t[4]).D
   hs=[h[0]for h in C.recs(D,'L')]
   D=None
   o=int(t[7])
   it=[]
   for k in range(len(hs)):
    v=S['lic'][o+k+1]if o+k+1<len(S['lic'])else 0
    it.append(('\u2713 'if v else '\xb7 ')+hs[k][1])
   r=U.menu(t[3],it,sel,'enter: abrir \xb7 \u2713 j\xe1 vista \xb7 esc')
   if r<0:
    return
   sel=r
   open_lesson(i,r)
 def open_lesson(i,k,pg=-1):
  t=th(i)
  gi=int(t[7])+k+1
  D=C.get('p',t[4]).D
  hs=C.recs(D,'L')
  if k>=len(hs):
   return
  h,pages,ans,fs=C.lesson(D,hs[k][0][0])
  D=None
  S['where']='li\xe7\xe3o '+h[0]
  pages[0]=pages[0]+linfo(h)
  if pg<0:
   pg=max(0,S['lic'][gi]-1)if gi<len(S['lic'])else 0
  top=0
  while True:
   k2,pg,top=U.lesson(h[1],pages,pg,top,ans,h[0],('c','l')if len(h)>3 and h[3]or(len(h)>7 and(h[6]or h[7]))else())
   if gi<len(S['lic']):
    S['lic'][gi]=pg+1
   S['pos']=[1,1,i,k,pg]
   if k2=='c'and len(h)>3 and h[3]:
    calc(h[3].split(' ')[0])
   elif k2=='l':
    links(h)
   else:
    break
  save('m1lic')
  save('m1pos')
 def linfo(h):
  o=['']
  if len(h)>5 and h[5]:
   o.append('N\xedvel: '+h[5]+(' \xb7 '+h[4]+'.\xba ano'if len(h)>4 and h[4]else ''))
  if len(h)>3 and h[3]:
   o.append('Calculadora: '+cname(h[3].split(' ')[0])+' (tecla c)')
  for j,nm in((6,'Pr\xe9-requisitos'),(7,'Liga\xe7\xe3o')):
   if len(h)>j and h[j]:
    o.append(nm+': '+', '.join([x.split(':')[1]for x in h[j].split(';')if ':'in x])+' (tecla l)')
  if len(h)>8 and h[8]:
   o.append('Fonte: '+h[8])
  return '\n'.join(o)
 def links(h):
  ls=[]
  for j in(6,7):
   if len(h)>j and h[j]:
    ls=ls+[x.split(':')for x in h[j].split(';')if ':'in x]
  if not ls:
   return
  r=U.menu('Li\xe7\xf5es ligadas',[x[1]for x in ls])
  if r>=0:
   goto_lesson(ls[r][0])
 def goto_lesson(lid):
  for i in range(len(K.TEMAS)):
   t=th(i)
   if lid in t[13].split(' '):
    open_lesson(i,t[13].split(' ').index(lid))
    return
  U.msg('Li\xe7\xe3o','Li\xe7\xe3o '+lid+' n\xe3o encontrada.',5)
 def calc(cid):
  mn,fn=cid.split('.')
  sp=getattr(C.get('c',mn),fn)()
  if sp is None:
   return
  t,fs,f=sp
  dflt=[x[2]for x in fs]
  old=S['vals'].get(cid)
  if old and len(old)==len(fs):
   for j in range(len(fs)):
    fs[j][2]=old[j][0]
    fs[j][3]=old[j][1]
  foc=0
  while True:
   S['where']='calculadora '+t
   if fs and(not U.form(t,fs,foc)):
    return
   foc=len(fs)-1
   v=N.rdf(fs)
   if fs:
    S['vals'][cid]=[(x[2],x[3])for x in fs]
   if v is None:
    for j in range(len(fs)):
     if fs[j][5]:
      foc=j
      break
    continue
   try:
    r=f(v)
   except ValueError as e:
    r=(ERR_+str(e),'',None)
   except ZeroDivisionError:
    r=(ERR_+'Divis\xe3o por zero: verifica os dados.','',None)
   except OverflowError:
    r=(ERR_+'Valor demasiado grande.','',None)
   except IndexError:
    r=(ERR_+'Faltam dados: verifica as listas.','',None)
   if r is None:
    return
   if r[0].startswith(ERR_):
    U.msg(t,'! '+r[0])
    if not fs:
     return
    continue
   if len(r)>2 and r[2]is not None:
    S['h'].insert(0,(t,r[2],r[3]if len(r)>3 else ''))
    del S['h'][5:]
    N.CF['ans']=r[2]
   k=res_menu(t,r)
   if k=='3':
    for j in range(len(fs)):
     fs[j][2]=dflt[j]
    foc=0
   elif k=='4':
    nav('calc_menu','')
    return
   elif k=='esc'or not fs:
    return
 def res_menu(t,r):
  gr=len(r)>4 and r[4]
  o='\n\nOp\xe7\xf5es: 1 passos \xb7 2 alterar \xb7 3 novo \xb7 4 usar'
  if gr:
   o=o+' \xb7 5 gr\xe1fico'
  while True:
   k=U.text(t,r[0]+o,'1-'+('5'if gr else '4')+': op\xe7\xf5es','',('1','2','3','4','5'))
   if k=='1':
    U.text(t+' \xb7 passos',r[1]if len(r)>1 and r[1]else 'Esta calculadora n\xe3o tem mais passos.')
   elif k=='5'and gr:
    U.graph(*r[4])
   elif k in('2','3','4','esc','enter'):
    return k
 ERR_='\u2717 '
 def run(f0=-1):
  S['f0']=f0
  P.init()
  C.get('f','m1_ini').start()
  C.drop('f')
  while True:
   try:
    main_menu()
    break
   except KeyboardInterrupt:
    break
   except MemoryError:
    for sl in list(C.SL):
     C.drop(sl)
    P.collect()
    U.msg('Mem\xf3ria','Faltou mem\xf3ria em: '+S['where']+'. Os pacotes foram libertados; voltas ao menu.',5)
   except C.Falta as e:
    U.msg('Falta um m\xf3dulo',str(e),5)
   except Exception as e:
    U.msg('Erro inesperado',type(e).__name__+': '+str(e)+'\nEcr\xe3: '+S['where']+'\nVoltas ao menu.',5)
  for sl in('p','c','f'):
   C.drop(sl)
  if P.E['g']:
   P.begin()
   U.title('M1TR4M')
   P.put(0,2,'At\xe9 \xe0 pr\xf3xima!')
   P.put(0,4,'Grava o documento (ctrl+S) para')
   P.put(0,5,'guardar o progresso e as defini\xe7\xf5es.')
   P.show()
 return _ns('P N U C K APPV S DEF GT TOL TT NIV DN apply_cfg save wipe g sfa th calcs grupos cname nav tool open_lesson goto_lesson calc run',P,N,U,C,K,APPV,S,DEF,GT,TOL,TT,NIV,DN,apply_cfg,save,wipe,
g,sfa,th,calcs,grupos,cname,nav,tool,open_lesson,goto_lesson,calc,run)


_F['m1_app'] = _m_m1_app


def _m_m1_calc():
 CALC=('c_mate.uni|Estat\xedstica de uma vari\xe1vel|M|d7\nc_mate.cls|Dados em classes e histograma|M|d8\nc_mate.caule|Caule-e-folhas|M|d7\nc_matf.fx|Fun\xe7\xe3o escrita por ti (tabela, zeros, gr\xe1fico)|M|'
'a9\nc_matf.afim|Fun\xe7\xe3o afim|M|a8\nc_matq.q2|Equa\xe7\xe3o do 2.\xba grau e fun\xe7\xe3o quadr\xe1tica|M|a9\nc_matr.tri|Tri\xe2ngulo ret\xe2ngulo: seno, cosseno e tangente|M|g9\nc_matr.rad|Graus,'
' radianos e valores exatos|M|g9\nc_matt.pit|Teorema de Pit\xe1goras e rec\xedproco|M|g8\nc_matt.sem|Semelhan\xe7a de figuras|M|g7\nc_mexp.eq1|Equa\xe7\xe3o do 1.\xba grau (passo a passo)|M|a7\nc_mexp.'
'ineq|Inequa\xe7\xe3o do 1.\xba grau|M|a9\nc_mexp.sis|Sistema de duas equa\xe7\xf5es (substitui\xe7\xe3o)|M|a8\nc_mgeo.ang|\xc2ngulos, tri\xe2ngulos e pol\xedgonos|M|g7\nc_mgeo.area|\xc1reas e per\xedm'
'etros de figuras planas|M|g7\nc_mgtr.iso|Isometrias: transla\xe7\xe3o, reflex\xe3o e rota\xe7\xe3o|M|g8\nc_mgtr.circ|\xc2ngulos na circunfer\xeancia|M|g9\nc_mnum.frac|Fra\xe7\xf5es e n\xfameros racion'
'ais (passo a passo)|M|n7\nc_mnum.pot|Pot\xeancias e regras das pot\xeancias|M|n7\nc_mnum.mdc|Fatores primos, m.d.c. e m.m.c.|M|n7\nc_mnum.dec|D\xedzimas e fra\xe7\xf5es|M|n8\nc_mpol.pol|Polin\xf3mios:'
' desenvolver e simplificar|M|a8\nc_mpol.fat|Fatorizar e resolver por fatoriza\xe7\xe3o|M|a8\nc_mprb.freq|Tabela de frequ\xeancias e gr\xe1fico de barras|M|d7\nc_mprb.prob|Probabilidade: lei de Laplace'
'|M|d9\nc_mprb.dados|Dois dados ou moedas (dupla entrada)|M|d9\nc_mprb.urna|Duas extra\xe7\xf5es com e sem reposi\xe7\xe3o (\xe1rvore)|M|d9\nc_mprp.seq|Sequ\xeancias: termo geral|M|a7\nc_mprp.prop|Prop'
'orcionalidade direta|M|a7\nc_mprp.inv|Proporcionalidade inversa|M|a9\nc_mprp.perc|Percentagens|M|a7\nc_mrea.ncie|Nota\xe7\xe3o cient\xedfica|M|n8\nc_mrea.rad|Ra\xedzes e radicais|M|n9\nc_mrea.intv|Int'
'ervalos de n\xfameros reais|M|n9\nc_msol.sol|S\xf3lidos: \xe1reas e volumes|M|g9')
 return _ns('CALC',CALC)


_F['m1_calc'] = _m_m1_calc


def _m_m1_cat():
 NLIC=48
 NEX=102
 NCART=117
 TEMAS=('n7|M|7|N\xfameros (7.\xba ano)|p_n7|x_n7|5|0|9|0|14|0|c_mnum.frac c_mnum.pot c_mnum.mdc c_mrea.rad|n7a n7b n7c n7d n7e','a7|M|7|\xc1lgebra (7.\xba ano)|p_a7|x_a7|5|5|9|9|11|14|c_mprp.seq c_mpol.pol c_mexp.eq1 c_mprp.prop c_mprp.perc|a7a a7b a7c a7d a7e',
'g7|M|7|Geometria e Medida (7.\xba ano)|p_g7|x_g7|5|10|9|18|14|25|c_mgeo.ang c_mgeo.area c_matt.sem|g7a g7b g7c g7d g7e','d7|M|7|Dados (7.\xba ano)|p_d7|x_d7|3|15|8|27|8|39|c_mprb.freq c_mate.uni c_mate.caule|d7a d7b d7c',
'n8|M|8|N\xfameros (8.\xba ano)|p_n8|x_n8|3|18|8|35|8|47|c_mnum.pot c_mrea.ncie c_mnum.dec|n8a n8b n8c','a8|M|8|\xc1lgebra (8.\xba ano)|p_a8|x_a8|5|21|9|43|12|55|c_mpol.pol c_mpol.fat c_mexp.eq1 c_mexp.sis c_matf.afim|a8a a8b a8c a8d a8e',
'g8|M|8|Geometria e Medida (8.\xba ano)|p_g8|x_g8|4|26|8|52|10|67|c_matt.pit c_mgtr.iso|g8a g8b g8c g8d','d8|M|8|Dados (8.\xba ano)|p_d8|x_d8|2|30|8|60|4|77|c_mate.uni c_mate.cls c_mprb.freq|d8a d8b','n9|M|9|N\xfameros (9.\xba ano)|p_n9|x_n9|3|32|8|68|6|81|c_mrea.rad c_mrea.intv c_mrea.ncie|n9a n9b n9c',
'a9|M|9|\xc1lgebra (9.\xba ano)|p_a9|x_a9|4|35|8|76|8|87|c_mexp.ineq c_matq.q2 c_mpol.fat c_mprp.inv c_matf.fx|a9a a9b a9c a9d','g9|M|9|Geometria e Medida (9.\xba ano)|p_g9|x_g9|6|39|10|84|15|95|c_mgtr.circ c_matr.tri c_matr.rad c_msol.sol|g9a g9b g9c g9d g9e g9f',
'd9|M|9|Probabilidades (9.\xba ano)|p_d9|x_d9|3|45|8|94|7|110|c_mprb.prob c_mprb.dados c_mprb.urna|d9a d9b d9c')
 BUILD='2026-10-23'
 LIMITES=('- Tempos e mem\xf3ria medidos s\xf3 no computador (MicroPython 1.12 de 32 bits). No aparelho, v\xea o Diagn\xf3stico.\n- S\xf3 n\xfameros reais: n\xe3o h\xe1 n\xfameros complexos.\n- Edi\xe7\xf5es de '
'reserva: s\xf3 FQ do 10.\xba ano ou Matem\xe1tica do 7.\xba ao 9.\xba ano, sem pesquisa.')
 return _ns('NLIC NEX NCART TEMAS BUILD LIMITES',NLIC,NEX,NCART,TEMAS,BUILD,LIMITES)


_F['m1_cat'] = _m_m1_cat


def _m_m1_cfg():
 P=_imp('m1_plat')
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 C=_imp('m1_cont')
 A=_imp('m1_app')
 def run():
  while True:
   A.S['where']='defini\xe7\xf5es'
   r=U.menu('Defini\xe7\xf5es, ajuda e Diagn\xf3stico',['Defini\xe7\xf5es','Ajuda','Sobre a M1TR4M','Diagn\xf3stico'])
   if r<0:
    return
   (settings,help_,about,diag)[r]()
 def settings():
  sel=0
  while True:
   c=A.S['cfg']
   it=['Casas decimais em Matem\xe1tica: '+str(c[1]),'Alg. significativos autom\xe1ticos em FQ: '+('sim'if c[2]else 'n\xe3o'),'Nota\xe7\xe3o cient\xedfica a partir de 10'+N.sup(c[3]),'Unidade angular: '+('graus'if c[4]==0 else 'radianos'),
'Valor de g: '+A.GT[c[5]],'Toler\xe2ncia dos exerc\xedcios: '+A.TT[c[6]],'Acentos e s\xedmbolos: '+('completos','s\xf3 Latin-1','letras simples')[2-c[7]],'Calibra\xe7\xe3o do texto no ecr\xe3','Apagar o progresso',
'Repor as predefini\xe7\xf5es']
   r=U.menu('Defini\xe7\xf5es',it,sel)
   if r<0:
    A.save('m1def')
    return
   sel=r
   if r==0:
    k=U.menu('Casas decimais',[str(i)for i in range(11)],c[1])
    if k>=0:
     c[1]=k
   elif r==1:
    c[2]=1-c[2]
   elif r==2:
    ops=(3,4,5,6,9)
    k=U.menu('Nota\xe7\xe3o cient\xedfica',['|x| \u2265 10'+N.sup(v)for v in ops])
    if k>=0:
     c[3]=ops[k]
   elif r==3:
    c[4]=1-c[4]
   elif r==4:
    k=U.menu('Valor de g',list(A.GT),c[5])
    if k>=0:
     c[5]=k
   elif r==5:
    k=U.menu('Toler\xe2ncia',list(A.TT),c[6])
    if k>=0:
     c[6]=k
   elif r==6:
    k=U.menu('Acentos e s\xedmbolos',['Completos (\u221a \u03c0 \u2248 \xb2)','S\xf3 Latin-1 (\xe1 \xe7 \xb2)','Letras simples (a c ^2)'],2-c[7])
    if k>=0:
     c[7]=2-k
   elif r==7:
    calib()
   elif r==8:
    A.wipe()
    continue
   elif U.ask('Predefini\xe7\xf5es','Repor todas as defini\xe7\xf5es?'):
    A.S['cfg']=list(A.DEF)
   A.apply_cfg()
   A.save('m1def')
 def calib():
  c=A.S['cfg']
  cw,lh,dy=(c[8],c[9],c[10])
  while True:
   P.metrics(cw,lh,dy)
   P.begin()
   U.title('Calibra\xe7\xe3o do texto')
   y=2*lh
   for i in range(0,P.E['W'],10):
    P.line(i,y,i,y+(6 if i%50==0 else 3),5)
   P.line(0,y,P.E['W'],y,5)
   n=P.E['cols']
   P.put(0,3,'M'*n,0)
   P.put(0,4,('0123456789'*(n//10+1))[:n],0)
   for r in range(3,6):
    P.line(0,r*lh,P.E['W'],r*lh,9)
   P.put(0,6,'cw='+str(cw)+' lh='+str(lh)+' dy='+str(dy)+' colunas='+str(n),2)
   P.put(0,7,'\u25c2\u25b8 largura \xb7 \u25b4\u25be altura \xb7 + - base',7)
   P.put(0,8,'Os M devem acabar antes da margem.',7)
   U.foot('enter: guardar \xb7 esc: cancelar')
   P.show()
   k=P.key()
   if k=='left':
    cw=max(5,cw-1)
   elif k=='right':
    cw=min(12,cw+1)
   elif k=='up':
    lh=max(12,lh-1)
   elif k=='down':
    lh=min(24,lh+1)
   elif k=='+':
    dy+=1
   elif k=='-':
    dy-=1
   elif k=='enter':
    c[8],c[9],c[10]=(cw,lh,dy)
    A.save('m1def')
    return
   elif k=='esc':
    P.metrics(c[8],c[9],c[10])
    return
 AJ=(('Teclas e navega\xe7\xe3o',('- n\xfamero: escolhe a op\xe7\xe3o (1 e depois 2 escolhe a 12)\n- setas \u25b4\u25be: mudam a op\xe7\xe3o ou deslizam o texto\n- setas \u25c2\u25b8: p\xe1gina anterior ou seguinte\n- enter: confirma; '
'num texto longo, avan\xe7a\n- esc ou 0: volta ao ecr\xe3 anterior\n- del: apaga um car\xe1cter; clear: limpa o campo\n- shift: uma mai\xfascula; tab: fixa as mai\xfasculas\nO rodap\xe9 diz sempre o qu'
'e fazem enter e esc.')),('N\xfameros e express\xf5es',('N\xfameros: 2,5 ou 2.5; fra\xe7\xf5es 3/4; nota\xe7\xe3o cient\xedfica 6,02e23 ou 6,02*10^23.\nExpress\xf5es: + - * / ^, par\xeanteses, |x| (m\xf3dulo), pi, sqrt( ) ou \u221a, sin cos tan (tamb\xe9m s'
'en e tg).\nMultiplica\xe7\xe3o impl\xedcita: 2x e 3(x+1).\nans \xe9 o \xfaltimo resultado de uma calculadora.\nListas de dados: separa os valores com espa\xe7os (2,5 3,1 4); com \xd7 10^n, usa ; entre'
' os valores.')),('Unidades e f\xf3rmulas qu\xedmicas',('Nas calculadoras, se um campo tem v\xe1rias unidades, \u25be leva \xe0 unidade e \u25c2\u25b8 mudam-na.\nF\xf3rmulas qu\xedmicas: mai\xfasculas e min\xfasculas como na tabela: H2SO4, Ca(OH)2, CuSO4.5H'
'2O (o ponto separa a \xe1gua de hidrata\xe7\xe3o). Co \xe9 cobalto; CO \xe9 mon\xf3xido de carbono.')),('Gravar o progresso','A app guarda as defini\xe7\xf5es e o progresso em vari\xe1veis do documento (m1def, m1prog...).\nPara ficarem guardados de vez, grava o documento: ctrl+S (ou menu Ficheiro > Guardar) antes de o fechar.'),
('Modo de exame','Em modo de exame (Press-to-Test) a calculadora torna os documentos inacess\xedveis. A M1TR4M n\xe3o tenta contornar isso: \xe9 uma ferramenta de estudo para usar fora dos testes.'))
 def help_():
  sel=0
  while True:
   r=U.menu('Ajuda',[a[0]for a in AJ],sel)
   if r<0:
    return
   sel=r
   U.text(AJ[r][0],AJ[r][1])
 def about():
  U.text('Sobre a M1TR4M','# M1TR4M '+A.APPV+' \xb7 by M1TR4M\nF\xedsica e Qu\xedmica A (10.\xba ano) e Matem\xe1tica (7.\xba ao 10.\xba ano).\nBuild: '+A.K.BUILD+('\n\n# Fontes\n- Aprendizagens Essenciais (DGE): FQ A, FQ 7.\xba-9.\xba, Matem\xe1tica 7.\xba-9.\xba (2021) e Mat A\n- Programa de F\xedsica e Qu\xedmica A (DGE)\n- Tabelas de constantes e formul\xe1ri'
'o do exame de FQ A (IAVE)\n- Dados da tabela peri\xf3dica: ver a ficha de cada elemento\n\n# Limita\xe7\xf5es conhecidas\n')+A.K.LIMITES)
 def diag():
  while True:
   A.S['where']='diagn\xf3stico'
   r=U.menu('Diagn\xf3stico',['Resumo do aparelho','Teste de teclas','Teste de grava\xe7\xe3o','R\xe9gua de calibra\xe7\xe3o'])
   if r<0:
    return
   if r==0:
    summary()
   elif r==1:
    keytest()
   elif r==2:
    savetest()
   else:
    calib()
 def summary():
  f=P.free()
  d=P.today()
  m=C.SL['p'][0]
  o=['Vers\xe3o: '+A.APPV+' (build '+A.K.BUILD+')','Plataforma: '+P.platform(),'Ecr\xe3: '+str(P.E['W'])+' x '+str(P.E['H'])+' px, '+str(P.E['cols'])+' colunas, '+str(P.E['rows'])+' linhas','Mem\xf3ria livre: arranque '+str(A.S['f0'])+', agora '+str(f),
'Importa\xe7\xe3o: '+A.S['imp']+(' ('+P.mod_file(P)+')'if P.mod_file(P)else ''),'sys.modules: '+('sim'if P.has_mods()else 'n\xe3o (m\xe1x. 2 pacotes)'),'Grava\xe7\xe3o: '+('funciona'if A.S['gv']else 'falhou'),
'Data: '+(str(d[2])+'/'+str(d[1])+'/'+str(d[0])if d else 'sem data (o progresso funciona sem datas)'),'S\xedmbolos: '+('completos','Latin-1','letras simples')[2-P.E['sym']]+' \xb7 teste: \u221a \u0394 \u03c0 \u2248 \u2192 \u2208 \u2264 \xb2 \xb3']
  for w in P.E['log']+C.WARN:
   o.append('! '+w)
  U.text('Diagn\xf3stico','\n'.join(o))
 def keytest():
  ks=[]
  while True:
   P.begin()
   U.title('Teste de teclas')
   P.put(0,1,'Carrega em teclas; esc duas vezes: sair.',7)
   for i in range(len(ks)):
    P.put(0,2+i,str(i+1)+': ['+ks[i]+'] \u2192 '+P.norm(ks[i]),0)
   U.foot('esc esc: sair')
   P.show()
   k=P.raw_key()
   ks.append(str(k))
   ks=ks[-8:]
   if len(ks)>=2 and P.norm(ks[-1])=='esc'and(P.norm(ks[-2])=='esc'):
    return
 def savetest():
  ok=P.save('m1t',[1,2.5,3])
  v=P.load('m1t')
  good=ok and v is not None and(len(v)==3)and(abs(v[1]-2.5)<1e-09)
  A.S['gv']=good
  U.msg('Teste de grava\xe7\xe3o','+ '+U.OKS+'store_list e recall_list funcionam.'if good else '! '+U.ERS+'A grava\xe7\xe3o falhou: a app funciona, mas sem guardar o progresso.')
 return _ns('P N U C A run summary',P,N,U,C,A,run,summary)


_F['m1_cfg'] = _m_m1_cfg


def _m_m1_cont():
 P=_imp('m1_plat')
 PVER=1
 SL={'p':[None,''],'c':[None,''],'f':[None,''],'k':[None,'']}
 SEEN=[]
 WARN=[]
 class Falta(Exception):
  pass
 def drop(slot):
  n=SL.get(slot,[None,''])[1]
  SL[slot]=[None,'']
  if n:
   P.unload(n)
  P.collect()
 def get(slot,name):
  s=SL.get(slot)
  if s and s[1]==name and(s[0]is not None):
   return s[0]
  drop(slot)
  if not P.has_mods()and name not in SEEN:
   if len(SEEN)>=2 and 0<=P.free()<250000:
    raise Falta('Mem\xf3ria: sai e volta a abrir a app para abrir outro tema (sem sys.modules).')
   SEEN.append(name)
   if len(SEEN)>2 and(not WARN):
    WARN.append('sem sys.modules: os pacotes ficam em mem\xf3ria')
  try:
   m=_imp(name)
  except ImportError:
   ed=globals().get('_ED')
   raise Falta('A edi\xe7\xe3o de reserva '+ed+' n\xe3o inclui '+name if ed else 'Falta o m\xf3dulo '+name+' (instala '+name+'.tns)')
  except MemoryError:
   P.collect()
   raise
  D=getattr(m,'D',None)
  if D is not None:
   try:
    check(D,name)
   except Falta:
    P.unload(name)
    raise
  SL[slot]=[m,name]
  return m
 def check(D,name):
  v=head(D,'V')
  if v!=str(PVER):
   raise Falta('M\xf3dulo '+name+' desatualizado (vers\xe3o '+v+'; esta app l\xea a '+str(PVER)+')')
  nl=head(D,'N')
  k=D.count('\n@L ')or D.count('\n@X ')
  if nl!=''and(not nl.isdigit()or(k and int(nl)!=k)):
   raise Falta('M\xf3dulo '+name+' estragado (instala '+name+'.tns de novo)')
 def head(D,k):
  i=D.find('@'+k+' ')
  if i<0 or i>200:
   return ''
  j=D.find('\n',i)
  return D[i+3:j].strip()
 def recs(D,tag):
  out=[]
  k='\n@'+tag+' '
  i=D.find(k)
  while i>=0:
   j=D.find('\n',i+1)
   out.append((D[i+len(k):j].split('|'),i))
   i=D.find(k,j)
  return out
 def body(D,i):
  j=D.find('\n',i+1)
  e=len(D)
  for t in('\n@L ','\n@E ','\n@X '):
   k=D.find(t,j)
   if 0<=k<e:
    e=k
  return D[j+1:e].rstrip('\n')
 def parts(txt):
  d={}
  fs=[]
  cur='T'
  buf=[]
  for ln in txt.split('\n'):
   if len(ln)>=2 and ln[0]=='@'and(ln[1]in 'ABCDEFGHIJROSPD')and(len(ln)==2 or ln[2]==' '):
    if cur is not None:
     d[cur]='\n'.join(buf)
    cur=ln[1]
    buf=[]
    if cur=='F'and len(ln)>3:
     fs.append(ln[3:].split('|'))
     cur=None
    elif len(ln)>3:
     buf.append(ln[3:])
    continue
   if cur is not None:
    buf.append(ln)
  if cur is not None:
   d[cur]='\n'.join(buf)
  d['F*']=fs
  return d
 def ftext(f):
  o=['# '+f[0],'= '+f[1]]
  if len(f)>2 and f[2]:
   for s in f[2].split(';'):
    o.append('- '+s.strip())
  if len(f)>3 and f[3]:
   o.append('Condi\xe7\xf5es: '+f[3])
  if len(f)>4 and f[4]:
   o.append('Exemplo: '+f[4])
  return '\n'.join(o)
 def lesson(D,lid):
  for h,i in recs(D,'L'):
   if h[0]==lid:
    d=parts(body(D,i))
    pg=[]
    for c in 'ABCDEFGHIJ':
     pg.append(d.get(c,''))
    fs=d['F*']
    if fs:
     pg[4]='\n\n'.join([ftext(f)for f in fs])
    return(h,pg,d.get('R',''),fs)
  raise Falta('Li\xe7\xe3o '+lid+' n\xe3o encontrada')
 return _ns('P SL WARN Falta drop get check recs body parts ftext lesson',P,SL,WARN,Falta,drop,get,check,recs,body,parts,ftext,lesson)


_F['m1_cont'] = _m_m1_cont


def _m_m1_ex():
 P=_imp('m1_plat')
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 C=_imp('m1_cont')
 A=_imp('m1_app')
 TIPO={'m':'Escolha m\xfaltipla','n':'Num\xe9rico','u':'Num\xe9rico com unidade','v':'Verdadeiro ou falso'}
 MARCA=('\xb7','\u2717','\u2713')
 SEM=[1]
 def rnd(n):
  SEM[0]=(SEM[0]*1103515245+12345)%2147483648
  return SEM[0]%n
 def baralha(lst):
  SEM[0]=P.ms()%2147483648 or 7
  for i in range(len(lst)-1,0,-1):
   j=rnd(i+1)
   lst[i],lst[j]=(lst[j],lst[i])
  return lst
 def load(ti):
  t=A.th(ti)
  D=C.get('p',t[5]).D
  out=[]
  for h,pos in C.recs(D,'X'):
   d=C.parts(C.body(D,pos))
   d['h']=h
   out.append(d)
  return out
 def first(x):
  t=x.get('T','').split('\n')[0]
  return t if t else TIPO[x['h'][0]]
 def state(gi):
  return A.S['ex'][gi]if gi<len(A.S['ex'])else 0
 def setst(gi,ok):
  if gi<len(A.S['ex']):
   if ok:
    A.S['ex'][gi]=2
   elif A.S['ex'][gi]!=2:
    A.S['ex'][gi]=1
 def ask(x,t,n,k,test=0):
  h=x['h']
  tp=h[0]
  head=t+' \xb7 '+str(k+1)+'/'+str(n)
  txt=x.get('T','')
  if tp in 'mv':
   ops=x.get('O','').split('|')if tp=='m'else['Verdadeiro','Falso']
   s=txt+'\n'
   for i in range(len(ops)):
    s=s+'\n'+str(i+1)+') '+ops[i]
   while True:
    r=U.text(head,s,'n\xfamero: responder','',tuple([str(i+1)for i in range(len(ops))]))
    if r=='esc':
     return None
    if r in '1234'and r:
     sol=x.get('S','').strip()
     if tp=='v':
      sol='1'if sol=='V'else '2'
     return r==sol
  if tp=='n':
   while True:
    a=U.edit(head,txt,'','Escreve o n\xfamero (aceita 2,5, 1/2, 5e-1). esc: '+('passar'if test else 'voltar'))
    if a is None:
     return None
    try:
     return N.check(a,N.num(x['S'])[0],h[3],A.TOL[A.S['cfg'][6]])
    except ValueError as e:
     U.msg(head,U.ERS+str(e),5)
  us=h[4].split(' ')
  fs=[N.fld('Valor','',''),N.fld('Unidade','','','c',us)]
  while True:
   if U.text(head,txt+'\n\nenter: responder (valor e unidade)','','',('enter',))=='esc':
    return None
   if not U.form(head,fs):
    return None
   try:
    v=N.num(fs[0][2])[0]
    v=N.conv(v,us[fs[1][3]],us[0])
    return N.check(v,N.num(x['S'])[0],h[3],A.TOL[A.S['cfg'][6]])
   except ValueError as e:
    fs[0][5]=str(e)
 def show_sol(x,t):
  s=x.get('D','')
  h=x['h']
  if h[0]=='m':
   ops=x.get('O','').split('|')
   k=int(x['S'])-1
   s='Resposta: '+str(k+1)+') '+ops[k]+'\n\n'+s
  elif h[0]=='v':
   s='Resposta: '+('Verdadeiro'if x['S'].strip()=='V'else 'Falso')+'\n\n'+s
  else:
   s='Resposta: '+x['S'].strip()+(' '+h[4].split(' ')[0]if h[0]=='u'else '')+'\n\n'+s
  U.text('Resolu\xe7\xe3o \xb7 '+t,s)
 def train(ti):
  t=A.th(ti)
  if not t[5]:
   U.msg('Exerc\xedcios','Este tema n\xe3o tem exerc\xedcios.')
   return
  off=int(t[9])+1
  sel=0
  while True:
   xs=load(ti)
   it=[]
   for i in range(len(xs)):
    st=state(off+i)
    it.append(MARCA[st]+' '+first(xs[i]))
   A.S['where']='treino '+t[0]
   r=U.menu('Treino \xb7 '+t[3],it,sel,'\u2713 certo \xb7 \u2717 errado \xb7 \xb7 por fazer \xb7 esc')
   if r<0:
    A.save('m1prog')
    return
   x=xs[r]
   xs=None
   while True:
    ok=ask(x,t[3],len(it),r)
    if ok is None:
     break
    setst(off+r,ok)
    if ok:
     k=U.text(t[3],'+ '+U.OKS+'Certo!\n\n1: ver a resolu\xe7\xe3o \xb7 enter: seguinte','','',('1',))
     if k=='1':
      show_sol(x,t[3])
     break
    k=U.text(t[3],'! '+U.ERS+'Ainda n\xe3o est\xe1 certo.\n\n1: tentar outra vez\n2: ver a pista\n3: ver a resolu\xe7\xe3o\n4: ir \xe0 li\xe7\xe3o','','',('1','2','3','4'))
    if k=='2':
     U.text('Pista',x.get('P',''))
     continue
    if k=='3':
     show_sol(x,t[3])
     break
    if k=='4':
     A.save('m1prog')
     A.goto_lesson(x['h'][2])
     break
    if k!='1':
     break
   A.save('m1prog')
   sel=min(r+1,len(it)-1)
 def one(a):
  ti,k=a
  t=A.th(ti)
  x=load(ti)[k]
  while True:
   ok=ask(x,t[3],int(t[8]),k)
   if ok is None:
    break
   setst(int(t[9])+1+k,ok)
   A.save('m1prog')
   if U.text(t[3],('+ '+U.OKS+'Certo!'if ok else '! '+U.ERS+'Ainda n\xe3o est\xe1 certo.')+'\n\n1: ver a resolu\xe7\xe3o \xb7 2: tentar outra vez','','',('1','2'))=='1':
    show_sol(x,t[3])
    break
   if ok:
    break
 def test(ti):
  t=A.th(ti)
  if not t[5]:
   U.msg('Teste','Este tema n\xe3o tem exerc\xedcios.')
   return
  off=int(t[9])+1
  xs=load(ti)
  n=len(xs)
  order=baralha(list(range(n)))
  res=[None]*n
  A.S['where']='teste '+t[0]
  if not U.ask('Teste do cap\xedtulo',str(n)+' perguntas por ordem baralhada. esc numa pergunta deixa-a sem resposta. Come\xe7ar?',1):
   return
  for k in range(n):
   i=order[k]
   r=ask(xs[i],t[3],n,k,1)
   res[i]=r
   if r is not None:
    setst(off+i,r)
  A.save('m1prog')
  c=len([r for r in res if r])
  A.S['tst'][1+2*ti]=c
  A.S['tst'][2+2*ti]=n
  A.save('m1tst')
  sel=0
  while True:
   it=[]
   for k in range(n):
    i=order[k]
    r=res[i]
    m='\u2014'if r is None else U.OKS if r else U.ERS
    it.append(m+first(xs[i]))
   r=U.menu(str(c)+' de '+str(n)+' certas',it,sel,'enter: ver a resolu\xe7\xe3o \xb7 esc: sair')
   if r<0:
    break
   sel=r
   show_sol(xs[order[r]],t[3])
  U.msg('Teste do cap\xedtulo',str(c)+' de '+str(n)+' certas.\n\nO resultado diz respeito s\xf3 a estas perguntas.')
 def cards(ti):
  t=A.th(ti)
  D=C.get('p',t[4]).D
  out=[]
  for f,pos in C.recs(D,'F'):
   out.append(('F\xf3rmula: '+f[0]+'\n\n(enter: ver)','= '+f[1]+('\n- '+'\n- '.join(f[2].split(';'))if len(f)>2 and f[2]else '')))
  for h,pos in C.recs(D,'L'):
   d=C.parts(C.body(D,pos))
   if d.get('J'):
    out.append((h[1]+'\n\n'+d['J']+'\n\n(enter: ver)',d.get('R','')))
  return out
 def review(ti):
  r=U.menu('Revis\xe3o r\xe1pida \xb7 '+A.th(ti)[3],['Resumos (p\xe1ginas I)','Cart\xf5es pergunta-resposta'])
  if r==0:
   A.nav('summary',ti)
  elif r==1:
   flash(ti)
 def flash(ti):
  t=A.th(ti)
  off=int(t[11])+1
  cs=cards(ti)
  if not cs:
   U.msg('Cart\xf5es','Este tema n\xe3o tem cart\xf5es.')
   return
  rv=A.S['rev']
  SEM[0]=P.ms()%2147483648 or 7
  pool=[]
  for i in range(len(cs)):
   b=rv[off+i]if off+i<len(rv)else 0
   pool=pool+[i]*(3-min(2,max(0,b-1)))
  feitos=0
  while feitos<10 and pool:
   i=pool[rnd(len(pool))]
   f,v=cs[i]
   k=U.text('Cart\xe3o '+str(feitos+1)+'/10',f)
   if k=='esc':
    break
   k=U.text('Cart\xe3o \xb7 verso',v+'\n\n1: sabia \xb7 2: n\xe3o sabia','','',('1','2'))
   if k=='esc':
    break
   if off+i<len(rv):
    b=max(1,rv[off+i])
    rv[off+i]=min(3,b+1)if k=='1'else 1
   pool=[j for j in pool if j!=i]+([i]if k!='1'else[])
   feitos+=1
  A.save('m1rev')
 def progress():
  while True:
   A.S['where']='progresso'
   r=U.menu('O meu progresso',['Continuar onde fiquei','Por tema','Temas a rever','Apagar o progresso'])
   if r<0:
    return
   if r==0:
    p=A.S['pos']
    if p[1]==1:
     A.open_lesson(p[2],p[3],p[4])
    else:
     U.msg('Continuar','Ainda n\xe3o abriste nenhuma li\xe7\xe3o.')
   elif r==1:
    bytheme()
   elif r==2:
    torev()
   else:
    A.wipe()
 def stats(i):
  t=A.th(i)
  nl=int(t[6])
  ol=int(t[7])+1
  vl=len([k for k in range(nl)if A.S['lic'][ol+k]])
  ne=int(t[8])
  oe=int(t[9])+1
  sts=[state(oe+k)for k in range(ne)]
  return(vl,nl,len([s for s in sts if s]),len([s for s in sts if s==2]),ne,A.S['tst'][1+2*i],A.S['tst'][2+2*i])
 def bytheme():
  o=[]
  for i in range(len(A.K.TEMAS)):
   vl,nl,f,c,ne,tc,tn=stats(i)
   o.append('# '+A.th(i)[3])
   s='Li\xe7\xf5es vistas: '+str(vl)+'/'+str(nl)
   if ne:
    s=s+'\nExerc\xedcios: '+str(f)+'/'+str(ne)+' feitos, '+str(c)+' certos'
   if tn:
    s=s+'\n\xdaltimo teste: '+str(tc)+' de '+str(tn)+' certas'
   o.append(s)
  U.text('Progresso por tema','\n'.join(o))
 def torev():
  o=[]
  for i in range(len(A.K.TEMAS)):
   vl,nl,f,c,ne,tc,tn=stats(i)
   if f and(f-c)*2>=f:
    o.append('- '+A.th(i)[3]+' ('+str(f-c)+' de '+str(f)+' errados)')
  U.text('Temas a rever','\n'.join(o)if o else 'Nenhum tema tem metade ou mais dos exerc\xedcios errados.')
 return _ns('P N U C A load ask train one test review progress',P,N,U,C,A,load,ask,train,one,test,review,progress)


_F['m1_ex'] = _m_m1_ex


def _m_m1_ini():
 P=_imp('m1_plat')
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 A=_imp('m1_app')
 K=_imp('m1_cat')
 S=A.S
 def start():
  load_state()
  splash()
 def _ld(nm,n,fill=0):
  v=P.load(nm)
  ok=v is not None and len(v)>=1
  if ok:
   try:
    v=[int(x)for x in v]
    ok=v[0]==1
   except Exception:
    ok=False
  if not ok:
   if v is None and nm=='m1def':
    S['gv']=P.save('m1t',[1])
   v=[1]
  v=v[:n+1]
  while len(v)<n+1:
   v.append(fill)
  return v
 def load_state():
  c=_ld('m1def',len(A.DEF)-1)
  if len(c)!=len(A.DEF)or(c[1]==0 and c[8]==0):
   c=list(A.DEF)
  S['cfg']=c
  S['ex']=_ld('m1prog',K.NEX)
  S['lic']=_ld('m1lic',K.NLIC)
  S['tst']=_ld('m1tst',2*len(K.TEMAS))
  S['rev']=_ld('m1rev',K.NCART)
  S['pos']=_ld('m1pos',4)
  A.apply_cfg()
 def splash():
  t0=P.ms()
  W=P.E['W']
  H=P.E['H']
  if not P.E['g']:
   print('M1TR4M \xb7 F\xedsica e Qu\xedmica A 10.\xba \xb7 Matem\xe1tica 7.\xba-10.\xba \xb7 by M1TR4M')
   return
  import math
  cx=W//2
  cy=62
  for fr in range(12):
   P.begin()
   a=fr*0.5
   for o in range(3):
    pts=[]
    for s in range(0,360,30):
     r=s*math.pi/180
     x=70*math.cos(r)
     y=22*math.sin(r)
     ang=o*math.pi/3
     pts.append((cx+x*math.cos(ang)-y*math.sin(ang),cy+x*math.sin(ang)+y*math.cos(ang)))
    P.poly([p[0]for p in pts],[p[1]for p in pts],4)
    r=a+o*2.1
    x=70*math.cos(r)
    y=22*math.sin(r)
    ang=o*math.pi/3
    P.circ(cx+x*math.cos(ang)-y*math.sin(ang),cy+x*math.sin(ang)+y*math.cos(ang),4,5,1)
   P.circ(cx,cy,9,2,1)
   for k in range(3):
    P.poly([18+k*8,40+k*8,29+k*8],[190-k*30,190-k*30,170-k*30],6 if k%2 else 3)
   big('M1TR4M',cx-84,104,4)
   s='F\xedsica e Qu\xedmica A 10.\xba \xb7 Matem\xe1tica 7.\xba-10.\xba'
   P.txt(cx-len(s)*P.E['cw']//2,146,s,0)
   P.txt(cx-6*P.E['cw']//2,166,'by M1TR4M',7)
   P.show()
   if P.key(0)or P.ms()-t0>1800:
    break
 BIG={'M':(17,27,21,21,17,17,17),'1':(4,12,4,4,4,4,14),'T':(31,4,4,4,4,4,4),'R':(30,17,17,30,20,18,17),'4':(2,6,10,18,31,2,2)}
 def big(s,x,y,k):
  for ch in s:
   rows=BIG.get(ch,())
   for r in range(len(rows)):
    for c in range(5):
     if rows[r]&16>>c:
      P.rect(x+c*k,y+r*k,k,k,2)
   x+=6*k
 return _ns('P N U A K S start',P,N,U,A,K,S,start)


_F['m1_ini'] = _m_m1_ini


def _m_m1_nav():
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 C=_imp('m1_cont')
 A=_imp('m1_app')
 S=A.S
 th=A.th
 DN=A.DN
 NIV=A.NIV
 calc=A.calc
 cname=A.cname
 calcs=A.calcs
 tool=A.tool
 K=A.K
 def pick():
  d=pick_disc()
  return pick_theme(d)if d else-1
 def pick_disc():
  r=U.menu('Disciplina',[DN['F'],DN['M']])
  return('F','M')[r]if r>=0 else ''
 def pick_theme(d):
  gs=A.grupos(d)
  if not gs:
   U.msg(DN[d],'Esta edi\xe7\xe3o n\xe3o tem temas de '+DN[d]+'.')
   return-1
  while True:
   g=0
   if len(gs)>1:
    g=U.menu(DN[d],[x[1]for x in gs])
    if g<0:
     return-1
   ts=gs[g][2]
   r=U.menu(gs[g][1],[th(i)[3]for i in ts])
   if r>=0:
    return ts[r]
   if len(gs)==1:
    return-1
 def ex_menu(i):
  r=U.menu(th(i)[3],['Treino (um exerc\xedcio de cada vez)','Teste do cap\xedtulo'])
  if r==0:
   tool('m1_ex','train',i)
  elif r==1:
   tool('m1_ex','test',i)
 def flist(i):
  D=C.get('p',th(i)[4]).D
  ls=C.recs(D,'L')
  out=[]
  for f,pos in C.recs(D,'F'):
   lt=''
   for h,p in ls:
    if p<pos:
     lt=h[1]
   out.append((f,lt))
  return out
 def formulas(i):
  fs=flist(i)
  if not fs:
   U.msg('Formul\xe1rio','Este tema n\xe3o tem f\xf3rmulas.')
   return
  sel=0
  while True:
   S['where']='formul\xe1rio'
   r=U.menu('Formul\xe1rio \xb7 '+th(i)[3],[f[0][0]for f in fs],sel)
   if r<0:
    return
   sel=r
   fshow(i,r,fs)
 def fshow(i,k,fs=None):
  if fs is None:
   fs=flist(i)
  f,lt=fs[k]
  s=C.ftext(f)+'\nLi\xe7\xe3o: '+lt
  cid=f[5]if len(f)>5 else ''
  if cid:
   s=s+'\nCalculadora: '+cname(cid)+' (tecla c)'
  if U.text('F\xf3rmula',s,'','',('c',)if cid else())=='c':
   calc(cid)
 def examples(i):
  D=C.get('p',th(i)[4]).D
  es=C.recs(D,'E')
  D=None
  if not es:
   U.msg('Exemplos','Este tema n\xe3o tem exemplos.')
   return
  sel=0
  while True:
   S['where']='exemplos'
   r=U.menu('Exemplos \xb7 '+th(i)[3],[NIV[int(e[0][0])]+': '+e[0][2]for e in es],sel)
   if r<0:
    return
   sel=r
   eshow(i,r)
 def eshow(i,k):
  D=C.get('p',th(i)[4]).D
  h,pos=C.recs(D,'E')[k]
  b=C.body(D,pos)
  D=None
  cid=h[3]if len(h)>3 else ''
  if U.text(NIV[int(h[0])]+': '+h[2],b,'c: calculadora'if cid else '','',('c',)if cid else())=='c':
   calc(cid)
 def summary(i):
  D=C.get('p',th(i)[4]).D
  o=[]
  for h,pos in C.recs(D,'L'):
   d=C.parts(C.body(D,pos))
   if d.get('I'):
    o.append('# '+h[1])
    o.append(d['I'])
    o.append('')
  D=None
  U.text('Resumo \xb7 '+th(i)[3],'\n'.join(o))
 def calc_menu(d):
  ds=(('F',DN['F']),('M',DN['M']),('C','Comuns'))
  while True:
   S['where']='calculadoras'
   r=U.menu('Calculadoras',[x[1]for x in ds]+['Hist\xf3rico (\xfaltimos 5)'])
   if r<0:
    return
   if r==3:
    hist()
    continue
   cs=[c for c in calcs()if c[2]==ds[r][0]]
   gs=[]
   for g in A.grupos(ds[r][0]):
    ids=[c[0]for i in g[2]for c in cs if c[3]==th(i)[0]]
    if ids:
     gs.append((g[1],ids))
   if not cs:
    U.msg(ds[r][1],'Esta edi\xe7\xe3o n\xe3o tem calculadoras de '+ds[r][1]+'.')
    continue
   if not gs:
    calc_list([c[0]for c in cs],ds[r][1])
    continue
   s=0
   while True:
    q=U.menu(ds[r][1],[g[0]for g in gs],s)
    if q<0:
     break
    s=q
    calc_list(gs[q][1],gs[q][0])
 def calc_list(ids,t):
  names=[cname(c)for c in ids]
  sel=0
  while True:
   r=U.menu(t,names,sel)
   if r<0:
    return
   sel=r
   calc(ids[r])
 def hist():
  h=S['h']
  if not h:
   U.msg('Hist\xf3rico','Ainda n\xe3o h\xe1 resultados.')
   return
  r=U.menu('Hist\xf3rico',[x[0]+' = '+N.fmt(x[1])+' '+x[2]for x in h],0,'enter: usar como ans \xb7 esc')
  if r>=0:
   N.CF['ans']=h[r][1]
   U.msg('Hist\xf3rico','Escreve ans num campo para usar '+N.fmt(h[r][1])+'.')
 def consts():
  r=U.menu('Constantes e unidades',['Constantes e dados','Conversor de unidades','Prefixos do SI'])
  if r>=0:
   calc(('c_comd.cte','c_comu.uni','c_comu.pre')[r])
 return _ns('N U C A S th DN NIV calc cname calcs tool K pick ex_menu formulas fshow examples eshow summary calc_menu calc_list consts',N,U,C,A,S,th,DN,NIV,calc,cname,calcs,tool,K,pick,ex_menu,formulas,
fshow,examples,eshow,summary,calc_menu,calc_list,consts)


_F['m1_nav'] = _m_m1_nav


def _m_m1_nucleo():
 import math
 P=_imp('m1_plat')
 LN10=math.log(10.0)
 CF={'ang':0,'dec':4,'sci':6,'ans':None}
 SUPD='\u2070\xb9\xb2\xb3\u2074\u2075\u2076\u2077\u2078\u2079'
 X='\xd7'
 AP='\u2248'
 def err(m):
  raise ValueError(m)
 def ok(v):
  return v-v==0
 def chk(v):
  if not ok(v):
   err('Valor demasiado grande')
  return v
 def sup(n):
  o=[]
  for ch in str(n):
   if ch=='-':
    o.append('\u207b')
   else:
    o.append(SUPD[ord(ch)-48])
  return ''.join(o)
 def _sc(a,k):
  while k>22:
   a=a*_p10(22)
   k-=22
  while k<-22:
   a=a/_p10(22)
   k+=22
  if k>=0:
   return a*_p10(k)
  return a/_p10(-k)
 def _p10(k):
  if k<=15:
   return float(10**k)
  return float(10**15)*float(10**(k-15))
 def dig(c):
  return '0'<=c<='9'
 def _fl(t):
  k=t.find('/')
  if k>0:
   return _fl(t[:k])/_fl(t[k+1:])
  neg=t.startswith('-')
  if neg or t.startswith('+'):
   t=t[1:]
  ex=0
  k=t.find('e')
  if k<0:
   k=t.find('E')
  if k>=0:
   ex=int(t[k+1:])
   t=t[:k]
  v=_dn(t,ex)
  return-v if neg else v
 def _dn(t,ex=0):
  t=t.replace('.',',')
  k=t.find(',')
  d=0
  if k>=0:
   d=len(t)-k-1
   t=t[:k]+t[k+1:]
  if t=='':
   t='0'
  return _sc(float(int(t)),ex-d)
 def _e10(a):
  e=int(math.floor(math.log(a)/LN10))
  v=_sc(a,-e)
  if v>=10:
   e+=1
  elif v<1:
   e-=1
  return e
 def _rnd(v):
  return int(math.floor(v+0.5+v*1e-15))
 def _ds(m,d):
  s=str(m)
  if d<=0:
   return s
  if len(s)<=d:
   s='0'*(d-len(s)+1)+s
  return s[:-d]+','+s[-d:]
 def _strip(s):
  if ','in s:
   s=s.rstrip('0')
   if s.endswith(','):
    s=s[:-1]
  return s
 def sci(m,e,n):
  s=_ds(m,n-1)
  if e==0:
   return s
  return s+' '+X+' 10'+sup(e)
 def fmt2(x,sf=0,dec=-1,strip=1):
  if isinstance(x,int)and sf<=0:
   if abs(x)<10**12:
    return(str(x),True)
   x=float(x)
  x=float(x)
  if not ok(x):
   err('Valor demasiado grande')
  neg=x<0
  a=-x if neg else x
  if a==0:
   if sf>0:
    return('0,'+'0'*(sf-1)if sf>1 else '0',True)
   return('0',True)
  e=_e10(a)
  hi=CF['sci']
  if sf>0:
   sf=min(sf,13)
   m,e=_sig(a,sf)
   exact=abs(_sc(float(m),e-sf+1)-a)<=a*1e-12
   if e>=hi or e<-3 or e>=sf:
    s=sci(m,e,sf)
   elif e==sf-1:
    s=str(m)
   else:
    s=_ds(m,sf-1-e)
  else:
   if dec<0:
    dec=CF['dec']
   if e>=12 or(e<-dec and e<-3):
    n=max(dec,4)
    m,e=_sig(a,n)
    exact=abs(_sc(float(m),e-n+1)-a)<=a*1e-12
    s=_strip(_ds(m,n-1))if strip else _ds(m,n-1)
    s=s+' '+X+' 10'+sup(e)
   else:
    if e+dec>12:
     dec=max(0,12-e)
    v=_sc(a,dec)
    m=_rnd(v)
    exact=abs(float(m)-v)<=v*1e-12+1e-09
    s=_ds(m,dec)
    if strip:
     s=_strip(s)
  if neg and s.strip('0,')!='':
   s='-'+s
  return(s,exact)
 def _sig(a,n):
  e=_e10(a)
  m=_rnd(_sc(a,n-1-e))
  if m>=10**n:
   m=m//10
   e+=1
  return(m,e)
 def fmt(x,sf=0,dec=-1):
  return fmt2(x,sf,dec)[0]
 def eq(x,sf=0,dec=-1):
  s,e=fmt2(x,sf,dec,0 if dec>=0 else 1)
  return('= 'if e else AP+' ')+s
 def fix(x,d):
  return fmt2(x,0,d,0)[0]
 def fsf(x,n):
  return fmt2(x,max(1,n))[0]
 def _clean(s):
  s=s.strip()
  for a,b in(('\u2212','-'),(X,'*'),('\xb7','*'),('\xf7','/'),(' ','')):
   s=s.replace(a,b)
  return s
 def num(s,allow_x=0):
  t=_clean(s)
  if t=='':
   err('Escreve um n\xfamero, por exemplo 2,5')
  r=_simple(t)
  if r is not None:
   return r
  v=ev(comp(t,0))
  return(chk(v),0)
 def _simple(t):
  i=0
  n=len(t)
  if i<n and t[i]in '+-':
   i+=1
  j=i
  seps=0
  while j<n and(dig(t[j])or t[j]in ',.'):
   if t[j]in ',.':
    seps+=1
   j+=1
  mant=t[i:j]
  if mant==''or mant in ',.':
   return None
  rest=t[j:]
  ex=0
  if rest:
   k=-1
   for p in('*10^','x10^','X10^','*10**'):
    if rest.startswith(p):
     k=len(p)
   if rest[0]in 'eE':
    k=1
   if rest.startswith('*10')and len(rest)>3 and(SUPD.find(rest[3])>=0)or rest.startswith('*10\u207b'):
    rest='*10^'+P.vis(rest[3:],0).lstrip('^')
    k=4
   if k<0:
    return None
   es=rest[k:]
   if es.startswith('(')and es.endswith(')'):
    es=es[1:-1]
   if not _isint(es):
    if es==''or _isint(es.lstrip('+-'))or es in '+-':
     err('Falta o expoente depois de '+rest[:k])
    return None
   ex=int(es)
  if seps>1 or mant[-1]in ',.'or(mant[0]in ',.'and len(mant)==1):
   err('N\xfamero mal escrito: '+t)
  if ex>300 or ex<-300:
   err('Valor demasiado grande')
  v=_dn(mant,ex)
  if t[0]=='-':
   v=-v
  chk(v)
  return(v,sfs(mant))
 def _isint(s):
  if s.startswith('+')or s.startswith('-'):
   s=s[1:]
  if s=='':
   return False
  for c in s:
   if not dig(c):
    return False
  return True
 def sfs(m):
  d=m.replace('.',',')
  has=','in d
  g=d.replace(',','').lstrip('0')
  if g=='':
   k=d.find(',')
   return max(1,len(d)-k-1)if has else 1
  return len(g)
 FN=(('sqrt',23),('raiz',23),('sin',20),('sen',20),('cos',21),('tan',22),('tg',22),('abs',24))
 PRI={10:1,11:1,12:2,13:2,15:3,20:3,21:3,22:3,23:3,24:3,14:4}
 OPC={'+':10,'-':11,'*':12,'/':13,'^':14}
 MAXLEN=200
 MAXDEP=20
 def comp(s,allow_x=1):
  s=_clean(s).replace('**','^').replace('[','(').replace(']',')')
  if s=='':
   err('Express\xe3o vazia')
  if len(s)>MAXLEN:
   err('Express\xe3o demasiado longa (m\xe1x. 200)')
  out=[]
  st=[]
  want=1
  dep=0
  i=0
  n=len(s)
  while i<n:
   ch=s[i]
   tok=None
   if dig(ch)or ch in ',.':
    j=i
    while j<n and(dig(s[j])or s[j]in ',.'):
     j+=1
    ex=0
    if j<n and s[j]in 'eE'and(j+1<n)and(dig(s[j+1])or(s[j+1]in '+-'and j+2<n and dig(s[j+2]))):
     k=j+1
     j+=2
     while j<n and dig(s[j]):
      j+=1
     ex=int(s[k:j])
    t=s[i:j]
    if 'e'in t or 'E'in t:
     t=t[:max(t.find('e'),t.find('E'))]
    if t.count(',')+t.count('.')>1 or t in ',.':
     err('N\xfamero mal escrito: '+t)
    if ex>300 or ex<-300:
     err('Valor demasiado grande')
    tok=_dn(t,ex)
    i=j
   elif ch=='\u03c0':
    tok=math.pi
    i+=1
   elif ch.isalpha()and ord(ch)<128:
    low=s[i:].lower()
    hit=0
    for nm,c in FN:
     if low.startswith(nm):
      hit=c
      i+=len(nm)
      break
    if hit:
     if not want:
      _push(12,out,st)
     st.append(hit)
     if i<n and s[i]=='(':
      st.append(31)
      dep+=1
      if dep>MAXDEP:
       err('Demasiados par\xeanteses (m\xe1x. 20 n\xedveis)')
      i+=1
     want=1
     continue
    if low.startswith('pi'):
     tok=math.pi
     i+=2
    elif low.startswith('ans'):
     tok=2
     i+=3
    elif ch in 'xX'and allow_x:
     tok=1
     i+=1
    elif ch in 'yY'and allow_x>1:
     tok=3
     i+=1
    else:
     err('S\xedmbolo desconhecido: '+ch)
   elif ch=='\u221a':
    if not want:
     _push(12,out,st)
    st.append(23)
    i+=1
    if i<n and s[i]=='(':
     st.append(31)
     dep+=1
     i+=1
    want=1
    continue
   if tok is not None:
    if not want:
     _push(12,out,st)
    if isinstance(tok,int)and tok==2 and(CF['ans']is None):
     err('Ainda n\xe3o h\xe1 resultado anterior (ans)')
    out.append(tok)
    want=0
    continue
   if ch=='(':
    if not want:
     _push(12,out,st)
    st.append(30)
    dep+=1
    if dep>MAXDEP:
     err('Demasiados par\xeanteses (m\xe1x. 20 n\xedveis)')
    want=1
    i+=1
    continue
   if ch==')':
    if want:
     err('Falta um valor antes de )')
    while st and st[-1]not in(30,31,32):
     out.append(st.pop())
    if not st or st[-1]==32:
     err('Par\xeantese a mais')
    m=st.pop()
    dep-=1
    if m==31:
     out.append(st.pop())
    i+=1
    continue
   if ch=='|':
    if not want and 32 in st:
     while st[-1]!=32:
      if st[-1]in(30,31):
       err('Falta fechar um par\xeantese')
      out.append(st.pop())
     st.pop()
     dep-=1
     out.append(24)
     i+=1
     continue
    if not want:
     _push(12,out,st)
    st.append(32)
    dep+=1
    if dep>MAXDEP:
     err('Demasiados par\xeanteses (m\xe1x. 20 n\xedveis)')
    want=1
    i+=1
    continue
   k=SUPD.find(ch)
   if k>=0 or ch=='\u207b':
    if want:
     err('Falta a base antes do expoente')
    j=i
    while j<n and(SUPD.find(s[j])>=0 or s[j]=='\u207b'):
     j+=1
    e=P.vis(s[i:j],0).lstrip('^')
    _push(14,out,st)
    if e.startswith('-'):
     out.append(-float(int(e[1:])))
    else:
     out.append(float(int(e)))
    want=0
    i=j
    continue
   if ch in OPC:
    o=OPC[ch]
    if want:
     if ch=='-':
      st.append(15)
      i+=1
      continue
     if ch=='+':
      i+=1
      continue
     err('Falta um n\xfamero antes de '+ch)
    _push(o,out,st)
    want=1
    i+=1
    continue
   err('S\xedmbolo desconhecido: '+ch)
  if want:
   if out or st:
    err('Falta um n\xfamero no fim')
   err('Express\xe3o vazia')
  while st:
   o=st.pop()
   if o in(30,31):
    err('Falta fechar um par\xeantese')
   if o==32:
    err('Falta fechar o m\xf3dulo |')
   out.append(o)
  return out
 def _push(o,out,st):
  p=PRI[o]
  while st:
   t=st[-1]
   if t>=30:
    break
   q=PRI[t]
   if q>p or(q==p and o!=14 and(t<15)):
    out.append(st.pop())
   else:
    break
  st.append(o)
 def ev(code,x=0.0,y=0.0):
  st=[]
  for c in code:
   if isinstance(c,float):
    st.append(c)
   elif c==1:
    st.append(x)
   elif c==3:
    st.append(y)
   elif c==2:
    st.append(CF['ans'])
   elif c<15:
    b=st.pop()
    a=st.pop()
    if c==10:
     a=a+b
    elif c==11:
     a=a-b
    elif c==12:
     a=a*b
    elif c==13:
     if b==0:
      raise ZeroDivisionError('Divis\xe3o por zero')
     a=a/b
    else:
     a=_pow(a,b)
    st.append(a)
   else:
    a=st.pop()
    if c==15:
     a=-a
    elif c==23:
     if a<0:
      err('Raiz de um n\xfamero negativo')
     a=math.sqrt(a)
    elif c==24:
     a=abs(a)
    else:
     r=a*math.pi/180 if CF['ang']==0 else a
     if c==20:
      a=math.sin(r)
     elif c==21:
      a=math.cos(r)
     else:
      if abs(math.cos(r))<1e-12:
       err('Tangente n\xe3o definida')
      a=math.tan(r)
    st.append(a)
  v=st[0]
  if not ok(v):
   err('Valor demasiado grande')
  return v
 def _pow(a,b):
  if a==0 and b<0:
   raise ZeroDivisionError('Divis\xe3o por zero')
  if a<0 and b!=int(b):
   f=frac(b,99)
   if f is not None and f[1]%2==1:
    r=(-a)**(1.0*f[0]/f[1])
    return-r if f[0]%2 else r
   err('Pot\xeancia de base negativa sem valor real')
  try:
   r=a**b
  except OverflowError:
   err('Valor demasiado grande')
  if isinstance(r,complex)or not ok(r):
   err('Valor demasiado grande')
  return r
 def gcd(a,b):
  a=abs(a)
  b=abs(b)
  while b:
   a,b=(b,a%b)
  return a
 def frac(x,maxd=1000):
  if not ok(x):
   return None
  neg=x<0
  a=-x if neg else x
  if a>1000000000.0:
   return None
  h0,h1=(0,1)
  k0,k1=(1,0)
  v=a
  for i in range(20):
   q=int(math.floor(v))
   h0,h1=(h1,q*h1+h0)
   k0,k1=(k1,q*k1+k0)
   if k1>maxd:
    return None
   if abs(a-1.0*h1/k1)<=1e-12*max(1.0,a):
    return(-h1 if neg else h1,k1)
   r=v-q
   if r<1e-12:
    return None
   v=1.0/r
  return None
 def rad(n):
  k=1
  m=n
  f=2
  while f*f<=m:
   while m%(f*f)==0:
    m//=f*f
    k*=f
   f+=1
  return(k,m)
 def fstr(n,d):
  g=gcd(n,d)or 1
  n//=g
  d//=g
  if d<0:
   n,d=(-n,-d)
  if d==1:
   return str(n)
  return str(n)+'/'+str(d)
 def rstr(k,m,d=1):
  if m==0 or k==0:
   return '0'
  if m==1:
   return fstr(k,d)
  g=gcd(k,d)or 1
  k//=g
  d//=g
  if d<0:
   k,d=(-k,-d)
  s=''if k==1 else '-'if k==-1 else str(k)
  s=s+'\u221a'+str(m)
  if d!=1:
   s=s+'/'+str(d)
  return s
 def exact(x):
  if not ok(x):
   return None
  f=frac(x)
  if f is not None:
   return fstr(f[0],f[1])
  f=frac(x*x,1000)
  if f is not None and f[0]>0:
   k,m=rad(f[0]*f[1])
   if m>1 and m<10000:
    return rstr(-k if x<0 else k,m,f[1])
  f=frac(x/math.pi,100)
  if f is not None:
   s=fstr(f[0],f[1])
   if '/'in s:
    a,b=s.split('/')
    return(''if a=='1'else '-'if a=='-1'else a)+'\u03c0/'+b
   return(''if s=='1'else '-'if s=='-1'else s)+'\u03c0'
  return None
 def rhs(x,dec=-1):
  s,ex=fmt2(x,0,dec)
  if ex:
   return '= '+s
  e=exact(x)
  if e is not None and e!=s:
   return '= '+e+' '+AP+' '+s
  return AP+' '+s
 UT=('m:L:1 km:L:1e3 hm:L:100 dam:L:10 dm:L:0.1 cm:L:0.01 mm:L:1e-3 \xb5m:L:1e-6 nm:L:1e-9 pm:L:1e-12 UA:L:1.496e11 a.l.:L:9.461e15 kg:M:1 t:M:1e3 g:M:1e-3 mg:M:1e-6 \xb5g:M:1e-9 u:M:1.66054e-27 s:t:1 ms:t:'
'1e-3 \xb5s:t:1e-6 ns:t:1e-9 min:t:60 h:t:3600 d:t:86400 ano:t:3.15576e7 m\xb3:V:1 dm\xb3:V:1e-3 L:V:1e-3 cm\xb3:V:1e-6 mL:V:1e-6 dL:V:1e-4 cL:V:1e-5 mm\xb3:V:1e-9 hL:V:0.1 m\xb2:A:1 cm\xb2:A:1e-4 mm'
'\xb2:A:1e-6 dm\xb2:A:0.01 km\xb2:A:1e6 ha:A:1e4 K:T:1:0 \xb0C:T:1:273.15 J:E:1 kJ:E:1e3 MJ:E:1e6 Wh:E:3600 kWh:E:3.6e6 eV:E:1.602176634e-19 cal:E:4.184 kcal:E:4184 W:W:1 mW:W:1e-3 kW:W:1e3 MW:W:1e6 GW'
':W:1e9 Pa:p:1 hPa:p:100 kPa:p:1e3 MPa:p:1e6 bar:p:1e5 atm:p:101325 mmHg:p:133.322 mol:n:1 mmol:n:1e-3 \xb5mol:n:1e-6 kmol:n:1e3 mol/dm\xb3:c:1e3 mol/L:c:1e3 mmol/L:c:1 mol/m\xb3:c:1 g/dm\xb3:m:1 g/L:m'
':1 mg/L:m:1e-3 kg/m\xb3:m:1 g/cm\xb3:d:1e3 g/mL:d:1e3 kg/m\xb3:d:1 kg/L:d:1e3 g/L:d:1 m/s:v:1 km/h:v:1/3.6 cm/s:v:0.01 N:F:1 kN:F:1e3 mN:F:1e-3 A:I:1 mA:I:1e-3 \xb5A:I:1e-6 kA:I:1e3 V:U:1 mV:U:1e-3 kV'
':U:1e3 \u03a9:R:1 k\u03a9:R:1e3 M\u03a9:R:1e6 m\u03a9:R:1e-3 Hz:f:1 kHz:f:1e3 MHz:f:1e6 GHz:f:1e9 THz:f:1e12 PHz:f:1e15 C:Q:1 mC:Q:1e-3 \xb5C:Q:1e-6 mAh:Q:3.6 Ah:Q:3600')
 _UD=None
 def _units():
  nonlocal _UD
  if _UD is None:
   _UD={}
   for it in UT.split(' '):
    p=it.split(':')
    if len(p)>=3:
     k=p[0]+':'+p[1]
     _UD[k]=(_fl(p[2]),_fl(p[3])if len(p)>3 else 0.0)
     if p[0]not in _UD:
      _UD[p[0]]=p[1]
  return _UD
 def ucat(u):
  r=_units().get(u)
  return r if isinstance(r,str)else ''
 def tobase(v,u,cat=''):
  d=_units()
  if not cat:
   cat=ucat(u)
  f=d.get(u+':'+cat)
  if f is None:
   err('Unidade desconhecida: '+u)
  return v*f[0]+f[1]
 def frombase(v,u,cat=''):
  d=_units()
  if not cat:
   cat=ucat(u)
  f=d.get(u+':'+cat)
  if f is None:
   err('Unidade desconhecida: '+u)
  return(v-f[1])/f[0]
 def conv(v,u1,u2,cat=''):
  if not cat:
   cat=ucat(u1)
  if cat!=ucat(u2)and(not u2+':'+cat in _units()):
   err('Unidades de grandezas diferentes: '+u1+' e '+u2)
  return frombase(tobase(v,u1,cat),u2,cat)
 def check(ans,sol,mode='r',tol=0.001):
  v=num(ans)[0]if isinstance(ans,str)else ans
  if mode[0]=='d':
   n=int(mode[1:])
   return fmt2(v,0,n,0)[0]==fmt2(sol,0,n,0)[0]
  if mode[0]=='s':
   n=int(mode[1:])
   return fsf(v,n)==fsf(sol,n)
  if sol==0:
   return abs(v)<=tol
  return abs(v-sol)<=tol*abs(sol)
 def fld(lab,u,t,k='n',o=None):
  return[lab,u.split(' ')if u else None,t,0,k,'',o]
 def pm(m,inc):
  if inc<=0:
   return fmt(m)
  k=_e10(abs(m))if m!=0 else 0
  if-3<=k<CF['sci']:
   k=0
  a=_sc(m,-k)
  b=_sc(inc,-k)
  e=_e10(b)
  i1=_sc(float(_rnd(_sc(b,-e)+0.0)),e)
  if i1<b:
   i1=_sc(float(int(math.ceil(_sc(b,-e)-1e-09))),e)
  d=max(0,-e)
  s='('+fmt2(a,0,d,0)[0]+' \xb1 '+fmt2(i1,0,d,0)[0]+')'
  return s+(' '+X+' 10'+sup(k)if k else '')
 def q(x,sf=0,u=''):
  return fmt(x,sf)+(' '+u if u else '')
 def lst(t):
  ps=[]
  for p in t.replace('\n',';').split(';'):
   p=p.strip()
   if not p:
    continue
   if ' 'in p and(not(X in p or '*'in p or 'x'in p.lower())):
    ps=ps+[x for x in p.split(' ')if x]
   else:
    ps.append(p)
  return ps
 def rdf(fs):
  out=[]
  bad=0
  for f in fs:
   f[5]=''
   try:
    k=f[4]
    if k=='o'and f[2].strip()=='':
     out.append(None)
    elif k=='n'or k=='o':
     v,sf=num(f[2])
     if f[1]and f[3]:
      v=conv(v,f[1][f[3]],f[1][0])
     out.append((v,sf))
    elif k=='u':
     v,sf=num(f[2])
     out.append((v,sf,f[3]))
    elif k=='l':
     vs=[num(x)for x in lst(f[2])]
     if not vs:
      err('Escreve os valores separados por espa\xe7os (2,5 3,1)')
     out.append(vs)
    elif k=='c':
     out.append(f[3])
    else:
     out.append(f[2].strip())
   except Exception as e:
    f[5]=str(e)
    bad=1
  return None if bad else out
 def need(c,m):
  if not c:
   err(m)
 def pos(v,nome):
  need(v>0,nome+' tem de ser positivo; escreve, por exemplo, 2,5')
  return v
 def low(s):
  return P.vis(s,0).lower()
 return _ns('P CF X AP err ok sup _sc _e10 sci fmt2 fmt eq fix fsf num comp ev gcd frac rad fstr exact rhs conv check fld pm q lst rdf need pos low',P,CF,X,AP,err,ok,sup,_sc,_e10,sci,fmt2,fmt,eq,fix,fsf,
num,comp,ev,gcd,frac,rad,fstr,exact,rhs,conv,check,fld,pm,q,lst,rdf,need,pos,low)


_F['m1_nucleo'] = _m_m1_nucleo


def _m_m1_plat():
 try:
  import ti_draw as D
 except Exception:
  D=None
 try:
  import ti_system as S
 except Exception:
  S=None
 try:
  import time as T
 except Exception:
  T=None
 try:
  import gc
 except Exception:
  gc=None
 try:
  import sys
 except Exception:
  sys=None
 E={'W':318,'H':212,'cw':7,'lh':17,'dy':13,'mx':4,'cols':44,'rows':12,'g':0,'buf':0,'sym':2,'log':[],'scr':[],'col':-1,'grid':None,'q':[],'tm':None}
 PAL=((0,0,0),(255,255,255),(0,51,153),(128,0,128),(0,96,160),(200,0,0),(0,128,0),(100,100,100),(204,224,255),(232,232,232),(255,255,255))
 def init():
  if D is not None:
   E['g']=1
   try:
    w,h=D.get_screen_dim()
    if w>100 and h>100:
     E['W']=int(w)
     E['H']=int(h)
   except Exception:
    E['log'].append('get_screen_dim falhou: usa 318x212')
   try:
    D.use_buffer()
    E['buf']=1
   except Exception:
    E['log'].append('use_buffer falhou: pode piscar')
  metrics(E['cw'],E['lh'],E['dy'])
 def metrics(cw,lh,dy):
  E['cw']=max(4,int(cw))
  E['lh']=max(8,int(lh))
  E['dy']=int(dy)
  E['cols']=(E['W']-2*E['mx'])//E['cw']
  E['rows']=E['H']//E['lh']
 def log(m):
  if len(E['log'])<12:
   E['log'].append(m)
 _AM=('\xe1 a#\xe0 a#\xe2 a#\xe3 a#\xe9 e#\xea e#\xe8 e#\xed i#\xf3 o#\xf4 o#\xf5 o#\xfa u#\xfc u#\xe7 c#\xc1 A#\xc0 A#\xc2 A#\xc3 A#\xc9 E#\xca E#\xcd I#\xd3 O#\xd4 O#\xd5 O#\xda U#\xc7 C#\xeb e#\xef i#\xce'
' I#\xdb U#\xd7 x#\xf7 /#\xb7 .#\u221a sqrt#\u03c0 pi#\u2248 ~#\u2264 <=#\u2265 >=#\u2260 !=#\u2192 ->#\u2190 <-#\u2194 <->#\u21d4 <=>#\u2208 em#\u2209 nao em#\u0394 D#\u03b4 d#\xb1 +-#\xb0 o#\xba o#'
'\xaa a#\u2212 -#\u2013 -#\u2014 -#\u2026 ...#\u201c "#\u201d "#\u2018 \'#\u2019 \'#\u2227 e#\u2228 ou#\u2016 |#\u211d R#\u221e inf#\u03bb lambda#\u03bd v#\u03c1 ro#\u03b7 eta#\u03b1 alfa#\u03b2 beta#'
'\u03b8 teta#\u03c3 sigma#\u03b5 eps#\u03bc u#\xb5 u#\u03a3 Soma#\u2220 ang#\u22a5 perp#\u2225 //#\u25b8 >#\u25c2 <#\u2713 v#\u2717 x#\u2605 *#\u2022 .#\u2032 \'#\u2033 "#\xbd 1/2#\u21cc <=>#\u2261 ==#'
'\xa0  #\u2080 0#\u2081 1#\u2082 2#\u2083 3#\u2084 4#\u2085 5#\u2086 6#\u2087 7#\u2088 8#\u2089 9#\u2223 |#\u2099 n#\u2090 a#\u2098 m#\u1d62 i#\u20d7 #\u0305 #\u2032 \'#\xab "#\xbb "#\u03a9 ohm#\u2113 '
'l#\u20ac EUR#\u2191 ^#\u2193 v#\u25cf o#\u25cb o#\u2502 |#\u2500 -#\u03b3 gama#\u2205 {}#\u221b raiz3#\u2229 inter#\u222a U#\u25b4 ^#\u25be v#\u207f ^n#\u0108 C#\u0302 #\u21a6 ->#\xf6 o#\u208a +#'
'\u208b -#\u2093 x#\u0304 ')
 _SUP='\u2070\xb9\xb2\xb3\u2074\u2075\u2076\u2077\u2078\u2079\u207b\u207a'
 _SUPP='0123456789-+'
 _AMD=None
 def _amap():
  nonlocal _AMD
  if _AMD is None:
   _AMD={}
   for p in _AM.split('#'):
    if len(p)>1:
     _AMD[p[0]]=p[2:]
  return _AMD
 def vis(s,lvl=-1):
  if lvl<0:
   lvl=E['sym']
  if lvl>=2:
   return s
  try:
   if len(s.encode())==len(s):
    return s
  except Exception:
   pass
  m=_amap()
  o=[]
  i=0
  n=len(s)
  while i<n:
   ch=s[i]
   k=_SUP.find(ch)
   if k>=0:
    j=i
    while j<n and _SUP.find(s[j])>=0:
     j+=1
    run=s[i:j]
    keep=lvl==1
    if keep:
     for c in run:
      if ord(c)>255:
       keep=False
    if keep:
     o.append(run)
    else:
     o.append('^')
     for c in run:
      o.append(_SUPP[_SUP.find(c)])
    i=j
    continue
   if ord(ch)>127 and(lvl==0 or ord(ch)>255):
    o.append(m.get(ch,'?'))
   else:
    o.append(ch)
   i+=1
  return ''.join(o)
 def _col(c):
  if c!=E['col']:
   E['col']=c
   r,g,b=PAL[c]
   D.set_color(r,g,b)
 def begin():
  if E['g']:
   E['col']=-1
   _col(1)
   D.fill_rect(0,0,E['W'],E['H'])
  else:
   E['grid']=[[' ']*E['cols']for i in range(E['rows'])]
 def show():
  if E['g']:
   if E['buf']:
    D.paint_buffer()
  else:
   g=E['grid']
   if g is None:
    return
   out=[]
   for r in g:
    out.append(''.join(r).rstrip())
   print('-'*E['cols'])
   print('\n'.join(out))
 def rect(x,y,w,h,c):
  if E['g']and w>0 and(h>0):
   _col(c)
   D.fill_rect(int(x),int(y),int(w),int(h))
 def frame(x,y,w,h,c):
  if E['g']:
   _col(c)
   D.draw_rect(int(x),int(y),int(w),int(h))
 def line(x1,y1,x2,y2,c):
  if E['g']:
   _col(c)
   D.draw_line(int(x1),int(y1),int(x2),int(y2))
 def circ(x,y,r,c,fill=0):
  if E['g']:
   _col(c)
   if fill:
    D.fill_circle(int(x),int(y),int(r))
   else:
    D.draw_circle(int(x),int(y),int(r))
 def poly(xs,ys,c,fill=0):
  if E['g']:
   _col(c)
   xs=[int(v)for v in xs]
   ys=[int(v)for v in ys]
   if fill:
    D.fill_poly(xs,ys)
   else:
    D.draw_poly(xs,ys)
 def txt(x,y,s,c=0):
  if not s:
   return
  if E['g']:
   if E['sym']<2:
    s=vis(s)
   _col(c)
   try:
    D.draw_text(int(x),int(y)+E['dy'],s)
   except Exception:
    if E['sym']>0:
     E['sym']=0
     log('draw_text falhou com simbolo: passa a letras simples')
     try:
      D.draw_text(int(x),int(y)+E['dy'],vis(s,0))
     except Exception:
      pass
  else:
   g=E['grid']
   r=int(y)//E['lh']
   cc=(int(x)-E['mx'])//E['cw']
   if g is None or r<0 or r>=len(g):
    return
   row=g[r]
   if E['sym']<2:
    s=vis(s)
   for ch in s:
    if 0<=cc<len(row):
     row[cc]=ch
    cc+=1
 def put(col,row,s,c=0):
  txt(E['mx']+col*E['cw'],row*E['lh'],s,c)
 KN={'center':'enter','\n':'enter','\r':'enter','return':'enter','ok':'enter','escape':'esc','backspace':'del','delete':'del','space':' ','\u2212':'-','pi':'\u03c0','\xd7':'*','\xf7':'/','clr':'clear',
'sqrt':'\u221a','sqrt(':'\u221a','ctrl':'ctrl','shift':'shift','tab':'tab','exp':'e','ee':'e','square':'^2','x^2':'^2','\xb2':'^2'}
 TXT_KEYS=('enter','esc','up','down','left','right','del','clear','tab','shift','home','menu','ctrl','ans','var')
 def raw_key(wait=1):
  if E['g']and S is not None:
   if wait:
    return S.get_key(1)
   return S.get_key()
  q=E['q']
  while not q:
   try:
    ln=input('tecla> ')
   except EOFError:
    raise KeyboardInterrupt
   for t in ln.split(' '):
    if t=='':
     continue
    if t in TXT_KEYS or t.lower()in KN:
     q.append(t)
    else:
     for ch in t:
      q.append(ch)
   if ln=='':
    q.append('enter')
  return q.pop(0)
 def norm(k):
  if not k:
   return ''
  if len(k)>1:
   k2=k.lower()
   return KN.get(k2,k2)
  return KN.get(k,k)
 def key(wait=1):
  return norm(raw_key(wait))
 def ms():
  if not E['tm']:
   try:
    v=int(S.get_time_ms())
    E['tm']=0
    return v
   except Exception:
    E['tm']=1
  if E['tm']==1:
   try:
    return int(T.ticks_ms())
   except Exception:
    E['tm']=2
  try:
   return int(T.time()*1000)
  except Exception:
   return 0
 def today():
  try:
   t=T.localtime()
   if t[0]>=2020 and 1<=t[1]<=12:
    return(t[0],t[1],t[2])
  except Exception:
   pass
  return None
 def free():
  try:
   gc.collect()
   return gc.mem_free()
  except Exception:
   return-1
 def collect():
  try:
   gc.collect()
  except Exception:
   pass
 def has_mods():
  return True
 def unload(n):
  _L.pop(n,None)
  return True
 def mod_file(m):
  return ''
 def save(n,lst):
  try:
   S.store_list(n,lst)
   return True
  except Exception:
   return False
 def load(n):
  try:
   r=S.recall_list(n)
   if r is None:
    return None
   return[v for v in r]
  except Exception:
   return None
 def platform():
  try:
   return str(S.get_platform())
  except Exception:
   if D is None:
    return 'texto'
   return '?'
 return _ns('D S T sys E init metrics log vis begin show rect frame line circ poly txt put raw_key norm key ms today free collect has_mods unload mod_file save load platform',D,S,T,sys,E,init,metrics,
log,vis,begin,show,rect,frame,line,circ,poly,txt,put,raw_key,norm,key,ms,today,free,collect,has_mods,unload,mod_file,save,load,platform)


_F['m1_plat'] = _m_m1_plat


def _m_m1_q():
 N=_imp('m1_nucleo')
 Z=(0,1)
 UM=(1,1)
 MAXLEN=200
 MAXPAR=20
 def mdc(a,b):
  a,b=(abs(a),abs(b))
  while b:
   a,b=(b,a%b)
  return a
 def mmc(a,b):
  return abs(a*b)//mdc(a,b)if a and b else 0
 def R(n,d=1):
  if d==0:
   N.err('Divis\xe3o por zero')
  if d<0:
   n,d=(-n,-d)
  g=mdc(n,d)or 1
  n,d=(n//g,d//g)
  if abs(n)>10**40 or d>10**40:
   N.err('N\xfamero demasiado grande')
  return(n,d)
 def add(a,b):
  return R(a[0]*b[1]+b[0]*a[1],a[1]*b[1])
 def sub(a,b):
  return R(a[0]*b[1]-b[0]*a[1],a[1]*b[1])
 def mul(a,b):
  return R(a[0]*b[0],a[1]*b[1])
 def div(a,b):
  if b[0]==0:
   N.err('Divis\xe3o por zero')
  return R(a[0]*b[1],a[1]*b[0])
 def neg(a):
  return(-a[0],a[1])
 def cmp(a,b):
  x=a[0]*b[1]-b[0]*a[1]
  return(x>0)-(x<0)
 def pw(a,k):
  if k<0:
   if a[0]==0:
    N.err('0 n\xe3o tem pot\xeancias de expoente negativo')
   a,k=(R(a[1],a[0]),-k)
  N.need(k<=60,'Expoente demasiado grande')
  return R(a[0]**k,a[1]**k)
 def qf(a):
  return a[0]/a[1]
 def qs(a):
  return str(a[0])if a[1]==1 else str(a[0])+'/'+str(a[1])
 def qp(a):
  s=qs(a)
  return '('+s+')'if a[0]<0 else s
 def numq(t):
  t=t.replace(',','.')
  e=0
  k=t.find('e')
  if k>=0:
   e=int(t[k+1:])
   t=t[:k]
  if t.count('.')>1 or t in('','.'):
   N.err('N\xfamero mal escrito: '+t)
  if '.'in t:
   a,b=t.split('.')
   r=R(int(a or '0')*10**len(b)+int(b or '0'),10**len(b))
  else:
   r=R(int(t),1)
  N.need(abs(e)<=30,'Expoente demasiado grande')
  return mul(r,pw((10,1),e))if e else r
 def fatores(n):
  n=abs(n)
  out=[]
  p=2
  while p*p<=n:
   e=0
   while n%p==0:
    n//=p
    e+=1
   if e:
    out.append((p,e))
   p+=1 if p==2 else 2
   N.need(p<2000000,'N\xfamero demasiado grande para decompor')
  if n>1:
   out.append((n,1))
  return out
 def fstr(fs):
  if not fs:
   return '1'
  return ' \xd7 '.join([str(p)+(N.sup(e)if e>1 else '')for p,e in fs])
 def dizima(a,maxp=60):
  n,d=a
  s='-'if n<0 else ''
  n=abs(n)
  s+=str(n//d)
  r=n%d
  if r==0:
   return s
  ds=[]
  vistos={}
  while r and r not in vistos and(len(ds)<maxp):
   vistos[r]=len(ds)
   r*=10
   ds.append(str(r//d))
   r%=d
  if r==0:
   return s+','+''.join(ds)
  if r in vistos:
   i=vistos[r]
   return s+','+''.join(ds[:i])+'('+''.join(ds[i:])+')'
  return s+','+''.join(ds)+'...'
 TROCA={'\u2212':'-','\u2013':'-','\xd7':'*','\xb7':'*','\xf7':':','[':'(','{':'(',']':')','}':')','\u221a':'r'}
 FUN={'sqrt':'r','raiz':'r'}
 def dig(c):
  return '0'<=c<='9'
 def toks(s):
  N.need(s.strip(),'Escreve uma express\xe3o')
  N.need(len(s)<=MAXLEN,'Express\xe3o demasiado longa (m\xe1ximo '+str(MAXLEN)+' carateres)')
  out=[]
  i=0
  while i<len(s):
   c=TROCA.get(s[i],s[i])
   if c==' ':
    i+=1
   elif dig(c)or(c in '.,'and i+1<len(s)and dig(s[i+1])):
    j=i
    while j<len(s)and(dig(s[j])or s[j]in '.,'):
     j+=1
    if j<len(s)and s[j]in 'eE'and(j+1<len(s))and(dig(s[j+1])or(s[j+1]in '+-'and j+2<len(s)and dig(s[j+2]))):
     j+=2
     while j<len(s)and dig(s[j]):
      j+=1
    t=s[i:j].lower()
    if t[-1]in '.,':
     N.err('N\xfamero mal escrito: '+s[i:j])
    out.append(('n',numq(t),i))
    i=j
   elif c in '\xb2\xb3':
    out.append(('o','^',i))
    out.append(('n',(2 if c=='\xb2'else 3,1),i))
    i+=1
   elif c=='r'and s[i]=='\u221a':
    out.append(('f','r',i))
    i+=1
   elif 'a'<=c.lower()<='z':
    j=i
    while j<len(s)and 'a'<=s[j].lower()<='z':
     j+=1
    w=s[i:j]
    if w.lower()in FUN:
     out.append(('f',FUN[w.lower()],i))
    else:
     for k in range(len(w)):
      out.append(('v',w[k],i+k))
    i=j
   elif c in '+-*/:^':
    out.append(('o',c,i))
    i+=1
   elif c in '()':
    out.append((c,c,i))
    i+=1
   else:
    N.err('S\xedmbolo desconhecido: '+s[i])
  return out
 class P:
  def __init__(self,s):
   self.s=s
   self.t=toks(s)
   self.i=0
   self.prof=0
  def ver(self):
   return self.t[self.i]if self.i<len(self.t)else(None,None,len(self.s))
  def tira(self):
   x=self.ver()
   self.i+=1
   return x
  def tudo(self):
   e=self.expr()
   if self.i<len(self.t):
    k=self.ver()
    N.err('N\xe3o percebo "'+self.s[k[2]:k[2]+8].strip()+'" (falta um sinal?)')
   return e
  def termos(self):
   out=[]
   sg=1
   k=self.ver()
   if k[0]=='o'and k[1]in '+-':
    self.tira()
    sg=-1 if k[1]=='-'else 1
   while True:
    a=self.ver()[2]
    t=self.termo()
    b=self.ver()[2]
    out.append((sg,t,self.s[a:b].strip()))
    k=self.ver()
    if k[0]=='o'and k[1]in '+-':
     self.tira()
     sg=-1 if k[1]=='-'else 1
    else:
     break
   if self.i<len(self.t):
    self.tudo()
   return out
  def expr(self):
   self.prof+=1
   N.need(self.prof<=MAXPAR,'Demasiados par\xeanteses')
   e=self.termo()
   while True:
    k=self.ver()
    if k[0]=='o'and k[1]in '+-':
     self.tira()
     e=(k[1],e,self.termo())
    else:
     break
   self.prof-=1
   return e
  def termo(self):
   e=self.unario()
   while True:
    k=self.ver()
    if k[0]=='o'and k[1]in '*/:':
     self.tira()
     d=self.unario()
     if k[1]=='/'and lit(e)and lit(d)and(d[0]=='n')and d[1][0]:
      n=e[1][0]if e[0]=='n'else-e[1][1][0]
      e=('n',R(n,d[1][0]))
      continue
     k2=self.ver()
     if k[1]!='/'and lit(d)and(k2[0]=='o')and(k2[1]=='/')and(self.i+1<len(self.t))and(self.t[self.i+1][0]=='n')and(self.t[self.i+1][1][1]==1)and self.t[self.i+1][1][0]:
      self.tira()
      q=self.tira()[1][0]
      n=d[1][0]if d[0]=='n'else-d[1][1][0]
      d=('n',R(n,q))
     e=('*'if k[1]=='*'else '/',e,d)
    elif k[0]in('n','v','(','f'):
     if k[0]=='n'and e[0]=='n':
      N.err('Falta um sinal entre dois n\xfameros')
     e=('*',e,self.unario())
    else:
     break
   return e
  def unario(self):
   k=self.ver()
   if k[0]=='o'and k[1]in '+-':
    self.tira()
    u=self.unario()
    return('u',u)if k[1]=='-'else u
   return self.pot()
  def pot(self):
   b=self.atomo()
   k=self.ver()
   if k[0]=='o'and k[1]=='^':
    self.tira()
    return('^',b,self.unario())
   return b
  def atomo(self):
   k=self.tira()
   if k[0]=='n':
    return('n',k[1])
   if k[0]=='v':
    return('v',k[1])
   if k[0]=='f':
    return(k[1],self.unario())
   if k[0]=='(':
    e=self.expr()
    f=self.tira()
    N.need(f[0]==')','Falta fechar um par\xeantese')
    return e
   if k[0]is None:
    N.err('A express\xe3o acaba antes do tempo')
   N.err('N\xe3o percebo "'+self.s[k[2]:k[2]+6].strip()+'"')
 def lit(e):
  if e[0]=='u':
   e=e[1]
  return e[0]=='n'and e[1][1]==1
 def arvore(s):
  return P(s).tudo()
 def letras(t,out=None):
  out=[]if out is None else out
  if t[0]=='v':
   if t[1]not in out:
    out.append(t[1])
  elif t[0]!='n':
   for x in t[1:]:
    if isinstance(x,tuple):
     letras(x,out)
  return out
 def mono(a,b):
  d={}
  for v,e in a+b:
   d[v]=d.get(v,0)+e
  return tuple(sorted([(v,d[v])for v in d if d[v]]))
 def padd(A,B,s=1):
  C=dict(A)
  for m in B:
   c=add(C.get(m,Z),B[m])if s>0 else sub(C.get(m,Z),B[m])
   if c[0]:
    C[m]=c
   elif m in C:
    del C[m]
  return C
 def pmul(A,B):
  C={}
  for a in A:
   for b in B:
    m=mono(a,b)
    c=add(C.get(m,Z),mul(A[a],B[b]))
    if c[0]:
     C[m]=c
    elif m in C:
     del C[m]
  return C
 def pesc(A,k):
  return dict([(m,mul(A[m],k))for m in A])if k[0]else{}
 def cte(A):
  for m in A:
   if m:
    return None
  return A.get((),Z)
 def grau(A,v=None):
  g=-1
  for m in A:
   g=max(g,sum([e for x,e in m if v is None or x==v]))
  return g
 def poli(t):
  k=t[0]
  if k=='n':
   return{():t[1]}if t[1][0]else{}
  if k=='v':
   return{((t[1],1),):UM}
  if k=='u':
   return pesc(poli(t[1]),(-1,1))
  if k=='+':
   return padd(poli(t[1]),poli(t[2]))
  if k=='-':
   return padd(poli(t[1]),poli(t[2]),-1)
  if k=='*':
   return pmul(poli(t[1]),poli(t[2]))
  if k=='/':
   d=cte(poli(t[2]))
   N.need(d is not None,'Divis\xe3o por uma express\xe3o com letras: n\xe3o \xe9 um polin\xf3mio')
   return pesc(poli(t[1]),div(UM,d))
  if k=='^':
   e=cte(poli(t[2]))
   N.need(e is not None and e[1]==1,'O expoente tem de ser um n\xfamero inteiro')
   e=e[0]
   b=poli(t[1])
   c=cte(b)
   if c is not None:
    return{():pw(c,e)}if pw(c,e)[0]else{}
   N.need(0<=e<=12,'Expoente demasiado grande ou negativo')
   r={():UM}
   for i in range(e):
    r=pmul(r,b)
   return r
  N.err('Ra\xedzes n\xe3o s\xe3o permitidas aqui')
 def ordem(A,vs=None):
  vs=vs or sorted(set([x for m in A for x,e in m]))
  def chave(m):
   d=dict(m)
   return[-sum([e for x,e in m])]+[-d.get(v,0)for v in vs]
  ms=list(A.keys())
  ms.sort(key=chave)
  return ms
 def mstr(m):
  return ''.join([v+(N.sup(e)if e>1 else '')for v,e in m])
 def pstr(A,vs=None):
  if not A:
   return '0'
  o=''
  for m in ordem(A,vs):
   c=A[m]
   a=(abs(c[0]),c[1])
   if m:
    t=(''if a==UM else '('+qs(a)+')'if a[1]>1 else qs(a))+mstr(m)
   else:
    t=qs(a)
   if not o:
    o=('-'if c[0]<0 else '')+t
   else:
    o+=(' - 'if c[0]<0 else ' + ')+t
  return o
 def coefs(A,v):
  g=grau(A)
  cs=[Z]*(g+1)
  for m in A:
   N.need(not m or(len(m)==1 and m[0][0]==v),'O polin\xf3mio s\xf3 pode ter a letra '+v)
   cs[m[0][1]if m else 0]=A[m]
  return cs
 def decoefs(cs,v):
  A={}
  for i in range(len(cs)):
   if cs[i][0]:
    A[((v,i),)if i else()]=cs[i]
  return A
 def valor(A,d):
  r=Z
  for m in A:
   t=A[m]
   for v,e in m:
    N.need(v in d,'Falta o valor de '+v)
    t=mul(t,pw(d[v],e))
   r=add(r,t)
  return r
 def denl(A):
  k=1
  for m in A:
   k=mmc(k,A[m][1])
  return k
 def raizes_rac(cs):
  while cs and cs[0][0]==0:
   cs=cs[1:]
  if len(cs)<2:
   return[]
  a0,an=(abs(cs[0][0]),abs(cs[-1][0]))
  N.need(a0<=10**9 and an<=10**9,'Coeficientes demasiado grandes')
  out=[]
  ps=[p for p in range(1,int(a0**0.5)+2)if a0%p==0]
  ps=ps+[a0//p for p in ps]
  qs_=[q for q in range(1,int(an**0.5)+2)if an%q==0]
  qs_=qs_+[an//q for q in qs_]
  vistos=[]
  for p in ps:
   for q in qs_:
    for s in(1,-1):
     r=R(s*p,q)
     if r in vistos:
      continue
     vistos.append(r)
     if valor(decoefs(cs,'x'),{'x':r})[0]==0:
      out.append(r)
  out.sort(key=lambda r:r[0]/r[1])
  return out
 def vstr(q):
  d=q[1]
  while d%2==0:
   d//=2
  while d%5==0:
   d//=5
  return dizima(q)if d==1 else qs(q)
 def istr(I):
  if I is None:
   return '\u2205'
  lo,lc,hi,hc=I
  if lo is not None and hi is not None and(cmp(lo,hi)==0):
   return '{'+vstr(lo)+'}'
  return('['if lc else ']')+('-\u221e'if lo is None else vstr(lo))+sepr(lo,hi)+('+\u221e'if hi is None else vstr(hi))+(']'if hc else '[')
 def sepr(lo,hi):
  for x in(lo,hi):
   if x is not None and ','in vstr(x):
    return '; '
  return ', '
 def cond(I):
  if I is None:
   return 'condi\xe7\xe3o imposs\xedvel'
  lo,lc,hi,hc=I
  p=[]
  if lo is not None:
   p.append(vstr(lo)+(' \u2264 'if lc else ' < '))
  p.append('x')
  if hi is not None:
   p.append((' \u2264 'if hc else ' < ')+vstr(hi))
  if lo is None and hi is None:
   return 'x \u2208 \u211d'
  if lo is not None and hi is not None and(cmp(lo,hi)==0):
   return 'x = '+vstr(lo)
  return ''.join(p)
 def inter(A,B):
  lo,lc=(A[0],A[1])
  if B[0]is not None and(lo is None or cmp(B[0],lo)>0):
   lo,lc=(B[0],B[1])
  elif B[0]is not None and lo is not None and(cmp(B[0],lo)==0):
   lc=lc and B[1]
  hi,hc=(A[2],A[3])
  if B[2]is not None and(hi is None or cmp(B[2],hi)<0):
   hi,hc=(B[2],B[3])
  elif B[2]is not None and hi is not None and(cmp(B[2],hi)==0):
   hc=hc and B[3]
  if lo is not None and hi is not None:
   c=cmp(lo,hi)
   if c>0 or(c==0 and(not(lc and hc))):
    return None
  return(lo,lc,hi,hc)
 def antes(A,B):
  if A[0]is None:
   return True
  if B[0]is None:
   return False
  c=cmp(A[0],B[0])
  return c<0 or(c==0 and A[1])
 def uniao(A,B):
  if not antes(A,B):
   A,B=(B,A)
  if A[2]is not None and B[0]is not None:
   c=cmp(B[0],A[2])
   if c>0 or(c==0 and(not(A[3]or B[1]))):
    return[A,B]
  if A[2]is None:
   return[A]
  if B[2]is None:
   return[(A[0],A[1],None,False)]
  c=cmp(B[2],A[2])
  if c>0:
   return[(A[0],A[1],B[2],B[3])]
  if c==0:
   return[(A[0],A[1],A[2],A[3]or B[3])]
  return[A]
 return _ns('N Z UM mdc mmc R add sub mul div neg cmp pw qf qs qp fatores fstr dizima P arvore letras padd pmul pesc cte grau poli ordem mstr pstr coefs decoefs valor denl raizes_rac vstr istr sepr cond inter antes uniao',
N,Z,UM,mdc,mmc,R,add,sub,mul,div,neg,cmp,pw,qf,qs,qp,fatores,fstr,dizima,P,arvore,letras,padd,pmul,pesc,cte,grau,poli,ordem,mstr,pstr,coefs,decoefs,valor,denl,raizes_rac,vstr,istr,sepr,cond,inter,antes,
uniao)


_F['m1_q'] = _m_m1_q


def _m_m1_ui():
 P=_imp('m1_plat')
 N=_imp('m1_nucleo')
 E=P.E
 MK={'= ':3,'> ':4,'! ':5,'+ ':6,'# ':2}
 OPS=('=','+','-','\u2212','\xd7','/','\xf7','\xb7','\u2248','<','>','\u2264','\u2265','\u21d4','\u2192')
 OKS='\u2713 '
 ERS='\u2717 '
 _WC=[None,None]
 _H=['']
 def cols():
  return E['cols']
 def body():
  return E['rows']-2
 def clip(s,n):
  if len(s)<=n:
   return s
  return s[:max(0,n-1)]+'\u2026'
 def title(t,right=''):
  P.rect(0,0,E['W'],E['lh'],2)
  w=cols()-len(right)-1
  P.put(0,0,clip(t,w),10)
  if right:
   P.put(cols()-len(right),0,right,10)
 def foot(t):
  if _H[0]:
   t=_H[0]
   _H[0]=''
  y=(E['rows']-1)*E['lh']
  P.rect(0,y,E['W'],E['H']-y,9)
  P.put(0,E['rows']-1,clip(t,cols()),7)
 def wrap(s,w=0,key=None):
  if w<=0:
   w=cols()
  if key is not None and _WC[0]==(key,w):
   return _WC[1]
  out=[]
  for para in s.split('\n'):
   st=MK.get(para[:2],0)
   if st:
    para=para[2:]
   ind='  'if para[:2]in('- ','  ')else ''
   cur=[]
   pre=''
   for wd in para.split(' '):
    while cur and len(pre)+len(' '.join(cur))+1+len(wd)>w:
     k=len(cur)
     if st==3:
      j=k-1
      while j>0 and cur[j]not in OPS:
       j-=1
      if j>0:
       k=j
     out.append((st,pre+' '.join(cur[:k])))
     cur=cur[k:]
     pre=ind
    cur.append(wd)
    t=pre+' '.join(cur)
    if len(t)>w:
     while len(t)>w:
      out.append((st,t[:w]))
      t=ind+t[w:]
     pre=ind
     cur=[t[len(ind):]]
   out.append((st,pre+' '.join(cur)))
  if key is not None:
   _WC[0]=(key,w)
   _WC[1]=out
  return out
 def lines(lst,top=0,row=1,n=0):
  if n<=0:
   n=body()
  for i in range(n):
   k=top+i
   if k>=len(lst):
    break
   st,t=lst[k]
   P.put(0,row+i,t,st)
 def bar(top,n,total,row=1):
  if total<=n or not E['g']:
   return
  x=E['W']-4
  y0=row*E['lh']
  h=n*E['lh']
  P.rect(x,y0,3,h,9)
  th=max(6,h*n//total)
  ty=y0+(h-th)*top//max(1,total-n)
  P.rect(x,ty,3,th,7)
 def hint(t):
  _H[0]=t
 def menu(t,items,sel=0,ft='',right=''):
  n=len(items)
  h=body()
  top=0
  pend=-1
  if not ft:
   ft='n\xfamero ou enter: abrir \xb7 esc: voltar'
  while True:
   if sel<top:
    top=sel
   if sel>=top+h:
    top=sel-h+1
   P.begin()
   title(t,right)
   w=cols()-4
   for i in range(min(h,n-top)):
    k=top+i
    y=(1+i)*E['lh']
    lab=str(k+1)
    if len(lab)<2:
     lab=' '+lab
    if k==sel:
     P.rect(0,y,E['W']-5,E['lh'],8)
     if not E['g']:
      lab='>'+lab[1:]
    P.put(0,1+i,lab,2)
    P.put(3,1+i,clip(items[k],w),0)
   bar(top,h,n)
   foot(ft if pend<0 else str(pend)+'_ \xb7 enter: op\xe7\xe3o '+str(pend))
   P.show()
   k=P.key()
   if k=='up':
    sel=(sel-1)%n
    pend=-1
   elif k=='down':
    sel=(sel+1)%n
    pend=-1
   elif k=='enter':
    return sel
   elif k=='esc':
    return-1
   elif k=='left':
    sel=max(0,sel-h)
   elif k=='right':
    sel=min(n-1,sel+h)
   elif len(k)==1 and '0'<=k<='9':
    d=ord(k)-48
    if pend>=0:
     v=pend*10+d
     pend=-1
     if 1<=v<=n:
      return v-1
     continue
    if d==0:
     return-1
    if d*10<=n:
     pend=d
     sel=d-1
     continue
    if d<=n:
     return d-1
   elif k:
    hint('Tecla sem fun\xe7\xe3o: usa os n\xfameros e as setas')
 def pager(t,ls,top=0,ft='',right='',keys=()):
  h=body()
  n=len(ls)
  while True:
   top=max(0,min(top,max(0,n-h)))
   P.begin()
   title(t,right)
   lines(ls,top)
   bar(top,h,n)
   a=top+1
   b=min(n,top+h)
   f=str(a)+'-'+str(b)+' de '+str(n)
   if b<n:
    f=f+' \xb7 enter: mais'
   if ft:
    f=ft+' \xb7 '+f+' \xb7 esc'
   else:
    f=f+' \xb7 esc: voltar'
   foot(f)
   P.show()
   k=P.key()
   if k in keys:
    return(k,top)
   if k=='down':
    top+=1
   elif k=='up':
    top-=1
   elif k=='right':
    top+=h
   elif k=='left':
    top-=h
   elif k=='enter':
    if top+h<n:
     top+=h
    else:
     return(k,top)
   elif k=='esc':
    return(k,top)
   elif k:
    hint('Tecla sem fun\xe7\xe3o: setas para ler, esc para voltar')
 def text(t,s,ft='',right='',keys=()):
  return pager(t,wrap(s),0,ft,right,keys)[0]
 def msg(t,s,st=0):
  ls=wrap(s)
  if st:
   ls=[(st,x[1])for x in ls]
  P.begin()
  title(t)
  lines(ls)
  foot('qualquer tecla: continuar')
  P.show()
  return P.key()
 def busy(s='A calcular\u2026'):
  y=E['rows']//2*E['lh']
  P.rect(20,y-4,E['W']-40,E['lh']+8,8)
  P.put(4,E['rows']//2,s,2)
  P.show()
 def ask(t,q,yes=0):
  r=menu(t,['Sim','N\xe3o'],0 if yes else 1,'1: sim \xb7 2: n\xe3o \xb7 esc: n\xe3o','')
  return r==0
 PAGS='ABCDEFGHIJ'
 PNOME=('O que vais aprender','Intui\xe7\xe3o','Defini\xe7\xe3o formal','Explica\xe7\xe3o detalhada','F\xf3rmulas','Exemplo resolvido','Interpreta\xe7\xe3o','Erros frequentes','Resumo','Exerc\xedcio de verifica\xe7\xe3o')
 def lesson(t,pages,pg=0,top=0,ans='',lid='',extra=()):
  avail=[i for i in range(len(pages))if pages[i]]
  if not avail:
   return('esc',pg,0)
  if pg not in avail:
   pg=avail[0]
  while True:
   ls=wrap('# '+PAGS[pg]+'. '+PNOME[pg])+wrap(pages[pg],0,(lid,pg))
   fx='\u25c2\u25b8 p\xe1gina'
   if pg==9 and ans:
    fx='r: resposta \xb7 '+fx
   i=avail.index(pg)
   k,top=pager(t,ls,top,fx,PAGS[pg]+' '+str(i+1)+'/'+str(len(avail)),('left','right','r')+extra)
   if k=='esc'or k in extra:
    return(k,pg,top)
   if k=='r':
    if pg==9 and ans:
     text('Resposta',ans)
    continue
   if k=='right'or k=='enter':
    if i+1<len(avail):
     pg=avail[i+1]
     top=0
    elif k=='enter':
     if pg==9 and ans:
      text('Resposta',ans)
     return('fim',pg,0)
   elif k=='left'and i>0:
    pg=avail[i-1]
    top=0
 def _ins(k,sh,caps):
  if k in('^2','\xb2'):
   return '^2'
  if k in('\u221a','\u03c0'):
   return k
  if k in('sin','cos','tan','sin(','cos(','tan('):
   return k.rstrip('(')+'('
  if k=='ans':
   return 'ans'
  if len(k)==1 and(k>=' 'or k=='\t'):
   if 'a'<=k<='z'and(sh or caps):
    return k.upper()
   return k
  return None
 def _box(row,s,cur,w,foc):
  off=0
  if cur>w-1:
   off=cur-w+1
  vis=s[off:off+w]
  y=row*E['lh']
  x0=E['mx']+2*E['cw']
  if foc:
   P.rect(x0-2,y,w*E['cw']+4,E['lh'],8)
  P.put(2,row,vis,0)
  if foc:
   cx=x0+(cur-off)*E['cw']
   if E['g']:
    P.rect(cx,y+2,1,E['lh']-4,0)
   else:
    P.put(2+cur-off,row,'_'if cur>=len(s)else s[cur],0)
 def edit(t,lab,s='',hint_='',err=''):
  cur=len(s)
  sh=0
  caps=0
  while True:
   P.begin()
   title(t)
   r=1
   for st,x in wrap(lab):
    P.put(0,r,x,st)
    r+=1
   _box(r,s,cur,cols()-4,1)
   r+=1
   if err:
    for st,x in wrap('! '+ERS+err):
     P.put(0,r,x,5)
     r+=1
   for st,x in wrap(hint_):
    if r<body():
     P.put(0,r,x,7)
     r+=1
   m=' \xb7 MAI'if caps else ' \xb7 mai'if sh else ''
   foot('enter: ok \xb7 esc: cancelar \xb7 del: apaga'+m)
   P.show()
   k=P.key()
   if k=='enter':
    return s
   if k=='esc':
    return None
   if k=='left':
    cur=max(0,cur-1)
   elif k=='right':
    cur=min(len(s),cur+1)
   elif k=='del':
    if cur>0:
     s=s[:cur-1]+s[cur:]
     cur-=1
   elif k=='clear':
    s=''
    cur=0
   elif k=='shift':
    sh=1-sh
    continue
   elif k=='tab':
    caps=1-caps
    continue
   elif k in('up','down'):
    continue
   else:
    a=_ins(k,sh,caps)
    if a is None:
     continue
    if len(s)+len(a)>200:
     err='Texto demasiado longo (m\xe1x. 200)'
     continue
    s=s[:cur]+a+s[cur:]
    cur+=len(a)
    err=''
   sh=0
 def form(t,fs,foc=0,ft=''):
  stops=[]
  for i in range(len(fs)):
   stops.append((i,0))
   if fs[i][1]and len(fs[i][1])>1 and(fs[i][4]!='c'):
    stops.append((i,1))
  si=0
  for j in range(len(stops)):
   if stops[j]==(foc,0):
    si=j
  cur=len(fs[stops[si][0]][2])
  sh=0
  caps=0
  top=0
  w=cols()-4
  while True:
   fi,part=stops[si]
   f=fs[fi]
   rows_=[]
   for i in range(len(fs)):
    g=fs[i]
    u=g[1][g[3]]if g[1]and g[4]!='c'else ''
    lab=clip(g[0],cols()-1)
    if u:
     us=' \u25c2'+u+'\u25b8'if len(g[1])>1 else ' '+u
     lab=clip(lab,cols()-len(us)-1)+us
    rows_.append((i,'L',lab))
    rows_.append((i,'V',g[2]))
    if g[5]:
     for st,x in wrap(ERS+g[5],cols()-2):
      rows_.append((i,'E',x))
   h=body()
   fr=0
   for j in range(len(rows_)):
    if rows_[j][0]==fi and rows_[j][1]=='V':
     fr=j
   if fr<top+1:
    top=max(0,fr-1)
   if fr>=top+h:
    top=fr-h+1
   P.begin()
   title(t,str(fi+1)+'/'+str(len(fs)))
   for r in range(h):
    j=top+r
    if j>=len(rows_):
     break
    i,kind,s=rows_[j]
    g=fs[i]
    row=1+r
    if kind=='L':
     if i==fi and part==1:
      P.rect(0,row*E['lh'],E['W'],E['lh'],8)
     P.put(0,row,s,2 if i==fi else 0)
    elif kind=='V':
     if g[4]=='c':
      s='\u25c2 '+g[6][g[3]]+' \u25b8'
      if i==fi:
       P.rect(E['mx']+2*E['cw']-2,row*E['lh'],len(s)*E['cw']+4,E['lh'],8)
      P.put(2,row,s,0)
     else:
      _box(row,s,cur if i==fi else len(s),w,i==fi and part==0)
    else:
     P.put(1,row,s,5)
   bar(top,h,len(rows_))
   if part==1:
    fx='\u25c2\u25b8 unidade'
   elif f[4]=='c':
    fx='\u25c2\u25b8 op\xe7\xe3o'
   else:
    fx='\u25c2\u25b8 cursor'
   fx=fx+(' \xb7 enter: calcular'if fi==len(fs)-1 else ' \xb7 enter: seguinte')
   if caps:
    fx=fx+' \xb7 MAI'
   foot((ft+' \xb7 'if ft else '')+fx+' \xb7 esc')
   P.show()
   k=P.key()
   if k=='esc':
    return False
   if k=='enter':
    if fi==len(fs)-1:
     return True
    si=stops.index((fi+1,0))
    cur=len(fs[fi+1][2])
    continue
   if k=='up'or k=='down':
    si=(si+(1 if k=='down'else-1))%len(stops)
    cur=len(fs[stops[si][0]][2])
    continue
   if f[4]=='c'or part==1:
    if k in('left','right'):
     opts=f[6]if f[4]=='c'else f[1]
     f[3]=(f[3]+(1 if k=='right'else-1))%len(opts)
     continue
    if f[4]=='c':
     continue
    si=stops.index((fi,0))
    part=0
    cur=len(f[2])
   s=f[2]
   if k=='left':
    cur=max(0,cur-1)
   elif k=='right':
    cur=min(len(s),cur+1)
   elif k=='del':
    if cur>0:
     f[2]=s[:cur-1]+s[cur:]
     cur-=1
   elif k=='clear':
    f[2]=''
    cur=0
   elif k=='shift':
    sh=1-sh
    continue
   elif k=='tab':
    caps=1-caps
    continue
   else:
    a=_ins(k,sh,caps)
    if a is not None and len(s)+len(a)<=200:
     f[2]=s[:cur]+a+s[cur:]
     cur+=len(a)
     f[5]=''
   sh=0
 def nice(a,b,n=5):
  d=(b-a)/max(1,n)
  if d<=0:
   return 1.0
  e=N._e10(d)
  m=d/N._sc(1.0,e)
  for c in(1,2,5,10):
   if m<=c:
    return c*N._sc(1.0,e)
  return 10*N._sc(1.0,e)
 def cseg(x1,y1,x2,y2,L,T,R,B):
  t0=0.0
  t1=1.0
  dx=x2-x1
  dy=y2-y1
  for p,q in((-dx,x1-L),(dx,R-x1),(-dy,y1-T),(dy,B-y1)):
   if p==0:
    if q<0:
     return None
   else:
    r=q/p
    if p<0:
     if r>t1:
      return None
     t0=max(t0,r)
    else:
     if r<t0:
      return None
     t1=min(t1,r)
  return(x1+t0*dx,y1+t0*dy,x1+t1*dx,y1+t1*dy)
 def graph(t,items,x0,x1,y0,y1,leg=''):
  if not E['g']:
   out=[]
   for it in items:
    if it[0]=='f':
     for i in range(5):
      x=x0+(x1-x0)*i/4
      try:
       out.append('x = '+N.fmt(x)+' \u2192 y = '+N.fmt(it[1](x)))
      except Exception:
       out.append('x = '+N.fmt(x)+' \u2192 sem valor')
    elif it[0]=='p':
     for p in it[1][:10]:
      out.append('('+N.fmt(p[0])+'; '+N.fmt(p[1])+')')
    elif it[0]=='t':
     for p in it[1]:
      out.append(p[2]+' = ('+N.fmt(p[0])+'; '+N.fmt(p[1])+')')
   text(t,'(Gr\xe1fico s\xf3 no ecr\xe3 gr\xe1fico.)\n'+'\n'.join(out)+('\n'+leg if leg else ''))
   return
  while True:
   busy()
   P.begin()
   title(t)
   L=30
   R=E['W']-6
   T=E['lh']+4
   B=(E['rows']-2)*E['lh']-2
   if leg:
    B-=E['lh']
   sx=(R-L)/(x1-x0)
   sy=(B-T)/(y1-y0)
   def px(x):
    return L+(x-x0)*sx
   def py(y):
    return B-(y-y0)*sy
   P.frame(L,T,R-L,B-T,9)
   st=nice(x0,x1)
   v=st*int(x0/st)
   while v<=x1:
    if v>=x0:
     X=px(v)
     P.line(X,B,X,B+3,7)
    v+=st
   st2=nice(y0,y1)
   v=st2*int(y0/st2)
   while v<=y1:
    if v>=y0:
     Y=py(v)
     P.line(L-3,Y,L,Y,7)
    v+=st2
   if x0<=0<=x1:
    P.line(px(0),T,px(0),B,7)
   if y0<=0<=y1:
    P.line(L,py(0),R,py(0),7)
   P.put(0,1,N.fmt(y1,2),7)
   P.put(0,E['rows']-3-(1 if leg else 0),N.fmt(y0,2),7)
   P.txt(L,B+2,N.fmt(x0,2),7)
   s=N.fmt(x1,2)
   P.txt(R-len(s)*E['cw'],B+2,s,7)
   for it in items:
    c=it[2]
    if it[0]=='f':
     f=it[1]
     last=None
     for X in range(int(L),int(R)+1,2):
      x=x0+(X-L)/sx
      try:
       y=f(x)
       Y=py(y)
       if Y<T-2 or Y>B+2:
        Y=None
      except Exception:
       Y=None
      if Y is not None and last is not None:
       P.line(X-2,last,X,Y,c)
      last=Y
    elif it[0]=='p':
     for p in it[1]:
      X=px(p[0])
      Y=py(p[1])
      if L<=X<=R and T<=Y<=B:
       P.rect(X-2,Y-2,5,5,c)
    elif it[0]=='s':
     for q in it[1]:
      s=cseg(px(q[0]),py(q[1]),px(q[2]),py(q[3]),L,T,R,B)
      if s:
       P.line(s[0],s[1],s[2],s[3],c)
    elif it[0]=='t':
     for q in it[1]:
      X=px(q[0])
      Y=py(q[1])
      if L<=X<=R and T<=Y<=B:
       P.txt(X+3,Y-E['lh']+3,q[2],c)
   if leg:
    P.put(0,E['rows']-2,clip(leg,cols()),0)
   foot('setas: mover \xb7 + -: escala \xb7 esc: voltar')
   P.show()
   k=P.key()
   dx=(x1-x0)/4
   dy=(y1-y0)/4
   if k=='esc'or k=='enter':
    return
   if k=='left':
    x0-=dx
    x1-=dx
   elif k=='right':
    x0+=dx
    x1+=dx
   elif k=='up':
    y0+=dy
    y1+=dy
   elif k=='down':
    y0-=dy
    y1-=dy
   elif k=='+':
    x0+=dx
    x1-=dx
    y0+=dy
    y1-=dy
   elif k=='-':
    x0-=2*dx
    x1+=2*dx
    y0-=2*dy
    y1+=2*dy
 return _ns('P N E OKS ERS cols body title foot bar menu text msg ask lesson edit form graph',P,N,E,OKS,ERS,cols,body,title,foot,bar,menu,text,msg,ask,lesson,edit,form,graph)


_F['m1_ui'] = _m_m1_ui


def _m_p_a7():
 D = "~{~| 5~F (7.`K ~o`s a7a|Sequ`B`M$0 $kidades|se~1`M $kidade ~[ &Fl term`L $L n lei de #/$d `ica `x se~1`M\
 aritmetica e ~[&3prp.seq&6`_`a `/ 7.`K `q Sequ`B`M$0 $kidades`v$- Descobrir a $kidade `Aa sequ`B`M.~= o ~[\
 &Fl `Aa sequ`B`M `J `i`)a `x.`3 ~[$0 ver se um `0 `( ~[.`u$- Term`L $L n: u(n); u(1) `( o 1.`K ~[.$- S$b\
 `i`)a ~m ~[s segui`O `( $> d, ent`'o ~f d n + (u(1) - d).$- #+ ~s u(20), $; n ~! 20.$- Um `0 `( ~[ se ~f `0\
 ~: ~O`)`'o n inteira e positiva.`? Termo &Fl (`i`)a `x)|~f d `, n + (u(1) - d)|d: `i`)a ~m ~[s segui`O;n:\
 $L|sequ`B`Ms `J `i`)a `x (aritm`(ticas)|3, 7, 11...: ~f 4n - 1&3prp.seq`?`< a sequ`B`M 3, 7, 11, 15, ...`1\
 ~[ &Fl, u(20) e ver se 95 `( ~[.`S &i`)a `x: d = 7 - 3 $h.`R ~f 4n + (3 - 4), ~/ ~f 4n - 1.`] u(20) $h `, 20\
 - 1 = 79$r 4n - 1 &f5 d`2 4n &f6 e n ~W4: 95 `( o 24.`K ~[.~x ~f 4n - 1; u(20) = 79; 95 `( ~[.`% u(1) $h - 1\
 &_ `N.`t`U `( o ~[ &Fl da sequ`B`M 10, 8, 6, 4, ...?`r\n\
d = -2, ~K ~f -2n + 12 (u(1) $i).`s a7b|#.`7 alg`(bricas|$/ao algebrica variavel monomio ~[s `[ ~5 reduzir\
 propriedade dis~7butiva `Z $^erico&3&?&6`_`a `/ 7.`K `q #.`7 alg`(bricas`v$- Traduzir situa`)`7 ~! $/`7 `J\
 #@s.$- $or, juntando ~[s `[.`3 o `Z `Aa $/`'o `V um `Z da vari`2vel.`u$- 3x e -5x s`'o ~[s `[ ($. &,te\
 literal): 3x - 5`| -2x.$- Dis~7butiva: a(b + c) &Zb + ac; -&+ 2) = -$X 2.$- Os ~[s `J x`- n`'&s juntam `J os\
 ~[s `J x.$- Valor $^`(rico: $; a #@ (usa &,`Bnteses nos $Ks).`? Propriedade dis~7butiva|a(b + c) &Zb + ac|a,\
 b, c: `0s ou $/`7|o $4 `H ~} &,cela|3&+ 4) &_x - 12&3&?`?`< 2(3x - 1) - ($X 4).`1 ~5 e ~s o `Z `V `| -2.`S\
 Dis~7butiva: 6x - 2 - x - 4.`R Termos `[: 6x - `| 5x e -2 - 4 = -6.`] #.`'o simplifi~}: 5x - 6.$r #+ `| -2:\
 5 `, (-2) - 6 = -16~x 5x - 6; `V `| -2 $Q -16.`% 2(3 `, (-2) - 1) - (-2 + 4) = -16 `N.`t\n\
$o 4a + 3 - (a - 5).`r\n\
4a + 3 - a + 5 &_a + 8 (`V a $j $Q 11).`s a7c|#5`)`7 &N`K &D|~3$d inco#C ~O$d membros ~3coe$0qui$Qntes ~S\
 &,enteses &Tivel $Tivel &b ${&3&y&6`_`a `/ 7.`K `q #5`)`7`v`l ~3`)`7 &N`K &D, mesmo `J &,`Bnteses.$-\
 Classificar `} ~3`)`'o (&T`;vel, $T`;vel, &b).`l ${ `J ~3`)`7.`u$- Tira os &,`Bnteses; os ~[s `J x $^ membro\
 #Es `0s no outro.$- Ao mudar de membro, o ~[ mud$< sinal.$- Reduz e $E $S coeficiente de x.$- 0`| 5:\
 $T`;vel; 0`| 0: &b (&;~1r x).$- Verifica: $; a ~O`)`'o nos ~2 membros.`? #5`)`'o &N`K &D|a `| b `h `| b /\
 a|a, b: `0s|a ~L 0 (s$b = 0, `( $T`;vel ou &b)|3`| 15 `h `| 5&3&y`?`< 3&+ 2) = $X 4.`1 ~S e verificar.`S\
 Par`Bnteses: 3x - 6 = $X 4.`R Mudar de membro: 3x - `| 4 + 6.`] Reduzir: 2`| 10, ~K `| 5.~x &- {5}.`% 3 `,\
 (5 - 2) &f e 5 + 4 &f `N.`t\n\
O dobro `A `0, $J 7, `( 31~- `( o `0?`r\n\
2$X 7 &_1 `h 2`| 24 `h `| 12.`s a7d|Pro~!$( di`n|`d di`n `x de `d y = kx regr$< tres ~u gra$U `n pela origem\
 escala&3prp.prop&6`_`a `/ 7.`K `q Pro~!$( di`n `Jo fun`)`'o`v`o &] di`n~T~!&I`3 a `x de `d e `Jpletar ~us.$-\
 Interp`nr o gr`2$U: `n ~1 $w $}.`u$- Di`n~T~!#3 y / x `( $> $8 `0 k.$- Fun`)`'`L `d di`n: y = kx.$- O gr`2$U\
 `( `} `n ~1 $w $} (0, 0).$- Valor em falta: y = k `, x ou `| y : k (regr$< tr`Bs simples).$- Escala: &E\
 n`L~Jho : &E ~Ql.`? Pro~!$( di`n|y = k `, x|k = y / x: `x de `d|&] di`n~T~!cionais|3 kg &Qm 6 `W: k ~W\
 `W/kg&3prp.prop`?`< 2 kg de laranjas &Qm 3,60 `W.`1 `x, pre`)`L 5 kg e peso ~1 se `Jpra `J 9 `W.`S k &_,60\
 $3 $j,80 `W/kg.`R 5 kg: 1,80 `, 5 &f `W.`] Com 9 `W: 9 / 1,80 &g kg.~x k $j,80 `W/kg (o pre`)o do quilo); 5\
 kg &Qm 9 `W.`% 9 / 5 $j,8, $8 k `N.`t&2 mapa $p escala 1 : 50 000, 3 cm correspondem a quantos quil`X~Rs?`r\n\
3 `, 50 000 $j50 000 cm $j,5 km.`s a7e|Percentagens|`z ~! cento aument`Lsconto iva `Z ~l varia$d $R#% $4\
 `Htivo&3prp.$Rc&6`_`a `/ 7.`K `q Percentagens`v`3 `} `z `Aa quantidade.$) aumento$0 $Ns.`3 o `Z ~l $b\
 varia`)`'o $R#%.`u$- p% d$b = (p / 100) `, a.$- Aument`L p%: a `, (1 + p/100); $N: a `, (1 - p/100).$- Valor\
 ~l: $E $S $4 (~! exemplo, ~! 1,23 `V tirar o IVA).$- Varia`)`'o $R#% = (novo - ~l) / ~l `, 100.$- +10% e\
 depois -10% n`'o volta ao `Z ~l.`? Aumento e $N|novo &Z `, (1 \xb1 p / 100)|a: `Z ~l;p: `z|+ `V aumento, -\
 `V $N|50 `W `J 20% de $N: 40 `W&3prp.$Rc`? Varia`)`'o $R#%|(b - a) / a `, 100|a: `Z ~l;b: `Z final|a ~L 0|de\
 80 `V 92: +15%&3prp.$Rc`?`< uns t`(nis &Qm 80 `W e t`Bm 15% de $N.`1 pre`)o `J $N e `z ~1 se poupa em\
 euros.`S Fator: 1 - #7 = 0,85.`R Pre`)o: 80 `, 0,85 = 68 `W.`] Poupan`)a: 80 - 68 $+ `W, ~1 `( 15% de 80.~x\
 Pag$s 68 `W.`% #7 `, 80 $+ `N.`t$H pre`)o passou de 40 `W `V 50 `W~- foi o aumento $R#%?`r\n\
(50 - 40) / 40 `, 100 ~W5%.~< 1|a7e1|Padr`'o `J f`X&m&3prp.seq|a7a`6 `J f`X&m fazem-se `Is ~H a ~H: 1 `I usa\
 4 f`X&m, 2 usam 7 e 3 usam 10. `ms f`X&m s`'o precisos `V 25 `Is?`C`)`'o:`S A `i`)a `( `x: 7 - 4 $i - 7\
 &_.`R ~f 3n + (4 - 3), ~/ ~f 3n + 1.`] u(25) &_ `, 25 + 1 = 76`4 76 f`X&m.`5`)`'o: ~} `I novo acrescenta 3\
 f`X&m ao $:.`. `Hr 25 ~! 4 (os la`O `Juns contam `} s`X vez).~< 2|a7e2|#5`)`'o `J o dobro #E ~7plo&3&y|a7c`6\
 a Ana ~: o ~7plo da idade do irm`'o. Daqui a 6 anos ter`2 o dobro. Que idades t`Bm?`C`)`'o:`S Irm`'o: x\
 anos; Ana: 3x anos.`R Daqui a 6 anos: 3$X 6 ~W($X 6).`] 3$X 6 ~W$X #L ~K `| 6.$r A Ana ~: 3 `, 6 $j8 anos.`4\
 o irm`'o ~: 6 ano$0 a Ana 18.`5`)`'o: daqui a 6 anos, 24 ~W `, 12 `N.`. ~'r 6 s`X a `} $c idades.~<\
 3|a7e3|Doi~Pscontos segui`O&3prp.$Rc|a7e`6 um casac`L 120 `W ~: 20% de $N e, na #', $J 10% sobr#E novo\
 pre`)o~- `( `Lsconto #9, em `z?`C`)`'o:`S Fator #9: 0,80 `, 0,90 = 0,72.`R Pre`)o final: 120 `, 0,72 = 86,40\
 `W.`] Desconto #9: 1 - 0,72 = 0,28, ~/ 28%.`4 28% de $N (e n`'o 30%).`5`)`'o: o 2.`K $N aplica-s$b um pre`)o\
 j`2 $J baixo.`. ~'r as $Rcentagens (20% + 10%).\n\
"
 return _ns('D', _dz(D))


_F['p_a7'] = _m_p_a7


def _m_p_a8():
 D = "~{~| 5~F (8.`K ~o`s a8a|Polin`Xmio$0 ~0 not`2veis|monomio &pinomio &D ~[s `[ `Hr &pinomios ~0 notaveis `I do\
 binomio `ic$< `Is&3&?|8|n`_`a `/ 8.`K `q #.`7 alg`(bricas (&pin`Xmios)`v$- &'r, #- e `Hr &pin`Xmios.~A os ~0\
 not`2&r~= um &pin`Xmio na #/ reduzida e dizer o &D.`u$- `{r: ~} ~[ `A ~! ~} ~[ do outro.$- &:`Xmio: (a +\
 b)`- &Z`- + 2ab + b`-; (a - b)`- &Z`- - 2ab + b`-.$- &i`)$< `Is: (a + b)(a - b) &Z`- - b`-.$- Cuidado: (a +\
 b)`- n`'o `( a`- + b`-.$- Forma reduzida: juntar os ~[s `[ e $[r $S &D.`? &:`Xmio|(a \xb1 b)`- &Z`- \xb1 2ab\
 + b`-|a, b: mon`Xmios|o ~[ do meio `( o dobro do ~X|($X 3)`- = x`- + 6$X 9&3&?`? &i`)$< `Is|(a + b)(a - b)\
 &Z`- - b`-|a, b: mon`Xmios|~' vezes `i`)a|&+ 1)($X 1) = x`- - 1&3&?`?`< ($X 3)`- - &+ 1)($X 1).`1 #/\
 reduzida e `Z `V `| 2.`S ($X 3)`- = x`- + 6$X 9.`R &+ 1)($X 1) = x`- - 1.`] x`- + 6$X 9 - x`- + 1 = 6$X\
 10.$r #+ `| 2: 6 `, 2 + 10 ~W2~x 6$X 10 (&D 1); $Q 22 `V `| 2.`% (2 + 3)`- - 1 `, 3 ~W2 `N.`t\n\
De~Jvolve (2x - 5)`-.`r\n\
4x`- - 20$X 25 (`V `| 1 $Q 9).`s a8b|Fatorizar e ~S ~3`)`7 ~! $4iza`)`'o|$4izar $4 `Jum ~! em evide`M ~0\
 notaveis `ic$< `Is lei do $6 ~X ~3$d do 2.o &D in`Jpleta&3&p.fat|8|n`_`a `/ 8.`K `q #5`)`7 ($4iza`)`'o)`v$-\
 Fatorizar pondo um $4 `Jum em evid`B`M.$- Fatorizar `J os ~0 not`2&r`l ~3`)`7 `J a lei do $6 ~X.`u$- Fator\
 `Jum: 2x`- - 8`| 2x&+ 4).$- &i`)$< `Is: x`- - 9 = &+ 3)($X 3).$- &:`Xmio: x`- + 6$X 9 = ($X 3)`-.$- Lei do\
 $6 ~X: a `, b = 0 `h a = 0 ou b = 0.$- #+ ~S: tudo no 1.`K membro, $4iza e &8a ~} $4 a 0.`? Lei do $6 ~X|a\
 `, b = 0 `h a = 0 #8 b = 0|a, b: `0s ou $/`7|um ~X `( 0 se um `O ~p for 0|x&+ 4) = 0 `h `| 0 #8 `|\
 4&3&p.fat`?`< 2x`- = 8x e x`- - 25 = 0.`1 ~S as ~) ~3`)`7.`S 2x`- - 8`| 0 `h 2x&+ 4) = 0 `h `| 0 #8 `| 4`R\
 x`- - 25 = 0 `h &+ 5)($X 5) = 0 `h `| 5 #8 `| -5~x &- {0; 4} e &- {-5; 5}.`% 2 `, 4`- &_2 e 8 `, 4 &_2 `N.`t\n\
Fatoriza x`- - 10$X 25.`r\n\
&+ 5)`-, um `I do bin`Xmio (`V `| 0 $Q 25).`s a8c|#5`)`7 `J ~+e$0 ~3`)`7 literais|~3$d `J ~+es mmc ~3$d\
 literal ~S em $L a `} #@ fo$ys isolar variavel&3&y|8|n`_`a `/ 8.`K `q #5`)`7 (literais)`v`l ~3`)`7 &N`K &D\
 `J ~+es.`l `} f`X$y em $L a `} $c #@s.`u$- Denominadores: `H os ~2 membros $S ~8$- Aten`)`'o a~q - antes `Aa\
 $G`)`'o: -&+ 1)/2 = (-$X 1)/2.$- #5`)`'o literal: a inc`X#C `( a #@ pedida; as outras s`'o `0s.$- Isola a\
 inc`X#C `Jo n`} ~3`)`'o $^`(rica.$- Ex.: &> b `, h $3 em $L a h: h ~WA / b (b ~L 0).`? $fr em $L a `}\
 #@|isolar a #@ pedida, `Jo n`} ~3`)`'o|as outras #@s s`'o `0s|n`'&s pode ~n ~! 0|v = d / t `h d = v `,\
 t&3&y`?`< &+ 1)/2 + x/3 $h.`1 ~S a ~3`)`'o.`S ~8(2, 3) = 6; `, 6: 3&+ 1) + 2`| 24.`R 3x - 3 + 2`| 24, ~K 5`|\
 27.`] `| 27/5 &g,4~x &- {5,4}.`% (5,4 - 1)/2 + 5,4/3 ~W,2 + 1,8 $h `N.`t\n\
$f P ~Wc + 2l em $L a l.`r\n\
2l = P - 2c, ~K l = (P - 2c) $3 (`J P ~W0 e c = 6, l $h).`s a8d|Sis~:a~P ~) ~3`)`7|sis~:$< ~) ~3&| &No &D ~)\
 inco#Cs metod`L $;$d ~O$d &, $[do &Tivel determinado indeterminado $Tivel `ns&3exp.sis|8|n`_`a `/ 8.`K `q\
 Sis~:a~P ~3`)`7`v`l sis~:as $S m`(tod`L $;`)`'o.$- Classificar um sis~:a.$- Interp`nr a ~O`)`'o `Jo o pont`L\
 interse`)`'`L ~) `ns.`u$- Isola `} inc`X#C n`} $c ~3`)`7.$- Substitui na outra e resolv$b ~3`)`'o `J `} s`X\
 inc`X#C.$- Volta $p $/`'o isolada `V ~s a outra inc`X#C.$- Poss`;vel e determinado: `} ~O`)`'o (`ns\
 concorrentes).$- Im&T`;vel: `ns `V#A; indeterminado: `ns coincidentes.`? M`(tod`L $;`)`'o|isolar `} inc`X#C\
 e $;r na outra ~3`)`'o|x, y: inc`X#Cs|sis~:a~P ~) ~3`)`7 &N`K &D|$X y $i e 2x - y ~W: (4, 6)&3exp.sis`?`< $X\
 y $i e 2x - y ~W.`1 ~S o sis~:a.`S Da 1.\xaa: `| 10 - y.`R Na 2.\xaa: 2(10 - y) - y ~W, ~K -3y = -18.`] y =\
 -18 : (-3) = 6$r `| 10 - 6 $h~x (x, y) = (4, 6): sis~:a &T`;vel e determinado.`% 2 `, 4 - 6 ~W `N.`t&2\
 ~kacionamento h`2 carro$0 motas: 20 ve`;culo$0 70 ro$c. `ms carros h`2?`r\n\
c + m ~W0 e 4c + 2m = 70: c $j5 carro$0 5 motas.`s a8e|Fun`)`'o afim|fun$d afim y = m$X b declive $[da $}\
 gra$U `n fun$d linear `d di`n zero da fun$d ~2 `k&3atf.afim|8|n`_`a `/ 8.`K `q Fun`)`7 (fun`)`'o afim)`v`o\
 `} fun`)`'o afim e &su gr`2$U (`} `n).$- Interp`nr `Lclive $b $[da $}.~= a $/`'o $9 de ~2 `k.`u$- Fun`)`'o\
 afim: #0 = m$X b; o gr`2$U `( `} `n.$- m (declive): quanto sobe y #D x #) 1.$- b ($[da $}): ond$b `n corta o\
 &u Oy.$- Com b = 0: fun`)`'o linear (`d di`n).$- Dois `k: m = (y~M - y~@) / (x~M - x~@); depois b = y~@ - m\
 x~@.`? Declive|m = (y~M - y~@) / (x~M - x~@)|(x~@, y~@) e (x~M, y~M): `k da `n|x~@ ~L x~M|(1, 3) e (3, 7): m\
 ~W&3atf.afim`? Fun`)`'o afim|#0 = m $X b|m: declive;b: $[da $}|o gr`2$U `( `} `n|m ~W, b $j: #0 ~W$X\
 1&3atf.afim`?`< a `n $w em A(1, 3) e B(3, 7).`1 $/`'o da fun`)`'o afim e zero.`S m = (7 - 3) / (3 - 1) ~W`R\
 b &_ - 2 `, 1 $j, ~K #0 ~W$X 1.`] Zero: 2$X 1 = 0 `h `| -0,5.~x #0 ~W$X 1; o zero `( -0,5.`% f(3) ~W `, 3 +\
 1 = 7 `N.`t$H t`2xi cobra 3,50 `W fixo$0 0,80 `W ~! km. `m &Q `} viagem de 10 km?`r\n\
#0 = 0,8$X 3,5; f(10) $j1,50 `W.~< 1|a8e1|&A~Q `A `I #)do&3&?|a8a`6 o ~H `A `I ~U x &x Aumenta-s#E ~H 3 &x `m\
 #) a `2~Q?`C`)`'o:`S Nova `2~Q: ($X 3)`- = x`- + 6$X 9.`R Aumento: x`- + 6$X 9 - x`- = 6$X 9.`] #+ `| 5: 6\
 `, 5 + 9 &_9 cm`-.`4 a `2~Q #) 6$X 9 cm`- (39 cm`- se `| 5).`5`)`'o: 8`- - 5`- &_9 `N.`. &zr ($X 3)`- = x`-\
 + 9.~< 2|a8e2|Bilhete~P cinema&3exp.sis|a8d`6 foram vendi`O 120 bilhetes: o~P adulto &Qm 7 `W #E~P crian`)a\
 4 `W. Receber$s 690 `W. `ms bilhete~P ~} tip&s venderam?`C`)`'o:`S a + c $+0 e 7a + 4c = 690.`R a $+0 - c;\
 7(120 - c) + 4c = 690, ~K -3c = -150.`] c &g0 $b $+0 - 50 = 70.`4 70 bilhete~P adulto e 50 de\
 crian`)a.`5`)`'o: 7 `, 70 + 4 `, 50 = 690 `N.`. trocar as inc`X#Cs na resposta.~< 3|a8e3|Duas tarifa~P\
 telem`Xvel&3atf.afim|a8e`6 o tarif`2rio A &Q 10 `W ~! m`B$0 0,05 `W ~! minuto. O B &Q #7 `W ~! minuto, sem\
 mensalidade. A &,tir de quantos minutos o A fica $J barato?`C`)`'o:`S A(x) = 0,05$X 10 e B(x) = #7x.`R\
 Iguais #D 0,05$X 10 = #7x, ~/ 0,1`| 10 e `| 100 min.`] #+ 200 min: A ~W0 `W e B &_0 `W.`4 acim$< 100\
 minutos, o tarif`2rio A `( $J barato.`5`)`'o: as ~) `ns cruz$s no $, (100, 15).`. `J`Vr s`X as mensalidades.\n\
"
 return _ns('D', _dz(D))


_F['p_a8'] = _m_p_a8


def _m_p_a9():
 D = "~{~| 4~F (9.`K ~o`s a9a|In~3`)`7 &N`K &D|in~3$d &No &D &%~O$d ~4 inverter ~q `Hr ~! $K in~3$d dupla &R$d\
 disjun$d&3exp.ineq|9|n`_`a `/ 9.`K `q In~3`)`7`v`l in~3`)`7 &N`K &D.~= o &%~O`)`'o `Jo ~4.`l &R`)`7 e\
 disjun`)`7 de in~3`)`7.`u$- $f-se `Jo `} ~3`)`'o: &,`Bnteses, ~+es, se`Vr ~[s.$- Ao `Hr ou ~n ~! um `0 $K,\
 ~q inverte-se.$- -2x ~c 4 `h x ~? -2.$- O &%~O`)`'o &G `J um ~4.$- \"e\": interse`)`'o `O ~4s; \"ou\":\
 reuni`'o.`? Inverter ~q|a < b `h -a > -b|`Hr ~! um `0 $K|$8 `V ~?, > e ~c|-2x ~c 4 `h x ~? -2&3exp.ineq`?`<\
 3 - 2x ~c 7.`1 ~S e &zr o &%~O`)`'o.`S -2x ~c 7 - 3, ~K -2x ~c 4.`R Divide ~! -2 e inverte ~q: x ~? -2.~x &-\
 ]-~,, -2].`% `V `| -3: 3 - 2 `, (-3) &f ~c 7 `N.`t\n\
$f 2$X 1 < $X 5.`r\n\
x < 4: &- ]-~,, 4[.`s a9b|#5`)`7 do 2.`K &D|~3$d do 2.o &D fo$y resolvente binomio &c in`Jpleta $4iza$d lei\
 do $6 ~X zeros ~O&|&3atq.q2|9|n`_`a `/ 9.`K `q #5`)`7 do 2.`K &D`v`l ~3`)`7 in`Jpletas ~! $4iza`)`'o.~A a\
 f`X$y resolvente.$- Saber quantas ~O`)`7 h`2 $S &c.`u$- Forma: ax`- + b$X c = 0, `J a ~L 0.$- In`Jpletas:\
 ax`- + b`| 0 ($4 `Jum x) ou ax`- + c = 0 (isolar x`-).$- F`X$y resolvente: `| (-b \xb1 `+$5) / (2a), `J $5 =\
 b`- - 4ac.$- $5 > 0: ~) ~O`)`7; $5 = 0: `}; $5 < 0: nenh`} (em \u211d).$- Passa $> tudo `V o 1.`K membro\
 ante~P aplicar a f`X$y.`? F`X$y resolvente|`| (-b \xb1 `+(b`- - 4ac)) / (2a)|a, b, c: coeficiente~P ax`- +\
 b$X c = 0|a ~L 0|2x`- - 5x - 3 = 0: `| -1/2 ou `| 3&3atq.q2`?`< 2x`- - 5x - 3 = 0.`1 ~S `J a f`X$y\
 resolvente.`S a ~W, b = -5, c = -3; $5 ~W5 + 24 $h9.`R `| (5 \xb1 7) / 4.`] `| 12 / 4 &_ ou `| -2 / 4 =\
 -0,5.~x &- {-1/2; 3}.`% 2 `, 3`- - 5 `, 3 - 3 = 0 `N.`t\n\
$f x`- - 16 = 0.`r\n\
x`- $j6, ~K `| 4 ou `| -4.`s a9c|Pro~!$( $C|`d $C `x k = xy y = k/x hi$Rbole ~u `Ze$0m falta &]\
 $C~T~!cionais&3prp.inv|9|n`_cleo||q5e:Dilui`)`'`L ~O`)`7|AE `/ 9.`K `q Pro~!$( $C`v`o &] $C~T~!&I`3 a `x e\
 `Ze$0m falta.`o o gr`2$U: ram`L hip`(rbole.`u$- Inversa~T~!#3 x `, y `( $> $8 `0 k.$- y = k / x (x ~L 0).$-\
 Se x duplica, y $w a $n.$- O gr`2$U (x > 0) `( um ram`L hip`(rbole: n`'o $w $}.$- A regr$< tr`Bs simples\
 n`'&srv$bqui.`? Pro~!$( $C|y = k / x|k = x `, y: `x|x ~L 0|4 torneira$0m 6 h: k ~W4&3prp.inv`?`< 4 pintores\
 pintam `} casa em 6 $!s.`1 $!s ~1 demoram 3 pintore$0 pintores `V a fazer em 2 $!s.`S k $h `, 6 ~W4\
 (pintores `, $!s).`R 3 pintores: 24 / 3 = 8 $!s.`] Em 2 $!s: 24 $3 $+ pintores.~x 8 $!$0 12 pintores.`% 3 `,\
 8 $+ `, 2 ~W4 `N.`t\n\
Se y $j8 / x, quanto $Q y #D `| 6?`r\n\
y $j8 / 6 &_.`s a9d|Fun`)`7 do tipo y &Zx`-|fun$d quadratica y &Zx^2 `Vbola ve$P eix`L #B~7a #H gra$U &/\
 objeto&3atf.fx|9|n`_`a `/ 9.`K `q Fun`)`7 (y &Zx`-)`v$- Repre~Jtar fun`)`7 do tipo y &Zx`-.$- &J ~q d$b `J a\
 #H.`3 imagen$0 objetos.`u$- O gr`2fic`L y &Zx`- (a ~L 0) `( `} &,`2bola `J v`($P $}.$- a > 0: #H `V cima; a\
 < 0: `V baixo.$- O &u Oy `( eix`L #B~7a: f(-x) = #0.$- `m `y `ga`g, $J \"fechada\" `( a &,`2bola.$- Objeto\
 `Aa &/: resolv$bx`- = y.`? Fun`)`'o y &Zx`-|#0 &Z x`-|a ~L 0|v`($P (0, 0); &u `| 0|a ~W: f(3)\
 $j8&3atf.fx`?`< #0 ~Wx`-.`1 f(3), f(-3) #Es objetos `J &/ 50.`S f(3) ~W `, 9 $j8 e f(-3) $j8.`R 2x`- &g0 `h\
 x`- ~W5 `h `| 5 #8 `| -5.~x f(3) = f(-3) $j8; objeto~P 50: -5 e 5.`% 2 `, 5`- &g0 `N.`t\n\
O $, (2, -12) $Rtenc$bo gr`2fic`L y &Zx`-~- `( a?`r$-12 &Z `, 4, ~K a = -3.~< 1|a9e1|In~3`)`'o `J\
 $G`)`7&3exp.ineq|a9a`6 resolve &+ 1)/2 < $X 1.`C`)`'o:`S `, 2: x - 1 < 2$X 2.`R x - 2x < 2 + 1, ~K -x < 3.`]\
 `, (-1), inverte-se ~q: x > -3.`4 &- ]-3, +~,[.`5`)`'o: `V `| 0: -0,5 < 1 `N.`. es~1cer de inverter ~q ao\
 `Hr ~! -1.~< 2|a9e2|&A~Q `A &<`!&3atq.q2|a9b`6 um &<`! ~: `J~E 3 cm `y do ~1 a largura e 40 cm`- de `2~Q.\
 Quais s`'o as dimens`7?`C`)`'o:`S x($X 3) $h0 `h x`- + 3x - 40 = 0.`R $5 &f + 160 $j69; `| (-3 \xb1 13)\
 $3.`] `| 5 ou `| -8 (n`'&srve: `( um `J~E).`4 #2 ~! 8 &x`5`)`'o: 5 `, 8 $h0 `N.`. aceitar a ~O`)`'o negativa\
 $^ problem$< medi$c.~< 3|a9e3|Velocidade e ~:po `Aa viagem&3prp.inv|a9c`6 a 90 km/h, `} viagem demora 2 h 20\
 min. `m ~:p`Lmora a 105 km/h?`C`)`'o:`S Tempo em horas: 2 h 20 min = 7/3 h.`R Velocidade e ~:po s`'o\
 $C~T~!#3 k &f0 `, 7/3 ~W10 km.`] A 105 km/h: 210 / 105 ~W h.`4 2 horas.`5`)`'o: k `( a ~B`M $Rcorrida, 210\
 km.`. &zr 2 h 20 min `Jo 2,2 h.\n\
"
 return _ns('D', _dz(D))


_F['p_a9'] = _m_p_a9


def _m_p_d7():
 D = "~{~| 3&X Da`O (7.`K ~o`s d7a|Tabela~P $%`B`M$0 gr`2fi~a|da`O &;itativos quantitativos fre~1`M ab~Ota fre~1`M\
 ~9 `z ~u de fre~1`Ms grafic`L barras gra$U &S setor ~I&3&4&6`_`a `/ 7.`K `q Da`O (repre~Jta`)`7)`v$- #J da`O\
 &;itativo~P quantitativos.~j `} ~u de $%`B`Ms ab~Ota$0 ~9s.`3 os `!s `A gr`2$U &S.`u$- Qualitativos:\
 categorias (cor, des~!to); quantitativos: `0s.$- Frequ`B`M ab~Ota: quantas vezes a&,ec#E `Z.$- Frequ`B`M ~9\
 = $%`B`M ab~Ota / n (n: #9 #!`O).$- As $%`B`Ms ~9s ~'m 1 (100%).$- Gr`2$U &S: `! d&stor = $%`B`M ~9 `,\
 360`8.`? Frequ`B`M ~9|fr = fa / n|fa: $%`B`M ab~Ota;n: `0 #!`O|~' de to$c $j|6 em 20: fr = 0,3 &_0%&3&4`? `e\
 d&stor|`9 = fr `, 360`8|fr: $%`B`M ~9|gr`2$U &S|fr = 0,25: `9 &f0`8&3&4`?`< des~!to preferid`L 20 alunos:\
 futebol 8, nata`)`'o 5, t`(nis 4, &L 3.`1 $%`B`Ms ~9$0 `!s do gr`2$U &S.`S Futebol: 8 $30 = 0,4 (40%); `!\
 0,4 `, 360`8 $j44`8.`R Nata`)`'o: 5 $30 = 0,25; `! 90`8.`] T`(nis: 4 $30 = 0,2; `! 72`8.$r Outros: 3 $30 =\
 #7; `! 54`8.~x `es: 144`8, 90`8, 72`8 e 54`8.`% 144 + 90 + 72 + 54 &[ `N.`t\n\
N`} turm$< 25 alunos, 10 v`Bm a p`(. Que `z vem a p`(?`r\n\
10 $35 = 0,4 $h0%.`s d7b|M`($!, moda, `P e `^|me$! aritmetic&doda `P `^ &E~P localiza$d da`O $[`O posi$d\
 central $^ero &, im&, #!`O&3&4&6`_`a `/ 7.`K `q Da`O (medi$c)`v`3 &d`($!, &doda $b `P.`3 a `^ `A &Rt`L\
 da`O.$- Escolher a &E $J ad~3da.`u$- M`($!: ~' `O da`O / `0 #!`O.$- Moda: o `Z $J fre~1nte (pode haver $J\
 `Aa ou nenh`}).$- Me$!na: $[ &M`O; `( o do meio (n `;m&,) ou &d`($! `O ~2 do meio (n &,).$- &) = `y `Z - &7\
 `Z.$- Um `Z muito `ite `O &L afeta &d`($!, mas pouco a `P.`? M`($!|x\u0304 = (x~@ + x~M + ... + x\u2099) /\
 n|n: `0 #!`O|da`O quantitativos|2, 4, 9: m`($! 5&3&4`? &)|&> m`2ximo - m`;nimo|da`O quantitativos|~U a\
 dis$Rs`'o|de 2 a 9: &> 7&3&4`?`< idades `O 8 jogadores `Aa equipa: 15, 16, 16, 14, 17, 16, 15, 19.`1 m`($!,\
 moda, `P e `^.`S M`($!: 128 / 8 $j6 anos.`R Moda: 16 (a&,ece 3 vezes).`] Ordena`O: 14, 15, 15, 16, 16, 16,\
 17, 19; `P = (16 + 16) $3 $j6.$r &): 19 - 14 &g anos.~x M`($!, moda e `P: 16 anos; `^: 5 anos.`% 15 + 16 +\
 16 + 14 + 17 + 16 + 15 + 19 $+8 `N.`t`U `( a `P de 3, 9, 4, 7, 5?`r\n\
Ordena`O: 3, 4, 5, 7, 9; a `P `( 5.`s d7c|Diagram$< caule-e-folhas|`p de caule e folhas caule folhas $[r da`O\
 `J`Vr ~2 &Rto~P da`O dis~7bui$d&3ate.caule&6`_`a `/ 7.`K `q Da`O (repre~Jta`)`7)`v~j um `p de\
 caule-e-folhas.$- Ler &M`O $[`O $9 do `p.$- Com`Vr ~2 &Rto~P da`O.`u$- Caule: os algarism&M~Pzenas; folhas:\
 os $c unidades.$- As folha$0screvem-se ~! $L crescente.$- O `p mostra &M`O j`2 $[`O: a `P l`B-se ~K.$-\
 Diagrama duplo: ~2 &Rtos, um de ~} ~H do caule.`? Caule-e-folhas|47 $l caule 4, folha 7|caule:\
 dezenas;folha: unidades|da`O `J 2 algarismos|42, 47, 51: 4 `g 2 7 e 5 `g 1&3ate.caule`?`< notas (0 a 100) de\
 9 alunos: 47, 62, 55, 71, 68, 53, 62, 80, 59.`1 `p de caule-e-folhas, `P e `^.`S 4 `g 7; 5 `g 3 5 9; 6 `g 2\
 2 8; 7 `g 1; 8 `g 0`R Me$!na: o 5.`K `Z $[do, 62.`] &): 80 - 47 &_3.~x Me$!na 62; `^ 33.`% h`2 1 + 3 + 3 + 1\
 + 1 &f folhas `N.`t\n\
No `p 2 `g 1 4 e 3 `g 0 5 5, &; `( &doda?`r\n\
A moda `( 35 (a&,ece ~) vezes).~< 1|d7e1|Cor preferida&3&4|d7a`6 $Rguntou-s$b cor preferida a 30 pessoas:\
 azul #L verde 9, vermelho 6, amarelo 3~- `( o `! d&stor do azul $^ gr`2$U &S?`C`)`'o:`S Frequ`B`M ~9 do\
 azul: 12 / 30 = 0,4.`R `e: 0,4 `, 360`8 $j44`8.`4 144`8.`5`)`'o: 40% $c pessoas preferem azul.`. usar 100 em\
 vez de 360 nos `!s.~< 2|d7e2|M`($! `J `} ~u de $%`B`Ms&3&4|d7b`6 `0 de irm`'os `O alunos `Aa &P: 0 irm`'os\
 (5 alunos), 1 (10), 2 (6), 3 (4). ~; &d`($! $b `P.`C`)`'o:`S n &g + 10 + 6 + 4 ~W5 alunos.`R &': 0 `, 5 + 1\
 `, 10 + 2 `, 6 + 3 `, 4 &_4.`] M`($!: 34 $35 $j,36 irm`'os.$r Me$!na: o 13.`K `Z $[do; os 15 $:s t`Bm 0 ou 1\
 irm`'o, ~K a `P `( 1.`4 m`($! 1,36; `P 1.`5`)`'o: &d`($! n`'o ~: de ser um `O `Zes `O da`O.`. ~n ~! 4 (o `0\
 de `Zes `ites).~< 3|d7e3|Um `Z ~kranho||d7b`6 sal`2rios di`2rios n`} loja (`W): 50, 52, 55, 55, 58, 300~- `(\
 a &E ~1 melhor repre~Jta os sal`2rios?`C`)`'o:`S M`($!: 570 / 6 &f5 `W.`R Me$!na: (55 + 55) $3 &g5 `W.`] A\
 m`($! `( puxada $S sal`2ri`L 300 `W.`4 a `P (55 `W) repre~Jt&delhor a `yia `O sal`2rios.`5`)`'o: `Zes muito\
 `ites afetam &d`($!, mas pouco a `P.`. escolher $> &d`($!, sem olhar `V &M`O.\n\
"
 return _ns('D', _dz(D))


_F['p_d7'] = _m_p_d7


def _m_p_d8():
 D = "~{~| 2&X Da`O (8.`K ~o`s d8a|Quarti$0 `p &H$0 &o|&o $: quartil terceiro quartil `P `^ &v `p &H$0 &o #' `J\
 bigodes outliers&3ate.uni|8|n`_`a `/ 8.`K `q Da`O (&o)`v`3 os &o `A &Rt`L da`O.~j e ler um `p &H$0 &o.`3 a\
 `^ &v.`u$- Ordena &M`O; a `P $E-o$0m ~) $ns.$- Q1: `P da $n de baixo; Q3: `P da $n de cima.$- Com n `;m&,, a\
 `P n`'o entra em nenh`} $n.$- Diagrama: m`;nimo, Q1, `P, Q3 e m`2ximo.$- &) &v: AIQ = Q3 - Q1 (onde ~k`'o os\
 50% centrais).`? &) &v|AIQ = Q3 - Q1|Q1, Q3: 1.`K e 3.`K &o|~U a dis$Rs`'o `O 50% centrais|Q1 = 6, Q3 $i:\
 AIQ $h&3ate.uni`?`< 3, 5, 6, 6, 7, 8, 9, 10, #L 20 (j`2 $[`O).`1 os cinco `0s do `p $b AIQ.`S n $i `( &,: `P\
 = (7 + 8) $3 = 7,5.`R $] baixo: 3, 5, 6, 6, 7, ~K Q1 = 6.`] $] cima: 8, 9, 10, #L 20, ~K Q3 $i.$r AIQ $i - 6\
 $h~x M`;nimo 3; Q1 = 6; `P 7,5; Q3 $i; m`2ximo 20.`% 20 ~k`2 muito acim$< Q3 + 1,5 `, AIQ $j6: `( um `Z\
 at`;pico.`t&2 `p, Q1 $+ e Q3 ~W0. Que `z `O da`O ~k`2 ~m 12 e 20?`r\n\
Cerc$< 50% (&M`O ~m Q1 e Q3).`s d8b|Da`O em $1$0 histograma|$1s `^ da $1 histograma $, medio $1 modal fre~1`M\
 acumulada ~u de fre~1`Ms agrupa$c da`O continuos&3ate.cls|8|n`_`a `/ 8.`K `q Da`O ($1$0 histogramas)`v$-\
 Agru&, da`O em $1s.~j e ler um histograma.`3 &d`($! $e `J os `k m`(dios.`u$- Classes [a, b[: o limite de\
 baixo entra, `L cima n`'o.$- Histograma: &<`!s juntos; a `c `( a $%`B`M.$- Classe modal: $< `y $%`B`M.$-\
 Ponto m`(di`L [a, b[: (a + b) $3.$- M`($! $e: \u03a3($, m`(dio `, $%`B`M) / n.`? M`($! #!`O agrupa`O|x\u0304\
 `: \u03a3(x\u1d62 `, n\u1d62) / n|x\u1d62: $, m`(dio da $1;n\u1d62: $%`B`M|`Z aproximado|[0, 10[ `J 3 e [10,\
 20[ `J 7: x\u0304 `: 12&3ate.cls`?`< `cs (cm) de 20 alunos: [150, 155[ 3; [155, 160[ 7; [160, 165[ 6; [165,\
 170[ 4.`1 $1 modal e m`($! $e.`S Classe modal: [155, 160[ (7 alunos).`R Pontos m`(dios: 152,5; 157,5; 162,5;\
 167,5.`] \u03a3 $j52,5 `, 3 + 157,5 `, 7 + 162,5 `, 6 + 167,5 `, 4 &_205.$r M`($! `: 3205 $30 $j60,25 &x~x\
 Classe modal [155, 160[; m`($! `: 160,25 &x`% 3 + 7 + 6 + 4 ~W0 alunos `N.`t`U `( o $, m`(dio da $1 [40, 50[?`r\n\
(40 + 50) $3 $h5.~< 1|d8e1|Quartis `J n `;m&,&3ate.uni|d8a`6 ~:pos (min) de 9 alunos a ir `V a escola: 9, 11,\
 #L 13, 14, 15, 16, 18, 20. ~; Q1, a `P e Q3.`C`)`'o:`S Me$!na: o 5.`K dado, 14.`R $] baixo: 9, 11, #L 13, ~K\
 Q1 = (11 + 12) $3 $j1,5.`] $] cima: 15, 16, 18, 20, ~K Q3 = (16 + 18) $3 $j7.`4 Q1 $j1,5; `P 14; Q3\
 $j7.`5`)`'o: $n `O aluno~Pmora ~m 11,5 e 17 minutos.`. p\xf4r a `P dentro $c $ns #D n `( `;m&,.~<\
 2|d8e2|Com`Vr ~) &Ps&3ate.uni|d8a`6 no t~ke, a &P A ~: `P 14 e AIQ 3; a &P B ~: `P 14 e AIQ 7. O ~1 se\
 conclui?`C`)`'o:`S As `Ps s`'o $_: o ~% $c notas `( $8.`R A AIQ da &P B `( `y: 7 - 3 $h `Zes a $J.`] As\
 notas centrais da &P A ~k`'o $J concentra$c.`4 a &P A `( $J homog`(nea.`5`)`'o: a AIQ ~U a dis$Rs`'o; a `P\
 ~U o ~%.`. concluir ~1 as &Ps s`'o $_ s`X pelas `Ps.~< 3|d8e3|Temp`L ~kudo agrupado&3ate.cls|d8b`6 ~:p`L\
 ~kud&smanal (h) de 25 alunos: [0, 2[ 4; [2, 4[ 9; [4, 6[ 8; [6, 8[ 4. ~; &d`($! $e $b `z ~1 ~kuda $S &C 4\
 h.`C`)`'o:`S Pontos m`(dios: 1, 3, 5 e 7.`R M`($! `: (1 `, 4 + 3 `, 9 + 5 `, 8 + 7 `, 4) $35 &_,96 h.`] Pelo\
 &C 4 h: 8 + 4 $+ alunos, ~/ 12 $35 $h8%.`4 m`($! `: 3,96 h; 48% ~kudam $S &C 4 h.`5`)`'o: &d`($! `( $e ~!~1\
 n`'&s sabem &M`O exatos.`. usar os limites $c $1$0m vez `O `k m`(dios.\n\
"
 return _ns('D', _dz(D))


_F['p_d8'] = _m_p_d8


def _m_p_d9():
 D = "~{~| 3&X ~t (9.`K ~o`s d9a|Ex~i`B`Ms aleat`Xria$0 lei de Laplace|ex~ie`M aleatoria espac`L &q`O $7 certo\
 $Tivel provavel `= lei de laplace ~0 &Kaveis ~0 &Tiveis $7 #Gario fre~1`M ~9&3prb.prob|9|n`_`a `/ 9.`K `q\
 ~t`v$- Identificar ex~i`B`Ms aleat`Xria$0 o espa`)`L &q`O.`3 `=s `J a lei de Laplace.~A o $7 #G`2rio.`u$-\
 Ex~i`B`M aleat`Xria: n`'&s sabe $Z ante~P a fazer.$- Lei de Laplace (&q`O &8~Tv`2veis): P(A) = ~0 &K`2veis /\
 ~0 &T`;&r$- 0 ~? P(A) ~? 1; $T`;vel: 0; certo: 1.$- Contr`2rio: P(n`'o A) $j - P(A).$- Com muitas\
 repeti`)`7, a $%`B`M ~9 aproxima-se da `=.`? Lei de Laplace|P(A) = ~0 &K`2veis / ~0 &T`;veis|&q`O\
 &8~Tv`2veis|0 ~? P(A) ~? 1|3 #( azui$0m 10: P = 0,3&3prb.prob`? Acontecimento #G`2rio|P(n`'o A) $j - P(A)|A:\
 $7|A #E #G`2rio n`'o acontecem juntos|P(A) = 0,3: P(n`'o A) = 0,7&3prb.prob`?`< um saco ~: 3 #( azuis, 5\
 vermelha$0 2 verdes; tira-se `} ao acaso.`1 P(azul), P(azul ou verde) e P(n`'o vermelha).`S Casos &T`;veis:\
 3 + 5 + 2 $i.`R P(azul) &_/10 = 0,3.`] P(azul ou verde) &g/10 = 0,5.$r P(n`'o vermelha) $j - 5/10 = 0,5.~x\
 0,3; 0,5 e 0,5.`% 0,3 + 0,5 + 0,2 $j (to$c as cores) `N.`t\n\
Lan`)a-se um dado~- `( a `= #1ir um `0 `y do ~1 4?`r\n\
Casos &K`2veis: 5 e 6; P ~W/6 $j/3.`s d9b|Ex~i`B`Ms `Jpostas: ~u~P dupla entrada|ex~ie`M `Jposta ~2 da`O ~)\
 moe$c ~u de dupla entrada ~' ~X ~0 &Tiveis &8~Tvaveis&3prb.da`O|9|n`_`a `/ 9.`K `q ~t (ex~i`B`Ms\
 `Jpostas)`v$- Organizar os &q`O de ~) ex~i`B`Ms n`} ~u.$- Contar os ~0 &T`;vei$0 os &K`2&r`3 `=$0m ex~i`B`Ms\
 `Jpostas.`u$- Dois da`O: ~u 6 `, 6 `J 36 ~0 &8~Tv`2&r$- Em ~} c`(lula &G $Z (~', ~X...).$- Contam-s$bs\
 c`(lulas &K`2&r$- Duas moe$c: EE, EN, NE, NN (4 ~0); EN e NE s`'o `ites.$- N`'o confundir \"~' 7\" (6 ~0) `J\
 \"&, (3, 4)\" (2 ~0).`? Probabilidade `J a ~u|P(A) = c`(lulas &K`2veis / #9 de c`(lulas|~u de dupla\
 entrada|c`(lulas &8~Tv`2veis|~' 7 `J ~2 da`O: 6/36 $j/6&3prb.da`O`?`< lan`)$s ~2 da`O e ~'$D `k.`1 P(~' 7) e\
 P(~' > 9).`S &' 7: (1,6) (2,5) (3,4) (4,3) (5,2) (6,1), ~/ 6 ~0.`R P(~' 7) = 6/36 $j/6`] &' > 9: 10 (3 ~0),\
 11 (2) e 12 (1): 6 ~0; P = 6/36 $j/6.~x As ~) `=s $Qm 1/6.`% a ~' 7 `( a $J prov`2vel (6 ~0 em 36).`t\n\
Lan`)$s ~) moe$c~- `( a `= #1`;rem faces `ites?`r\n\
EN e NE: P ~W/4 = 0,5.`s d9c|Diagrama$0m `2&=: `J e ~g`)`'o|`p em a&= extra$d `J reposi$d ~g$d ~) extra&| `Hr\
 `=s ramos #4&3prb.urna|9|n`_`a `/ 9.`K `q ~t (`p$0m `2&=)`v~j um `p em `2&=.$- #J extra`)`7 `J e ~g`)`'o.`3\
 `=~P caminho$0 de $7s.`u$- Cada ramo leva a `= desse passo.$- Ao longo `A caminho, `Hm-s$bs `=s.$- V`2rios\
 #4 &K`2veis: ~'m-s$bs `=s.$- Sem reposi`)`'o: na 2.\xaa extra`)`'o h`2 &C `} bola (e &C `} da cor ~1\
 saiu).$- A ~' $c `=~P to`O os #4 `( 1.`? Probabilidade `A caminho|P(1.\xaa A e 2.\xaa B) = P(A) `, P(B\
 depoi~P A)|ramos do `p|`H-s$bo longo do caminho|3 azui$0 2 brancas, ~g`)`'o: P(AA) &_/5 `, 2/4&3prb.urna`?`<\
 `} #' ~: 3 #( azui$0 2 brancas; tir$s ~), ~g`)`'o.`1 P(~) azuis) e P(cores `ites).`S P(AA) &_/5 `, 2/4\
 &_/10`R P(AB) &_/5 `, 2/4 &_/10 e P(BA) ~W/5 `, 3/4 &_/10.`] Cores `ites: 3/10 + 3/10 &_/5~x P(~) azuis) =\
 0,3 e P(cores `ites) = 0,6.`% P(BB) ~W/5 `, 1/4 $j/10 e 3/10 + 3/5 + 1/10 $j `N.`t\n\
E s$b extra`)`'o fosse `J reposi`)`'o, &; seria P(~) azuis)?`r\n\
3/5 `, 3/5 &f/25 = 0,36.~< 1|d9e1|Escolher um aluno&3prb.prob|d9a`6 `} &P ~: 12 rapaze$0 16 ra&,igas.\
 Escolhe-se um aluno ao acaso~- `( a `= de ser ra&,iga?`C`)`'o:`S Casos &T`;veis: 12 + 16 ~W8.`R P(ra&,iga)\
 $j6/28 $h/7 `: 0,57.`4 4/7, ~N 57%.`5`)`'o: `( $J prov`2vel sair `} ra&,iga do ~1 um rapaz.`. ~n 16 ~! 12\
 (rapazes) em vez de 28 (to`O).~< 2|d9e2|Produt`L ~2 da`O&3prb.da`O|d9b`6 lan`)$s ~2 da`O e `H$D `k~- `( a `=\
 d#E ~X ser &,?`C`)`'o:`S O ~X `( `;m&, s`X s#Es ~2 forem `;m&,es: 3 `, 3 &f ~0.`R Produto &,: 36 - 9 ~W7\
 ~0.`] P(&,) ~W7/36 &_/4`4 3/4, ~/ 75%.`5`)`'o: basta um `O da`O ser &, `V o ~X ser &,.`. pensar ~1 &, e\
 `;m&, t`Bm a $. `=.~< 3|d9e3|Pelo &C `} verde&3prb.urna|d9c`6 um saco ~: 2 #( verde$0 4 amarelas. Tir$s ~),\
 ~g`)`'o~- `( a `= #1ir $S &C `} verde?`C`)`'o:`S Contr`2rio: nenh`} verde, ~/ ~) amarelas.`R P(~) amarelas)\
 $h/6 `, 3/5 ~W/5`] P($S &C `} verde) $j - 2/5 &_/5`4 3/5, ~/ 0,6.`5`)`'o: `J o #G`2rio evita-se ~'r tr`Bs\
 #4.`. es~1cer ~1, ~g`)`'o, ficam 5 #(.\n\
"
 return _ns('D', _dz(D))


_F['p_d9'] = _m_p_d9


def _m_p_g7():
 D = "~{~| 5$@~7$? (7.`K ~o`s g7a|`e$0 `ns `V#A|~Is `J#? #:es &W ~hs `ns `V#A secante ~Is &. $M ~C $M ~rs$B&6`_`a\
 `/ 7.`K `q Figuras planas (`!s)`v~A `!s `J#?, #:e$0 &W ~hs.`o &,e~P `!$0m `ns `V#A corta$c ~! `} secante.`3\
 `^~Psconheci$c.`u$- Com#?: ~'m 90`8. Su#?: ~'m 180`8.$- Verticalmente ~hs: s`'o $_.$- #+lela$0 secante: &.,\
 $M ~C e $M ~rs s`'o $_.$- Internos d$8 ~H da secante: s`'o #:es.$- $q $> a #K`'o: \"$M ~C\" ou \"#:es\".`?\
 `es `Jplementare$0 #:es|`9 + \u03b2 &f0`8 (`J#?); `9 + \u03b2 $j80`8 (#:es)|`9, \u03b2: `^s|`!s agu`O t`Bm\
 `Jplementar|35`8 e 55`8; 35`8 e 145`8$B`?`< ~) `ns `V#A corta$c ~! `} secante; um `O `!s ~U 35`8.`1 `^s `O\
 &L sete `!s.`S O &W ~h tamb`(m ~U 35`8.`R O #: ~U 180`8 - 35`8 $j45`8.`] Correspondente$0 $M s`'o $_: quatro\
 `!~P 35`8 e quatr`L 145`8.~x H`2 quatro `!~P 35`8 e quatr`L 145`8.`% 35`8 + 145`8 $j80`8 `N.`t`U `( o\
 `Jplementar `A `! de 62`8?`r\n\
90`8 - 62`8 ~W8`8.`s g7b|`e~P ~7`!$0 &p`;~ys|~' `O ~Is ~C ~7~I ~I ~r &pi~y convexo &pi~y $k $!gonais n\
 la`O$B&6`_`a `/ 7.`K `q Figuras planas (&p`;~ys)`v~A a ~' `O `!s ~C `A ~7`!.`3 a ~' `O `!s ~C `A &p`;~y.`3 o\
 `! $| e ~r `A &p`;~y $k.`u$- Tri`!: `9 + \u03b2 + \u03b3 $j80`8.$- `e ~r `A ~7`! = ~' `O ~2 ~C n`'o ~>s.$-\
 Pol`;gon`L n la`O: S = (n - 2) `, 180`8 ($E-se em n - 2 ~7`!s).$- `es ~rs `A &p`;~y convexo: ~'m $> 360`8.$-\
 Pol`;~y $k: $| = S : n; ~r &[`8 : n.$- Diagonais: n(n - 3) $3.`? &' `O `!s ~C|S = (n - 2) `, 180`8|n: `0 de\
 la`O|&p`;~ys convexos|hex`2~y: 720`8$B`? `e ~r do &p`;~y $k|e &[`8 / n|n: `0 de la`O|$| $j80`8 - e|pent`2~y:\
 72`8$B`?`< um oct`X~y $k.`1 ~' `O `!s ~C, `! $| e `0 de $!gonais.`S S = (8 - 2) `, 180`8 $i80`8`R `e $|:\
 1080`8 : 8 $j35`8`] Diagonais: 8 `, 5 $3 ~W0~x 1080`8, 135`8 e 20 $!gonais.`% ~r &[`8 : 8 $h5`8 e 135`8 +\
 45`8 $j80`8 `N.`t&2 ~7`!, ~2 `!s ~Um 48`8 e 75`8. `m ~U o terceiro?`r\n\
180`8 - 48`8 - 75`8 &g7`8.`s g7c|&A~Q$0 $R`;~R~P &p`;~ys|a~Q ~i~R `I `nngulo `Vlelogramo ~7~I losango\
 trapezio &pi~y $k apo~:a unidade~P a~Q&3&t~Q&6`_`a `/ 7.`K `q Medida (`2~Qs)`v`3 `2~Q$0 $R`;~R~P\
 quadril`2tero$0 ~7`!s.`3 a `2~Q `A &p`;~y $k.`3 `} &E $9 da `2~Q.`u$- Ret`!: &> c `, l. #+lelogramo: &> b `,\
 h.$- Tri`!: &> b `, h $3. Losango: &> D `, d $3.$- Trap`(zio: &> (B + b) $3 `, h.$- Pol`;~y $k: &> $R`;~R $3\
 `, ap`X~:a.$- A `c `( $R&B $p ~].$- 1 m`- $i0 dm`- $i 000 cm`-.`? &A~Q do trap`(zio|&> (B + b) $3 `, h|B, b:\
 ~]s;h: `c|~]s `V#A|#6 8, b &g, h $h: A ~W6&3&t~Q`? &A~Q do &p`;~y $k|&> P $3 `, ap|P: $R`;~R;ap:\
 ap`X~:a|&p`;~ys $kes|hex`2gon`L ~H 4 $bp`X~:a 3,46: A `: 41,5&3&t~Q`?`< um trap`(zio ~: ~]~P 8 cm e #2 e `c\
 de 4 &x Um ~7`! ~: a $. `2~Q e ~] 13 &x`1 `2~Q do trap`(zio e `c do ~7`!.`S &> (8 + 5) $3 `, 4 ~W6 cm`-`R\
 Tri`!: 26 $j3 `, h $3.`] h ~W `, 26 / 13 $h cm~x 26 cm`-; o ~7`! ~: 4 $2 `c.`% 13 `, 4 $3 ~W6 `N.`t$H &<`!\
 ~: 48 cm`- de `2~Q e 6 $2 largura~- `( o $R`;~R?`r\n\
Com~E 48 / 6 = 8 cm; P ~W `, 8 + 2 `, 6 ~W8 &x`s g7d|C`;#=: $R`;~R e `2~Q|ci#= `fe`M $z $!~R pi ~i~R a~Q\
 setor &S `J~E do &O coroa &S&3&t~Q&6`_`a `/ 7.`K `q Medida (c`;#=)`v`3 o $R`;~R $b `2~Q `A c`;#=.`3 o $z $9\
 do $R`;~R ou da `2~Q.`3 a `2~Q `A setor &S.`u$- Di&9~R: d ~Wr. `> `: 3,14 (`( a #K`'o $R`;~R / di&9~R).$-\
 Per`;~R: P ~W`>r = `>d.$- &A~Q: &> `>r`-.$- Setor de `9 &Ds: &> `9/360 `, `>r`-.$- D`2 o `Z exato (`J `>) e\
 um `Z aproximado.`? Per`;~R do c`;#=|P ~W `> r|r: $z|`> `: 3,14|r &g: P $i`> `: 31,4&3&t~Q`? &A~Q do\
 c`;#=|&> `> r`-|r: $z|`> `: 3,14|r &g: A ~W5`> `: 78,5&3&t~Q`?`< `} roda ~: 60 $2 di&9~R.`1 $R`;~R, `2~Q e\
 voltas `V $Rcorrer 1 km.`S r = 60 $3 &_0 cm; P ~W`> `, 30 = 60`> `: 188,#2`R &> `> `, 30`- &f00`> `: 2827\
 cm`-`] 1 km $i0 000 cm; voltas: 100 000 / 188,5 `: 531~x P `: 188,#2, A `: 2827 cm`- e ~N 531 voltas.`% 531\
 `, 188,5 `: 100 094 cm, $Rt`L 1 km `N.`t$H c`;#= ~: 12`> $2 $R`;~R~- `( o $z?`r\n\
2`>r $+`>, ~K r = 6 &x`s g7e|Semelhan`)$< $F|$Wca #Ka`L $Wca &n$d redu$d la`O &. ~Is $_ criterio~P $Wc$<\
 ~7~Is aa lal lll a~Qs k^2&3att.sem&6`_`a `/ 7.`K `q Semelhan`)a`v`o $F `[ $b #K`'`L $W`)a.~A os crit`(rio~P\
 $W`)$< ~7`!s.$- &J $R`;~R$0 `2~Q~P $F `[.`u$- Semelhantes: `!s iguai$0 la`O pro~!&I$- Raz`'o k = ~H da nova\
 / ~H correspondente da original.$- k > 1: &n`)`'o; k < 1: redu`)`'o; k $j: $F $_.$- Tri`!s: basta AA (~2 `!s\
 $_), LAL ou LLL.$- Per`;~Rs `Hm ~! k; `2~Qs ~! k`-.`? Raz`'`L $W`)a|k = ~H da nova figura / ~H\
 correspondente|la`O &.|k > 0|4 cm $l 6 cm: k $j,5&3att.sem`? &A~Q~P $F `[|A' = k`- `, A|k: #K`'`L $W`)a|$F\
 `[|k ~W: a `2~Q quadruplica&3att.sem`?`< um ~7`! de la`O 4, 5 e 6 cm `( &ndo; o lad`L 4 cm $w a 6 &x A `2~Q\
 ~l `( 9,92 cm`-.`1 #K`'o, &L la`O e `2~Q da &n`)`'o.`S k = 6 / 4 $j,5`R La`O: 5 `, 1,5 = 7,#2 e 6 `, 1,5 &f\
 &x`] &A~Q: 1,5`- `, 9,92 ~W2,32 cm`-.~x k $j,5; la`O 6; 7,5 e 9 cm; `2~Q 22,32 cm`-.`% 7,5 / 5 $j,5 `N.`t\n\
Duas $F `[ t`Bm #K`'o 3. S$b &7 ~: #2`- de `2~Q, &; `( a `2~Q da `y?`r\n\
3`- `, 5 $h#2`-.~< 1|g7e1|`e `A &p`;~y $k$B|g7b`6 ~} `! $| `A &p`;~y $k ~U 140`8. `ms la`O ~:?`C`)`'o:`S `e\
 ~r: 180`8 - 140`8 $h0`8.`R n &[`8 : 40`8 &f`4 `( um ene`2~y (9 la`O).`5`)`'o: os 9 `!s ~rs ~'m 9 `, 40`8\
 &[`8 `N.`. ~n 360`8 $S `! $|.~< 2|g7e2|&A~Q `A canteiro&3&t~Q|g7d`6 um canteiro `( um `I de 6 m de ~H `J um\
 semic`;#= apoiado $^ `O la`O~- `( a `2~Q #E $R`;~R do canteiro?`C`)`'o:`S Quadrado: 6 `, 6 &_6 m`-.`R\
 Semic`;rcul`L $z 3 m: `> `, 3`- $3 `: 14,14 m`-.`] &A~Q #9 `: 36 + 14,14 &g0,14 m`-.$r Per`;~R: 3 la`O do `I\
 e meia `f`B`M: 18 + 3`> `: 27,42 m.`4 A `: 50,14 m`- e P `: 27,42 m.`5`)`'o: o ~H onde ~k`2 &smic`;#= n`'o\
 conta no $R`;~R.`. usar o di&9~R (6) `Jo $z.~< 3|g7e3|Altura `Aa `2&= pela &l&3att.sem|g7e`6 um poste de 2 m\
 faz `} sombr$< 1,6 m. \xc0 $. hora, `} `2&= faz `} sombr$< 7,2 m~- `( a `c da `2&=?`C`)`'o:`S Os $z~P sol\
 s`'o `Vlelos: os ~7`!s s`'o `[ (crit`(rio AA).`R Raz`'o: k = 7,2 / 1,6 $h,5`] Altura: 2 `, 4,5 &f m.`4 a\
 `2&= ~: 9 m.`5`)`'o: `c$0 &ls s`'o di`n~T~!&I`. ~n a &l do poste pela da `2&=.\n\
"
 return _ns('D', _dz(D))


_F['p_g7'] = _m_p_g7


def _m_p_g8():
 D = "~{~| 4$@~7$? (8.`K ~o`s g8a|$'`2goras|teorem$< pitagoras `b ~Zs ~7~I `nngulo ~s um ~H ~V &j\
 ~_&3att.pit|8|n`_`a `/ 8.`K `q $'`2goras`v$- Identificar a `b #Es ~Zs.`3 um ~H `A ~7`! &<`!.$) o teorema a\
 $!gonai$0 `cs.`u$- Num ~7`! &<`!: c`- &Z`- + b`- (c: `b).$- A `b `( o ~H ~h ao `! &<o (o `y).$- Hi$genusa: c\
 = `+(a`- + b`-).$- Cateto: a = `+(c`- - b`-).$- Diagonal `A &<`! c `, l: `+(c`- + l`-).$- D`2 o `Z exato\
 (`+) #E aproximado.`? $'`2goras|c`- &Z`- + b`-|c: `b;a, b: ~Zs|s`X em ~7`!s &<`!s|~Zs 3 e 4: c\
 &g&3att.pit`?`< um ecr`' `nngular ~: 48 cm ~! 27 &x`1 medir a ~V, em &pega$c (1 &p ~W,54 cm).`S d`- $h8`- +\
 27`- ~W304 + 729 &_033`R d = `+3033 `: 55,07 cm`] Em &pega$c: 55,07 $3,54 `: 21,7~x A ~V ~U ~N 5#2, ~/ quase\
 22 &pega$c.`% 55,07`- `: 3033 `N.`t$Ha es~} de 5 m ~k`2 en~atada a `} &,ede, `J o p`( a 1,4 m da &,ede. A ~1\
 `c chega?`r\n\
`+(5`- - 1,4`-) = `+23,04 $h,8 m.`s g8b|Rec`;proco do teorem$< Pit`2gora$0 aplica`)`7|reciproco do teorem$<\
 pitagoras verificar ~7~I `nngulo dista`M ~m ~2 `k ~V espacial ternos pitagori~a&3att.pit|8|n`_`a `/ 8.`K `q\
 $'`2goras (rec`;proco)`v$- Verificar se um ~7`! `( &<`! $Ss la`O.`3 a ~B`M ~m ~2 `k do plano.`3 a ~V `A\
 `Vlelep`;pedo.`u$- Rec`;proco: s#E `y ~H ao `I `( a ~' `O `Is `O &L, o ~7`! `( &<`!.$- Maior`- > ~':\
 obtus`!; `y`- < ~': acut`!.$- Dist&9`M: d = `+((x~M - x~@)`- + (y~M - y~@)`-).$- Diagonal espacial: `+(c`- +\
 l`- + h`-).$- Ternos pitag`Xri~a: 3, 4, 5; 5, #L 13; 8, 15, 17.`? Dist&9`M ~m ~2 `k|d = `+((x~M - x~@)`- +\
 (y~M - y~@)`-)|(x~@, y~@) e (x~M, y~M): os `k|plano `J refere`Ml|(1, 2) e (4, 6): d &g|`?`< la`O de 9, 12 e\
 1#2; `k A(1, 2) e B(7, 10).`1 ver s#E ~7`! `( &<`! e ~s AB.`S 15`- ~W25 e 9`- + 12`- = 81 + 144 ~W25: `(\
 &<`!.`R A#6 `+(6`- + 8`-) = `+100 $i~x O ~7`! `( &<`!; AB $i.`% 9, #L 15 `( o terno 3, 4, 5 vezes 3 `N.`t$H\
 ~7`! ~: la`O 6, 7 e 9. \xc9 &<`!?`r\n\
N`'o: 9`- = 81 e 6`- + 7`- = 85; `Jo 81 < 85, `( acut`!.`s g8c|Vetore$0 $A`)`7|$= dire$d ~Jtido `J~E norma\
 $A$d associada a um $= ~^ `A $= ~' de $=es &/&3&w|8|n`_`a `/ 8.`K `q Vetore$0 $A`)`7`v$- Caracterizar um $=\
 (dire`)`'o, ~Jtido e `J~E).$) `} $A`)`'o a `} figura.$- &'r $=e$0 usar ~^.`u$- Vetor: dire`)`'o, ~Jtido e\
 `J~E.$- Vetor A#6 B - A (~^).$- Transla`)`'`L $= (a, b): (x, y) $l ($X a, y + b).$- A $A`)`'o mant`(m `J~Es,\
 `!$0 a orienta`)`'o.$- Som$< $=es: ~'m-s$bs ~^ (regra do `Vlelogramo).`? Transla`)`'`L $= (a, b)|(x, y) $l\
 ($X a, y + b)|(a, b): ~^ do $=|no plano `J refere`Ml|A(1, 1) `J (3, 2): A'(4, 3)&3&w`? Vetor definido ~! ~2\
 `k|A#6 B - &> (x_B - x_A, y_B - y_A)|A e B: `k|AB e BA s`'o sim`(~7~a|A(1, 2) e B(4, 6): A#6 (3, 4)|`?`<\
 ~7`! A(1, 1), B(4, 1), C(2, 3) #E $= u = (3, 2).`1 &/ pela $A`)`'`L $= u.`S A'(1 + 3, 1 + 2) = A'(4, 3)`R\
 B'(4 + 3, 1 + 2) = B'(7, 3)`] C'(2 + 3, 3 + 2) = C'(5, 5)~x A'(4, 3), B'(7, 3) e C'(5, 5).`% A#6 A'B' &_\
 `N.`t`U `( o $= ~1 leva P(2, -1) a Q(5, 3)?`r\n\
PQ = (5 - 2, 3 - (-1)) = (3, 4); `J~E 5.`s g8d|Isome~7as: $m`7 e &a`)`7|isome~7a $mao eix`L $mao &a$d ~% `^\
 meia-volta #B~7a axial #B~7$< &a$d &/ ~^&3&w|8|n`_`a `/ 8.`K `q Isome~7as`v$) $m`7 e &a`)`7 a $F.~A as &e `J\
 ~^.`o #B~7as `Aa figura.`u$- Isome~7a: mant`(m `J~E$0 `!s (a &/ `( congruente).$- Reflex`'o no &u Ox: (x,\
 -y); no &u Oy: (-x, y); na `n y = x: (y, x).$- Rota`)`'`L 90`8 (~Jtido positivo) de ~% O: (-y, x).$-\
 Rota`)`'`L 180`8 de ~% O: (-x, -y) (meia-volta).$- A $m`'o troca a orienta`)`'o; $A`)`7 e &a`)`7\
 mant`Bm-na.`? Rota`)`'`L 90`8 de ~% O|(x, y) $l (-y, x)|~Jtido positivo (#G`2rio ao `O ponteiros)|~% $}|(4,\
 1) $l (-1, 4)&3&w`? Reflex`7 no$0ixos|Ox: (x, -y); Oy: (-x, y)|eix`L $m`'o|o &u `( &de$!~7z de ~} $u\
 [PP']|(2, 3) em Ox: (2, -3)&3&w`?`< o $, P(4, 1).`1 imagens ~! $m`'o em Oy, &a`)`'`L 90`8 e meia-volta (~%\
 O).`S Reflex`'o em Oy: (-4, 1).`R Rota`)`'`L 90`8: (-1, 4).`] Meia-volta: (-4, -1).~x (-4, 1), (-1, 4) e\
 (-4, -1).`% to$c ~k`'o a `+17 `: 4,12 de O, `Jo P `N.`t\n\
`m$0ixo~P #B~7a ~: um hex`2~y $k?`r\n\
Tem 6 &u~P #B~7a e #B~7$< &a`)`'`L $L 6.~< 1|g8e1|Diagonal `A campo&3att.pit|g8a`6 um camp`L futebol ~: 105 m\
 ~! 68 m. `m ~U a ~V?`C`)`'o:`S d`- $i5`- + 68`- $j1 025 + 4624 $j5 649`R d = `+15 649 `: 125,1 m`4 ~N 125\
 m.`5`)`'o: `( $J curto atravessar na ~V do ~1 $Ss la`O (173 m).`. ~'r os la`O sem o$0levar ao `I.~<\
 2|g8e2|Altura `A ~7`! equil`2tero&3att.pit|g8a`6 um ~7`! equil`2tero ~: 6 $2 ~H. ~; a `c $b `2~Q\
 (`Ze$0xatos).`C`)`'o:`S A `c $E a ~] ao meio: ~Zs 3 e h; `b 6.`R h = `+(6`- - 3`-) = `+27 &_`+3 `: 5,20 &x`]\
 &A~Q = 6 `, 3`+3 $3 &f`+3 `: 15,59 cm`-.`4 h &_`+3 cm e &> 9`+3 cm`-.`5`)`'o: em &Fl, h = l`+3 $3.`. usar o\
 ~H $a (6) `Jo ~Z.~< 3|g8e3|Uma &a`)`'`L ~% &;~1r&3&w|g8d`6 roda o $, P(4, 1) 90`8 (~Jtido positivo) em torno\
 do ~% C(1, 1).`C`)`'o:`S Vetor CP = (4 - 1, 1 - 1) = (3, 0).`R Rodar 90`8: (a, b) $l (-b, a), ~K (3, 0) $l\
 (0, 3).`] P' = C + (0, 3) = (1, 4).`4 P'(1, 4).`5`)`'o: CP = CP' &_: a &a`)`'o mant`(m a ~B`M ao ~%.`. rodar\
 P em torno da origem.\n\
"
 return _ns('D', _dz(D))


_F['p_g8'] = _m_p_g8


def _m_p_g9():
 D = "~{~| 6$@~7$? (9.`K ~o`s g9a|Circunfer`B`M: `!$0 ar~a|`fe`M ~I ao ~% ~I ~( &O angul`L $u ve$P no interior\
 exterior semi`fe`M quadrilatero ~( &pi~y ~(&3gtr.circ|9|n`_`a `/ 9.`K `q Circunfer`B`M (`!s)`v$- &J `!s ao\
 ~% e ~(s `J os ar~a.`3 `!s `J v`($P dentro e fora da `f`B`M.~A as propriedades `O quadril`2teros ~(s.`u$- `e\
 ao ~% = &O correspondente.$- `e ~( = $n do &O (o `! de $u tamb`(m).$- Inscrito n`} semi`f`B`M: `( &<o\
 (90`8).$- V`($P #F~' `O ar~a; no exterior: semi`i`)a.$- Quadril`2tero ~(: `!s ~hs #:es.`? `e ~(|`9 = &O\
 $3|&O: `^ do &O `Jpreendido ~m os la`O|v`($P na `f`B`M|arc`L 80`8: `9 $h0`8&3gtr.circ`? `e~P v`($P interior\
 e exterior|interior: (a + b)/2; exterior: (a - b)/2|a, b: ar~a `Jpreendi`O (a o `y)|v`($P dentro ou fora do\
 c`;#=|ar~a 100`8 e 40`8: 70`8 e 30`8&3gtr.circ`?`< n`} `f`B`M, o &O AB ~U 80`8.`1 `! ao ~% AOB, `! ~( AVB #E\
 outro `! ~(.`S Ao ~%: AO#6 80`8.`R Inscrito `J o v`($P no outro &O: 80`8 $3 $h0`8.`] Com o v`($P no &O AB:\
 (360`8 - 80`8) $3 $j40`8.~x 80`8, 40`8 e 140`8.`% 40`8 + 140`8 $j80`8 (quadril`2tero ~() `N.`t$H `! ~( ~U\
 35`8. `m ~U o &O correspondente?`r\n\
2 `, 35`8 = 70`8.`s g9b|Raz`7 ~7~ym`(~7cas `A `! &1~7~yme~7a ~Jo ~a~Jo #, #Koes ~7~yme~7cas ~I agudo ~Z ~h ~>\
 `b ~7~I `nngulo #I~Hra&3atr.~7|9|n`_cleo|g8a:$'`2goras;g7e:Semelhan`)$< $F|f1b:Trabalho `Aa for`)a `x|AE `/\
 9.`K `q Tri~yme~7a`v$- Definir ~Jo, ~a~Jo e #, `A `! agudo.`3 #K`7 ~7~ym`(~7cas $^ ~7`! &<`!.~A a #I~Hra `V\
 obter #K`7 e `!s.`u$- ~J `9 = ~Z ~h / `b.$- ~a `9 = ~Z ~> / `b.$- tg `9 = ~Z ~h / ~Z ~>.$- #+ `9 agudo: 0 <\
 ~J `9 < 1 e 0 < ~a `9 < 1.$- `e $9 da #K`'o: ~J`T#>, ~a`T#>, tg`T#> (em &Ds).$- As #K`7 s`X dependem do `!\
 (~7`!s `[).`? Seno, ~a~Jo e #,|~J `9 = op / hip; ~a `9 &Zdj / hip; tg `9 = op / adj|`9: `! &1~7`! &<`!|la`O\
 3, 4, 5: ~J `9 = 0,6&3atr.~7`?`< `} es~} de 5 m ~k`2 en~atada a `} &,ede, `J o p`( a 1,5 m da &,ede.`1 `! da\
 es~} `J o ch`'o e `c a ~1 chega.`S ~a `9 $j,5 / 5 = 0,3.`R `9 = ~a`T#> 0,3 `: 72,5`8.`] Altura: `+(5`- -\
 1,5`-) = `+22,75 `: 4,77 m.~x `9 `: 72,5`8 $b es~} chega a ~N 4,77 m.`% 5 `, ~J 72,5`8 `: 4,77 m `N.`t\n\
O ~Z ~h a `9 ~U 6 $b `b 10. `m $Q ~J `9?`r\n\
~J `9 = 6 / 10 = 0,6.`s g9c|$fr ~7`!s &<`!s|~S ~7~I `nngulo angul`L eleva$d angul`L depressao `c &l dista`Ms\
 inacessiveis rampa ${&3atr.~7|9|n`_cleo|g9b:Raz`7 ~7~ym`(~7cas `A `! &1f1d:For`)as conservativa$0\
 conserva`)`'o da energi&dec&9nica|AE `/ 9.`K `q Tri~yme~7a (${)`v`3 la`O e `!s `A ~7`! &<`!.`l ${ `J `!~P\
 eleva`)`'o e de depress`'o.$- Escolher a #K`'o ~7~ym`(~7ca ad~3da.`u$- Escolh$b #K`'o ~1 liga o ~1 sabes ao\
 ~1 procuras.$- Oposto = `b `, ~J `9; ~> = `b `, ~a `9.$- Oposto = ~> `, tg `9.$- Eleva`)`'o: acima da\
 horizontal; depress`'o: abaixo.$- Os ~2 `!s agu`O ~'m 90`8.`? La`O $9 `A `!|~h = hip `, ~J `9; ~> = hip `,\
 ~a `9; ~h &Zdj `, tg `9|`9: `! &1~7`! &<`!|~> 12 e `9 &_5`8: ~h `: 8,40&3atr.~7`?`< a &l `Aa `2&= ~U 12 m #D\
 o Sol ~k`2 a 35`8 de eleva`)`'o.`1 `c da `2&=.`S tg 35`8 = `c / 12.`R Altura $+ `, tg 35`8 `: 8,40 m.`] Do\
 topo $p ponta da &l: 12 / ~a 35`8 `: 14,65 m.~x A `2&= ~: ~N 8,4 m.`% 8,40`- + 12`- `: 214,6 `: 14,65`-\
 `N.`t$Ha es~} de 4 m faz 60`8 `J o ch`'o. A ~1 `c chega?`r\n\
4 `, ~J 60`8 ~W`+3 `: 3,46 m.`s g9d|Rela`)`7 ~m as #K`7 e `Ze$0xatos|fo$y fundamental ~J^2 + ~a^2 $j tg = ~J\
 / ~a `Ze$0xatos 30 45 60 ~Is `J#?&3atr.rad|9|n`_cleo|g9b:Raz`7 ~7~ym`(~7cas `A `! &1|AE `/ 9.`K `q\
 Tri~yme~7a (rela`)`7)`v~A ~J`- `9 + ~a`- `9 $j e tg `9 = ~J `9 / ~a `9.$- Conhecer os `Ze$0xato~P 30`8, 45`8\
 e 60`8.$- &J as #K`7 de `!s `J#?.`u$- ~J`- `9 + ~a`- `9 $j; tg `9 = ~J `9 / ~a `9.$- ~J `9 = ~a (90`8 -\
 `9).$- ~J 30`8 = ~a 60`8 $j/2.$- ~J 60`8 = ~a 30`8 = `+3/2.$- ~J 45`8 = ~a 45`8 = `+2/2; tg 45`8 $j.`? F`X$y\
 fundamental|~J`- `9 + ~a`- `9 $j|`9: `! &1&;~1r `! &1~J `9 = 0,6: ~a `9 = 0,8&3atr.rad`? Tangente|tg `9 = ~J\
 `9 / ~a `9|`9: `! &1~a `9 ~L 0|0,6 / 0,8 = 0,75&3atr.rad`?`< `9 `( agudo e ~J `9 = 0,6.`1 ~a `9 e tg `9.`S\
 ~a`- `9 $j - 0,36 = 0,64.`R ~a `9 = 0,8 (positivo, ~!~1 `9 `( agudo).`] tg `9 = 0,6 / 0,8 = 0,75.~x ~a `9 =\
 0,8 e tg `9 = 0,75.`% 0,6`- + 0,8`- $j `N.`t\n\
`m $Q ~J 30`8 + ~a 60`8?`r\n\
1/2 + 1/2 $j.`s g9e|S`Xli`O: `2~Q$0 $Vs|$V a~Q lateral a~Q #9 prisma &V piramide cone esfera &F~7z apo~:a\
 capacidade litros&3sol.sol|9|n`_`a `/ 9.`K `q Medida (s`Xli`O)`v`3 $V~P prismas, &Vs, pir&9mides, cone$0\
 esferas.`3 `2~Qs laterai$0 totais.`3 `} &E $9 do $V.`u$- Prisma e &V: V = `2~Q da ~] `, `c.$- Pir&9mide e\
 cone: V = `2~Q da ~] `, `c / 3.$- Esfera: V $h/3 `>r`j; `2~Q $h`>r`-.$- Cone: &F~7z g = `+(r`- + h`-); `2~Q\
 lateral = `>rg.$- 1 dm`j $j L; 1 cm`j $j mL.`? Volume da pir&9mide e do cone|V = Ab `, h / 3|Ab: `2~Q da\
 ~];h: `c|a `c `( $R&B $p ~]|cone r &_, h $h: V $+`>&3sol.sol`? Volume e `2~Q da esfera|V $h/3 `> r`j; A $h\
 `> r`-|r: $z|esfera|r &_: V &_6`>&3sol.sol`?`< um cone ~: 3 $2 $z e 4 $2 `c.`1 $V, &F~7z e `2~Q #9.`S V = `>\
 `, 3`- `, 4 / 3 $+`> `: 37,70 cm`j.`R g = `+(3`- + 4`-) &g &x`] At = `> `, 3`- + `> `, 3 `, 5 ~W4`> `: 75,40\
 cm`-.~x V $+`> cm`j e At ~W4`> cm`-.`% o &V `J a $. ~] e `c ~: 36`>, o ~7pl`L 12`> `N (3 vezes).`t`U `( o $V\
 `Aa esfera `J 3 $2 $z (`Z exato)?`r\n\
4/3 `, `> `, 27 &_6`> cm`j.`s g9f|Lugares geom`(~7~a|lugar geome~7co me$!~7z bisse~7z `fe`M &{ `k a $.\
 dista`M constru&| regua e `Jpasso||9|n`_`a `/ 9.`K `q Lugares geom`(~7~a`v`o &de$!~7z, a bisse~7z $b `f`B`M\
 `Jo lugares geom`(~7~a.~j lugares geom`(~7~a `J r`(gua e `Jpasso.`l ${ `J `k &{s.`u$- Circunfer`B`M: `k a `}\
 ~B`M r `A ~%.$- Me$!~7z de [AB]: `k $p $. ~B`M de A e de B.$- Bisse~7z `A `!: `k $p $. ~B`M `O ~2 la`O.$-\
 C`;#=: `k a ~B`M ~? r do ~%.$- O circun~% `A ~7`! ~k`2 nas tr`Bs me$!~7zes.`? Me$!~7z|P&> PB|A, B: extremos\
 do $u|`n $R&B a [AB] no $, m`(dio|A(0, 0) e B(4, 0): `| 2|`?`< h`2 ~) casa$0m A(0, 0) e B(6, 0). Quer-se um\
 poste $p $. ~B`M $c ~).`1 onde pode ficar o poste? Pode ficar no &u Oy?`S Os `k &{~P A e B ~k`'o n&de$!~7z\
 de [AB].`R Ponto m`(dio: (3, 0); &de$!~7z `( a `n `| 3.`] No &u Oy (`| 0) n`'o h`2 `k d&de$!~7z.~x O poste\
 ~: de ~kar na `n `| 3; ~! exemplo, P(3, 4).`% P&> `+(9 + 16) &g = PB `N.`t\n\
Que lugar geom`(~7co #/m os `k a 2 cm `A $, O?`r$Ha `f`B`M de ~% O e $z 2 cm ($R`;~R 4`> `: #L57 cm).~<\
 1|g9e1|`e n`} semi`f`B`M&3gtr.circ|g9a`6 [AB] `( um di&9~R e C um $, da `f`B`M. O `! CAB ~U 35`8. `m ~U o `!\
 ABC?`C`)`'o:`S O `! ACB ~k`2 ~( n`} semi`f`B`M: ~U 90`8.`R ABC $j80`8 - 90`8 - 35`8 &g5`8.`4 55`8.`5`)`'o: o\
 ~7`! ABC `( &<`! em C.`. pensar ~1 o `! &<o ~k`2 em A ou em B.~< 2|g9e2|Altura `A pr`(dio&3atr.~7|g9c`6 a 30\
 m `A pr`(dio, o topo v`B-se `J um `! de eleva`)`'`L 50`8. Os olhos ~k`'o a 1,6 m do ch`'o~- `( a `c do\
 pr`(dio?`C`)`'o:`S tg 50`8 = h / 30, ~Jdo h a `c acima `O olhos.`R h &_0 `, tg 50`8 `: 35,75 m.`] Altura do\
 pr`(dio: 35,75 + 1,6 `: 37,35 m.`4 ~N 37,4 m.`5`)`'o: sem a `c `O olhos, $Z ficava 1,6 m curto.`. usar ~J\
 50`8 (o dado `( o ~Z ~>).~< 3|g9e3|Ge~H $^ cone&3sol.sol|g9e`6 um cone de bolacha ~: 3 $2 $z e 10 $2 `c. Por\
 cima lev&deia esfer$< ge~H `J $8 $z~- `( o $V #9?`C`)`'o:`S Cone: `> `, 3`- `, 10 / 3 &_0`> `: 94,2#2`j.`R\
 Meia esfera: 4/3 `, `> `, 27 $3 $j8`> `: 56,5#2`j.`] Total: 48`> `: 150,8 cm`j.`4 ~N 151 cm`j (#7\
 L).`5`)`'o: 48`> $j50,8 cm`j `( ~N #7 L.`. es~1cer o 1/3 no $V do cone.\n\
"
 return _ns('D', _dz(D))


_F['p_g9'] = _m_p_g9


def _m_p_n7():
 D = "~{~| 5&X N`_~b (7.`K ~o`s n7a|N`_~b `Q: `J`Vr e $[r|nu~b `Q ~6 $Ks #B~7co `Z ab~Oto `n $^erica `J`Vr $[r $G&|\
 di~ws&3$^.$Gc&6`_`a `/ 7.`K `q N`_~b `Q`v$- Repre~Jtar `0s `Q na `n $^`(rica.~A o sim`(~7co #E `Z ab~Oto.$-\
 Com`Vr e $[r `0s `Q.`u$- Racional: &G `Jo a/b, `J a e b ~6 e b ~L 0.$- Sim`(~7c`L 3: -3. Valor ab~Oto:\
 `g-3`g &_ (~B`M a 0).$- Na `n $^`(rica, o `y ~k`2 $J $p direita.$- Entre $Ks, `( `y `L &7 `Z ab~Oto: -2 >\
 -5.$- Fra`)`7: reduz ao mesm`Lnominador ou $w a d`;~w.`? Valor ab~Oto|`ga`g &Z s$b ~c 0; `ga`g = -a s$b <\
 0|a: `0 racional|~B`M d$b a 0 na `n|`g-3,5`g &_,5|`? Com`Vr $G`)`7|a/b < c/d `h a `, d < c `, b|b e d\
 positivos|`J o mesm`Lnominador, `J`V os $^eradores|2/3 < 3/4 ~!~1 8 < 9&3$^.$Gc`?`< -3/4, 0,7, -0,8 e 2/3.`1\
 $[r do &7 `V o `y.`S Em d`;~w: -3/4 = -0,75 e 2/3 `: 0,667.`R Negativos: -0,8 < -0,75, ~!~1 0,8 > 0,75.`]\
 Positivos: 2/3 `: 0,667 < 0,7.~x -0,8 < -3/4 < 2/3 < 0,7.`% `O $Ks, -0,8 ~: o `y `Z ab~Oto.`t`U `( `y: -5/2\
 ou -2,4?`r$-2,4: ~k`2 $J $Rt`L 0, ~!~1 `g-5/2`g ~W,5 `( `y do ~1 2,4.`s n7b|O$Ra`)`7 `J `0s `Q|$G&| adi$d\
 subtra$d `H$d divisao &k prioridade $c o$Ra&| &,enteses sinais nu~b $Ks ~8&3$^.$Gc&6`_`a `/ 7.`K `q N`_~b `Q\
 (o$Ra`)`7)`v$- &'r e #- $G`)`7 `J o ~8 `O ~+es.$- `{r e ~n $G`)`7.$- Respeitar a prioridade $c o$Ra`)`7 $bs\
 &e `O sinais.`u$- &'r: reduz ao mesm`Lnominador e ~' os $^eradores.$- `{r: $^erador `, $^erador e ~+ `,\
 ~+.$- Dividir: `H $S &k do divisor.$- Sinais: (+)(+) e (-)(-) d`'o +; (+)(-) d`2 -.$- Ordem: &,`Bnteses,\
 $g`B`Ms, `, e :, ~! fim + e -.$- $o $Z ($G`)`'o irredut`;vel).`? Som$< $G`)`7|a/b + c/d = (ad + cb) / (bd)|b\
 e d `ite~P 0|melhor `J o ~8 `O ~+es|1/4 + 1/6 &_/12 + 2/12 &g/12&3$^.$Gc`? Divis`'`L $G`)`7|a/b : c/d &Z/b\
 `, d/c|c/d `ite de 0|`H-se $S &k|2/3 : 4/5 ~W/3 `, 5/4 &g/6&3$^.$Gc`?`< 1/2 + 3/4 `, (2/3 - 1).`1 ~s o `Z\
 exato.`S Par`Bnteses: 2/3 - 1 ~W/3 - 3/3 = -1/3`R `{`)`'o: 3/4 `, (-1/3) = -3/12 = -1/4`] Adi`)`'o: 1/2 +\
 (-1/4) ~W/4 - 1/4 $j/4~x O `Z `( 1/4 = 0,25.`% na #I~Hra, 0,5 + 0,75 `, (-0,333...) `: 0,25.`t\n\
~; 2/3 : 4/9.`r\n\
2/3 `, 9/4 $j8/12 &_/2.`s n7c|Pot`B`M~P `@ natural|$ge`M ~] `@ `I cubo $ge`M~P 10 ~X quociente de $ge`Ms $.\
 ~] mesmo `@ $ge`M de $ge`M ~] negativa&3$^.$g&6`_`a `/ 7.`K `q Pot`B`Ms`v`3 $g`B`M~P ~] racional e `@\
 natural.$) as &e $c $g`B`Ms.$- Saber ~q `Aa $g`B`M de ~] negativa.`u$- a^n &Z `, a `, ... `, a (n ~p); a#>\
 &Z; a#< $j (a ~L 0).$- Mesma ~]: a^n `, a^m ~' os `@s; a^n : a^m subtrai-os.$- Mesmo `@: a^n `, b^n = (a `,\
 b)^n.$- Pot`B`M de $g`B`M: (a^n)^m `H os `@s.$- Base negativa: `@ &, d`2 positivo; `;m&, d`2 $K.$- (-2)`w\
 $j6, mas -2`w = -16.`? Produto `J a $. ~]|a^n `, a^m &Z^(n + m)|a: ~];n e m: `@s naturais|a $. ~]|2`j `, 2`w\
 ~W&@ $+8&3$^.$g`? Pot`B`M de $g`B`M|(a^n)^m &Z^(n `, m)|n e m: `@s|`H$D `@s|(3`-)`j &_&^ = 729&3$^.$g`?`<\
 2`j `, 2`w : 2~d e (-3)`j + (-1)#>#<.`1 ~s as ~) $/`7.`S 2`j `, 2`w ~W&@; 2&@ : 2~d ~W`- $h`R (-3)`j = -27\
 (`@ `;m&,: $K).`] (-1)#>#< $j (`@ &,: positivo).$r -27 + 1 = -26~x 4 e -26.`% 8 `, 16 : 32 $h.`t\n\
$q `Jo `} s`X $g`B`M: 5`j `, 2`j.`r\n\
(5 `, 2)`j $i00, ~/ 10`j.`s n7d|Raiz ~_ e &j c`_bica|&j ~_ &j cubica `I $Rfeito cubo $Rfeito &j `Aa $G$d\
 enquadrar ~m ~6&3~Q.rad&6`_`a `/ 7.`K `q Ra`;zes ~_$0 c`_bicas`v`o `I$0 cubos $Rfeitos.`3 ra`;zes ~_$0\
 c`_bicas.$- Enquadrar `} &j ~m ~2 ~6.`u$- `+a `( o `0 positivo cujo `I `( a: `+49 = 7.$- &!a `( o `0 cujo\
 cubo `( a: &!64 $h e &!(-8) = -2.$- Quadra`O $Rfeitos: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100...$- Raiz `Aa\
 $G`)`'o: `+(a/b) = `+a / `+b.$- Se n`'o `( `I $Rfeito, enquadra: 6`- < 40 < 7`-, ~K 6 < `+40 < 7.`? Raiz\
 ~_|`+a = b `h b`- &Z e b ~c 0|a ~c 0|s`X `V `0s n`'o $Ks|`+144 $+&3~Q.rad`? Raiz c`_bica|&!a = b `h b`j\
 &Z|a: &;~1r `0 racional|existe `V $Ks|&!(-27) = -3&3~Q.rad`?`< `+(9/25), &!(-125) e `+40.`1 ~s as ~)\
 primeira$0 enquadrar `+40.`S `+(9/25) = `+9 / `+25 &_/5`R &!(-125) = -5, ~!~1 (-5)`j = -125.`] 6`- &_6 < 40\
 < 49 = 7`-, ~K 6 < `+40 < 7.~x 3/5, -5 e 6 < `+40 < 7.`% `+40 `: 6,32 na #I~Hra.`t\n\
Entre ~1 ~6 &h ~k`2 `+70?`r\n\
Entre 8 e 9, ~!~1 8`- = 64 < 70 < 81 &f`- (`+70 `: 8,37).`s n7e|Fatores primos, ~v e ~8|nu~b primo~P`Jposi$d\
 em ~p primos maximo divisor `Jum minimo multiplo `Jum mdc mmc ~5 $G&| divisores\
 multiplos&3$^.mdc|6|revis`'o|||AE `/ 6.`K `q N`_~b naturais (revis`'o `V o 7.`K ~o`v$- De`J~! um `0 em ~p\
 primos.`3 o ~v #E ~8 $9 `O ~p.~A o ~v `V ~5 $G`)`7.`u$- Primo: s`X ~: ~2 divisores, 1 e ele pr`Xprio (2, 3,\
 5, 7, 11...).$- De`J~!: $E $Ss primos, do &7 `V o `y.$- ~v: ~p `Juns, ~} um `J o &7 `@.$- ~8: to`O os ~p, ~}\
 um `J o `y `@.$- ~v(a, b) `, ~8(a, b) &Z `, b.`? ~v e ~8 $Ss ~p|~v: `Juns, &7 `@; ~8: to`O, `y `@|a e b: `0s\
 naturais|de`J~! $: em ~p primos|60 e 72: ~v #L ~8 360&3$^.mdc`?`< 60 e 72.`1 ~v, ~8 e ~5 60/72.`S 60 ~W`- `,\
 3 `, 5 e 72 ~W`j `, 3`-.`R ~v ~W`- `, 3 $+`] ~8 ~W`j `, 3`- `, 5 &[$r 60/72 = (60 : 12) / (72 : 12) &g/6~x\
 ~v $+, ~8 &[ e 60/72 &g/6.`% 12 `, 360 $h320 = 60 `, 72.`t\n\
Dois autocarros saem juntos $ps 8 h; um pass$< 12 em 12 min #E outr`L 18 em 18 min. Quando voltam a sair juntos?`r\n\
Ao fim de ~8(#L 18) &_6 min, $ps 8 h 36 min.~< 1|n7e1|Tem$Raturas negativas||n7a`6 $^ $! de inverno, as\
 ~:$Raturas m`;nimas foram -3,5 `8C em Bragan`)a, -1 `8C na Guarda e 2,5 `8C em Lisboa. Ordena-a$0 #Ila a\
 `i`)a ~m a `y $b &7.`C`)`'o:`S Na `n $^`(rica: -3,5 < -1 < 2,5.`R &i`)a: 2,5 - (-3,5) ~W,5 + 3,5 = 6 `8C.`4\
 -3,5 < -1 < 2,5; a `i`)a `( de 6 `8C.`5`)`'o: #- um $K `( ~'r &su sim`(~7co.`. pensar ~1 -3,5 `( `y do ~1 -1\
 ~! ter 3,5 > 1.~< 2|n7e2|#.`'o `J $G`)`7 e $g`B`Ms&3$^.$Gc|n7b`6 #Ila o `Z exat`L (1/2)`- - 2/3 :\
 (-4).`C`)`'o:`S Pot`B`M: (1/2)`- $j/4`R Divis`'o: 2/3 : (-4) ~W/3 `, (-1/4) = -1/6`] 1/4 - (-1/6) &_/12 +\
 2/12 &g/12`4 5/12.`5`)`'o: $: $g`B`Ms, depois `, e :, ~! fim + e -.`. es~1cer ~1 ~n ~! -4 `( `Hr ~! -1/4.~<\
 3|n7e3|Re&,tir um &5&3$^.$Gc|n7b`6 $^ &5, 2/5 s`'o relvado e 1/3 do r~ko `( horta. O r~kante, 120 m`-, `(\
 pomar~- `( a `2~Q do &5?`C`)`'o:`S R~k`Lpois do relvado: 1 - 2/5 &_/5`R Horta: 1/3 de 3/5 $j/5 do &5.`]\
 Pomar: 1 - 2/5 - 1/5 ~W/5 do &5.$r 2/5 do &5 s`'o 120 m`-, ~K o &5 ~: 120 : 2/5 &_00 m`-.`4 300 m`-.`5`)`'o:\
 \"1/3 do r~ko\" `( `} $G`)`'o `Aa $G`)`'o: `H-se.`. ~'r 2/5 + 1/3 `Jo s$bmbas fossem do &5 todo.\n\
"
 return _ns('D', _dz(D))


_F['p_n7'] = _m_p_n7


def _m_p_n8():
 D = "~{~| 3&X N`_~b (8.`K ~o`s n8a|Pot`B`M~P `@ $a|$ge`M `@ $K `@ zero &k &e $c $ge`Ms $G&| $ge`M~P\
 10&3$^.$g|8|n`_`a `/ 8.`K `q Pot`B`M~P `@ $a`v`3 $g`B`Ms `J `@ $K ou nulo.$) as &e $c $g`B`Ms `J `@s ~6.~=\
 um `0 `Jo $g`B`M de ~] 10.`u$- a#< $j (a ~L 0).$- Expoente $K: a`T#; $j / a^n; ~! exemplo, 2`T`j $j/8.$-\
 (a/b)`T#; = (b/a)^n: inverte-s$b ~] e ~q do `@.$- As &e $c $g`B`Ms $Qm `V `@s ~6.$- 10`T`j = 0,001; 10`T#> =\
 0,1.`? Expoente $K|a`T#; $j / a^n|a ~L 0;n: $a positivo|a ~] n`'o pode ser 0|5`T`- $j/25&3$^.$g`? Base\
 $Gcion`2ria `J `@ $K|(a/b)`T#; = (b/a)^n|a e b `ite~P 0|inverte-s$b ~]|(2/3)`T`- &f/4&3$^.$g`?`< 2`T`j `,\
 2~d e (2/3)`T`- `, (3/2)`j.`1 ~s as ~) $/`7.`S Mesma ~]: 2`T`j `, 2~d ~W`T`j\u207a~d ~W`- $h`R (2/3)`T`- =\
 (3/2)`- &f/4`] Mesma ~] 3/2: (3/2)`- `, (3/2)`j = (3/2)~d ~W43/32~x 4 e 243/32 (`: 7,59).`% 0,125 `, 32 $h `N.`t\n\
$q 0,0001 `Jo $g`B`M de ~] 10.`r\n\
1 / 10 000 $j/10000, ~/ 10`T`w.`s n8b|Nota`)`'~G`;fica|notaca~Gifica &U $L de grandeza $ge`M de 10 `Hr ~n ~'r\
 nu~b muito grandes muito pe~1nos&3~Q.ncie|8|n`_cleo||q1b:Tamanho `O `2tomos: orden~P grandeza e escalas|AE\
 `/ 8.`K `q Nota`)`'~G`;fica`v~= `0$0m nota`)`'~G`;&}$- `{r e ~n `0$0m nota`)`'~G`;&}$- &'r e #-, &8ando as\
 $g`B`M~P 10.`u$- Nota`)`'~G`;fica: a `, 10^n, `J 1 ~? a < 10 e n $a.$- V`;rgula `V a es~1rda: o `@ #); `V a\
 direita, diminui.$- `{r: `H$D `0$0 ~'$D `@s.$- Dividir: $E$D `0$0 subtrae$D `@s.$- &'r: $: a $. $g`B`M de\
 10.$- No fim, acerta a `V ficar ~m 1 e 10.`? Nota`)`'~G`;fica|a `, 10^n|1 ~? a < 10;n: $a|`0s positivos (`J\
 sinal, -a `, 10^n)|0,00052 &g,2 `, 10`T`w&3~Q.ncie`? Produto $x`)`'~G`;fica|(a `, 10^n)(b `, 10^m) = (a b)\
 `, 10^(n + m)|a, b: &Us|acertar a &U no fim|(3 `, 10~d)(4 `, 10`T`-) $j,2 `, 10`w&3~Q.ncie`?`< &> 3 `, 10~d\
 e B $h `, 10`T`-.`1 A `, B e A : B $x`)`'~G`;&}`S A `, #6 (3 `, 4) `, 10~d`T`- $+ `, 10`j $j,2 `, 10`w`R A :\
 #6 (3 : 4) `, 10~d\u207a`- = 0,75 `, 10&@ = 7,5 `, 10&^~x A `, B $j,2 `, 10`w e A : #6 7,5 `, 10&^.`% 300\
 000 `, 0,04 $+ 000 `N.`t\n\
$q 0,000 038 $x`)`'~G`;&}`r\n\
3,8 `, 10`T~d ($Q 0,000038).`s n8c|D`;~ws &0$0 ~zs ~i`Xdicas|di~w &0 di~w ~z ~iodica ~iodo $G$d &F~7z\
 converter $G$d em di~w ~+ 2 e 5&3$^.dec|8|n`_`a `/ 8.`K `q N`_~b `Q (d`;~ws)`v$- Saber se `} $G`)`'o d`2\
 d`;~w &0 ou ~i`Xdica.~= `} d`;~w ~i`Xdica `J $R`;odo.$- En#Gar a $G`)`'o &F~7z `Aa d`;~w ~i`Xdica.`u$-\
 Fra`)`'o irredut`;vel `J ~+ s`X `J ~p 2 e 5: d`;~w &0.$- Outros ~p n`Lnominador: d`;~w ~z ~i`Xdica.$- 1/3\
 d`2 0,333..., ~1 se &z 0,(3); o $R`;odo `( 3.$- Fra`)`'o &F~7z: `H d ~! $g`B`M~P 10 e subtrai `V o\
 $R`;od`Lsa&,ecer.$- To$c as d`;~ws &0$0 ~i`Xdicas s`'o `0s `Q.`? Fra`)`'o &F~7z ($R`;od`L k algarismos)|10^k\
 d - d = &,te inteira (sem d`;~w ~z)|d: d`;~w ~i`Xdica pura|`J ante$R`;odo, `H $: ~! 10|0,(36): 99d &_6, d\
 $h/11&3$^.dec`?`< d = 0,(36) $b $G`)`'o 7/12.`1 $G`)`'`L d e d`;~w de 7/12.`S 100d &_6,(36); 100d - d &_6,\
 ~K 99d &_6.`R d &_6/99 $h/11`] 7/12: 12 ~W`- `, 3 ~: o $4 3, ~K `( ~i`Xdica.$r 7 : 12 = 0,58333... = 0,58(3)\
 `: 0,583.~x 0,(36) $h/11 e 7/12 = 0,58(3).`% 4 : 11 = 0,3636... `: 0,364 `N.`t\n\
A $G`)`'o 9/40 d`2 `} d`;~w &0 ou ~i`Xdica?`r\n\
Finita: 40 ~W`j `, 5 (9/40 = 0,225).~< 1|n8e1|Massa `A `2tomo&3~Q.ncie|n8b`6 um `2tom`L hidrog`(nio ~: massa\
 1,67 `, 10`T`-&@ kg~- `( &dass$< 3 `, 10`-#< `2tomos?`C`)`'o:`S `{ as &Us: 1,67 `, 3 &g,01.`R &' os `@s: -27\
 + 20 = -7.`] Massa: 5,01 `, 10`T&@ kg.`4 ~N 5,01 `, 10`T&@ kg (0,5 mg).`5`)`'o: mesmo muit`;ssimos `2tomos\
 t`Bm `} mass&din`_scula.`. `Hr os `@$0m vez d#Es ~'r.~< 2|n8e2|&' $x`)`'~G`;fica&3~Q.ncie|n8b`6 #Ila 2,5 `,\
 10`w + 3 `, 10`j e &z $Z $x`)`'~G`;&}`C`)`'o:`S A $. $g`B`M de 10: 3 `, 10`j &G 0,3 `, 10`w.`R &': (2,5 +\
 0,3) `, 10`w ~W,8 `, 10`w.`4 2,8 `, 10`w.`5`)`'o: 25 000 + 3000 ~W8 000 `N.`. ~'r os `@s, `Jo na `H`)`'o.~<\
 3|n8e3|Fra`)`'o `Aa d`;~w `J ante$R`;odo&3$^.dec|n8c`6 &z d $j,2(5) `Jo $G`)`'o irredut`;vel.`C`)`'o:`S 10d\
 $+,(5) e 100d $+5,(5).`R Subtraindo: 100d - 10d $+5 - #L ~/ 90d $j13.`] d $j13/90`4 1,2(5) $j13/90.`5`)`'o:\
 113 : 90 $j,2555... `N.`. tratar o 2 `Jo &,te do $R`;odo.\n\
"
 return _ns('D', _dz(D))


_F['p_n8'] = _m_p_n8


def _m_p_n9():
 D = "~{~| 3&X N`_~b (9.`K ~o`s n9a|N`_~b ~Qis: `Q e ir`Q|nu~b ~Qis `Q ir`Q di~w ~z nao ~iodica &j ~_ pi `n ~Ql `Z\
 aproximado enquadramento `J`Vr&3~Q.rad|9|n`_`a `/ 9.`K `q N`_~b ~Qis`v$- #J `0s `Q de ir`Q.$- Repre~Jtar\
 ir`Q na `n ~Ql.$- Com`Vr `0s ~Qi$0 enquadr`2-los.`u$- Ra#3 d`;~ws &0s ou ~zs ~i`Xdicas.$- Ir`Q: d`;~ws ~zs\
 n`'o ~i`Xdicas (`+2, `+3, `>).$- Raiz ~_ `A `0 natural ~1 n`'o `( `I $Rfeito: irracional.$- Reais = `Q +\
 ir`Q; ~} $, da `n `( um ~Ql.$- #+ `J`Vr, usa `Zes aproxima`O ou os `Is (positivos).`? Com`Vr ra`;zes|0 ~? a\
 < b `h `+a < `+b|a, b: `0s n`'o $Ks|a &j ~_ `( crescente|`+10 < `+11&3~Q.rad`?`< os `0s 3,1(4), `>, `+10 e\
 22/7.`1 orden`2-lo$0 dizer quais s`'o ir`Q.`S 3,1(4) &_,1444... e 22/7 `: 3,1429 s`'o `Q.`R `> `: 3,1416 e\
 `+10 `: 3,1623 s`'o ir`Q.`] Ordem: `> < 22/7 < 3,1(4) < `+10.~x `> < 22/7 < 3,1(4) < `+10; ir`Q: `> e\
 `+10.`% 3,16`- `: 9,99, quase 10 `N.`t\n\
`+49 `( racional ou irracional?`r\n\
Racional: `+49 = 7.`s n9b|Radicais: ~5 #E$Rar|$v ~5 &j ~_ o$Ra&| `J $v ~'r $v `[ produt`L &jes racionalizar\
 ~+es&3~Q.rad|9|aprofundamento|||AE `/ 9.`K `q N`_~b ~Qis (aprofundamento; $v no 10.`K ~o`v$- $or ra`;zes\
 ~_s.$- &'r $v `[ e `Hr ra`;zes.$- Racionalizar um ~+ simples.`u$- `+(a `, b) = `+a `, `+b (a, b ~c 0): `+50\
 = `+(25 `, 2) &g`+2.$- S`X se ~'m $v `[: 5`+2 + 2`+2 = 7`+2.$- `+a `, `+a &Z.$- Racionalizar: 6/`+3 = (6 `,\
 `+3)/(`+3 `, `+3) ~W`+3.$- Procura o `y `I $Rfeito ~1 $E o radicando.`? Produt`L ra`;zes|`+a `, `+b = `+(a\
 b)|a, b ~c 0|serve `V ~5|`+50 = `+25 `, `+2 &g`+2&3~Q.rad`?`< `+50 + 2`+8 - `+18.`1 ~5.`S `+50 &g`+2; `+8\
 ~W`+2; `+18 &_`+2.`R 5`+2 + 2 `, 2`+2 - 3`+2 = (5 + 4 - 3)`+2.`] Resultado: 6`+2 `: 8,49.~x `+50 + 2`+8 -\
 `+18 = 6`+2.`% 7,071 + 5,657 - 4,243 `: 8,485 `N.`t\n\
$o `+12 `, `+3.`r\n\
`+36 = 6.`s n9c|Intervalo~P `0s ~Qis|~4s `n ~Ql ~4 aberto fechad&smiaberto infinito interse$d reuniao condi&|\
 &R$d disjun$d&3~Q.intv|9|n`_`a `/ 9.`K `q N`_~b ~Qis (~4s)`v~= &Rto~P `0s ~Qis `Jo ~4s.$- Repre~Jtar ~4s na\
 `n ~Ql.`3 a interse`)`'o $b reuni`'`L ~4s.`u$- [a, b]: a ~? x ~? b (fechado); ]a, b[: a < x < b (aberto).$-\
 [a, +~,[: x ~c a; ]-~,, b[: x < b. Do ~H do ~, o ~4 `( $> aberto.$- Interse`)`'o ~D B: os `0s ~1 ~k`'o nos\
 ~2 (\"e\").$- Reuni`'o $O B: os ~1 ~k`'o $S &C $^ (\"ou\").$- De~Jha os ~2 na `n `V n`'o te enganares.`?\
 Interse`)`'o e reuni`'o|$t ~D B `h $t A e $t B; $t $O B `h $t A ou $t B|A, B: ~4s|\u2229: &R`)`'o; \u222a:\
 disjun`)`'o|[-2, 5[ \u2229 ]1, +~,[ = ]1, 5[&3~Q.intv`?`< &> [-2, 5[ e #6 ]1, +~,[.`1 ~D B, $O B #Es ~6 de\
 ~D B.`S ~D #6 ]1, 5[ (1 < x < 5).`R $O #6 [-2, +~,[.`] Inteiro$0m ~D B: 2, 3 e 4 (3 `0s).~x ~D #6 ]1, 5[ e\
 $O #6 [-2, +~,[.`% a `^ de ]1, 5[ `( 5 - 1 $h.`t\n\
$q `Jo ~4: x ~c -3 e x < 2.`r\n\
[-3, 2[ (`^ 5).~< 1|n9e1|Um irracional na `n||n9a`6 `J&s marca `+2 na `n ~Ql `J r`(gua e `Jpasso?`C`)`'o:`S\
 De~Jha-se um `I de ~H 1 sobr#E $u [0, 1].`R A ~V ~U `+(1`- + 1`-) = `+2 `: 1,414 (Pit`2goras).`] Com o\
 `Jpasso no 0, roda-s$b ~V at`( $p `n.`4 o $, marcado ~: abcissa `+2.`5`)`'o: h`2 `k da `n ~1 n`'o s`'o `Q.`.\
 pensar ~1 `+2 $j,41 exatamente.~< 2|n9e2|Enquadrar `} &j&3~Q.rad|n9a`6 enquadra `+30 ~m ~2 ~6 e ~m ~)\
 d`(cimas.`C`)`'o:`S 5`- ~W5 < 30 < 36 = 6`-, ~K 5 < `+30 < 6.`R 5,4`- ~W9,16 e 5,5`- &_0,25: 5,4 < `+30 <\
 5,5.`4 5 < `+30 < 6 e 5,4 < `+30 < 5,5.`5`)`'o: `+30 `: 5,477.`. `J`Vr 30 `J 5 e 6 em vez de 25 e 36.~<\
 3|n9e3|Intervalo$0 condi`)`7&3~Q.intv|n9c`6 &> ]-~,, 3] e #6 [0, 7[. $q ~D B, $O B #Es ~6 de ~D B.`C`)`'o:`S\
 ~D #6 [0, 3]: 0 ~? x ~? 3.`R $O #6 ]-~,, 7[.`] Inteiro$0m ~D B: 0, 1, 2 e 3, ~/ 4 `0s.`4 [0, 3] e ]-~,,\
 7[.`5`)`'o: na reuni`'o basta ~kar $^ `O ~4s.`. fechar o ~4 no ~H do -~,.\n\
"
 return _ns('D', _dz(D))


_F['p_n9'] = _m_p_n9


def _m_x_a7():
 D = "~{~| 9~F (7.`K ~o`D n|a7x1|a7a|r|\n\
Na sequ`B`M 5, 9, 13, 17, ..., &; `( o term`L $L 30?`E 121`F d $h e ~f 4n + 1.`G\n\
u(30) $h `, 30 + 1 $+1.`D m|a7x2|a7a|r|`U `( o ~[ &Fl da sequ`B`M 2, 5, 8, 11, ...?~e ~f 3n + 2|~f n + 3|~f\
 3n - 1|u(n) ~Wn + 3`E 3`F d &_; u(1) ~W.`G\n\
~f 3n + (2 - 3) &_n - 1.`D n|a7x3|a7b|r|`U `( o `Z de 3x`- - 2x `V `| -2?`E 16`F (-2)`- $h.`G\n\
3 `, 4 - 2 `, (-2) $+ + 4 $j6.`D m|a7x4|a7b|r|`U `( a #/ simplifi~} de 5&+ 2) - 3x?~e 2x - 10|2$X 10|8x -\
 10|2x - 2`E 1`F 5&+ 2) &gx - 10.`G\n\
5x - 10 - 3`| 2x - 10.`D n|a7x5|a7c|r|\n\
$f 5x - 3 ~W$X 9.`E 4`F Passa 2x `V o 1.`K membro e -3 `V o 2.`K.`G\n\
3`| #L ~K `| 4.`D v|a7x6|a7c|r|\n\
A ~3`)`'o 2($X 1) ~W$X 3 `( $T`;vel.`E V`F Tira os &,`Bntese$0 reduz.`G\n\
2$X 2 ~W$X 3 d`2 0`| 1: n`'o h`2 ~O`)`'o, `( $T`;vel.`D n|a7x7|a7d|r|\n\
x e y s`'o di`n~T~!cionais; `V `| 4, y $i. `m $Q y `V `| 7?`E 17,5`F k = y / x.`G\n\
k $i / 4 ~W,5 e y ~W,5 `, 7 $j7,5.`D n|a7x8|a7e|r|$H telem`Xvel &Q 250 `W sem IVA. `m &Q `J IVA de 23%?`E\
 307,5`F `{ ~! 1,23.`G\n\
250 `, 1,23 &_07,50 `W.`D n|a7x9|a7e|r|$H bilhete passou de 12 `W `V 9 `W~- foi a varia`)`'o $R#% (em %)?`E\
 -25`F (novo - ~l) / ~l `, 100.`G\n\
(9 - 12) / 12 `, 100 = -25%: diminuiu 25%.\n\
"
 return _ns('D', _dz(D))


_F['x_a7'] = _m_x_a7


def _m_x_a8():
 D = "~{~| 9~F (8.`K ~o`D m|a8x1|a8a|r|`U `( `L~Jvolviment`L &+ 4)`-?~e x`- - 16|x`- - 8$X 16|x`- + 16|x`- - 4$X\
 16`E 2`F (a - b)`- &Z`- - 2ab + b`-.`G\n\
x`- - 2 `, 4$X 16 = x`- - 8$X 16.`D n|a8x2|a8a|r|`U `( o `Z de (3$X 1)(3x - 1) `V `| 2?`E 35`F \xc9 `} `i`)$<\
 `Is: 9x`- - 1.`G\n\
9 `, 4 - 1 &_5.`D m|a8x3|a8b|r|`U `( a $4iza`)`'`L 3x`- - 12?~e (3x - 2)($X 6)|3&+ 2)($X 2)|3&+ 2)`-|3x&+\
 4)`E 2`F Fator `Jum 3 e depois `i`)$< `Is.`G\n\
3(x`- - 4) &_&+ 2)($X 2).`D n|a8x4|a8b|r|\n\
A ~3`)`'o x`- = 7x ~: ~) ~O`)`7~- `( a ~O`)`'o `ite de zero?`E 7`F x`- - 7`| 0 `h x&+ 7) = 0.`G\n\
`| 0 ou `| 7.`D n|a8x5|a8c|r|\n\
$f x/2 - &+ 3)/4 ~W.`E 5`F `{ tudo ~! 4.`G\n\
2x - &+ 3) = 8 `h $X 3 = 8 `h `| 5.`D m|a8x6|a8c|r|`U `( a f`X$y v = d / t resolvida em $L a t?~e t = d / v|t\
 = v `, d|t = d - v|t = v / d`E 1`F `{ ~! t e $E ~! v.`G\n\
v t = d, ~K t = d / v (v ~L 0).`D n|a8x7|a8d|r|\n\
No sis~:a x - y &_ e $X y $j1, quanto $Q x?`E 7`F &' as ~) ~3`)`7 ou isola x na primeira.`G\n\
`| y + 3; 2y + 3 $j1, y $h e `| 7.`D v|a8x8|a8d|r|\n\
O sis~:a $X y ~W e $X y &g `( $T`;vel.`E V`F Pode $X y $Qr 2 e 5 a$8 ~:po?`G\n\
Verdadeiro: as `ns $X y ~W e $X y &g s`'o `V#A; n`'o h`2 ~O`)`'o.`D n|a8x9|a8e|r|`U `( `Lclive da `n ~1 $w em\
 (2, 5) e (6, 3)?`E -0,5`F m = (y~M - y~@) / (x~M - x~@).`G\n\
(3 - 5) / (6 - 2) = -0,5.\n\
"
 return _ns('D', _dz(D))


_F['x_a8'] = _m_x_a8


def _m_x_a9():
 D = "~{~| 8~F (9.`K ~o`D m|a9x1|a9a|r|`U `( o &%~O`)`'`L -3x > 12?~e ]-~,, -4[|]-~,, 4[|]-4, +~,[|]4, +~,[`E 1`F\
 Divide ~! -3 e inverte ~q.`G\n\
x < -4: ]-~,, -4[.`D n|a9x2|a9a|r|`U `( o &7 `0 $a ~1 verifica 2x - 5 > 4?`E 5`F x > 4,5.`G\n\
2x > 9, x > 4,5; o &7 $a `( 5.`D n|a9x3|a9b|r|`U `( o &c de x`- - 6$X 5 = 0?`E 16`F $5 = b`- - 4ac.`G\n\
36 - 20 $j6.`D m|a9x4|a9b|r|\n\
Quantas ~O`)`7 ~: x`- + 2$X 5 = 0?~e Nenh`}|Uma|Duas|In&0s`E 1`F ~; $5.`G\n\
$5 $h - 20 = -16 < 0: n`'o ~: ~O`)`7 ~Qis.`D n|a9x5|a9b|r|\n\
x`- - 5$X 6 = 0 ~: ~) ~O`)`7~- `( a `y?`E 3`F `| (5 \xb1 1) $3.`G\n\
`| 2 ou `| 3.`D n|a9x6|a9c|r|\n\
x e y s`'o $C~T~!cionais; `V `| 3, y = 8. `m $Q y `V `| 4?`E 6`F k = x `, y.`G\n\
k ~W4; y ~W4 / 4 = 6.`D v|a9x7|a9c|r|\n\
O gr`2$U `Aa fun`)`'`L `d $C $w $} do refere`Ml.`E F`F Pode x ser 0 em y = k / x?`G$I `| 0 n`'o $Rtenc$bo\
 dom`;nio; o gr`2$U `( um ram`L hip`(rbole.`D n|a9x8|a9d|r|\n\
Se #0 = -x`-, &; `( f(-4)?`E -16`F (-4)`- $j6.`G$-16: f(-4) = -(16) = -16.\n\
"
 return _ns('D', _dz(D))


_F['x_a9'] = _m_x_a9


def _m_x_d7():
 D = "~{~| 8&X Da`O (7.`K ~o`D n|d7x1|d7a|r|&2 inqu`(rito a 40 pessoas, 14 responderam \"sim\"~- `( a $%`B`M ~9 do\
 \"sim\", em `z?`E 35`F fr $j4 / 40.`G\n\
14 / 40 = 0,35 &_5%.`D n|d7x2|d7a|r|&2 gr`2$U &S, `} categoria ~: $%`B`M ~9 #7~- `( o `! d&stor (em &Ds)?`E\
 54`F `{ ~! 360`8.`G\n\
#7 `, 360`8 &g4`8.`D m|d7x3|d7a|r|`U d~kes da`O `( &;itativo?~e N`_mer`L irm`'os|Temp`L ~Q`)`'o (s)|Altura\
 (cm)|Cor `O olhos`E 4`F Qualitativos n`'o s`'o `0s.`G\n\
A cor `O olhos `( `} categoria, n`'o um `0.`D n|d7x4|d7b|r|`U `( &d`($! de #L 15, 9, 14 e 10?`E 12`F &' e $E ~! 5.`G\n\
60 / 5 $+.`D n|d7x5|d7b|r|`U `( a `P de 8, 3, 6, 10, 4, 7?`E 6,5`F Ordena; h`2 um `0 &, #!`O.`G\n\
3, 4, 6, 7, 8, 10: (6 + 7) $3 = 6,5.`D v|d7x6|d7b|r|\n\
A m`($! `A &Rt`L da`O `( $> um `O da`O.`E F`F Ex~imenta `J 1 e 2.`G$I &d`($! de 1 e 2 `( 1,5, ~1 n`'o `(\
 nenhum `O da`O.`D n|d7x7|d7b|r|\n\
A m`($! de 4 t~kes `( 14. Que nota precisa o 5.`K t~ke `V &d`($! $wr a 15?`E 19`F A ~' `O 4 t~kes `( 4 `, 14.`G\n\
&' precisa: 5 `, 15 = 75; j`2 ~: 4 `, 14 &g6; falta 75 - 56 $j9.`D n|d7x8|d7c|r|\n\
No `p de caule-e-folhas 1 `g 2 5 8, 2 `g 0 3 3 7, 3 `g 1, &; `( a `^ `O da`O?`E 19`F M`2ximo 31 e m`;nimo 12.`G\n\
31 - 12 $j9.\n\
"
 return _ns('D', _dz(D))


_F['x_d7'] = _m_x_d7


def _m_x_d8():
 D = "~{~| 8&X Da`O (8.`K ~o`D n|d8x1|d8a|r|\n\
~; Q1 `O da`O 2, 4, 5, 7, 8, 10, 11, 13.`E 4,5`F $] baixo: 2, 4, 5, 7.`G\n\
Q1 = (4 + 5) $3 $h,5.`D n|d8x2|d8a|r|\n\
~; Q3 `O da`O 1, 3, 3, 4, 6, 7, 9 (n = 7).`E 7`F Com n `;m&,, a `P (4) fic$< fora.`G\n\
$] cima: 6, 7, 9; Q3 = 7.`D n|d8x3|d8a|r|&2 `p &H$0 &o: m`;nimo 2, Q1 &g, `P 8, Q3 $j1, m`2ximo 15~- `( a `^\
 &v?`E 6`F AIQ = Q3 - Q1.`G\n\
11 - 5 = 6.`D m|d8x4|d8a|r|\n\
Que `z `O da`O ~k`2, $emente, abaix`L Q1?~e 50%|75%|25%|10%`E 3`F Os &o $Em &M`O em quatro &,tes.`G\n\
Abaix`L Q1 ~k`2 ~N 25% `O da`O.`D v|d8x5|d8a|r|\n\
A `^ &v `( $> `y do ~1 a `^ #9.`E F`F A AIQ s`X usa os 50% centrais.`G$I AIQ = Q3 - Q1 nunca `( `y do ~1\
 m`2ximo - m`;nimo.`D n|d8x6|d8b|r|`U `( o $, m`(dio da $1 [#L5; 17,5[?`E 15`F (a + b) $3.`G\n\
(#L5 + 17,5) $3 $j5.`D n|d8x7|d8b|r|\n\
Classes [0, 10[ `J 2 da`O, [10, 20[ `J 5 e [20, 30[ `J 3~- `( &d`($! $e?`E 16`F Pontos m`(dios 5, 15 e 25.`G\n\
(5 `, 2 + 15 `, 5 + 25 `, 3) / 10 $j6.`D m|d8x8|d8b|r|&2 histograma, as barras...~e ~k`'&s`V$c ~!\
 espa`)os|t`Bm larguras ao acaso|repre~Jtam da`O &;itativos|~k`'o en~ata$c `}s $ps outras`E 4`F As $1s s`'o\
 ~4s segui`O.`G&2 histograma as barras ~k`'o en~ata$c: as $1s s`'o ~4s cont`;guos.\n\
"
 return _ns('D', _dz(D))


_F['x_d8'] = _m_x_d8


def _m_x_d9():
 D = "~{~| 8&X ~t (9.`K ~o`D n|d9x1|d9a|r|\n\
N`} #' h`2 4 #( branca$0 6 p`ns~- `( a `= de tirar `} branca?`E 0,4`F P = &K`2veis / &T`;&r`G\n\
4/10 = 0,4.`D m|d9x2|d9a|r|\n\
Tira-se `} carta `A baralh`L 52~- `( a `= de ser um `2s?~e 1/13|1/52|4/13|1/4`E 1`F H`2 4 ases.`G\n\
4/52 $j/13.`D v|d9x3|d9a|r|\n\
Se P(A) = 0,35, ent`'o P(n`'o A) = 0,65.`E V`F P(n`'o A) $j - P(A).`G\n\
Verdadeiro: 1 - 0,35 = 0,65.`D n|d9x4|d9b|r|\n\
Lan`)$s ~2 da`O~- `( a `= #1`;rem ~2 `0s $_?`E 1/6`F Os &,es (1,1), (2,2)...`G\n\
6 ~0 em 36: 1/6.`D n|d9x5|d9b|r|\n\
Lan`)$s tr`Bs moe$c~- `( a `= #1`;rem exatamente ~) face$0uropeias?`E 0,375`F S`'o 8 ~0: EEN, ENE, NEE...`G\n\
3 ~0 em 8: 3/8 = 0,375.`D n|d9x6|d9b|r|\n\
Lan`)$s ~2 da`O~- `( a `= d$b ~' ser 4?`E 1/12`F (1,3), (2,2) e (3,1).`G\n\
3 ~0 em 36: 1/12.`D n|d9x7|d9c|r|$Ha #' ~: 2 #( branca$0 3 p`ns. Tir$s ~), `J reposi`)`'o~- `( a `= #1`;rem\
 ~) brancas?`E 0,16`F 2/5 `, 2/5.`G\n\
4/25 = 0,16.`D n|d9x8|d9c|r|\n\
A $. #' (2 brancas, 3 p`ns), agora ~g`)`'o~- `( a `= #1`;rem ~) brancas?`E 0,1`F 2/5 `, 1/4.`G\n\
2/20 = 0,1.\n\
"
 return _ns('D', _dz(D))


_F['x_d9'] = _m_x_d9


def _m_x_g7():
 D = "~{~| 9$@~7$? (7.`K ~o`D n|g7x1|g7a|r|`U `( o #: `A `! de 47`8?`E 133`F Su#? ~'m 180`8.`G\n\
180`8 - 47`8 $j33`8.`D m|g7x2|g7a|r|\n\
Duas `ns `V#A s`'o corta$c ~! `} secante. Dois `!s $M ~C ~Um 3x e 60`8. `m $Q x?~e 20|10|60|40`E 1`F Alternos\
 ~C s`'o $_.`G\n\
3`| 60, ~K `| 20.`D n|g7x3|g7b|r|`U `( a ~' `O `!s ~C `A hex`2~y (em &Ds)?`E 720`F S = (n - 2) `, 180`8.`G\n\
(6 - 2) `, 180`8 = 720`8.`D v|g7x4|g7b|r|$H ~7`! pode ter ~2 `!s obtusos.`E F`F Dois `!s obtusos ~'m mai~P\
 180`8.`G$I a ~' `O tr`Bs `!s `( 180`8, e ~2 obtusos j`2 $wm `O 180`8.`D n|g7x5|g7c|r|$H losango ~: $!gonai~P\
 10 cm e 7 cm~- `( a `2~Q (em cm`-)?`E 35`F &> D `, d $3.`G\n\
10 `, 7 $3 &_#2`-.`D n|g7x6|g7d|d2|`U `( a `2~Q `A c`;#= `J 4 $2 $z, em cm`-, `J ~) ~.`E 50,27`F &> `>r`-.`G\n\
`> `, 4`- $j6`> `: 50,27 cm`-.`D n|g7x7|g7d|d2|$Ha piza `J 30 $2 di&9~R `( cortada em 8 fatias $_~- `( a `2~Q\
 de ~} fatia, em cm`-, `J ~) ~.`E 88,36`F Raio 1#2; ~} fatia `( 1/8 do c`;#=.`G\n\
`> `, 15`- / 8 `: 88,36 cm`-.`D n|g7x8|g7e|r|$Ha fotografi$< 10 cm ~! 1#2 `( &nda `J #K`'o 3~- `( a `2~Q da\
 &n`)`'o (em cm`-)?`E 1350`F A `2~Q `H ~! k`-.`G\n\
&A~Q ~l 150 cm`-; 3`- `, 150 $j350 cm`-.`D m|g7x9|g7e|r|`U d~kes crit`(rios N\xc3O garante ~1 ~2 ~7`!s s`'o\
 `[?~e Um `! &8 e um ~H &8|Dois `!s $_ (AA)|Os tr`Bs la`O pro~!cionais (LLL)|Dois la`O pro~!cionai$0 o `! ~m\
 eles &8 (LAL)`E 1`F Os crit`(rios s`'o AA, LLL e LAL.`G$H `! e um ~H $_ n`'o chegam: os &L la`O podem n`'&sr pro~!&I\n\
"
 return _ns('D', _dz(D))


_F['x_g7'] = _m_x_g7


def _m_x_g8():
 D = "~{~| 8$@~7$? (8.`K ~o`D n|g8x1|g8a|r|\n\
Os ~Zs `A ~7`! &<`! ~Um #2 e 12 &x `m ~U a `b?`E 13`F c = `+(a`- + b`-).`G\n\
`+(25 + 144) = `+169 $j3 &x`D n|g8x2|g8a|d2|\n\
A ~V `A `I ~U 10 &x `m ~U o ~H, `J ~) ~.`E 7,07`F l`- + l`- $i`-.`G\n\
2l`- $i0, l = `+50 `: 7,07 &x`D m|g8x3|g8b|r|`U d~kes ternos s`'o os la`O `A ~7`! &<`!?~e 4, 5, 6|5, #L 13|6,\
 8, 11|7, 8, 9`E 2`F T~ka `y`- = ~' `O &L ~2 ao `I.`G\n\
13`- $j69 ~W5 + 144.`D n|g8x4|g8b|r|`U `( a ~B`M ~m A(-1, 2) e B(5, 10)?`E 10`F d = `+($5x`- + $5y`-).`G\n\
`+(6`- + 8`-) $i.`D n|g8x5|g8b|d2|$Ha #' ~: 30 cm `, 40 cm `, 20 cm~- `( o `J~E da ~V espacial, em cm, `J ~)\
 ~.`E 53,85`F `+(c`- + l`- + h`-).`G\n\
`+(900 + 1600 + 400) = `+2900 `: 53,85 &x`D m|g8x6|g8c|r|\n\
A $A`)`'`L $= (-2, 5) leva o $, (3, -1) a...~e (1, -6)|(1, 4)|(5, -6)|(-6, -5)`E 2`F &' as ~^ do $=.`G\n\
(3 - 2, -1 + 5) = (1, 4).`D m|g8x7|g8d|r|`U `( a &/ de (2, -3) pela &a`)`'`L 180`8 de ~% O?~e (-3, 2)|(2,\
 3)|(3, 2)|(-2, 3)`E 4`F Meia-volta: (x, y) $l (-x, -y).`G\n\
(-2, 3).`D v|g8x8|g8d|r|\n\
A $m`'o $^ &u mant`(m a orienta`)`'o `O v`($Ps da figura.`E F`F Olha `V `} m`'o ao espelho.`G$I a $m`'o troca\
 a orienta`)`'o; $A`)`7 e &a`)`7 mant`Bm-na.\n\
"
 return _ns('D', _dz(D))


_F['x_g8'] = _m_x_g8


def _m_x_g9():
 D = "~{~| 10$@~7$? (9.`K ~o`D n|g9x1|g9a|r|\n\
N`} `f`B`M, um `! ao ~% ~U 110`8. `m me`A `! ~( ~1 `Jpreende $8 &O?`E 55`F O ~( `( $n do &O.`G\n\
110`8 $3 &g5`8.`D n|g9x2|g9a|r|\n\
Duas cor$c cruz$s dentro `Aa `f`B`M; os ar~a `Jpreendi`O ~Um 70`8 e 50`8. `m ~U o `!?`E 60`F V`($P #F~' `O ar~a.`G\n\
(70`8 + 50`8) $3 = 60`8.`D n|g9x3|g9b|d3|\n\
O ~Z ~h a `9 ~U 5 $b `b 13. `m $Q ~J `9, `J 3 ~.`E 0,385`F ~J `9 = ~h / `b.`G\n\
~J `9 &g / 13 `: 0,385.`D m|g9x4|g9b|r|&2 ~7`! &<`!, o ~Z ~> a `9 a ~n pela `b `(...~e o ~a~J`L `9|o ~J`L\
 `9|a #, de `9|o &k do ~J`L `9`E 1`F ~a `9 = ~> / `b.`G\n\
\xc9 o ~a~J`L `9.`D n|g9x5|g9c|d2|$Ha es~} de 6 m faz 60`8 `J o ch`'o. A ~1 `c chega, em ~Rs, `J 2 ~.`E\
 5,20`F Altura = `J~E `, ~J 60`8.`G\n\
6 `, ~J 60`8 &_`+3 `: 5,20 m.`D n|g9x6|g9d|r|\n\
`9 `( agudo e ~J `9 = 0,8. `m $Q ~a `9?`E 0,6`F ~a`- `9 $j - ~J`- `9.`G\n\
~a`- `9 $j - 0,64 = 0,36, ~K ~a `9 = 0,6.`D m|g9x7|g9d|r|`U `( o `Z exat`L ~a 30`8?~e `+2/2|`+3|`+3/2|1/2`E\
 3`F Num ~7`! equil`2ter`L ~H 2, a `c `( `+3.`G\n\
~a 30`8 = ~J 60`8 = `+3/2.`D n|g9x8|g9e|d2|`U `( o $V `A &V `J 2 $2 $z e 5 $2 `c, em cm`j, `J ~) ~.`E 62,83`F\
 V = `>r`-h.`G\n\
`> `, 4 `, 5 ~W0`> `: 62,83 cm`j.`D n|g9x9|g9e|r|$Ha pir&9mide quadrangular ~: ~] de 6 $2 ~H e 10 $2 `c~- `(\
 o $V (em cm`j)?`E 120`F V = Ab `, h / 3.`G\n\
36 `, 10 / 3 $+0 cm`j.`D m|g9x10|g9f|r|\n\
Os `k ~1 ~k`'o $p $. ~B`M de A e de B #/m...~e a `f`B`M de di&9~R [AB]|o $u [AB]|&de$!~7z de [AB]|a bisse~7z\
 do `! AOB`E 3`F Equidistante~P ~2 `k.`G\n\
\xc9 &de$!~7z de [AB]: a $R&B a [AB] no $, m`(dio.\n\
"
 return _ns('D', _dz(D))


_F['x_g9'] = _m_x_g9


def _m_x_n7():
 D = "~{~| 9&X N`_~b (7.`K ~o`D m|n7x1|n7a|r|`U d~kas afirma`)`7 `( verdadeira?~e `g-4`g < `g3`g|-7 < -9|0 <\
 -0,1|-1/2 > -3/4`E 4`F Entre $Ks, o `y ~k`2 $J $Rt`L 0.`G$-0,5 > -0,75: -1/2 ~k`2 $J $p direita na `n\
 $^`(rica.`D n|n7x2|n7b|r|\n\
~; 3/4 - 5/6 &( `J `} $G`)`'o).`E -1/12`F O ~8 de 4 e 6 `( 12.`G\n\
9/12 - 10/12 = -1/12.`D n|n7x3|n7b|r|\n\
~; -2/5 `, 15/4 &( `J `} $G`)`'o).`E -3/2`F `{ $^eradore$0 ~+e$0 simpli&}`G$-30/20 = -3/2.`D v|n7x4|n7c|r|\n\
(-2)`w e -2`w t`Bm $8 `Z.`E F`F Em -2`w, o `@ s`X s$bplica ao 2.`G\n\
(-2)`w $j6 e -2`w = -16.`D n|n7x5|n7c|r|\n\
~; 3~d : 3`j `, 3.`E 27`F Mesma ~]: subtrai e ~' os `@s.`G\n\
3~d`T`j\u207a#> &_`j ~W7.`D n|n7x6|n7d|r|\n\
~; &!(-64) + `+81.`E 5`F (-4)`j = -64 e 9`- = 81.`G$-4 + 9 &g.`D m|n7x7|n7d|r|\n\
Entre ~1 ~6 &h ~k`2 `+50?~e 6 e 7|49 e 51|24 e 25|7 e 8`E 4`F Procura os `Is $Rfeitos $p volt$< 50.`G\n\
7`- $h9 < 50 < 64 = 8`-, ~K 7 < `+50 < 8.`D n|n7x8|n7e|r|`U `( o ~v de 84 e 126?`E 42`F 84 ~W`- `, 3 `, 7 e\
 126 ~W `, 3`- `, 7.`G\n\
~v ~W `, 3 `, 7 $h2.`D n|n7x9|n7e|r|`U `( o ~8 de 8, 12 e 18?`E 72`F 8 ~W`j, 12 ~W`- `, 3 e 18 ~W `, 3`-.`G\n\
~8 ~W`j `, 3`- = 72.\n\
"
 return _ns('D', _dz(D))


_F['x_n7'] = _m_x_n7


def _m_x_n8():
 D = "~{~| 8&X N`_~b (8.`K ~o`D n|n8x1|n8a|r|\n\
~; 5`T`- &( `J `} $G`)`'o).`E 1/25`F a`T#; $j / a^n.`G\n\
5`T`- $j / 5`- $j/25 = 0,04.`D n|n8x2|n8a|r|\n\
~; (1/2)`T`j.`E 8`F Invert$b ~]: (1/2)`T`j ~W`j.`G\n\
2`j = 8.`D m|n8x3|n8a|r|`U `( o `Z de 3`w `, 3`T&^?~e 9|-9|3`T`-`w|1/9`E 4`F Mesma ~]: ~'$D `@s.`G\n\
3`w`T&^ &_`T`- $j/9.`D v|n8x4|n8b|r|\n\
O `0 12 `, 10~d ~k`2 escrito $x`)`'~G`;&}`E F`F A &U ~: de ~kar ~m 1 e 10.`G$I 12 > 10; $x`)`'~G`;fica `( 1,2\
 `, 10&^.`D n|n8x5|n8b|r|\n\
O `@ n de 6 `, 10\u2078 : (1,5 `, 10`j) $h `, 10^n `(...`E 5`F Na divis`'o, subtrae$D `@s.`G\n\
8 - 3 &g: 4 `, 10~d.`D m|n8x6|n8b|r|`U `( o `y d~kes `0s?~e 1,1 `, 10`T`-|0,0099|5 `, 10`T`w|9,9 `, 10`T`j`E\
 1`F Com`V $: os `@s.`G\n\
1,1 `, 10`T`- = 0,011 `( o `y; 9,9 `, 10`T`j = 0,0099.`D m|n8x7|n8c|r|`U d~kas $G`)`7 d`2 `} d`;~w ~z\
 ~i`Xdica?~e 7/20|9/25|3/8|5/6`E 4`F De`Jp\xf5#Es ~+es.`G\n\
O ~+ 6 ~W `, 3 ~: o $4 3: 5/6 d`2 a d`;~w 0,8(3).`D n|n8x8|n8c|r|\n\
$q 0,(7) `Jo $G`)`'o.`E 7/9`F 10d - d = 7.`G\n\
9d = 7, ~K d = 7/9.\n\
"
 return _ns('D', _dz(D))


_F['x_n8'] = _m_x_n8


def _m_x_n9():
 D = "~{~| 8&X N`_~b (9.`K ~o`D m|n9x1|n9a|r|`U d~kes `0s `( irracional?~e `+7|-3/8|0,(25)|`+16`E 1`F 7 n`'o `( um\
 `I $Rfeito.`G\n\
`+7 `: 2,6457... `( `} d`;~w ~z n`'o ~i`Xdica.`D m|n9x2|n9a|r|\n\
Entre ~1 ~6 &h ~k`2 -`+20?~e -5 e -4|4 e 5|-4 e -3|-20 e -19`E 1`F 4 < `+20 < 5.`G$-5 < -`+20 < -4, ~!~1 `+20\
 `: 4,47.`D v|n9x3|n9a|r|\n\
A ~' de ~2 `0s ir`Q `( $> irracional.`E F`F Ex~imenta `+2 + (-`+2).`G$I `+2 + (-`+2) = 0, ~1 `( racional.`D\
 m|n9x4|n9b|r|`U `( a #/ simplifi~} de `+75?~e 5`+3|25`+3|15|3`+5`E 1`F 75 ~W5 `, 3.`G\n\
`+75 = `+25 `, `+3 &g`+3.`D n|n9x5|n9b|r|\n\
~; (`+5)`- + `+9.`E 8`F (`+a)`- &Z.`G\n\
5 + 3 = 8.`D m|n9x6|n9c|r|`U `( ~D B, `J &> [1, 6] e #6 ]4, 9]?~e ]4, 6]|]1, 4]|[4, 6[|[1, 9]`E 1`F Os `0s ~1\
 ~k`'o nos ~2.`G\n\
4 < x ~? 6: ]4, 6].`D n|n9x7|n9c|r|\n\
`ms `0s ~6 h`2 no ~4 ]-3, 2]?`E 5`F -2, -1, 0, ...`G$-2, -1, 0, 1 e 2: 5 `0s.`D m|n9x8|n9c|r|`U `( a\
 condi`)`'o ~1 defin#E ~4 ]-~,, 4[?~e x < 4|x ~c 4|x > 4|x ~? 4`E 1`F O 4 n`'o $Rtenc$bo ~4.`G\n\
]-~,, 4[ `( x < 4.\n\
"
 return _ns('D', _dz(D))


_F['x_n9'] = _m_x_n9


_imp('m1')
