
def html_create(directory_data):
    print("Creating HTML")
    d = f'<body>\n'
    d += f'<h1>Personal Cloud</h1>\n'
    d += f'<form action = "/upload" method = "post" enctype="multipart/form-data">\n\t <input type="file" name="file" />\n\t <input type = "submit" value="Upload">\n </form>\n'
    d += f'<table style="width:100%">\n\t <tr>\n\t'

    if len(directory_data) == 0:
        print("No files in directory")
        for var in directory_data[0]:
            d += f'\t<th> {var} </th>\n\t'
        d += f'\t</tr>'
        for ds in directory_data:
            d += f'\n\t<tr>\n\t'
            for k in ds:
                v = ds[k]
                print(v)
                d += f'\t<td> {v} </td>\n\t'
                #print(v)
            d += f'</tr>\n\t'
        d += f'\n</table>'

        d += f'\n</body>'
        with open("/home/ubuntu/Desktop/mp/personal-cloud/src/templates/index.html", "w") as file:
            file.write(d)