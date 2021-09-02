#address.py

def ipv4_bin(ip):
	r"""Convert IPv4 address to binary representation"""

	return ''.join([bin(int(_)+256)[3:] for _ in ip.split('.')])

def ipv6_bin(ip):
	r"""Convert IPv6 address to binary representation"""

	return ''.join([bin(int(_, 16)+65536)[3:] for _ in ipv6_unpack(ip)])

def ipv6_unpack(ipv6):
	r"""Convert IPv6 address to form with explicit zeros"""

	ipv6 = ipv6.split(':')
	i = ipv6.index('')
	ipv6[i] = '0'
	for _ in range(8-len(ipv6)):
		ipv6.insert(i, '0')
	return ipv6

def bin_ipv4(ip):
	r"""Convert binary address to decimal IPv4 form"""

	return '.'.join([str(int(ip[i:i+8], 2)) for i in range(0, len(ip), 8)])

def bin_ipv6(ip):
	r"""Convert binary address to hexadecimal IPv6 form"""

	return ':'.join([str(hex(int(ip[i:i+16], 2)))[2:] for i in range(0, len(ip), 16) if int(ip[i:i+16], 2)!=0]) + '::'

def common_prefix(s1, s2, bitmask=129):
	r"""Finds longest common prefix's length"""
	
	l = len(s1)

	if bitmask < l:
		l = bitmask

	while s1[:l] != s2[:l]:
		l -= 1

	if l < bitmask:
		bitmask = l

	return bitmask

def ipv4_test():
	ip_list =  ['192.168.1.2', 
				'192.168.1.3',
				'192.168.1.5']
	bin_list = [ipv4_bin(ip) for ip in ip_list]
	bin_list.sort()
	bitmask = common_prefix(bin_list[0], bin_list[-1])
	common_subnet = bin_list[0][:bitmask] + '0' * (32 - bitmask)
	print(bin_ipv4(common_subnet), '/', bitmask, sep='')


def ipv6_test():
	ip_list =  ['ffe0::1:0:0:0',
				'ffe0::2:0:0:0',
				'ffe0::4:0:0:0',
				'ffe0::8:0:0:0',
				'ffe0::10:0:0:0',
				'ffe0::20:0:0:0',
				'ffe0::40:0:0:0',
				'ffe0::80:0:0:0',]
	bin_list = [ipv6_bin(ip) for ip in ip_list]
	bin_list.sort()
	bitmask = common_prefix(bin_list[0], bin_list[-1])
	common_subnet = bin_list[0][:bitmask] + '0' * (bitmask // 16)
	print(bin_ipv6(common_subnet), '/', bitmask, sep='')

if __name__ == '__main__':
	ipv4_test()	
	ipv6_test()