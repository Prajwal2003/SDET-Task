from browsermobproxy import Server

bmp_path = "/Users/starkz/Downloads/browsermob-proxy-2.1.4/bin/browsermob-proxy"
server = Server(bmp_path)
server.start()
proxy = server.create_proxy()

print(f"Proxy started at {proxy.proxy}")
proxy.new_har("example", options={"captureHeaders": True, "captureContent": True})
ssl_cert_url = f"http://localhost:8086/proxy/{proxy.proxy}/download-ssl-cert"
print(ssl_cert_url)
