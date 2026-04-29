import re
import ipaddress
import pandas as pd

txt = "The rain in Sp1ain"
x = re.search("^The.*Sp11ain$", txt)
# print(x)

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
# print(x)



"""

000.000.000.000



((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)
 
"""

txt = "127.0.0.1"
x = re.search("^((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$", txt)

x = re.search("^([0-9]{1,3}.){3}[0-9]{1,3}$", txt)
print(txt)
print("Valido" if x else "invalido")



x = re.search("\d", "dasdsadasdasdasds1dsfsfdsdfdsfsd")
print(x)


ipaddress.ip_address(txt)

df = pd.read_csv("log.csv")
print(df.head())

