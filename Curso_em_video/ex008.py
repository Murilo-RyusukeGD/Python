medida = float(input("Uma distância em metros: "))

print ("A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm".format(medida, medida/1000, medida/100, medida/10, medida*10, medida*100, medida*1000))