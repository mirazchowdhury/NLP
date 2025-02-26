"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 
Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3


Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.



"""

def numJewelsInStones_Count(jewels: str, stones: str) -> int:
    sum = 0
    for j in jewels:
         sum += (stones.count(j))

    """
    for j in jewels:

    Ei line ta ekta for loop chalay je jewels string-er prottek ta character (j) loop er moddhe dhukbe.
    Mane jewels string-er prottek ta letter niye sequentially check korbo.
    """
    
    """sum += (stones.count(j))

    stones.count(j) → stones string er moddhe j (jewel) koybar ache seta count kore.
    sum += mane sei count ta amra sum-er sathe jog kore rakhbo.
    Ebhabe prottekta jewel er jonno check korbo je stones e kotobar ache ebong seta total sum e store hobe.
    """

    return sum

    # return sum(stones.count(j) for j in jewels)

# Example test cases
print(numJewelsInStones_Count("aA", "aAAbbbb"))  # Output: 3
print(numJewelsInStones_Count("z", "ZZ"))        # Output: 0