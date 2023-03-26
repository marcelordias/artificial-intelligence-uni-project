from classes import Map, City

portugal = Map('Portugal')

aveiro = City('Aveiro')
braga = City('Braga')
braganca = City('Bragança')
beja = City('Beja')
castelo = City('Castelo Branco')
coimbra = City('Coimbra')
evora = City('Évora')
faro = City('Faro')
guarda = City('Guarda')
leiria = City('Leiria')
lisboa = City('Lisboa')
porto = City('Porto')
vila = City('Vila Real')
viseu = City('Viseu')
viana = City('Viana do Castelo')
setubal = City('Setúbal')
portalegre = City('Portalegre')
santarem = City('Santarém')

portugal.add_city(aveiro)
portugal.add_city(braga)
portugal.add_city(braganca)
portugal.add_city(beja)
portugal.add_city(castelo)
portugal.add_city(coimbra)
portugal.add_city(evora)
portugal.add_city(faro)
portugal.add_city(guarda)
portugal.add_city(leiria)
portugal.add_city(lisboa)
portugal.add_city(porto)
portugal.add_city(vila)
portugal.add_city(viseu)
portugal.add_city(viana)
portugal.add_city(setubal)
portugal.add_city(portalegre)
portugal.add_city(santarem)

aveiro.add_neighbor(porto, 68)
aveiro.add_neighbor(viseu, 95)
aveiro.add_neighbor(coimbra, 68)
aveiro.add_neighbor(leiria, 115)

braga.add_neighbor(viana, 48)
braga.add_neighbor(vila, 106)
braga.add_neighbor(porto, 53)

braganca.add_neighbor(vila, 137)
braganca.add_neighbor(guarda, 202)

beja.add_neighbor(evora, 78)
beja.add_neighbor(faro, 152)
beja.add_neighbor(setubal, 142)

castelo.add_neighbor(coimbra, 159)
castelo.add_neighbor(guarda, 106)
castelo.add_neighbor(portalegre, 80)
castelo.add_neighbor(evora, 203)

coimbra.add_neighbor(viseu, 96)
coimbra.add_neighbor(leiria, 67)

evora.add_neighbor(lisboa, 150)
evora.add_neighbor(santarem, 117)
evora.add_neighbor(portalegre, 131)
evora.add_neighbor(setubal, 103)

faro.add_neighbor(setubal, 249)
faro.add_neighbor(lisboa, 299)

guarda.add_neighbor(vila, 157)
guarda.add_neighbor(viseu, 85)

leiria.add_neighbor(lisboa, 129)
leiria.add_neighbor(santarem, 70)

lisboa.add_neighbor(santarem, 78)
lisboa.add_neighbor(setubal, 50)

porto.add_neighbor(viana, 71)
porto.add_neighbor(vila, 116)
porto.add_neighbor(viseu, 133)

vila.add_neighbor(viseu, 110)

for i in portugal.find_path(porto, castelo):
    print(i.city.name)
