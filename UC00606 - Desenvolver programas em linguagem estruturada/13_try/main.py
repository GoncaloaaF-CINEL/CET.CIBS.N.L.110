import time

def validarIP(ip):
    #logica cool para validar ip

    if ip: # ip valido
        return ip
    else:
        raise Exception("Invalid IP")

try:
    resp = validarIP(False)
    ## code
    ## code

    print(resp)
except Exception:
    print("Invalid IP")

finally:
    time.sleep(10)
    print("finally") # é semper executado


