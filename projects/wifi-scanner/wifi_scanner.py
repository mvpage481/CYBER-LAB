import nmap
import csv

def scan_network(network="192.168.1.0/24"):
    print(f"🔍 Escaneando red: {network}\n")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=network, arguments='-sn')
    results = []

    for host in scanner.all_hosts():
        if scanner[host].state() == "up":
            hostname = scanner[host].hostname()
            results.append((host, hostname))

    if results:
        with open("scan_results.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["IP", "Nombre del host"])
            writer.writerows(results)
        print(f"✅ Se guardaron {len(results)} resultados en scan_results.csv")
    else:
        print("⚠️ No se encontraron dispositivos activos.")

if __name__ == "__main__":
    scan_network()
