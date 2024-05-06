# import socket
#
# def ip_adres():
#     hostname = socket.gethostname()
#     ip_address = socket.gethostbyname(hostname)
#
#     print("Sizning IP-adresingiz: {} ".format(ip_address))
#     print("Kompyuter egasi: {} ".format(hostname))
#
# ip_adres()

##import speedtest module
from speedtest import Speedtest

def tezlikk():
    print("Iltimos ozgina sabrli bo'ling!")

    st = Speedtest()
    down_tezligi = st.download()/1048576

    print("Musaffo osmon ostidagi internet tezligingiz: {:.2f} MB/s\n".format(down_tezligi))

tezlikk()

#ghp_atgQ3yjhjlwDU6QmE
# TQay6NVA90uUy34ri11