def display(product, options=[]):
    if 'monitor' in product:
        options.append('HDMI')

    print(product, options)
options2 = []
display('Acer monitor', options2)
display('Samsung monitor',options2)
print()
print(options2)
