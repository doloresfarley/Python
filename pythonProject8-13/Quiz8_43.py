def display(product, options=[]):
    print(options)
    if 'monitor' in product:
        options.append('HDMI')
    print(product, options)

display('Acer monitor')
display('Samsung monitor')