# Vinicius Gabriel Machado - GRR20182552 - Bacharelado em Ciencia da Computacao

from scapy.all import *

#################################################

n_packets = 0
ip_packets = 0
tcp_packets = 0
udp_packets = 0
tcp_sessions = 0
udp_sessions = 0
not_ip_packets = 0

dictionary = {
  'TCP': {},
  'UDP': {}
}

#################################################

data = rdpcap('trace.pcap')

# data.summary()

for packet in data:
  n_packets += 1
  
  if packet.getlayer('IP'):
    ip_packets += 1

    ip_src=packet[IP].src
    ip_dst=packet[IP].dst

    if packet.getlayer('TCP'):
      tcp_packets += 1
      tcp_sport=packet[TCP].sport
      tcp_dport=packet[TCP].dport
      if str(ip_src) + ':' + str(tcp_sport) + '-' + str(ip_dst) + ':' + str(tcp_dport) in  dictionary['TCP']:
        dictionary['TCP'][str(ip_src) + ':' + str(tcp_sport) + '-' + str(ip_dst) + ':' + str(tcp_dport)].append(packet.getlayer('TCP').payload)
      else:
        dictionary['TCP'][str(ip_src) + ':' + str(tcp_sport) + '-' + str(ip_dst) + ':' + str(tcp_dport)] = []
      # dictionary['TCP'][str(ip_src) + ':' + str(tcp_sport) + '-' + str(ip_dst) + ':' + str(tcp_dport)] = 0

    if packet.getlayer('UDP'):
      udp_packets += 1
      udp_sport=packet[UDP].sport
      udp_dport=packet[UDP].dport
      if str(ip_src) + ':' + str(udp_sport) + '-' + str(ip_dst) + ':' +str(udp_dport) in dictionary['UDP']:
        dictionary['UDP'][str(ip_src) + ':' + str(udp_sport) + '-' + str(ip_dst) + ':' +str(udp_dport)].append(packet.getlayer('UDP').payload)
      else:
        dictionary['UDP'][str(ip_src) + ':' + str(udp_sport) + '-' + str(ip_dst) + ':' +str(udp_dport)] = []
      # dictionary['UDP'][str(ip_src) + ':' + str(udp_sport) + '-' + str(ip_dst) + ':' +str(udp_dport)] = 0

  else:
    not_ip_packets += 1

tcp_sessions = len(dictionary['TCP'])
udp_sessions = len(dictionary['UDP'])

print('O arquivo "trace.pcap" possui:')
print(str(n_packets) + ' pacotes no total')
print(str(ip_packets) + ' pacotes IP')
print(str(tcp_packets) + ' pacotes TCP')
print(str(udp_packets) + ' pacotes UDP')
print(str(tcp_sessions) + ' sessoes TCP')
print(str(udp_sessions) + ' sessoes UDP')
print(str(not_ip_packets) + ' pacotes nao-IP')