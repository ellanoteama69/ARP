# ARP Spoofing y Detección

Este repositorio contiene scripts para realizar y detectar ataques de ARP spoofing en una red local.

## Requisitos

- Python 3.x
- Scapy (solo en la máquina atacante)

### Instalar Scapy en la Máquina Atacante

#### Verificar que ambas maquinas esten conectadas en la misma red y verificar que ambos esten en el mismo router

- Obtener IP y MAC del router

##### Ejecutar el codigo de ARP Spoofing

- Obtener en otra instancia los datos de la maquina atacante como la ip y la direccion mac
- Ingresar los datos solicitados en la maquina atacante

- ###### Ejecutar el codigo de deteccion
- ejecutar arp -a para ver la direccion del router
- obtener los datos de la maquina victima
- ingresar los datos solicitados
- una vez en funcionamiento volver a ejecutar en otra instancia arp -a y ver los cambios

