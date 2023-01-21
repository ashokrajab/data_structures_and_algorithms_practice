"""
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

    For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.

 

Example 1:

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:

Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:

Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

 

Constraints:

    1 <= s.length <= 20
    s consists of digits only.
"""
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        s_len = len(s)
        ans = []
        def backtrack(i, ip_addr):
            nonlocal ans
            if i < s_len and len(ip_addr) == 4:
                return
            if i == s_len:
                if len(ip_addr) == 4:
                    ans.append(".".join(ip_addr))
                return

            d = 3
            if int(s[i]) == 0:
                d = 1
            elif int(s[i]) > 2:
                d = 2

            for j in range(1,d+1):
                if i+j <= s_len and int(s[i:i+j])<=255:
                    ip_addr.append(s[i:i+j])
                    backtrack(i+j, ip_addr)
                    ip_addr.pop()
        backtrack(0,[])
        return ans 