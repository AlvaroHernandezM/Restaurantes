import nltk 
from nltk import word_tokenize

def clearEmptyWords(text):
	stopwords = nltk.corpus.stopwords.words('spanish')
	stopwords.remove('sí')
	#stopwords.remove('A veces')
	stopwords = addMoreStopWords(stopwords)
	return list(nltk.FreqDist(w.lower() for w in text if w not in stopwords).keys())

def addMoreStopWords(stopwords):
	aditionalWords = str('rico,ves,vez,comida,disfruto,pienso,comer,llevo,dedico,prefiero,gusta,pagar,pensado,ganas,larry,edad,años,hola,ola,a,adelante,ademas,además,adrede,ahi,ahí,ahora,al,alli,allí,alrededor,antano,antaño,ante,antes,apenas,aproximadamente,aquel,aquél,aquella,aquélla,aquellas,aquéllas,aquello,aquellos,aquéllos,aqui,aquí,arriba,abajo,asi,así,aun,aún,aunque,b,bajo,bastante,bien,breve,c,casi,cerca,como,cómo,con,conmigo,contigo,contra,cual,cuál,cuales,cuáles,cuando,cuándo,cuanta,cuánta,cuantas,cuántas,cuanto,cuánto,cuantos,cuántos,d,de,debajo,del,delante,demasiado,dentro,deprisa,desde,despacio,despues,después,detras,detrás,dia,día,dias,días,donde,dónde,dos,durante,e,el,él,ella,ellas,ellos,en,encima,enfrente,enseguida,entre,es,esa,ésa,esas,ésas,ese,ése,eso,esos,ésos,esta,está,ésta,estado,estados,estan,están,estar,estas,éstas,este,éste,esto,estos,éstos,ex,excepto,f,final,fue,fuera,fueron,g,general,gran,h,ha,habia,había,habla,hablan,hace,hacia,han,hasta,hay,horas,hoy,i,incluso,informo,informó,j,junto,k,l,la,lado,las,le,lejos,lo,los,luego,m,mal,mas,más,mayor,me,medio,mejor,menos,menudo,mia,mía,mias,mías,mientras,mio,mío,mios,míos,mis,mismo,mucho,muy,n,nada,ninguna,nos,nosotras,nosotros,nuestra,nuestras,nuestro,nuestros,nueva,nuevo,o,os,otra,otros,p,pais,paìs,para,parte,pasado,peor,pero,poco,por,porque,pronto,proximo,próximo,puede,q,qeu,que,qué,quien,quién,quienes,quiénes,quiza,quizá,quizas,quizás,r,raras,repente,s,salvo,se,sé,segun,según,ser,sera,será,sido,siempre,sin,sobre,solamente,solo,sólo,son,soyos,su,supuesto,sus,suya,suyas,suyo,t,tambien,también,tampoco,tarde,te,temprano,ti,tiene,todavia,todavía,todo,todos,tras,tu,tú,tus,tuya,tuyas,tuyo,tuyos,u,un,una,unas,uno,unos,usted,ustedes,v,veces,vosotras,vosotros,vuestra,vuestras,vuestro,vuestros,w,x,y,ya,yo,z,acá,ajena,ajenas,algo,algúna,algúno,algúnas,allá,ambos,atrás,cabe,cada,cierta,ciertos,conseguimos,conseguir,consigo,consigue,consiguen,consigues,cualquiera,cualquieras,cuan,dejar,demás,demasiada,demasiadas,empleáis,emplean,emplear,empleas,empleo,entonces,eras,eramos,eran,eres,estaba,estáis,estamos,esteo,estes,estoy,etc,fin,fui,fuimos,bueno,haces,hacéis,hacemos,hacen,hacer,hago,intentas,intentáis,intentamos,intentan,intentar,intento,ir,juntos,largo,misma,mismas,modo,muchas,muchísima,muchísimas,muchos,ni,ningúna,ningúno,ningúnas,nosotrasos,otras,parecer,poca,pocas,podéis,podemos,poder,podrías,podríais,podríamos,podrían,por qué,primero,pueden,puedo,pues,querer,quienesquiera,quienquiera,sabes,saben,sabéis,sabemos,saber,siendo,sino,so,sois,somos,soy,sr,sra,sres,sta,tales,tan,tanta,tantas,tenéis,tenemos,tener,tengo,tiempo,tienen,toda,todas,tomar,trabaja,trabajáis,trabajamos,trabajan,trabajar,trabajas,último,ultimo,usas,usáis,usamos,usan,usar,uso,van,vais,valor,vamos,variasos,vaya,verdadera,vosotrasos,voy,ajeno,algúnos,cierto,ello,muchísimo,ningúnos,otro,tanto,trabajo').split(',')
	stopwords.extend([word for word in aditionalWords if word not in stopwords])
	return stopwords

def separateText(text):
	return nltk.word_tokenize(text)

def isWordAfirmative(word):
	listAfirmative = ['mi','mis','afirmativamente','evidentemente','sí','si','claro','talves','talvez','tal','supuesto','obvio','efectivamente','duda','correctamente','acuerdo']
	return True if word in listAfirmative else False

def isWordNegative(word):
	listNegative = ['negativamente','nunca','jamás','jamas','no','ningún','ningun','desacuerdo','jamaz','tampoco']
	return True if word in listNegative else False

def filterSignes(allWords):
	aux= []
	for word in allWords:
		if len(deleteSigne(word))!=0:
			aux.append(word)
	return aux

def islistBreakfast(text):
	listBreakfast = ['desayunar','desayuno','desayunaré','desayunare','desayunarse','desayunito','desayunote','desayunaremos','desayunara','desayunará']
	return True if text in listBreakfast else False

def islistLunch(text):
	listLunch = ['almorzar','almorzare','almorsar','almuerzo','almorzarse','almuercito','almorzaremos','almorzará','almorzara']
	return True if text in listLunch else False

def islistDinner(text):
	listDinner = ['cenar','cena','sena','cenare','cenaré','cenaremos','ceno','cenita','cenota','cenará','cenara']
	return True if text in listDinner else False

def deleteSigne(word):
	return word.replace(',','').replace('-','').replace(';','').replace('.','').replace(':','').replace('*','').replace(':','').replace('_','')


#print(filterSignes(list(clearEmptyWords(separateText("hola , hoy estoy bien pero solo tengo hasta ahora 15 años de edad.")))))