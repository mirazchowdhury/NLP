class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")


# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".","[.]")

# sol = Solution()
# address = input()

# print(sol.defangIPaddr(address))


# def defangIPaddr(address: str) -> str:
#     return address.replace(".","[.]")

# print(defangIPaddr("1.1.1.1"))
# print(defangIPaddr("255.100.50.0"))