import utils
import email_validator as val

tp = (12,11)

print(tp)
print(tp[0])
print(tp[1])

print(type(tp))



teste = set(tp)
print(teste)

print(utils.idIpValid("127.0.0.1"))
print(utils.idIpValid("127.0.2.1"))
print(utils.idIpValid("256.0.0.1"))

print(val.validate_email("1n#eyekow107@sapo.pt"))

