name = GET.get("name")
data = get(name)

if data:
  print("Info")
  print(data["first_name"])
  print(data["last_name"])
else:
  print("Sorry.  No user found with the name " + name)
