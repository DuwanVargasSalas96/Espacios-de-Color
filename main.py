# -*- coding: UTF-8 -*-

# Importar
import conversiones as conversion
import menu_creator


# Menú
def menu():
    # Imprimir
    menu_creator.table("Conversión de Espacios de Color", ["1. Conversiones desde YIQ.", "2. Conversiones desde rva.", "3. Conversiones desde YCbCr.", "4. Salir."])

    # Capturar
    opcion = input("> Su opción es: ")

    # Retorno
    return opcion


# Función principal
def main():
	# Bucle
	while (True):
		# Capturar
		opcion = menu()

		# Control conversiones
		if opcion == '1':
			# Imprimir
			menu_creator.header("1. Conversiones desde YIQ")

			# Control
			try:
				# Capturar
				y = float(input("\n> Digite el valor de Y: "))
				i = float(input("> Digite el valor de I: "))
				q = float(input("> Digite el valor de Q: "))

				# Conversiones de formato
				r, v, a = conversion.YIQ_a_rva(y, i, q)
				y, cb, cr = conversion.rva_a_YCbCr(r, v, a)

				# Imprimir
				menu_creator.table("Conversión a rva", ["r = " + str(r), "v = " + str(v), "a = " + str(a)])
				menu_creator.table("Conversión a YCbCr", ["Y = " + str(y), "Cb = " + str(cb), "Cr = " + str(cr)])
			except:
				# Imprimir
				menu_creator.header("Valor ingresado incorrecto, intente nuevamente.")

				# Retorno
				main()
		
		elif opcion == '2':
			# Imprimir
			menu_creator.header("2. Conversiones desde rva")

			# Control
			try:
				# Capturar
				r = float(input("\n> Digite el valor de r: "))
				v = float(input("> Digite el valor de v: "))
				a = float(input("> Digite el valor de a: "))

				# Conversiones de formato
				y, i, q = conversion.rva_a_YIQ(r, v, a)
				_y, cb, cr = conversion.rva_a_YCbCr(r, v, a)

				# Imprimir
				menu_creator.table("Conversión a YIQ", ["Y = " + str(y), "I = " + str(i), "Q = " + str(q)])
				menu_creator.table("Conversión a YCbCr", ["Y = " + str(_y), "Cb = " + str(cb), "Cr = " + str(cr)])
			except:
				# Imprimir
				menu_creator.header("Valor ingresado incorrecto, intente nuevamente.")

				# Retorno
				main()
		
		elif opcion == '3':
			# Imprimir
			menu_creator.header("3. Conversiones desde YCbCr")

			# Control
			try:
				# Capturar
				y = float(input("\n> Digite el valor de Y: "))
				cb = float(input("> Digite el valor de Cb: "))
				cr = float(input("> Digite el valor de Cr: "))

				# Conversiones de formato
				r, v, a = conversion.YCbCr_a_rva(y, cb, cr)
				y, i, q = conversion.rva_a_YIQ(r, v, a)

				# Imprimir
				menu_creator.table("Conversión a rva", ["r = " + str(r), "v = " + str(v), "a = " + str(a)])
				menu_creator.table("Conversión a YIQ", ["Y = " + str(y), "I = " + str(i), "Q = " + str(q)])
			except:
				# Imprimir
				menu_creator.header("Valor ingresado incorrecto, intente nuevamente.")

				# Retorno
				main()

		elif opcion == '4':
			# Imprimir
			menu_creator.header("Saliendo...")
			
			# Salir
			exit()
		else:
			# Imprimir
			menu_creator.header("Opción invalida. Intente nuevamente")

			# Retorno
			main()


# Ejecucion
main()