string = """Любіть Україну, як сонце любіть,

як вітер, і трави, і води...

В годину щасливу і в радості мить,

любіть у годину негоди.



Любіть Україну у сні й наяву,

вишневу свою Україну,

красу її, вічно живу і нову,

і мову її солов'їну.



Без неї — ніщо ми, як порох і дим,

розвіяний в полі вітрами...

Любіть Україну всім серцем своїм

і всіми своїми ділами."""

# цикл для видалення знаків пунктуації
punctuation = [",", ".", ":", ";", "-", "—", "!", "?"]
for i in punctuation:
    string = string.replace(i, "")

string = string.lower()
lst = string.split()
keys = set(lst)     # множина унікальних слів - ключів для словника

# цикл для формування списку значень словника - к-ть входжень слів у рядок
values = []
for i in keys:
    values.append(lst.count(i))
# створено словник
dct = dict(zip(keys, values))
# формування словника з максимальними значеннями
mx = max(dct.values())
mx_item = {j: k for j, k in dct.items() if k == mx}
# формування словника з мінімальними значеннями
mn = min(dct.values())
mn_item = {n: m for n, m in dct.items() if m == mn}

print("Most often words:", list(mx_item.items()))
print("Rarest words:", list(mn_item.items()))
