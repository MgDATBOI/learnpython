import pickle


# s -> string, no s -> file-like obj
# pickle.load()
# pickle.loads()
# pickle.dump()
# pickle.dumps()


class Box:
    size = [4, 4, 2]
    name = "Awesome Box"
    data = {"Owner": "me", "id": 4}


box = Box()
print(box.size)

pickle_box = pickle.dumps(box)

print(f"Pickled object\n{pickle_box}")

box.data = None

old_box = pickle.loads(pickle_box)
print(old_box.data)
