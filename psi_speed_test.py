import speedtest

s = speedtest.Speedtest()

print('Connection speed test has started.\n')

print('Your download speed is:', (s.download() / 1000000), 'Mbps\n' )
print('Your upload speed is:', (s.upload() / 1000000), 'Mbps\n')

print("The best server in the region has the following properties:    \n")
best_server = s.get_best_server()
for key, value in best_server.items():
    print(key, ' : ', value)
