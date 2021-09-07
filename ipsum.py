import sys

def common_prefix(s1: str, s2: str) -> int:
	"""Binary search of fullest common prefix's length for two strings.
	Accordingly to IP addresses common prefix length
	is the same as bitmask length.
	"""
	
	r: int = len(s1) - 1
	l: int = 0

	while r - l > 1:
		m: int = (l + r) // 2
		if s1[:m+1] == s2[:m+1]:
			l = m
		else:
			r = m

	return r


def ipv4_summarize(ip_list: list[str]) -> str:
	"""Summarization IPv4 addresses."""

	def ipv4_bin(ip: str) -> str:
		"""Convert IPv4 address to binary representation."""

		return ''.join([bin(int(_)+256)[3:] for _ in ip.split('.')])

	def bin_ipv4(ip: str) -> str:
		"""Convert binary address to decimal IPv4 form."""

		return '.'.join([str(int(ip[i:i+8], 2)) for i in range(0, len(ip), 8)])

	bin_list: list = [ipv4_bin(ip) for ip in ip_list]
	bin_list.sort()
	bitmask: int = common_prefix(bin_list[0], bin_list[-1])
	common_subnet: str = bin_list[0][:bitmask] + '0' * (32 - bitmask)
	return bin_ipv4(common_subnet) + '/' + str(bitmask)


def ipv6_summarize(ip_list: list[str]) -> str:
	"""Summarization IPv6 addresses."""

	def ipv6_bin(ip: str) -> str:
		"""Convert IPv6 address to binary representation."""

		return ''.join([bin(int(_, 16)+65536)[3:] for _ in ipv6_unpack(ip)])

	def ipv6_unpack(ipv6: str) -> list[str]:
		"""Convert IPv6 address to form with explicit zeros."""

		ipv6_full: list = ipv6.split(':')

		if ipv6_full[-1] == '':
			del ipv6_full[-1]

		i: int = ipv6_full.index('')
		ipv6_full[i] = '0'
		for _ in range(8-len(ipv6_full)):
			ipv6_full.insert(i, '0')
		return ipv6_full

	def bin_ipv6(ip: str) -> str:
		"""Convert binary address to hexadecimal IPv6 form."""

		return ':'.join([str(hex(int(ip[i:i+16], 2)))[2:] \
			for i in range(0, len(ip), 16) if int(ip[i:i+16], 2)!=0]) + '::'

	bin_list: list = [ipv6_bin(ip) for ip in ip_list]
	bin_list.sort()
	bitmask: int = common_prefix(bin_list[0], bin_list[-1])
	common_subnet: str = bin_list[0][:bitmask] + '0' * (bitmask // 16)
	return bin_ipv6(common_subnet) + '/' + str(bitmask)

def ipv4_test():
	ipv4_list = ['192.168.1.2', 
				 '192.168.1.3',
				 '192.168.1.5']
	print(ipv4_summarize(ipv4_list))

def ipv6_test():
	ipv6_list = ['ffe0::1:0:0:0',
				 'ffe0::2:0:0:0',
				 'ffe0::4:0:0:0',
				 'ffe0::8:0:0:0',
				 'ffe0::10:0:0:0',
				 'ffe0::20:0:0:0',
				 'ffe0::40:0:0:0',
				 'ffe0::80:0:0:0',]
	print(ipv6_summarize(ipv6_list))


def main():
	path: str = sys.argv[1]
	version: str = sys.argv[2]
	ip_list: list = open(path, 'r').read().split()

	if version == 'v4':
		print('Result net:', ipv4_summarize(ip_list))
	elif version == 'v6':
		print('Result net:', ipv6_summarize(ip_list))


if __name__ == '__main__':
	main()