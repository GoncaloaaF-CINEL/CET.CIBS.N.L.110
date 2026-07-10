
linha = "[10.30 16:49:07] chrome.exe - proxy.cse.cuhk.edu.hk:5070 open through proxy proxy.cse.cuhk.edu.hk:5070 HTTPS"

def tratar_linha(linha:str, ano:int=2015):
    # encontrar ]
    fim_data = linha.find("]") # diz me o idx da 1 ocur de ]
    #print(fim_data)
    data = linha[1:fim_data].strip() # data  txt[n:m] -> n a m-1
    data = f"{ano}.{data}"

    # print("Data:", data)
    linha = linha[fim_data+1:].lstrip()
    #print(linha)

    fim_app = linha.find(" - ")

    # print(fim_app)
    app = linha[:fim_app].strip() # app  # strip - > remover espaços no final
    # print("App:" , app)

    linha = linha[fim_app + 1:].lstrip(" -") # lstrip -> removes espaços no inicio
    # print(linha)

    fim_url_port = linha.find(" ")

    url_port = linha[:fim_url_port].strip().lstrip()
    # print("url_port:",url_port)

    linha = linha[fim_url_port:].lstrip()
    #print(linha)

    fim_status = linha.find(" ")
    # status = linha[:fim_status]
    # print(status)
    status = linha[:fim_status].lstrip().strip(",") # -> remove o char
    # print("status:", status)

    msg = linha[fim_status:].lstrip(" :")
    # print("msg:", msg)

    return f"{data};{app};{url_port};{status};{msg.lstrip()}"


"""

[07.26 15:38:33] MobaXterm.exe - 183.62
[07.26 15:39:37] git-remote-https.exe - proxy

    fim_app = linha.find(" - ") 
    app = linha[:fim_app].strip() # app  # strip - > remover espaços no final
"""

linha = "[07.26 15:39:37] git-remote-https.exe - proxy.cse.cuhk.edu.hk:5070 open through proxy proxy.cse.cuhk.edu.hk:5070 HTTPS"
# linha = "[10.30 16:49:07] chrome.exe - proxy.cse.cuhk.edu.hk:5070 open through proxy proxy.cse.cuhk.edu.hk:5070 HTTPS"
# linha = "[10.30 20:57:23] chrome.exe - proxy.cse.cuhk.edu.hk:5070 close, 2798 bytes (2.73 KB) sent, 15599 bytes (15.2 KB) received, lifetime 04:05"
# linha = "[10.30 20:55:49] YodaoDict.exe - oimagea5.ydstatic.com:80 error : A connection request was canceled before the completion. "
print(tratar_linha(linha))