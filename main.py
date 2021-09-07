# -*- coding: UTF-8 -*-

#Conversiones YIQ
def convertir_yiq_a_rva(y, i, q):
  #Conversion a rva
  r = y + 0.955 * i + 0.618 * q
  v = y - 0.271 * i - 0.645 * q
  a = y - 1.11 * i + 1.7 * q
  
  #Retorno
  return r, v, a

def convertir_yiq_a_ycbcr(y, i, q):
  #Conversion a rva
  r = convertir_yiq_a_rva(y, i, q)[0]
  v = convertir_yiq_a_rva(y, i, q)[1]
  a = convertir_yiq_a_rva(y, i, q)[2]
  
  #Conversion a YCbCr
  y = convertir_rva_a_ycbcr(r, v, a)[0]
  cb = convertir_rva_a_ycbcr(r, v, a)[1]
  cr = convertir_rva_a_ycbcr(r, v, a)[2]
  
  #Retorno
  return y, cb, cr

#Conversiones rva
def convertir_rva_a_yiq(r, v, a):
  #Conversion a YIQ
  y = 0.299 * r + 0.587 * v + 0.114 * a
  i = 0.596 * r - 0.275 * v - 0.321 * a
  q = 0.212 * r - 0.528 * v + 0.311 * a
  
  #Retorno
  return y, i, q

def convertir_rva_a_ycbcr(r, v, a):
  #Conversion a YCbCr
  y = 0.299 * r + 0.587 * v + 0.114 * a
  cb = 0.1687 * r - 0.3313 * v - 0.5 * a
  cr = 0.5 * r - 0.418 * v + 0.0813 * a
  
  #Retorno
  return y, cb, cr

#Conversiones ycbcr
def convertir_ycbcr_a_yiq(y, cb, cr):
  #Conversion a rva
  r = convertir_ycbcr_a_rva(y, cb, cr)[0]
  v = convertir_ycbcr_a_rva(y, cb, cr)[1]
  a = convertir_ycbcr_a_rva(y, cb, cr)[2]
  
  #Conversion a YIQ
  y = convertir_rva_a_yiq(r, v, a)[0]
  i = convertir_rva_a_yiq(r, v, a)[1]
  q = convertir_rva_a_yiq(r, v, a)[2]
  
  #Retorno
  return y, i, q

def convertir_ycbcr_a_rva(y, cb, cr):
  #Convertir a rva
  r = y + 1.402 * cr
  v = y + 0.344 * cb - 0.714 * cr
  a = y + 1.772 * cb
  
  #Retorno
  return r, v, a

#Funcion principal
def main():
  #lectura espacio de color YIQ 
  print("Espacio de color YIQ")
  y = float(input("Digite el valor de Y: "))
  i = float(input("Digite el valor de I: "))
  q = float(input("Digite el valor de Q: "))

  #lectura espacio de color RVA
  print("\nEspacio de color rva")
  r = float(input("Digite el valor de r: "))
  v = float(input("Digite el valor de v: "))
  a = float(input("Digite el valor de a: "))

  #lectura espacio de color YCbCr 
  print("\nEspacio de color YCbCr")
  y = float(input("Digite el valor de Y: "))
  cb = float(input("Digite el valor de Cb: "))
  cr = float(input("Digite el valor de Cr: "))

  #Converiones YIQ
  rva = convertir_yiq_a_rva(y, i, q)
  ycbcr = convertir_yiq_a_ycbcr(y, i, q)
  #Imprimir
  print("\nDesde YIQ")
  print("La conversión a rva es: r =", rva[0], ", v =", rva[1], ", a =", rva[2])
  print("La conversión a YCbCr es: Y =", ycbcr[0], ", Cb=", ycbcr[1],", Cr =", ycbcr[2])

  #Conversiones rva
  ycbcr = convertir_rva_a_ycbcr(r, v, a)
  yiq = convertir_rva_a_yiq(r, v, a)
  #Imprimir
  print("\nDesde rva")
  print("La conversion a YCbCr es: Y =", ycbcr[0], ", Cb =", ycbcr[1], ", Cr =", ycbcr[2])
  print("La conversion a YIQ es: Y =", yiq[0], ", I =", yiq[1], ", Q =", yiq[2])
  
  #Conversiones YCbCr
  rva = convertir_ycbcr_a_rva(y, cb, cr)
  yiq = convertir_ycbcr_a_yiq(y, cb, cr)
  #Imprimir
  print("\nDesde YCbCr")
  print("La conversión a rva es: r =", rva[0], ", v =", rva[1], ", a =", rva[2])
  print("La conversión a YIQ es: Y =", yiq[0], ", I =", yiq[1], ", Q =", yiq[2])

#Ejecucion
main()