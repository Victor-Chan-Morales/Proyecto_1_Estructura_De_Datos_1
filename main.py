from flota_vehiculos import FlotaVehiculos

def main():
    flota = FlotaVehiculos()

    while True:
        print("\n--- Menú de Gestión de Flota de Vehículos ---")
        print("1. Registrar un vehículo")
        print("2. Eliminar un vehículo")
        print("3. Buscar un vehículo")
        print("4. Listar todos los vehículos")
        print("5. Agregar mantenimiento a un vehículo")
        print("6. Eliminar mantenimiento de un vehículo")
        print("7. Mostrar historial de mantenimientos de un vehículo")
        print("8. Calcular costo total de mantenimientos de un vehículo")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                print("\nRegistrar un vehículo:")
                placa = input("Placa: ")
                marca = input("Marca: ")
                modelo = input("Modelo: ")
                año = int(input("Año: "))
                kilometraje = float(input("Kilometraje: "))
                flota.registrar_vehiculo(placa, marca, modelo, año, kilometraje)
                print("Vehículo registrado exitosamente.")

            elif opcion == "2":
                print("\nEliminar un vehículo:")
                placa = input("Placa del vehículo a eliminar: ")
                flota.eliminar_vehiculo(placa)
                print("Vehículo eliminado exitosamente.")

            elif opcion == "3":
                print("\nBuscar un vehículo:")
                placa = input("Placa del vehículo a buscar: ")
                vehiculo = flota.buscar_vehiculo(placa)
                print(f"Vehículo encontrado: {vehiculo.marca} {vehiculo.modelo}, Año: {vehiculo.año}, Kilometraje: {vehiculo.kilometraje}")

            elif opcion == "4":
                print("\nListar todos los vehículos:")
                flota.listar_vehiculos()

            elif opcion == "5":
                print("\nAgregar mantenimiento a un vehículo:")
                placa = input("Placa del vehículo: ")
                vehiculo = flota.buscar_vehiculo(placa)
                fecha = input("Fecha del mantenimiento (YYYY-MM-DD): ")
                descripcion = input("Descripción del servicio: ")
                costo = float(input("Costo del mantenimiento: "))
                vehiculo.agregar_mantenimiento(fecha, descripcion, costo)
                print("Mantenimiento agregado exitosamente.")

            elif opcion == "6":
                print("\nEliminar mantenimiento de un vehículo:")
                placa = input("Placa del vehículo: ")
                vehiculo = flota.buscar_vehiculo(placa)
                fecha = input("Fecha del mantenimiento a eliminar (YYYY-MM-DD): ")
                vehiculo.eliminar_mantenimiento(fecha)
                print("Mantenimiento eliminado exitosamente.")

            elif opcion == "7":
                print("\nMostrar historial de mantenimientos de un vehículo:")
                placa = input("Placa del vehículo: ")
                vehiculo = flota.buscar_vehiculo(placa)
                vehiculo.mostrar_historial()

            elif opcion == "8":
                print("\nCalcular costo total de mantenimientos de un vehículo:")
                placa = input("Placa del vehículo: ")
                vehiculo = flota.buscar_vehiculo(placa)
                costo_total = vehiculo.costo_total_mantenimientos()
                print(f"Costo total de mantenimientos: {costo_total}")

            elif opcion == "9":
                print("Saliendo del programa...")
                break

            else:
                print("Opción no válida. Intente de nuevo.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()