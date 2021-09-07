import sys

from typing import List

def common_prefix(s1: str, s2: str) -> int:
	"""Binary search of fullest common prefix"s length for two strings.
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


def ipv4_summarize(ip_list: List[str]) -> str:
	"""Summarization IPv4 addresses."""

	def is_valid_ipv4(ipv4: str) -> bool:
		"""True if IPv4 is valid, else returns False."""

		octets: List[str] = str(ipv4).split(".")
		
		if len(octets) == 4:
			for octet in octets:
				if not octet.isdigit():
					return False
			
				tmp = int(octet)
				if 0 > tmp or tmp > 255:
					return False
		
			return True
		return False

	def ipv4_bin(ipv4: str) -> str:
		"""Convert IPv4 address to binary representation."""

		if not is_valid_ipv4(ipv4):
			raise ValueError(f"Incorrect IPv4 address: {ipv4}")

		return "".join([bin(int(_)+256)[3:] for _ in ipv4.split(".")])

	def bin_ipv4(ip: str) -> str:
		"""Convert binary address to decimal IPv4 form."""

		return ".".join([str(int(ip[i:i+8], 2)) for i in range(0, len(ip), 8)])

	if len(ip_list) == 1 and is_valid_ipv4(ip_list[0]):
		return ip_list[0]

	bin_list: list = [ipv4_bin(ip) for ip in ip_list]
	bin_list.sort()
	bitmask: int = common_prefix(bin_list[0], bin_list[-1])
	common_subnet: str = bin_list[0][:bitmask] + "0" * (32 - bitmask)
	return bin_ipv4(common_subnet) + "/" + str(bitmask)


def ipv6_summarize(ip_list: List[str]) -> str:
	"""Summarization IPv6 addresses."""

	def is_valid_ipv6(ipv6: str) -> bool:
		"""True if IPv6 is valid, else returns False."""

		octets: List[str] = str(ipv6).split(":")
		double_colon: int = 0

		for octet in octets:
			if octet == "":
				double_colon += 1
				continue

			if not all(d in '0123456789abcdefABCDEF' for d in octet):
				return False

			tmp = int(octet, 16)
			if 0 > tmp or tmp > 65535:
				return False

		if double_colon > 1:
			return False

		return True

	def ipv6_unpack(ipv6: str) -> List[str]:
		"""Convert IPv6 address to form with explicit zeros."""

		if not is_valid_ipv6(ipv6):
			raise ValueError(f"Incorrect IPv6 address: {ipv6}")
		
		octets: List[str] = ipv6.split(":")

		if "" in octets:
			if octets[-1] == "":
				del octets[-1]

			i: int = octets.index("")
			octets[i] = "0"
			for _ in range(8-len(octets)):
				octets.insert(i, "0")

		return octets

	def ipv6_bin(ip: str) -> str:
		"""Convert IPv6 address to binary representation."""

		return "".join([bin(int(_, 16)+65536)[3:] for _ in ipv6_unpack(ip)])

	def bin_ipv6(ip: str) -> str:
		"""Convert binary address to hexadecimal IPv6 form."""

		return ":".join([str(hex(int(ip[i:i+16], 2)))[2:] \
			for i in range(0, len(ip), 16) if int(ip[i:i+16], 2)!=0]) + "::"

	if len(ip_list) == 1 and is_valid_ipv6(ip_list[0]):
		return ip_list[0]

	bin_list: list = [ipv6_bin(ip) for ip in ip_list]
	bin_list.sort()
	bitmask: int = common_prefix(bin_list[0], bin_list[-1])
	common_subnet: str = bin_list[0][:bitmask] + "0" * (bitmask // 16)
	return bin_ipv6(common_subnet) + "/" + str(bitmask)


def main():
	args: int = len(sys.argv)
	
	if args != 3:
		raise TypeError(f"ipsum takes exactly two arguments")

	path: str = sys.argv[1]
	version: str = sys.argv[2]
	ip_list: list = open(path, "r").read().split()	

	if version == "v4":
		print("Result net:", ipv4_summarize(ip_list))
	elif version == "v6":
		print("Result net:", ipv6_summarize(ip_list))


if __name__ == "__main__":
	main()