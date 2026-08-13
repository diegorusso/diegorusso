import glob

pattern = "Lib/test/test_importlib/**/*.py"

normal = sorted(glob.glob(pattern, recursive=True))

print("glob.glob(..., recursive=True)")
for path in normal[:5]:
    print(" ", path)
print(f"{len(normal)} files found")
print()

shortcut = sorted(glob.rglob(pattern))

print("glob.rglob(...)")
for path in shortcut[:5]:
    print(" ", path)
print(f"{len(shortcut)} files found")
print()

print("Same results:", normal == shortcut)
