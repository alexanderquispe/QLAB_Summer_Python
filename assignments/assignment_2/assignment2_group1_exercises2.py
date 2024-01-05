# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 17:15:30 2023

@author: Daniela
"""

#LISTS
##1
###We could not get the result of this exercise. Here, we show the different paths we tried.
import numpy as np
f_list = [np.nan , np.nan, "Austria", "Germany", np.nan, "Pakistan", "np.nan", np.nan ]
f_list.index(str('nan'))
f_list.index(str(item)=='nan')
f_list.index(str(values)=="nan")
s1=[item for item in f_list if str (item) !='nan']
np.argwhere(np.isnan(f_list))
np.argwhere(f_list)
type(f_list)
###We just were able to eliminate the elements np.nan.
f_list=[item for item in f_list if str (item) !='nan']
print(f_list)
###Here is the f-string, that would have been used in case we had arrived the result.
F'The indices {index} have np.nan values'

##2
###We create the list "p2_list"
p2_list = [ 2 , 3, 4, 5 ] 
###We multiply it by 4
p2_list*4

##3
###f_list is already created, so we use the lenght function
print(len(f_list))
###The size of the list is of 8 values.

##4
###We create the list "text_1" and we join it to form a whole sentence
text1=['My', 'teacher', 'assistant', 'is', 'so', 'boring.']
text1join=" ".join(text1)
print(text1join)

##5
###We create the list of text2 so it can be more easy to extend the "text1"
text2= [' but is very funny.']
###We create an empty list, so it can be easier. Here we will put both lists "text1" and "text2".
textsum = []
textsum.extend(text1)
textsum.extend(text2)
###We join all the values of the list
textsum=" ".join(textsum)
###We replace some strings, so the text is exactly what was asked.
textsum=textsum.replace("teacher assistant", "TA")
textsum=textsum.replace("boring.", "boring,")

print(textsum)

##6
###We create the list
values1 = [ 86, 86, 85, 85, 85, 83, 23, 0, 84, 1 ] 
###We use the function max and min to get the values required
numbermax = max(values1)
numbermin=min(values1)
###We locate these results at the list
indexmax=values1.index(86)
indexmin=values1.index(0)
###Here are the fstrings, were the values will be replaced by the results
print(F'The max value of values1 is {numbermax} and is located in the {indexmax} index.')
print(F'The min value of values1 is {numbermin} and is located in the {indexmin} index.')

##7
###We create the list "last_and_name"
last_and_name = [ "CORNEJO SANCHEZ, CHRISTIAN SANTOS", "ORELLANA QUISPE, CRISTIAN NASSER", "MORALES CHOQUEHUANCA, ANGELICA KARINA", "GUIMARAY RIBEYRO, JOSE ROBERTO", "CAMACHO GAVIDIA, ABEL FERNANDO", "TINTAYA ORIHUELA, MEIR ALVARO", "CHAVEZ MARTINEZ, JOSELIN ALEXANDRA", "FIGUEROA MURO, LEONEL ARTURO", "GOMEZ CRIBILLERO, JOSE FELIPE", "PALOMINO SEGUÍN, AFRANIA", "LUZON CUEVA, BIANCA MARIETTE", "SUAÑA ZEGARRA, ADRIAN ANDRE", "SOTO POMACHAGUA, DORKAS YOMIRA JHERMY", "FIORENTINO MARTINEZ, LADY ALY", "LAMA MAVILA, HECTOR ANDRE", "MEZA HINOJO, GUSTAVO", "LOZADA MURILLO, PERSEO MARCELO", "ZAMBRANO JIMENEZ, MIGUEL ALONZO", "JACOBS LUQUE, NICOLAS", "VIDAL VIDAL, ROCIO GABRIELA", "TORRES ANICAMA, JANE CAMILA", "LOPEZ ESTRADA, MARIA ELISA", "BOYCO ORAMS, ALEJANDRO", "DIAZ BERROSPI, KARLINE ROSMELI", "RIEGA ESCALANTE, STEPHY ROSARIO", "LEVANO TORRES, VALERIA CECILIA", "ESQUIVES BRAVO, SEBASTIAN RENATO", "PEREZ GONZALES, JUAN CARLOS", "OTERO MAGUIÑA, MARIANA", "CLAVO CAMPOS, ANDREA BRIZETH", "AGUILAR GARCIA, ERICK JOSUE", "CALDAS VELASQUEZ, JOSUE DANIEL", "SALAS NUÑEZ BORJA, FABIO MANUEL", "PIZARRO VILLANES, FERNANDA NICOLLE", "QUILLATUPA MORALES, ANGELA ADELINA", "HUANCAYA IDONE, CESAR DANTE", "CALVO PORTOCARRERO, GABRIELA ISABEL", "IBAÑEZ ABANTO, ANGEL MAURICIO", "MELÉNDEZ APONTE, JUAN DIEGO", "CRISTIAN SERRANO, ARONE", "HINOJOSA CAHUANA, PERCY ALBERTH", "ANGLAS GARCÍA, KEVIN ARTURO", "ALDAVE ACOSTA, CESAR ERNESTO", "NÚÑEZ HUAMÁN, CÉSAR AGUSTO", "OBREGON HUAMAN, DIANA EDITH", "SOTO PACHERRES, RODRIGO FRANCO", "INGARUCA RIVERA, GRETTEL ALEXANDRA", "ROJAS HUAMAN, ROSA ANGELA", "NEYRA SALAS, DANTE OMAR", "HUERTA ESPINOZA, YAJAIRA ALEXANDRA", "HUANCA MARTINEZ, JORGE ALBERTO", "FLORES CADILLO, ALEXIS" ]
###We have selected the comma to separate the values, and we use function split
last_and_name=[item.split(',') for item in last_and_name ]
###Now, the function map identify two lists, that we name "last_names" and "names". 
last_names, names = map(list, zip(*last_and_name))
###We print both results
print(names)
print(last_names)

##8
###We create the list "emails"
emails = ["cscornejo@pucp.edu.pe", "orellana.cn@pucp.edu.pe", "karina.morales@pucp.edu.pe", "a20083223@pucp.pe", "abel.camacho@pucp.pe", "mtintaya@pucp.edu.pe", "joselin.chavez@pucp.edu.pe", "a20105737@pucp.pe", "jfgomezc@pucp.pe", "afrania.palomino@pucp.pe", "luzon.bianca@pucp.pe", "adrian.suanaz@pucp.pe", "soto.y@pucp.edu.pe", "a20132766@pucp.pe", "andre.lama@pucp.edu.pe", "gustavo.meza@pucp.edu.pe", "pmlozada@pucp.edu.pe", "m.zambranoj@pucp.edu.pe", "nicolas.jacobs@pucp.edu.pe", "gvidal@pucp.edu.pe", "jane.torres@pucp.edu.pe", "m.lopez@pucp.edu.pe", "alejandro.boyco@pucp.edu.pe", "a20167070@pucp.edu.pe", "riega.stephy@pucp.edu.pe", "vlevanot@pucp.edu.pe", "sesquives@pucp.edu.pe", "perez.juanc@pucp.edu.pe", "mariana.otero@pucp.edu.pe", "aclavo@pucp.edu.pe", "a20182474@pucp.edu.pe", "josue.caldas@pucp.edu.pe", "fabio.salas@pucp.edu.pe", "fernanda.pizarro@pucp.edu.pe", "aquillatupa@pucp.pe", "", "", "", "", "", "f0873079@pucp.edu.pe", "", "", "", "", "", "", "", "", "", "", "flores.alexis@pucp.edu.pe", ]
###We use the function zip to join both lists (last_names, used above, and emails)
emailsnames=list( zip( emails , last_names ) )
###We print the result
print(emailsnames)
###We create a list with just the lastnames that don't have a corresponding email.
notemail=[item[1] for item in emailsnames if item[0]=='']
###With the print, we can see the lastnames of the students that don't have email.
print(notemail)