#1108. Defanging an IP Address
#https://leetcode.com/problems/defanging-an-ip-address/

class Solution(object):
    def defangIPaddr(self, address):
        address = address.replace(".","[.]")
        return address
        

