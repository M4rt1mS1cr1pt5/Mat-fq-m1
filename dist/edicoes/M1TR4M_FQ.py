# M1TR4M_FQ.py - M1TR4M: edicao de reserva "M1TR4M FQ" num so ficheiro
# (gerada pelo build; nao editar). Usa-se so se importar modulos entre
# programas nao funcionar no aparelho. Leva: 9 temas (q1 q2 q3 q4 q5 q6 f1 f2 f3), 38 calculadoras.



_F = {}
_L = {}
_ED = 'FQ'


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



_T = "\xe3`\xe7`\xf5es`\u207b`\xd7 10`energia`\xe9`\xe1`eletr`\u2082`\xed`resist\xeancia`temperatura`\xf3`\xb9`o\
 de`\xb2`de val\xeancia`\u0394`\xd7`\n\
Objetivo:`com`liga`\n\
Erros a evitar:`que`massa`trabalho`\xfa`\xb3`mol`\n\
- Calcular`\n\
Dados:`\n\
Verifica`Energia`para`A 10.\xba,`\n\
- Relacionar`mais`\xea`ncia`elemento`grupo`\u2074`\n\
Resultado:`\n\
@D`\n\
Interpreta`tomos`\u2076`\n\
Exemplo:`\n\
@F`corrente`culas`\n\
- Confundir`cerca de`solu`\u03bb`\u03a9`\n\
- Achar`de um`quantidade`diferen`\u2083`tem`\xb0`\n\
- Es`de ioniza`\xe2`\u2079`\u2078`part`algarismos significativos`volume`velocidade`\n\
@X`\n\
@S`\n\
@P`\n\
- Distinguir`\n\
- Definir`aumenta`\n\
O`por`concentra`conservativas`interna`priment`uma`\u2075`dos`\u03b5`\n\
1.`\n\
- Usar`a de`radia`pares`\n\
2.`\u03b7 =`\n\
Um`hidrog`a vizinhan`\n\
- Explicar`a mesma`\n\
A`\u2192`de grandeza`o do`for`mesmo`rendimento`configura`\u2248`\u2077`orbitais`vel`entre`\n\
3.`propriedades`diminui`\u2022`\u03c1`menos`cada`metais`das`constante`carga`= 10`explica`o\
 da`mica`maior`percentagem`conserva`\u2099`absorve`fot`\u207a`atrito`ponente`\xe0`transferida`ltimo\
 n`gua`valor`0,50`\u2084`\n\
@R`\n\
@L`\n\
@J`\n\
@I`\n\
@H`\n\
@G`\n\
@C`\n\
@B`\n\
@A`muito`menor`per`varia`ozono`reatividade`final`isso`fica`corpo`orbital`cer`Qual`\n\
Enu`Massa e tamanho`= 2,0`m s`\n\
-`polar`s de`ntes`\n\
Exemplo`metro`rea`est`\n\
Calcula`resistividade`altura`neutr`espetro`tomo`Tabela Peri`desemparelha`||AE FQ`nica`relativa`e\
 movimentos`terminais`mer`covalente`\n\
Verdadeiro:`tens`ordem`100`radicais livres`\u03b8`pot`idade`= 6,0`\u03b1`\n\
@O`recebe`tica`veis`\n\
Re`o qu`\u2070`= -2,18`cula`= \xbd`|c_fqel.conf`transfer`gases`abund`troca`simples`bloco`\u2113`de mat`n\
 =`c\u2098 =`cional`coloide`de remo`depende`da resultante`subn`subst`3,0`Liga`raio`Gases e dis`o\
 se`topos`onegativ`\u2261`\u03a3`\n\
@E`\n\
4.`soma`kg de`suspens`preciso`2,0`\n\
Quantos`ssica`espessura`\u221a(2`o e`metal`do:`nos`cloro`Mendeleiev`\n\
Que`1,0`pilha`posi`dilui`fra`rmula`a luz`4,0`mistura`inicial`odo`\n\
Por`Eletr`radical`corresponde`ria e`carbono`passar`total`prot`= 6,63`resultado`riscas`\n\
>`6,02`durante`\n\
Para`o n`material`dois`entalpia`o cient`necida)`condutor`tabela`qual`model`5,0`g\
 de`emiss`absor`cao`\u2081`\u207f`Corrente`, logo`sem`slocamento.`sis`rmicos e`liza`quando`multiplicar`fator\
 de`ratosfera`convec`Trocar`Interpretar`vezes`dupla`dissipada`W(R) =`calor`sinal`mudan`de refer`intera`)\
 =`0,20`vermelh`em vez`= 9,0`||10|n`tricos`s funcionais`s e`trica`o m`pode`liberta`gerador`o: a`o at`e\
 a`crever`rendiment`quantos`Aplicar a`omotriz`Vi = cf`o a`volta`solvente`deslocament`@V 1`\n\
@T`\n\
@N`E =`\n\
Num`U =`mesma`Massa`\u2191`\u03b7`equivalente`\n\
\xc9`1,5`P =`tend`pelo`alcali`I =`regra do`pende da`Epg`opostos.`0\
 =`Protocol`emite`cobre`Com`cin`\u2265`duas`ado fundamental?`transi`contar`circuito.`Concentra`Quanto`o:\
 o`nio`mar`grande`frequ`etanol`dissipam-se`Dizer`e de`a sua`c =`ante`Teorema da`ir de`e do repous`cido\
 carbox`Lei de`catalisador`22,4`(em`oxig`\n\
Em`mas`nuclear`oioniza`Segunda`500`\u2193`tamanho`\xba`usar`painel`ngulo`mpada`muita`miscibil`metano,\
 CH`condutiv`carbo`Prever a`Q = m`Identi`1 / Req`,\
 a`isolado`0,250`polue`halog`tamb`ximo`recebida`vale`pouco`organiza`ppm`pont`os n`piramidal`os\
 do`pico`peso`mL de`o (`m de`lelo`aproxima`f =`brar`Primeira`= 1,96\
 g`18,02`onde`Stefan-Boltzmann`Rendiment`multiplica`London`J kg`6,0`00 /`vis`pre`+ 2`\n\
No`N =`nte`dia`num`onda`til) / E(`camad`trans`|10|n`|c_fqlg.lew`|c_fqso.gas`|c_fqci.assoc`= h\
 c`saparece.`materiais`divide-se`\u20ac`\u2093`\u2086`ria`tivos.`tes.`trajet`nota`l grav`pela`0,25`(M\
 =`mec`vizinhan`o s`quase`o long`o gelo`nobres`primeiro`pendi`kg a`horizontal.`funciona`m-se`Forma`m =`e\
 fen`linear`livre`da Termodin`indica`Tyndall.`Mais`J|c_fqen.em`geomet`gasta`, fen`\n\
Falso.`exot`3,34`tom`duplicar`dica`omagn`nuvem`contr`cont`condu`endot`R =`cati`quina`par n`cadeia`neos`hmico:\
 R`atra`aparelho`luz`\u2088`|c_fqat.mm`\u03c3`Princ`ocupam`irradi`P\xf4r`Pensar`Multiplica`Contar`1 \u2264 a`\n\
Duplicar`2p 3s 3p`\n\
Dois`1, 2,`+ O`quanto`0 %.`mite`+ 1`hexano`\n\
M`em gra`brio t`cos`M em g`bra`Z ="


def _m_c_comd():
 import math
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 X=N.X
 CTE=('Velocidade de propaga\xe7\xe3o da luz no v\xe1cuo|c|3,00 \xd7 10\u2078|m s\u207b\xb9|IAVE, Tabela de Constantes do exame de FQ A (715)|2024 (confirmar)\nM\xf3dulo da acelera\xe7\xe3o grav\xedtica junt'
'o \xe0 superf\xedcie da Terra|g|10|m s\u207b\xb2|IAVE, Tabela de Constantes do exame de FQ A (715)|2024 (confirmar)\nConstante de gravita\xe7\xe3o universal|G|6,67 \xd7 10\u207b\xb9\xb9|N m\xb2 kg'
'\u207b\xb2|IAVE, Tabela de Constantes do exame de FQ A (715)|2024 (confirmar)\nConstante de Avogadro|NA|6,02 \xd7 10\xb2\xb3|mol\u207b\xb9|IAVE, Tabela de Constantes do exame de FQ A (715)|2024 (confi'
'rmar)\nConstante de Stefan-Boltzmann|\u03c3|5,67 \xd7 10\u207b\u2078|W m\u207b\xb2 K\u207b\u2074|IAVE, Tabela de Constantes do exame de FQ A (715); extens\xe3o no 10.\xba ano|2024 (confirmar)\nProduto'
' i\xf3nico da \xe1gua (25 \xb0C)|Kw|1,00 \xd7 10\u207b\xb9\u2074||IAVE, Tabela de Constantes do exame de FQ A (715); mat\xe9ria do 11.\xba ano|2024 (confirmar)\nVolume molar de um g\xe1s (PTN)|Vm|22,4'
'|dm\xb3 mol\u207b\xb9|IAVE, Tabela de Constantes do exame de FQ A (715)|2024 (confirmar)\nConstante de Planck|h|6,63 \xd7 10\u207b\xb3\u2074|J s|valor arredondado; CODATA: 6,626 070 15 \xd7 10\u207b'
'\xb3\u2074 J s (exato)|2018\nCarga elementar|e|1,60 \xd7 10\u207b\xb9\u2079|C|valor arredondado; CODATA: 1,602 176 634 \xd7 10\u207b\xb9\u2079 C (exato)|2018\nEletr\xe3o-volt|eV|1,60 \xd7 10\u207b\xb9'
'\u2079|J|1 eV = e \xd7 1 V; CODATA|2018\nUnidade de massa at\xf3mica|u|1,66 \xd7 10\u207b\xb2\u2077|kg|valor arredondado; CODATA: 1,660 539 066 60 \xd7 10\u207b\xb2\u2077 kg|2018\nAcelera\xe7\xe3o gra'
'v\xedtica padr\xe3o|gn|9,80665|m s\u207b\xb2|valor convencional (3.\xaa CGPM)|1901\nEnergia do eletr\xe3o no n\xedvel n do \xe1tomo de hidrog\xe9nio|En|-2,18 \xd7 10\u207b\xb9\u2078/n\xb2|J|modelo de '
'Bohr (valor usado nos manuais)|\u2014\nCapacidade t\xe9rmica m\xe1ssica da \xe1gua l\xedquida|c|4,18 \xd7 10\xb3|J kg\u207b\xb9 K\u207b\xb9|valor usado nos manuais (varia com a temperatura)|\u2014\nVa'
'ria\xe7\xe3o de entalpia (m\xe1ssica) de fus\xe3o do gelo|\u0394Hf|3,34 \xd7 10\u2075|J kg\u207b\xb9|valor tabelado a 0 \xb0C|\u2014\nVaria\xe7\xe3o de entalpia (m\xe1ssica) de vaporiza\xe7\xe3o da '
'\xe1gua|\u0394Hv|2,26 \xd7 10\u2076|J kg\u207b\xb9|valor tabelado a 100 \xb0C|\u2014\nMassa vol\xfamica da \xe1gua (4 \xb0C)|\u03c1|1,00 \xd7 10\xb3|kg m\u207b\xb3|valor arredondado|\u2014\nPress\xe3o'
' normal (1 atm)|p|1,01325 \xd7 10\u2075|Pa|valor convencional|\u2014\nZero da escala Celsius em kelvin|T0|273,15|K|defini\xe7\xe3o da escala Celsius|\u2014')
 def cte():
  cs=[c.split('|')for c in CTE.split('\n')if c]
  sel=0
  while True:
   r=U.menu('Constantes e dados',[c[1]+': '+c[0]for c in cs],sel)
   if r<0:
    return None
   sel=r
   c=cs[r]
   s='# '+c[0]+'\n= '+c[1]+' = '+c[2]+(' '+c[3]if c[3]else '')+'\nFonte: '+c[4]+('\nAno: '+c[5]if c[5]and c[5]!='\u2014'else '')
   try:
    val=N.num(c[2].replace(' ',''))[0]
   except ValueError:
    val=None
   k=U.text('Constante',s+('\n\n1: usar como ans'if val is not None else ''),'','',('1',))
   if k=='1'and val is not None:
    N.CF['ans']=val
    U.msg('Constante','ans = '+c[2]+'. Escreve ans num campo de uma calculadora.')
 def exp():
  return('Dados experimentais',[N.fld('Valores medidos (separa com espa\xe7os)','','','t'),N.fld('Unidade (opcional)','','','t'),N.fld('Incerteza de leitura (opcional)','','','o'),N.fld('Valor de refer\xeancia (opcional)',
'','','o')],_exp)
 def _exp(v):
  txt,un,il,ref=v
  ps=N.lst(txt)
  N.need(len(ps)>=1,'Escreve os valores medidos separados por espa\xe7os')
  xs=[N.num(p)[0]for p in ps]
  n=len(xs)
  m=sum(xs)/n
  ds=[abs(x-m)for x in xs]
  dm=max(ds)
  u=' '+un if un else ''
  o=['= m\xe9dia = ('+' + '.join(ps)+') / '+str(n),'> m\xe9dia '+N.eq(m,0,-1)+u]
  st=['Desvios |x(i) - m\xe9dia|:']
  for p,d in zip(ps,ds):
   st.append('- '+p+': '+N.fmt(d,0,6))
  inc=dm
  src='maior desvio'
  if il is not None and il[0]>inc:
   inc=il[0]
   src='incerteza de leitura (maior do que os desvios)'
  if n==1 and il is None:
   o.append('Com um s\xf3 valor, indica a incerteza de leitura do instrumento.')
   return('\n'.join(o),'',m,un)
  o.append('Incerteza absoluta = '+src+' = '+N.fmt(inc,0,6)+u)
  if inc>0:
   o.append('> x = '+N.pm(m,inc)+u)
   o.append('(incerteza com 1 algarismo significativo, arredondada por excesso; m\xe9dia com as mesmas casas)')
   if m!=0:
    o.append('Incerteza relativa = '+N.fmt(inc/abs(m)*100,0,2)+' % (quanto menor, maior a precis\xe3o)')
  if ref is not None:
   r=ref[0]
   ea=abs(m-r)
   o.append('Erro absoluto = |m\xe9dia - x_ref| = '+N.fmt(ea,0,6)+u)
   if r!=0:
    o.append('> Erro percentual = '+N.fmt(ea/abs(r)*100,0,2)+' % (quanto menor, maior a exatid\xe3o)')
   else:
    o.append('Com valor de refer\xeancia 0 n\xe3o h\xe1 erro percentual.')
  return('\n'.join(o),'\n'.join(st),m,un)
 return _ns('N U X cte exp',N,U,X,cte,exp)


_F['c_comd'] = _m_c_comd


def _m_c_comu():
 import math
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 X=N.X
 def sci():
  return('Calculadora cient\xedfica',[N.fld('Express\xe3o (ex.: 2^10+\u221a2, sen 30)','','','t')],_sci)
 def _sci(v):
  e=v[0]
  if not e:
   N.err('Escreve uma express\xe3o, por exemplo 2^10 + sqrt(2)')
  r=N.ev(N.comp(e,0))
  a='graus'if N.CF['ang']==0 else 'radianos'
  t='= '+e+'\n> '+N.rhs(r,10)+'\n\nUnidade angular: '+a+' (muda nas Defini\xe7\xf5es).'
  return(t,'O valor exato aparece quando \xe9 uma fra\xe7\xe3o, uma raiz ou um m\xfaltiplo de \u03c0; o aproximado tem as casas das Defini\xe7\xf5es (aqui at\xe9 10).',r,'')
 def info(s):
  v,sf=N.num(s)
  if sf==0:
   N.err('Escreve n\xfameros decimais (n\xe3o fra\xe7\xf5es): '+s)
  t=N._clean(s).lstrip('+-')
  j=0
  while j<len(t)and(N.dig(t[j])or t[j]in ',.'):
   j+=1
  mant=t[:j]
  m=N._dn(mant)
  ex=0
  if m!=0 and v!=0:
   ex=int(math.floor(math.log(abs(v)/m)/N.LN10+0.5))
  return(v,sf,N.dps(mant)-ex,mant,ex)
 def sf():
  return('Algarismos significativos',[N.fld('Opera\xe7\xe3o','','','c',['contar e arredondar','soma','subtra\xe7\xe3o (1.\xba - restantes)','multiplica\xe7\xe3o','divis\xe3o (1.\xba / restantes)']),N.fld('N\xfameros (separa com espa\xe7os)',
'','0,0250 12,3','t'),N.fld('Arredondar a (alg. sig., opcional)','','','o')],_sf)
 def why(mant):
  d=mant.replace('.',',')
  g=d.replace(',','')
  lz=len(g)-len(g.lstrip('0'))
  o=[]
  if lz and g.strip('0'):
   o.append(str(lz)+' zero(s) \xe0 esquerda n\xe3o contam')
  tz=len(g)-len(g.rstrip('0'))
  if tz and g.strip('0'):
   if ','in d:
    o.append(str(tz)+' zero(s) \xe0 direita, depois da v\xedrgula, contam')
   else:
    o.append(str(tz)+' zero(s) \xe0 direita sem v\xedrgula s\xe3o amb\xedguos (contados); usa nota\xe7\xe3o cient\xedfica')
  return '; '.join(o)
 def _sf(v):
  op,txt,rn=v
  ps=N.lst(txt)
  if not ps:
   N.err('Escreve pelo menos um n\xfamero')
  xs=[info(p)for p in ps]
  o=[]
  if op==0:
   for p,x in zip(ps,xs):
    s=p+': '+str(x[1])+' alg. sig.'
    w=why(x[3])
    if w:
     s=s+' ('+w+')'
    o.append('- '+s)
    if rn is not None:
     n=int(rn[0])
     N.need(n>=1 and n==rn[0],'Arredonda a um n\xfamero inteiro de algarismos (1, 2, 3...)')
     o.append('> arredondado a '+str(n)+': '+N.fsf(x[0],n))
   return('\n'.join(o),'Regras: contam todos os algarismos diferentes de zero, os zeros entre eles e os zeros \xe0 direita depois da v\xedrgula. Os zeros \xe0 esquerda s\xf3 marcam a posi\xe7\xe3o.',
None,'')
  N.need(len(xs)>=2,'Escreve pelo menos dois n\xfameros')
  if op in(1,2):
   D=max([x[2]for x in xs]+[0])
   S=0
   for i in range(len(xs)):
    k=int(N._rnd(abs(N._sc(xs[i][0],D))))
    k=-k if xs[i][0]<0 else k
    S=S+k if op==1 or i==0 else S-k
   r=S/N._p10(D)if D<=22 else N._sc(float(S),-D)
   d=min([x[2]for x in xs])
   if d>=0:
    q=10**(D-d)
    m=(abs(S)+q//2)//q
    s=('-'if S<0 and m else '')+N._ds(m,d)
   else:
    n=N._e10(abs(r))+d+1 if r!=0 else 1
    s=N.fsf(r,max(1,n))
   t=(' + 'if op==1 else ' - ').join(ps)
   o.append('= '+t+' = '+N.fmt(r,0,12))
   o.append('Regra da '+('soma'if op==1 else 'subtra\xe7\xe3o')+': o resultado fica com as casas decimais do dado com menos casas ('+str(d)+').')
   o.append('> '+s)
   return('\n'.join(o),'',N.num(s)[0],'')
  r=xs[0][0]
  for x in xs[1:]:
   if op==3:
    r=r*x[0]
   else:
    N.need(x[0]!=0,'Divis\xe3o por zero')
    r=r/x[0]
  n=min([x[1]for x in xs])
  t=(' '+X+' 'if op==3 else ' / ').join(ps)
  o.append('= '+t+' = '+N.fmt(r,0,12))
  o.append('Regra do produto e do quociente: o resultado fica com os algarismos significativos do dado com menos ('+str(n)+').')
  s=N.fsf(r,n)
  o.append('> '+s)
  return('\n'.join(o),'',N.num(s)[0],'')
 CATS=(('L','Comprimento'),('M','Massa'),('t','Tempo'),('A','\xc1rea'),('V','Volume'),('T','Temperatura'),('E','Energia'),('W','Pot\xeancia'),('p','Press\xe3o'),('n','Quantidade de mat\xe9ria'),('c','Concentra\xe7\xe3o'),
('m','Concentra\xe7\xe3o m\xe1ssica'),('d','Massa vol\xfamica'),('v','Velocidade'),('F','For\xe7a'),('I','Corrente el\xe9trica'),('U','Diferen\xe7a de potencial'),('R','Resist\xeancia el\xe9trica'),('f',
'Frequ\xeancia'),('Q','Carga el\xe9trica'))
 def uni():
  r=U.menu('Conversor de unidades',[c[1]for c in CATS])
  if r<0:
   return None
  cat=CATS[r][0]
  us=N.ulist(cat)
  f=N.fld('Valor',' '.join(us),'1')
  return(CATS[r][1],[f,N.fld('Converter para','','','c',us)],lambda v:_uni(v,cat,us,f))
 def _uni(v,cat,us,f):
  x=v[0][0]
  u0=us[0]
  ui=us[f[3]]
  uo=us[v[1]]
  r=N.conv(x,u0,uo,cat)
  xi=N.conv(x,u0,ui,cat)
  s=N.fmt(xi,0,12)+' '+ui
  o=['= '+s+' = '+N.fmt(r,0,12)+' '+uo]
  if cat=='T':
   o.append('T (K) = \u03b8 (\xb0C) + 273,15')
  else:
   k=N.conv(1.0,ui,uo,cat)
   o.append('1 '+ui+' = '+N.fmt(k,0,12)+' '+uo)
  sf=v[0][1]
  if sf:
   o.append('> '+N.fsf(r,sf)+' '+uo+' ('+str(sf)+' alg. sig.)')
  return('\n'.join(o),'Para converter, multiplica-se pelo fator de convers\xe3o (uma fra\xe7\xe3o igual a 1).',r,uo)
 PREF=('tera T 10\xb9\xb2','giga G 10\u2079','mega M 10\u2076','quilo k 10\xb3','hecto h 10\xb2','deca da 10\xb9','deci d 10\u207b\xb9','centi c 10\u207b\xb2','mili m 10\u207b\xb3','micro \xb5 10\u207b\u2076',
'nano n 10\u207b\u2079','pico p 10\u207b\xb9\xb2','femto f 10\u207b\xb9\u2075')
 def pre():
  return('Prefixos do SI',[],_pre)
 def _pre(v):
  o=['Prefixo, s\xedmbolo e fator:']
  for p in PREF:
   a=p.split(' ')
   o.append('- '+a[0]+' ('+a[1]+') = '+a[2])
  o.append('Exemplo: 2,5 km = 2,5 '+X+' 10\xb3 m; 3 mL = 3 '+X+' 10\u207b\xb3 L.')
  return('\n'.join(o),'',None,'')
 return _ns('N U X sci sf uni pre',N,U,X,sci,sf,uni,pre)


_F['c_comu'] = _m_c_comu


def _m_c_fqat():
 N=_imp('m1_nucleo')
 X=N.X
 NA=6.02e+23
 VM=22.4
 SUB='\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089'
 AR=('H 1.01 He 4.00 Li 6.94 Be 9.01 B 10.81 C 12.01 N 14.01 O 16.00 F 19.00 Ne 20.18 Na 22.99 Mg 24.31 Al 26.98 Si 28.09 P 30.97 S 32.06 Cl 35.45 Ar 39.95 K 39.10 Ca 40.08 Sc 44.96 Ti 47.87 V 50.94 Cr 52.0'
'0 Mn 54.94 Fe 55.85 Co 58.93 Ni 58.69 Cu 63.55 Zn 65.38 Ga 69.72 Ge 72.63 As 74.92 Se 78.97 Br 79.90 Kr 83.80 Rb 85.47 Sr 87.62 Y 88.91 Zr 91.22 Nb 92.91 Mo 95.95 Tc 98 Ru 101.07 Rh 102.91 Pd 106.42 A'
'g 107.87 Cd 112.41 In 114.82 Sn 118.71 Sb 121.76 Te 127.60 I 126.90 Xe 131.29 Cs 132.91 Ba 137.33 La 138.91 Ce 140.12 Pr 140.91 Nd 144.24 Pm 145 Sm 150.36 Eu 151.96 Gd 157.25 Tb 158.93 Dy 162.50 Ho 16'
'4.93 Er 167.26 Tm 168.93 Yb 173.05 Lu 174.97 Hf 178.49 Ta 180.95 W 183.84 Re 186.21 Os 190.23 Ir 192.22 Pt 195.08 Au 196.97 Hg 200.59 Tl 204.38 Pb 207.20 Bi 208.98 Po 209 At 210 Rn 222 Fr 223 Ra 226 A'
'c 227 Th 232.04 Pa 231.04 U 238.03 Np 237 Pu 244 Am 243 Cm 247 Bk 247 Cf 251 Es 252 Fm 257 Md 258 No 259 Lr 262 Rf 267 Db 268 Sg 269 Bh 270 Hs 269 Mt 278 Ds 281 Rg 282 Cn 285 Nh 286 Fl 289 Mc 290 Lv 2'
'93 Ts 294 Og 294')
 _T={}
 def ar_of(s):
  if not _T:
   p=AR.split(' ')
   for i in range(0,len(p)-1,2):
    _T[p[i]]=p[i+1]
  return _T.get(s)
 def _num(p,i):
  j=i
  while j<len(p)and N.dig(p[j]):
   j+=1
  return(int(p[i:j])if j>i else 1,j)
 def norm(s):
  o=[]
  for c in s:
   k=SUB.find(c)
   o.append(str(k)if k>=0 else c)
  s=''.join(o).replace(' ','').replace('\xb7','.').replace('*','.')
  ch=''
  k=s.find('^')
  if k>=0:
   ch=s[k+1:]
   s=s[:k]
  else:
   e=len(s)
   while e>0 and s[e-1]in '\u207a\u207b\xb2\xb3\xb9\u2074':
    e-=1
   if e<len(s):
    ch=N.P.vis(s[e:],0).lstrip('^')
    s=s[:e]
   elif s.endswith('+')or s.endswith('-'):
    ch=s[-1]
    s=s[:-1]
  return(s,ch)
 def parse(s):
  f,ch=norm(s)
  N.need(f!='','Escreve uma f\xf3rmula qu\xedmica, por exemplo H2SO4')
  tot=[]
  for part in f.split('.'):
   if part=='':
    N.err('Falta a parte depois do ponto (ex.: CuSO4.5H2O)')
   co,i=_num(part,0)
   st=[[]]
   p=part
   while i<len(p):
    c=p[i]
    if c in '([':
     st.append([])
     i+=1
    elif c in ')]':
     N.need(len(st)>1,'Par\xeantese a mais')
     g=st.pop()
     k,i=_num(p,i+1)
     for a,b in g:
      st[-1].append((a,b*k))
    elif 'A'<=c<='Z':
     sy=c
     i+=1
     if i<len(p)and 'a'<=p[i]<='z':
      sy+=p[i]
      i+=1
     N.need(ar_of(sy)is not None,'Elemento desconhecido: '+sy+' (Co \xe9 cobalto; CO \xe9 carbono + oxig\xe9nio)')
     k,i=_num(p,i)
     st[-1].append((sy,k))
    elif 'a'<=c<='z':
     N.err('Os s\xedmbolos come\xe7am por mai\xfascula: '+c)
    else:
     N.err('S\xedmbolo desconhecido na f\xf3rmula: '+c)
   N.need(len(st)==1,'Falta fechar um par\xeantese')
   for a,b in st[0]:
    for x in tot:
     if x[0]==a:
      x[1]+=b*co
      break
    else:
     tot.append([a,b*co])
  return(tot,ch)
 def pretty(s):
  f,ch=norm(s)
  o=[]
  idx=False
  for c in f:
   if N.dig(c):
    o.append(SUB[ord(c)-48]if idx else c)
   else:
    idx=c.isalpha()or c in ')]'
    o.append('\xb7'if c=='.'else c)
  if ch:
   if len(ch)>1 and ch[:-1].isdigit():
    o.append(N.sup(int(ch[:-1])))
   o.append('\u207a'if ch.endswith('+')else '\u207b')
  return ''.join(o)
 def mm():
  return('Massa molar',[N.fld('F\xf3rmula qu\xedmica (ex.: H2SO4, CuSO4.5H2O)','','H2O','t')],_mm)
 def _mm(v):
  tot,ch=parse(v[0])
  pf=pretty(v[0])
  M=0.0
  a=[]
  b=[]
  for s,n in tot:
   t=ar_of(s)
   M+=n*N._fl(t)
   a.append((str(n)+' '+X+' 'if n>1 else '')+'Ar('+s+')')
   b.append((str(n)+' '+X+' 'if n>1 else '')+t.replace('.',','))
  o=['= M('+pf+') = '+' + '.join(a),'= M = '+' + '.join(b),N.res('M',M,'g mol\u207b\xb9',0,2),'Composi\xe7\xe3o (% em massa):']
  for s,n in tot:
   w=n*N._fl(ar_of(s))/M*100
   o.append('- '+s+': '+N.fix(w,2)+' %')
  if ch:
   o.append('A carga ('+ch+') n\xe3o muda a massa molar: a massa dos eletr\xf5es \xe9 desprez\xe1vel.')
  st='Ar com 2 casas decimais, como na tabela peri\xf3dica do exame.\nA massa molar em g/mol tem o mesmo valor que a massa molecular relativa Mr.'
  return('\n'.join(o),st,M,'g/mol')
 def qm():
  return('Quantidade de mat\xe9ria',[N.fld('Massa molar M (g/mol, se usas a massa)','','','o'),N.fld('Massa m','g kg mg','','o'),N.fld('Quantidade n','mol mmol','','o'),N.fld('N.\xba de part\xedculas N',
'','','o'),N.fld('Volume de g\xe1s em PTN V','dm\xb3 L mL cm\xb3 m\xb3','','o')],_qm)
 def _qm(v):
  Mm,m,n,Np,V=v
  dados=[x for x in(m,n,Np,V)if x is not None]
  N.need(len(dados)==1,'Preenche s\xf3 um dos campos m, n, N ou V (e M se usares a massa)')
  o=[]
  if m is not None:
   N.need(Mm is not None,'Para usar a massa, escreve a massa molar M')
   N.pos(m[0],'A massa')
   N.pos(Mm[0],'A massa molar')
   s=N.sfm(m[1],Mm[1])
   q=m[0]/Mm[0]
   o+=['= n = m / M','= n = '+N.q(m[0],m[1],'g')+' / '+N.q(Mm[0],Mm[1],'g mol\u207b\xb9'),N.res('n',q,'mol',s)]
  elif n is not None:
   N.pos(n[0],'A quantidade')
   q=n[0]
   s=N.sfm(n[1])
   o.append('n = '+N.q(q,s,'mol'))
  elif Np is not None:
   N.pos(Np[0],'O n\xfamero de part\xedculas')
   s=N.sfm(Np[1],3)
   q=Np[0]/NA
   o+=['= n = N / NA','= n = '+N.q(Np[0],Np[1])+' / '+N.q(NA,3,'mol\u207b\xb9'),N.res('n',q,'mol',s)]
  else:
   N.pos(V[0],'O volume')
   s=N.sfm(V[1],3)
   q=V[0]/VM
   o+=['= n = V / Vm','= n = '+N.q(V[0],V[1],'dm\xb3')+' / '+N.q(VM,3,'dm\xb3 mol\u207b\xb9'),N.res('n',q,'mol',s)]
  if m is None and Mm is not None:
   s2=N.sfm(s,Mm[1])
   o+=['= m = n '+X+' M',N.res('m',q*Mm[0],'g',s2)]
  if Np is None:
   o+=['= N = n '+X+' NA = '+N.q(q,s)+' '+X+' '+N.q(NA,3),N.res('N',q*NA,'',N.sfm(s,3))]
  if V is None:
   o+=['= V = n '+X+' Vm (s\xf3 para gases em PTN)',N.res('V',q*VM,'dm\xb3',N.sfm(s,3))]
  st='NA = 6,02 '+X+' 10\xb2\xb3 mol\u207b\xb9 e Vm = 22,4 dm\xb3 mol\u207b\xb9 (tabela de constantes do exame; 3 alg. sig.).\nO resultado tem os algarismos significativos do dado com menos.'
  return('\n'.join(o),st,q,'mol')
 def ar():
  return('Massa at\xf3mica relativa m\xe9dia',[N.fld('Massas isot\xf3picas relativas','','','l'),N.fld('Abund\xe2ncias em %','','','l')],_ar)
 def _ar(v):
  ms,ab=v
  N.need(len(ms)==len(ab),'Escreve tantas abund\xe2ncias como massas')
  N.need(len(ms)>=1,'Escreve pelo menos um is\xf3topo')
  s=sum([a[0]for a in ab])
  for a in ab:
   N.need(a[0]>=0,'As abund\xe2ncias n\xe3o podem ser negativas')
  N.need(s>0,'As abund\xe2ncias somam 0 %')
  r=sum([ms[i][0]*ab[i][0]for i in range(len(ms))])/s
  sf=N.sfm(*[x[1]for x in ms]+[x[1]for x in ab])
  t=' + '.join([N.q(ms[i][0],ms[i][1])+' '+X+' '+N.q(ab[i][0],ab[i][1])for i in range(len(ms))])
  o=['= Ar m\xe9dio = \u03a3 (Ar(i) '+X+' abund\xe2ncia(i)) / 100','= Ar m\xe9dio = ('+t+') / 100',N.res('Ar m\xe9dio',r,'',sf)]
  if abs(s-100)>0.1:
   o.append('! As abund\xe2ncias somam '+N.fmt(s,0,3)+' % (e n\xe3o 100 %): dividi pela soma. Confirma os dados.')
  return('\n'.join(o),'A massa at\xf3mica relativa m\xe9dia \xe9 a m\xe9dia pesada das massas dos is\xf3topos.',r,'')
 def fr():
  return('Fra\xe7\xe3o molar e m\xe1ssica',[N.fld('Tipo','','','c',['fra\xe7\xe3o molar (n em mol)','fra\xe7\xe3o m\xe1ssica (m em g)']),N.fld('Quantidades ou massas','','','l'),N.fld('Nomes dos componentes (opcional)',
'','','t')],_fr)
 def _fr(v):
  tp,xs,nm=v
  N.need(len(xs)>=2,'Uma mistura tem pelo menos 2 componentes')
  for x in xs:
   N.need(x[0]>=0,'Os valores n\xe3o podem ser negativos')
  tot=sum([x[0]for x in xs])
  N.need(tot>0,'O total \xe9 zero')
  ns=[x for x in nm.replace(';',' ').split(' ')if x]if nm else[]
  sy='x'if tp==0 else 'w'
  o=['= '+sy+'(i) = '+('n(i) / n total'if tp==0 else 'm(i) / m total'),'Total = '+N.fmt(tot,0,6)+(' mol'if tp==0 else ' g')]
  sf=N.sfm(*[x[1]for x in xs])
  for i in range(len(xs)):
   lab=ns[i]if i<len(ns)and ns[i]else 'componente '+str(i+1)
   f=xs[i][0]/tot
   o.append('> '+sy+'('+lab+') '+N.eq(f,sf)+' ('+N.fix(f*100,2)+' %)')
  o.append('A soma das fra\xe7\xf5es \xe9 1 (100 %).')
  return('\n'.join(o),'',xs[0][0]/tot,'')
 return _ns('N X NA norm mm qm ar fr',N,X,NA,norm,mm,qm,ar,fr)


_F['c_fqat'] = _m_c_fqat


def _m_c_fqci():
 N=_imp('m1_nucleo')
 X=N.X
 US='V mV kV'
 IS='A mA \xb5A'
 RS='\u03a9 k\u03a9 M\u03a9 m\u03a9'
 MAT='cobre|1.7e-8 alum\xednio|2.7e-8 tungst\xe9nio|5.6e-8 ferro|9.7e-8 constantan|4.9e-7 n\xedquel-cr\xf3mio|1.1e-6'
 def um(v,nome):
  f=[i for i in range(len(v))if v[i]is None]
  N.need(len(f)==1,'Deixa vazio s\xf3 o campo que queres calcular ('+nome+')')
  return f[0]
 def todos_pos(v,nomes):
  for x,nm in zip(v,nomes):
   if x is not None:
    N.pos(x[0],nm)
 def ohm():
  return('Resist\xeancia el\xe9trica',[N.fld('Diferen\xe7a de potencial U',US,'','o'),N.fld('Resist\xeancia R',RS,'','o'),N.fld('Corrente el\xe9trica I',IS,'','o')],_ohm)
 def _ohm(v):
  U,R,I=v
  k=um(v,'U, R ou I')
  todos_pos(v,('A diferen\xe7a de potencial','A resist\xeancia','A corrente'))
  s=N.sfv(*v)
  if k==0:
   r=R[0]*I[0]
   o=['= U = R I = '+N.q(R[0],R[1],'\u03a9')+' '+X+' '+N.q(I[0],I[1],'A'),N.res('U',r,'V',s)]
   U=(r,s)
   u='V'
  elif k==1:
   r=U[0]/I[0]
   o=['= R = U / I = '+N.q(U[0],U[1],'V')+' / '+N.q(I[0],I[1],'A'),N.res('R',r,'\u03a9',s)]
   u='\u03a9'
  else:
   r=U[0]/R[0]
   o=['= I = U / R = '+N.q(U[0],U[1],'V')+' / '+N.q(R[0],R[1],'\u03a9'),N.res('I',r,'A',s)]
   I=(r,s)
   u='A'
  o.append('Pot\xeancia: P = U I = '+N.q(U[0]*I[0],s,'W'))
  st='R = U / I define a resist\xeancia (em \u03a9 = V/A).\nCondutor \xf3hmico: R constante (a temperatura constante); o gr\xe1fico U(I) \xe9 uma reta que passa na origem.'
  return('\n'.join(o),st,r,u)
 def rho():
  return('Resistividade',[N.fld('Material','','','c',['escrevo \u03c1']+[x.split('|')[0]for x in MAT.split(' ')]),N.fld('Resistividade \u03c1 (\u03a9 m)','','','o'),N.fld('Comprimento \u2113','m cm km mm',
'','o'),N.fld('\xc1rea da sec\xe7\xe3o A','mm\xb2 cm\xb2 m\xb2','','o'),N.fld('Resist\xeancia R',RS,'','o')],_rho)
 def _rho(v):
  m,p,l,a,R=v
  if a is not None:
   a=(a[0]*1e-06,a[1])
  if m:
   N.need(p is None,'Escolheste um material: deixa \u03c1 vazio')
   p=(float(MAT.split(' ')[m-1].split('|')[1]),2)
  w=[p,l,a,R]
  k=um(w,'\u03c1, \u2113, A ou R')
  todos_pos(w,('A resistividade','O comprimento','A \xe1rea','A resist\xeancia'))
  s=N.sfv(*w)
  o=['= R = \u03c1 \u2113 / A']
  if m:
   o.append('\u03c1('+MAT.split(' ')[m-1].split('|')[0]+') = '+N.q(p[0],2,'\u03a9 m')+' (a 20 \xb0C)')
  if k==3:
   r=p[0]*l[0]/a[0]
   o+=['R = '+N.q(p[0],p[1],'\u03a9 m')+' '+X+' '+N.q(l[0],l[1],'m')+' / ('+N.q(a[0],a[1],'m\xb2')+')',N.res('R',r,'\u03a9',s)]
   u='\u03a9'
  elif k==0:
   r=R[0]*a[0]/l[0]
   o+=['\u03c1 = R A / \u2113',N.res('\u03c1',r,'\u03a9 m',s)]
   u='\u03a9 m'
  elif k==1:
   r=R[0]*a[0]/p[0]
   o+=['\u2113 = R A / \u03c1',N.res('\u2113',r,'m',s)]
   u='m'
  else:
   r=p[0]*l[0]/R[0]
   o+=['A = \u03c1 \u2113 / R',N.res('A',r,'m\xb2',s),'= '+N.fmt(r*1000000.0,s)+' mm\xb2']
   u='m\xb2'
  st='A resist\xeancia aumenta com o comprimento e diminui com a \xe1rea da sec\xe7\xe3o.\n\u03c1 depende do material e da temperatura (nos metais, aumenta com a temperatura).\n1 mm\xb2 = 10\u207b\u2076 m\xb2.'
  return('\n'.join(o),st,r,u)
 def assoc():
  return('Resist\xeancias em s\xe9rie e em paralelo',[N.fld('Associa\xe7\xe3o','','','c',['em s\xe9rie','em paralelo']),N.fld('Resist\xeancias em \u03a9 (separa com espa\xe7os)','','10 20 30','l'),N.fld('Diferen\xe7a de potencial total U (opcional)',
US,'','o')],_assoc)
 def _assoc(v):
  k,rs,U=v
  N.need(len(rs)>=2,'Escreve pelo menos duas resist\xeancias')
  N.need(len(rs)<=10,'No m\xe1ximo 10 resist\xeancias')
  for x in rs:
   N.pos(x[0],'Cada resist\xeancia')
  s=N.sfm(*[x[1]for x in rs])
  if k==0:
   r=sum([x[0]for x in rs])
   o=['= Req = R1 + R2 + ...',N.res('Req',r,'\u03a9',s),'Req \xe9 maior do que a maior resist\xeancia.']
  else:
   r=1/sum([1/x[0]for x in rs])
   o=['= 1/Req = 1/R1 + 1/R2 + ...',N.res('Req',r,'\u03a9',s),'Req \xe9 menor do que a menor resist\xeancia.']
  if U is not None:
   N.pos(U[0],'A diferen\xe7a de potencial')
   s2=N.sfm(s,U[1])
   i=U[0]/r
   o.append(N.res('I total',i,'A',s2))
   for j in range(len(rs)):
    if k==0:
     o.append('R'+str(j+1)+': I = '+N.fmt(i,s2)+' A; U = '+N.fmt(rs[j][0]*i,s2)+' V')
    else:
     o.append('R'+str(j+1)+': U = '+N.fmt(U[0],s2)+' V; I = '+N.fmt(U[0]/rs[j][0],s2)+' A')
  st='S\xe9rie: a mesma corrente em todas; as tens\xf5es somam-se.\nParalelo: a mesma tens\xe3o em todas; as correntes somam-se.'
  return('\n'.join(o),st,r,'\u03a9')
 def ger():
  return('Gerador',[N.fld('For\xe7a eletromotriz \u03b5',US,'','o'),N.fld('Resist\xeancia interna r',RS,'','o'),N.fld('Corrente I',IS,'','o'),N.fld('Tens\xe3o nos terminais U',US,'','o')],_ger)
 def _ger(v):
  e,ri,I,U=v
  k=um(v,'\u03b5, r, I ou U')
  for x,nm in((e,'A for\xe7a eletromotriz'),(I,'A corrente')):
   if x is not None:
    N.pos(x[0],nm)
  for x,nm in((ri,'A resist\xeancia interna'),(U,'A tens\xe3o')):
   if x is not None:
    N.nneg(x[0],nm)
  s=N.sfv(*v)
  o=['= U = \u03b5 - r I']
  if k==3:
   r=e[0]-ri[0]*I[0]
   N.need(r>=0,'Com esta corrente U < 0: maior do que a de curto-circuito (\u03b5 / r)')
   o.append(N.res('U',r,'V',s))
   U=(r,s)
   u='V'
  elif k==0:
   r=U[0]+ri[0]*I[0]
   o+=['\u03b5 = U + r I',N.res('\u03b5',r,'V',s)]
   e=(r,s)
   u='V'
  elif k==1:
   N.need(U[0]<=e[0],'U n\xe3o pode ser maior do que \u03b5 num gerador')
   r=(e[0]-U[0])/I[0]
   o+=['r = (\u03b5 - U) / I',N.res('r',r,'\u03a9',s)]
   ri=(r,s)
   u='\u03a9'
  else:
   N.need(U[0]<=e[0],'U n\xe3o pode ser maior do que \u03b5 num gerador')
   N.need(ri[0]>0,'Com r = 0 a corrente n\xe3o fica determinada')
   r=(e[0]-U[0])/ri[0]
   o+=['I = (\u03b5 - U) / r',N.res('I',r,'A',s)]
   I=(r,s)
   u='A'
  pe=e[0]*I[0]
  pu=U[0]*I[0]
  o+=['Pot\xeancias: gerada \u03b5 I = '+N.q(pe,s,'W')+';','\xfatil U I = '+N.q(pu,s,'W')+'; dissipada r I\xb2 = '+N.q(ri[0]*I[0]**2,s,'W')]
  if pe>0:
   o.append('Rendimento: \u03b7 = U / \u03b5 = '+N.fmt(pu/pe*100,s)+' %')
  if ri[0]>0:
   o.append('Curto-circuito: I = \u03b5 / r = '+N.q(e[0]/ri[0],s,'A'))
  st='O gerador fornece \u03b5 I; parte dissipa-se dentro dele (r I\xb2) e o resto vai para o circuito (U I).\nGr\xe1fico U(I): reta de declive -r e ordenada na origem \u03b5.'
  return('\n'.join(o),st,r,u)
 def pot():
  return('Pot\xeancia, energia e custo',[N.fld('Pot\xeancia P (preenche 2 de P, U, I, R)','W kW mW','','o'),N.fld('Tens\xe3o U',US,'','o'),N.fld('Corrente I',IS,'','o'),N.fld('Resist\xeancia R',RS,'','o'),
N.fld('Tempo de funcionamento \u0394t (opcional)','h min s','','o'),N.fld('Pre\xe7o do kWh em euros (opcional)','','','o')],_pot)
 def _pot(v):
  P,U,I,R,t,c=v
  d=[P,U,I,R]
  N.need(len([x for x in d if x is not None])==2,'Preenche exatamente dois de P, U, I e R')
  todos_pos(d,('A pot\xeancia','A tens\xe3o','A corrente','A resist\xeancia'))
  s=N.sfv(*d)
  o=[]
  if U is not None and I is not None:
   p=U[0]*I[0]
   o.append('= P = U I')
  elif I is not None and R is not None:
   p=R[0]*I[0]**2
   o.append('= P = R I\xb2 (efeito Joule)')
  elif U is not None and R is not None:
   p=U[0]**2/R[0]
   o.append('= P = U\xb2 / R')
  elif U is not None:
   p=P[0]
   o+=['= I = P / U',N.res('I',p/U[0],'A',s)]
  elif I is not None:
   p=P[0]
   o+=['= U = P / I',N.res('U',p/I[0],'V',s)]
  else:
   p=P[0]
   o+=['= I = \u221a(P / R)',N.res('I',(p/R[0])**0.5,'A',s)]
  if P is None:
   o.append(N.res('P',p,'W',s))
  r=p
  u='W'
  if t is not None:
   N.pos(t[0],'O tempo')
   s2=N.sfm(s,t[1])
   e=p*t[0]*3600
   o+=['= E = P \u0394t',N.res('E',e,'J',s2),'= '+N.fmt(e/3600000.0,s2)+' kWh (1 kWh = 3,6 '+X+' 10\u2076 J)']
   r=e
   u='J'
   if c is not None:
    N.nneg(c[0],'O pre\xe7o')
    o.append('Custo: '+N.fmt(e/3600000.0,s2)+' kWh '+X+' '+N.fmt(c[0])+' \u20ac/kWh = '+N.fix(e/3600000.0*c[0],2)+' \u20ac')
  st='P = U I = R I\xb2 = U\xb2 / R.\nEfeito Joule: num condutor a energia el\xe9trica passa a energia interna (aquecimento).\nEnergia em kWh: P em kW vezes \u0394t em horas.'
  return('\n'.join(o),st,r,u)
 return _ns('N X um ohm rho assoc ger pot',N,X,um,ohm,rho,assoc,ger,pot)


_F['c_fqci'] = _m_c_fqci


def _m_c_fqel():
 N=_imp('m1_nucleo')
 X=N.X
 H=6.63e-34
 C=300000000.0
 NA=6.02e+23
 E1=2.18e-18
 EV=1.6e-19
 REG=((1e-11,'raios gama'),(1e-08,'raios X'),(4e-07,'ultravioleta'),(7e-07,'vis\xedvel'),(0.001,'infravermelho'),(1.0,'micro-ondas'),(1e+99,'ondas de r\xe1dio'))
 COR=((4.5e-07,'violeta'),(4.95e-07,'azul'),(5.7e-07,'verde'),(5.9e-07,'amarelo'),(6.2e-07,'laranja'),(7e-07,'vermelho'))
 def regiao(lam):
  for lim,nm in REG:
   if lam<lim:
    if nm=='vis\xedvel':
     for l2,c in COR:
      if lam<l2:
       return 'vis\xedvel ('+c+')'
    return nm
  return REG[-1][1]
 def fot():
  return('Espetros e fot\xf5es',[N.fld('Valor conhecido (\u03bb, f ou E)','nm m \xb5m pm Hz THz PHz J eV','500','u')],_fot)
 def _fot(v):
  x,sf,iu=v[0]
  N.pos(x,'O valor')
  s=N.sfm(sf,3)
  o=[]
  if iu<=3:
   lam=x*(1e-09,1.0,1e-06,1e-12)[iu]
   f=C/lam
   e=H*f
   o+=['= f = c / \u03bb = '+N.q(C,3,'m s\u207b\xb9')+' / '+N.q(lam,sf,'m'),N.res('f',f,'Hz',s)]
   o+=['= E = h f',N.res('E',e,'J',s)]
  elif iu<=6:
   f=x*(1.0,1000000000000.0,1000000000000000.0)[iu-4]
   lam=C/f
   e=H*f
   o+=['= \u03bb = c / f',N.res('\u03bb',lam,'m',s),'= E = h f = '+N.q(H,3)+' J s '+X+' '+N.q(f,sf,'Hz'),N.res('E',e,'J',s)]
  else:
   e=x*(1.0,EV)[iu-7]
   f=e/H
   lam=C/f
   o+=['= f = E / h',N.res('f',f,'Hz',s),'= \u03bb = c / f',N.res('\u03bb',lam,'m',s)]
  o.append('\u03bb = '+N.fmt(lam*1000000000.0,s)+' nm')
  o.append('E = '+N.fmt(e/EV,s)+' eV por fot\xe3o')
  o.append('Por mole de fot\xf5es: '+N.fmt(e*NA/1000,s)+' kJ mol\u207b\xb9')
  o.append('Regi\xe3o do espetro: '+regiao(lam)+' (limites aproximados)')
  st='h = 6,63 '+X+' 10\u207b\xb3\u2074 J s e c = 3,00 '+X+' 10\u2078 m s\u207b\xb9.\nQuanto maior a frequ\xeancia, maior a energia e menor o comprimento de onda.'
  return('\n'.join(o),st,e,'J')
 def hid():
  return('\xc1tomo de hidrog\xe9nio',[N.fld('n inicial','','3'),N.fld('n final (0 = ioniza\xe7\xe3o)','','2')],_hid)
 def en(n):
  return-E1/(n*n)
 def _hid(v):
  ni,nf=(v[0][0],v[1][0])
  N.need(ni==int(ni)and nf==int(nf),'Os n\xedveis s\xe3o n\xfameros inteiros (1, 2, 3...)')
  ni,nf=(int(ni),int(nf))
  N.need(ni>=1,'O n\xedvel inicial \xe9 1 ou mais')
  N.need(nf>=0,'O n\xedvel final \xe9 1 ou mais (0 = ioniza\xe7\xe3o)')
  N.need(ni<=50 and nf<=50,'Usa n\xedveis at\xe9 50')
  N.need(ni!=nf,'O n\xedvel inicial e o final s\xe3o iguais: n\xe3o h\xe1 transi\xe7\xe3o')
  ei=en(ni)
  ef=0.0 if nf==0 else en(nf)
  d=ef-ei
  o=['= E\u2099 = -2,18 '+X+' 10\u207b\xb9\u2078 / n\xb2 J','E('+str(ni)+') = '+N.fmt(ei,3)+' J','E('+('\u221e'if nf==0 else str(nf))+') = '+N.fmt(ef,3)+' J','= \u0394E = E final - E inicial',N.res('\u0394E',
d,'J',3)]
  if d>0:
   o.append('Absor\xe7\xe3o: o eletr\xe3o recebe energia (sobe de n\xedvel).')
   if nf==0:
    o.append('n final = \u221e: \xe9 a energia de ioniza\xe7\xe3o a partir de n = '+str(ni)+'.')
  else:
   o.append('Emiss\xe3o: o \xe1tomo emite um fot\xe3o (o eletr\xe3o desce).')
  e=abs(d)
  lam=H*C/e
  o.append('Fot\xe3o: E = '+N.fmt(e,3)+' J; \u03bb = '+N.fmt(lam*1000000000.0,3)+' nm')
  o.append('Regi\xe3o: '+regiao(lam))
  lo=min(ni,nf)if nf else ni
  if nf!=0:
   ser={1:'Lyman (UV)',2:'Balmer (vis\xedvel e UV)',3:'Paschen (IV)'}.get(lo,'')
   if ser:
    o.append('S\xe9rie de '+ser+': n\xedvel mais baixo n = '+str(lo))
  st='O \xe1tomo s\xf3 absorve ou emite fot\xf5es com energia igual \xe0 diferen\xe7a entre dois n\xedveis: a energia est\xe1 quantizada.\n\u03bb = h c / E.'
  return('\n'.join(o),st,d,'J')
 ORB=('1s','2s','2p','3s','3p','4s','3d','4p')
 CAP=(2,2,6,2,6,2,10,6)
 SIMB=('H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr')
 def config(z):
  o=[]
  r=z
  for i in range(len(ORB)):
   if r<=0:
    break
   n=min(r,CAP[i])
   o.append([ORB[i],n])
   r-=n
  if z in(24,29):
   for x in o:
    if x[0]=='4s':
     x[1]=1
    if x[0]=='3d':
     x[1]+=1
  return o
 def caixas(o):
  s=[]
  for orb,n in o:
   k={'s':1,'p':3,'d':5}[orb[1]]
   cx=[]
   for i in range(k):
    e=(1 if n>i else 0)+(1 if n>i+k else 0)
    cx.append('['+('\u2191\u2193'if e==2 else '\u2191 'if e==1 else '  ')+']')
   s.append(orb+' '+''.join(cx))
  return s
 def conf():
  return('Configura\xe7\xe3o eletr\xf3nica',[N.fld('N\xfamero at\xf3mico Z (1 a 36)','','8'),N.fld('Carga do i\xe3o (0 = \xe1tomo)','','0')],_conf)
 def _conf(v):
  z,q=(v[0][0],v[1][0])
  N.need(z==int(z)and 1<=z<=36,'Escreve um Z inteiro de 1 a 36')
  N.need(q==int(q),'A carga \xe9 um n\xfamero inteiro (ex.: 2 ou -1)')
  z,q=(int(z),int(q))
  ne=z-q
  N.need(0<=ne<=36,'Esse i\xe3o teria '+str(ne)+' eletr\xf5es')
  if ne==0:
   return('Sem eletr\xf5es (\xe9 s\xf3 o n\xfacleo).','',None,'')
  o=config(ne)
  if q>0 and z>20:
   o=config(z)
   r=q
   for x in o:
    if x[0]=='4s':
     t=min(r,x[1])
     x[1]-=t
     r-=t
   for x in o[::-1]:
    if r and x[0]=='3d':
     t=min(r,x[1])
     x[1]-=t
     r-=t
   o=[x for x in o if x[1]]
  nome=SIMB[z-1]+(N.sup(abs(q))if abs(q)>1 else '')+('\u207a'if q>0 else '\u207b'if q<0 else '')
  t=[nome+' (Z = '+str(z)+', '+str(ne)+' eletr\xf5es)','> '+' '.join([x[0]+N.sup(x[1])for x in o])]
  t+=caixas(o)
  des=0
  for orb,n in o:
   k={'s':1,'p':3,'d':5}[orb[1]]
   des+=n if n<=k else 2*k-n
  t.append('Eletr\xf5es desemparelhados: '+str(des))
  if q==0 and z<=20:
   nmax=max([int(x[0][0])for x in o])
   val=sum([x[1]for x in o if int(x[0][0])==nmax])
   g=val if val<=2 else val+10
   if z==2:
    g=18
   t.append('Eletr\xf5es de val\xeancia: '+str(val))
   t.append('Posi\xe7\xe3o: per\xedodo '+str(nmax)+', grupo '+str(g)+', bloco '+o[-1][0][1])
  if ne>20:
   t.append('(Al\xe9m do programa do 10.\xba ano, que vai at\xe9 4s.)')
  if z in(24,29)and q==0:
   t.append('Exce\xe7\xe3o: '+SIMB[z-1]+' fica com 4s\xb9 (mais est\xe1vel).')
  st=('Princ\xedpio da Constru\xe7\xe3o: as orbitais enchem-se por ordem de energia: 1s 2s 2p 3s 3p 4s 3d 4p.\nPrinc\xedpio de Exclus\xe3o de Pauli: no m\xe1ximo 2 eletr\xf5es por orbital, com spins opostos.'
'\nRegra de Hund: nas orbitais com a mesma energia, primeiro um eletr\xe3o em cada uma, com o mesmo spin.')
  return('\n'.join(t),st,None,'')
 return _ns('N X H C NA fot hid conf',N,X,H,C,NA,fot,hid,conf)


_F['c_fqel'] = _m_c_fqel


def _m_c_fqen():
 import math
 N=_imp('m1_nucleo')
 X=N.X
 MS='kg g'
 VS='m/s km/h'
 HS='m cm km'
 ES='J kJ MJ Wh kWh'
 def g():
  return N.CF.get('g',10.0)
 def gtxt():
  return 'g = '+N.fmt(g())+' m s\u207b\xb2 (muda nas Defini\xe7\xf5es)'
 def pq(x,sf,u):
  s=N.q(x,sf,u)
  return '('+s+')'if x<0 else s
 def um(v,nome):
  f=[i for i in range(len(v))if v[i]is None]
  N.need(len(f)==1,'Deixa vazio s\xf3 o campo que queres calcular ('+nome+')')
  return f[0]
 def em():
  return('Energia mec\xe2nica',[N.fld('Massa m',MS,''),N.fld('Velocidade v (opcional)',VS,'','o'),N.fld('Altura h (opcional)',HS,'','o')],_em)
 def _em(v):
  m,vv,h=v
  N.pos(m[0],'A massa')
  N.need(vv is not None or h is not None,'Escreve a velocidade, a altura ou as duas')
  o=[]
  r=None
  ec=ep=0.0
  if vv is not None:
   N.nneg(vv[0],'A velocidade (m\xf3dulo)')
   ec=0.5*m[0]*vv[0]**2
   o+=['= Ec = \xbd m v\xb2 = \xbd '+X+' '+N.q(m[0],m[1],'kg')+' '+X+' ('+N.q(vv[0],vv[1],'m s\u207b\xb9')+')\xb2',N.res('Ec',ec,'J',N.sfv(m,vv))]
   r=ec
  if h is not None:
   ep=m[0]*g()*h[0]
   o+=['= Epg = m g h = '+N.q(m[0],m[1],'kg')+' '+X+' '+N.q(g(),0,'m s\u207b\xb2')+' '+X+' '+pq(h[0],h[1],'m'),N.res('Epg',ep,'J',N.sfv(m,h))]
   r=ep
  if vv is not None and h is not None:
   r=ec+ep
   o+=['= Em = Ec + Epg',N.res('Em',r,'J',N.sfv(m,vv,h))]
  if h is not None and h[0]<0:
   o.append('h < 0: o corpo est\xe1 abaixo do n\xedvel de refer\xeancia.')
  st='Ec = \xbd m v\xb2 (m em kg, v em m/s).\nEpg = m g h, com h medida a partir do n\xedvel de refer\xeancia (Epg = 0).\nEm = Ec + Epg.\n'+gtxt()
  return('\n'.join(o),st,r,'J')
 def cons():
  return('Conserva\xe7\xe3o da energia mec\xe2nica',[N.fld('Altura inicial hA',HS,'','o'),N.fld('Velocidade inicial vA',VS,'0','o'),N.fld('Altura final hB',HS,'0','o'),N.fld('Velocidade final vB',VS,'',
'o'),N.fld('Massa m (s\xf3 com energia dissipada)',MS,'','o'),N.fld('Energia dissipada Ed (opcional)','J kJ','','o')],_cons)
 def _cons(v):
  ha,va,hb,vb,m,ed=v
  falta=[i for i in range(4)if v[i]is None]
  N.need(len(falta)<=1,'Deixa vazio s\xf3 o campo que queres calcular (ou nenhum, para calcular a energia dissipada)')
  for x,nm in((va,'A velocidade inicial'),(vb,'A velocidade final')):
   if x is not None:
    N.nneg(x[0],nm+' (m\xf3dulo)')
  if m is not None:
   N.pos(m[0],'A massa')
  s=N.sfv(*v)
  gg=g()
  o=[]
  if not falta:
   N.need(ed is None,'Com os quatro campos preenchidos, a energia dissipada \xe9 o resultado: deixa-a vazia')
   ea=0.5*va[0]**2+gg*ha[0]
   eb=0.5*vb[0]**2+gg*hb[0]
   o+=['= Em/m = \xbd v\xb2 + g h (por kg)','A: '+N.fmt(ea,s)+' J/kg; B: '+N.fmt(eb,s)+' J/kg']
   d=ea-eb
   if ea>0:
    o.append(N.res('Dissipada',d/ea*100,'% de Em(A)',s))
   if m is not None:
    o.append(N.res('Ed',d*m[0],'J',s))
   if d<0:
    o.append('! A energia mec\xe2nica aumentou: houve uma for\xe7a a fornecer energia (por exemplo, um motor).')
   st='Ed = Em(A) - Em(B). Sem a massa, a app d\xe1 a energia por kg e a percentagem.\n'+gtxt()
   return('\n'.join(o),st,d,'J/kg')
  w=0.0
  if ed is not None:
   N.nneg(ed[0],'A energia dissipada')
   N.need(m is not None,'Com energia dissipada, escreve tamb\xe9m a massa')
   w=ed[0]/m[0]
   o.append('= \xbd m vA\xb2 + m g hA - Ed = \xbd m vB\xb2 + m g hB')
  else:
   o.append('= \xbd m vA\xb2 + m g hA = \xbd m vB\xb2 + m g hB')
   o.append('A massa aparece nos dois membros e corta-se.')
  k=falta[0]
  if k==3:
   q=va[0]**2+2*gg*(ha[0]-hb[0])-2*w
   N.need(q>=0,'Com estes dados o corpo n\xe3o chega \xe0 altura final')
   r=math.sqrt(q)
   o+=['vB = \u221a(vA\xb2 + 2 g (hA - hB)'+(' - 2 Ed/m'if w else '')+')',N.res('vB',r,'m s\u207b\xb9',s)]
   u='m/s'
  elif k==1:
   q=vb[0]**2+2*gg*(hb[0]-ha[0])+2*w
   N.need(q>=0,'Com estes dados n\xe3o h\xe1 velocidade inicial poss\xedvel')
   r=math.sqrt(q)
   o+=['vA = \u221a(vB\xb2 + 2 g (hB - hA)'+(' + 2 Ed/m'if w else '')+')',N.res('vA',r,'m s\u207b\xb9',s)]
   u='m/s'
  elif k==2:
   r=ha[0]+(va[0]**2-vb[0]**2)/(2*gg)-w/gg
   o+=['hB = hA + (vA\xb2 - vB\xb2) / (2 g)'+(' - Ed/(m g)'if w else ''),N.res('hB',r,'m',s)]
   u='m'
  else:
   r=hb[0]+(vb[0]**2-va[0]**2)/(2*gg)+w/gg
   o+=['hA = hB + (vB\xb2 - vA\xb2) / (2 g)'+(' + Ed/(m g)'if w else ''),N.res('hA',r,'m',s)]
   u='m'
  st='S\xf3 atuam for\xe7as conservativas (ou for\xe7as que n\xe3o realizam trabalho): Em(A) = Em(B).\nCom for\xe7as n\xe3o conservativas: Em(B) = Em(A) - Ed.\n'+gtxt()
  return('\n'.join(o),st,r,u)
 def tr():
  return('Trabalho de uma for\xe7a constante',[N.fld('Intensidade da for\xe7a F','N kN',''),N.fld('Deslocamento d',HS,''),N.fld('\xc2ngulo \u03b1 entre F e d (graus)','','0')],_tr)
 def _tr(v):
  F,d,a=v
  N.pos(F[0],'A for\xe7a')
  N.pos(d[0],'O deslocamento')
  N.need(0<=a[0]<=180,'O \xe2ngulo tem de estar entre 0\xb0 e 180\xb0')
  c=math.cos(a[0]*math.pi/180)
  if abs(c)<1e-12:
   c=0.0
  w=F[0]*d[0]*c
  s=N.sfv(F,d)
  o=['= W = F d cos \u03b1 = '+N.q(F[0],F[1],'N')+' '+X+' '+N.q(d[0],d[1],'m')+' '+X+' cos '+N.fmt(a[0])+'\xb0',N.res('W',w,'J',s),'Componente eficaz: F cos \u03b1 = '+N.q(F[0]*c,s,'N')]
  if c>0:
   o.append('Trabalho potente (W > 0): a for\xe7a favorece o movimento.')
  elif c==0:
   o.append('Trabalho nulo: a for\xe7a \xe9 perpendicular ao deslocamento.')
  else:
   o.append('Trabalho resistente (W < 0): a for\xe7a op\xf5e-se ao movimento.')
  st='S\xf3 a componente da for\xe7a na dire\xe7\xe3o do deslocamento realiza trabalho.\n0\xb0 \u2264 \u03b1 < 90\xb0: potente; \u03b1 = 90\xb0: nulo; 90\xb0 < \u03b1 \u2264 180\xb0: resistente.'
  return('\n'.join(o),st,w,'J')
 def wp():
  return('Trabalho do peso',[N.fld('Massa m',MS,''),N.fld('Altura inicial hi',HS,''),N.fld('Altura final hf',HS,'0')],_wp)
 def _wp(v):
  m,hi,hf=v
  N.pos(m[0],'A massa')
  s=N.sfv(m,hi,hf)
  w=m[0]*g()*(hi[0]-hf[0])
  o=['= W(P) = m g (hi - hf) = -\u0394Epg','P = m g = '+N.q(m[0]*g(),m[1],'N'),N.res('W(P)',w,'J',s),N.res('\u0394Epg',-w,'J',s)]
  if w>0:
   o.append('O corpo desce: trabalho potente e a Epg diminui.')
  elif w<0:
   o.append('O corpo sobe: trabalho resistente e a Epg aumenta.')
  else:
   o.append('Mesma altura: o trabalho do peso \xe9 nulo.')
  st='O peso \xe9 uma for\xe7a conservativa: o trabalho s\xf3 depende do desn\xedvel, n\xe3o da trajet\xf3ria.\nW(P) = -\u0394Epg.\n'+gtxt()
  return('\n'.join(o),st,w,'J')
 def tec():
  return('Teorema da energia cin\xe9tica',[N.fld('Massa m',MS,''),N.fld('Velocidade inicial vi',VS,'','o'),N.fld('Velocidade final vf',VS,'','o'),N.fld('Trabalho da resultante W','J kJ','','o'),N.fld('Deslocamento d (opcional)',
HS,'','o')],_tec)
 def _tec(v):
  m,vi,vf,w,d=v
  N.pos(m[0],'A massa')
  k=um(v[1:4],'vi, vf ou W')+1
  for x,nm in((vi,'A velocidade inicial'),(vf,'A velocidade final')):
   if x is not None:
    N.nneg(x[0],nm+' (m\xf3dulo)')
  s=N.sfv(*v[:4])
  o=['= W(resultante) = \u0394Ec = \xbd m vf\xb2 - \xbd m vi\xb2']
  if k==3:
   r=0.5*m[0]*(vf[0]**2-vi[0]**2)
   wr=r
   o.append(N.res('W',r,'J',s))
   u='J'
  elif k==2:
   q=vi[0]**2+2*w[0]/m[0]
   N.need(q>=0,'O corpo para antes: o trabalho resistente \xe9 maior do que a energia cin\xe9tica inicial')
   r=math.sqrt(q)
   wr=w[0]
   o+=['vf = \u221a(vi\xb2 + 2 W / m)',N.res('vf',r,'m s\u207b\xb9',s)]
   u='m/s'
  else:
   q=vf[0]**2-2*w[0]/m[0]
   N.need(q>=0,'N\xe3o h\xe1 velocidade inicial poss\xedvel com estes dados')
   r=math.sqrt(q)
   wr=w[0]
   o+=['vi = \u221a(vf\xb2 - 2 W / m)',N.res('vi',r,'m s\u207b\xb9',s)]
   u='m/s'
  if wr>0:
   o.append('W > 0: a energia cin\xe9tica aumenta.')
  elif wr<0:
   o.append('W < 0: a energia cin\xe9tica diminui.')
  if d is not None:
   N.pos(d[0],'O deslocamento')
   o+=['Se a resultante tiver a dire\xe7\xe3o do deslocamento:',N.res('F(R)',abs(wr)/d[0],'N',N.sfm(s,d[1]))]
  st='O trabalho da resultante das for\xe7as \xe9 igual \xe0 varia\xe7\xe3o da energia cin\xe9tica.\nW(R) = soma dos trabalhos de todas as for\xe7as.'
  return('\n'.join(o),st,r,u)
 def pot():
  return('Pot\xeancia',[N.fld('Energia E (vazio = calcular)',ES,'','o'),N.fld('Intervalo de tempo \u0394t','s min h','','o'),N.fld('Pot\xeancia P','W kW mW MW','','o')],_pot)
 def _pot(v):
  e,t,p=v
  k=um(v,'E, \u0394t ou P')
  for x,nm in((e,'A energia'),(t,'O intervalo de tempo'),(p,'A pot\xeancia')):
   if x is not None:
    N.pos(x[0],nm)
  s=N.sfv(*v)
  o=['= P = E / \u0394t']
  if k==0:
   r=p[0]*t[0]
   o+=['E = P \u0394t',N.res('E',r,'J',s),'= '+N.fmt(r/3600000.0,s)+' kWh (1 kWh = 3,6 '+X+' 10\u2076 J)']
   u='J'
  elif k==1:
   r=e[0]/p[0]
   o+=['\u0394t = E / P',N.res('\u0394t',r,'s',s)]
   if r>=60:
    o.append('= '+N.fmt(r/60,s)+' min = '+N.fmt(r/3600,s)+' h')
   u='s'
  else:
   r=e[0]/t[0]
   o+=[N.res('P',r,'W',s)]
   u='W'
  st='Pot\xeancia: energia transferida por unidade de tempo.\nUnidades SI: E em J, \u0394t em s, P em W (1 W = 1 J/s).'
  return('\n'.join(o),st,r,u)
 def ren():
  return('Rendimento',[N.fld('Energia (ou pot\xeancia) \xfatil','','','o'),N.fld('Energia (ou pot\xeancia) fornecida','','','o'),N.fld('Rendimento \u03b7 (%)','','','o')],_ren)
 def _ren(v):
  eu,ef,n=v
  k=um(v,'\xfatil, fornecida ou \u03b7')
  for x,nm in((eu,'A energia \xfatil'),(ef,'A energia fornecida'),(n,'O rendimento')):
   if x is not None:
    N.pos(x[0],nm)
  s=N.sfv(*v)
  o=['= \u03b7 = E(\xfatil) / E(fornecida) '+X+' 100 %']
  if k==2:
   N.need(eu[0]<=ef[0],'\u03b7 > 100 % \xe9 imposs\xedvel: a energia \xfatil n\xe3o pode ser maior do que a fornecida (trocaste-as?)')
   r=eu[0]/ef[0]*100
   o.append(N.res('\u03b7',r,'%',s))
   a,b=(eu[0],ef[0])
  else:
   N.need(n[0]<=100,'\u03b7 > 100 % \xe9 imposs\xedvel')
   if k==0:
    r=n[0]/100*ef[0]
    o+=['E(\xfatil) = \u03b7 '+X+' E(fornecida) / 100',N.res('E(\xfatil)',r,'',s)]
    a,b=(r,ef[0])
   else:
    r=eu[0]*100/n[0]
    o+=['E(fornecida) = E(\xfatil) '+X+' 100 / \u03b7',N.res('E(fornecida)',r,'',s)]
    a,b=(eu[0],r)
  o.append('Dissipada: '+N.fmt(b-a,s)+' ('+N.fmt((b-a)/b*100,s)+' % da fornecida)')
  o.append('Unidades: as da energia (ou pot\xeancia) que escreveste.')
  st='E(fornecida) = E(\xfatil) + E(dissipada).\nO rendimento \xe9 sempre menor do que 100 %: h\xe1 sempre energia dissipada.'
  return('\n'.join(o),st,r,'%'if k==2 else '')
 return _ns('N X g um em cons tr wp tec pot ren',N,X,g,um,em,cons,tr,wp,tec,pot,ren)


_F['c_fqen'] = _m_c_fqen


def _m_c_fqlg():
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 X=N.X
 MOL=('H\u2082|hidrog\xe9nio|2|1 simples|0|linear||apolar|H-H\nF\u2082|fl\xfaor|14|1 simples|6 (3 em cada F)|linear||apolar|F-F\nCl\u2082|cloro|14|1 simples|6 (3 em cada Cl)|linear||apolar|Cl-Cl\nO\u2082|oxi'
'g\xe9nio|12|1 dupla|4 (2 em cada O)|linear||apolar|O=O\nN\u2082|azoto|10|1 tripla|2 (1 em cada N)|linear||apolar|N\u2261N\nHF|fluoreto de hidrog\xe9nio|8|1 simples|3 (no F)|linear||polar|H-F\nHCl|clor'
'eto de hidrog\xe9nio|8|1 simples|3 (no Cl)|linear||polar|H-Cl\nH\u2082O|\xe1gua|8|2 simples|2 (no O)|angular|104,5\xb0|polar|H-O-H\nH\u2082S|sulfureto de hidrog\xe9nio|8|2 simples|2 (no S)|angular|92'
'\xb0|polar|H-S-H\nNH\u2083|amon\xedaco|8|3 simples|1 (no N)|piramidal trigonal|107\xb0|polar|H-N(-H)-H\nCH\u2084|metano|8|4 simples|0|tetra\xe9drica|109,5\xb0|apolar|C ligado a 4 H\nCCl\u2084|tetraclo'
'reto de carbono|32|4 simples|12 (3 em cada Cl)|tetra\xe9drica|109,5\xb0|apolar|C ligado a 4 Cl\nCO\u2082|di\xf3xido de carbono|16|2 duplas|4 (2 em cada O)|linear|180\xb0|apolar|O=C=O\nHCN|cianeto de h'
'idrog\xe9nio|10|1 simples e 1 tripla|1 (no N)|linear|180\xb0|polar|H-C\u2261N\nCH\u2082O|metanal|12|2 simples e 1 dupla|2 (no O)|triangular plana|120\xb0|polar|H\u2082C=O\nC\u2082H\u2086|etano|14|7 si'
'mples|0|tetra\xe9drica em cada C|109,5\xb0|apolar|H\u2083C-CH\u2083\nC\u2082H\u2084|eteno|12|5 simples e 1 dupla|0|triangular plana em cada C|120\xb0|apolar|H\u2082C=CH\u2082\nC\u2082H\u2082|etino|10|'
'2 simples e 1 tripla|0|linear|180\xb0|apolar|HC\u2261CH')
 def lew():
  ms=[m.split('|')for m in MOL.split('\n')]
  sel=0
  while True:
   r=U.menu('Lewis, geometria e polaridade',[m[0]+' \xb7 '+m[1]for m in ms],sel)
   if r<0:
    return None
   sel=r
   m=ms[r]
   s=['# '+m[0]+' ('+m[1]+')','Estrutura: '+m[8],'Eletr\xf5es de val\xeancia: '+m[2]+' ('+str(int(m[2])//2)+' pares)','Liga\xe7\xf5es: '+m[3],'Pares n\xe3o ligantes: '+m[4],'Geometria: '+m[5]+(' (\xe2ngulo '+m[6]+')'if m[6]else ''),
'> Mol\xe9cula '+m[7]]
   if m[7]=='apolar'and m[0]not in('H\u2082','F\u2082','Cl\u2082','O\u2082','N\u2082'):
    s.append('As liga\xe7\xf5es podem ser polares, mas a geometria sim\xe9trica anula os efeitos.')
   s.append('Fonte: tabela verificada da M1TR4M (s\xf3 mol\xe9culas do programa).')
   U.text(m[0],'\n'.join(s))
 EL=('H-H 436 C-H 413 C-C 348 C=C 614 C#C 839 C-O 358 C=O 799 O-H 463 O=O 498 O-O 146 N-H 391 N-N 163 N=N 418 N#N 945 C-N 293 C#N 891 H-F 567 H-Cl 431 H-Br 366 H-I 299 F-F 159 Cl-Cl 242 Br-Br 193 I-I 151 C-'
'Cl 328 C-F 485 S-H 339')
 def energia(lig):
  t=EL.split(' ')
  a=lig.replace('\u2261','#')
  b='-'.join(a.split('-')[::-1])if '-'in a else a
  for k in range(0,len(t)-1,2):
   x=t[k]
   if x==a or x==b or('='in x and x.split('=')[::-1]==a.split('='))or('#'in x and x.split('#')[::-1]==a.split('#')):
    return int(t[k+1])
  return None
 def termos(txt):
  out=[]
  for p in txt.replace(',',';').replace('\n',';').split(';'):
   if not p.strip():
    continue
   p=p.strip()
   k=0
   while k<len(p)and N.dig(p[k]):
    k+=1
   n=int(p[:k])if k else 1
   rest=p[k:].strip()
   e=None
   if ':'in rest:
    rest,ev=rest.split(':')
    e=N.num(ev)[0]
   rest=rest.strip()
   N.need(rest!='','Falta a liga\xe7\xe3o em "'+p+'"')
   if e is None:
    e=energia(rest)
    N.need(e is not None,'Liga\xe7\xe3o '+rest+' sem energia na tabela: escreve-a assim: '+rest+':valor')
   out.append((n,rest,e))
  return out
 def dh():
  return('Entalpia de rea\xe7\xe3o',[N.fld('Liga\xe7\xf5es quebradas (ex.: 4 C-H; 2 O=O)','','4 C-H; 2 O=O','t'),N.fld('Liga\xe7\xf5es formadas (ex.: 2 C=O; 4 O-H)','','2 C=O; 4 O-H','t')],_dh)
 def _dh(v):
  q=termos(v[0])
  f=termos(v[1])
  N.need(q and f,'Escreve as liga\xe7\xf5es quebradas e as formadas')
  sq=sum([n*e for n,l,e in q])
  sf=sum([n*e for n,l,e in f])
  d=sq-sf
  o=['= \u0394H = \u03a3 E(quebradas) - \u03a3 E(formadas)','Quebradas: '+' + '.join([str(n)+' '+X+' '+N.fmt(e)for n,l,e in q])+' = '+N.fmt(sq)+' kJ','Formadas: '+' + '.join([str(n)+' '+X+' '+N.fmt(e)for n,
l,e in f])+' = '+N.fmt(sf)+' kJ',N.res('\u0394H',d,'kJ mol\u207b\xb9',0,0)]
  if d<0:
   o.append('\u0394H < 0: rea\xe7\xe3o exot\xe9rmica (liberta energia).')
  elif d>0:
   o.append('\u0394H > 0: rea\xe7\xe3o endot\xe9rmica (absorve energia).')
  else:
   o.append('\u0394H = 0 (com estes valores).')
  st='Quebrar liga\xe7\xf5es absorve energia; formar liga\xe7\xf5es liberta energia.\nAs energias da tabela s\xe3o m\xe9dias aproximadas: usa sempre as do enunciado (escreve C=O:805, por exemplo).'
  return('\n'.join(o),st,d,'kJ/mol')
 SUB='\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089'
 def contar(f):
  o=[]
  for c in f:
   k=SUB.find(c)
   o.append(str(k)if k>=0 else c)
  f=''.join(o).replace('\xb7','.')
  tot={}
  for part in f.split('.'):
   i=0
   co=1
   k=0
   while k<len(part)and N.dig(part[k]):
    k+=1
   if k:
    co=int(part[:k])
    i=k
   st=[{}]
   while i<len(part):
    c=part[i]
    if c in '([':
     st.append({})
     i+=1
    elif c in ')]':
     N.need(len(st)>1,'Par\xeantese a mais em '+f)
     g=st.pop()
     j=i+1
     while j<len(part)and N.dig(part[j]):
      j+=1
     m=int(part[i+1:j])if j>i+1 else 1
     for a in g:
      st[-1][a]=st[-1].get(a,0)+g[a]*m
     i=j
    elif 'A'<=c<='Z':
     s=c
     i+=1
     if i<len(part)and 'a'<=part[i]<='z':
      s+=part[i]
      i+=1
     j=i
     while j<len(part)and N.dig(part[j]):
      j+=1
     m=int(part[i:j])if j>i else 1
     st[-1][s]=st[-1].get(s,0)+m
     i=j
    else:
     N.err('S\xedmbolo inesperado "'+c+'" em '+f)
   N.need(len(st)==1,'Falta fechar um par\xeantese em '+f)
   for a in st[0]:
    tot[a]=tot.get(a,0)+st[0][a]*co
  return tot
 def ace():
  return('Acerto de equa\xe7\xf5es',[N.fld('Equa\xe7\xe3o (ex.: H2 + O2 -> H2O)','','CH4 + O2 -> CO2 + H2O','t')],_ace)
 def _ace(v):
  t=v[0].replace('\u2192','->').replace('=','->')
  N.need('->'in t,'Separa os reagentes dos produtos com ->')
  a,b=t.split('->',1)
  rs=[x.strip()for x in a.split('+')if x.strip()]
  ps=[x.strip()for x in b.split('+')if x.strip()]
  N.need(rs and ps,'Faltam reagentes ou produtos')
  sp=rs+ps
  N.need(len(sp)<=8,'No m\xe1ximo 8 esp\xe9cies')
  cs=[contar(x)for x in sp]
  els=[]
  for c in cs:
   for e in c:
    if e not in els:
     els.append(e)
  els.sort()
  for e in els:
   N.need(any([e in c for c in cs[:len(rs)]])and any([e in c for c in cs[len(rs):]]),'O elemento '+e+' s\xf3 aparece de um dos lados')
  M=[[c.get(e,0)if j<len(rs)else-c.get(e,0)for j,c in enumerate(cs)]for e in els]
  k=nulo(M,len(sp))
  N.need(k is not None,'N\xe3o consegui acertar esta equa\xe7\xe3o (verifica as f\xf3rmulas)')
  N.need(max(k)<=1000,'Coeficientes demasiado grandes')
  lado=lambda xs,ks:' + '.join([(str(n)+' 'if n>1 else '')+x for x,n in zip(xs,ks)])
  o=['> '+lado(rs,k[:len(rs)])+' \u2192 '+lado(ps,k[len(rs):])]
  o.append('Confer\xeancia (\xe1tomos de cada elemento):')
  for i,e in enumerate(els):
   r=sum([k[j]*cs[j].get(e,0)for j in range(len(rs))])
   o.append('- '+e+': '+str(r)+' = '+str(r))
  return('\n'.join(o),'Lei de Lavoisier: numa rea\xe7\xe3o qu\xedmica a massa conserva-se, porque o n\xfamero de \xe1tomos de cada elemento \xe9 o mesmo antes e depois.',None,'')
 def nulo(M,n):
  A=[[(x,1)for x in r]for r in M]
  piv=[]
  r=0
  for c in range(n):
   p=-1
   for i in range(r,len(A)):
    if A[i][c][0]!=0:
     p=i
     break
   if p<0:
    continue
   A[r],A[p]=(A[p],A[r])
   pv=A[r][c]
   A[r]=[_div(x,pv)for x in A[r]]
   for i in range(len(A)):
    if i!=r and A[i][c][0]!=0:
     f=A[i][c]
     A[i]=[_sub(A[i][j],_mul(f,A[r][j]))for j in range(n)]
   piv.append(c)
   r+=1
  livres=[c for c in range(n)if c not in piv]
  if len(livres)!=1:
   return None
  lv=livres[0]
  x=[(0,1)]*n
  x[lv]=(1,1)
  for i,c in enumerate(piv):
   x[c]=(-A[i][lv][0],A[i][lv][1])
  den=1
  for a,b in x:
   den=den*b//N.gcd(den,b)
  ks=[a*den//b for a,b in x]
  g=0
  for k in ks:
   g=N.gcd(g,k)
  ks=[k//g for k in ks]
  if ks[0]<0:
   ks=[-k for k in ks]
  if min(ks)<=0:
   return None
  return ks
 def _nr(a,b):
  g=N.gcd(a,b)or 1
  if b<0:
   a,b=(-a,-b)
  return(a//g,b//g)
 def _mul(x,y):
  return _nr(x[0]*y[0],x[1]*y[1])
 def _div(x,y):
  return _nr(x[0]*y[1],x[1]*y[0])
 def _sub(x,y):
  return _nr(x[0]*y[1]-y[0]*x[1],x[1]*y[1])
 return _ns('N U X lew energia dh contar ace nulo',N,U,X,lew,energia,dh,contar,ace,nulo)


_F['c_fqlg'] = _m_c_fqlg


def _m_c_fqso():
 N=_imp('m1_nucleo')
 X=N.X
 VM=22.4
 VS='dm\xb3 L mL cm\xb3'
 MS='g mg kg'
 def con():
  return('Concentra\xe7\xe3o de uma solu\xe7\xe3o',[N.fld('Massa de soluto m (opcional)',MS,'','o'),N.fld('Massa molar M em g/mol (opcional)','','','o'),N.fld('Quantidade de soluto n (opcional)','mol mmol',
'','o'),N.fld('Volume da solu\xe7\xe3o V',VS,'0,250')],_con)
 def _con(v):
  m,M,n,V=v
  N.pos(V[0],'O volume')
  N.need(m is not None or n is not None,'Escreve a massa ou a quantidade de soluto')
  o=[]
  s=V[1]
  q=None
  if n is None and m is not None and(M is not None):
   N.pos(M[0],'A massa molar')
   q=m[0]/M[0]
   sn=N.sfm(m[1],M[1])
   o+=['= n = m / M = '+N.q(m[0],m[1],'g')+' / '+N.q(M[0],M[1],'g mol\u207b\xb9'),N.res('n',q,'mol',sn)]
   s=N.sfm(sn,V[1])
  elif n is not None:
   N.pos(n[0],'A quantidade')
   q=n[0]
   s=N.sfm(n[1],V[1])
  if q is not None:
   c=q/V[0]
   o+=['= c = n / V',N.res('c',c,'mol dm\u207b\xb3',s)]
  if m is not None:
   N.pos(m[0],'A massa')
   cm=m[0]/V[0]
   o+=['= c\u2098 = m / V = '+N.q(m[0],m[1],'g')+' / '+N.q(V[0],V[1],'dm\xb3'),N.res('c\u2098',cm,'g dm\u207b\xb3',N.sfm(m[1],V[1]))]
  elif q is not None and M is not None:
   o+=['= c\u2098 = c '+X+' M',N.res('c\u2098',q/V[0]*M[0],'g dm\u207b\xb3',N.sfm(s,M[1]))]
  st='c em mol dm\u207b\xb3 e c\u2098 em g dm\u207b\xb3, com V em dm\xb3 (1 dm\xb3 = 1 L = 1000 mL).\nc\u2098 = c '+X+' M.'
  return('\n'.join(o),st,q/V[0]if q is not None else None,'mol/dm\xb3')
 def pes():
  return('Massa de soluto a pesar',[N.fld('Concentra\xe7\xe3o pretendida c (mol/dm\xb3)','','0,100'),N.fld('Volume do bal\xe3o V','mL '+VS.replace(' mL',''),'250'),N.fld('Massa molar M (g/mol)','','58,44')],
_pes)
 def _pes(v):
  c,V,M=v
  N.pos(c[0],'A concentra\xe7\xe3o')
  N.pos(V[0],'O volume')
  N.pos(M[0],'A massa molar')
  Vd=V[0]/1000.0
  n=c[0]*Vd
  m=n*M[0]
  s=N.sfm(c[1],V[1],M[1])
  o=['= n = c '+X+' V = '+N.q(c[0],c[1],'mol dm\u207b\xb3')+' '+X+' '+N.q(Vd,V[1],'dm\xb3'),N.res('n',n,'mol',s),'= m = n '+X+' M',N.res('m',m,'g',s),'Pesa '+N.fsf(m,max(1,s or 3))+' g de soluto, dissolve num pouco de \xe1gua e completa o bal\xe3o at\xe9 ao tra\xe7o.']
  return('\n'.join(o),'Primeiro a quantidade de mat\xe9ria, depois a massa.',m,'g')
 def per():
  return('Percentagem e ppm',[N.fld('Calcular','','','c',['% em massa (m/m)','% em volume (V/V)','ppm em massa (mg/kg)']),N.fld('Soluto (massa ou volume)','',''),N.fld('Solu\xe7\xe3o (mesma unidade)','',
'')],_per)
 def _per(v):
  k,a,b=v
  N.pos(a[0],'O soluto')
  N.pos(b[0],'A solu\xe7\xe3o')
  N.need(a[0]<=b[0],'O soluto n\xe3o pode ser mais do que a solu\xe7\xe3o')
  s=N.sfm(a[1],b[1])
  if k==2:
   p=a[0]/b[0]*1000000.0
   o=['= ppm = m(soluto) / m(solu\xe7\xe3o) '+X+' 10\u2076',N.res('ppm',p,'',s),'1 ppm = 1 mg de soluto por kg de solu\xe7\xe3o.']
  else:
   nm='% (m/m)'if k==0 else '% (V/V)'
   p=a[0]/b[0]*100
   o=['= '+nm+' = soluto / solu\xe7\xe3o '+X+' 100',N.res(nm,p,'%',s)]
  return('\n'.join(o),'As duas grandezas t\xeam de estar na mesma unidade.',p,'%'if k<2 else 'ppm')
 def dil():
  return('Dilui\xe7\xe3o',[N.fld('c inicial (mol/dm\xb3), vazio = calcular','','','o'),N.fld('V inicial','mL dm\xb3 L','','o'),N.fld('c final (mol/dm\xb3)','','','o'),N.fld('V final','mL dm\xb3 L','','o')],
_dil)
 def _dil(v):
  ci,vi,cf,vf=v
  falta=[i for i in range(4)if v[i]is None]
  N.need(len(falta)==1,'Deixa vazio s\xf3 o campo que queres calcular')
  for x,nm in((ci,'c inicial'),(vi,'V inicial'),(cf,'c final'),(vf,'V final')):
   if x is not None:
    N.pos(x[0],nm)
  s=N.sfm(*[x[1]for x in v if x is not None])
  k=falta[0]
  o=['= ci '+X+' Vi = cf '+X+' Vf']
  if k==0:
   r=cf[0]*vf[0]/vi[0]
   o.append(N.res('c inicial',r,'mol dm\u207b\xb3',s))
   ci=(r,s)
  elif k==1:
   r=cf[0]*vf[0]/ci[0]
   o.append(N.res('V inicial',r,'mL',s))
   vi=(r,s)
  elif k==2:
   r=ci[0]*vi[0]/vf[0]
   o.append(N.res('c final',r,'mol dm\u207b\xb3',s))
   cf=(r,s)
  else:
   r=ci[0]*vi[0]/cf[0]
   o.append(N.res('V final',r,'mL',s))
   vf=(r,s)
  N.need(cf[0]<=ci[0]*(1+1e-09),'c final maior do que c inicial: isso n\xe3o \xe9 uma dilui\xe7\xe3o')
  f=vf[0]/vi[0]
  o.append('Fator de dilui\xe7\xe3o: f = Vf / Vi = ci / cf '+N.eq(f,s))
  o.append('Volumes em mL (os dois na mesma unidade).')
  return('\n'.join(o),'Na dilui\xe7\xe3o a quantidade de soluto n\xe3o muda: n = ci Vi = cf Vf.',r,'')
 def gas():
  return('Gases em PTN',[N.fld('Massa molar M (g/mol)','',''),N.fld('Massa m (opcional)',MS,'','o'),N.fld('Quantidade n (opcional)','mol mmol','','o'),N.fld('Volume V (opcional)',VS,'','o')],_gas)
 def _gas(v):
  M,m,n,V=v
  N.pos(M[0],'A massa molar')
  rho=M[0]/VM
  s0=N.sfm(M[1],3)
  o=['= \u03c1 = M / V\u2098 = '+N.q(M[0],M[1],'g mol\u207b\xb9')+' / 22,4 dm\xb3 mol\u207b\xb9',N.res('\u03c1',rho,'g dm\u207b\xb3',s0)]
  ds=[x for x in(m,n,V)if x is not None]
  N.need(len(ds)<=1,'Preenche no m\xe1ximo um de m, n ou V')
  if ds:
   if m is not None:
    N.pos(m[0],'A massa')
    q=m[0]/M[0]
    s=N.sfm(m[1],M[1])
   elif n is not None:
    N.pos(n[0],'A quantidade')
    q=n[0]
    s=N.sfm(n[1])
   else:
    N.pos(V[0],'O volume')
    q=V[0]/VM
    s=N.sfm(V[1],3)
   o+=['n = '+N.q(q,s,'mol'),'m = n '+X+' M = '+N.q(q*M[0],N.sfm(s,M[1]),'g'),'V = n '+X+' V\u2098 = '+N.q(q*VM,N.sfm(s,3),'dm\xb3')]
  o.append('Ar seco: \u03c1 \u2248 1,29 g dm\u207b\xb3 em PTN (M \u2248 28,97 g mol\u207b\xb9).')
  o.append('Gases com M maior do que a do ar s\xe3o mais densos.')
  st='Lei de Avogadro: volumes iguais de gases, \xe0 mesma press\xe3o e temperatura, t\xeam a mesma quantidade de mat\xe9ria.\nEm PTN (0 \xb0C e 1 atm), V\u2098 = 22,4 dm\xb3 mol\u207b\xb9.'
  return('\n'.join(o),st,rho,'g/dm\xb3')
 return _ns('N X con pes per dil gas',N,X,con,pes,per,dil,gas)


_F['c_fqso'] = _m_c_fqso


def _m_c_fqte():
 import math
 N=_imp('m1_nucleo')
 X=N.X
 MS='kg g'
 TS='\xb0C K'
 QS='J kJ MJ'
 CU='J kg\u207b\xb9 K\u207b\xb9'
 CMAT='\xe1gua|4.18e3 gelo|2.1e3 alum\xednio|9.0e2 ferro|4.5e2 cobre|3.9e2 chumbo|1.3e2'
 HF=334000.0
 HV=2260000.0
 CA=4180.0
 def um(v,nome):
  f=[i for i in range(len(v))if v[i]is None]
  N.need(len(f)==1,'Deixa vazio s\xf3 o campo que queres calcular ('+nome+')')
  return f[0]
 def dec(x):
  if x[0]==0:
   return x[1]-1
  return x[1]-1-int(math.floor(math.log10(abs(x[0]))+1e-12))
 def sfdif(a,b,d):
  if not(a[1]and b[1]):
   return 0
  if d==0:
   return 1
  e=int(math.floor(math.log10(abs(d))+1e-12))
  return max(1,e+1+min(dec(a),dec(b)))
 def mat(t,k):
  p=t.split(' ')[k-1].split('|')
  return(p[0],float(p[1]))
 def cal():
  return('Capacidade t\xe9rmica m\xe1ssica',[N.fld('Material','','','c',['escrevo c']+[x.split('|')[0]for x in CMAT.split(' ')]),N.fld('Energia Q',QS,'','o'),N.fld('Massa m',MS,'','o'),N.fld('c (J kg\u207b\xb9 K\u207b\xb9)',
'','','o'),N.fld('Temperatura inicial \u03b8i',TS,'','o'),N.fld('Temperatura final \u03b8f',TS,'','o')],_cal)
 def _cal(v):
  k0,Q,m,c,ti,tf=v
  if k0:
   N.need(c is None,'Escolheste um material: deixa c vazio')
   nm,x=mat(CMAT,k0)
   c=(x,2 if x<4000.0 else 3)
  w=[Q,m,c,ti,tf]
  k=um(w,'Q, m, c, \u03b8i ou \u03b8f')
  for x,t in((m,'A massa'),(c,'A capacidade t\xe9rmica m\xe1ssica')):
   if x is not None:
    N.pos(x[0],t)
  if ti is not None and tf is not None:
   dt=tf[0]-ti[0]
   s=N.sfm(N.sfv(Q,m,c),sfdif(ti,tf,dt))
  else:
   s=N.sfv(Q,m,c,ti,tf)
  o=['= Q = m c \u0394T']
  if k0:
   o.append('c('+nm+') = '+N.q(c[0],c[1],CU))
  if k==0:
   N.need(dt!=0,'Temperatura igual no in\xedcio e no fim: Q = 0')
   r=m[0]*c[0]*dt
   o+=['\u0394T = '+N.fmt(dt)+' K (igual a \u0394\u03b8 em \xb0C)',N.res('Q',r,'J',s)]
   o.append('Q > 0: o corpo recebe energia.'if r>0 else 'Q < 0: o corpo cede energia.')
   u='J'
  elif k==1:
   N.need(dt!=0,'Com \u0394T = 0 n\xe3o d\xe1 para calcular a massa')
   r=Q[0]/(c[0]*dt)
   N.need(r>0,'Sinais incoerentes: se o corpo aquece, Q > 0')
   o+=['m = Q / (c \u0394T)',N.res('m',r,'kg',s)]
   u='kg'
  elif k==2:
   N.need(dt!=0,'Com \u0394T = 0 n\xe3o d\xe1 para calcular c')
   r=Q[0]/(m[0]*dt)
   N.need(r>0,'Sinais incoerentes: se o corpo aquece, Q > 0')
   o+=['c = Q / (m \u0394T)',N.res('c',r,CU,s)]
   u='J/(kg K)'
  else:
   d=Q[0]/(m[0]*c[0])
   if k==3:
    r=tf[0]-d
    o+=['\u03b8i = \u03b8f - Q / (m c)',N.res('\u03b8i',r,'\xb0C',s)]
   else:
    r=ti[0]+d
    o+=['\u03b8f = \u03b8i + Q / (m c)',N.res('\u03b8f',r,'\xb0C',s)]
   u='\xb0C'
  st='c: energia para aquecer 1 kg do material 1 K (ou 1 \xb0C).\n\u0394T em K \xe9 igual a \u0394\u03b8 em \xb0C.\n\xc1gua: c = 4,18 '+X+' 10\xb3 J kg\u207b\xb9 K\u207b\xb9 (muito elevada).'
  return('\n'.join(o),st,r,u)
 def est():
  return('Mudan\xe7a de estado',[N.fld('Mudan\xe7a','','','c',['fus\xe3o do gelo','vaporiza\xe7\xe3o da \xe1gua','escrevo \u0394H']),N.fld('\u0394H (J/kg, s\xf3 se escreves)','','','o'),N.fld('Massa m',
MS,'','o'),N.fld('Energia Q',QS,'','o')],_est)
 def _est(v):
  k0,h,m,Q=v
  if k0<2:
   N.need(h is None,'Escolheste a mudan\xe7a: deixa \u0394H vazio')
   h=((HF,HV)[k0],3)
  w=[h,m,Q]
  k=um(w,'\u0394H, m ou Q')
  for x,nm in((h,'\u0394H'),(m,'A massa'),(Q,'A energia')):
   if x is not None:
    N.pos(x[0],nm)
  s=N.sfv(*w)
  o=['= Q = m \u0394H']
  if k0<2:
   o.append('\u0394H = '+N.q(h[0],3,'J kg\u207b\xb9')+(' (a 0 \xb0C)'if k0==0 else ' (a 100 \xb0C)'))
  if k==2:
   r=m[0]*h[0]
   o.append(N.res('Q',r,'J',s))
   u='J'
  elif k==1:
   r=Q[0]/h[0]
   o+=['m = Q / \u0394H',N.res('m',r,'kg',s)]
   u='kg'
  else:
   r=Q[0]/m[0]
   o+=['\u0394H = Q / m',N.res('\u0394H',r,'J kg\u207b\xb9',s)]
   u='J/kg'
  o.append('Durante a mudan\xe7a de estado a temperatura n\xe3o varia.')
  st='\u0394H: energia para mudar o estado de 1 kg, \xe0 temperatura de mudan\xe7a.\nSolidifica\xe7\xe3o e condensa\xe7\xe3o libertam a mesma energia.'
  return('\n'.join(o),st,r,u)
 def eq():
  return('Temperatura de equil\xedbrio',[N.fld('Massa do corpo 1',MS,''),N.fld('c do corpo 1 (J kg\u207b\xb9 K\u207b\xb9)','','4,18e3'),N.fld('Temperatura do corpo 1',TS,''),N.fld('Corpo 2','','','c',['sem mudan\xe7a de estado',
'gelo a 0 \xb0C (funde)']),N.fld('Massa do corpo 2',MS,''),N.fld('c do corpo 2 (J kg\u207b\xb9 K\u207b\xb9)','','4,18e3'),N.fld('Temperatura do corpo 2',TS,'0')],_eq)
 def _eq(v):
  m1,c1,t1,g,m2,c2,t2=v
  for x,nm in((m1,'A massa do corpo 1'),(c1,'c do corpo 1'),(m2,'A massa do corpo 2'),(c2,'c do corpo 2')):
   N.pos(x[0],nm)
  s=N.sfv(m1,c1,t1,m2,c2,t2)
  a=m1[0]*c1[0]
  o=[]
  if g==0:
   b=m2[0]*c2[0]
   r=(a*t1[0]+b*t2[0])/(a+b)
   o+=['= m1 c1 (\u03b8e - \u03b81) + m2 c2 (\u03b8e - \u03b82) = 0','\u03b8e = (m1 c1 \u03b81 + m2 c2 \u03b82) / (m1 c1 + m2 c2)',N.res('\u03b8e',r,'\xb0C',s),'Energia transferida: '+N.q(abs(a*(r-t1[0])),
s,'J')]
  else:
   N.need(t1[0]>0,'A \xe1gua tem de estar acima de 0 \xb0C')
   o.append('= m1 c1 (\u03b81 - \u03b8e) = m2 \u0394Hf + m2 c(\xe1gua) \u03b8e')
   if a*t1[0]<m2[0]*HF:
    f=a*t1[0]/HF
    r=0.0
    o+=['Nem todo o gelo funde: \u03b8e = 0 \xb0C.',N.res('Funde',f,'kg',s),'Sobra '+N.q(m2[0]-f,s,'kg')+' de gelo.']
   else:
    r=(a*t1[0]-m2[0]*HF)/(a+m2[0]*CA)
    o+=['\u03b8e = (m1 c1 \u03b81 - m2 \u0394Hf) / (m1 c1 + m2 c(\xe1gua))',N.res('\u03b8e',r,'\xb0C',s),'Para fundir o gelo: '+N.q(m2[0]*HF,s,'J')]
  st='Sistema isolado: a energia cedida pelo corpo quente \xe9 igual \xe0 recebida pelo corpo frio.\n\u0394Hf(gelo) = 3,34 '+X+' 10\u2075 J kg\u207b\xb9; c(\xe1gua) = 4,18 '+X+' 10\xb3 J kg\u207b\xb9 K\u207b\xb9.'
  return('\n'.join(o),st,r,'\xb0C')
 def cond():
  return('Condu\xe7\xe3o t\xe9rmica',[N.fld('Condutividade k (W m\u207b\xb9 K\u207b\xb9)','','','o'),N.fld('\xc1rea A','m\xb2 cm\xb2','','o'),N.fld('Diferen\xe7a de temperatura \u0394T (K ou \xb0C)','',
'','o'),N.fld('Espessura \u2113','m cm mm','','o'),N.fld('Pot\xeancia P (energia por segundo)','W kW','','o')],_cond)
 def _cond(v):
  k,A,dT,l,P=v
  j=um(v,'k, A, \u0394T, \u2113 ou P')
  for x,nm in((k,'A condutividade'),(A,'A \xe1rea'),(dT,'A diferen\xe7a de temperatura'),(l,'A espessura'),(P,'A pot\xeancia')):
   if x is not None:
    N.pos(x[0],nm)
  s=N.sfv(*v)
  o=['= P = k A \u0394T / \u2113']
  if j==4:
   r=k[0]*A[0]*dT[0]/l[0]
   o+=['P = '+N.q(k[0],k[1])+' '+X+' '+N.q(A[0],A[1],'m\xb2')+' '+X+' '+N.q(dT[0],dT[1],'K')+' / '+N.q(l[0],l[1],'m'),N.res('P',r,'W',s)]
   u='W'
  elif j==0:
   r=P[0]*l[0]/(A[0]*dT[0])
   o+=['k = P \u2113 / (A \u0394T)',N.res('k',r,'W m\u207b\xb9 K\u207b\xb9',s)]
   u='W/(m K)'
  elif j==1:
   r=P[0]*l[0]/(k[0]*dT[0])
   o+=['A = P \u2113 / (k \u0394T)',N.res('A',r,'m\xb2',s)]
   u='m\xb2'
  elif j==2:
   r=P[0]*l[0]/(k[0]*A[0])
   o+=['\u0394T = P \u2113 / (k A)',N.res('\u0394T',r,'K',s)]
   u='K'
  else:
   r=k[0]*A[0]*dT[0]/P[0]
   o+=['\u2113 = k A \u0394T / P',N.res('\u2113',r,'m',s)]
   u='m'
  st='Bons condutores t\xeam k grande (metais); isoladores t\xeam k pequeno (ar, l\xe3, esferovite).\nA energia passa do lado mais quente para o mais frio.'
  return('\n'.join(o),st,r,u)
 def pl():
  return('Primeira Lei da Termodin\xe2mica',[N.fld('Trabalho W (recebido > 0)',QS,'','o'),N.fld('Calor Q (recebido > 0)',QS,'','o'),N.fld('Radia\xe7\xe3o R (recebida > 0)',QS,'0','o'),N.fld('Varia\xe7\xe3o da energia interna \u0394U',
QS,'','o')],_pl)
 def _pl(v):
  W,Q,R,dU=v
  k=um(v,'W, Q, R ou \u0394U')
  s=N.sfv(*v)
  o=['= \u0394U = W + Q + R']
  nm=('W','Q','R','\u0394U')[k]
  if k==3:
   r=W[0]+Q[0]+R[0]
  else:
   r=dU[0]-sum([v[i][0]for i in range(3)if i!=k])
   o.append(nm+' = \u0394U - (as outras parcelas)')
  o.append(N.res(nm,r,'J',s))
  if k==3:
   o.append('\u0394U > 0: a energia interna aumenta.'if r>0 else '\u0394U < 0: a energia interna diminui.'if r<0 else '\u0394U = 0: a energia interna n\xe3o varia.')
  elif r<0:
   o.append(nm+' < 0: o sistema cede energia desta forma.')
  else:
   o.append(nm+' > 0: o sistema recebe energia desta forma.')
  st='Conven\xe7\xe3o: energia recebida pelo sistema \xe9 positiva; cedida \xe9 negativa.\nSistema isolado: W = Q = R = 0 e \u0394U = 0.'
  return('\n'.join(o),st,r,'J')
 def pv():
  return('Painel fotovoltaico',[N.fld('Irradi\xe2ncia Er (W/m\xb2)','','1,0e3'),N.fld('\xc1rea do painel A','m\xb2 cm\xb2',''),N.fld('Pot\xeancia el\xe9trica P (ou U e I)','W kW mW','','o'),N.fld('Tens\xe3o U (opcional)',
'V mV','','o'),N.fld('Corrente I (opcional)','A mA','','o')],_pv)
 def _pv(v):
  er,A,P,U,I=v
  N.pos(er[0],'A irradi\xe2ncia')
  N.pos(A[0],'A \xe1rea')
  o=['= P(radia\xe7\xe3o) = Er A',N.res('P(rad)',er[0]*A[0],'W',N.sfv(er,A))]
  if P is None:
   N.need(U is not None and I is not None,'Escreve a pot\xeancia el\xe9trica ou a tens\xe3o e a corrente')
   N.pos(U[0],'A tens\xe3o')
   N.pos(I[0],'A corrente')
   p=U[0]*I[0]
   s=N.sfv(U,I)
   o+=['= P(el\xe9trica) = U I',N.res('P(el)',p,'W',s)]
  else:
   N.need(U is None and I is None,'Escreve a pot\xeancia el\xe9trica ou U e I, n\xe3o os tr\xeas')
   N.pos(P[0],'A pot\xeancia')
   p=P[0]
   s=P[1]
  r=p/(er[0]*A[0])*100
  N.need(r<=100,'\u03b7 > 100 %: imposs\xedvel (verifica a \xe1rea e as unidades)')
  o+=['= \u03b7 = P(el) / P(rad) '+X+' 100 %',N.res('\u03b7',r,'%',N.sfm(s,er[1],A[1]))]
  st='Irradi\xe2ncia: pot\xeancia da radia\xe7\xe3o por unidade de \xe1rea (W m\u207b\xb2).\nCom sol direto, \xe0 superf\xedcie, Er \u2248 1,0 '+X+' 10\xb3 W m\u207b\xb2.\nOs pain\xe9is comuns t\xeam \u03b7 entre cerca de 15 % e 22 %.'
  return('\n'.join(o),st,r,'%')
 return _ns('N X HF um dec mat cal est eq cond pl pv',N,X,HF,um,dec,mat,cal,est,eq,cond,pl,pv)


_F['c_fqte'] = _m_c_fqte


def _m_m1():
 MODO='edi\xe7\xe3o de reserva FQ'
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
 CALC=('c_comd.cte|Constantes e dados|C|\nc_comu.sci|Calculadora cient\xedfica|C|\nc_comu.sf|Algarismos significativos|C|\nc_comu.uni|Conversor de unidades|C|\nc_comu.pre|Prefixos do SI|C|\nc_fqat.mm|Massa mo'
'lar|F|q1\nc_fqat.qm|Quantidade de mat\xe9ria|F|q1\nc_fqat.ar|Massa at\xf3mica relativa m\xe9dia|F|q1\nc_fqat.fr|Fra\xe7\xe3o molar e fra\xe7\xe3o m\xe1ssica|F|q1\nc_fqci.ohm|Resist\xeancia el\xe9trica'
' (U = R I)|F|f2\nc_fqci.rho|Resistividade (R = \u03c1 \u2113 / A)|F|f2\nc_fqci.assoc|Resist\xeancias em s\xe9rie e em paralelo|F|f2\nc_fqci.ger|Gerador: for\xe7a eletromotriz e resist\xeancia interna|'
'F|f2\nc_fqci.pot|Pot\xeancia, energia e custo el\xe9tricos|F|f2\nc_fqel.fot|Espetros e fot\xf5es|F|q2\nc_fqel.hid|\xc1tomo de hidrog\xe9nio|F|q2\nc_fqel.conf|Configura\xe7\xe3o eletr\xf3nica|F|q2\nc_f'
'qen.em|Energia cin\xe9tica, potencial e mec\xe2nica|F|f1\nc_fqen.cons|Conserva\xe7\xe3o da energia mec\xe2nica|F|f1\nc_fqen.tr|Trabalho de uma for\xe7a constante|F|f1\nc_fqen.wp|Trabalho do peso|F|f1'
'\nc_fqen.tec|Teorema da energia cin\xe9tica|F|f1\nc_fqen.pot|Pot\xeancia|F|f1\nc_fqen.ren|Rendimento|F|f1\nc_fqlg.lew|Lewis, geometria e polaridade|F|q4\nc_fqlg.dh|Entalpia de rea\xe7\xe3o (energias d'
'e liga\xe7\xe3o)|F|q6\nc_fqlg.ace|Acerto de equa\xe7\xf5es qu\xedmicas|F|q6\nc_fqso.con|Concentra\xe7\xe3o de uma solu\xe7\xe3o|F|q5\nc_fqso.pes|Massa de soluto a pesar|F|q5\nc_fqso.per|Percentagem e '
'partes por milh\xe3o|F|q5\nc_fqso.dil|Dilui\xe7\xe3o de solu\xe7\xf5es|F|q5\nc_fqso.gas|Gases (PTN)|F|q5\nc_fqte.cal|Capacidade t\xe9rmica m\xe1ssica (Q = m c \u0394T)|F|f3\nc_fqte.est|Mudan\xe7a de e'
'stado (Q = m \u0394H)|F|f3\nc_fqte.eq|Temperatura de equil\xedbrio de uma mistura|F|f3\nc_fqte.cond|Condu\xe7\xe3o t\xe9rmica (P = k A \u0394T / \u2113)|F|f3\nc_fqte.pl|Primeira Lei da Termodin\xe2mic'
'a|F|f3\nc_fqte.pv|Painel fotovoltaico e irradi\xe2ncia|F|f3')
 return _ns('CALC',CALC)


_F['m1_calc'] = _m_m1_calc


def _m_m1_cat():
 NLIC=43
 NEX=88
 NCART=124
 TEMAS=('q1|F|q|Massa e tamanho dos \xe1tomos|p_q1|x_q1|5|0|10|0|18|0|c_fqat.qm c_fqat.mm c_fqat.ar c_fqat.fr c_comu.sci c_comu.sf c_comu.uni|q1a q1b q1c q1d q1e','q2|F|q|Energia dos eletr\xf5es nos \xe1tomos|p_q2|x_q2|5|5|10|10|14|18|c_fqel.fot c_fqel.hid c_fqel.conf c_comu.sci c_comu.uni|q2a q2b q2c q2d q2e',
'q3|F|q|Tabela Peri\xf3dica|p_q3|x_q3|3|10|9|20|8|32|c_fqel.conf c_fqel.fot c_fqat.mm|q3a q3b q3c','q4|F|q|Liga\xe7\xe3o qu\xedmica|p_q4|x_q4|6|13|10|29|13|40|c_fqlg.lew c_fqlg.dh c_fqel.conf c_fqat.mm|q4a q4b q4c q4d q4e q4f',
'q5|F|q|Gases e dispers\xf5es|p_q5|x_q5|5|19|10|39|14|53|c_fqso.gas c_fqso.con c_fqso.pes c_fqso.per c_fqso.dil c_fqat.mm c_fqat.fr|q5a q5b q5c q5d q5e','q6|F|q|Transforma\xe7\xf5es qu\xedmicas|p_q6|x_q6|3|24|9|49|9|67|c_fqlg.dh c_fqel.fot c_fqlg.ace|q6a q6b q6c',
'f1|F|f|Energia e movimentos|p_f1|x_f1|5|27|10|58|15|76|c_fqen.em c_fqen.cons c_fqen.tr c_fqen.wp c_fqen.tec c_fqen.pot c_fqen.ren|f1a f1b f1c f1d f1e','f2|F|f|Energia e fen\xf3menos el\xe9tricos|p_f2|x_f2|5|32|10|68|16|91|c_fqci.ohm c_fqci.rho c_fqci.assoc c_fqci.ger c_fqci.pot c_fqen.ren|f2a f2b f2c f2d f2e',
'f3|F|f|Energia, fen\xf3menos t\xe9rmicos e radia\xe7\xe3o|p_f3|x_f3|6|37|10|78|17|107|c_fqte.cal c_fqte.est c_fqte.eq c_fqte.cond c_fqte.pl c_fqte.pv c_fqen.ren c_comu.uni|f3a f3b f3c f3d f3e f3f')
 BUILD='2026-10-23'
 LIMITES='ver RELATORIO.md'
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
' os valores.')),('Unidades e f\xf3rmulas qu\xedmicas',('Nas calculadoras, escolhe a unidade de cada campo com \u25c2\u25b8 (quando h\xe1 mais do que uma).\nF\xf3rmulas qu\xedmicas: mai\xfasculas e min\xfasculas como na tabela: H2SO4, Ca(OH)2, CuSO4.5H2O (o'
' ponto separa a \xe1gua de hidrata\xe7\xe3o). Co \xe9 cobalto; CO \xe9 mon\xf3xido de carbono.')),('Gravar o progresso','A app guarda as defini\xe7\xf5es e o progresso em vari\xe1veis do documento (m1def, m1prog...).\nPara ficarem guardados de vez, grava o documento: ctrl+S (ou menu Ficheiro > Guardar) antes de o fechar.'),
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
   v=head(D,'V')
   if v!=str(PVER):
    P.unload(name)
    raise Falta('M\xf3dulo '+name+' desatualizado (vers\xe3o '+v+'; esta app l\xea a '+str(PVER)+')')
   nl=head(D,'N')
   if nl!=''and(not nl.isdigit()):
    raise Falta('M\xf3dulo '+name+' estragado')
  SL[slot]=[m,name]
  return m
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
 return _ns('P SL WARN Falta drop get recs body parts ftext lesson',P,SL,WARN,Falta,drop,get,recs,body,parts,ftext,lesson)


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
 def dps(m):
  m=m.replace('.',',')
  k=m.find(',')
  return 0 if k<0 else len(m)-k-1
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
 def val(s,x=0.0):
  return ev(comp(s),x)
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
 def ulist(cat):
  o=[]
  for it in UT.split(' '):
   p=it.split(':')
   if len(p)>=3 and p[1]==cat:
    o.append(p[0])
  return o
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
 def sfm(*vs):
  if not CF.get('sfa',1):
   return 0
  m=0
  for v in vs:
   if v and(m==0 or v<m):
    m=v
  return m
 def sfv(*xs):
  return sfm(*[x[1]for x in xs if x is not None and x[0]!=0])
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
 def res(sym,x,u='',sf=0,dec=-1):
  s=eq(x,sf,dec)
  return '> '+sym+' '+s+(' '+u if u else '')
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
 def nneg(v,nome):
  need(v>=0,nome+' n\xe3o pode ser negativo')
  return v
 def low(s):
  return P.vis(s,0).lower()
 return _ns('P LN10 CF X err ok sup _sc _p10 dig _fl _dn _e10 _rnd _ds sci fmt eq fix fsf _clean num dps comp ev val gcd rad rhs ulist conv check fld sfm sfv pm res q lst rdf need pos nneg low',P,LN10,
CF,X,err,ok,sup,_sc,_p10,dig,_fl,_dn,_e10,_rnd,_ds,sci,fmt,eq,fix,fsf,_clean,num,dps,comp,ev,val,gcd,rad,rhs,ulist,conv,check,fld,sfm,sfv,pm,res,q,lst,rdf,need,pos,nneg,low)


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


def _m_m1_tp():
 P=_imp('m1_plat')
 N=_imp('m1_nucleo')
 U=_imp('m1_ui')
 A=_imp('m1_app')
 TD=('1|H|Hidrog\xe9nio|1.008|1|1|s|n\xe3o metal|g\xe1s|53|1312\n2|He|H\xe9lio|4.0026|18|1|s|g\xe1s nobre|g\xe1s|31|2372\n3|Li|L\xedtio|6.94|1|2|s|metal alcalino|s\xf3lido|167|520\n4|Be|Ber\xedlio|9.0122|2|'
'2|s|metal alcalinoterroso|s\xf3lido|112|900\n5|B|Boro|10.81|13|2|p|semimetal|s\xf3lido|87|801\n6|C|Carbono|12.011|14|2|p|n\xe3o metal|s\xf3lido|67|1086\n7|N|Azoto|14.007|15|2|p|n\xe3o metal|g\xe1s|56|'
'1402\n8|O|Oxig\xe9nio|15.999|16|2|p|n\xe3o metal|g\xe1s|48|1314\n9|F|Fl\xfaor|18.998|17|2|p|halog\xe9neo|g\xe1s|42|1681\n10|Ne|N\xe9on|20.180|18|2|p|g\xe1s nobre|g\xe1s|38|2081\n11|Na|S\xf3dio|22.990|'
'1|3|s|metal alcalino|s\xf3lido|190|496\n12|Mg|Magn\xe9sio|24.305|2|3|s|metal alcalinoterroso|s\xf3lido|145|738\n13|Al|Alum\xednio|26.982|13|3|p|metal|s\xf3lido|118|578\n14|Si|Sil\xedcio|28.085|14|3|p|'
'semimetal|s\xf3lido|111|787\n15|P|F\xf3sforo|30.974|15|3|p|n\xe3o metal|s\xf3lido|98|1012\n16|S|Enxofre|32.06|16|3|p|n\xe3o metal|s\xf3lido|88|1000\n17|Cl|Cloro|35.45|17|3|p|halog\xe9neo|g\xe1s|79|125'
'1\n18|Ar|\xc1rgon|39.95|18|3|p|g\xe1s nobre|g\xe1s|71|1521\n19|K|Pot\xe1ssio|39.098|1|4|s|metal alcalino|s\xf3lido|243|419\n20|Ca|C\xe1lcio|40.078|2|4|s|metal alcalinoterroso|s\xf3lido|194|590\n21|Sc|'
'Esc\xe2ndio|44.956|3|4|d|metal de transi\xe7\xe3o|s\xf3lido|184|633\n22|Ti|Tit\xe2nio|47.867|4|4|d|metal de transi\xe7\xe3o|s\xf3lido|176|659\n23|V|Van\xe1dio|50.942|5|4|d|metal de transi\xe7\xe3o|s'
'\xf3lido|171|651\n24|Cr|Cr\xf3mio|51.996|6|4|d|metal de transi\xe7\xe3o|s\xf3lido|166|653\n25|Mn|Mangan\xeas|54.938|7|4|d|metal de transi\xe7\xe3o|s\xf3lido|161|717\n26|Fe|Ferro|55.845|8|4|d|metal de '
'transi\xe7\xe3o|s\xf3lido|156|762\n27|Co|Cobalto|58.933|9|4|d|metal de transi\xe7\xe3o|s\xf3lido|152|760\n28|Ni|N\xedquel|58.693|10|4|d|metal de transi\xe7\xe3o|s\xf3lido|149|737\n29|Cu|Cobre|63.546|1'
'1|4|d|metal de transi\xe7\xe3o|s\xf3lido|145|745\n30|Zn|Zinco|65.38|12|4|d|metal de transi\xe7\xe3o|s\xf3lido|142|906\n31|Ga|G\xe1lio|69.723|13|4|p|metal|s\xf3lido|136|579\n32|Ge|Germ\xe2nio|72.630|14'
'|4|p|semimetal|s\xf3lido|125|762\n33|As|Ars\xe9nio|74.922|15|4|p|semimetal|s\xf3lido|114|947\n34|Se|Sel\xe9nio|78.971|16|4|p|n\xe3o metal|s\xf3lido|103|941\n35|Br|Bromo|79.904|17|4|p|halog\xe9neo|l'
'\xedquido|94|1140\n36|Kr|Cr\xedpton|83.798|18|4|p|g\xe1s nobre|g\xe1s|88|1351\n37|Rb|Rub\xeddio|85.468|1|5|s|metal alcalino|s\xf3lido|265|403\n38|Sr|Estr\xf4ncio|87.62|2|5|s|metal alcalinoterroso|s'
'\xf3lido|219|550\n39|Y|\xcdtrio|88.906|3|5|d|metal de transi\xe7\xe3o|s\xf3lido|212|600\n40|Zr|Zirc\xf3nio|91.224|4|5|d|metal de transi\xe7\xe3o|s\xf3lido|206|640\n41|Nb|Ni\xf3bio|92.906|5|5|d|metal d'
'e transi\xe7\xe3o|s\xf3lido|198|652\n42|Mo|Molibd\xe9nio|95.95|6|5|d|metal de transi\xe7\xe3o|s\xf3lido|190|684\n43|Tc|Tecn\xe9cio|[98]|7|5|d|metal de transi\xe7\xe3o|s\xf3lido|183|702\n44|Ru|Rut\xe9n'
'io|101.07|8|5|d|metal de transi\xe7\xe3o|s\xf3lido|178|710\n45|Rh|R\xf3dio|102.91|9|5|d|metal de transi\xe7\xe3o|s\xf3lido|173|720\n46|Pd|Pal\xe1dio|106.42|10|5|d|metal de transi\xe7\xe3o|s\xf3lido|16'
'9|804\n47|Ag|Prata|107.87|11|5|d|metal de transi\xe7\xe3o|s\xf3lido|165|731\n48|Cd|C\xe1dmio|112.41|12|5|d|metal de transi\xe7\xe3o|s\xf3lido|161|868\n49|In|\xcdndio|114.82|13|5|p|metal|s\xf3lido|156|'
'558\n50|Sn|Estanho|118.71|14|5|p|metal|s\xf3lido|145|709\n51|Sb|Antim\xf3nio|121.76|15|5|p|semimetal|s\xf3lido|133|834\n52|Te|Tel\xfario|127.60|16|5|p|semimetal|s\xf3lido|123|869\n53|I|Iodo|126.90|17|'
'5|p|halog\xe9neo|s\xf3lido|115|1008\n54|Xe|X\xe9non|131.29|18|5|p|g\xe1s nobre|g\xe1s|108|1170\n55|Cs|C\xe9sio|132.91|1|6|s|metal alcalino|s\xf3lido||\n56|Ba|B\xe1rio|137.33|2|6|s|metal alcalinoterros'
'o|s\xf3lido||\n57|La|Lant\xe2nio|138.91|3|6|d|lantan\xeddeo|s\xf3lido||\n58|Ce|C\xe9rio|140.12||6|f|lantan\xeddeo|s\xf3lido||\n59|Pr|Praseod\xedmio|140.91||6|f|lantan\xeddeo|s\xf3lido||\n60|Nd|Neod'
'\xedmio|144.24||6|f|lantan\xeddeo|s\xf3lido||\n61|Pm|Prom\xe9cio|[145]||6|f|lantan\xeddeo|s\xf3lido||\n62|Sm|Sam\xe1rio|150.36||6|f|lantan\xeddeo|s\xf3lido||\n63|Eu|Eur\xf3pio|151.96||6|f|lantan\xedde'
'o|s\xf3lido||\n64|Gd|Gadol\xednio|157.25||6|f|lantan\xeddeo|s\xf3lido||\n65|Tb|T\xe9rbio|158.93||6|f|lantan\xeddeo|s\xf3lido||\n66|Dy|Dispr\xf3sio|162.50||6|f|lantan\xeddeo|s\xf3lido||\n67|Ho|H\xf3lmi'
'o|164.93||6|f|lantan\xeddeo|s\xf3lido||\n68|Er|\xc9rbio|167.26||6|f|lantan\xeddeo|s\xf3lido||\n69|Tm|T\xfalio|168.93||6|f|lantan\xeddeo|s\xf3lido||\n70|Yb|It\xe9rbio|173.05||6|f|lantan\xeddeo|s\xf3lid'
'o||\n71|Lu|Lut\xe9cio|174.97||6|f|lantan\xeddeo|s\xf3lido||\n72|Hf|H\xe1fnio|178.49|4|6|d|metal de transi\xe7\xe3o|s\xf3lido||\n73|Ta|T\xe2ntalo|180.95|5|6|d|metal de transi\xe7\xe3o|s\xf3lido||\n74|W'
'|Tungst\xe9nio|183.84|6|6|d|metal de transi\xe7\xe3o|s\xf3lido||\n75|Re|R\xe9nio|186.21|7|6|d|metal de transi\xe7\xe3o|s\xf3lido||\n76|Os|\xd3smio|190.23|8|6|d|metal de transi\xe7\xe3o|s\xf3lido||\n77'
'|Ir|Ir\xeddio|192.22|9|6|d|metal de transi\xe7\xe3o|s\xf3lido||\n78|Pt|Platina|195.08|10|6|d|metal de transi\xe7\xe3o|s\xf3lido||\n79|Au|Ouro|196.97|11|6|d|metal de transi\xe7\xe3o|s\xf3lido||\n80|Hg|'
'Merc\xfario|200.59|12|6|d|metal de transi\xe7\xe3o|l\xedquido||\n81|Tl|T\xe1lio|204.38|13|6|p|metal|s\xf3lido||\n82|Pb|Chumbo|207.2|14|6|p|metal|s\xf3lido||\n83|Bi|Bismuto|208.98|15|6|p|metal|s\xf3lid'
'o||\n84|Po|Pol\xf3nio|[209]|16|6|p|metal|s\xf3lido||\n85|At|\xc1stato|[210]|17|6|p|halog\xe9neo|s\xf3lido||\n86|Rn|R\xe1don|[222]|18|6|p|g\xe1s nobre|g\xe1s||\n87|Fr|Fr\xe2ncio|[223]|1|7|s|metal alcal'
'ino|s\xf3lido||\n88|Ra|R\xe1dio|[226]|2|7|s|metal alcalinoterroso|s\xf3lido||\n89|Ac|Act\xednio|[227]|3|7|d|act\xednideo|s\xf3lido||\n90|Th|T\xf3rio|232.04||7|f|act\xednideo|s\xf3lido||\n91|Pa|Protact'
'\xednio|231.04||7|f|act\xednideo|s\xf3lido||\n92|U|Ur\xe2nio|238.03||7|f|act\xednideo|s\xf3lido||\n93|Np|Nept\xfanio|[237]||7|f|act\xednideo|s\xf3lido||\n94|Pu|Plut\xf3nio|[244]||7|f|act\xednideo|s'
'\xf3lido||\n95|Am|Amer\xedcio|[243]||7|f|act\xednideo|s\xf3lido||\n96|Cm|C\xfario|[247]||7|f|act\xednideo|s\xf3lido||\n97|Bk|Berqu\xe9lio|[247]||7|f|act\xednideo|s\xf3lido||\n98|Cf|Calif\xf3rnio|[251]'
'||7|f|act\xednideo|s\xf3lido||\n99|Es|Einst\xe9nio|[252]||7|f|act\xednideo|s\xf3lido||\n100|Fm|F\xe9rmio|[257]||7|f|act\xednideo|desconhecido||\n101|Md|Mendel\xe9vio|[258]||7|f|act\xednideo|desconheci'
'do||\n102|No|Nob\xe9lio|[259]||7|f|act\xednideo|desconhecido||\n103|Lr|Laur\xeancio|[262]||7|f|act\xednideo|desconhecido||\n104|Rf|Rutherf\xf3rdio|[267]|4|7|d|metal de transi\xe7\xe3o (previsto)|desco'
'nhecido||\n105|Db|D\xfabnio|[268]|5|7|d|metal de transi\xe7\xe3o (previsto)|desconhecido||\n106|Sg|Seab\xf3rgio|[269]|6|7|d|metal de transi\xe7\xe3o (previsto)|desconhecido||\n107|Bh|B\xf3hrio|[270]|7'
'|7|d|metal de transi\xe7\xe3o (previsto)|desconhecido||\n108|Hs|H\xe1ssio|[269]|8|7|d|metal de transi\xe7\xe3o (previsto)|desconhecido||\n109|Mt|Meitn\xe9rio|[278]|9|7|d|metal de transi\xe7\xe3o (prev'
'isto)|desconhecido||\n110|Ds|Darmst\xe1cio|[281]|10|7|d|metal de transi\xe7\xe3o (previsto)|desconhecido||\n111|Rg|Roentg\xe9nio|[282]|11|7|d|metal de transi\xe7\xe3o (previsto)|desconhecido||\n112|Cn'
'|Copern\xedcio|[285]|12|7|d|metal de transi\xe7\xe3o (previsto)|desconhecido||\n113|Nh|Nip\xf3nio|[286]|13|7|p|metal (previsto)|desconhecido||\n114|Fl|Fler\xf3vio|[289]|14|7|p|metal (previsto)|desconh'
'ecido||\n115|Mc|Mosc\xf3vio|[290]|15|7|p|metal (previsto)|desconhecido||\n116|Lv|Liverm\xf3rio|[293]|16|7|p|metal (previsto)|desconhecido||\n117|Ts|Tenesso|[294]|17|7|p|halog\xe9neo (previsto)|desconh'
'ecido||\n118|Og|Ogan\xe9sson|[294]|18|7|p|g\xe1s nobre (previsto)|desconhecido||')
 FONTES='Ar: IUPAC (valores abreviados); [n] = n.\xba de massa do is\xf3topo mais est\xe1vel. Raio: calculado (Clementi e outros, 1967). Energia de ioniza\xe7\xe3o: NIST, convertida para kJ/mol.'
 ORB=('1s','2s','2p','3s','3p','4s','3d','4p')
 CAP=(2,2,6,2,6,2,10,6)
 BC={'s':8,'p':9,'d':1,'f':9}
 def rows():
  return[ln.split('|')for ln in TD.split('\n')if ln]
 def el(z):
  i=TD.find('\n'+str(z)+'|')if z>1 else-1
  j=TD.find('\n',i+1)
  return TD[i+1:j if j>0 else len(TD)].split('|')
 def cell(e):
  z=int(e[0])
  if e[4]=='':
   return(7 if z<89 else 8,z-(55 if z<89 else 87))
  return(int(e[5])-1,int(e[4])-1)
 def conf(z):
  if z>36:
   return ''
  o=[]
  r=z
  for i in range(len(ORB)):
   if r<=0:
    break
   n=min(r,CAP[i])
   o.append([ORB[i],n])
   r-=n
  if z in(24,29):
   for x in o:
    if x[0]=='4s':
     x[1]=1
    if x[0]=='3d':
     x[1]+=1
  return ' '.join([x[0]+N.sup(x[1])for x in o])
 def valence(e):
  b=e[6]
  if b=='s'or b=='p':
   g=int(e[4])
   return str(g if g<=2 else g-10)if int(e[0])>2 else e[0]
  return ''
 def ar2(e):
  a=e[3]
  if a.startswith('['):
   return a
  return N.fmt(N._fl(a),0,2)
 def sheet(z):
  e=el(z)
  s=['# '+e[2]+' ('+e[1]+')','N\xfamero at\xf3mico: Z = '+e[0],'Massa at\xf3mica relativa: Ar = '+e[3].replace('.',',')+(''if e[3].startswith('[')else ' (tabela do exame: '+ar2(e)+')')]
  if e[4]:
   s.append('Grupo '+e[4]+', per\xedodo '+e[5]+', bloco '+e[6])
  else:
   s.append('Per\xedodo '+e[5]+', bloco '+e[6]+' (s\xe9rie dos '+('lantan\xeddeos)'if z<89 else 'act\xednideos)'))
  s.append('Tipo: '+e[7])
  s.append('Estado f\xedsico a 25 \xb0C: '+e[8])
  c=conf(z)
  if c:
   s.append('Configura\xe7\xe3o eletr\xf3nica: '+c+(' (al\xe9m do programa: o 10.\xba ano vai at\xe9 4s)'if z>20 else ''))
   v=valence(e)
   if v and z<=20:
    s.append('Eletr\xf5es de val\xeancia: '+v)
  if e[9]:
   s.append('Raio at\xf3mico: '+e[9]+' pm')
   s.append('Energia de 1.\xaa ioniza\xe7\xe3o: '+e[10]+' kJ/mol')
  else:
   s.append('Raio e energia de ioniza\xe7\xe3o: sem dados nesta app.')
  s.append('')
  s.append('Fontes: '+FONTES)
  U.text(e[2],'\n'.join(s))
 def find(q):
  q=q.strip()
  if not q:
   return 0
  if q.isdigit():
   z=int(q)
   return z if 1<=z<=118 else 0
  lq=N.low(q)
  best=0
  for e in rows():
   if e[1].lower()==lq:
    return int(e[0])
   if not best and N.low(e[2]).startswith(lq):
    best=int(e[0])
  return best
 def run():
  es=rows()
  grid={}
  for e in es:
   grid[cell(e)]=e
  r,c=(0,0)
  flt=0
  q=''
  cw=17
  ch=15
  x0=(P.E['W']-18*cw)//2
  y0=P.E['lh']+2
  while True:
   A.S['where']='tabela peri\xf3dica'
   cur=grid[r,c]
   P.begin()
   U.title('Tabela peri\xf3dica',('','grupo '+cur[4],'per\xedodo '+cur[5],'bloco '+cur[6])[flt])
   tl=[[' ']*36 for i in range(9)]
   for(rr,cc),e in grid.items():
    on=flt==0 or(flt==1 and e[4]==cur[4]and e[4])or(flt==2 and e[5]==cur[5]and(rr<7))or(flt==3 and e[6]==cur[6])
    if not P.E['g']:
     s='##'if(rr,cc)==(r,c)else e[1]if on else '..'
     tl[rr][2*cc]=s[0]
     if len(s)>1:
      tl[rr][2*cc+1]=s[1]
     continue
    x=x0+cc*cw
    y=y0+rr*ch+(4 if rr>=7 else 0)
    if(rr,cc)==(r,c):
     P.rect(x,y,cw-1,ch-1,2)
     P.txt(x+1,y-2,e[1],10)
    else:
     P.rect(x,y,cw-1,ch-1,BC[e[6]]if on else 1)
     P.txt(x+1,y-2,e[1],0 if on else 9)
   if not P.E['g']:
    for k in range(9):
     P.put(0,1+k,''.join(tl[k]),0)
   info=cur[0]+' '+cur[1]+' '+cur[2]+'  Ar '+ar2(cur)
   P.put(0,10,U.clip(info,U.cols()),2)
   U.foot(('procura: '+q+'_'if q else 'setas \xb7 enter: ficha')+' \xb7 tab: filtro \xb7 esc')
   P.show()
   k=P.key()
   if k=='esc':
    if q:
     q=''
     continue
    return
   if k=='enter':
    if q:
     z=find(q)
     q=''
     if z:
      r,c=cell(el(z))
     else:
      U.hint('Elemento n\xe3o encontrado')
     continue
    sheet(int(cur[0]))
   elif k=='tab':
    flt=(flt+1)%4
   elif k=='del':
    q=q[:-1]
   elif k in('left','right'):
    d=-1 if k=='left'else 1
    cc=c+d
    while 0<=cc<18 and(r,cc)not in grid:
     cc+=d
    if 0<=cc<18:
     c=cc
   elif k in('up','down'):
    d=-1 if k=='up'else 1
    rr=r+d
    while 0<=rr<9:
     if(rr,c)in grid:
      r=rr
      break
     if rr>=7 or r>=7:
      cs=[cc for a,cc in grid if a==rr]
      if cs:
       c=min(cs,key=lambda x:(abs(x-c),x))
       r=rr
       break
     rr+=d
   elif len(k)==1 and(k.isalpha()or '0'<=k<='9')and(len(q)<12):
    q=q+k
 return _ns('P N U A rows el conf sheet find run',P,N,U,A,rows,el,conf,sheet,find,run)


_F['m1_tp'] = _m_m1_tp


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
 return _ns('P N E OKS ERS cols body clip title foot bar hint menu text msg ask lesson edit form graph',P,N,E,OKS,ERS,cols,body,clip,title,foot,bar,hint,menu,text,msg,ask,lesson,edit,form,graph)


_F['m1_ui'] = _m_m1_ui


def _m_p_f1():
 D = "#3#5 5#4 `G $:~f f1a|`G #N`,$J, $De`M*p`0$J e *t`k$8|`+ #Ne$J `+ $De`M*pi$J `+ *ta$8 &[`ga *tanico &N~P `ni$P\
 &F centr`5 `? ni~A &ne`M|c_fqen.em*_`Acleo|r9a:Movimentos: rapidez*-celera`%`!${ gr`-fiYg;r9b:For`%as: Lei$(\
 Newton, ~Z e impuls`!o|m5a:A fun`%`!$Madr`-$J e $ku gr`-fico|AE FQ `I `G $:~m`u `+ #N`,tic~, `+\
 $De`M*p`0$J.`D Ec, #G e Em.~+ o &N~P `n`0$P &F.`icolher um n`0~A &n`L`M `H a #G.~l~1 carr${m andamento, um\
 livr&E~! prateleira e ~! bola a cair t`Lm `+.~6 `+ associada a&zovimento `, a #N`,$J; a associada ~] &,`%`!o\
 `, a $De`Ml.\n\
Soma~K, d`!#/ `+ *t`k$8.~k$% `G #N`,$J: Ec $Q m v`6 (m em kg, v em $!`(`4, Ec em J).$% `G $De`M*p`0$J do\
 &[`ga ~w + Terra: #G = m g h.$% h: $1 acima d&E`0~A &n`L`M, *I #G = 0.$% `G *t`k$8: EY) Ec + #G.$% Part`0$P\
 &F: o ~w reduz-s#'o centr`5 `?, `; toda a `?.$% O &N$krve &_ s`3 i*Vressa a *^la`%`!~9 ~w.`R`V m ~} kg, v =\
 $g $!`(`4, h = &O m e g ~N $!`(`6.\n\
Ec $Q `9 $v `9 $g`6 &t J.\n\
#G ~} `) `9 &O = &) `)`6 J.#o &t + $A = 1,1 `)`6 J.\n\
Ec nunca `, negativa; #G `, negativa abaix~9 n`0~A &n`L`M.YW a `q quadruplica a `+ #N`,$J.YW a `? duplica Ec\
 e #G.`x n`0~A &n`L`M escolhe-se; a ~q`%`!`5 #G n`!`5pend#ble.~6 `+ `| (agita`%`!${ `<`%`' ~K `n`0`Z) n`!o\
 faz `ne da `+ *t`k$8.`W `G #N`,$J|Ec $Q m v`6|m: `? (kg);v: m`3dul~P `q ($!`(`4)|Ec #O 0|m ~} kg e v = $g\
 $!`(`4: Ec &t Y2`W `G $De`M*p`0$J|#G = m g h|g: acelera`%`!o grav`0$J ($!`(`6);h: $1 acima d&E`0~A &n`L`M\
 (m)|~pt~P su~pf`0cie da Terra|m ~} kg e h = &O m: #G = &) `)`6 Y2`W `G *t`k$8|EY) Ec + #G|Ec e #G em J|&[`ga\
 ~w + Terra|Em &t + $A = 1,1 `)`6 Y2`W`E bol~, 0,45 *} 12 $!`(`4*- $v m do ch`!o; g ~N $!`(`6.`: Ec, #G\
 (refer`L`M no ch`!o) e Em.~) Ec $Q `9 0,45 `9 12`6 = 32 J~/ #G = 0,45 `) `9 $v &t J~C EY) 32,4 + 9,#I 41 J&A\
 Em ~> 41 J.`F`%`!o: Ec > #G, `y`> a `q `, #[ #' $1 `, pe`>na.~j~6 `+ *t`k$8 ~O montanhas-russas, `>~K e\
 saltos.Yduitos proble#p resolveY' &X conhe~y as ~:`%as: basta `;`Hr `+s.~i`i`>~y $Madrad~P `q em Ec.~+ a `?\
 Ye#p ou a `q em km/h.$% Medir as $1s a `n#g n`0$K `e*m`b `> a #G `g de ser &,tiva.~h$% Ec $Q m v`6 ($c de\
 v`6).$% #G = m g h ($c d&E`0~A &n`L`M).$% EY) Ec + #G.$% Part`0$P &F: o ~w reduz-s#'o centr`5 `?.~g~1 carr`5\
 1,2 `)`B kg pass~, 10 $!`(`4 `H 20 $!`(`4. Por quant$k *L #c `+ #N`,$J?~e&5 4: a `q duplica e Ec `, pro`y$_\
 a v`6 (pass~, *O `)`P J `H 2,4 `)~% J).~f f1b|Trabalh`5 ~! ~:`%a ~L|`@ ~:ca ~L #2#/#z `;~[ e~vz `@ $De*V\
 re&[te*V nulo joule|c_fqen.tr*_`Acleo|f1a:`G #N`,$J, $De`M*p`0$J e *t`k$8|m8a:Vetores: dire`%`!o, sentid${\
 norma;m8g:Produt${scalar (ex$?`!o, 11.#w);g9b:Raz`' trigonom`,&ys `c `kngul#/gudo|AE FQ `I `G $:~m`v `@ `;o\
 $S`L`M de `+ `y a`%`!`5 ~! ~:`%a.`D o trabalh`5 ~! ~:`%a ~L.$% Classi~vr o `@ `;o $De*V, re&[te*V ou nulo.$%\
 *+~vr a `;~[ e~vz da ~:`%a.~l#opurrar um carrinho $Se-lhe `+; segurar ~! mala `Hd&E`!o.#o F`0sica, s`3 h`-\
 `@ &_ a ~:`%a `g `;~[ na dire`%`!o d`5&Z~k$% Trabalho, W: `+ ~^ `y ~! ~:`%a cujo *9`5 aplica`%`!$k\
 desloca.$% W = F d Yg $G (F em N, d em m, W em J).$% $G: `k#z ~B a ~:`%a e `5&Z$% #M~[ e~vz: F Yg $G, na\
 dire`%`!o d`5&Z$% $G < 90`h: $De*V (W > 0); $G = 90`h: nulo; $G > 90`h: re&[te*V (W < 0).$% 1 J = 1 N `9 1\
 m.`R`V puxa-se um caixote &O m `; ~! ~:`%~, 10 N a 60`h do ch`!o.\n\
W ~N `9 &O `9 Yg 60`h = 25 J ($De*V).\n\
S`3 a `;~[ e~vz, 10 `9 Yg 60`h = &O N, $-&^ `@.~6 `;~[ ~p*|$Pr, F sen $G, n`!o $-&^ `@.#7 plano horizontal, o\
 pes${ a $-`%`!&Eormal s`!o ~p*|$Pres a`5slocamento: W = 0.`x ~Z op\xf5e-s#'&zovimento: $G = 180`h.`V atrit`5\
 &1 N a*x`5 $g m: W = &1 `9 $g `9 Yg 180`h = -12 J.\n\
#M v`-*ks ~:`%as, o `@ &< `, a $r ~' `@$( ~I ~:`%a.`x `@ &< `, i~al ao `@ $d.`W Trabalh`5 ~! ~:`%a ~L|W = F d\
 Yg $G|F: in$?$E da ~:`%a (N);d: #2*@m);$G: `k#z ~B a ~:`%a e `5slocamento|~:`%a ~L e *n`3*k retil`0nea|F ~N\
 N, d = &O m e $G = 60`h: W = 25 J|c_fqen.tr`W`E empurra-se um carrinho 8,0 m `; 50 N a 30`h d`5slocamento; o\
 ~Z *5 15 N.`: trabalh`5 ~I ~:`%a e `@ &<.~) W(F&p 50 `9 8,0 `9 Yg 30`h = 3,5 `)`6 J~/ W(Fa&p 15 `9 8,0 `9 Yg\
 180`h = -1,2 `)`6 J~C W(P&p W(N&p 0 (~:`%as ~p*|$Pres a`5slocamento)$q W(&<&p 346 - 12#I 2,3 `)`6 J&A W(&<)\
 ~> 2,3 `)`6 J ($De*V).`F`%`!#! ~:`%a apli~I $Se `K `+ do `> o ~Z retira.~j`x `@ med#' `+ `> ~! ~:`%a $Se.\n\
$h as ~:`%as, do 9.#w ano, ~] `+, do 10.#w ano.~i~+ o `k#z `; a ver$Jl &s do `k#z `; `5&Z`i`>~y `> o ~Z `g $G\
 = 180`h.`b `> segurar um *> `Hdo $-&^ `@.`D o Ygseno `; a cal$Pdora em ~-&!.~h$% W = F d Yg $G.$% $G < 90`h:\
 $De*V; 90`h: nulo; $G > 90`h: re&[te*V.$% S`3 a `;~[ e~vz $-&^ `@.$% Trabalho &< = $r ~' `@s.~g~1a ~:`%~, 20\
 N, ~p*|$Pr a um #2`5 &1 m, $-&^ `> `@?~e\n\
Nenhum: W = 20 `9 &1 `9 Yg 90`h = 0 J.~f f1c|#f `+ #N`,$J|teorema da `+ #Ne$J `@ $d $r ~' `@s ~qca~P `+ #Ne$J\
 travagem|c_fqen.tec*_`Acleo|f1b:Trabalh`5 ~! ~:`%a ~L|m8b:O~pa`%`' `; vetores|AE FQ `I `G $:~m$% Enu`Mr o\
 teorema da `+ #N`,$J.`D o `@ $d a `nir da ~q`%`!`5 Ec.`D `qs a `nir do `@ ~K ~:`%as.`J o &l do `@ &< `; a\
 ~q`%`!`5 Ec.~l\n\
Quando v`-*ks ~:`%as atuam *X ~w, ${feit&Ea `q $c do trabalh`5 to~K.\n\
Se o `@ &< `, &,tivo, o ~w acelera; se `, negativo, trava.~k$% #f `+ #N`,$J: &j `8E#d Ec,f - Ec,i.$% W(R): `@\
 $d, i~al ~] $r ~' `@$( to~K as ~:`%as.$% W(R) > 0: Ec `w; W(R) < 0: Ec ~E.$% &j 0: Ec n`!o ~q.$% Vale `H\
 to~K as ~:`%as, `{ ou n`!o.`R`V um carr`5 $A0 kg pass~, 10 $!`(`4 `H 20 $!`(`4.\n\
W(R) $Q `)00 `9 (20`6 - 10`6&p #? `)~% J.`V um bloc`5 $v *} &1 $!`(`4 `H ao fi*A &1 m, travado #B ~Z.\n\
`8E#d 0 - \xbd `9 $v `9 &1`6 = -16 J&W W(Fa&p -16 J.\n\
#Mo W(Fa&p -Fa d, o ~Z *5 16 / &1 = &1 N.&D obter a `q ~t: v*D \u221a(vi`6 *S W(R) / m).`x teorema dispensa o\
 c`-lcul~P acelera`%`!o.`W #f `+ #N`,$J|&j `8Ec $Q m vf`6 - \xbd m vi`6|W(R): `@ $d (J);vi e vf: `qs &3 e\
 ~t|~:`%a$( &M`>r tipo|$A0 $s 10 `H 20 $!`(`4: &j #? `)~% J|c_fqen.tec`W`E um tren`3 de 50 kg `n#ho. Puxa-se\
 `; 120 N, na dire`%`!~9 movimento*-*x`5 10 m. O ~Z *5 40 N.`: `q ~t.~) W(F&p 120 `) = 1,2 `)`B J~/ W(Fa&p\
 -40 `) = -&1 `)`6 J~C &j 1200 - 40#I 8,0 `)`6 J$q v*D $z `9 8*P 50&p 5,7 $!`(`4&A vf ~> 5,7 $!`(`4.`F`%`!o:\
 Ec ~t $Q `9 50 `9 5,66`6 ~> 8,0 `)`6 J = W(R).~j`x teorema `< o `@ ~K ~:`%as ~] ~q`%`!~P `q.#> ~n `Atil\
 quand$k conhecem as ~:`%a&x as dist`k`Ms, #p n`!o o `gpo.~i~+ o trabalh`5 ~! s`3 ~:`%a &s do `@ &<.`i`>~y o\
 &l negativ~9 `@ do ~Z.`D vf`6 e es`>~y a raiz quadrada.$% So#Z `qs &s de `+s.~h$% &j `8Ec.$% &j $r ~' `@$(\
 to~K as ~:`%as.$% W(R) > 0: acelera; W(R) < 0: trava.~g~1 corp`5 &1 kg `g E#d 50 J. Que `@ &< `, $u `H o `Hr?~e\n\
&j 0 - 5#I -50 J (`@ re&[te*V).~f f1d|For`%as `{ e ~T`%`!~P `+ *t`k$8|~:ca ~Ttiva nao ~Ttiva `@ do *> *no*k\
 ~Tca~P `+ *ta$8 `>da Y- escorrega $1 maxima|c_fqen.cons*_`Acleo|f1c:#f `+ #N`,$J|g9c:Resolver tri`k#zs\
 ret`k#zs|AE FQ `I `G $:~m`u ~:`%as `{ de n`!o `{.`J o `@ do *> `; a ~q`%`!`5 #G.$% #, ~T`%`!~P `+ *t`k$8.`D\
 `q&x $1s *q ~T`%`!o.~l~1a bola atirada a#/r ~pde `q a subir e recu~pa-a ~,s~y.\n\
Sem `1 d#/r, #0 ~] m`!o `; ~5 `q: a `+ *t`k$8 ~T-se.~k$% For`%a ~Ttiva: o `@ ~B &G *9*:`!`5#F *n`3*k (ex.:\
 *>).$% Trabalh~9 *>: W(P&p -`8#G = m g (hi - hf).$% N`!o `{: ~Z, `1 d#/r, ~:`%a$( motores.$% Se s`3 as\
 ~:`%as `{ $-&^m `@: Em,i = Em,f.$% Nesse caso, `8E#d -`8#G.`R`V um ~w cai 20 m a `nir do repouso, &X `1 d#/r\
 (g ~N $!`(`6).\n\
m g h $Q m v`6 #' `? corta-se: v = $z `) `9 20&p 20 $!`(`4.~6 `q ~t n`!`5#F `?.#7 escorrega &X ~Z*- `q no\
 fund*v`3 $c d`5sn`0~A.~6 $-`%`!&Eormal `, ~p*|$Pr a`5slocamento: W(N&p 0 e n`!#/ltera a Em.\n\
Lan`%amento ver$Jl `; 12 $!`(`4: h m`-x = 12`6 / (2 `)&p 7,2 m.~1 corp`5 $v $ssce &O m: W(P) ~} `) `9 &O = &)\
 `)`6 J.~6 subir, o `@ do *> `, negativ${ a #G `w.`W Trabalh~9 *>|W(P&p -`8#G = m g (hi - hf)|hi e hf: $1s &3\
 e ~t (m)|*> ~L (~pt~P Terra)|$v $ssce &O m: W(P&p &) `)`6 J|c_fqen.wp`W Conserva`%`!~P `+ *t`k$8|\xbd m vi`6\
 + m g hi $Q m vf`6 + m g hf|i e f: $.a~' &3 e ~t|s`3 ~:`%as `{ $-&^m `@|`>d~, 20 m a `nir do repouso: v = 20\
 $!`(`4|c_fqen.cons`W`E u$!kater `n#h&Eo top`5 ~! rampa `; 3,2 *A $1. Sem ~Z; g ~N $!`(`6.`: `q no fund${ a\
 1,4 *A $1.~) No fun$} v = $z `) `9 3,2&p 8,0 $!`(`4~/ A 1,4 m: v = $z `) `9 (3,2 - 1,4)) $F $!`(`4&A v = 8,0\
 $!`(`4 no fund${ *O $!`(`4 a 1,4 m.`F`%`!#! 1,4 m ainda h`- #G, `y ~u a `q `, ~o.~j~6 ~T`%`!~P `+ *t`k$8\
 resolv$: `;plica~' `;`Hnd*v`3 &G $.a~'.\n\
Na $-l$E h`- &Xpr#'lgum ~Z: a ~T`%`!o `, um &No.~i`b `> a `q de `>d~,#F `?.~+ a ~T`%`!$Mando h`- ~Z ou `1\
 d#/r.$% Medir $1s a `n#g n`0$K `e*m$% &e o &l em W(P&p -`8#G.~h$% O *> `, ~! ~:`%a ~Ttiva.$% W(P&p -`8#G.$%\
 S`3 ~:`%as `{: Em ~L.$% Queda a `nir do repouso: v = $z g h).~g\n\
Duas bolas, de 1 kg #b 5 kg, caem d~5 $1 &X `1 d#/r. ~z chega ao ch`!o `K de*Rssa?~e\n\
Chegam `; ~5 `q: v = $z g h) n`!`5#F `?.~f f1e|For`%as n`!o `{, $D`L`M e ~<|~:cas nao `{ ~Z re&[te`M d#/r `+\
 &i ~qca~P `+ *ta$8 $De`M watt ~< quilowatt-hora|c_fqen.ren*_`Acleo|f1d:For`%as `{ e ~T`%`!~P `+ *t`k$8$7 `I\
 `G $:~m`J o `@ ~K ~:`%as n`!o `{ `; `8Em.`D a `+ &i.`D a $D`L`M.`D o #)`5 um processo.~l~1 carro trava e `H:\
 a `+ #N`,$J passa `H `+ `| ~' trav`' e d#/r.\n\
Nenh~! m`-YD aproveita toda a `+ `> $I.~k$% W(Fnc&p `8Em: `@ ~K ~:`%as n`!o `{.$% #M ~Z ou `1 d#/r, W(Fnc) <\
 0 #' Em ~E.$% `G &i: Ed = -`8Em (`w a `+ `|).$% Pot`L`M: #@ E / `8t #m W; 1 W = 1 J s`(`4).$% *Ko: ~0\
 E(`A*[~:&J `)Y_$% 1 kWh = 3,6 `)`U J.`R`V ~! bol~, 57 g cai de 1,20 m e ressalta at`, 0,90 m (g ~N\
 $!`(`6).#o,i = 0,057 `) `9 1,2#I 0,68 J; Em,*D 0,057 `) `9 0,9#I 0,51 J.\n\
Dissipada: 0,684 - 0,513 = 0,17 J, isto `,, 25 % da &3.`V um motor eleva 50 *} *O m em 10 &x $I &1 kJ.\n\
E(`Atil&p 50 `) `9 6,#I $g `)`B J; P(`Atil&p 30*P 1#I $g `)`6 W.\n\
~0 30*P 4000 `)#I 75 %.~6 `+ &< ~T-se &X*R: a &i n`!`5*e\n\
Dissipar `, tornar a `+ ~H `Atil, `K \"espalhada\".`W For`%as n`!o `{|W(Fnc&p `8Em|W(Fnc): `@ ~K ~:`%as n`!o\
 `{ (J)|~Z, `1 d#/r, motores|bol~, 57 &P 1,20 m a 0,90 m: `8EY) -0,17 J|c_fqen.cons`W Pot`L`M|#@ E / `8t|E:\
 `+ ~^ (J);`8t: i*Vrval`5 `gp*@s)|$D`L`M m`,*W|$g kJ em 10 s: #@ $g `)`6 W|c_fqen.$D`W *Ko|~0 E(`A*[~:&J `)0\
 %|*2`,m `; $D`L`Ms `Atei&x ~:neci~K|#< < $A %|$g kJ `Atei$( &1 kJ: ~0 75 %|c_fqen.ren`W`E ~! gru~, $v kW\
 eleva 400 *} 15 m em 40 s; g ~N $!`(`6.`: `+ `Atil, `+ ~:necida e ~<.~) E(`Atil&p 400 `) `9 15 $F `)`P J~/\
 E(~:&J ~} `)`B `9 4#I 8,0 `)`P J~C ~0 *O `)`P / (8,0 `)`P) `)#I 75 %&A ~0 75 %; #_ $v `)`P J.`F`%`!o: #< <\
 $A %, `;o `g de ser.~j~6 `+ `> ~! m`-YD $I vai toda `H algum la$} `ne `, `Atil, o r$.o `, &i.~6umentar o ~<\
 poupa `+ e dinheiro.~i`i`>~y `> W(Fnc) `, negativ$Mando h`- dissipa`%`!o.$% Juntar $D`L`M em kW `; `gp${$!\
 &X converter.$% &e a `+ `Atil `; a ~:necida (d`- #< > $A %).$% #a `> a `+ dissipad~,*e~h$% W(Fnc&p `8Em.$%\
 Ed = -`8Em.$% #@ E / `8t.$% ~0 E(`A*[~:&J `)Y_~g~1a l`kmpad~, 60 W *^~:ma *O J `y segund${m YK. ~z `, $ku ~<?~e\n\
~0 *O / 60 `)0 ~N %; o r$.o `, dissipado `;o &k.$p 1|f1e1|`G #N`,$J `c ciclista|c_fqen.em|f1a~{`M$} um\
 ciclista #' bicicleta t`Lm 70 kg e seguem a 36 km/h. ~z `, a `+ #N`,$J?`E Y) 70 kg; v = 36 km/h.$L`^`%`!o:~)\
 v = 36 / 3,6 ~N $!`(`4~/ Ec $Q `9 70 `)`6 = 3,5 `)`B J`Q E#d 3,5 `)`B J.`S`%`!#! 72 km/h a `+ #N`,$J se*k 4\
 &g ~R.`= #x 36 km/h diretame*V na f`3&/ (d`- um ~b 13 &g ~R).$p 2|f1e2|Bloc&Eum plano inclinado `;\
 ~Z|c_fqen.cons|f1e~{`M$} um bloc`5 $v kg `n#h${ desce &O m *X plano inclinad#/ 30`h. Chega ao fund#/ *O\
 $!`(`4 (g ~N $!`(`6).$/ a `+ &i #' ~:`%~, ~Z.$L`^`%`!o:~) Altura: h = &O `9 sen 30`h = 2,5 m~/ Em,i ~} `) `9\
 2,5 = 50 J~C Em,f $Q `9 $v `9 *O`6 = 36 J$q Ed = 50 - 36 = 14 J\n\
5. W(Fa&p -Fa d&W Fa = 14 / &O = 2,8 N`Q #_ 14 J; o ~Z *5 2,8 N.`S`%`!o: &X ~Z chega*k ao fund#/ $z `) `9\
 2,5) ~> 7,1 $!`(`4.`= #x d = &O m `;o $1.$p 3|f1e3|Montanha-russa $-l|c_fqen.cons|f1e~{`M$} um carr`5 #t kg\
 `n#h#/ 30 *A $1. Passa a 10 *A $1 `; 18 $!`(`4 (g ~N $!`(`6).&( ~S da `+ *t`k$8 foi &i?$L`^`%`!o:~) Em,i =\
 #t `) `9 3#I #? `)~% J~/ Em,f $Q `9 #t `9 18`6 + #t `) `) = 1,31 `)~% J~C Ed = 150 000 - 131 00#I 1,9 `)`P\
 J$q Percentagem: 19 0*P 150 000 `)#I 13 %`Q #_ `] 13 % da `+ *t`k$8.`S`%`!o: &X ~Z, chega*k aos 10 m a $z `)\
 `9 20&p 20 $!`(`4.`= es`>~y a #G no *9#/ 10 m.\n\
"
 return _ns('D', _dz(D))


_F['p_f1'] = _m_p_f1


def _m_p_f2():
 D = "#3#5 5#4 `G Y+`3~H el`,&v~f f2a|&V el`,&y, `e`%~, $De`Ml e `1|`X `.ica ~M `.ica `ec~, $De`Ml $?ao re&[te`M\
 `.ica lei de ohm &K ohmic#/m~pe volt ohm am~pi$, volti$,|c_fqci.ohm*_`Acleo|r9c:&6ic$E: circuitos,\
 #[za&xl`,&y&x $D`L`M|a7d:Pro`y$_$E direta;m4c:Fun`%`!#/fim|AE FQ `I `G Y+`3~H el`,&v~m`v `X el`,&y e\
 calcul`--la a `nir da ~M.`v `e`%~, $De`Ml el`,trico.`v `1 el`,&y e #x YB U / I.$% *+~vr &Kes `3hmiYg.~l#7\
 fio `<d#/ ~! &+*-s ~Ms movem-s#b ~:ma *7da: h`- `X el`,&y.~6 &+ d`- `+ ~]s ~Ms; os `;~[s do circuito $Im\
 essa `+.~6 `1 med#' o&,`%`!`5 um `;~[ ~] passagem da `X.~k$% &V el`,&y: #D Q / `8t #m A; 1 A = 1 C s`(`4).$%\
 Sentido conven$_: do polo + `H o polo -, no circuit${xterior.$% Diferen`%~, $De`Ml ($?`!o): #8 E / Q, `+ `y\
 un$E de ~M (1 V = 1 J C`(`4).$% Re&[t`L`M el`,&y: YB U / I #m `a; 1 `a = 1 V A`(`4).$% Condutor `3YH ~L a `2\
 ~L; U(I) `, ~! reta *q origem.`R`V 30 C YIvessam ~! sec`%`!`5 um fi${m &) min.\n\
#D 30 / 6#I ~c A.#7 $|, `>$!e move s`!o os `.`', e$!entido Y>`-ri#/o conven$_.~1a pilh~, #? V $Se #? J `H ~I\
 coulomb `> a YIvessa.`V ~! l`k#{ a *O V `, ~pcorrida `y *r A.\n\
R $F / *r = 24 `a.`x am~p`0$, `<-se e$!`,rie; o volt`0$, `<-se em `H*B.~1 filament`5 l`k#{ n`!o `, `3YH `w &_ a`>ce.\n\
&V Y?`0nua: sentido ~L (&+s); alternada: $kntid&zuda (rede, 50 Hz).`W &V el`,&y|#D Q / `8t|Q: ~M (C);`8t:\
 i*Vrval`5 `gp*@s)|`X ~L|30 C em 60 s: #D ~c A|c_fqci.ohm`W Diferen`%~, $De`Ml|#8 E / Q|E: `+ ~^ (J);Q: ~M\
 (C)|~B &G *9*< circuito|#? J `y coulomb: #8 #? V|`W Re&[t`L`M el`,&y|YB U / I|U: `e`%~, $De`Ml (V);I: `X\
 (A)|&K `3YH ~L|*O V e *r A: YB 24 `a|c_fqci.ohm`W`E um carregador ~:nece $v A a ~! bate*k &C 30 min.`: ~M ~^\
 e n`A$<`5 `.`' (e = 1,60 `)`(`4`l C).~) `8t = 30 `9 6#I 1800 s~/ Q = I `8t ~} `9 180#I 3,6 `)`B C~C *U Q / e\
 = 36*P 1,60 `)`(`4`l = 2,3 `)`6`6 `.`'&A Q = 3,6 `)`B C, `] 2,3 `)`6`6 `.`'.`F`%`!o: ~I `.`!o `g ~! ~M\
 min`As$P, `y ~u s`!o $us muit`0ssimos.~j\n\
&V, $?`!${ `1 s`!#/s tr`Ls #[zas b`-sica$( &M`>r #T\n\
Saber relacion`--las ~pYa escolher &+s, fio&x `;~[s.~i`[ `X (A) `; $?`!*@V).$% $hr #/m~p`0$, em `H*B ou o\
 volt`0$, e$!`,rie.~+ o `gp${m minuto&xm #D Q / `8t.`b `> to~' os `;~[s s`!o `3hmiYg.~h$% #D Q / `8t.$% #8 E\
 / Q.$% YB U / I.$% \xd3YH ~L; U(I) reta *q origem.~g\n\
S#' `X *X &K `3hmico Y:, o `> aco*Vce ~] `e`%~, $De`Ml &! seus $;?~e\n\
Duplica: #8 R I e R mant`,Y'.~f f2b|Re&[tiv$E e `2|$0 `;`}#/re~, sec&S &F `2 fio &K ~J &Xi&Kes\
 termistor|c_fqci.rho*_`Acleo|f2a:&V el`,&y, `e`%~, $De`Ml e `1$7 `I `G Y+`3~H el`,&v~m`J a `1 `; o `;`}${ a\
 `-$- `c fio.~+ a $0 `;o propriedade do &F.`D a `1 `c fio.`J a $0 `; a `2.~l~1 fio `;prid${ fino re&[te `K ~]\
 `X do `> um curt${ grosso.`x &F *2`,m Y?a: o #L Y@z ~n melhor do `> o ferro.~k$% YB ~G $Z / A.$% $Z:\
 `;`}*@m); A: `-$- da sec`%`!*@m`6).$% ~G: $0, caracter`0s$J do &F (`a m).$% Bons &Kes t`Lm ~G pe`>na (#L:\
 1,7 `)`(`m `a m*- 20 `hC).$% Nos ~J, ~G `w `; a `2.$% Nos &Xi&Kes, ~G ~E `; a `2.`R`V fi`5 #L `; $A m e\
 sec`%`!`5 #? mm`6.~6 = #? mm`6 = #? `)`(`U m`6.\n\
YB 1,7 `)`(`m `)0 / (#? `)`(`U&p 1,1 `a.YW o `;`}o duplica R; Y: a `-$- reduz R a metade.`xs fio$( #L ~K\
 casas s`!o grossos `H R ser pe`>na #'`>~yem *6.`x filamento `>*V `ca l`k#{ `g `K `1 do `> frio.\n\
Term`0stores: `;~[s cuja `1 ~q ~n `; a `2 (term`3$,s `.`3niYg).\n\
1 mm`6 ~N`(`U m`6.`W Re&[tiv$E|YB ~G $Z / A|~G: $0 (`a m);$Z: `;`}*@m);A: `-$- da sec`%`!*@m`6)|fio\
 homog`,neo*- `2 ~L|#L, $A m e #? mm`6: YB 1,1 `a|c_fqci.rho`W`E fi`5 n`0`>l-cr`3mi*@~G = 1,1 `)`(`U `a m) `;\
 &q mm`6 de sec`%`!o.`: `;`}&Eecess`-rio `H ter YB 22 `a.~) A = &q `)`(`U ~} `)`(~? m`6~/ $Z = R A / ~G = 22\
 `9 $v `)`(~? / (1,1 `)`(`U&p &1 m&A $Z = &1 m.`F`%`!o: &E`0`>l-cr`3mio `g ~G #[, `y ~u basta *6 fio.~j~6 $0\
 ~O a escolha ~' *f: #L `H fios, n`0`>l-cr`3mio `H a`>cedores.~i`i`>~y de &; mm`6 `H m`6.`b `> a `1 s`3 $c do\
 &F.$% &e $Z e A na f`3&/.`b `> to~' os *f `wm R `; a `2.~h$% YB ~G $Z / A.$% ~G $c do &F e da `2.$% Metais:\
 ~G `w `; a `2.~gYZ fi*< ~; #L t`Lm o ~; `;`}o; um `g ~9br~P `-$- do outro. ~z `g ~o `1?~e`x de ~R `-$-: R `,\
 inversame*V pro`y$_ a A, `y ~u `g metade da `1.~f f2c|Circuito&x$!`,rie e em `H*B|associaca${$!erie em `H*B\
 re&[te`M #= `X $?ao &! malhas instalaca~9m$.ica am~pi$, volti$,*c*_`Acleo|f2a:&V el`,&y, `e`%~, $De`Ml e\
 `1$7 `I `G Y+`3~H el`,&v~m`u associa`%`' e$!`,rie e em `H*B.`D a `1 #=.`D `X&x $?`' em ~I `;~[.~4 `y`> `, `>\
 as casas usam `<`%`' em `H*B.~l\n\
N~! s`,rie*- `X s`3 `g um caminho; em `H*B, *g `y v`-rios.#o casa, des`<r ~! l`k#{ n`!#/paga as outras:\
 $.`!${m `H*B.~k$% S`,rie: ~5 `X em to~'; #8 U1 + U2 + ...$% S`,rie: Req = R1 + R2 + ...$% Para*B: ~5 $?`!${m\
 to~'; #D I1 + I2 + ...$% Para*B: *, = 1 / R1 Yb / R2 + ...$% Em `H*B, Req `, ~o do `> a ~o ~K `1s.`R$+\
 e$!`,rie: 10 `a, 20 `a e 30 `a `<~K a 12 V.$Lq ~N *S0 + 3#I 60 `a e #D 12 / 6#I &q A.\n\
U1 ~N `9 &q ~} V; U2 = &1 V; U3 $F V; a $r d`- 12 V.$+ em `H*B: *O `a e $g `a.\n\
*, = 1 / *O Yb / $g = ~c `a`(`4&W Req ~} `a.#o `H*B*- `X ~R passa na `1 ~o.\n\
N*:`3s*- $r ~K `Xs `> entram `, i~al ~] $r ~K `> saem (~T`%`!~P ~M).#o casa, to~' os YJs ~vm a 230 V e Y%*A\
 ~:ma in$c*V.`W Associa`%`!${$!`,rie|Req = R1 + R2 + ...|R1, R2: `1s (`a)|#9 `X em to~K|10 *S0 + 3#I 60\
 `a*c`W Associa`%`!${m `H*B|*, = 1 / R1 Yb / R2 + ...|R1, R2: `1s (`a)|#9 $?`!${m to~K|*O `a e $g `a: Req ~}\
 `a*c`W`E #P l`kmpa~K de 12 `a em `H*B, `<~K a *O V.`: `X em ~I l`k#{, `X &< e Req.~) Em ~I l`k#{: I $F / 12\
 = ~c A~/ &V &<: #D ~c + ~c = &) A~C Req $F / &) $F `a&A ~c A em ~I l`k#{; &) A no &<; Req $F `a.`F`%`!o: #P\
 `1s i~ai&xm `H*B d`!&zetade `ca: 12 / 2 $F `a.~j~6s associa`%`' ~Om as instala`%`' el`,&y&x os circuitos ~' YJs.\n\
Juntar `K YJ&xm `H*B `w a `X &<: `, `y ~u `> h`- disjuntores.~i$% So#Z `1&xm `H*B `;$k fos&X e$!`,rie.`i`>~y\
 de inverter *, no fim.`b `> e$!`,rie ~I `;~[ `g a $?`!o toda.`b `> a `X se \"Y4\" a*x~9 #T~h$% S`,rie: #9 I;\
 Req = $r.$% Para*B: #9 U; 1/Req = $r ~' inversos.$% N`3s: `Xs `> entraY) `Xs `> saem.~g\n\
Tr`Ls `1$( 30 `a $.`!${m `H*B. ~z `, a `1 #=?~e\n\
*, = 3 / 30&W Req ~N `a.~f f2d|Geradores: ~:`%a `.#- e `1 `||&} &+ ~:ca `.#- re&[te`M `| $?ao &! $;\
 curto-circuito circuit#/berto caracteris$J reta|c_fqci.ger*_`Acleo|f2a:&V el`,&y, `e`%~, $De`Ml e\
 `1|m4c:Fun`%`!#/fim|AE FQ `I `G Y+`3~H el`,&v~m`v ~:`%a `.#- `c &}.`J a $?`!o &! $; `; a `X: #8 ~( - r I.$%\
 &f o gr`-fico U(I) `c &}.`D a `X de curto-#T~l~1a &+ nova ~p`c pouc`5 $?`!$Mando ~:nece #| `X.\n\
Parte da `+ ~v na pr`3p*k &+, `> `g ~! `1 `|.~k$% For`%a `.#-, ~(: `+ `> o &} ~:nece `y un$E de ~M (V).$%\
 Re&[t`L`M `|, r: `1 do pr`3prio &} (`a).$% Tens`!o &! $;: #8 ~( - r I.$% Circuit#/bert*@#D 0): #8 ~(.$%\
 Curto-circuit*@#8 0): #D ~( / r.`R`V &+ `; ~( &t V e r = #? `a a ~:ne~y 0,40 A.\n\
U &t - #? `9 0,4#I 8,4 V.\n\
Curto-circuito: I &t / #? $F A (~pigos#! &+ a`>ce ~n).`x gr`-fico U(I) `, ~! reta: ordenada na origem ~( #bclive -r.\n\
#M ~. (I, U) medi~'*- regress`!o Y, d`- ~( e r (AL 2.1).\n\
$hndo o &} a ~! `1 R: #D ~( / (R + r).~1 &} ideal te*k r = 0 e #8 ~( &X*R.`W Gerador|#8 ~( - r I|~(: ~:`%a\
 `.#- (V);r: `1 `| (`a);I: `X (A)|&} de $?`!o Y?`0nua|9,0 V, #? `a e 0,40 A: #8 8,4 V|c_fqci.ger`W &V de\
 curto-circuito|#D ~( / r|~(: ~:`%a `.#- (V);r: `1 `| (`a)|$; `<~' &X `1|9,0 V e #? `a: I $F A|c_fqci.ger`W`E\
 ~! &+ d`- #8 1,40 V `; #D &q A e #8 1,30 V `; #D 0,60 A.`: ~:`%a `.#- e `1 `|.~) r = (1,40 - 1,30) / (0,60 -\
 &q&p *r `a~/ ~( = U + r #D 1,40 + *r `9 &q = 1,45 V&A ~( = 1,45 V e r = *r `a.`F`%`!o: 1,45 - *r `9 0,6#I\
 1,30 V, `;&zedido.~j~6 `1 `| ~O `y`> `, `> ~! &+ a`>ce e ~pde $?`!$Mando lhe pedimos #| `X.~i`b `> a $?`!o\
 &! $; `, &X*R i~al a ~(.$% &e o &l: #8 ~( + r I *X &}.$% Ler `5clive do gr`-fico `;o +r.`i`>~y a `1 `| em #D\
 ~( / (R + r).~h$% #8 ~( - r I.$% Circuit#/berto: #8 ~(.$% Curto-circuito: #D ~( / r.$% Gr`-fico U(I):\
 declive -r, ordenada ~(.~g~1a &+ `g ~( = 4,5 V e r = #? `a. ~z `, a $?`!o &! $; &_ a `X `, nula?~e\n\
#8 ~( = 4,5 V: &X `X, n`!o h`- ~pda na `1 `|.~f f2e|Efeito Joule, $D`L`M e `+ el`,&y|efeito joule $De`M `.ica\
 `+ `.ica quilowatt-hora custo ~Tca~P `+ ~< a`>cimento disjuntor|c_fqci.$D*_`Acleo|f2d:Geradores: ~:`%a `.#-\
 e `1 `||m5a:A fun`%`!$Madr`-$J e $ku gr`-fico|AE FQ `I `G Y+`3~H el`,&v~m`D a $D`L`M el`,&y: #@ U I.~4\
 ${feito Joule e #x #@ R I`6.`D a `+ el`,&y em J e em kWh e $ku custo.$% #, ~T`%`!~P `+ a um #T~l~1 a`>cedor,\
 ~! torradeira e um ferr`5 engo#Z a`>cem `y`> a `X passa n~! `1.~6 fatura d&0 coYi a `+, em kWh, n`!#/\
 $D`L`M.~k$% Pot`L`M el`,&y: #@ U I #m W).$% Efeito Joule: #@ R I`6 (`+ el`,&y passa a `+ `|).$% Tamb`,m #@\
 U`6 / R.$% `G: #6 P `8t; 1 kWh = 3,6 `)`U J.$% Conserva`%`!#! $D`L`M do &}, ~( I, `, i~al ~] $r ~K $D`L`Ms\
 &! `;~[s, incluindo r I`6.$% *K`5 um &}: ~0 U / ~(.`R`V a`>cedor de 46 `a `<d#/ 230 V.\n\
#@ 230`6 / 46 = 1,2 `)`B W.#o $v h: #6 1,15 `9 $v = 2,3 kWh.~6 0,16 *h `y kWh, o custo `, 2,3 `9 0,16 = 0,37 *h.\n\
Exempl`5 ~T`%`!o: &+ `; ~( &t V, r = #? `a e #D 0,40 A.\n\
~( #D 3,6 W; r I`6 = 0,24 W; U #D 8,4 `9 0,4#I 3,4 W.\n\
3,6 W = 0,24 W + 3,36 W: a `+ ~T-se.`x efeito Joule `, `Atil em a`>cedore&x indesejado &! fio&x &!\
 `;putadores.`W Pot`L`M el`,&y|#@ U I|U: $?`!*@V);I: `X (A)|&M`>r `;~[|230 V e &O A: #@ 1,2 `)`B\
 W|c_fqci.$D`W Efeito Joule|#@ R I`6|R: `1 (`a);I: `X (A)|$D`L`M &i n~! `1|10 `a e $v A: #@ 40 W|c_fqci.$D`W\
 `G el`,&y|#6 P `8t|P: $D`L`M (W ou kW);`8t: `gp*@s ou h)|1 kWh = 3,6 `)`U J|1,15 kW &C $v h: #6 2,3\
 kWh|c_fqci.$D`W`E ~! `1 de 10 `a `, ~pcorrida `y $v A &C &O min.`: $D`L`M e `+ dissipa~K.~) #@ R I`6 ~N `9\
 $v`6 = 40 W~/ `8t = &O `9 6#I $g `)`6 s~C #6 P `8t = 40 `9 30#I 1,2 `)`P J&A #@ 40 W e #6 1,2 `)`P\
 J.`F`%`!o: em kWh, 12 0*P 3,6 `)`U ~> 0,0033 kWh, um ~b pe`>no.~j~6 $D`L`M diz a rapidez `; `> a `+ `, ~^; a\
 `+ `, o `> se paga.\n\
Poupar `+ `, #x ~H $D`L`M ou &C ~H `gpo.~i`[ $D`L`M (W) `; `+ (J ou kWh).~+ `8t em minutos `; P em W `H obter\
 J.`i`>~y $Madrad${m R I`6.`b `> o kWh `, ~! un$E de $D`L`M.~h$% #@ U #D R I`6 = U`6 / R.$% #6 P `8t; 1 kWh =\
 3,6 `)`U J.$% ~( #D r I`6 + U I.$% #<(&}&p U / ~(.~g~1a l`kmpad~, 10 W $.`- acesa &O h `y *W &C 30 *Ws.\
 Quanta `+ Y4, em kWh?~e\n\
#6 0,010 `9 &O `9 3#I #? kWh.$p 1|f2e1|Re&[t`L`M e $D`L`M `ca l`k#{|c_fqci.ohm|f2a~{`M$} ~! l`k#{ `<da a 230\
 V `, ~pcorrida `y 0,26 A. Cal$P a `1 #' $D`L`M.`E #8 230 V; #D 0,26 A.$L`^`%`!o:~) YB U / #D 230 / 0,26 =\
 8,8 `)`6 `a~/ #@ U #D 230 `9 0,26 = 60 W`Q R ~> 8,8 `)`6 `a e P ~> 60 W.`S`%`!o: `, ~! l`kmpad~, `] 60 W.`=\
 dar `K `o do `> o$( 0,26 A (2).$p 2|f2e2|Pilha `; `1 `| `<da a ~! `1|c_fqci.ger|f2d~{`M$} ~! &+ `; ~( = 4,5\
 V e r = #? `a alimenta ~! `1 de 7,5 `a.$/ a `X*- $?`!o &! $; e o ~< da &+.$L`^`%`!o:~) #D ~( / (R + r&p 4,5\
 / (7,5 + #?&p ~c A~/ #8 ~( - r #D 4,5 - #? `9 ~c = 3,8 V~C ~0 U / ~( = 3,75 / 4,5 `)#I 83 %`Q #D ~c A, U ~>\
 3,8 V e #< ~> 83 %.`S`%`!o: `] 17 % da `+ ~v na &+ (efeito Joule em r).`= #x #D ~( / R, es`>cend#/ `1 `|.$p\
 3|f2e3|#V custa um a`>cedor?|c_fqci.$D|f2e~{`M$} um a`>cedor de $v kW Y% $g h `y *W &C 30 *Ws. Considera\
 0,16 *h `y kWh.$/ a `+ Y4 #m kWh e em J) e o custo.$L`^`%`!o:~) Tempo &<: $g `9 3#I 90 h~/ E ~} `9 9#I 1,8\
 `)`6 kWh~C Em joules: 180 `9 3,6 `)`U = 6,5 `)`m J$q Custo: 180 `9 0,16 = 29 *h`Q 1,8 `)`6 kWh, `] 6,5 `)`m\
 J, e `] 29 *h.`S`%`!o: reduzir ~! hora `y *W poupa `] 9,6 *h `y m`Ls.`= &a a $D`L`M em W #B `gp${m hora&x\
 cha#Z-lhe kWh.\n\
"
 return _ns('D', _dz(D))


_F['p_f2'] = _m_p_f2


def _m_p_f3():
 D = "#3#5 6#4 `GY5`3~H t`,&] ~-`%`!o~f f3a|Sis`ga, `+ `| e `2|&[`ga fro*Vir~3ca &[`ga *. fechad#/berto `+ `| `2\
 kelvin celsiu&xquiliYfermico zer#/b`^to termo$,|c_`;u.uni*_`Acleo|r7c:`G: fo$), $S`L`Ms, `2 e &k$7 `I\
 `GY5`3~H t`,&] ~-`%`!o~m`u &[`ga, fro*Vira e *u`%a.$% Classi~vr &[`gas `;o isola~', fecha~' ou abertos.`J a\
 `+ `| `; as `n`0`Z do &[`ga.$% Converter `2s ~B Celsiu&x Kelvin.~4 ${quil`0Yf`,rmico.~l&D $.udar $V$( `+,\
 escolhe-se o `> i*Vressa (o &[`ga) e se`H-se do r$.o.~6 `2 med#' agita`%`!o ~K `n`0`Z: Y^ `K agita~K, `K\
 `>*V.~k$% Sis`ga: o `> se $.uda; *u`%a: o r$.o; fro*Vira: o `> os se`H.$% Isola$} n`!o $V nada; fecha$} s`3\
 $V `+; aberto: `+ e mat`,*k.$% `G `|, U: $r ~K `+s ~K `n`0`Z (#N`,$J e $De`Ml).$% Tem~patura: relacionada `;\
 a `+ #N`,$J m`,*W ~K `n`0`Z.$% T (K&p $C (`hC) *S73,15.$% Equil`0Yf`,rmico: ~w&xm Y?acto ~vm ~] #9 `2.`R`V\
 25 `hC &8m a 25 *S73,15 = 298,15 K.~1a ~q`%`!`5 1 `hC `, i~al a ~! ~q`%`!`5 1 K.`x zer#/b`^to, 0 K = -273,15\
 `hC, `, a `2 `K baixa poss`0~A.~1 term`3$, med#' sua pr`3p*k `2: `, $u es~par pel${quil`0Yf`,rmico.\n\
Y1 `? ~] #9 `2 `g `K `+ `|.~1a garrafa-term#/proxima-se `c &[`ga *..`x ~w h~!no `, u$!is`ga aberto: $V\
 mat`,&9 `+.`W Kelvin e Celsius|T = $C *S73,15|T: `2 (K);$C: `2 (`hC)|`8T (K&p `8$C (`hC)|25 `hC = 298,15\
 K|c_`;u.uni`W`E a `-~a ferv#' $A `hC (*Rss`!&Eormal) e #/zoto l`0quid#/ 77 K.`: es#( as #P `2s nas\
 dua&xscalas.~) $A `hC ~N0 *S73,15 = 373,15 K~/ 77 K = 77 - 273,15 = -196 `hC&A $A `hC = 373,15 K e 77 K ~>\
 -196 `hC.`F`%`!o: em kelvin as `2s s`!$km*R &,tivas.~j\n\
Escolher bem o &[`ga `, o *{ pass`5 &M`>r balan`%${nerg`,tico.~i`[ `2 `; `+ `|.$% So#Z 273 a ~! ~q`%`!`5\
 `2.`b `> u$!is`ga fechad&E`!o $V `+.`i#( \"graus kelvin\" (diz-se s`3 kelvin, K).~h$% Sis`ga, *u`%a e\
 fro*Vira.$% Isolado, fechad${ aberto.$% T (K&p $C (`hC) *S73,15.$% Equil`0Yf`,rmico: ~5 `2.~g~1a lata\
 fechada a`>c#'*vol. \xc9 u$!is`ga *., fechado ou aberto?~e\n\
Fecha$} $V `+ ($I ~-`%`!o), #p n`!o $V mat`,*k.~f f3b|Calor, `@ e ~-`%`!o; YQ`k`M e pain`,is ~Wo#0iYg|&k `@\
 ~-&S $Se`M de `+ ir~-`M #y ~Wo#0ico coletor solar &Qao &R&S in&.&ro ~<|c_fqte.pv*_`Acleo|f3a:Sis`ga, `+ `| e\
 `2$7 `I `GY5`3~H t`,&] ~-`%`!o~m$% *+~vr &k, `@ e ~-`%`!o `;o $S`L`M$( `+.`J a ~-`%`!${mitida `; a `2.`v\
 YQ`k`M.`D o #)`5 um #y ~Wo#0ico.~l`x Sol a`>ce-&! &X Y?act#! `+ chega `y ~-`%`!o.\n\
Esfregar as m`!os a`>ce-as `y `@; ~! caneca `>nt#'`>ce-as `y &k.~k$% Calor: `+ ~^ `y `e`%~, `2 (Y@`%`!${\
 &d`%`!o).$% Trabalho: `+ ~^ `y a`%`!`5 ~:`%as (ou `y `X el`,&y).$% Ra*W`%`!o: `+ ~^ `y on~K `.Y<`,$Js, ~; no\
 v`-cuo.$% To~' os ~w&xmi`g ~-`%`!o; Y^ `K `>$), `K emi`g.$% Irradi`k`M: Er = P / A (W m`(`6).$% Painel: ~0\
 P(el`,&y) / P(~-`%`!o) `)Y_`R\n\
\xc0 `2 ambie*V, os ~w&xmi`g sobretudo in&.&ro; ~n `>$), *2`,m *Q`0~A.~1 bom &Rsor de ~-`%`!o `, *2`,m um bom em~ur.\n\
Su~pf`0cie&xscuras ~Vm `K; su~pf`0cies clara&x poli~K refle`g `K.\n\
Co$!ol direto, ~] su~pf`0cie da Terra, Er ~> &) `)`B W m`(`6.`V um #y de $v m`6 `; Er = &) `)`B W m`(`6 $I P\
 ~} `)`B W.\n\
Se produzir 320 W el`,&v: ~0 320 / 2000 `)#I 16 %.\n\
Painel ~Wo#0ico: ~-`%`!o ~7 `+ el`,&y.\n\
Coletor solar: ~-`%`!o ~7 `+ `| da `-~a.`x #)`5#F inclina`%`!o, da `2 e da hora do *W.`W Irradi`k`M|Er = P /\
 A|P: $D`L`M da ~-`%`!*@W);A: `-$- (m`6)|~-`%`!o ~p*|$Pr ~] su~pf`0cie|&) `)`B W m`(`6 em $v m`6: P ~} `)`B\
 W|c_fqte.pv`W *K`5 um #y ~Wo#0ico|~0 P(el`,&y) / (Er A) `)0 %|Er: YQ`k`M (W m`(`6);A: `-$- (m`6)|#< < $A\
 %|320 W de 2000 W: ~0 16 %|c_fqte.pv`W`E um #y de 1,6 m`6 $I Er = 8,0 `)`6 W m`(`6 e ~:nece &1 A a 48 V.`:\
 ~<.~) P(rad&p 8,0 `)`6 `9 1,6 = 1,3 `)`B W~/ P(el&p U #D 48 `9 &1 = 1,9 `)`6 W~C ~0 192 / 1280 `)#I 15 %&A\
 #< ~> 15 %.`F`%`!o: $.`- na gama habitual ~' pain`,is `;erciais (`] 15 % a 22 %).~j~6 `+ do Sol `, renov`-~A\
 e gratuita; `5safio `, aproveit`--la `; bom ~<.~i`b `> o &k `, `+ \"Y?ida\" *X ~w.`i`>~y `> a ~-`%`!&E`!o\
 *Rcis~, meio &F.~+ a `-$- em cm`6 &X converter.`[ #y ~Wo#0ico `; coletor solar.~h$% Calor, `@ e ~-`%`!o $Sem\
 `+.$% Er = P / A.$% ~0 P(el) / P(rad) `)Y_~g&5`> `, `> os coletores solares Ygt~!$!er *Rtos?~e~6s\
 su~pf`0cie&xscuras ~Vm `K ~-`%`!o; assim, $Se-se `K `+ `H a `-~a.~f f3c|Condu`%`!${ &d`%`!o|Y@&S &d&S *%$E\
 ter~Q isolamento termico bom &K *.r fluido `X$( &d&S janela parede|c_fqte.cond*_`Acleo|f3b:Calor, `@ e\
 ~-`%`!o; YQ`k`M e pain`,is ~Wo#0iYg$7 `I `GY5`3~H t`,&] ~-`%`!o~m~4 a Y@`%`!${ a &d`%`!o.$% #M`Hr *f *q *%$E\
 t`,r~Q.`D a `+ ~^ `y Y@`%`!${m ~I segundo.`J o isolamento t`,rmico `; mate*ki$( k pe`>no.~l~1a colher de $|\
 *X ch`- `>nt#'`>c#'t`, ao cabo: `, Y@`%`!o.~6 `-~a a`>cida no fund~P panela sobe #' fri~,sce: `,\
 &d`%`!o.~k$% Condu`%`!o: $S`L`M `y colis`' ~B `n`0`Z, &X *^`yte $[`,*k.$% Convec`%`!o: $S`L`M pel&zoviment~9\
 pr`3prio fluid*@l`0quido ou g`-s).$% Condutiv$E t`,r~Q, k (W m`(`4 K`(`4): facil$E em Y@zir.$% #@ k A `8T /\
 $Z: `+ ~^ `y segundo.$% Bons &Kes: ~J (k #[); *.res: ar, l`!, esferovite (k pe`>no).`R\n\
Valores *C~' de k (W m`(`4 K`(`4): #L 4 `)`6; vidro 0,8; ar 0,03.`V janel~, vidro `; #? m`6, &1 m*A $y e 20 K\
 de `e`%a.\n\
#@ 0,80 `9 #? `9 20 / 0,0040 $F `)`B W.`xs vidros duplos t`Lm ~! *]~, ar, `> Y@z ~n *6.`x fluido `>*V `, ~H\
 dens${ sobe; o fri`5sce.~6 &d`%`!o ~O as brisas, #/`>ciment`5 ~! sala #'s `Xs oce`k$8s.`xs ~-dores ~vm em\
 baix${ os YJ$( ar condicionad${m cima.`W Condu`%`!o t`,r~Q|#@ k A `8T / $Z|k: *%$E t`,r~Q (W m`(`4 K`(`4);A:\
 `-$- (m`6);`8T: `e`%~, `2 (K);$Z: $y (m)|regime $.acion`-rio|vidro, #? m`6, 20 K e &1 mm: P $F `)`B\
 W|c_fqte.cond`W`E pared#b 10 m`6, &q *A $y e k = 0,60 W m`(`4 K`(`4; 20 `hC dentr${ 5 `hC ~:a.`: `+ ~pdida\
 `y Y@`%`!&E~! hora.~) `8T = 20 - 5 = 15 K~/ #@ 0,60 `) `9 15 / &q = 4,5 `)`6 W~C #6 450 `9 360#I 1,6 `)`U\
 J&A PerdeY' `] 1,6 `)`U J `y hora.`F`%`!o: Y: a $y reduzi*k a ~pda a metade.~j\n\
Isolar bem ~! casa reduz a `+ ~pdida #' fatura d#/`>cimento.~i`b `> na &d`%`!&E`!o h`- *^`yte $[`,*k.`i`>~y\
 de &; a $y `H $,s.`b `> o $| fri#/o to`> $.`- a ~o `2 do `> a madeira ao lado.`[ *%$E t`,r~Q `; $0\
 el`,&y.~h$% Condu`%`!o: colis`' ~B `n`0`Z.$% Convec`%`!o: moviment~9 fluido.$% #@ k A `8T / $Z.$% k pe`>no:\
 bom *.r.~g~1 tapete e um ch`!`5 mosaico $.`!o ~] #9 `2. Por`> `, `> o tapete parece `K `>*V?~e`x mosaico `g\
 ~R *%$E t`,r~Q: retira `+ do p`, `K de*Rssa e `y ~u parece `K frio.~f f3d|Capac$E t`,r~Q m`-$x e &m`%a$(\
 $.ado|capac$E ter~Q ma$x ~qca`5 entalpi~, fusao va`yiza&S &mc~, $.ado balanc${nergetico `2 de equilibrio\
 pata#Z gel#/~a|c_fqte.cal*_`Acleo|f3a:Sis`ga, `+ `| e `2|a7d:Pro`y$_$E direta|AE FQ `I `GY5`3~H t`,&]\
 ~-`%`!o~m`v capac$E t`,r~Q m`-$x.`D a `+ `H a`>~y um ~w: *) c `8T.`D a `+ `ca &m`%~, $.a$} *) `8H.$% Fazer\
 balan`%o&xnerg`,tiYg $W.~l~6 `-gu~,mora ~n a a`>~y #' arrefe~y: `g ~! capac$E t`,r~Q m`-$x #[.&5 ~u o clima\
 junt#/&zar `, `K ameno.~k$% Capac$E t`,r~Q m`-$x, c: `+ `H a`>~y 1 kg em 1 K (*N`(`4 K`(`4).$% *) c `8T.$%\
 \xc1~a l`0quida: #d 4,18 `)`B *N`(`4 K`(`4.$% Va*k`%`!`5 &H m`-ssic~, &m`%~, $.ado, `8H (*N`(`4): *) `8H.$%\
 Fus`!~9 gelo: Y8 `)~% *N`(`4; va`yiza`%`!~P `-~a: 2,26 `)`U *N`(`4.$% Dur#e ~! &m`%~, $.ado*- `2 n`!o\
 ~q.`R`V a`>~y ~c0 $s `-gu~, 20,0 `hC a 80,0 `hC.\n\
Q = ~c0 `9 4,18 `)`B `9 60,#I 1,25 `)~% J.\n\
Fundir 0,$A $s gel#/ 0 `hC: Q = 0,$A `9 Y8 `)~% = Y8 `)`P J.\n\
#M essa `+, ~5 `-~a l`0quida a`>~yia `] 80 `hC.\n\
Nu$!is`ga *.*- `+ cedida #B ~w `>*V `, i~al ~] *4 #B frio.`V &q0 $s `-~a a 60 `hC `; 0,$A *} 15 `hC.\n\
$Ce = (&q0 `9 60 + 0,$A `9 15) / 0,30#I 45 `hC.#7 gr`-fico $C(t) d#'`>cimento, os pata#Zes s`!#/s &m`%a$(\
 $.ado.`W Capac$E t`,r~Q m`-$x|*) c `8T|m: `? (kg);c: capac$E t`,r~Q m`-$x (*N`(`4 K`(`4);`8T: ~q`%`!`5 `2\
 (K)|&X &m`%~, $.ado|~c0 $s `-~a e 60 K: Q = 1,25 `)~% J|c_fqte.cal`W Mudan`%~, $.ado|*) `8H|`8H: ~q`%`!`5 &H\
 m`-$x (*N`(`4)|`2 ~L|0,$A $s gelo: Q = Y8 `)`P J|c_fqte.$.`W Tem~patur~, equil`0brio|$Ce = (m1 c1 $C1 + m2\
 c2 $C2) / (m1 c1 + m2 c2)|1 e 2: os &G ~ws|&[`ga *., &X &m`%a$( $.ado|&q0 *} 60 `hC e 0,$A *} 15 `hC: 45\
 `hC|c_fqte.eq`W`E 0,300 $s `-~a a 40 `hC $Im 0,050 $s gel#/ 0 `hC, *X recipie*V *..`: `2 ~t.~) Fundir *y:\
 0,050 `9 Y8 `)~% = 1,7 `)`P J~/ Balan`%o: 0,300 `9 4180 `9 (40 - $Ce&p 16 700 + 0,050 `9 4180 `9 $Ce~C $Ce =\
 (50 160 - 16 700) / (1254 *S09&p 23 `hC&A $Ce ~> 23 `hC.`F`%`!#! `-~a arrefece ~n, `y`> fundir *y Y4 #|\
 `+.~j~6 #[ capac$E t`,r~Q m`-$x da `-~a torna-a `3tima `H *^`ytar `+ (~-dores, motores).~i$% So#Z 273 a ~!\
 `e`%~, `2.`i`>~y a `+ da &m`%~, $.ado &! balan`%os.~+ a `? Ye#p.`b `> a `2 sobe &C a fus`!o.~h$% *) c `8T.$%\
 *) `8H (`2 ~L).$% Sis`ga isola$} `+ cedida = `+ *4.~g&5`> `, `> ~! mistur~, `-~a e gelo ~v a 0 `hC enY^\
 houver gelo?~e~6 `+ *4 `, usada `H fundir o gel*@&m`%~, $.ado), n`!o `H subir a `2.~f f3e|*F e #s Leis\
 Y.`k~Q e ~<|primeira lei da termodina~Q segunda lei `+ `| convenca`5 sinai$(gradaca~P `+ maYD ter~Q ~<\
 ~T&S|c_fqte.pl*_`Acleo|f3d:Capac$E t`,r~Q m`-$x e &m`%a$( $.ado$7 `I `GY5`3~H t`,&] ~-`%`!o~m$% Enu`Mr a *F\
 Lei Y.`k~Q.$% #, conven`%`!`5 sinais.$% &f a #s Lei `;`5grada`%`!~P `+.`D o #)`5 m`-YDs t`,r~Qs.~l~6 `+\
 nunca se ~pde, #p ~v ~I vez ~H `Atil.~1 motor nunca *^~:ma toda a `+ do `;bust`0~A em movimento.~k$% *F Lei:\
 `8#8 W + Q + R (~T`%`!~P `+).$% `G *4 #B &[`ga `, &,tiva; cedida `, negativa.$% Sis`ga isola$} `8#8 0.$% #s\
 Lei: &! processo&xs*9`kYG*- `+ `Atil ~E (degrada`%`!o).$% O &k flui es*9aneame*V do ~w `>*V `H o frio.$%\
 Nenh~! m`-YD t`,r~Q `g #)`5 $A %.`R`V um g`-s $I #t J `y &k e $-&^ 200 J de `@ sobre ~3`%a.\n\
W = -200 J e Q = +#t J&W `8#8 -200 + 50#I 300 J.\n\
#Mprim#g*Rssa #/r `ca bomb~, bicicleta: W > 0 #' `2 sobe.Yd`-YD t`,r~Q: $I `+ `ca fo*V `>*V, $-&^ `@ e cede o\
 r$.#/ ~! fo*V f*k.$Lndimento: ~0 W / Q(~:&J `)Y_`V um motor $I &) `)`P J e $-&^ 2,5 `)`B J de `@: ~0 25\
 %.`xs r$.a$) 7,5 `)`B J #_ n~3`%a.`W *F Lei Y.`k~Q|`8#8 W + Q + R|W: `@;Q: &k;R: ~-`%`!*@J; recebi~' >\
 0)|&M`>r &[`ga|Q = #t J e W = -200 J: `8#8 300 J|c_fqte.pl`W *K`5 ~! m`-YD t`,r~Q|~0 W / Q(~:&J `)0 %|W: `@\
 `Atil (J);Q(~:&J: `+ *4 da fo*V `>*V (J)|#< < $A % (#s Lei)|2,5 `)`B J de &) `)`P J: ~0 25 %|c_fqen.ren`W`E\
 ~3`%a $-&^ 150 J de `@ sobre u$!is`ga, `> cede 400 J `y &k; YB 0.`: ~q`%`!~P `+ `|.~) W = +150 J (recebido)\
 e Q = -400 J (cedido).~/ `8#8 150 - 400 + #I -250 J&A `8#8 -250 J: a `+ `| ~E.`F`%`!#W &[`ga cede `K `+ do\
 `> $I, `y ~u `8U < 0.~j~6 *F Lei diz `> a `+ se ~T; a #s diz `H *I ela se \"espalha\".~i$% &e os sinai$( W\
 #b Q.`b `> a `+ dissipad~,*e`i~par ~<$( $A %.`[ &k `; `2.~h$% `8#8 W + Q + R.$% Recebido > 0; cedido < 0.$%\
 #s Lei: degrada`%`!~P `+; #< < $A %.~g~6 `+ `| `c &[`ga *. &{ `wr?~e\n\
N`!o: nu$!is`ga *. W = Q = YB 0&W `8#8 0.~f f3f|Lei$( *J #b Wien (ex$?`!o)|lei de stefan-boltzmann lei de\
 wien #2`5 wien ~w negr${missiv$E `;`}`5 ond~, maxima &Qao $.relas cor||10|ex$?`!o|f3b:Calor, `@ e ~-`%`!o;\
 YQ`k`M e pain`,is ~Wo#0iYg||Ex$?`!*@~:a ~K AE do 10.#w ano); ~Ls da &L d${xam#b FQ A~m`J a $D`L`M emitida `;\
 a `2.`J o `;`}`5 ond~, m`-xima &Q`!o `; a `2.$% Reconhe~y `> $.as leis s`!${x$?`!&Eo 10.#w ano.~l~1 ferr#/o\
 rubro brilha &ro; `K `>*V, ~v Yinc#! cor $c da `2.~k$% Ex$?`!o: $.as leis n`!o fazem `ne ~K A*Rndizagens\
 Esse`Mis do 10.#w ano.$% *J: #@ e YN A T`P (T em K).$% YN = 5,67 `)`(`m W m`(`6 K`(`P; e: &Qiv$E, ~B 0 e\
 1.$% Wien: `_m`-x T = 2,898 `)`(`B m K.$% #V ~R T, ~o `_m`-x.`R\n\
Wien: o Sol*- `] 5800 K, #K `K a `_m`-x = 2,898 `)`(`B / 580#I &O `)`(~? m (*Q`0~A).\n\
Wien: o ~w h~!no*- 310 K, #K `K a `_m`-x ~> 9,3 `)`(`U m (in&.&ro).\n\
*J: Y: T *L a $D`L`M emitida `y 2`P = 16.~6s c`k#Zas t`,r~Q$(tetam o in&.&r${mitido #Bs ~ws.`W #j *J\
 (ex$?`!o)|#@ e YN A T`P|YN = 5,67 `)`(`m W m`(`6 K`(`P;e: &Qiv$E;A: `-$- (m`6);T: `2 (K)|T em kelvin|Y: T: P\
 &g 16|`W #j Wien (ex$?`!o)|`_m`-x T = 2,898 `)`(`B m K|`_m`-x: `;`}`5 ond~, m`-xima &Q`!*@m);T: `2 (K)|~w\
 negr*@*C`%`!o)|Sol, 5800 K: `_m`-x = &O `)`(~? m|`W`E ~! $.rela `g `_m`-x = $g `)`(~? m.`: `2 da\
 su~pf`0cie.~) T = 2,898 `)`(`B / ($g `)`(~?&p 9,7 `)`B K&A T ~> 9,7 `)`B K.`F`%`!o: `_m`-x ~o do `> ~9 Sol&W\
 a $.rela `, `K `>*V.~j~6 cor ~K $.relas Y/ #c `2: as azula~K s`!#/s `K `>$).~i~+ a `2 em `hC.`i`>~y a quarta\
 $D`L`M em *J.`b `> um ~w fri&E`!${Ya ~-`%`!o.~h$% #@ e YN A T`P.$% `_m`-x T = 2,898 `)`(`B m K.$% Y1 `>*V:\
 #K `K #' ~o `_.~g~1a $.rela azulada e outra a&rada: &M `g ~R `2 ~] su~pf`0cie?~e~6 azulada: ~o `_m`-x &8 a\
 ~R `2 (lei de Wien).$p 1|f3e1|A`>~y `-~a|c_fqte.cal|f3d~{`M$} `> `+ `, necess`-*k `H a`>~y $v $s `-gu~, 15\
 `hC a 45 `hC?`E m ~} kg; #d 4,18 `)`B *N`(`4 K`(`4; `8$C = 30 `hC.$L`^`%`!o:~) `8T = 45 - 15 = 30 K~/ Q ~}\
 `9 4,18 `)`B `9 3#I 2,5 `)~% J`Q Q ~> 2,5 `)~% J.`S`%`!o: `, #| `+, `y`> a `-~a `g c elevada.`= $rr 273 ~]\
 ~q`%`!`5 `2.$p 2|f3e2|#V `gp`5mora ~! chaleira?|c_fqte.cal|f3d~{`M$} ~! chaleir~, 2000 W a`>ce &) $s `-gu~,\
 20 `hC a $A `hC, `; #)`5 8Y_\n\
#V `gp`5mora?$L`^`%`!o:~) Q(`Atil&p &) `9 4180 `9 8#I 3,3 `)~% J~/ E(~:&J = Q(`Atil) / 0,8#I 4,2 `)~% J~C `8t\
 = E / #@ 418 0*P 200#I 2,1 `)`6 s`Q `] 2,1 `)`6 s (3,5 min).`S`%`!o: &X ~p~K, basta*km 1,7 `)`6 s.`= &a #B\
 ~< &s de dividir.$p 3|f3e3|Medir a entalpi~, fus`!~9 gelo|c_fqte.eq|f3d~{`M$} *X &k`0$,, */ $s `-~a a 40,0\
 `hC $Im 0,060 $s gel#/ 0 `hC; a `2 ~t `, 1*O `hC.$/ `8H de fus`!${ ${rro ~pcentual (~b &L$} Y8 `)~%\
 *N`(`4).$L`^`%`!o:~) Cedida *q `-~a: */ `9 4180 `9 (40,0 - 1*O&p 2,51 `)`P J~/ Para a`>~y *y fundid#%`, 1*O\
 `hC: 0,060 `9 4180 `9 16,#I &1 `)`B J~C Para fundir *y: 25 080 - 4013 = 2,1 `)`P J$q `8H = 21 067 / 0,06#I\
 3,5 `)~% *N`(`4\n\
5. Erro: (3,51 - Y8) / Y8 `)#I 5 %`Q `8H ~> 3,5 `)~% *N`(`4, `; err`5 `] 5 %.`S`%`!#W &k`0$, n`!o `, ~pfeito:\
 $V alg~! `+ `; ~3`%a.`= es`>~y `> *y fundido *2`,m a`>c#b 0 `hC a 1*O `hC.\n\
"
 return _ns('D', _dz(D))


_F['p_f3'] = _m_p_f3


def _m_p_q1():
 D = "#3#5 5#4 ~| ~' `-`T~f q1a|Constitui`%`!~9 `-$4 e is`3$l|a$4 nucleo &=ao $2ao `.a&Eu$<#%omic&Eu$<`5 `? isotopo\
 iao YCa#/niao|c_fqat.ar*_`Acleo|r9d:\xc1`T, distribui`%`!o `.`3$8 e `<`%`!$M`0~Q$7 `I ~| ~' `-`T~m$% Des#( o\
 `-$4: n`Acleo `; &=`' e $2`', e `.`'.`v n`A$<#%`3mic*@Z) e n`A$<`5 `? (A).`D &E`A$<`5 $2`' a `n#g Z #b A.`u\
 is`3$l `c ~; `N.`J a ~M `c i`!o `; os `.`' ganhos ou ~pdi~'.~l\n\
Imagina um $.`-dio `; ~! ervilha no centro. A ervilha `, &E`Acleo, `; *w toda a `?. Os `.`' YP o r$.o, *w\
 vazio.`x n`A$<`5 &=`' `, o \"cart`!`5 cidad`!o\" do `N. Outr&E`A$<`5 $2`' d`- outro is`3topo. Outr&E`A$<`5\
 `.`' d`- um i`!o.~k$% Prot`!*@~M +1) e $2`!*@&X ~M) $.`!&E&E`Acleo.$% &6`!o: ~M -1; `? 1840 &g ~o `> a do\
 &=`!o.$% N`A$<#%`3mico, Z: n`A$<`5 &=`'.$% N`A$<`5 `?, A: &=`' + $2`'.$% Is`3$l: `-`T `; o ~; Z e `ete A.$%\
 Re*Rsenta`%`!o: `B~%&T\u2087Cl (A em cima, Z em baixo).`R`x n`A$<`5 $2`' obt`,Y' `y *U A - Z.#7 `-$4 $2o h`-\
 tantos `.`' `;o &=`'.~1 i`!o &,tiv*@YC`!o) ~pdeu `.`'.~1 i`!&Eegativ*@ani`!o) ganhou `.`'.`V Na~X `g 11 &=`'\
 e 10 `.`'.`V Cl`( `g 17 &=`' e 18 `.`'.`xs is`3$l do &: s`!o `4`6C, `4`BC e `4`PC.\n\
T`Lm 6, 7 e 8 $2`', #p to~' t`Lm 6 &=`'.\n\
T`Lm o ~; `;`ytament$M`0mico, `y`> t`Lm os ~;s `.`'.\n\
Diferem na `? e na $.abil$E d&E`Acleo.\n\
Cas${special: o `4H n`!o `g $2`'.`x n`Acleo `, `] $A 000 &g ~o do `> o `-$4.`x `-$4 `g di`kmetr~P $@ de\
 10`(`4$N m.`W N`A$<`5 $2`'|*U A - Z|N: n`A$<`5 $2`';A: n`A$<`5 `?;Z: n`A$<#%`3mico|&M`>r n`Acleo|`B~%Cl: *U\
 35 - 17 = 18|`W &6`' `c i`!o|n.#w de `.`' = Z - ~M|Z: n`A$<#%`3mico;~M: ~M do i`!o, `; &l (+2, -1...)|i`'\
 monoat`3miYg|Mg`6~X: 12 - 2 ~N `.`'|`W`E i`!o `B`6&T*jS`6`( (enxofre).`: &=`', $2`' e `.`'.~) Prot`': Yj\
 16.~/ Neutr`': *U A - Yj 32 - 16 = 16.~C A ~M 2- Y/ `> ganhou 2 `.`'.$q &6`': 16 *S = 18.&A 16 &=`', 16 $2`'\
 e 18 `.`'.`F`%`!o: ~M = 16 - 18 = -2.~j\n\
Z identi~v o `N: se Z muda, muda o `N. A ~M `c i`!o ve$!`3 ~' `.`' ganhos ou ~pdi~'.`x n`Acle&E`!&zuda n~!\
 $-`%`!$M`0~Q. O &No ~K \"bolinhas\" `, ~! simpli~v`%`!#Ws `.`' n`!o t`Lm *n`3*k$(fini~K.~i`[ A `; &E`A$<`5\
 $2`': *U A - Z.`b `> um YC`!o ganhou `.`': ~pdeu.$% YS `> is`3$l s`!o `Ns `etes: t`Lm o ~; Z.`i`>~y `> a `?\
 $.`- *w toda n&E`Acleo.$% &e A e Z na re*Rsenta`%`!o: A ~v em cima.~h$% \xc1$4: n`Acle*@&=`' e $2`') e\
 `.`'.$% Yj n.#w de &=`'; A = &=`' + $2`'.$% *U A - Z.$% Is`3$l: ~; Z, `ete A.$% Cati`!o ~pdeu `.`'; ani`!o\
 ganhou.$% O n`Acleo `, `] 10~% &g ~o `> o `-$4.~g$w $2`' e #+ `.`' `g o i`!o ~%`U`/*jFe`B~X?~e\n\
Neutr`': *U 56 - 26 = 30.\n\
&6`': 26 - 3 = 23.~f q1b|Tamanho ~' `-`T: ordens ~8 e escalas|$@ ~8 *oca&Ii~v escala nano$, pi`;etro #v $i\
 aY9ic&Eanotecnologia|c_`;u.uni*_`Acleo||n8b:Nota`%`!&I`0~v|AE FQ `I ~| ~' `-`T~m`i#( n`A$<o&xm\
 *o`%`!&I`0~v.$% Determinar a $@ ~8 `c ~b.$% #M`Hr #vs dividindo ordens ~8.$% Converter ~B m, nm e pm.$%\
 Situar objet*:a&xscalas, do $, a&E`Acleo.~l`xs `-`T s`!o ~n pe`>&! `H *:`A$<*< *W a *W.\n\
Es#( 0,000 000 000 1 m cansa e engana.\n\
1 `)`(`4$N m diz &zesm`5 ~:ma curta.~6 $@ ~8 `, a $D`L`M de 10 `K pr`3xima.\n\
Serve `H `;`Hr &X Y?as finas.~k$% Nota`%`!&I`0~v: a `)&U, `; YV < 10 e n i*Viro.$% Ordem ~8: $D`L`M de 10 `K\
 pr`3xima do ~b.$% Regra: s#' < 5*- $@ `, 10&U; s#' #O 5, `, 10&U~X`4.$% Alguns livros usam 3,16 (raiz de 10)\
 &s de 5.$% 1 nm ~N`(`l m e 1 pm ~N`(`4`6 m.`R`x rai~9 `-Y9`5 ~2`,#X `, 5,3 `)`(`4`4 m.\n\
#Mo 5,3 #O 5*- $@ ~8 `, 10`(`4$N m.~1 cabelo `g `] 8 `)`(~% *A largura.~6 sua $@ ~8 `, 10`(`P m.&D `;`Hr, *g:\
 10`(`P / 10`(`4$N ~N`U.`x cabelo `, `] um milh`!`5 &g `K largo.\n\
Escala$( #v:$% objetos *Q`0$K: 10`(`P m ou `K;$% c`,lulas: `] 10`(~% m;$% nanoescala: 1 nm a $A nm;$% `-`T:\
 `] 10`(`4$N m;$% n`Acleos: 10`(`4~% m a 10`(`4`P m.~6 nanotecnologia usa *f `; 1 nm a $A nm.`W\
 Nota`%`!&I`0~v|x = a `)&U, `; YV < 10|a: mantissa;n: expoe*V (i*Viro)|&M`>r n`A$<o `et#b 0|0,00052 = 5,2\
 `)`(`P|c_`;u.sci`W Ordem ~8|OG ~N&U s#' < 5; OG ~N&U~X`4 s#' #O 5|a e n: da *o`%`!&I`0~v a `)&U|`;`Hr\
 #vs|5,3 `)`(`4`4 m `g OG 10`(`4$N m|`W Nan`3$, e pic`3$,|1 nm ~N`(`l m; 1 pm ~N`(`4`6 m|nm: nan`3$,;pm:\
 pic`3$,|`;`}os ~] escala at`3~Q|154 pY) #?4 `)`(`4$N m|c_`;u.uni`W`E um `-Y9`5 ouro `g 0,288 n*A di`k$,.~1a\
 folh~, ouro `g &) `)`(~? *A $y.`: #+ `-`T cabem na $y.~) 0,288 nY) 2,88 `)`(`4$N m.~/ $] &) `)`(~? m / 2,88\
 `)`(`4$N Y) 347~C #M 2 `o: n ~> 3,5 `)`6.$q #Mo 3,5 < 5*- $@ ~8 `, 10`6.&A Cabem `] 350 `-`T ($@\
 10`6).`F`%`!o: 350 `9 2,88 `)`(`4$N m ~> &) `)`(~? m.~j~6 $@ ~8 d`- a escala, n`!o o ~b exato. Chega `H\
 `;`Hr objetos ~n `e*m`xs `-`T n`!o t`Lm ~! fro*Vira n`0tida. Por ~u, o rai`5pende d&z`,tod`5 medida #'s &Ls\
 d`!o ~bes um *6 `e*m~i`i#( 34 `)`B &s de 3,4 `)`P.$% Errar o &l d${xpoent#'o &; de pm `H m.$% #, #E 5 &X &;\
 `H *o`%`!&I`0~v.$% So#Z expoe$) ao dividir: subtraeY'.`[ nm (10`(`l m) `; \xb5m (10`(`U m).~h$%\
 Nota`%`!&I`0~v: a `)&U, `; YV < 10.$% Ordem ~8: 10&U s#' < 5; 10&U~X`4 s#' #O 5.$% 1 nm ~N`(`l m; 1 pm\
 ~N`(`4`6 m.$% \xc1$4: `] 10`(`4$N m; n`Acleo: 10`(`4~% m a 10`(`4`P m.$% Para `;`Hr, *g (subtraeY'\
 expoe$)).~g`x rai~9 `-Y9`5 ~2`,#X `, 53 pm.\n\
Escreve-${m $,s, em *o`%`!&I`0~v.\n\
InY; #c $@ ~8.~e\n\
53 pY) 5,3 `)`(`4`4 m.\n\
#Mo 5,3 #O 5*- $@ ~8 `, 10`(`4$N m.~f q1c|#: at`3~Q $9|un$E de `? ato~Q `? ato~Q $9 me*W iso$l $Ua`M `?\
 `Ce$Pr $9 mr ar|c_fqat.ar*_`Acleo|q1a:Constitui`%`!~9 `-$4 e is`3$l$7 `I ~| ~' `-`T~m`v a un$E de `? at`3~Q\
 (u).`v `? at`3~Q $9, Ar.`D Ar m`,*W a `nir ~' is`3$l e $U`k`Ms.`D a `? `Ce$Pr $9, Mr.~4 `y`> Ar n`!o `, um\
 n`A$<o i*Viro.~l`xs `-`T s`!o leve$(`K `H se pesarem Ye#p. Usa-se ~! \"un$E de `-$4\": 1/12 da `? do\
 &:-12.~1 `N `, ~! mistur~, is`3$l. Ar `, ~! m`,*W pesada, `;o ~! m`,di~, t$.es `; *>s `e*m O is`3topo `K\
 $U#e pesa `K na m`,*W.~k$% Un$E de `? at`3~Q: 1 u = 1/12 da `? `c `-Y9`5 `4`6C.$% 1 u ~> 1,66 `)`(`6~? kg.$%\
 #: isot`3pica $9: `? do is`3top#/ dividir `y 1 u.$% Abund`k`M: ~S de `-`T de ~I is`3top&Ea natureza.$% Ar:\
 m`,*W ~K `?s isot`3picas, pesada *qs $U`k`Ms.$% Mr: $r ~K Ar de to~' os `-`T da f`3&/.$% Ar e Mr n`!o t`Lm\
 un$Es.`R`x &% `g &G is`3$l $.`-$K.`x `B~%Cl `g `? 34,97 e $U`k`M 75,76 %.`x `B~?Cl `g `? 36,97 e $U`k`M\
 24,24 %.~6r = (34,97 `9 75,76 + 36,97 `9 24,24) / $A = 35,45.`x ~b ~v ~pt`5 35 `y`> o `B~%Cl `, o `K $U#e.\n\
Nenhum `-Y9`5 &% `g `? 35,45: `, ~! m`,*W.&D `C`,`Z, $rm-s#'s Ar de to~' os `-`T.Ydr(H`/O&p 2 `9 &)1 Yb*O#I\
 *H.Ydr(CO`/&p 1$v1 *S `9 1*O#I 4&11.`xs ~be$( Ar $.`!&Ea &L ~pi`3Y;.`x exame usa Ar `; #P casa$(ci`K.`W #:\
 at`3~Q $9 m`,*W|Ar = $o (Ar,i `9 %i) / $A|Ar,i: `? isot`3pica $9 do is`3topo i;%i: $U`k`M do is`3topo i, em\
 %|as $U`k`Ms $rm $A %|Cl: (34,97 `9 75,76 + 36,97 `9 24,24) / $A = 35,45|c_fqat.ar`W #: `Ce$Pr $9|Mr = $o\
 (n.#w de `-`T `9 Ar)|Ar: `? at`3~Q relativ~, ~I `N|&M`>r f`3&/ qu`0~Q|Mr(H`/O&p 2 `9 &)1 Yb*O#I *HYM`W Un$E\
 de `? at`3~Q|1 u = m(`4`6C) / 12 ~> 1,66 `)`(`6~? kg|m(`4`6C): `? `c `-Y9`5 &:-12|`?$( `-`T e `C`,`Z|um\
 `-Y9`5 `4H `g `] &) u|`W`E is`3$l d&zagn`,sio.$% `6`PMg: 23,99 e 78,99 %$% `6~%Mg: 24,99 e 10,00 %$% `6`UMg:\
 25,98 e 1&)1 %`: Ar(Mg).~) YT ~I `? *q $U`k`M.~/ Ar = (23,99 `9 78,99 *S4,99 `),00 *S5,98 `9 1&)1) / $A~C Ar\
 = 2430,9 / $A = 24,31&A Ar(Mg&p 24,31`F`%`!o: 24,31 $.`- ~B 23,99 e 25,98 e ~pt`5 24.`x `6`PMg `, o `K\
 $U#e&W a m`,*W ~v ~pt`5 24.~j~6r `, ~! m`,*W: diz Y^ pesa, em m`,*W, um `-Y9~9 `N.`x is`3topo `K $U#e\
 \"puxa\" a m`,*W.`xs ~bes da &L v`L*A #|s medi`%`' (espectrometri~, `?).~6s $U`k`Ms &{m ~qr um pouc`5\
 amostra `H amostra.~i$% Fazer a m`,*W $W (dividir `y 2) &X #x as $U`k`Ms.`i`>~y de dividir `y $A &_ as\
 $U`k`Ms $.`!${m %.$% Dar un$Es a Ar ou a Mr: s`!&E`A$<os &X un$Es.`[ &E`A$<`5 `? A (i*Viro) `; a `?\
 isot`3pica.$% YS `> to~' os `-`T de &% t`Lm 35,45 u.~h$% 1 u = 1/12 da `? do `4`6C ~> 1,66 `)`(`6~? kg.$% Ar\
 = $o (Ar,i `9 %i) / $A.$% Ar `, a m`,*W pesada ~K `?s ~' is`3$l.$% Mr = $r ~K Ar ~' `-`T da f`3&/.$% Ar e Mr\
 n`!o t`Lm un$Es.~g`x boro `g os is`3$l `4$NB (10,01; 19,9 %) e `4`4B (1&)1; 80,1 %).$/ Ar(B).~e~6r = (10,01\
 `9 19,9 Yb&)1 `9 80,1) / $A ~N,81.~f q1d|Quant$E $[`,&9 `? `Car|`d $[e*k `C `Ce ~L d#'vogadro `? `Car nu$<`5\
 `ni`Z n m m n na|c_fqat.qm*_`Acleo|q1c:#: at`3~Q $9$7 `I ~| ~' `-`T~m`v `d $[`,&9 #c un$E*- `Ce.~+ a ~L de\
 Avogadro `H #S `n`0`Z.`v `? `Car e relacion`--la `; Ar e Mr.`D n, m e N `; $] m / M e *U n `9 NA.$%\
 A*Rsentar resulta~' `; os `o ~ytos.~l\n\
H`- bili`' de `-`T em &M`>r gr`!`5 areia.\n\
YU um a um `, imposs`0~A.~6 qu`0~Q Y?a \"~]s d`Azias\", #p `; ~! d`Azia gig#e: a `Ce.~1a `Ce `g &B `)`6`B\
 `n`0`Z.~6 `? `ca `Ce `, a `? `Car.#o gra#p, `g o ~; ~b `> Mr.~k$% Quant$E $[`,*k, n: Y?a `n`0`Z; un$E SI:\
 `Ce (`C).$% Constant#b Avogadro: NA $F2 `)`6`B `C`(`4.$% NA `, &E`A$<`5 `n`0`Z n~! `Ce.$% #: `Car, M: `? `ca\
 `Ce; un$E g `C`(`4.$% Yh `C`(`4 `g o ~b *X`,ric`5 Mr (ou de Ar).`R`x n`A$<`5 `n`0`Z `, *U n `9 NA.~6 `? #'\
 `d `<Y' `y $] m / M.\n\
Juntan$} *U (m / M) `9 NA.\n\
Diz &Xpr#b `> `n`0`Z falas.\n\
1 `C de H`/O `g 1 `C de `C`,`Z.\n\
Tem *2`,m 2 `C de `-`T de H e 1 `C de `-`T de O.~6o t&4, s`!o 3 `C de `-`T.\n\
#M Yh `C`(`4*- `? `g de $.ar Ye#p.\n\
NA `g 3 `o (&B).`x &? n`!o &{ ter `K algarism*< `> os da~'.\n\
Desde 2019, NA *5 exatame*V &B2 140 76 `)`6`B `C`(`4.`x exame usa o ~b arred*Zdo &B `)`6`B `C`(`4.`W Quant$E\
 $[`,&9 `?|$] m / M|n: `d $[`,*k (`C);m: `? (g);M: `? `Car (g `C`(`4)|$f`k`M pura|$] 3*O4 g / *H g `C`(`4\
 ~}00 `C|c_fqat.qm`W N`A$<`5 `n`0`Z|*U n `9 NA|N: n`A$<`5 `n`0`Z;n: `d $[`,*k (`C);NA: &B `)`6`B `C`(`4|&M`>r\
 tip`5 `n`0$P|~c `C t`Lm $g `)`6`B `n`0`Z|c_fqat.qm`W #: `Car|M = m / n|M: `? `Car (g `C`(`4);m: `? (g);n: `d\
 $[`,*k (`C)|Yh `C`(`4 `g o ~b de Mr|M(CO`/&p 4&11 g `C`(`4YM`W\n\
Pergunta: quantas `C`,`Z e #+ `-`T h`- em 9,0 &P `-~a?`E m &t g; M(H`/O&p *H g `C`(`4.~) $] m / M &t g / *H g\
 `C`(`4 = ~c `C~/ *U n `9 NA = ~c `C `9 &B `)`6`B `C`(`4~C *U $g `)`6`B `C`,`Z$q Cada `C`,$P `g 3 `-`T: 3 `9\
 $g `)`6`B &t `)`6`B&A $g `)`6`B `C`,`Z e 9,0 `)`6`B `-`T.`x &? `g 2 `o, `;#/ `?.`F`%`!o: 9,0 g `, metad#b 18\
 g&W `, meia `Ce.~j~6 `Ce `< &zundo ~' `-`T ~] balan`%a do laborat`3rio.\n\
#:s i~ai$( $f`k`Ms `etes t`Lm n`A$<o$( `n`0`Z `e*m\n\
1 &P H`/ `g ~n `K `C`,`Z do `> 1 &P O`/.~1a `C#b &M`>r $f`k`M `g o ~; n`A$<`5 `n`0`Z.~i~+ NA `H &; de `? a\
 `Ce: `, $u M.`i`>~y #+ `-`T `g ~I `C`,$P.`i#( Yh &s de g `C`(`4.$% Arred*Zr n ced`5`K e ~pder algarismos.$%\
 Dar `K `o do `> os da~'.~h$% n em `C; 1 `C $F2 `)`6`B `n`0`Z.$% $] m / M e *U n `9 NA.$% Yh `C`(`4 `g o ~b\
 de Mr.$% Diz &Xpr#b `> `n`0`Z falas.$% O &? `g os alg. sig. d~Pdo `; ~H.~g$/ n e &E`A$<`5 `C`,`Z em 2$v &P CO`/.\n\
Usa M(CO`/&p 4&11 g `C`(`4.~e\n\
$] 2$v g / 4&11 g `C`(`4 = ~c0 `C.\n\
*U ~c0 `9 &B `)`6`B = $g1 `)`6`B `C`,`Z.~f q1e|Fra`%`!o `Car e &.`%`!&z`-$x|&.&S `Car &.&S ma$x `;&,&S &2 ~S\
 em `?|c_fqat.fr*_`Acleo|q1d:Quant$E $[`,&9 `? `Car|a7e:Percentagens|AE FQ `I ~| ~' `-`T~m`v &.`%`!o `Car e\
 &.`%`!&z`-$x.`D a `;&,`%`!`5 ~! &2.$% Passar ~! &.`%`!#/ ~S.$% Veri~vr `> as &.`%`' `ca &2 $rm 1.~l\n\
N~! &2, ~I `;~[ `g #c \"fatia\".~6 fatia &{ #S `n`0`Z: `, a &.`%`!o `Car.\n\
Tamb`,m &{ #S `?: `, a &.`%`!&z`-$x.~6s #P fatias diferem &_ as `n`0`Z t`Lm `?s `e*m~k$% Fra`%`!o `Car de A:\
 x_A = n_A / n_&<.$% Fra`%`!&z`-ssic~, A: w_A = m_A / m_&<.$% As &.`%`' n`!o t`Lm un$Es.$% Em ~S, *L-se `y\
 $A.$% A $r ~K &.`%`' de to~' os `;~[s `, 1.`R&D a &.`%`!o `Car, to~K as `ds v`Lm em `C.\n\
Se $? `?s, passa-as primeir#/ `C `; $] m / M.&D a &.`%`!&z`-$x, to~K as `?s v`Lm n~5 un$E.`V &) `C de N`/ e\
 $g `C de H`/.\n\
x(H`/&p $g / &1 = 0,75 e x(N`/&p *r.~6s `?s s`!o 28 &P N`/ e 6,1 &P H`/.~6ssim, w(H`/) `, s`3 `] 0,18.`x H`/\
 `g `K `C`,`Z, #p ~H `?.`W Fra`%`!o `Car|x_A = n_A / n_&<|x_A: &.`%`!o `Car de A;n_A: `d de A (`C);n_&<: `d\
 &< (`C)|&2s|1 `C de A em 4 `C: x_A = *r|c_fqat.fr`W Fra`%`!&z`-$x|w_A = m_A / m_&<|w_A: &.`%`!&z`-ssic~,\
 A;m_A: `? de A;m_&<: `? &<, n~5 un$E|&2&x `;postos|20 &P sal em 200 g: w = 0,10|c_fqat.fr`WYdistura: 3*O &P\
 `-~a *s *H g `C`(`4).\n\
Y1 4*O &P #^ *s 4*O8 g `C`(`4).`: &.`%`!o `Car e &.`%`!&z`-$x da `-~a.~) n(`-~a&p 3*O / *H ~}0 `C~/ n(#^&p\
 4*O / 4*O8 = 0,998 `C~C x(`-~a) ~}0 / ($v0 + 0,998&p 0,667$q w(`-~a&p 3*O / (3*O + 4*O&p 0,439&A x(`-~a&p\
 0,667 (66,7 %); w(`-~a&p 0,439 (43,9 %)`F`%`!o: x(#^&p 1 - 0,667 = 0,333~j~6 `-~a `g `K `C`,`Z&W ~R &.`%`!o `Car.\n\
Tem ~H `?&W ~o &.`%`!&z`-$x.~6s `C`,`Z de `-~a s`!o `K leves do `> a$( #^.~6s &.`%`' n`!`5pendem do tamanh~P\
 amostra.~i$% Juntar `?&x `ds no ~; &<.$% Dar un$Es ~]s &.`%`'.~+ x &_ ${nu`Mdo pede w, ou o Y>`-rio.`i`>~y\
 de &a `y $A `H obter %.$% Arred*Zr ced${ as &.`%`' n`!o $rrem 1.~h$% x_A = n_A / n_&<; w_A = m_A / m_&<.$%\
 Sem un$Es; as &.`%`' $rm 1.$% Em %: *L `y $A.$% x e w diferem &_ as `?s `Cares diferem.~g~1 lat`!o `g 70 &P\
 #L e 30 &P zinco.\n\
~z `, a &.`%`!&z`-$x do zinco?~e\n\
w(Zn&p 30 g / (70 g + 30 g&p 0,30, ou seja, 3Y_$p 1|q1e1|\xc1`T n~! amostr~, ferro|c_fqat.qm|q1d~{`M$} #+\
 `-`T h`- em $v `C de ferro?`E n ~} `C; NA $F2 `)`6`B `C`(`4.`: n`A$<`5 `-`T, N.Yd`,to$} *U n `9\
 NA.$L`^`%`!o:~) N ~} `C `9 &B `)`6`B `C`(`4~/ *U 1,204 `)`6`P~C #M 2 `o: *U 1,2 `)`6`P`Q h`- 1,2 `)`6`P `-`T\
 de ferro.`S`%`!o: #P `Ces t`Lm ~9bro ~K `n`0`Z `ca `Ce.`= dar o &? `; 4 algarismos (~Pdo `g 2).$p 2|q1e2|#:\
 at`3~Q $9 do #L|c_fqat.ar|q1c~{`M$} cal$P Ar(Cu) a `nir ~' is`3$l.`E `U`BCu, `? 62,93, $U`k`M 69,15 %.\n\
`U~%Cu, `? 64,93, $U`k`M 30,85 %.`: `? at`3~Q $9 m`,*W.Yd`,to$} Ar = $o (Ar,i `9 %i) / $A.$L`^`%`!o:~) 62,93\
 `9 69,15 = 4351,6~/ 64,93 `9 30,85 = 2003,1~C Ar = (4351,6 *S003,1) / $A = 63,55`Q Ar(Cu&p 63,55.`S`%`!#W ~b\
 ~v `K ~pt`5 63, o is`3topo `K $U#e.`= fazer a m`,*W $W, (62,93 + 64,93) / 2 = 63,93.$p 3|q1e3|\xc1`T de\
 #n`,ni&Eu$!al hidratadoYM|q1d~{`M$} #+ `-`T de #n`,#X h`- em &O0 &P CuSO~d\xb75H`/O?`E Y) &O0 g; NA $F2\
 `)`6`B `C`(`4.`: n`A$<`5 `-`T de O.Yd`,to$} M, depois n, depois `n`0`Z, depois `-`T de O.$L`^`%`!o:~) M =\
 63,55 + 3$v6 + 4 `9 1*O0 + 5 `9 *H = 249,71 g `C`(`4~/ $] &O0 / 249,71 = 0,0200 `C~C Cada un$E `g 4 + 5 = 9\
 `-`T de O.$q n(O&p 9 `9 0,020#I 0,180 `C\n\
5. N(O&p 0,180 `9 &B `)`6`B = &)8 `)`6`B`Q &)8 `)`6`B `-`T de #n`,#X.`S`%`!#! `-gu~, hidrata`%`!o *2`,m `g\
 #n`,ni${ Y?a.`= #S s`3 os 4 O d*vulfato.\n\
"
 return _ns('D', _dz(D))


_F['p_q1'] = _m_p_q1


def _m_p_q2():
 D = "#3#5 5#4 `G ~' `.`' &! `-`T~f q2a|Espetro&x ~-`%`!o `.Y<`,$J|$3 Y?inu`5sY?inu${missao &R&S ~-&S `.Y<e$J ~Wao\
 fre`>`M `;`}`5 *Z e = h f #d lambda f t$.#b chama|c_fqel.~W*_`Acleo|r8e:Luz: $3, reflex`!o, re&.`%`!${\
 le$)$7 `I `G ~' `.`' &! `-`T~m`u $3s Y?`0nuo$( desY?`0nuos (de &@).`u $3$( &Q`!`5 $3$( &R`%`!o.$% Ordenar as\
 regi`' do $3 `.Y<`,tico.`J `+, #]`L`M e `;`}`5 *Z.~+ #6 h f e #d `_ f.~l~6 YK Yinca, *X prisma*-bre-se *X\
 arco-`0ris Y?`0nuo: `, um $3 Y?`0nuo.~6 YK `c g`-s a`>cid*v`3 `g alg~!s cores: `, um espetr`5 &@.\n\
Cada `N `g as suas &@, `;o ~! im*Rss`!o digital. Assi$!e identi~vm `Ns nas $.relas.~k$% Ra*W`%`!o `.Y<`,$J:\
 `+ *^`ytada `y ~W`'.`ipetro Y?`0nuo: to~K as cores (s`3lido incandesce*V).`ipetr`5sY?`0nu*@de &@): s`3\
 alg~!s cores ($T).$% Emiss`!o: &@ colori~K; &R`%`!o: &@ escuras.$% #6 h f, `; h &> `)`(`B`P J s (~L de\
 Planck).$% #d `_ f, `; #d $g0 `)`m $!`(`4 no v`-cuo.`R&5 $@ crescent#b `+ (#b #]`L`M):$% on~K de r`-dio,\
 micro-on~K, in&.&r*@IV);$% *Q`0~A (de `] 700 nm a 400 nm);$% ultravioleta (UV), $is X e $is gama.`x `;`}`5\
 *Z segu#' $@ Y>`-*k.~6 YK *Q`0~A vai do &r*@~H `+) ao violeta (`K `+).&D o ~; `N*-s risca$( &Q`!${ de\
 &R`%`!o $.`!&Eas #9s &,`%`'.`x `-$4 ~V e #K ~W`' `; as #9s `+s.*T t$.#b chama, os `.`' excita~' emi`g YK ao\
 regressar a n`0$K `K baixos.~6 cor da chama identi~v o `N: *v`3dio d`- a#Zelo-alaranjado.`xs liYas ~K regi`'\
 s`!#/proxima~' e ~qm um *6 ~B livros.`W `G `c ~W`!o|#6 h f|E: `+ do ~W`!*@J);h: ~L de Planck, 6,63 `)`(`B`P\
 J s;f: #]`L`M (Hz)|&M`>r ~-`%`!o `.Y<`,$J|*D &O0 `)`4`P Hz: #6 3,32 `)`(`4`l J|c_fqel.~W`W Veloc$E d&0|#d `_\
 f|c: $g0 `)`m $!`(`4 (v`-cuo);`_: `;`}`5 *Z (m);f: #]`L`M (Hz)|~-`%`!&Eo v`-cu*@n#/r, *w i~al)|`_ = 600 nm:\
 *D &O0 `)`4`P Hz|c_fqel.~W`W`E &0 a#Zela d*v`3dio `g `_ = 589 nm.`: #]`L`M e `+ `c ~W`!o.~) `_ = 589 nY)\
 5,89 `)`(~? m~/ *D c / `_ = $g0 `)`m / 5,89 `)`(~? = &O9 `)`4`P Hz~C #6 h *D h c / `_ &> `)`(`B`P `9 $g0\
 `)`m / 5,89 `)`(~? = 3,38 `)`(`4`l J&A *D &O9 `)`4`P Hz e #6 3,38 `)`(`4`l J`F`%`!o: $.`- ~B o &r${ o\
 violeta (*Q`0~A).~j~1 ~W`!`5 UV `g `K `+ do `> u*A YK *Q`0~A. Por ~u o UV &{ dani~vr a pele.~6 `+ `c\
 ~W`!`5pende s`3 da #]`L`M, n`!~P in$?$E d&0.~1&0 `K in$?a `g `K ~W`', n`!o ~W`' `K energ`,tiYg.~i`i`>~y de\
 &; nm `H m (1 nm ~N`(`l m).`b `> ~R `;`}`5 *Z d`- `K `+: d`- ~H.$% &e &Q`!*@&@ claras) `; &R`%`!*@&@\
 escuras).`[ in$?$E d&0 `; `+ de ~I ~W`!o.~+ #d `_ f `; `_ em nm e c em $!`(`4.~h$% Cont`0nuo: to~K as cores;\
 de &@: s`3 alg~!s.$% Emiss`!o: &@ claras; &R`%`!o: &@ escuras.$% `G cresce*V: r`-dio, micro-on~K, IV,\
 *Q`0~A, UV, X, gama.$% #6 h f e #d `_ f.$% Maior #]`L`M: `K `+, ~o `_.~g~1 ~W`!o `g `_ = 400 nm. Cal$P #c `+.~e\n\
*D $g0 `)`m / &10 `)`(~? = 7,50 `)`4`P Hz.\n\
E &> `)`(`B`P `9 7,50 `)`4`P = 4,97 `)`(`4`l J.~f q2b|Quantiza`%`!~P `+ e `-Y9`5 ~2`,#X|quantizaca&Eivei$( `+\
 &N`5 bohr aY9`5 ~2e#X #Rca${xcitaca`5sexcita&S ioniza&S lyman bal$< paschen $.ado\
 fundamental|c_fqel.hid*_`Acleo|q2a:Espetro&x ~-`%`!o `.Y<`,$J$7 `I `G ~' `.`' &! `-`T~m~4 `> a `+ do `.`!o\
 $.`- quantizada.`D a `+ `c n`0~A do `-Y9`5 ~2`,#X.`J #R`%`' `; &Q`!o ou &R`%`!`5 ~W`'.$% Associar as\
 s`,rie$( Lyman, Bal$< e Paschen a regi`' do $3.`D a `+ `j`%`!#/ `nir `c n`0~A.~l\n\
Imagina ~! es~I: s`3 &{s $.ar nu*Agrau, nunca ~B &G.*T `-$4, o `.`!*v`3 &{ ter ~ytas `+s: *:`0$K.&D subir\
 u*Agrau, ~V `+; a`5s~y, #K um ~W`!o.\n\
#Mo o$(graus s`!o fixos, os ~W`' s`3 t`Lm ~ytas `+s: da`0 as &@.~k$% `G quantizada: s`3 &{ ter ~ytos ~bes.$%\
 N`0~A n ($] Y[ 3...): E~U $O `)`(`4`m / n`6 J.`itado fundamental: $] 1 (`+ m`0nima).`ita~' excita~': n #O\
 2.$% `G do ~W`!o: #6 |E ~t - E &3|.$% Ioniza`%`!#W `.`!o vai `H $] \u221e, *I #6 0.`R~6s `+s ~' n`0$K\
 s`!&Eegativas: o `.`!o $.`- `<d#/&E`Acleo.\n\
E&T $O `)`(`4`m J; E`/ = -5,45 `)`(`4`l J; E`f = -2,42 `)`(`4`l J.`xs n`0$K ~vm `K pr`3*3s ~] medida `> n `w.\n\
Desexcita`%`!*@des~y de n`0~A): #K um ~W`!o.\n\
Excita`%`!*@sub#g n`0~A): ~V um ~W`!o `; a `+ exata.\n\
S`,rie$( risca$( &Q`!o, con~:me &E`0~A ~t:$% Lyman: ~t $] 1, no ultravioleta;$% Bal$<: ~t $] 2, no *Q`0~A\
 (#'lgum UV);$% Paschen: ~t $] 3, no in&.&ro.~6 risca &r~, Bal$< vem da #R`%`!o 3 ~7 2.~6 `+ `j`%`!#/ `n#g $]\
 1 `, 2,18 `)`(`4`m J.~1 ~W`!o `; `+ ~B &G n`0$K n`!o `, &Rvido.`W `G `c n`0~A (H)|E~U $O `)`(`4`m / n`6 J|n:\
 n`A$<~9 n`0~A (Y[ 3...);E~U: `+ do `.`!&E&E`0~A n|s`3 `H o `-Y9`5 ~2`,#X|E`/ $O `)`(`4`m / 4 = -5,45\
 `)`(`4`l J|c_fqel.hid`W `G do ~W`!&E~! #R`%`!o|E ~W`!o = \u2223E ~t - E &3\u2223|E ~t, E &3: `+s ~'\
 n`0$K|&Q`!*@desce) ou &R`%`!*@sobe)|3 ~7 2: $g3 `)`(`4`l J|c_fqel.hid`W`E #R`%`!~9 `.`!`5 $] 4 `H $] 2 no\
 ~2`,#X.`: `+ e `;`}`5 *Z do ~W`!${mitido.~) E~d $O `)`(`4`m / 16 = -1,363 `)`(`4`l J~/ E`/ $O `)`(`4`m / 4 =\
 -5,45 `)`(`4`l J~C E ~W`!o = |E`/ - E~d| = &19 `)`(`4`l J$q `_ *d / #6 4,87 `)`(~? Y) 487 nm&A Fot`!`5 &19\
 `)`(`4`l J (487 nm): risca azul-esverdead~, Bal$<.`F`%`!o: &E`0~A ~t `, $] 2 (s`,ri#b Bal$<, *Q`0~A).`x ~b\
 medido `, 486 nm: o &N`5 Bohr a~yta ~n bem.~j~6s &@ provam `> a `+ no `-$4 $.`- quantizada.`x &N`5 Bohr ~O\
 bem o ~2`,#X, #p falha em `-`T `; `K `.`'.\n\
Hoje usa-se o &N~P Y= `.`3$8.~i`i`>~y o &l ~H ~K `+s ~' n`0$K.$% #a `> o `-$4 ~V &M`>r ~W`!o: s`3 o$( `+\
 exata.$% &e &Q`!*@desce) `; &R`%`!*@sobe).~+ a f`3rmul~, E~U `H `-`T `> n`!*v`!o o ~2`,#X.`i`>~y `> #6 0 &8\
 a $] \u221e (`.`!o Y-).~h$% `G quantizada: s`3 ~yt*:`0$K.$% E~U $O `)`(`4`m / n`6 J (~2`,#X).$% Des~y #K;\
 subir ~V: E ~W`!o = |`8E|.$% Lyman (UV), Bal$< (*Q`0~A), Paschen (IV).$% Ioniza`%`!#/ `n#g $] 1: 2,18\
 `)`(`4`m J.~g$/ a `+ do ~W`!${mitid&Ea #R`%`!o $] 3 ~7 $] 1.~e\n\
#6 |E&T - E`f| = 2,18 `)`(`4`m `9 (1 - 1/9&p 1,94 `)`(`4`m J (s`,ri#b Lyman, UV).~f q2c|Espetroscopia\
 ~Wo`.`3$8 e `+ $b`%`!o|$3scopia ~Wo`.o$8 pes `+ $b&S `.oes ni$K $ei$K `+ `j&S&u`Acleo|q2b:Quantiza`%`!~P `+\
 e `-Y9`5 ~2`,#X$7 `I `G ~' `.`' &! `-`T~m`v `+ $b`%`!`5 um `.`!o.$% &f um $3 ~Wo`.`3nico $W.`J *=s `; n`0$K\
 e $e`0vei$( `+.`J a $1 `c *= `; &E`A$<`5 `.`'.~l#7 `-$4 `; ~ns `.`', nem to~' $.`!o i~alme*V *Rsos.`xs `K\
 ~pt~9 n`Acleo *Rcisa*A #| `+ `H sair.~6 $3scopia ~Wo`.`3$8 \"pesa\" essa `+, `.`!#/ `.`!o.~k$% `G $b`%`!o:\
 `+ m`0nima `H retirar um `.`!`5 um `-$4.`ipetroscopia ~Wo`.`3$8: med#'s `+$( remo`%`!o.$% Cada *= &8 a\
 u$!ubn`0~A (1s, 2s, 2p...).$% A $1 do *= `, pro`y$_ a&E`A$<`5 `.`' do $e`0~A.$% `G `j`%`!o: `+ $b`%`!~9\
 `.`!o `K f`-cil de retirar.`R`x n`,on (1s`6 2s`6 2p`U) `g tr`Ls *=s, `; `+s *C~K de:$% 1s: 8&1 MJ `C`(`4 (2\
 `.`');$% 2s: 4,68 MJ `C`(`4 (2 `.`');$% 2p: $v8 MJ `C`(`4 (6 `.`', o *= `K alto).`x s`3dio `g um pic#/ `K,\
 3s*- `] ~c MJ `C`(`4.`x `.`!o 3s d*v`3dio `, o `K f`-cil $bver.`xs *=s agrupaY' `y n`0$K ($] Y[ 3) e,\
 dentr`5stes, `y $e`0$K.`xs `.`' `c ~; $e`0~A t`Lm ~5 `+ $b`%`!o.*T ~; n`0~A, os `.`' p s`!o removi~' `; ~H\
 `+ do `> os s.\n\
Este m`,t&4 confirma a exist`L`M de n`0$K e $e`0$K.`W `G $b`%`!o `y `.`!o|E (J&p E (J `C`(`4) / NA|NA: &B\
 `)`6`B `C`(`4|&; de ~b `y `C#' ~b `y `.`!o|~c MJ `C`(`4 = 8,3 `)`(`4`l J `y `.`!o|c_`;u.sci`W`E *=s `c $3 a\
 104, 6,84, 3,67 e ~c MJ `C`(`4.~6lturas $9s 2 : 2 : 6 : 1.`: identi~vr o `N.~) H`- 4 *=s: $e`0$K 1s, 2s, 2p\
 e 3s.~/ N`A$<`5 `.`': 2 *S + 6 Yb = 11~C Yj 11: `, *v`3dio, Na.$q Configura`%`!o: 1s`6 2s`6 2p`U 3s`4.&A O\
 `N `, *v`3di*@11 `.`').`F`%`!#W pic`5 ~o `+ `, ~c MJ `C`(`4 = #t kJ `C`(`4. Est`- ~pt~P `+ `j`%`!~9 Na (496\
 kJ `C`(`4).~j\n\
#V `K ~pt~9 n`Acleo, `K `+ `, $u `H remover o `.`!o.`xs `.`' `7 s`!o os `K f`-cei$( remover: s`!o os `>\
 `nicipam nas $-`%`'.~i`b `> to~' os `.`' `c `-$4 t`Lm ~5 `+.$% Ler a $1 do *= `;o `+: a `+ $.`- n${ixo\
 Y!`i`>~y `> o *= `K alto `, o $e`0~A `; `K `.`'.`[ `+ $b`%`!o `; `+ d&E`0~A (&l oposto).~h$% `G $b`%`!o: `+\
 `H retirar um `.`!o.$% Um *= `y $e`0~A; $1 pro`y$_ a&E.#w de `.`'.$% Y1 ~pt~9 n`Acleo: ~R `+ $b`%`!o.$% O\
 pic`5 ~o `+ `, a `+ `j`%`!o.~g~1 $3 `g *=$( $1s 2 : 2 : 4. Que `N `,?~e\n\
2 *S + 4 = 8 `.`' (1s`6 2s`6 2p`P): `, o #n`,#X, O.~f q2d|Model~P Y= `.`3$8: n`0$K, $e`0$K, ~@ e spin|Y=\
 `.o$8 ~x ni~A $ei~A spin &N$Mantic*v p d&u`Acleo|q2c:Espetroscopia ~Wo`.`3$8 e `+ $b`%`!o$7 `I `G ~' `.`' &!\
 `-`T~m$% Des#( o &N~P Y= `.`3$8.`v ~x, n`0~A e $e`0~A.$% InY;r quantas ~@ `g ~I $e`0~A.~4 o `> `, *vpin do `.`!o.~l\n\
N`!*vabemos *I $.`- o `.`!#/ ~I inst#e.\n\
Sabemos *I `, `K prov`-~A enY>`--lo.~6 Y= `.`3$8 `, `K densa *I essa probabil$E `, ~R.#> `;o ~! ~Wografia `;\
 `gp`5 ex&,`%`!*x`5 ~! abelha ~] #0 `ca flor.~k$% Orbital: zona *I `, ~n prov`-~A enY>ar o `.`!o.$% Cada ~x\
 `g, n&z`-*3, 2 `.`'.$% N`0~A n: conjunt`5 ~@ `; o ~; n (Y[ 3...).$% Subn`0$K: s (1 ~x), p (3 ~@), d (5\
 ~@).$% O n`0~A n `g n $e`0$K: $] 2 `g 2&x 2p.$% Spin: propriedade do `.`!o `; &G ~bes (#; e #u).`R~6s ~@ s\
 s`!${sf`,ricas.~6s ~@ p t`Lm &G l`3bulo&x s`!o tr`Ls: px, py e pz.`x n`0~A 1 s`3 `g a ~x 1s (m`-xim`5 2\
 `.`').`x n`0~A 2 `g 2&x 2p: 4 ~@ #'t`, 8 `.`'.`x n`0~A 3 `g 3s, 3p e 3d: 9 ~@ #'t`, 18 `.`'.#7 `-$4 `;\
 v`-rios `.`'*- `+ $c d&E`0~A e do $e`0~A.~6 $@ de `+ `, 1s < 2s < 2p < 3s < 3p < 4s < 3d.`xrbitais do ~;\
 $e`0~A t`Lm ~5 `+ (~@ degenera~K).YZ `.`' n~5 ~x t`L$!pins #H`W &6`' `y n`0~A|m`-*3 = 2n`6|n: n`A$<~9\
 n`0~A|~I n`0~A `;pleto|$] 3: 2 `9 9 = 18 `.`'|`W Orbitais `y $e`0~A|s: 1; p: 3; d: 5|~I ~x: n&z`-*3 2\
 `.`'|to~' os `-`T|$e`0~A p: at`, 6 `.`'$R`W`E n`0~A $] 2.`: $e`0$K, ~@ e n`A$<&z`-xim`5 `.`'.~) Subn`0$K:\
 2&x 2p ($] 2 `g 2 $e`0$K).~/ Orbitais: 1 (2s) + 3 (2p&p 4~C &6`': 2 `9 4 = 8&A O n`0~A 2 `g 4 ~@ #'t`, 8\
 `.`'.`F`%`!o: 2n`6 = 2 `9 2`6 = 8.~j`x &N~P Y= `.`3$8 $fituiu as `3rbita$( Bohr.`x `.`!&E`!o ~pcorre ~!\
 *n`3*k: `g ~! probabil$E de $.ar em ~I zona.~i$% Desenhar ~@ `;o `3rbitas cir$Pres.$% YR 3 `.`' n~5 ~x.$% #a\
 `> o $e`0~A p `g 2 ~@: `g 3.`i`>~y `> 4s `g ~H `+ do `> 3d.~h$% Orbital: zon~, probabil$E*-t`, 2 `.`'.$% s:\
 1 ~x; p: 3; d: 5.$% N`0~A n: n $e`0$K*-t`, 2n`6 `.`'.$% Spin: &G ~bes; n~5 ~x, #H~g$w `.`' cabem, n&z`-*3,\
 no $e`0~A 3p?~e\n\
3 ~@ `9 2 = 6 `.`'.~f q2e|Configura`%`!o `.`3$8|~=&S `.o$8 principi~P constru&S aufbau exclusa`5 pauli regr~,\
 hund *Wgram~, caixas `.oe$( *5`M$R*_`Acleo|q2d:Model~P Y= `.`3$8: n`0$K, $e`0$K, ~@ e spin$7 `I `G ~' `.`'\
 &! `-`T~m`i#( ~=`%`' `.`3$8s at`, Yj 20 (at`, 4s).$% Aplicar o YO`0pi~P Constru`%`!o.$% Aplicar o YO`0pi`5\
 Exclus`!`5 Pauli.$% #, Regr~, Hund &! *Wgrama$( caixas.$% *+~vr os `.`' `7.~l\n\
Encher as ~@ `, `;${ncher um pr`,dio: *{ os andare$( baixo.#o ~I quart*@~x) s`3 cabem #P pessoas, vira~K ao\
 Y>`-rio.#o quartos i~ais, ~I pessoa ~v sozinha #e$( `nilhar.~k$% YO`0pi~P Constru`%`!#!s ~@ encheY' `y $@\
 crescent#b `+.$% Ordem: 1s 2s YX 4s.$% Exclus`!`5 Pauli: ~I ~x `g, n&z`-*3, 2 `.`', `; spins #H$% Regr~,\
 Hund: em ~@ `; ~5 `+, *{ um `.`!${m ~I ~!, `; o ~; spin.$% &6`' `7: *< `A~_`0~A.`R\n\
Escreve-se ~I $e`0~A `; &E`A$<`5 `.`' em expoe*V.`V #n`,#X, Yj 8: 1s`6 2s`6 2p`P.*T *Wgram~, caixas, os 4\
 `.`' 2p ~vm: [#;#u][#; ][#; ].\n\
Pela Regr~, Hund, h`- 2 `.`' $6~'.`V $D`-ssio, Yj 19: 1s`6 2s`6 2p`U 3s`6 3p`U 4s`4.`x 4&xnche-s#'$) do 3d,\
 `y`> `g ~H `+.`xs `.`' `7 do $D`-ssio: 1 (o 4s`4).`x `A~_`0~A Y/ o ~p`0o$} $D`-ssi&Eo 4.#w ~p`0&4.*Ts `Os 1\
 e 2, &E`A$<`5 `.`' `7 `, ~9 `O.*Ts `Os 13 a 18, `, &E`A$<~9 `O ~H 10.\n\
I`': Na~X (10 `.`') ~v 1s`6 2s`6 2p`U, `;o &E`,on.`W Orde*A *Renchimento|1s 2s YX 4s (3d 4p)|s: at`, 2\
 `.`';p: at`, 6;d: at`, 10|YO`0pi~P Constru`%`!*@$.ado fundamental)|Yj 12: 1s`6 2s`6 2p`U 3s`6$R`W &6`' `7 e\
 `O|`Os 1-2: n.#w do `O; `Os 13-18: `O - 10|`.`' `7: *< `A~_`0~A|`Ns ~' $Xs &x p|&%, `O 17: 7 `.`' `7$R`W`E\
 f`3s~:o, P, Yj 15.`: ~=`%`!o, *Wgram~, caixa&x val`L`M.~) 15 `.`': 1s`6 2s`6 2p`U 3s`6 3p`B ($r: 2 *S + 6 *S\
 + 3 = 15)~/ 3p`B *q Regr~, Hund: [#; ][#; ][#; ] (3 $6~')~C \xda~_`0~A $] 3: 3s`6 3p`B&W 5 `.`' `7.$q\
 Per`0&4 3, `O 5 Yb#I 15.&A P: 1s`6 2s`6 2p`U 3s`6 3p`B; 5 `.`' `7.`F`%`!#W `O 15 `g 5 `.`' `7.~j~6 ~=`%`!o\
 `.`3$8 ~O a &,`%`!&Ea &L ~pi`3Y;.`xs `.`' `7 ~Om as ~D qu`0~Qs.\n\
Element*< ~; `O t`Lm ~=`%`' `7 &Xelha$).~i$% Encher 3d #e$( 4s.$% YR &G `.`' n~! ~x p #e$( ocupar as outras\
 (viola Hund).$% YR os &G `.`' d~5 ~x `; o ~; spin (viola Pauli).$% YU `;o val`L`M `.`' de n`0$K\
 i*Vriores.`i`>~y de $rr os `.`' `H confir#Z Z.~h$% Ordem: 1s 2s YX 4s.$% Pauli: m`-xim`5 2 `y ~x, spins #H$%\
 Hund: um `y ~x #e$( emparelhar.$% Val`L`M: `.`' do `A~_`0~A.$% \xda~_`0~A = ~p`0&4.~g\n\
Escrev#' ~=`%`!o `.`3$8 d${nxofre, S (Yj 16).~e\n\
1s`6 2s`6 2p`U 3s`6 3p`P (2 *S + 6 *S + 4 = 16 `.`'; 6 `7).$p 1|q2e1|`G `c ~W`!`5 YK &ra|c_fqel.~W|q2a~{`M$}\
 um laser &r${Ya YK `; `_ = 650 nm.$/ a `+ `c ~W`!o.`E `_ = 650 nY) 6,50 `)`(~? m; h &> `)`(`B`P J s; #d $g0\
 `)`m $!`(`4.Yd`,to$} *D c / `_ #bpois #6 h f.$L`^`%`!o:~) *D $g0 `)`m / 6,50 `)`(~? = 4,62 `)`4`P Hz~/ E &>\
 `)`(`B`P `9 4,62 `)`4`P = $g6 `)`(`4`l J`Q ~I ~W`!o `g $g6 `)`(`4`l J.`S`%`!o: `, pouca `+; um laser #K ~ns\
 ~W`' `y segundo.`= #x `_ em nan`3$,s na f`3&/.$p 2|q2e2|Risc~, Bal$< do ~2`,#X|c_fqel.hid|q2b~{`M$} cal$P o\
 `;`}`5 *Z da risca emitida na #R`%`!o 3 ~7 2.`E E~U $O `)`(`4`m / n`6 J.Yd`,to$} `e`%~, `+&x `_ *d /\
 E.$L`^`%`!o:~) E`f $O `)`(`4`m / 9 = -2,42 `)`(`4`l J~/ E`/ $O `)`(`4`m / 4 = -5,45 `)`(`4`l J~C E ~W`!o =\
 E`f - E`/ = $g3 `)`(`4`l J$q `_ &> `)`(`B`P `9 $g0 `)`m / $g3 `)`(`4`l = 6,56 `)`(~? m`Q `_ ~> 656 nm*-\
 risca &r~, Bal$<.`S`%`!#W ~b medido `, 656 nm; o &N`5 Bohr a~yta bem no ~2`,#X.`= fazer E`/ - E`f e obter `+\
 negativa `H o ~W`!o.$p 3|q2e3|`G `H ionizar ~! `C#b `-`T de ~2`,#X|c_fqel.hid|q2b~{`M$} `> `+ `, $u `H\
 ionizar &)0 `C de `-`T de H no $.#Q\n\
E &M o ~R `;`}`5 *Z `c ~W`!o capaz `jr um `-$4?`E E&T $O `)`(`4`m J; NA $F2 `)`6`B `C`(`4.$L`^`%`!o:~) Por\
 `-$4: #6 0 - E&T = 2,18 `)`(`4`m J~/ Por `Ce: 2,18 `)`(`4`m `9 &B `)`6`B = 1,31 `)`U J `C`(`4~C `_ m`-*3 *d\
 / E &> `)`(`B`P `9 $g0 `)`m / 2,18 `)`(`4`m = 9,12 `)`(`m m`Q 1,31 `)`U J (1312 kJ) `y `Ce; `_ m`-xim`5 91,2\
 nm (UV).`S`%`!o: ~W`' `; `_ ~R n`!o t`Lm `+ `H ionizar o `-$4.`= es`>~y `> a `+ ~t do `.`!o Y- `, 0.\n\
"
 return _ns('D', _dz(D))


_F['p_q2'] = _m_p_q2


def _m_p_q3():
 D = "#3#5 3#4 $5`3Y;~f q3a|Hist`3&9 *7`%`!~P $5`3Y;|&L ~pioY; histo*k mendeleiev moseley dobereiner newlands `O\
 ~pi&4 $X *7&S$R*_`Acleo|q2e:Configura`%`!o `.`3$8$7 `I $5`3Y;~m$% Referir Y>ibutos hist`3riYg `H a $5`3Y;.~4\
 a *7`%`!${m `Os, ~p`0o~' e $Xs.`J a &,`%`!`5 um `N `; #c ~=`%`!o `.`3$8.$% Loca&^r um `N a `n#g Z.~l*T\
 s`,culo XIX conheciaY' `] 60 `N&x procurava-se ~! $@.\n\
&' arrumou-os `;o cartas `c jogo, `y ~D pareci~K.\n\
Deixou lugares vazios `H `Ns ainda `y descobrir. A~ytou!~k$% Grupo: coluna (1 a 18); `Ns `; ~5 ~=`%`!`5\
 val`L`M.$% Per`0o$} linha (1 a 7); i~al a&E`A$<~9 `A~_`0~A `; `.`'.$% Bloco: $e`0~A `> $.`- a encher (s, p,\
 d ou f).$% Hoje os `Ns $.`!o ordena~' `y n`A$<#%`3mico, Z.`R\n\
Contributos hist`3riYg:$% D\xf6bereiner (1829): tr`0a~K de `Ns &Xelha$).$% Newlands (1864): lei ~K oitavas.$%\
 &' (1869): $@ da `? at`3~Q, `; lacuna&x *R*Q`'.$% Previu ${ka-sil`0cio, descobert`5pois: o germ`k#X.$%\
 Moseley (1913): a $@ ~yta `, a d&E`A$<#%`3mico.`xrganiza`%`!#/ `nir ~K ~=`%`':$% $X s: `Os 1 e 2;$% $X p:\
 `Os 13 a 18;$% $X d: `Os 3 a 12;$% $X f: lantan`0deo&x actin`0deos.`x h`,li*@1s`6) ~v no `O 18, `; os $T\
 *z.`V Al, 1s`6 2s`6 2p`U 3s`6 3p`4: ~p`0&4 3 e $X p, `O 13.`W Per`0&4|~p`0&4 = n do `A~_`0~A|n:\
 n`A$<$M`kntico principal do `A~_`0~A ocupado|$.ado fundamental|Al (3s`6 3p`4): ~p`0&4 3$R`W Grup*@$Xs &x\
 p)|$X s: `O = `.`' `7; $X p: `O = `.`' `7 Yb0|`.`' `7: *< `A~_`0~A|`Ns re*Rsentativos (exceto He)|S (3s`6\
 3p`P): 6 Yb#I 16$R`W`E `N `; Yj 19.`: ~p`0&4, `O e $X.~) Configura`%`!o: 1s`6 2s`6 2p`U 3s`6 3p`U 4s`4 ($r\
 19)~/ \xda~_`0~A: $] 4&W ~p`0&4 4.~C Val`L`M: 4s`4, 1 `.`!o, $X s, `O 1.&A Per`0&4 4, `O 1, $X s: `, o\
 $D`-ssio, K.`F`%`!#Ws ~J #C&! (`O 1) t`Lm um `.`!*v `7.~j~6 $5`3Y; resume #| in~:ma`%`!#! &,`%`!o *Rv`L ~D.\n\
&' mostrou o ~b `c bom &No: fez *R*Q`' `> se confir#Zam.~i`b `> a &L atual $.`- ordenada *q `? at`3~Q: `, `y\
 Z.$% YU o grup`5 um `N do $X p se$!o#Z 10.`[ ~p`0&4 (linha) `; `O (coluna).$% YR o h`,li&Eo `O 2 `y ter 2\
 `.`' `7.~h$% Grupos: colunas (1-18); ~p`0o~': linhas (1-7).$% Ordem atual: n`A$<#%`3mic*@Moseley).$% BloYg\
 s, p, d e f: $e`0~A em *Renchimento.$% Per`0&4 = `A~_`0~A ocupado.$% &' *Rviu `Ns `y descobrir.~g#o `>\
 ~p`0&4, `O e $X $.`- o `N `; ~=`%`!o 1s`6 2s`6 2p~%?~e\n\
\xda~_`0~A $] 2: ~p`0&4 2. Val`L`M 2s`6 2p~% = 7 `.`', $X p, `O 7 Yb#I 17 (`, o fl`Aor).~f q3b|Rai#%`3mic${\
 `+ `j`%`!o|$i aY9ico `+ `j&S #Ae`Ms ~piodic$E ~M #q blindagem `O ~pi&4&u`Acleo|q3a:Hist`3&9 *7`%`!~P\
 $5`3Y;$7 `I $5`3Y;~m`v $i at`3mic${ `+ `j`%`!o.$% *( ~q`%`!~9 $i at`3mic&Eum `O e *X ~p`0&4.$% *( ~q`%`!~P\
 `+ `j`%`!&Eum `O e *X ~p`0&4.`J as #P #A`L`Ms.~l`xs `.`' `7 s`!o puxa~' pel&E`Acle${ afasta~' #Bs outros `.`'.\n\
Y1 n`0$K afastam a val`L`M: o `-$4 cresce.\n\
Y1 &=`' no ~; n`0~A puxam `K: o `-$4 encolhe.\n\
#V `K pe`>no, `K dif`0cil `, arrancar um `.`!o.~k$% Rai#%`3mico: medida do tamanh~9 `-$4 #m pm).$% `G\
 `j`%`!o: `+ m`0nima `H remover um `.`!~9 `-$4 isolad&Eo $.ado fundamental.$% Exprime-se em kJ `C`(`4 (ou em\
 J `y `-$4).$% No ~p`0o$} o $i ~E #' `+ `j`%`!o `w.$% No `O: o $i `w #' `+ `j`%`!o ~E.`R~6*x`5 um ~p`0&4, os\
 `.`' `7 ~vm no ~; n`0~A.~6 ~M #q `w&W os `.`' s`!o `K YI`0~'.&5 ~u o $i ~E #' `+ `j`%`!o `w.~6`5s~y um `O,\
 h`- `K um n`0~A ocupado.`xs `.`' `7 ~vm `K longe e `K blinda~'.&5 ~u o $i `w #' `+ `j`%`!o ~E.$+s ($i\
 cal$Pdo, em pm): Li 167, Na 190, K 243.*T ~p`0&4 3: Na 190, Mg 145, Al 118, Cl 79.\n\
`Gs `j`%`!*@kJ `C`(`4): Li 520, Na 496, K 419.*T ~p`0&4 2: Li 520, C 1086, F 1681, Ne 2081.\n\
H`- pe`>na&xxce`%`' (`y exemplo, B < Be e O < N).`xs $T *z t`Lm as ~Res `+s `j`%`!`5 ~I ~p`0&4.`xs ~be$( $i\
 mudam con~:me &z`,t&4; as #A`L`Ms s`!#/s #9s.`W `G `j`%`!o `y `-$4|E (J&p E (kJ `C`(`4) `)*P NA|NA: &B\
 `)`6`B `C`(`4|&; de `Ce `H `-$4|Na: 496 kJ `C`(`4 = 8,24 `)`(`4`l J|c_`;u.sci`W Tend`L`Ms|~p`0&4 ~7: $i #u,\
 EI #;; `O #u: $i #;, EI #u|$i: $i at`3mico;EI: `+ `j`%`!o|`Ns re*Rsentativos (h`- exce`%`' *9uais)|Na > Mg\
 ($i); Mg < Cl (EI)|`W`E `+s `j`%`!~9 Na e do K: 496 e 419 kJ `C`(`4.`: `;`Hr e ~Or.~) Diferen`%a: 496 - 419\
 = 77 kJ `C`(`4~/ Por `-Y9`5 K: 419 `)*P &B `)`6`B = 6,96 `)`(`4`l J~C O K `g `K um n`0~A (4s) do `> o Na\
 (3s).$q O `.`!o 4s $.`- `K longe d&E`Acle${ `K blindado.&A O K ~pde o `.`!`5 val`L`M `; `K facil$E.`F`%`!o:\
 K $.`- abaix~9 Na no `O 1: EI ~o, `;o *R*Qto.~j~6 `+ `j`%`!o baixa ~O a ~s ~' ~J #C&!.`x $D`-ssio $-ge `; a\
 `-gu~, ~:ma `K violenta do `> *v`3dio.~i$% #a `> o $i `w no ~p`0&4 `y haver `K `.`'.`b `> `K `.`'\
 torna$!em*R o `-$4 ~R.$% Inverter as #A`L`Ms da `+ `j`%`!o.`i`>~y o \"*.\" e o \"$.ado fundamental\"\
 n~,fini`%`!o.$% #M`Hr `N$( `O&x ~p`0o~' `etes &X cuidado.~h$% Per`0&4 (~7): $i ~E, EI `w.$% Grup*@#u): $i\
 `w, EI ~E.$% Causa no ~p`0o$} ~M #q ~R, ~; n`0~A.$% Causa no `O: `K n`0$K, `K blindagem.$% EI em kJ `C`(`4;\
 `y `-$4 *g `y NA.~g`xrdena `y $@ crescent#b $i at`3mico: Mg, Na, Cl.~e\n\
Est`!&Eo ~p`0&4 3: o $i ~E a*x~9 ~p`0&4.`xrdem cresce*V: Cl < Mg < Na (79, 145 e 190 pm, ~bes cal$P~').~f\
 q3c|Y(`%`!`5 i`' e ~D ~' `Ns|ioes YCa#/niao ~J nao ~J ~J #C&! #Cnoterrosos *1eYG $T *z $fa`M elementar ~s\
 ~D&u`Acleo|q3b:Rai#%`3mic${ `+ `j`%`!o$7 `I $5`3Y;~m$% *( ~M ~' i`' ~' `Ns ~' `Os Y[ 16 e 17.`J a facil$E de\
 ~:#Z i`' `; a `+ `j`%`!o.$% Des#( ~D ~' ~J #C&!, #Cnoterrosos, *1`,neo&x $T *z.`u element`5 $f`k`M\
 elementar.~l`xs `-`T ~vm `K $.`-$K `; a ~=`%`!`5 um g`-s nobre.`xs ~J chegam l`- ~pdendo `.`'; *:`!o ~J,\
 ganhando.`xs $T *z j`- l`- $.`!o: *w n`!o $-gem.~k$% Metais #Aem a ~:#Z YC`' (i`' &,tivos).$% N`!o ~J #Aem a\
 ~:#Z ani`' (i`' negativos).$% Grupo 1: X~X; `O 2: X`6~X; `O 16: X`6`(; `O 17: X`(.$% Elemento: tip`5 `-$4\
 (~; Z).$% Subst`k`M elementar: $f`k`M ~:mada s`3 `y um `N (Na, O`/, O`f).`R`xs ~J #C&! (`O 1) s`!o `Ce&x ~n\
 $-*l$Lagem `; a `-~a: ~:mam um hidr`3xid${ ~2`,#X.`V 2 Na *S H`/O ~7 2 NaOH + H`/.~6 ~s `w a`5s~y o `O (EI\
 ~E).`xs #Cnoterrosos (`O 2) s`!o ~H $-tiv*< `> os #C&!.`xs *1`,YG (`O 17) ~:mam `C`,`Z *Wt`3~Qs: F`/, Cl`/,\
 Br`/, I`/.\n\
\xc0 `2 ambie*V: F`/ e Cl`/ gasosos, Br`/ l`0quido, I`/ s`3lido.~6 ~s ~' *1`,YG ~E a`5s~y o `O.`xs $T *z (`O\
 18) exis`g `;o `-`T isola~' e s`!o *6 $-*l`x ~; `N &{ ~:#Z $f`k`Ms `etes: O`/ e O`f (~r).`xs ~J Y@zem bem a\
 `X el`,&y e o &k; *:`!o ~J, em geral, n`!o.`W Carga ~' i`' (`Os Y[ 16, 17)|`O 1: +1; `O 2: +2; `O 16: -2; `O\
 17: -1|~M: `.`' ~pdi~' (+) ou ganhos (-)|`Ns re*Rsentativo$(stes `Os|Mg`6~X e S`6`($R`W`E magn`,si*@Yj 12) e\
 &% (Yj 17).`: *Rver os i`' #' f`3&/ do `;posto.~) Mg: 1s`6 2s`6 2p`U 3s`6; ~pde 2 `.`': Mg`6~X (`;o\
 &E`,on).~/ Cl: 1s`6 2s`6 2p`U 3s`6 3p~%; ganha 1 `.`!o: Cl`( (`;o o `-rgon).~C Neutral$E: 1 `9 (+2) *S `9\
 (-1&p 0&A O `;posto `, MgCl`/.`F`%`!o: Mg`6~X `g 12 - 2 ~N `.`', `;o &E`,on.~j~6 #A`L`M `H ~:#Z i`' vem da\
 `+ `j`%`!${ da ~=`%`!o.\n\
*( ~M ~' i`' ~pYa es#( f`3&/$( `;postos i`3niYg.~i`b `> os ~J ganham `.`'.`i#( Cl &s de Cl`/ `H o &%\
 gasoso.`[ o `N #n`,#X `; a $f`k`M O`/.$% #a `> a ~s ~' *1`,YG `w no `O.~h$% Metais: YC`'; n`!o ~J: ani`'.$%\
 Grupo 1: X~X; 2: X`6~X; 16: X`6`(; 17: X`(.$% Alcali&!: ~s `w no `O.$% Halog`,YG: *Wt`3miYg; ~s ~E no `O.$%\
 Gases *z: ~n *6 $-*l~g&( i`!o ~:ma ${nxofre (`O 16) e `; #+ `.`' ~v?~e\n\
Ganha 2 `.`': S`6`(, `; 16 *S = 18 `.`' (`;o o `-rgon).$p 1|q3e1|Posi`%`!`5 um `N a `n#g Z$R|q3a~{`M$} Y/ o\
 ~p`0&4, o `O e o bloc~9 `N `; Yj 13.`E Yj 13.Yd`,to$} es#( a ~=`%`!${ ler o `A~_`0~A.$L`^`%`!o:~) 1s`6 2s`6\
 2p`U 3s`6 3p`4 (2 *S + 6 *S Yb = 13)~/ \xda~_`0~A $] 3: ~p`0&4 3.~C Val`L`M: 3s`6 3p`4, 3 `.`', $X p.$q\
 Grupo: 3 Yb#I 13.`Q ~p`0&4 3, `O 13, $X p (alum`0#X).`= dizer `O 3 (falta $rr 10 no $X p).$p 2|q3e2|#M`Hr\
 $is at`3miYg||q3b~{`M$} ordena Na, Mg e K `y $i at`3mic${ `;`H K `; Na.\n\
Da~' ($i cal$Pdo): Na 190 pm, Mg 145 pm, K 243 pm.Yd`,to$} #x as #A`L`M&x confir#Z `; os da~'.$L`^`%`!o:~) Na\
 e Mg: ~; ~p`0&4; Mg `g `K ~M #q&W `, ~o.~/ Na e K: ~; `O; K `g `K um n`0~A&W `, ~R.~C Ordem: Mg < Na < K.$q\
 K / Na = 243 / 19#I 1,28`Q o rai~9 K `, `] 1,28 &g ~9 Na.`S`%`!#Ws da~' confirmam as #A`L`Ms *R*Qtas.`=\
 `;`Hr s`3 pel&E`A$<`5 `.`'.$p 3|q3e3|Fot`!o capaz `jr *v`3dio|c_fqel.~W|q3b~{`M$} &M o ~R `_ `c ~W`!o `>\
 ioniza um `-Y9`5 s`3dio?`E EI(Na&p 496 kJ `C`(`4; NA $F2 `)`6`B `C`(`4; h &> `)`(`B`P J s; #d $g0 `)`m\
 $!`(`4.$L`^`%`!o:~) Por `-$4: #6 496 `)`B / &B `)`6`B = 8,24 `)`(`4`l J~/ `_ *d / E &> `)`(`B`P `9 $g0 `)`m\
 / 8,24 `)`(`4`l = 2,41 `)`(~? m`Q `_ m`-xim`5 241 nm (ultravioleta).`S`%`!o: &0 *Q`0~A (400 a 700 nm) n`!o\
 ioniza *v`3dio.`= #x a `+ `y `Ce `;o `+ `c ~W`!o.\n\
"
 return _ns('D', _dz(D))


_F['p_q3'] = _m_p_q3


def _m_p_q4():
 D = "#3#5 6#4 $h`%`!$M`0~Q~f q4a|$h`%`!$M`0~Q: $.abil$E, `+ e `;`}o|`<ca$Mi~Q $.abil$E `+ de `<&S `;`}`5 `<&S `+\
 $De`Ml `<&S $W &h tripla|c_fqlg.dh*_`Acleo|q3c:Y(`%`!`5 i`' e ~D ~' `Ns;r9d:\xc1`T, distribui`%`!o `.`3$8 e\
 `<`%`!$M`0~Q$7 `I $h`%`!$M`0~Q~m~4 `y`> os `-`T se `<m.$% &f a curva da `+ em fun`%`!~P dist`k`M ~B `-`T.`v\
 `+ de `<`%`!${ `;`}`5 `<`%`!o.$% #M`Hr `<`%`' $W, &h&x triplas.~lYZ `-`T `<Y' &_ juntos ~vm `; ~H `+ do `>\
 se`H~'.#> `;o #P bolas *X *5: ~vm ond#' `+ `, m`0nima.\n\
Se s#'fastam*- `+ sobe; se s#'proxima*A`K, *:`Acleos repeleY'.~k$% $h`%`!$M`0~Q: &? ~K YI`%`' e repuls`' ~B\
 n`Acleo&x `.`'.$% #M`}`5 `<`%`!o: dist`k`M ~B *:`Acle*:a `+ m`0nima.$% `G de `<`%`!o: `+ `H `>*E a\
 `<`%`!*@`y `Ce, em kJ `C`(`4).$% Que*E `<`%`' ~V `+; ~:#Z `<`%`' &| `+.$% Y1 `.`' `nilha~': `<`%`!o `K curta\
 e `K ~:te.`R\n\
Na `C`,cul~, H`/*- `+ `, m`0nima a 74 pm.#> $u 436 kJ `H `>*E as `<`%`' de 1 `C de H`/.`x ~b 436 kJ `C`(`4 `,\
 a `+ de `<`%`!o H-H.~6 curv~, `+ `g tr`Ls zonas:$% longe: os `-`T *w n`!o &ogem (`+ ~pt`5 0);$% n&z`0nimo:\
 `<`%`!o $.`-~A;$% ~n ~pt#! repuls`!o ~B n`Acleos faz a `+ subir ~n.\n\
$h`%`' ~B *'&!:$% C-C ($W): 154 pm e 348 kJ `C`(`4;$% C=C (&h): 134 pm e 614 kJ `C`(`4;$% C$nC (tripla): 120\
 pm e 839 kJ `C`(`4.~1a `<`%`!o &h `, `K ~:te, #p n`!o `, ~9br~P $W.`W `G `H `>*E `<`%`'|#6 n `9\
 E(`<`%`!o)|n: `d de `<`%`' (`C);E(`<`%`!o): `+ de `<`%`!*@kJ `C`(`4)|~bes m`,dios ~K &Ls|$v `C de H-H: $v `9\
 436 = 872 kJ|c_fqlg.dh`W Orde*A ~:`%a|C-C < C=C < C$nC|`K ~. `nilha~': `K ~:te e `K curta|`<`%`' ~B os ~;s\
 `-`T|C$nC: 839 kJ `C`(`4 e 120 pm|`W`E `+ de `<`%`!o H-H = 436 kJ `C`(`4.`: `+ `H `>*E as `<`%`' em &1 &P\
 H`/.~) M(H`/) ~}2 g `C`(`4~/ $] &1 / $v2 = 1,98 `C~C #6 1,98 `9 436 = 8,6 `)`6 kJ&A S`!o $us `] 8,6 `)`6\
 kJ.`x &? `g 2 alg. sig., `;#/ `?.`F`%`!o: 2 `C da*k 872 kJ; 1,98 `C d`- um *6 ~H.~j~6s `<`%`' ~ardam `+: `,\
 `y ~u `> as $-`%`' qu`0~Qs $Vm `+.~6 `+ de `<`%`!&zed#' $.abil$E: `<`%`' `K ~:tes s`!o `K dif`0cei$(\
 `>*E.~i$% #a `> ~:#Z ~! `<`%`!o Y4 `+: &|.`b `> a `<`%`!o &h `g ~9br~P `+ da $W.`[ `;`}`5 `<`%`!o `; o\
 tamanh~P `C`,$P.`i`>~y `> a `+ de `<`%`!o `, `y `Ce.~h$% $h`%`!o: $.ad`5 `+ m`0nima.$% #M`}o: dist`k`M ~B\
 n`Acle*:&z`0nimo.$% `G de `<`%`!o: `H `>*E 1 `C de `<`%`'.$% Que*E ~V; ~:#Z &|.$% Simples < &h < tripla\
 (~:`%a); `;`}#/o Y>`-rio.~g`xrdena as `<`%`' C-C, C=C e C$nC `y `;`}o cresce*V.~e\n\
C$nC (120 pm) < C=C (134 pm) < C-C (154 pm).~f q4b|$h`%`' $=, i`3$8 e met`-lica|`<&S $= io$8 $|ica `nilh~,\
 `.oes ioes rede cristalina #Z de `.oes `.$m$E&u`Acleo|q4a:$h`%`!$M`0~Q: $.abil$E, `+ e `;`}o$7 `I\
 $h`%`!$M`0~Q~m`u `<`%`!o $=, i`3$8 e met`-lica.`J o tip`5 `<`%`!o `; os `N&xnvolvi~'.~4 ~D de ~J #b `;postos\
 i`3niYg.~+ a `.$m$E `H *Rver a $'$E da `<`%`!o.~l`xs `-`T &{m `nilhar `.`', troc`--los ou p\xf4-lo&xm\
 `;um.YZ n`!o ~J `nilham: $=.~1 $| d`- `.`' a um n`!o $|: i`3$8.Yduitos `-`T de $| p\xf5em `.`' *X \"#Z\"\
 `;um: met`-lica.~k$% Co*5*V: `nilh~, ~. de `.`' (~B n`!o ~J).$% I`3$8: YI`%`!o ~B YC`' #'ni`' ($| e n`!o\
 $|).$% Met`-lica: YC`' n~! nuve*A `.`' desloca&^~'.$% &6$m$E: #A`L`M `c `-$4 `H YIir os `.`' da `<`%`!o.$%\
 $h`%`!o $= $': ~B `-`T de `.$m$E `ete.`R\n\
H`/O, CO`/ e CH~d s`!o $f`k`Ms `; `<`%`' co*5$).`x NaCl `, i`3nico: ~:ma ~! red#b i`' Na~X e Cl`(\
 alterna~'.`xs `;postos i`3niYg s`!*v`3li~' ~] `2 ambie*V.\n\
Fundi~' ou em `^`%`!o, Y@zem a `X el`,&y.*Ts ~J, os `.`' desloca&^~' ~Om a boa Y@`%`!${l`,&y e t`,r~Q.\n\
Tamb`,m ~Om o brilh${ a facil$E d#b~:#Z &X `nir.\n\
&6$m$E (escal~, Pauling): F &1; O 3,4; N $g; C 2,6; H 2,2.\n\
H-H `, $= a$'; H-Cl `, $= $' (o Cl YIi `K).\n\
#V ~R a `e`%~, `.$m$E, `K $' a `<`%`!o.~6 `.$m$E `w no ~p`0od${ ~E no `O.`W Tip`5 `<`%`!o|n`!o $| + n`!o $|:\
 $=; $| + n`!o $|: i`3$8; $| + $|: met`-lica|$|: #A#' ~pder `.`';n`!o $|: #A#' ganhar ou `nilhar|regra geral\
 (h`- casos i*Vrm`,dios)|NaCl: i`3$8; Cl`/: $=; Cu: met`-lica|`W`E $f`k`Ms HCl, KBr e Fe.`: tip`5 `<`%`!`5 ~I\
 ~!.~) HCl: H e Cl s`!&E`!o ~J: $= $'.~/ KBr: K `, $| (`O 1) e Br `, n`!o $|: i`3$8.~C Fe: s`3 `-`T de $|:\
 met`-lica.&A HCl $=; KBr i`3$8; Fe met`-lica.`F`%`!o: no KBr, K~X `g 18 `.`' e Br`( `g 36.~j`x tip`5 `<`%`!o\
 ~O as ~D ~K $f`k`Ms.`xs ~J s`!o bons &Kes; os s`3li~' i`3nic*:`!o, #p as suas `^`%`' sim.~i$% #a `> no NaCl\
 h`- `C`,`Z: h`- ~! red#b i`'.`b `> a `<`%`!o $= `, s`3 ~B `-`T i~ais.`[ `<`%`!&zet`-lica `; i`3$8.$%\
 Inverter a #A`L`M da `.$m$E.~h$% Co*5*V: `nilha (n`!o ~J).$% I`3$8: YC`' #'ni`' ($| e n`!o $|).$% Met`-lica:\
 `.`' desloca&^~'.$% &6$m$E `ete: `<`%`!o $'.$% F `, o `N `K `.$mo.~g&( tip`5 `<`%`!${xiste no `3xid`5\
 magn`,sio, MgO?~eYdg `, $| e O `, n`!o $|: `<`%`!o i`3$8 (i`' Mg`6~X e O`6`(*-mbos `; 10 `.`').~f\
 q4c|Nota`%`!`5 Lewi&x #E octeto|*oca`5 lewis #E octeto ~. `<$) ~. nao `<$) `.oe$( *5`M ~:mul~,\
 $.rutura*a*_`Acleo|q4b:$h`%`' $=, i`3$8 e met`-lica$7 `I $h`%`!$M`0~Q~m$% Re*Rsentar `-`T e `C`,`Z na\
 *o`%`!`5 Lewis.$% #, #E octeto.$% YU ~. `<$) e ~. n`!o `<$).$% *+~vr `<`%`' $W, &h&x triplas.~l\n\
Na *o`%`!`5 Lewis s`3 s#bsenham os `.`' `7.`xs `-`T `nilham `.`' at`, ~I um ~vr `; 8 ~] #0, `;o um g`-s\
 nobre.`x ~2`,#X `, exce`%`!o: ~v `; 2, `;o o h`,lio.~k$% S`0mbol`5 Lewis: s`0mbol$M`0mico `; os `.`' `7\
 (*9os).$% Regra do octeto: ~I `-$4 #A#' ~vr `; 8 `.`' `7 (H `; 2).$% Par `<*V: par `nilhad*@tra`%o ~B\
 `-`T).$% Par n`!o `<*V: par s`3 `c `-$4.$% $h`%`!o $W: 1 par; &h: 2 ~.; tripla: 3 ~..`RYd`,t&4 `H ~!\
 `C`,$P:~) Soma os `.`' `7 de to~' os `-`T.~/ Divide `y 2: `, &E`A$<`5 ~..~C $h os `-`T `; ~. $W.$q #Mpleta\
 os octetos `; ~. n`!o `<$).\n\
5. Se faltarem `.`', faz `<`%`' &hs ou triplas.$+ H`/O: 2 `9 1 + 6 = 8 `.`', 4 ~..\n\
2 ~. `<$) (O-H) e 2 n`!o `<$) no O.$+ N`/: 2 `9 5 ~N `.`', 5 ~.: N$nN e 1 YE`!o `<*V em ~I N.$+ CO`/: 4 *S `9\
 6 = 16, 8 ~.: O=C=O e 2 ~. em ~I O.$+ NH`f: 5 + 3 = 8, 4 ~.: 3 `<$) e 1 n`!o `<*V no N.`W Pare$( `.`' `7|~.\
 = ($o `.`' `7) / 2|`.`' `7: `O (1-2) ou `O - 10 (13-18)|`C`,`Z $2as|CO`/: (4 *S `9 6) / 2 = 8 ~.*a`W`E\
 `C`,cul~, *!~d.`: *o`%`!`5 Lewis.~) &6`' `7: 4 + 4 `9 1 = 8~/ Pares: 8 / 2 = 4~C O C `<-s#' ~I H `; um par:\
 4 `<`%`' $W C-H.$q Pares n`!o `<$): 4 - 4 = 0&A CH~d: 4 ~. `<$), 0 n`!o `<$); o C ~v `; octeto.`F`%`!o: ~I H\
 ~v `; 2 `.`' e o C `; 8.~j~6 *o`%`!`5 Lewis *Rv`L `;o os `-`T se `<m e `, o *{ passo `H a Y3*k.`xs ~. n`!o\
 `<$) *2`,m YP espa`%${ afetam a ~:ma da `C`,$P.~i$% YU to~' os `.`' e n`!*v`3 os `7.`i`>~y os ~. n`!o\
 `<$).$% Dar 8 `.`' ao ~2`,#X: s`3 `g 2.$% YR `<`%`' $W no N`/ (`, tripla).$% So#Z mal: o O `g 6 `.`' `7.~h$%\
 Lewis: s`3 `.`' `7.$% Octeto: 8 `.`' (H: 2).$% Pares = `.`' `7 / 2.$% Simples, &h e tripla: 1, 2 e 3 ~..$%\
 N`!${s`>~y os ~. n`!o `<$).~g$w ~. de `.`' `7 `g a `C`,cul~, O`/ e `> `<`%`!o h`- ~B os O?~e\n\
2 `9 6 = 12 `.`': 6 ~.. $h`%`!o &h O=O e 2 ~. n`!o `<$) em ~I O.~f q4d|Geomet&9 $'$E ~K `C`,`Z|Y3*k `Ce$Pr Y,\
 angular *; trigonal tetraedrica t*kngular plana angul`5 `<&S $'$E `Ce$P $' a$'*a*_`Acleo|q4c:Nota`%`!`5\
 Lewi&x #E octeto$7 `I $h`%`!$M`0~Q~m$% *( Y3ri~, `C`,`Z $W.$% InY;r `k#z$( `<`%`!`5 `C`,`Z do programa.`u\
 `<`%`!o $' de `C`,$P $'.$% Prever se ~! `C`,$P `, $' ou a$'.~l`xs ~. de `.`' repeleY': afastaY' o `K poss`0~A.\n\
Iss`5fin#' ~:ma da `C`,$P.~1a `C`,$P `, $' s#'s ~Ms parciais n`!$k anulam, `;o um `0man.~k$% Linear: 180`h\
 (CO`/, HCN) ou s`3 &G `-`T (H`/, HCl).$% Angular: H`/O (104,5`h).$% Piramidal trigonal: NH`f (107`h).$%\
 Tetra`,drica: CH~d (109,5`h).$% T*kngular plana: CH`/O e ~I C d${ten*@120`h).$% Mol`,$P $': h`- ~!\
 se`H`%`!`5 ~Ms `> n`!$k anula.`R`xs ~. n`!o `<$) repelem `K do `> os `<$).&5 ~u o `kngul&Ea H`/O (104,5`h)\
 `, ~o do `> no CH~d (109,5`h).`x NH`f `g 1 YE`!o `<*V: 107`h.\n\
Polar$E `ca `C`,$P:$% #P `<`%`' $'es i~ai&xm linha anulaY' (CO`/ `, a$');$% n~! `C`,$P angular n`!$k anulam\
 (H`/O `, $').`x CH~d e o CCl~d s`!#/$'es: a ~:ma tetra`,drica `, sim`,&y.`x HCl `, $': s`3 h`- ~! `<`%`!o, e\
 `, $'.~6s `C`,`Z de &G `-`T i~ais (H`/, O`/, N`/) s`!#/$'es.~6 $'$E ~O ~D `;#/ `^bil$E.`W Geomet&9 ~.|2 `Os:\
 Y,; 3: t*kngular plana; 4: tetra`,drica, *; ou angular|`Os: `<`%`' e ~. n`!o `<$) ~] #0 do `-$4\
 central|`C`,`Z do programa|NH`f: 4 `Os, 1 n`!o `<*V: *;*a`W`E `C`,`Z CO`/ e H`/O.`: Y3&9 $'$E de ~I ~!.~)\
 CO`/: O=C=O, &X ~. n`!o `<$) no C: Y,, 180`h.~/ As #P `<`%`' C=O s`!o $'es, #p opostas: anulaY'.~C H`/O: 2\
 `<`%`' e 2 ~. n`!o `<$) no O: angular, 104,5`h.$q As #P `<`%`' O-H n`!$k anulam.&A CO`/ a$' (Y,); H`/O $'\
 (angular).`F`%`!o: na H`/O h`- 2 *S = 4 `Os ~] #0 do O.~j~6 ~:ma ~O a `e`%a: a `-~a `, $' e o di`3xid`5 &:\
 n`!o.&5 ~u a `-~a d~ulve sal e o CO`/ `, *6 sol`A~A em `-~a.~i$% #a `> a H`/O `, Y,.`b `> `<`%`' $'es\
 d`!$km*R `C`,`Z $'es.`i`>~y os ~. n`!o `<$) ao *Rver a ~:ma.$% &e os `k#zs do NH`f (107`h) e da H`/O\
 (104,5`h).~h$% Pares repeleY' #'fastaY'.$% CO`/ Y,; H`/O angular; NH`f *;; CH~d tetra`,drica.$% \xc2#zs:\
 180`h, 104,5`h, 107`h, 109,5`h.$% Polar: as ~Ms parciais n`!$k anulam.$% Mol`,`Z sim`,&ys s`!#/$'es.~g~6\
 `C`,cul~, NH`f `, $' ou a$'? Porqu`L?~e\n\
Polar: a ~:ma *; trigonal (107`h) n`!#/nula as 3 `<`%`' N-H $'es.~f q4e|Hidro*'neto&x `O&w|hidro*'netos\
 alca&! alce&! alci&! nomenclatura `O&w alcool aldeido cetona a#iilic#/mina ~:mula\
 qui~Q&u`Acleo|q4c:Nota`%`!`5 Lewi&x #E octeto$7 `I $h`%`!$M`0~Q~m`u alca&!*-lce&! #'lci&!.$% Dar nom#'\
 hidro*'netos $W (at`, 4 *'&!).$% Reconhe~y os `O&w do programa.$% Associar &Eome `c `;post#/$ku `O\
 fun$_.~l`xs hidro*'netos s`!o YF$( &: `; ~2`,#X ~] #0.\n\
&e um H `y outro grup`5 `-`T muda as ~D: `, o `O fun$_.#> `;o p\xf4r ~! pe`%a `ete *X brin`>d`5 encaixe.~k$%\
 Hidro*'neto: s`3 C e H.$% Alcano: s`3 `<`%`' $W, C~UH`/~U\u208a`/ (metano, etano, propano, butano).$%\
 Alceno: ~! `<`%`!o &h C=C, C~UH`/~U (eteno, propeno).$% Al#No: ~! `<`%`!o tripla C$nC, C~UH`/~U\u208b`/\
 (etino).$% Prefixos: met (1 C), et (2), prop (3), but (4).`R\n\
Grupo&w do programa:$% `-lcool: -OH (#^, CH`fCH`/OH; termina`%`!o -ol);$% alde`0$} -CHO, no fim da YF\
 (etanal, CH`fCHO; -al);$% cetona: C=O n&zei~P YF (propanona, CH`fCOCH`f; -ona);$% `-#i`0lico: -COOH\
 (`-cid${tanoico, CH`fCOOH; -oico);$% amina: -NH`/ (metilamina, CH`fNH`/).$+$( f`3&/s:$% metano CH~d, etano\
 C`/H*j, propano C`fHYL, butano C~dH&T\u2080;$% eteno C`/H~d, propeno C`fH*j;$% etino C`/H`/.`x #^ e o\
 `-cid${tanoico t`Lm 2 *'&!; &Eome Y/-*@et-).`W F`3&/s gerais|alcano C~UH`/~U\u208a`/; alceno C~UH`/~U; al#No\
 C~UH`/~U\u208b`/|n: n`A$<`5 `-`T de &:|YFs abertas `; ~! s`3 `<`%`!&z`Altipla|$] 3: propano C`fHYLYM`W`E\
 hidro*'net`5 YF aberta `; 4 C e ~! `<`%`!o &h.`: fam`0lia, f`3&/ e `? `Car.~) $h`%`!o &h C=C: `, um\
 alcen*@but-: 4 C), buteno.~/ F`3&/ C~UH`/~U: C~dHYL.~C M = 4 `9 1$v1 + 8 `9 &)1 = 56,12 g `C`(`4&A Buteno,\
 C~dHYL, M = 56,12 g `C`(`4.`F`%`!o: #/lcano `; 4 C (C~dH&T\u2080) `g `K 2 H.~j`x `O fun$_ decide o\
 `;`ytament$M`0mico. Um `-lcool e um `-#i`0lic*v`!o ~n `etes, ~; `; o ~; n`A$<`5 *'&!.~i`[ alde`0d*@no fim da\
 YF) `; cetona (n&zeio).`i`>~y o H na f`3&/ geral d#/lcano: C~UH`/~U\u208a`/.$% Cha#Z \"propanol\" a um\
 `;post`5 2 *'&!.$% YS `> os `O&w s`!o hidro*'netos.~h$% Alca&!: $W; alce&!: &h; alci&!: tripla.$% met, et,\
 prop, but: Y[ 3, 4 *'&!.$% -OH `-lcool; -CHO alde`0do; C=O cetona.$% -COOH `-#i`0lico; -NH`/ amina.~g\n\
~z `, a f`3&/ `Ce$Pr do propan${ #+ ~2`,#Xs `g?~e~6lcano `; $] 3: C`fHYL, `; 2 `9 3 *S = 8 ~2`,#Xs.~f\
 q4f|I*Vra`%`' i*Vr`Ce$Pres, `^bil$E e #}$E|&ocoes i*Vr`Ce$Pres ~:ca$( london dis~psao dipolo dipolo `<coe$(\
 ~2e#X `^bil$E #}$E *9`5 ebuli&S&u`Acleo|q4d:Geomet&9 $'$E ~K `C`,`Z$7 `I $h`%`!$M`0~Q~m`u `<`%`' qu`0~Q$(\
 &o`%`' i*Vr`Ce$Pres.$% *+~vr &o`%`' de *M, dipolo-dipol${ `<`%`' de ~2`,#X.`J as &o`%`' `; o *9`5\
 ebuli`%`!o.$% Prever `^bil$E e #}$E.~l~6s `C`,`Z YIeY' ~!s ~]s outras, #p ~n ~H do `> os `-`T dentr`5las.\n\
Essas YI`%`' decide$!e ~! $f`k`M `, g`-s, l`0quido ou s`3lido.\n\
\"Semelh#e d~ulve &Xelh#e\": `-~a `; `-~a, `3leo `; `3leo.~k$% I*Vra`%`' i*Vr`Ce$Pres: YI`%`' ~B `C`,`Z (`K\
 &.cas do `> as `<`%`').$% *M (dis~ps`!o): exis`g ~B to~K as `C`,`Z.$% Dipolo-dipolo: ~B `C`,`Z $'es.$%\
 $h`%`!`5 ~2`,#X: H `<d#/ N, O ou F YI`0do #B N, O ou F de outra `C`,$P.$% Misc`0$K: l`0qui~' `> se &2m em\
 &M`>r pro`y`%`!o.`R\n\
I*Vra`%`' `K ~:tes d`!o *9o$( ebuli`%`!o `K altos.~6 `-~a ferv#' $A `hC; o H`/S, de `? ~R, ferv#' `] -60\
 `hC.~6 `e`%a vem ~K `<`%`' de ~2`,ni&Ea `-~a.~6s &o`%`' de *M crescem `; o tamanh~P `C`,$P.*Ts *1`,YG: F`/ e\
 Cl`/ s`!o $T, Br`/ `, l`0quido, I`/ `, s`3lido.\n\
Solubil$E e #}$E:$% `-~a e #^ s`!&zisc`0$K (`<`%`' de ~2`,#X ~B ambos);$% `-~a e hexan&E`!*v`!&zisc`0$K (o Yc\
 `, a$');$% o i&4*-$', d~ulve-se melhor em hexan~9 `> em `-~a.`x sal d~ulve-se na `-~a `y`> os i`'\
 s`!#%ra`0~' *qs `C`,`Z $'es.`W Regra da `^bil$E|&Xelh#e d~ulve &Xelh#e|$' `; $' (ou i`3nico); a$' `;\
 a$'|regra &Mitativa|#^ e `-~a: misc`0$K|`W`E H`/O *s *H g `C`(`4) e H`/S *s 3&19 g `C`(`4).`: ~Or `y`> a\
 `-~a `g *9`5 ebuli`%`!o `K alto.~) A H`/S `g `] 1,89 &g a `? `Car da `-~a.~/ S`3 `y *M*- H`/S deve*k ferver\
 `K alto.~C A `-~a `g `<`%`' de ~2`,#X (H `<d#/ O).$q Essas &o`%`' s`!o ~n `K ~:*m&A A `-~a ferv#' $A `hC #'\
 H`/S a `] -60 `hC.`F`%`!#! `e`%a `, de `] 160 `hC.~j~6s `<`%`' de ~2`,#X ~Om #|s ~D da `-~a, `;o *y\
 flutuar.~6 #}$E `, usada `H se`Hr e extrair $f`k`Ms.~i$% #a `> ferver a `-~a `>Yi `<`%`' O-H: se`H `C`,`Z.`b\
 `> h`- `<`%`' de ~2`,ni${m &M`>r `C`,$P `; H.`i`>~y as &o`%`' de *M nas `C`,`Z $'es.`[ sol`A~A `;\
 misc`0~A.~h$% I*Vr`Ce$Pres: `K &.cas do `> as `<`%`'.$% *M: to~K; dipolo-dipolo: $'es.$% $h`%`!`5 ~2`,#X:\
 H-N, H-O, H-F.$% Y1 &o`%`': ~R *9`5 ebuli`%`!o.$% Semelh#e d~ulve &Xelh#e.~g`x #^ #' `-~a s`!&zisc`0$K. Que\
 &o`%`' ~Om ~u?~e\n\
$h`%`' de ~2`,#X ~B o -OH d${tanol #' `-~a (*2`,m *M e dipolo-dipolo).$p 1|q4e1|Pare$( `.`'\
 n#/mon`0aco*a|q4c~{`M$} re*Rsenta o NH`f na *o`%`!`5 Lewis.`E N `g 5 `.`' `7 e H `g 1.Yd`,to$} #S `.`', ~:#Z\
 ~. e `;pletar octetos.$L`^`%`!o:~) &6`' `7: 5 + 3 `9 1 = 8~/ Pares: 8 / 2 = 4~C Tr`Ls ~. `<$) N-H.$q SoYi 4\
 - 3 = 1 YE`!o `<*V no N.`Q 3 `<`%`' $W e 1 YE`!o `<*V n#/zoto.`S`%`!#W YE`!o `<*V faz a `C`,$P *;.`= es`>~y\
 o YE`!o `<*V.$p 2|q4e2|`G ~K `<`%`' `ca amostr~, etino|c_fqlg.dh|q4a~{`M$} `> `+ `, $u `H `>*E as `<`%`'\
 C$nC em 1$g &P etino, C`/H`/?`E E(C$nC&p 839 kJ `C`(`4; M(C`/H`/&p 2*O4 g `C`(`4.Yd`,to$} `d $[`,&9 `+ `y\
 `Ce.$L`^`%`!o:~) $] 1$g / 2*O4 = 0,499 `C~/ Cada `C`,$P `g 1 `<`%`!o C$nC: 0,499 `C de `<`%`'.~C #6 0,499 `9\
 839 = 419 kJ`Q `] 419 kJ.`S`%`!#!s `<`%`' triplas s`!o ~n ~:*m`= #x a `+ da `<`%`!o $W C-C.$p 3|q4e3|Lewis,\
 Y3&9 $'$E do CO`/*a|q4d~{`M$} ~O `y`> o CO`/ `, a$'*-pesar de ter `<`%`' $'es.`E C `g 4 `.`' `7 e O `g\
 6.$L`^`%`!o:~) &6`' `7: 4 *S `9 6 = 16, ou seja, 8 ~..~/ O=C=O usa 4 ~.; soYim 4 ~. n`!o `<$) (2 em ~I O).~C\
 O C n`!o `g ~. n`!o `<$): a `C`,$P `, Y, (180`h).$q Cada C=O `, $', #p as #P a*9am e$!enti~' #H`Q as $'$Es\
 anulaY': o CO`/ `, a$'.`S`%`!#! Y3ri~,cid#' $'$E da `C`,$P.`= concluir \"$'\" s`3 `y haver `<`%`' $'es.\n\
"
 return _ns('D', _dz(D))


_F['p_q4'] = _m_p_q4


def _m_p_q5():
 D = "#3#5 5#4 $j~ps`'~f q5a|#j Avogadro, `p `Car e `? vol`Amic~, $T|lei d#'vogadro `p `Car ptn `? volumic~,ns$E $T\
 condicoes nor`K de *Rssa${ `2*b*_`Acleo|q1d:Quant$E $[`,&9 `? `Car$7 `I $j~ps`'~m$% Enu`Mr a #j Avogadro.~+\
 o `p `Car `c g`-&xm PTN.`J `p, `d $[`,&9 `? `c g`-s.`D a `? vol`A~Q `c g`-&xm PTN.~l#7 g`-s as `C`,`Z $.`!o\
 ~n afasta~K ~!s ~K outras.`x `p $c de quantas `C`,`Z h`-, n`!~9 tip`5 `C`,$P.YZ bal`' i~ais, um `; h`,li${\
 outro `; ar, nas #9s condi`%`', t`Lm o ~; n`A$<`5 `C`,`Z.~k$% #j Avogadro: `ps i~ai$( $T `etes, ~] #9\
 *Rss`!${ `2, t`Lm o ~; n`A$<`5 `n`0`Z.$% Volume `Car, Vm: `p de 1 `C de g`-s.$% PTN: 0 `hC e 1 atm; VY) #l\
 dm`B `C`(`4.$% V = n `9 Vm.$% #: vol`A~Q: ~G = m / V; `H um g`-&xm PTN, ~G = M / Vm.`R`x `p `Car $c da\
 *Rss`!${ da `2, n`!~9 g`-s.~6 25 `hC e 1 atm, Vm `, `] 24,5 dm`B `C`(`4.#o PTN, 1 `C de O`/, de N`/ ou de\
 CO`/ ocupa #l dm`B.~6 `? vol`A~Q `c g`-s `, pro`y$_ ~] sua `? `Car.`V ~G(CO`/&p 4&11 / #l *G dm`(`B em\
 PTN.`x ar seco `g ~G ~> 1,29 g dm`(`B em PTN (M ~> 28,97 g `C`(`4).\n\
Gases `; M ~R do `> a d#/r acumulaY' em baix*@CO`/).\n\
Gases `; M ~o sobem (He, H`/).`xs `p$( $T n~5 *Rss`!${ `2 $rY' `;#/s `ds.`W Volume `c g`-s|V = n `9 Vm|V: `p\
 (dm`B);n: `d (`C);Vm: #l dm`B `C`(`4 em PTN|$T em PTN|~c `C: V = 11,2 dm`B*b`W #: vol`A~Q `c g`-s|~G = M /\
 Vm|~G: `? vol`A~Q (g dm`(`B);M: `? `Car (g `C`(`4);Vm: `p `Car (dm`B `C`(`4)|g`-s nas condi`%`' de Vm|O`/ em\
 PTN: 3$v0 / #l = 1,43 g dm`(`B*b`W`E 8,80 &P CO`/ em PTN; M(CO`/&p 4&11 g `C`(`4.`: `p e `? vol`A~Q.~) $]\
 8,80 / 4&11 = &q0 `C~/ V = &q0 `9 #l = 4,48 dm`B~C ~G = 4&11 / #l *G dm`(`B&A V = 4,48 dm`B; ~G *G\
 dm`(`B.`F`%`!o: ~G = m / V = 8,80 / 4,48 *G dm`(`B.~j~6 #j Avogadro ~pYa #S `C`,`Z de g`-s medindo `ps.#> `y\
 ~u `> o CO`/, `K dens~9 `> #/r, s#'cumula em cave&x po`%os.~i~+ #l dm`B `C`(`4 ~:a ~K condi`%`' PTN.~+ Vm `H\
 l`0qui~' ou s`3li~'.`i`>~y de &; a `? a `C #e$( #x Vm.`[ `? vol`A~Q (g dm`(`B) `; `? `Car (g `C`(`4).~h$%\
 Avogadro: ~;s P e T, ~; V, ~; n.#w de `n`0`Z.$% PTN: VY) #l dm`B `C`(`4.$% V = n `9 Vm; ~G = M / Vm.$% Gases\
 `K pesa~' `> #/r: M > 29 g `C`(`4.~g&( `p YP 3,2 &P O`/ em PTN? *s 3$v0 g `C`(`4)~e\n\
$] 3,2 / 3$v#I 0,10 `C; V = 0,10 `9 #l = 2,2 dm`B.~f q5b|#M&,`%`!~P troposfera e *0$)|troposfera atmosfera\
 `;&,ca~9 ar azoto #neni#/rgon dioxid`5 &: *0$) monoxid`5 &: oxi~' d#'zoto dioxid`5 enxofre ~r\
 `ni`Z&u`Acleo|q5a:#j Avogadro, `p `Car e `? vol`Amic~, $T$7 `I $j~ps`'~m$% InY;r a `;&,`%`!#/proximada d#/r\
 seco.$% Exprimir a `;&,`%`!${m ~S e em *8.$% *+~vr os principais *0$) #'s suas origens.`J *0$) `;\
 efeit*:#/mbie*V e na sa`Ade.~l`x ar `, ~! mistur~, $T `> respiramos &X pensar.\n\
Quase 4 em ~I 5 `C`,`Z s`!`5 azoto.~6lguns $T, ~; em `ds m`0ni#p, fazem mal: s`!o os *0$).~k$% Troposfera:\
 *]a da atmosfera junto ~] su~pf`0cie (at`, `] 12 km).$% Ar seco #m `p): N`/ 78 %, O`/ 21 %, Ar 0,9 %, CO`/\
 `] 0,04 %.$% Para $T, % em `p = &.`%`!o `Car `)0.$% Polue*V: $f`k`M `>, n~! ~yta `z`%`!o, faz mal aos seres\
 vivos ou a#/mbie*V.$% *8: `nes `y milh`!*@1 *8 ~N`(`P %).`R`x va`y de `-~a ~q muit`5 lugar `H lugar; `y ~u\
 fala-se d#'r seco.`x CO`/ anda #Bs 420 *8 (da~' de 2023 e 2024) e $.`- a `wr.\n\
YOipais *0$) e origens:$% CO: `;bust`' in`;pletas (motores, lareiras);$% NO e NO`/ (NO*i): motores a altas\
 `2s;$% SO`/: `>im~, `;bust`0$K `; enxofre, vulc`';$% O`f troposf`,rico: ~:ma-s#' `n#g NO*i `; YK solar;$%\
 `n`0`Z finas (PM10, PM2,5): fumo&x poeiras.\n\
Efeitos: proble#p respirat`3rios, chuvas `-ci~K (SO`/, NO*i) e smog.`x CO `, ~pigoso `y`> se `< ~]\
 hemoglobina d*vangue.`x ~r `, bom na $.&c (filtra UV) e mau na troposfera.`W *8 e ~S|*8 = &.`%`!o `)`U; % =\
 &.`%`!o `)0|&.`%`!o: em `p ($T) ou em `?|1 % ~N 000 *8|CO`/ a 420 *8 = 0,042 %|c_fqso.~p`W`E #/r seco `g\
 0,93 % de `-rgon em `p.`: &.`%`!o `Car, *8 e `p de `-rgon em 50,0 dm`B d#'r.~) x(Ar&p 0,93 / $A = 0,0093~/\
 Em *8: 0,0093 `)`U = 9300 *8~C V(Ar&p 0,0093 `9 50,#I 0,465 dm`B ~> 0,47 dm`B&A x = 0,0093 (9300 *8); 0,47\
 dm`B de `-rgon.`F`%`!o: 0,465 / 50,0 `)#I 0,93 %.~j\n\
Pe`>nas ~pcentagens &{$!er im`yta$): o CO`/ `, s`3 0,04 % d#/r, #p `g #[ efeit&Eo clima.Ydedir em *8 torna\
 *:`A$<os pe`>&! `K f`-cei$( ler.~i`b `> o #n`,#X `, o g`-s `K $U#e: `, #/zoto.`[ *8 `; ~S (1 % ~N 000 *8).$%\
 YS `> o ~r `, &X*R bom.`i`>~y `> a `;&,`%`!o `, d#/r seco.~h$% Ar seco: N`/ 78 %, O`/ 21 %, Ar 0,9 %, CO`/\
 0,04 %.$% Gases: % em `p = &.`%`!o `Car `)0.$% 1 *8 ~N`(`P %.$% Polue$): CO, NO*i, SO`/, O`f, `n`0`Z.$%\
 Chuva `-cida: SO`/ e NO*i.~g\n\
Exprime 0,042 % de CO`/ em *8.~e\n\
0,042 % = 0,00042 = 420 *8.~f q5c|Solu`%`', $a&x $t`'|dis~psoes `^coes $as $toe&xfeit`5 tyndall `^to #1 #v ~K\
 `ni`Z &2 homogenea heterogenea&u`Acleo|r7b:Mate*kis: $f`k`Ms, &2&x `? vol`A~Q$7 `I $j~ps`'~m`u `^`%`', $a&x\
 $t`'.`J ~I tipo `; o #v ~K `n`0`Z dis~psas.$% Des#( ${feit`5 Y0$% Dar exempl*< *W a *W.~lYdistura sal em\
 `-~a: de*e Mistura areia: vai ao fundo.`x leite ~v ~B os &G: n`!#/ssenta, #p *2`,m n`!o `, *^pare*V.`x #v ~K\
 `n`0`Z faz a `e`%a.~k$% Dis~ps`!o: &2 `ca $f`k`M (dis~pso) noutra (dis~ps#e).$% Solu`%`!o: `n`0`Z ~oes do `>\
 1 nm; homog`,nea; n`!$kdimenta.$% Coloide: `n`0`Z ~B 1 nm e $A0 nm; parece homog`,neo; dis~psa &0.$%\
 Suspens`!o: `n`0`Z ~Res do `> $A0 nm; heterog`,nea; sedimenta.$% Efeit`5 Tyndall: dis~ps`!`5 um feix#b YK `y um $a.`R\n\
N~! `^`%`!o, o `^to $.`- dis~ps&Eo #1 #m geral, o `> existe em ~R `d).$+$( `^`%`': `-~a salgada*-r,\
 lat`!*@`^`%`!*v`3lida).$+$( $as: leite, maionese, nevoeiro, gelatina, sangue.$+$( $t`': `-~a `; areia, sumo\
 `; polpa.~1 feix#b laser YIvessa ~! `^`%`!$k$!e ver.#7 $a, o feixe v`L-se: `, ${feit`5 Y0~6s $t`' se`HY' `y\
 decanta`%`!o ou filtra`%`!o.~6s `^`%`' n`!$k se`Hm `y filtra`%`!o.`W Tamanho ~K `n`0`Z|`^`%`!o < 1 nm < $a <\
 $A0 nm < $t`!o|nm: nan`3$, (10`(`l m)|liYas *C~'|o leite `, um $a|`W`E tr`Ls &2s: A (passa o filtro, feixe\
 in*Q`0~A); B (passa o filtro, feixe *Q`0~A); C (~v no filtro).`: classi~vr.~) A: `^`%`!*@`n`0`Z < 1 nm).~/\
 B: $a (efeit`5 Tyndall).~C C: $t`!*@`n`0`Z > $A0 nm).&A A `^`%`!o, B $a, C $t`!o.`F`%`!o: $A0 nY) &) `)`(`U\
 m (1 \xb5m).~j`x efeit`5 Tyndall ~O os $i$( sol *Q`0$K *X nevoeiro ou n~! sala `; p`3.Yduitos alimento&x\
 meY;mentos s`!o $as.~i`b `> to~K as &2s homog`,neas ~] *Qta s`!o `^`%`'.$% #a `> um $a sedimenta `; o\
 `gpo.`[ `^t*@dis~pso) `; #1.`i`>~y as `^`%`' s`3li~K e gasosas.~h$% Solu`%`!o < 1 nm; $a 1 a $A0 nm; $t`!o >\
 $A0 nm.$% Coloide: efeit`5 Y0$% Suspens`!o: sedimenta e filtra-se.$% Solu`%`' &{$!er s`3li~K, l`0qui~K ou\
 gasosas.~g`x nevoeiro dis~psa &0 ~' far`3is. Que tip`5 dis~ps`!o `,?~e#> um $a (got`0`Z de 1 a $A0 nm n#/r):\
 ${feit`5 Tyndall mostra-o.~f q5d|#M&,`%`!$Mantitativ~, `^`%`'|`z&S `z&S ma$x ~S em `? ~S em `p *8 &.&S `Car\
 `^to #1 `^&S `C dm3|c_fqso.con*_`Acleo|q5c:Solu`%`', $a&x $t`'|a7e:Percentagens|AE FQ `I $j~ps`'~m`D a\
 `z`%`!*@`C dm`(`B) `ca `^`%`!o.`D a `z`%`!&z`-$x (g dm`(`B).`D ~pcentagen&xm `? e em `p e *8.`J `z`%`!${\
 `z`%`!&z`-$x.`D a `? de `^t#/ pesar `H *R`Hr ~! `^`%`!o.~l~1a colher d#'`%`Acar *X copo ou *X jarr#W sabor\
 muda.~6 `z`%`!o diz Y^ `^to h`- em ~I litr`5 `^`%`!o.\n\
Pode #S-se em `Ces, Ye#p ou em ~S.~k$% #U`%`!o: #d n / V (`C dm`(`B), V `, o `p da `^`%`!o.$% #U`%`!&z`-$x:\
 $^ m / V (g dm`(`B).$% % (m/m&p m `^to / m `^`%`!o `)0.$% % (V/V&p V `^to / V `^`%`!o `)0.$% *8 = m `^to / m\
 `^`%`!o `)`U (1 *8 = 1 mg kg`(`4).$% $^ c `9 M.`R`x V `, &X*R o `p da `^`%`!o, n`!o ~9 #1.\n\
Passa os `ps a dm`B: 250 mL = */ dm`B.&D *R`Hr ~! `^`%`!`5 `z`%`!o conhecida:~) cal$P $] c `9 V;~/ cal$P Y) n\
 `9 M;~C pesa o `^to, d~ulve-${ `;pleta o bal`!o volum`,trico.`V 250 *? NaCl 0,$A `C dm`(`B: $] 0,0250 `C e\
 Y) 1,46 g.~6s ~pcentagens `;`Hm ~5 #[za: `? `; `?, `p `; `p.`x *8 usa-se `H `z`%`' ~n pe`>nas, `;o *0$) na\
 `-~a.`W #U`%`!o|#d n / V|c: `z`%`!*@`C dm`(`B);n: `d de `^t*@`C);V: `p da `^`%`!*@dm`B)|`^`%`'|0,10 `C em\
 ~c0 dm`B: #d &q `C dm`(`B|c_fqso.con`W #U`%`!&z`-$x|$^ m / V|c\u2098: `z`%`!&z`-$x (g dm`(`B);m: `? de\
 `^t*@g);V: `p da `^`%`!*@dm`B)|`^`%`'|&O g em */ dm`B: $^ 20 g dm`(`B|c_fqso.con`W Percentagem em `?|%\
 (m/m&p m `^to / m `^`%`!o `)0|m: `?s n~5 un$E|`? da `^`%`!o = `^to + #1|20 g em 200 g: 10 %|c_fqso.~p`W`E\
 2,92 &P NaCl em #t *? `^`%`!o; M(NaCl&p 58,44 g `C`(`4.`: `z`%`!${ `z`%`!&z`-$x.~) $] 2,92 / 58,44 = 0,0#t\
 `C~/ V = #t mL = ~c0 dm`B~C #d 0,0#t / ~c#I 0,$A `C dm`(`B$q $^ 2,92 / ~c#I 5,84 g dm`(`B&A #d 0,$A `C\
 dm`(`B; $^ 5,84 g dm`(`B.`F`%`!o: $^ c `9 M = 0,$A `9 58,44 = 5,84 g dm`(`B.~j~6 `z`%`!o ~pYa medir `d$(\
 `^to `; ~! pipeta &s `ca balan`%a.\n\
R`3tulo$( bebi~K usam % (V/V) `H o `-lcool.~i~+ o `p do #1 &s do `p da `^`%`!o.`i`>~y de &; mL `H dm`B.$%\
 So#Z s`3 a `? do `^t&Ea `? da `^`%`!o.`[ c (`C dm`(`B) `; c\u2098 (g dm`(`B).~h$% #d n / V; $^ m / V; $^ c\
 `9 M.$% % (m/m), % (V/V) e *8: #9 #[za em cima e em baixo.$% V da `^`%`!${m dm`B.$% Pre`Hr: $] c V, Y) n\
 M.~g&( `? de gliYge *s 180,2 g `C`(`4) `, $u `H $A *? `^`%`!o &q0 `C dm`(`B?~e\n\
$] &q0 `9 0,$A = 0,0200 `C; Y) 0,0200 `9 180,2 = 3,60 g.~f q5e|Dilui`%`!`5 `^`%`'|&-&S &b &-&S `^&S mae `^&S\
 &-da pipeta balao `ptrico ci vi cf vf|c_fqso.dil*_`Acleo|q5d:#M&,`%`!$Mantitativ~, `^`%`'|a9c:Pro`y$_$E\
 inversa|AE FQ `I $j~ps`'~m~4 o `> `, &-r ~! `^`%`!o.~+ ci `9 #. `9 Vf.`D o &b &-`%`!o.$% Des#( `;o *R`Hr ~!\
 `^`%`!o dilu`0da.~l\n\
Juntar `-~a a u$!umo `zd&E`!&zuda a `d de sumo, s`3 o `p.\n\
Na &-`%`!#/ `d de `^to ~v i~al; a `z`%`!o ~E.~k$% Diluir: juntar #1; a `d de `^t&E`!&zuda.$% ni = nf&W ci `9\
 #. `9 Vf.$% Fator de &-`%`!o: *D Vf / Vi = ci / cf.$% f `, ~R do `> 1 e n`!o `g un$Es.`R`V `ca `^`%`!o ~c0\
 `C dm`(`B *R`Hr $A *? 0,$A `C dm`(`B.\n\
#. `9 Vf / ci = 0,$A `)0 / ~c#I 20,0 mL.\n\
f ~N0 / 20,#I &O0: a `^`%`!o ~v 5 &g `K dilu`0da.\n\
Procedimento:~) medir Vi `; ~! pipeta volum`,&y;~/ &; `H um bal`!o volum`,tric`5 `p Vf;~C `;pletar `; `-~a\
 at`, ao tra`%${ homogeneizar.`xs &G `ps &{m $.ar em mL, desde `> n~5 un$E.\n\
#V ~R o &b &-`%`!o, ~o a `z`%`!o ~t.`W Dilui`%`!o|ci `9 #. `9 Vf|ci, cf: `z`%`!o &3 e ~t;Vi, Vf: `ps &3 e ~t\
 (#9 un$E)|a `d de `^t&E`!&zuda|~c0 `9 20,#I 0,$A `)0|c_fqso.dil`W Fator de &-`%`!o|*D Vf / Vi = ci / cf|f:\
 &b &-`%`!*@&X un$Es)|f > 1|Vi ~N mL, V*D 50 mL: *D 5|c_fqso.dil`W`E `^`%`!`5 HCl &)0 `C dm`(`B; *R#AeY' 250\
 *? 0,0400 `C dm`(`B.`: `p a medir e &b &-`%`!o.~) #. `9 Vf / ci = 0,0400 `9 250 / &)0 ~N,0 mL~/ *D Vf / Vi =\
 250 / 10,#I 2&O&A MedeY' 10,0 mL e &--s#'t`, 250 mL (*D 2&O).`F`%`!o: ci / c*D &)0 / 0,040#I 2&O.~j~6s\
 &-`%`' ~pmi`g *R`Hr v`-*ks `^`%`' a `nir `ca s`3 (`^`%`!&z`!e).\n\
S`!o rigorosas `y`> usam pipeta&x bal`' volum`,&v.~i`b `> a `d de `^t&zuda ao &-r.~+ Vf `;o `p de `-~a a\
 juntar (`, o `p ~t).$% Misturar mL `; dm`B n~5 f`3&/.$% Obter f < 1 ($Vr os `ps).~h$% Diluir: n de `^to\
 ~L.$% ci #. Vf.$% *D Vf / Vi = ci / cf > 1.$% Pipeta `H Vi; bal`!o volum`,trico `H Vf.~g\n\
Dilu`0raY' &O mL `ca `^`%`!#%`, $A,0 mL. ~z `, o &b &-`%`!o?~e\n\
f ~N0,0 / &O = 20.$p 1|q5e1|Volume `c g`-&xm PTN*b|q5a~{`M$} `> `p YP 0,35 `C de N`/ em PTN?`E $] 0,35 `C;\
 VY) #l dm`B `C`(`4.Yd`,to$} V = n `9 Vm.$L`^`%`!o:~) V = 0,35 `9 #l = 7,8 dm`B`Q 7,8 dm`B (2 alg. sig.,\
 `;&E).`S`%`!#W ~; `p valia `H &M`>r g`-&xm PTN.`= dar 7,84 dm`B (algarismos a `K).$p 2|q5e2|Pre`Hr ~!\
 `^`%`!o `y &-`%`!o|c_fqso.dil|q5e~{`M$} $? ~! `^`%`!o $v0 `C dm`(`B. Pre`H #t *? */ `C dm`(`B.`E ci ~}0; c*D\
 */ `C dm`(`B; V*D #t mL.Yd`,to$} ci #. Vf.$L`^`%`!o:~) Vi = */ `9 #t / $v#I 62,5 mL~/ *D #t / 62,5 = 8,00`Q\
 medir 62,5 mL e `;pletar at`, #t mL.`S`%`!#! `^`%`!o ~t `, 8 &g `K dilu`0da.`= juntar #t *? `-~a (o `p ~t\
 ~v*k ~R).$p 3|q5e3|#U`%`!${ ~S `ca `^`%`!`5 a`%`Acar|c_fqso.con|q5d~{`M$} d~ulveY' 34,2 &P sacarose *s 342,3\
 g `C`(`4) em `-~a at`, 200 mL.~6 `^`%`!o `g `? vol`A~Q &)5 g cm`(`B.`: `z`%`!${ % em `?.$L`^`%`!o:~) $] 34,2\
 / 342,3 = 0,0999 `C~/ #d 0,0999 / &q#I ~c0 `C dm`(`B~C #: da `^`%`!o: &)5 `9 20#I 210 g$q % (m/m&p 34,2 /\
 210 `)#I 16,3 %`Q #d ~c0 `C dm`(`B e 16,3 % em `?.`S`%`!#! `? da `^`%`!o inclui o `^t${ o #1.`= #x 200 g `;o\
 `? da `^`%`!o.\n\
"
 return _ns('D', _dz(D))


_F['p_q5'] = _m_p_q5


def _m_p_q6():
 D = "#3#5 3#4 Trans~:ma`%`' qu`0~Qs~f q6a|`G nas $-`%`': ~q`%`!`5 &H|$-ca$Mi~Q `>Yi ~:maca`5 `<coes ~qca`5 &H\
 Y7er~Q YAer~Q &[`g~3ca `+$( `<&S|c_fqlg.dh*_`Acleo|q4a:$h`%`!$M`0~Q: $.abil$E, `+ e `;`}o;r8b:Equa`%`'\
 qu`0~Q&x #j Lavoisier$7 `I Trans~:ma`%`' qu`0~Qs~m~4 ~! $-`%`!o `;o `>Yi e ~:ma`%`!`5 `<`%`'.`u $-`%`'\
 Y7`,r~Q$( YA`,r~Qs.$% &f o &l da ~q`%`!`5 &H, `8H.`D `8H a `nir ~K `+$( `<`%`!o.~l\n\
N~! $-`%`!o*-s `<`%`' ~' $-ge$) par`g-se e ~:maY' `<`%`' novas &! produtos.\n\
Partir custa `+; ~:#Z devolve `+.\n\
Se s#bvolve `K do `> se Y4*- $-`%`!#/`>ce ~3`%a: `, Y7`,r~Q.~k$% Sis`ga: o `> se $.uda ($-ge$) e produtos);\
 *u`%a: o r$.o.$% Va*k`%`!`5 &H, `8H: `+ tro~I `;o &k*- *Rss`!o ~L.$% Exot`,r~Q: `8H < 0 (&| `+ `H ~3`%a).$%\
 Endot`,r~Q: `8H > 0 (~V `+ d~3`%a).$% `8H = $o E(`<`%`' `>Yi~K) - $o E(`<`%`' ~:ma~K).`R`V `;bust`!~9 *!~d\
 *S O`/ ~7 CO`/ *S H`/O.&(YiY' 4 C-H e 2 O=O: 4 `9 413 *S `9 498 = 2648 kJ.\n\
Y(Y' 2 C=O e 4 O-H: 2 `9 799 + 4 `9 463 = 3450 kJ.\n\
`8H = 2648 - 345#I -802 kJ `C`(`4: `, Y7`,r~Q.~6s `+$( `<`%`!*v`!&z`,*Ws; o ~b obtido `, *Cdo.$+&xxot`,rmiYg:\
 `;bust`', respira`%`!o celular.$+&xndot`,rmiYg: ~Woss`0$)e, de`;&,`%`!~9 calc`-rio.\n\
N~! $-`%`!${ndot`,r~Q ~3`%a arrefece.\n\
`8H refere-se ~]s `ds da equa`%`!#/~ytada.\n\
S#' equa`%`!$k &a `y 2, `8H *2`,m duplica.`W Va*k`%`!`5 &H|`8H = $o E(`>Yi~K) - $o E(~:ma~K)|E: `+$(\
 `<`%`!*@kJ `C`(`4)|~bes m`,dios; usa os d${nu`Mdo|H`/ + Cl`/ ~7 2 HCl: 678 - 862 = -184 kJ|c_fqlg.dh`W Sinal\
 de `8H|`8H < 0: Y7`,r~Q; `8H > 0: YA`,r~Q|`8H: ~q`%`!`5 &H do &[`ga|*Rss`!o ~L|`8H = -802 kJ:\
 Y7`,r~Q|c_fqlg.dh`W`E H`/ + Cl`/ ~7 2 HCl.\n\
`Gs (kJ `C`(`4): H-H 436; Cl-Cl 242; H-Cl 431.`: `8H e tip`5 $-`%`!o.~) QueYi~K: 436 *S42 = 678 kJ~/ Y(~K: 2\
 `9 431 = 862 kJ~C `8H = 678 - 862 = -184 kJ `C`(`4&A `8H = -184 kJ `C`(`4: $-`%`!${xot`,r~Q.`F`%`!o: ~:maY'\
 `K `<`%`' ~:tes do `> as `> se par`g.~j`x &l de `8H diz `H *I vai a `+: `H ~:a (exo) ou `H dentr*@endo).#>\
 `y ~u `> as `;bust`' servem `H a`>~y e `H produzir `+.~i$% Fazer ~:ma~K ~H `>Yi~K (o &l ~v $Vdo).`i`>~y de\
 &a #Bs coeficie$) da equa`%`!o.`b `> YA`,r~Q signi~v \"`> a`>ce\".`i`>~y `> a `+ de `<`%`!o `, `y `Ce.~h$%\
 Rea`%`!o: `>*E e ~:#Z `<`%`'.$% `8H = $o `>Yi~K - $o ~:ma~K.$% `8H < 0: Y7`,r~Q; `8H > 0: YA`,r~Q.$% YT #Bs\
 coeficie$) da equa`%`!o.~g~1a $-`%`!o `g `8H = +180 kJ `C`(`4. \xc9 Y7`,r~Q ou YA`,r~Q?~e\n\
Endot`,r~Q: `8H > 0, o &[`ga ~V 180 kJ `y `C#b $-`%`!o.~f q6b|Rea`%`' ~Woqu`0~Q&x $B|$-&S ~Woqui~Q ~Wolise\
 ~Wod~ucia&S ~W#r&S $B `.a`5&Xparelhado YK ultravioleta|c_fqel.~W*_`Acleo|q6a:`G nas $-`%`': ~q`%`!`5 &H$7 `I\
 Trans~:ma`%`' qu`0~Qs~m`v $-`%`!o ~Woqu`0~Q.`u ~Wod~ucia`%`!`5 ~W#r`%`!o.`v &7 Y- e ~Or #c ~s.`D a `+\
 m`0nima `c ~W`!o `H `>*E ~! `<`%`!o.~l~6lguns ~W`', sobretud`5 UV, t`Lm `+ `H `nir `<`%`'.#> assim `> &0\
 d*vol descora teci~' e `>ima a pele.`xs &.gmentos `> ~vm `; `.`' $6~' s`!o ~n $-*l~k$% Rea`%`!o ~Woqu`0~Q:\
 $-`%`!o provo~I pel&0.$% Fotod~ucia`%`!o: &0 `>Yi ~! `<`%`!*@ex.: O`/ ~7 2 O).$% Fot#r`%`!o: &0 remove um\
 `.`!*@ex.: N`/ ~7 N`/~X + e`().$% RaY;l Y-: esp`,cie `; um ou `K `.`' $6~' (ex.: Cl~F, O~F, ~FOH).$% Os $B\
 s`!o ~n $-*l`R&D `>*E ~! `<`%`!o, um ~W`!o *Rcis~, `+ i~al ou su~pior ~] `+ de `<`%`!o.~6 `+ `y `C`,$P\
 obt`,Y' dividindo `y NA.`V O=O, 498 kJ `C`(`4, ou 8,27 `)`(`4`l J `y `C`,$P.`x `_ m`-*3 `, h c / #6 2,40\
 `)`(~? Y) 240 nm (UV).\n\
Luz *Q`0~A n`!o `g `+ suficie*V `H $.a `>Yi.~6 ~Woss`0$)e *2`,m `, ~! $-`%`!o ~Woqu`0~Q.*Ts raY;is, o *9*@~F)\
 #Zca o `.`!`5&Xparelhado.`xs $B `nicipam em $-`%`' em YF.*T ~w h~!no, &{m dani~vr c`,lulas (os antioxida$)\
 ajudam a trav`--los).`W `G `y `C`,$P|#6 E(kJ `C`(`4) `)*P NA|NA: &B `)`6`B `C`(`4|~! `<`%`!o `y `C`,$P|O=O:\
 498 `)*P NA = 8,27 `)`(`4`l J|c_fqel.~W`W #M`}`5 *Z m`-*3|`_ m`-x *d / E|E: `+ necess`-*k `y `C`,$P (J);h #d\
 1,99 `)`(`6~% J m|~W`' `; `_ ~o *2`,$!ervem|O=O: `_ m`-x = 240 nm|c_fqel.~W`W`E `+ da `<`%`!o Cl-Cl = 242 kJ\
 `C`(`4.`: ~R `_ capaz de d~uciar o Cl`/.~) #6 242 `)*P &B `)`6`B = &12 `)`(`4`l J~/ `_ &> `)`(`B`P `9 $g0\
 `)`m / &12 `)`(`4`l = 4,95 `)`(~? m&A `_ m`-*3 ~> 495 nm (YK *Q`0~A azul-esverdeada).`F`%`!#! `<`%`!o Cl-Cl\
 `, &.ca; at`, YK *Q`0~A a `>Yi.~j\n\
$h`%`' `K &.cas `>YiY' `; YK de ~o `+.&5 ~u o Cl`/ $-ge `; o H`/ ~] YK e *w n`!o $-ge n${scuro.~i~+ a `+ `y\
 `Ce `;$k fosse `y `C`,$P.`b `> um ~W`!o `; ~H `+ do `> a `<`%`!#/ `>Yi.`i`>~y `> os raY;is t`Lm `.`' $6~'.`[\
 ~Wod~ucia`%`!o `; ~W#r`%`!o.~h$% Rea`%`!o ~Woqu`0~Q: provo~I pel&0.$% Fotod~ucia`%`!o: `>br~, `<`%`';\
 ~W#r`%`!o: ~pd~, `.`!o.$% RaY;l Y-: `.`!`5&Xparelhado, ~n $-tivo.$% `_ m`-x *d / E (E `y `C`,$P).~g&5`> `,\
 `> um &7 Y- `;o o Cl~F `, t`!o $-tivo?~e\n\
Tem um `.`!`5&Xparelha$} #A#' ~:#Z ~! `<`%`!o `; outra esp`,cie `H ~vr `; o octeto.~f q6c|Ozono\
 $.ratosf`,ric${ CFC|~r $.&c *]~, ~r cfc &%fluoro*'netos raY;is &% burac~9 ~r ~-&S ultravioleta &=ocol`5\
 mont$-l&u`Acleo|q6b:Rea`%`' ~Woqu`0~Q&x $B$7 `I Trans~:ma`%`' qu`0~Qs~m~4 a ~:ma`%`!${ ~,`;&,`%`!~9 ~r na\
 $.&c.`J a *]~, ~r `; a filtragem da ~-`%`!o UV.~4 `;o os CFC d$.roem o ~r.$% Referir medi~K de &=e`%`!~P *]~, ~r.~l\n\
L`- em cima, o ~r Y% `;o um &=etor solar do planeta.\n\
Y(-se #bsfaz-se &X `Hr, ~Vndo UV.`xs CFC &|m &%, `> desfaz o ~r muit`5*Rssa.~k$% Ozono: O`f; existe\
 sobretud&Ea $.&c (`] 15 km a 35 km).$% Y(`%`!o: O`/ + UV ~7 2 O; depois O Y]`/ ~7 O`f.$% De`;&,`%`!o: O`f +\
 UV ~7 O`/ Y].$% CFC: &%fluoro*'netos (ex.: CCl`fF), usa~' em aeross`3i&x frigor`0fiYg.$% Na $.&c*- ~-`%`!o\
 UV &| raY;is Cl~F ~' CFC.`R~6 ~:ma`%`!${ ~,`;&,`%`!~9 ~r ~Vm ~-`%`!o UV.`x equil`0brio ~B as #P mant`,m a\
 *]~, ~r.`x &7 clor`5str`3i o ~r em YF:$% Cl~F Y]`f ~7 ClO~F Y]`/;$% ClO~F Y] ~7 Cl~F Y]`/.`x &% #0 a ~vr Y-:\
 u$!`3 &7 d$.r`3i milhare$( `C`,`Z de O`f.\n\
Funciona `;o #k d~,`;&,`%`!o.~6 ~E`%`!~9 ~r sobr#' Ant`-rtida chama-se \"burac~9 ~r\".Yde&! ozon`5ixa &; `K\
 UV: `K cancr`5 pele e cataratas.`x #J`5 Mont$-l (1987) proibiu gradualme*V os CFC.`xs $fitutos (HCFC, HFC)\
 n`!`5stroem tanto o ~r.~6 *]~, ~r $.`- a recu~par devagar.`W Y(`%`!~9 ~r|O`/ + UV ~7 2 O; O Y]`/ ~7 O`f|O:\
 #n`,ni#%`3mic*@&7)|$.&c|~V ~-`%`!o UV|`W D$.rui`%`!o #B &%|Cl~F Y]`f ~7 ClO~F Y]`/; ClO~F Y] ~7 Cl~F\
 Y]`/|Cl~F: &7 &% (regenerad&Eo fim)|$.&c, na *Rsen`%~, CFC|um Cl~F d$.r`3i #|s `C`,`Z de O`f|`W`E as\
 dua&xtapas d~,strui`%`!~9 ~r #B &%.`: equa`%`!o global e papel do &%.~) Cl~F Y]`f ~7 ClO~F Y]`/~/ ClO~F Y]\
 ~7 Cl~F Y]`/~C Soma, cortando o `> aparece ~' &G la~': O`f Y] ~7 2 O`/.$q O Cl~F aparece no in`0ci${ no fim:\
 n`!$k Y4.&A Global: O`f Y] ~7 2 O`/; o Cl~F `, um #k.`F`%`!o: h`- 4 `-`T de O de ~I lad*@3 Yb = 2 `9 2).~j\n\
Pe`>nas `d$( CFC causam #[ dano `y`> o clor$k regenera.`x #J`5 Mont$-l `, um exempl`5 sucess`5\
 coo~pa`%`!#/mbiental.~i`[ o ~r $.ratosf`,ric*@`Atil) `; o troposf`,ric*@*0*V).`b `> o burac~9 ~r `, a causa\
 principal d#/`>cimento global.`i`>~y `> o &7 &% `, regenerado.$% YS `> os CFC s`!o t`3xiYg a&E`0~A\
 d*vol*@s`!o $.`-$K; o ~pigo `, l`- em cima).~h$% O`f na $.&c filtra UV.$% Y(-s#b O`/ + UV #b`;p\xf5e-se `;\
 UV.$% CFC + UV &|m Cl~F.$% Cl~F catalisa ~,strui`%`!~9 O`f.$% #J`5 Mont$-l (1987): fim ~' CFC.~g&5`> `, `> o\
 &7 Cl~F `, chamado #k n~,strui`%`!~9 ~r?~e&5`> `nicipa na $-`%`!&zas `, regenerad&Eo fim: n`!$k Y4 e repete\
 o cicl&zuitas &g.$p 1|q6e1|Exot`,r~Q ou YA`,r~Q?||q6a~{`M$} a `;bust`!`5 1 `C de #^ `g `8H = -1367 kJ `C`(`4.\n\
Classi~v a $-`%`!${ cal$P a `+ &|da `y ~c `C.$L`^`%`!o:~) `8H < 0: $-`%`!${xot`,r~Q.~/ `G &|da: ~c `9 1367 =\
 6,8 `)`6 kJ`Q Y7`,r~Q; ~c `C &|m `] 6,8 `)`6 kJ.`S`%`!o: `, a `+ `> a`>ce ~3`%a.`= dar o &? `; &l &,tivo `;o\
 \"`+ &Rvida\".$p 2|q6e2|Entalpia da s`0$)e d#/mon`0aco|c_fqlg.dh|q6a~{`M$} $.ima `8H `H N`/ + 3 H`/ ~7 2 NH`f.\n\
Da~' (kJ `C`(`4): N$nN 945; H-H 436; N-H 391.$L`^`%`!o:~) QueYi~K: 945 + 3 `9 436 = 2253 kJ~/ Y(~K: 2 `9 3 `9\
 391 = 2346 kJ (~I NH`f `g 3 `<`%`' N-H)~C `8H = 2253 - 2346 = -93 kJ `C`(`4`Q `8H ~> -93 kJ `C`(`4:\
 Y7`,r~Q.`S`%`!#W ~b &Ldo `, -92 kJ `C`(`4; as `+s m`,*Ws d`!o ~! $.imativa.`= #S s`3 3 `<`%`' N-H (s`!o\
 6).$p 3|q6e3|Fot`!o `H `>*E a `<`%`!o O=O|c_fqel.~W|q6b~{`M$} `> `_ m`-*3 &{ ter um ~W`!o `> d~ucia o O`/?`E\
 E(O=O&p 498 kJ `C`(`4; NA $F2 `)`6`B `C`(`4.$L`^`%`!o:~) Por `C`,$P: 498 `)*P &B `)`6`B = 8,27 `)`(`4`l J~/\
 `_ &> `)`(`B`P `9 $g0 `)`m / 8,27 `)`(`4`l = 2,40 `)`(~? m`Q `_ m`-*3 ~> 240 nm (UV).`S`%`!o: na $.&c*-\
 ~-`%`!o UV d~ucia o O`/ e ~pYa ~:#Z O`f.`= es`>~y de dividir `y NA.\n\
"
 return _ns('D', _dz(D))


_F['p_q6'] = _m_p_q6


def _m_x_f1():
 D = "#3#5 10#4 `G $:`r n|f1x1|f1a|r|\n\
~z `, a `+ #N`,$J #m J) `ca bol~, ~c *} &1 $!`(`4?`s 4`t Ec $Q m v`6.`R\n\
Ec $Q `9 ~c `9 &1`6 = &1 J.`r m|f1x2|f1b|r|~1 caixot#bs&^ *X ch`!o Y! Que ~:`%a n`!o $-&^ `@?$H O *>|O ~Z|Uma\
 ~:`%a `> o puxa na horizontal|A `1 d#/r`s 1`t #M`H a dire`%`!`5 ~I ~:`%a `; a d`5&Z`R`x *> `, ~p*|$Pr\
 a`5slocamento horizontal ($G = 90`h): W = 0.`r n|f1x3|f1b|r|~1a ~:`%~, 30 N faz 60`h `; um #2`5 $v m. ~z `,\
 $ku `@ #m J)?`s 30`t W = F d Yg $G.`R\n\
W = 30 `9 $v `9 Yg 60`h = 30 J.`r v|f1x4|f1d|r|`x `@ $-&^do #B pes`5 um corp`5#F *n`3*k ~B &G *9os.`s F`t O\
 *> `, ~! ~:`%a ~Ttiva.`R\n\
Fals#W *> `, ~Ttivo; o `@ s`3 $c d`5sn`0~A, W(P&p -`8#G.`r n|f1x5|f1d|r|~1 ~w cai &O m a `nir do repouso, &X\
 `1 d#/r (g ~N $!`(`6). #M `> `q #m $!`(`4) chega ao ch`!o?`s 10`t Conserva`%`!~P `+ *t`k$8: m g h $Q m v`6.`R\n\
v = $z `) `9 &O) ~N $!`(`4.`r u|f1x6|f1a|r|J kJ$/ a #G `ca pesso~, 60 *} 12 m acima do ch`!*@g ~N $!`(`6;\
 refer`L`M no ch`!o).`s 7200`t #G = m g h; &{s resp*Ir em J ou em kJ.`R\n\
#G = 60 `) `9 12 = 7,2 `)`B J = 7,2 kJ.`r n|f1x7|f1e|r|~1 motor $I #t J e $-&^ 400 J de `@ `Atil. ~z `, o ~<\
 #m %)?`s 80`t ~0 E(`A*[~:&J `)Y_`R\n\
~0 4*P #t `)#I 8Y_`r m|f1x8|f1c|r|\n\
Se o `@ $d ~K ~:`%as `> atuam *X ~w `, negativo:$H a `+ #N`,$J n`!o ~q|a `+ $De`Ml `w &X*R|a `+ #N`,$J do ~w\
 ~E|a `+ #N`,$J do ~w `w`s 3`t #f `+ #N`,$J: &j `8Ec.`R\n\
&j `8Ec < 0: a `+ #N`,$J ~E (o ~w trava).`r n|f1x9|f1e|r|~1 YJ $Se $g `)`P J em &) min. ~z `, #c $D`L`M #m\
 W)?`s #t`t #@ E / `8t, `; `8t e$!egun~'.`R\n\
#@ $g `)`P / 6#I &O `)`6 W.`r n|f1x10|f1c|r|~1 bloc`5 $v *} $g $!`(`4 `H ao fi*A #? m *X ch`!o Y! ~z `, a\
 in$?$E da ~:`%~, ~Z #m N)?`s 6`t W(Fa&p `8Ec e W(Fa&p -Fa d.`R\n\
`8E#d 0 - \xbd `9 $v `9 $g`6 = -9,0 J.\n\
Fa &t / #? $F N.\n\
"
 return _ns('D', _dz(D))


_F['x_f1'] = _m_x_f1


def _m_x_f2():
 D = "#3#5 10#4 `G Y+`3~H el`,&v`r n|f2x1|f2a|r|~1a carg~, *O C YIvessa um fi${m $v s. ~z `, a `X #m A)?`s 3`t #D Q / `8t.`R\n\
I $F / $v = $g A.`r n|f2x2|f2a|r|~1 &K `3hmic#/ 12 V `, ~pcorrido `y 0,40 A. ~z `, #c `1 #m `a)?`s 30`t YB U / I.`R\n\
YB 12 / 0,4#I 30 `a.`r m|f2x3|f2c|r|#7 circuito `; `;~[&x$!`,rie:$H des`<r um `;~[ n`!#/feta os outros|a `X\
 `, ~5 em to~' os `;~[s|a $?`!o `, ~5 em to~' os `;~[s|a `1 #= `, ~o do `> ~I `1`s 2`t E$!`,rie*- `X s`3 `g\
 um caminho.`R\n\
E$!`,rie h`- u$!`3 caminh#! `X `, ~5 em to~' os `;~[s.`r n|f2x4|f2c|r|\n\
~z `, a `1 #= #m `a) de *O `a e $g `a em `H*B?`s 2`t *, = 1 / R1 Yb / R2.`R\n\
*, = 1 / *O Yb / $g = ~c&W Req ~} `a.`r v|f2x5|f2b|r|~6 $0 `c $| `w &_ a `2 `w.`s V`t Pensa no filament`5 ~!\
 l`k#{.`R$> &! ~J, ~G `w `; a `2 (o filamento `>*V `g `K `1).`r n|f2x6|f2d|r|~1 &} `; ~( = 12 V e r = ~c `a\
 ~:nece &1 A. ~z `, a $?`!o &! seus $; #m V)?`s 10`t #8 ~( - r I.`R\n\
#8 12 - ~c `9 &1 ~N V.`r u|f2x7|f2e|r|kWh J MJ~1 aparelh`5 1#t W Y% &C $v h. Que `+ Y4?`s 3`t #6 P `8t; `; P\
 em kW e `8t em h d`- kWh.`R\n\
#6 #? `9 $v = $g kWh = &)8 `)~? J.`r n|f2x8|f2e|r|~1a `1 de 50 `a `, ~pcorrida `y $v A. Que $D`L`M dissipa `y\
 efeito Joule #m W)?`s 200`t #@ R I`6.`R\n\
#@ 50 `9 $v`6 ~} `)`6 W.`r m|f2x9|f2a|r|&D medir a `e`%~, $De`Ml &! $; `ca l`k#{, o volt`0$, `<-se:$H\
 e$!`,rie `; a l`k#{|e$!`,rie `; a &+|em &M`>r *9~9 circuito|em `H*B `; a l`k#{`s 4`t O volt`0$, `;`H &G *9*<\
 #T`R`x volt`0$, `<-se em `H*B*-os &G $; do `;~[.`r n|f2x10|f2b|s2|\n\
~z `, a `1 #m `a) de 50 *A fi`5 #L (~G = 1,7 `)`(`m `a m) `; &) mm`6 de sec`%`!o?`s 0,85`t YB ~G $Z / A, `; A\
 em m`6.`R~6 = &) `)`(`U m`6; YB 1,7 `)`(`m `9 50 / (&) `)`(`U&p 0,85 `a.\n\
"
 return _ns('D', _dz(D))


_F['x_f2'] = _m_x_f2


def _m_x_f3():
 D = "#3#5 10#4 `GY5`3~H t`,&] ~-`%`!o`r n|f3x1|f3a|r|\n\
Converte 25 `hC `H kelvin.`s 298,15`t T (K&p $C (`hC) *S73,15.`R\n\
T = 25 *S73,15 = 298,15 K.`r m|f3x2|f3a|r|~1 &[`ga fecha$}$H $V mat`,*k #p n`!o $V `+|$V `+ e mat`,*k|$V `+\
 `; ~3`%a #p n`!o $V mat`,*k|n`!o $V `+ nem mat`,*k`s 3`t Fechado refere-se ~] mat`,*k.`R~1 &[`ga fechado $V\
 `+ (&k, `@, ~-`%`!o), #p n`!o $V mat`,*k.`r n|f3x3|f3d|s2|&( `+ #m J) $I &q $s `-~a a#/`>~y 10 `hC? (#d 4,18\
 `)`B *N`(`4 K`(`4)`s 8360`t *) c `8T.`R\n\
Q = &q `9 4,18 `)`B `) = 8,4 `)`B J.`r n|f3x4|f3d|s3|&( `+ #m J) `, *Rcisa `H fundir ~c $s gel#/ 0 `hC? (`8H\
 = Y8 `)~% *N`(`4)`s 167000`t *) `8H.`R\n\
Q = ~c `9 Y8 `)~% = 1,67 `)~% J.`r v|f3x5|f3d|r|\n\
Durant#' ebuli`%`!~P `-~a pura*- *Rss`!o ~L*- `2 `w.`s F`t O `> aco*Vce ~] `2 n~! &m`%~, $.ado?`R\n\
Falso: &C a &m`%~, $.ad#/ `2 mant`,Y' (pata#Z).`r n|f3x6|f3e|r|~1 &[`ga $I 300 J `y &k e $-&^ $A J de `@\
 sobre ~3`%a (YB 0). ~z `, `8U #m J)?`s 200`t `8#8 W + Q + R; o `@ $-&^do #B &[`ga `, cedid*@negativo).`R\n\
`8#8 -$A + 300 + #I 200 J.`r m|f3x7|f3c|r|~6 &d`%`!o `, um process`5 $S`L`M de `+ `> ocorre:$H s`3 no\
 v`-cuo|s`3 em ~J|s`3 e$!`3li~'|em l`0qui~' e $T`s 4`t Precisa `> a mat`,*k se possa mover.`R~6 &d`%`!${xige\
 moviment~9 flui$} s`3 aco*Vce em l`0qui~' e $T.`r n|f3x8|f3b|r|~1 #y de #? m`6 $I Er = &) `)`B W m`(`6 e\
 ~:nece 270 W el`,&v. ~z `, o ~< #m %)?`s 18`t ~0 P(el) / (Er A) `)Y_`R\n\
P(rad&p &) `)`B `9 #? = #? `)`B W; ~0 270 / 1#t `)#I 18 %.`r n|f3x9|f3d|r|YdisturaY' 0,10 $s `-~a a 80 `hC `;\
 0,30 $s `-~a a 20 `hC, *X recipie*V *.. ~z `, a `2 ~t #m `hC)?`s 35`t M`,*W pesada *qs `?s (~5 c).`R\n\
$Ce = (0,10 `9 80 + 0,30 `9 20) / 0,4#I 35 `hC.`r n|f3x10|f3c|r|~1a placa *.ra (k = 0,040 W m`(`4 K`(`4) `g\
 $v m`6 e &O c*A $y; `8T = 20 K. ~z `, a $D`L`M ~^ #m W)?`s 32`t #@ k A `8T / $Z, `; $Z em $,s.`R\n\
#@ 0,040 `9 $v `9 20 / 0,05#I 32 W.\n\
"
 return _ns('D', _dz(D))


_F['x_f3'] = _m_x_f3


def _m_x_q1():
 D = "#3#5 10#4 ~| ~' `-`T`r m|q1x1|q1a|r|`x i`!o `6~?&T`fAl`B~X `g:$H 13 &=`', 14 $2`' e 10 `.`'|13 &=`', 14 $2`'\
 e 16 `.`'|27 &=`', 13 $2`' e 10 `.`'|13 &=`', 27 $2`' e 13 `.`'`s 1`t *U A - Z; um YC`!o 3+ ~pdeu 3 `.`'.`R\n\
Prot`': Yj 13. Neutr`': 27 - 13 = 14.\n\
&6`': 13 - 3 ~N (~pdeu 3 `.`').`r n|q1x2|q1a|r|$w $2`' `g &E`Acle`5 ~%`U`/*jFe?`s 30`t Usa *U A - Z.`R\n\
*U A - Yj 56 - 26 = 30.`r v|q1x3|q1a|r|`xs is`3$l `c `N t`Lm o ~; n`A$<`5 `?.`s F`t O `> `, i~al &! is`3$l: Z\
 ou A?`RY6 Os is`3$l t`Lm o ~; n`A$<#%`3mic*@Z).\n\
T`Lm n`A$<o$( `? (A) `etes, `y`> t`Lm $2`' `e*m`r m|q1x4|q1b|r|\n\
~z `, a $@ de #[z~, 6,5 `)`(`4$N m?$H 10`(`l m|10`(`4$N m|10`(`m m|10`(`4`4 m`s 1`t #M`H a mantissa `; 5.`R~6\
 mantissa `, 6,5 e 6,5 #O 5.&5 ~u*- $@ ~8 `, 10`(`4$N~X`4 ~N`(`l m.`r n|q1x5|q1c|d2|`x l`0tio `g os is`3$l\
 `ULi (&B; 7,59 %) e ~?Li (7,02; 92,41 %).$/ Ar(Li), `; #P casa$(ci`K.`s 6,94`t Ar = $o (`? `9 $U`k`M) /\
 $A.`R~6r = (&B `9 7,59 + 7,02 `9 92,41) / $A = 6,94.`r u|q1x6|q1d|s3|g kg mg$/ a `? de */ `C de cloret`5 s`3dio.\n\
Usa M(NaCl&p 58,44 g `C`(`4. Escolh#' un$E.`s 14,6`t Y) n `9 M.`R\n\
Y) n `9 M = */ `C `9 58,44 g `C`(`4 = 14,6 g.\n\
(Tamb`,m *5 0,0146 kg ou 1,46 `)`P mg.)`r n|q1x7|q1d|s2|\n\
Quantas `C`,`Z h`- em 0,10 `C de O`/?$Lsp*I `; 2 `o.`s *Oe22`t *U n `9 NA, `; NA $F2 `)`6`B `C`(`4.`R\n\
*U 0,10 `9 &B `)`6`B $F `)`6`6 `C`,`Z.`r n|q1x8|q1d|s2|\n\
~z `, a `d $[`,&9m 8,0 &P *!~d?\n\
Usa M(CH~d&p 1*O5 g `C`(`4 e 2 `o.`s ~c`t $] m / M.`R\n\
$] 8,0 g / 1*O5 g `C`(`4 = ~c `C.`r m|q1x9|q1e|r|~1a &2 `g &) `C de N`/ e $g `C de H`/.~6 &.`%`!o `Car do H`/\
 `,:$H *r|0,33|$g|0,75`s 4`t x = n(H`/) / n(&<).`R\n\
x(H`/&p $g / (&) + $g&p 0,75.\n\
0,33 se*k &) / $g, `> n`!o `, ~! &.`%`!o `Car.`r v|q1x10|q1b|r|~1 nan`3$, `, i~al a 10`(`l m.`s V`t nano\
 ~N`(`l.`R$> o *Rfix&Eano &8 a 10`(`l.\n\
Logo 1 nm ~N`(`l m ~N00 pm.\n\
"
 return _ns('D', _dz(D))


_F['x_q1'] = _m_x_q1


def _m_x_q2():
 D = "#3#5 10#4 `G ~' `.`' &! `-`T`r m|q2x1|q2a|r|\n\
~z ~K ~-`%`' `g ~W`' `; `K `+?$H Luz violeta|Micro-on~K|Luz &ra|In&.&ro`s 1`t Y1 `+ &8 a ~R #]`L`M e ~o `_.`R\n\
Das op`%`', &0 violeta `g a ~R #]`L`M (~o `_).&5 ~u os seus ~W`' t`Lm `K `+.`r n|q2x2|q2a|s3|$/ a #]`L`M `ca\
 ~-`%`!o `; `_ = #t nm.$Lsp*I em Hz, `; 3 `o.`s *O0e14`t *D c / `_, `; `_ em $,s.`R\n\
*D $g0 `)`m / &O0 `)`(~? $F0 `)`4`P Hz.`r v|q2x3|q2a|r|#7 espetr`5 &R`%`!o, um g`-s produz &@ escuras sobre\
 um $3 Y?`0nuo.`s V`t O g`-s retira alg~!s cores ~] YK Yinca.`R$> o g`-s ~V ~W`' `; ~ytas `+s.\n\
Essas cores faltam no $3 #'parecem `;o &@ escuras.`r n|q2x4|q2b|s3|\n\
~z `, a `+ d&E`0~A $] 3 do `-Y9`5 ~2`,#X, em joules?`s -2,42e-19`t E~U $O `)`(`4`m / n`6.`R\n\
E`f $O `)`(`4`m / 3`6 = -2,42 `)`(`4`l J.`r m|q2x5|q2b|r|~6 #R`%`!o $] 5 ~7 $] 3 no `-Y9`5 ~2`,#X:$H #K um\
 ~W`!`5 in&.&ro|~V um ~W`!`5 in&.&ro|#K um ~W`!`5 ultravioleta|#K um ~W`!o *Q`0~A`s 1`t Desce ou sobe? N`0~A\
 ~t $] 3 `, a s`,ri#b Paschen.`R`x `.`!`5sce (5 ~7 3): h`- &Q`!o.\n\
#M n`0~A ~t $] 3 (s`,ri#b Paschen), o ~W`!o `, de in&.&ro.\n\
`_ *d / `8#6 1,28 `)`(`U m.`r m|q2x6|q2c|r|`x $3 ~Wo`.`3nic`5 um `N `g *=s `; $1s 2 : 2 : 6 : 2.\n\
~z `, o `N?$H Magn`,sio|Oxig`,#X|S`3dio|N`,on`s 1`t Soma os `.`' de to~' os *=s.`R\n\
2 *S + 6 *S = 12 `.`': Yj 12, magn`,si*@1s`6 2s`6 2p`U 3s`6).`r v|q2x7|q2d|r|~1a ~x &{ ter, n&z`-*3, &G `.`',\
 `; spins #H`s V`t YO`0pi`5 Exclus`!`5 Pauli.`R$> `, o YO`0pi`5 Exclus`!`5 Pauli.`r m|q2x8|q2e|r|\n\
~z `, a ~=`%`!o `.`3$8 do c`-lcio, Ca (Yj 20), no $.#Q$H 1s`6 2s`6 2p`U 3s`6 3p`U 3d`6|1s`6 2s`6 2p`U 3s`6\
 3p`m|1s`6 2s`6 2p`m 3s`6 3p`U|1s`6 2s`6 2p`U 3s`6 3p`U 4s`6`s 4`t Depoi$( 3p`U, o $e`0~A segui*V `, o\
 4s.`R`xrde*A *Renchimento: 1s 2s YX 4s.\n\
#M 20 `.`': 1s`6 2s`6 2p`U 3s`6 3p`U 4s`6.`x 4&xnche-s#'$) do 3d; p s`3 leva 6 `.`'.`r n|q2x9|q2e|r|$w `.`'\
 $6~' `g #/zoto, N (Yj 7), no $.#Q`s 3`t 2p`B: aplica a Regr~, Hund.`R\n\
N: 1s`6 2s`6 2p`B. Pela Regr~, Hund, os 3 `.`' 2p ~vm em ~@ `e*m\n\
H`- 3 `.`' $6~'.`r n|q2x10|q2e|r|$w `.`' `7 `g o &%, Cl (Yj 17)?`s 7`t Escrev#' ~=`%`!${ Y?a os `.`' do `A~_`0~A.`R\n\
Cl: 1s`6 2s`6 2p`U 3s`6 3p~%. \xda~_`0~A $] 3: 2 + 5 = 7 `.`' `7.\n\
"
 return _ns('D', _dz(D))


_F['x_q2'] = _m_x_q2


def _m_x_q3():
 D = "#3#5 9#4 $5`3Y;`r m|q3x1|q3a|r|&(m ordenou os `Ns pel&E`A$<#%`3mico, `;&Ea &L atual?$H\
 Moseley|D\xf6bereiner|Newlands|&'`s 1`t &' usou a `? at`3~Q.`RYdoseley (1913) mostrou `> a $@ ~yta `, a\
 d&E`A$<#%`3mico.\n\
&' (1869) tinha usad#/ `? at`3~Q.`r n|q3x2|q3a|r|#o `> ~p`0&4 $.`- ${lement`5 ~=`%`!o 1s`6 2s`6 2p`U 3s`6\
 3p`U 4s`6?`s 4`t O ~p`0&4 `, o `A~_`0~A ocupado.`R`x `A~_`0~A ocupado `, $] 4 (4s`6): ~p`0&4 4 (`, o\
 c`-lcio).`r m|q3x3|q3a|r|`x `N `; ~=`%`!`5 val`L`M 3s`6 3p`P ~ptenc#'o:$H `O 4, ~p`0&4 3|`O 16, ~p`0&4 4|`O\
 16, ~p`0&4 3|`O 6, ~p`0&4 3`s 3`t Bloco p: `O = `.`' `7 Yb0.`R\n\
Val`L`M: 2 + 4 = 6 `.`' n&E`0~A 3.\n\
Bloco p: `O 6 Yb#I 16; ~p`0&4 3 (`, ${nxofre).`r v|q3x4|q3b|r|~6*x`5 um ~p`0&4, o $i at`3mico `w.`s F`t Pensa\
 na ~M #q e n&E`0~A ~' `.`' `7.`RY6 No ~p`0&4*- ~M #q `w e &E`0~A `, o ~;.`xs `.`' s`!o `K YI`0~': o $i ~E.`r\
 m|q3x5|q3b|r|\n\
~z ~' `Ns `g ~R `+ `j`%`!o?$H Pot`-ssio|Fl`Aor|L`0tio|S`3dio`s 2`t EI `w no ~p`0&4 (~7) e ~E no `O (#u).`R`x\
 fl`Aor $.`- `K ~] direita e `K acima: `g a ~R EI (1681 kJ `C`(`4).`r n|q3x6|q3b|s3|~6 EI do l`0tio `, 520 kJ\
 `C`(`4. ~z `, a `+ `H ionizar um `-$4, em J?`s 8,64e-19`t YT `y $A0 e divide `y NA.`R\n\
#6 520 `)*P &B `)`6`B = 8,64 `)`(`4`l J.`r m|q3x7|q3c|r|&( i`!o #A#' ~:#Z o c`-lci*@`O 2)?$H\
 Ca`(|Ca`6~X|Ca`6`(|Ca~X`s 2`t Os ~J do `O 2 ~pdem os 2 `.`' `7.`R`x c`-lcio ~pde os 2 `.`' 4&x ~:ma Ca`6~X\
 (~=`%`!~9 `-rgon).`r v|q3x8|q3c|r|~6 ~s ~' *1`,YG `w a`5s~y o `O 17.`s F`t Os *1`,YG captam `.`'; ~u `, `K\
 f`-cil em `-`T pe`>&!.`RY6 A ~s ~' *1`,YG ~E no `O: o fl`Aor `, o `K $-tivo.`r m|q3x9|q3c|r|\n\
~z `, a f`3&/ do `;posto ~:mado `y alum`0#X (Al`B~X) e #n`,#X (O`6`()?$H Al`/O`f|Al`fO`/|AlO|AlO`/`s 1`t A $r\
 ~K ~Ms `g de ser zero.`R\n\
2 `9 (+3) + 3 `9 (-2&p 0: a f`3&/ `, Al`/O`f.\n\
"
 return _ns('D', _dz(D))


_F['x_q3'] = _m_x_q3


def _m_x_q4():
 D = "#3#5 10#4 $h`%`!$M`0~Q`r m|q4x1|q4a|r|\n\
~z ~K `<`%`' `, a `K curta?$H C=C|To~K t`Lm o ~; `;`}o|C$nC|C-C`s 3`t Y1 ~. `nilha~' *Cm `K *:`Acleos.`R~6\
 tripla C$nC (120 pm) `, a `K curta #' `K ~:te.`r v|q4x2|q4a|r|~6 ~:ma`%`!`5 ~! `<`%`!$M`0~Q &| `+.`s V`t A\
 `+ ~' `-`T `<~' `, ~o do `> se`H~'.`R$> ao ~:#Z a `<`%`!o, o &[`ga ~v `; ~H `+ e &| a `e`%a.`r\
 m|q4x3|q4b|r|&( tip`5 `<`%`!o h`- no cloret`5 $D`-ssio, KCl?$H Co*5nt#'$'|I`3$8|Met`-lica|Co*5*V $'`s 2`t K\
 `, $|; Cl `, n`!o $|.`RYdetal e n`!o $|: o K ~pde 1 `.`!${ o Cl ganha-o: `<`%`!o i`3$8.`r n|q4x4|q4c|r|$w ~.\
 de `.`' n`!o `<$) `g a `C`,cul~, H`/O?`s 2`t Conta os `.`' `7 e os ~. `<$).`R\n\
2 `9 1 + 6 = 8 `.`', 4 ~.. 2 s`!o `<$) (O-H): soYim 2 n`!o `<$) no O.`r m|q4x5|q4c|r|&( `<`%`!${xiste ~B os\
 `-`T d#'zot&Eo N`/?$H Simples|I`3$8|Tripla|Dupla`s 3`t 10 `.`' `7; ~I N *Rcis~, octeto.`R\n\
2 `9 5 ~N `.`', 5 ~.. N$nN usa 3 ~.; 1 YE`!o `<*V em ~I N.`r m|q4x6|q4d|r|\n\
~z `, a Y3*k da `C`,cul~, *!~d?$H Tetra`,drica|Quadrangular plana|Piramidal trigonal|Angular`s 1`t 4 ~. `<$)\
 e nenhum n`!o `<*V ~] #0 do C.`R\n\
4 `Os ~] #0 do C afastam-s#'&z`-*3: tetra`,drica, `; 109,5`h.`r v|q4x7|q4d|r|~1a `C`,$P `; `<`%`' $'es `,\
 &X*R $'.`s F`t Pensa no CO`/.`RY6 No CO`/ as `<`%`' s`!o $'es, #p a ~:ma Y, anula as $'$Es.`r\
 m|q4x8|q4e|r|`x `O fun$_ -COOH caracteriza:$H os `-lcoois|as aminas|os `-ci~' *'x`0liYg|as cetonas`s 3`t\
 \xc1cid${tanoico: CH`fCOOH.`R$%COOH `, o `O *'xilo ~' `-ci~' *'x`0liYg (ex.: `-cid${tanoico).`r\
 n|q4x9|q4e|r|$w `-`T de ~2`,#X `g #/lcano `; 6 `-`T de &:?`s 14`t Alca&!: C~UH`/~U\u208a`/.`R\n\
2 `9 6 *S = 14: Yc, C*jH&T~d.`r m|q4x10|q4f|r|&5`> `, `> a `-~a e o hexan&E`!$k &2m?$H Ambos t`Lm `<`%`' de\
 ~2`,#X|Ambos s`!o $'es|A `-~a `, $' e o Yc `, a$'|O Yc `, i`3nico`s 3`t Semelh#e d~ulve &Xelh#e.`R~6 `-~a `,\
 $' (`; `<`%`' de ~2`,#X); o Yc `, a$'.~6s `C`,`Z de `-~a YIeY' `K ~B si: os l`0qui~' n`!$k &2m.\n\
"
 return _ns('D', _dz(D))


_F['x_q4'] = _m_x_q4


def _m_x_q5():
 D = "#3#5 10#4 $j~ps`'`r n|q5x1|q5a|s3|&( `p YP 2,50 `C `c g`-&xm PTN, em dm`B?`s 5*O`t V = n `9 Vm.`R\n\
V = 2,50 `9 #l = 5*O dm`B.`r m|q5x2|q5a|r|\n\
~z ~' $T `, `K dens~9 `> #/r em PTN?$H CO`/ *s 4&11 g `C`(`4)|CH~d *s 1*O5 g `C`(`4)|H`/ (M ~}2 g `C`(`4)|He\
 *s &10 g `C`(`4)`s 1`t ~G = M / Vm: `;`H M `; a d#/r (`] 29 g `C`(`4).`R\n\
S`3 o CO`/ `g M ~R do `> a d#/r: ~G = 4&11 / #l *G dm`(`B (ar: 1,29).`r v|q5x3|q5b|r|`x g`-s `K $U#e n#/r\
 seco `, o #n`,#X.`s F`t 78 % d#/r seco `,...`R\n\
Falso: #/zot*@N`/) `, `] 78 % d#/r seco; o #n`,#X `] 21 %.`r m|q5x4|q5b|r|\n\
~z ~' *0$) Y>ibui `H as chuvas `-ci~K?$H CO|SO`/|Ar (`-rgon)|O`f $.ratosf`,rico`s 2`t \xd3xi~' de enxofre e\
 d#'zoto ~:mam `-ci~' `; a `-~a.`R`x SO`/ (e os NO*i) $-gem `; a `-~a da atmosfera e ~:mam `-ci~'.`r\
 m|q5x5|q5c|r|~1a &2 dis~psa um feix#b laser e n`!$kdimenta. \xc9:$H ~! `^`%`!o|~! $f`k`M pura|~! $t`!o|um\
 $a`s 4`t Efeit`5 Y0`R\n\
Dis~psar &0 se$!edimentar `, pr`3pri`5 um $a (efeit`5 Tyndall).`r n|q5x6|q5d|s3|\n\
D~ulveY' &q0 `C de `^t#%`, 0,400 dm`B de `^`%`!o.\n\
~z `, a `z`%`!o, em `C dm`(`B?`s ~c0`t #d n / V.`R\n\
#d &q0 / 0,40#I ~c0 `C dm`(`B.`r u|q5x7|q5d|s3|g mg kg&( `? de NaOH *s 40,00 g `C`(`4) `, $u `H 250 *?\
 `^`%`!o 0,$A `C dm`(`B?`s &)0`t $] c `9 V; Y) n `9 M.`R\n\
$] 0,$A `9 *r#I 0,0250 `C; Y) 0,0250 `9 40,0#I &)0 g.`r n|q5x8|q5e|s3|&( `p, em mL, de `^`%`!o &)0 `C dm`(`B\
 se usa `H *R`Hr 200 *? 0,0#t `C dm`(`B?`s 10,0`t ci #. Vf.`R\n\
Vi = 0,0#t `9 2*P &)0 ~N,0 mL.`r m|q5x9|q5e|r|\n\
Diluiu-se ~! `^`%`!o `; &b &-`%`!o 4. A `z`%`!o ~t `,:$H i~al ~] &3|1/2 da &3|1/4 da &3|4 &g a &3`s 3`t *D ci / cf.`R\n\
*D ci / c*D 4&W c*D ci / 4.`r n|q5x10|q5d|s2|~1a `-~a `g 0,050 &P nitrato&xm &) kg. ~z `, a `z`%`!${m *8?`s\
 50`t *8 = m `^to / m `^`%`!o `)`U (#9 un$E).`R\n\
0,050 g / $A0 g `)`U = 50 *8 (50 mg `y kg).\n\
"
 return _ns('D', _dz(D))


_F['x_q5'] = _m_x_q5


def _m_x_q6():
 D = "#3#5 9#4 Trans~:ma`%`' qu`0~Qs`r m|q6x1|q6a|r|~1a $-`%`!o `; `8H = -250 kJ `C`(`4:$H ~V `+ d~3`%a|n`!o $V\
 `+|s`3 ocorre `; YK|&| `+ `H ~3`%a`s 4`t O &l de `8H diz `H *I vai a `+.`R\n\
`8H < 0: $-`%`!${xot`,r~Q, &| `+ `H ~3`%a.`r n|q6x2|q6a|r|\n\
Estima `8H (kJ `C`(`4) de H`/ + F`/ ~7 2 HF. Da~': H-H 436; F-F 159; H-F 567.`s -539`t `8H = $o `>Yi~K - $o\
 ~:ma~K.`R&(Yi~K: 436 Yb59 = 595 kJ. Y(~K: 2 `9 567 = 1134 kJ.\n\
`8H = 595 - 1134 = -539 kJ `C`(`4.`r v|q6x3|q6a|r|\n\
N~! $-`%`!${ndot`,r~Q*- `2 d~3`%~,sce.`s V`t O &[`ga ~V `+ de *I?`R$> o &[`ga ~V `+ d~3`%a, `> arrefece.`r\
 m|q6x4|q6b|r|~1 &7 Y- `, ~! esp`,cie `>:$H `g #B ~H um `.`!`5&Xparelhado|`g to~' os `.`' emparelha~'|s`3\
 existe no $.ad*v`3lido|`g ~M &,tiva`s 1`t O *9${m Cl~F Y/...`R`xs $B t`Lm um ou `K `.`' $6~'; `y ~u s`!o ~n\
 $-*l`r n|q6x5|q6b|s3|~6 `+ da `<`%`!o Br-Br `, 193 kJ `C`(`4. ~z `, o `_ m`-*3 #m nm) `c ~W`!o `> a `>Yi?`s\
 620`t Passa `H J `y `C`,$P e usa `_ *d / E.`R\n\
#6 193 `)*P &B `)`6`B = 3,21 `)`(`4`l J.\n\
`_ &> `)`(`B`P `9 $g0 `)`m / 3,21 `)`(`4`l = 6,20 `)`(~? Y) 620 nm.`r m|q6x6|q6b|r|~6 $-`%`!o O`/ + ~-`%`!o\
 UV ~7 2 O `, ~!:$H ~Wod~ucia`%`!o|$2a&^`%`!o|`;bust`!o|~W#r`%`!o`s 1`t A `<`%`!o O=O `ne-se.`R~6 YK `n#'\
 `<`%`!o O=O: `, ~! ~Wod~ucia`%`!o.`r v|q6x7|q6c|r|~1 `Anico &7 &% &{ d$.ruir #|s `C`,`Z de ~r.`s V`t O Cl~F\
 `, regenerad&Eo fim do ciclo.`R$> o Cl~F atua `;o #k e `, regenerado, repetindo o ciclo.`r m|q6x8|q6c|r|&(\
 acordo `|$_ levou ao fim do uso ~' CFC?$H #J`5 Quioto|Tratad`5 Lisboa|Acord`5 Paris|#J`5 Mont$-l`s 4`t Foi\
 assinad${m 1987.`R`x #J`5 Mont$-l (1987) reduziu e eliminou os CFC.`r m|q6x9|q6c|r|\n\
~z `, a principal fun`%`!~P *]~, ~r?$H Produzir #n`,#X `H respirar|Refletir &0 *Q`0~A|Absorver `ne da ~-`%`!o\
 ultravioleta|Absorver o di`3xid`5 &:`s 3`t O ~r \"filtra\" um tip`5 ~-`%`!o ~pigosa.`R`x ~r $.ratosf`,rico\
 ~V #[ `ne da ~-`%`!o UV do Sol.\n\
"
 return _ns('D', _dz(D))


_F['x_q6'] = _m_x_q6


_imp('m1')
