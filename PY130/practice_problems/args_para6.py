def concat_strings(*args, sep="-"):
    return sep.join(args)

print(concat_strings('a', 'b', 'c'))
print(concat_strings('1', '2', '3', sep='|'))