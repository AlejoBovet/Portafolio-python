import ctypes
import sys
import win32serviceutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def start_service(service_name):
    try:
        win32serviceutil.StartService(service_name)
        print(f'Servicio {service_name} iniciado exitosamente.')
    except Exception as e:
        print(f'Error al iniciar el servicio {service_name}: {e}')
        print(f'Tipo de excepción: {type(e).__name__}')
        print(f'Argumentos de la excepción: {e.args}')

def stop_service(service_name):
    try:
        win32serviceutil.StopService(service_name)
        print(f'Servicio {service_name} detenido exitosamente.')
    except Exception as e:
        print(f'Error al detener el servicio {service_name}: {e}')
        print(f'Tipo de excepción: {type(e).__name__}')
        print(f'Argumentos de la excepción: {e.args}')

def check_service_status(service_name):
    try:
        status = win32serviceutil.QueryServiceStatus(service_name)
        if status[1] == 4:
            print(f'El servicio {service_name} está en ejecución.')
        else:
            print(f'El servicio {service_name} no está en ejecución. Estado: {status[1]}')
    except Exception as e:
        print(f'Error al comprobar el estado del servicio {service_name}: {e}')
        print(f'Tipo de excepción: {type(e).__name__}')
        print(f'Argumentos de la excepción: {e.args}')

def print_menu():
    print("\nMenu:")
    print("1. Verificar estado del servicio")
    print("2. Iniciar servicio")
    print("3. Detener servicio")
    print("4. Salir")

def main():
    if not is_admin():
        print("Este script necesita ejecutarse con privilegios de administrador.")
        sys.exit(1)

    service_name = 'MSSQLSERVER'  # Nombre del servicio de SQL Server

    while True:
        print_menu()
        choice = input("Selecciona una opción: ")

        if choice == '1':
            check_service_status(service_name)
        elif choice == '2':
            start_service(service_name)
        elif choice == '3':
            stop_service(service_name)
        elif choice == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

if __name__ == '__main__':
    main()
