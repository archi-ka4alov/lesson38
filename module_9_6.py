def all_variants(text):
    for i in range(len(text)):
        for y in range(len(text)):
            if len(text) > i + y:
                yield text[y:y + i + 1:]


a = all_variants("abc")
for i in a:
    print(i)
