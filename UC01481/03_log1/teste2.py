


def splitLog(msg):
    fim_data = msg.find("]")
    # print(msg[15])
    data = msg[1:15]

    # print(data)
    msg = msg[fim_data + 1:].lstrip()
    aux = msg.split(" - ")
    app = aux[0]
    msg = aux[1]
    # print(app)

    fim_proxy_port = msg.find(" ")
    proxy_port = msg[:fim_proxy_port]
    # print(proxy_port)
    msg = msg[fim_proxy_port + 1:].lstrip()
    # print(msg)

    # evento
    fim_evento = msg.find(" ")
    evento = msg[:fim_evento].lstrip().rstrip(",")

    # print(evento)
    msg = msg[fim_evento + 1:].lstrip(":").lstrip()
    # print(msg)

    return data,app, proxy_port, evento, msg


msg = "[10.30 16:49:06] chrome.exe - proxy.cse.cuhk.edu.hk:5070 open through proxy proxy.cse.cuhk.edu.hk:5070 HTTPS"
msg = "[07.26 17:23:51] WeChat.exe - 223.167.104.147:80 error : Could not connect to proxy proxy.cse.cuhk.edu.hk:5070 - Could not resolve proxy.cse.cuhk.edu.hk error 11001"
msg = "[10.30 16:49:07] chrome.exe - proxy.cse.cuhk.edu.hk:5070 close, 0 bytes sent, 0 bytes received, lifetime 00:01"



print(splitLog(msg))


"""
data = []
with open("Proxifier_2k.log", "r") as f:
    data = f.readlines()

for linha in data:
    print(splitLog(linha.strip()))

"""

