meyveler1=['Elma','Nar','Portakal','Muz','Goz']#list
meyveler2=('Nar','Portakal','Muz','Goz','Elma')#tuple
print(meyveler1)
print(meyveler2)

print("Dizi uzunluğu: ",len(meyveler1))

meyveler1.append("Dut")
meyveler2+=("Dut",)
print(meyveler1)
print(meyveler2)   

print(type('Elma'))

abc={"ad":"Ali","tel":"05425516537",44:"aaa",55:23}
print(abc)

print("1 indexli eleman:",meyveler1[1])
print("ad keyli eleman:",abc["ad"])
print("44 keyli eleman:",abc[44])
print("55 keyli eleman:",abc[55])