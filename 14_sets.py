# Sets

example = set()
dir(example)
example.add(42)
example.add(False)
example.add(3.14159)
example.add("Carbon")
example
len(example) """shows the number of values in there"""
example.remove(42) """delete value"""
example
len(example)
example.discard(50) """delete too but quitly"""

example2 = set([28. True, 2.71828, "Helium"])
len(example2)
example2.clear() """delete everything in there"""
len(example2)
example2