import socket
from dtls.wrapper import wrap_server
from os import path
from coapthon.server.coap import CoAP as CoAPServer
from resources import Temperature, Humidity, Pressure
import time
from logging import basicConfig, DEBUG, getLogger, root, Filter
basicConfig(level=DEBUG, format="%(asctime)s - %(threadName)-30s - %(name)s - %(levelname)s - %(message)s")
_logger = getLogger(__name__)


def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serversocket.settimeout(300)
    cert_path = path.join(path.abspath(path.dirname(__file__)), "certs")
    host_address = ("212.201.8.88", 6657)

    # Create a server side DTLS socket
    dtls_sock = wrap_server(serversocket,
                            keyfile=path.join(cert_path, "keycert.pem"),
                            certfile=path.join(cert_path, "keycert.pem"),
                            ca_certs=path.join(cert_path, "ca-cert.pem"), )
    dtls_sock.bind(host_address)
    dtls_sock.listen(1)
    print ("Waiting for CoAP Client to Connect ..")

    # Connect the Listening DTLS socket to CoAP
    server = CoAPServer(host_address, sock=dtls_sock)
    server.add_resource('temperature/', Temperature())
    server.add_resource('humidity/', Humidity())
    server.add_resource('pressure/', Pressure())
    print("CoAP Server start on " + host_address[0] + ":" + str(host_address[1]))
    while True:
        time.sleep(0.5)
        try:
            server.listen(1)
        except KeyboardInterrupt:
            print "Server Shutdown"
            server.close()
            print "Exiting..."


if __name__ == "__main__":
    main()
