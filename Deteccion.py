import subprocess
import time

def get_arp_table():
    # Obtiene la tabla ARP del sistema utilizando el comando "arp -a"
    # subprocess.check_output ejecuta el comando y devuelve la salida
    arp_table = subprocess.check_output("arp -a", shell=True).decode('utf-8')
    # Retorna la tabla ARP como una cadena de texto decodificada
    return arp_table

def monitor_arp_table(router_ip, expected_mac):
    try:
        while True:
            # Llama a la función get_arp_table para obtener la tabla ARP actual
            arp_table = get_arp_table()
            spoofed = False  # Bandera para indicar si se detecta spoofing
            # Recorre cada línea de la tabla ARP
            for line in arp_table.splitlines():
                # Verifica si la línea contiene la IP del router
                if router_ip in line:
                    # Obtiene la dirección MAC actual de la entrada ARP
                    current_mac = line.split()[1]
                    # Compara la dirección MAC actual con la dirección MAC esperada
                    if current_mac.lower() != expected_mac.lower():
                        # Imprime una advertencia si las direcciones MAC no coinciden
                        print(f"WARNING: Possible ARP spoofing detected! Current MAC: {current_mac}, Expected MAC: {expected_mac}")
                        spoofed = True
            # Si no se detecta spoofing, imprime que la tabla ARP es correcta
            if not spoofed:
                print("ARP table is correct.")
            # Espera 5 segundos antes de volver a verificar
            time.sleep(5)
    except KeyboardInterrupt:
        # Maneja la interrupción del teclado (Ctrl+C) y detiene el monitoreo
        print("Stopping ARP monitoring.")

if __name__ == '__main__':
    # Solicita al usuario la IP del router
    router_ip = input("Ingrese la IP del router: ")
    # Solicita al usuario la dirección MAC esperada del router
    expected_mac = input("Ingrese la dirección MAC esperada del router: ")
    # Llama a la función monitor_arp_table con los datos ingresados por el usuario
    monitor_arp_table(router_ip, expected_mac)
