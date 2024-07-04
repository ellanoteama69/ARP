import subprocess
import time

def obtener_tabla_arp():
    # Obtiene la tabla ARP del sistema utilizando el comando "arp -a"
    tabla_arp = subprocess.check_output("arp -a", shell=True).decode('utf-8')
    return tabla_arp

def monitorear_tabla_arp(ip_router, mac_esperada):
    try:
        while True:
            # Llama a la función obtener_tabla_arp para obtener la tabla ARP actual
            tabla_arp = obtener_tabla_arp()
            spoofed = False  # Bandera para indicar si se detecta spoofing
            # Recorre cada línea de la tabla ARP
            for line in tabla_arp.splitlines():
                # Verifica si la línea contiene la IP del router
                if ip_router in line:
                    # Imprime la línea para depuración
                    print(f"Línea ARP encontrada: {line}")
                    # Obtiene la dirección MAC actual de la entrada ARP
                    # El formato de la línea de salida del comando "arp -a" puede variar,
                    # por lo que es importante ajustar el índice correcto para obtener la MAC
                    parts = line.split()
                    if len(parts) >= 4:  # Asegura que hay suficientes partes en la línea
                        mac_actual = parts[3]
                        # Compara la dirección MAC actual con la dirección MAC esperada
                        if mac_actual.lower() != mac_esperada.lower():
                            # Imprime una advertencia si las direcciones MAC no coinciden
                            print(f"ADVERTENCIA: ¡Posible ARP spoofing detectado! MAC actual: {mac_actual}, MAC esperada: {mac_esperada}")
                            spoofed = True
            # Si no se detecta spoofing, imprime que la tabla ARP es correcta
            if not spoofed:
                print("La tabla ARP es correcta.")
            # Espera 5 segundos antes de volver a verificar
            time.sleep(5)
    except KeyboardInterrupt:
        # Maneja la interrupción del teclado (Ctrl+C) y detiene el monitoreo
        print("Deteniendo el monitoreo de ARP.")

if __name__ == '__main__':
    # Solicita al usuario la IP del router
    ip_router = input("Ingrese la IP del router: ")
    # Solicita al usuario la dirección MAC esperada del router
    mac_esperada = input("Ingrese la dirección MAC esperada del router: ")
    # Llama a la función monitorear_tabla_arp con los datos ingresados por el usuario
    monitorear_tabla_arp(ip_router, mac_esperada)
