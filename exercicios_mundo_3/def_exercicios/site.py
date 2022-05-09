def ler(site):
    import urllib.request
    import urllib.error
    try:
        urllib.request.urlopen('https://'+ site +'/')
    except urllib.error.URLError:
        print(f'Deu erro! O site {site} não está acessível.')
    else:
        print(f'O site {site} está acessível.')