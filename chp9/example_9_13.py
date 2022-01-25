from example_9_7 import Vector2d

v1 = Vector2d(1.1, 2.2)
dumpd = bytes(v1)
print(dumpd)
print(len(dumpd))

v1.typecode = "f"
dumpf = bytes(v1)
print(dumpf)