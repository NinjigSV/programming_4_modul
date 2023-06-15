def polindrom(string):
    if string[::-1].lower() == string.lower():
        print(string, '=', True)
    else:
        print(string, '=', False)

polindrom('шАла   Ш')
polindrom('хЕлоуворлд')