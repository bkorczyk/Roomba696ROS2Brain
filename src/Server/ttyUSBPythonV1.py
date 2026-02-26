import os, pty, socket, select, termios, tty, time 

  

ESP_IP = "192.168.88.103" 

ESP_PORT = 8888 

  

def start_bridge(): 

    master, slave = pty.openpty() 

    s_name = os.ttyname(slave) 

  

    # 1. Ustawiamy tryb surowy 

    tty.setraw(master) 

    tty.setraw(slave) 

     

    # 2. BEZWZGLĘDNE WYŁĄCZENIE ECHA w systemie Linux 

    attrs = termios.tcgetattr(slave) 

    attrs[3] = attrs[3] & ~termios.ECHO 

    termios.tcsetattr(slave, termios.TCSANOW, attrs) 

  

    if os.path.exists("/dev/ttyUSB0"): 

        os.remove("/dev/ttyUSB0") 

    os.symlink(s_name, "/dev/ttyUSB0") 

    os.chmod(s_name, 0o666) 

  

    print(f"[Most Diagnostyczny] Aktywny: /dev/ttyUSB0 -> {ESP_IP}:{ESP_PORT}") 

  

    bytes_to_roomba = 0 

    bytes_from_roomba = 0 

    last_print = time.time() 

  

    while True: 

        try: 

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

            sock.connect((ESP_IP, ESP_PORT)) 

            sock.setblocking(0) 

            print("Polaczono z siecia ESP32!") 

  

            while True: 

                # Dodajemy timeout 1.0s, aby licznik mogl sie wyswietlac na biezaco 

                r, w, e = select.select([master, sock], [], [], 1.0) 

                 

                # Ruch: ROS 2 -> ESP32 

                if master in r: 

                    data = os.read(master, 2048) 

                    if data: 

                        sock.sendall(data) 

                        bytes_to_roomba += len(data) 

                         

                # Ruch: ESP32 -> ROS 2 

                if sock in r: 

                    data = sock.recv(2048) 

                    if data: 

                        os.write(master, data) 

                        bytes_from_roomba += len(data) 

                 

                # Raport liczbowy co 5 sekund 

                if time.time() - last_print >= 5.0: 

                    print(f"[{time.strftime('%H:%M:%S')}] Bilans: Wyslano z ROS2: {bytes_to_roomba} B | Odebrano z ESP32: {bytes_from_roomba} B") 

                    last_print = time.time() 

  

        except Exception as e: 

            print(f"Blad polaczenia: {e}, ponawiam za 2s...") 

            time.sleep(2) 

  

if __name__ == "__main__": 

    start_bridge() 