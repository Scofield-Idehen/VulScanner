import port_scan

target_ip = input('[+] + Enter Target to scan for Vul open Port: ')
port_num = int(input('[+] + Enter Number of ports you wish to scan - first 500 ports'))
Vul_file = input('[+] + Enter Path to the File with Vul Software')
print('\n')

target = port_scan.portscan(target_ip, port_num)
target.scan()

with open(Vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(target.open_port[count]))

        count += 1