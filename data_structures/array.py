"""
Python built-in data types
Text Type:          str
Numeric Types:      int, float, complex
Sequence Types:     list, tuple, range
Mapping Type:       dict
Set Types:          set, frozenset
Boolean Type:       bool
Binary Types:       bytes, bytearray, memoryview
None Type:          None
"""

if __name__ == "__main__":
    print("hello")

    mylist: list[str] = ["My", "name", "is", "Liam"]

    for i in mylist:
        print(i)

    for index, element in enumerate(mylist):
        print(index, element)

    print(mylist[0])
