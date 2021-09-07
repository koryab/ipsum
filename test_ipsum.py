import pytest

from ipsum.__main__ import ipv4_summarize, ipv6_summarize, main

class TestIPSum:
	@pytest.mark.parametrize("ip_list, expected",[
		([
			"192.168.1.2",
			"192.168.1.3",
			"192.168.1.5",
			],
			"192.168.1.0/29"),
		(["0.0.0.0",], "0.0.0.0"),
		])
	def test_ipv4_ok(self, ip_list, expected):
		res_net = ipv4_summarize(ip_list)
		assert res_net == expected

	@pytest.mark.parametrize("ip_list, expected",[
		([
			"ffe0::1:0:0:0",
			"ffe0::2:0:0:0",
			"ffe0::4:0:0:0",
			"ffe0::8:0:0:0",
			"ffe0::10:0:0:0",
			"ffe0::20:0:0:0",
			"ffe0::40:0:0:0",
			"ffe0::80:0:0:0",
			],
			"ffe0::/72"),
		([
			"ffe0::1:0:0:0"
			],
			"ffe0::1:0:0:0")
		])
	def test_ipv6_ok(self, ip_list, expected):
		res_net = ipv6_summarize(ip_list)
		assert res_net == expected

	@pytest.mark.parametrize("ip_list",[
		["1124548.5478"],
		["192:168:c:0"],
		["192.168.1.256"],
		["ffe0::80:0:0:0"],
		["4.8.15.16.23.42"],
		])
	def test_ipv4_raises_value_error(self, ip_list):
		with pytest.raises(ValueError) as exc_info:
			ipv4_summarize(ip_list)
		assert str(exc_info.value) == f"Incorrect IPv4 address: {ip_list[0]}"

	@pytest.mark.parametrize("ip_list",[
		["2001:0db8:85a3:0011500:0000:8a2e:0370:734"],
		["ffe0::z:0:0:0"],
		["192.168.1.1"],
		["ffe0::1:0::0:0"],
		])
	def test_ipv6_raises_value_error(self, ip_list):
		with pytest.raises(ValueError) as exc_info:
			ipv6_summarize(ip_list)
		assert str(exc_info.value) == f"Incorrect IPv6 address: {ip_list[0]}"

	def test_args(self):
		with pytest.raises(TypeError) as exc_info:
			main()
		assert str(exc_info.value) == f"ipsum takes exactly two arguments"