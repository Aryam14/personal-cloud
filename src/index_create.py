def html_create(directory_data):
    print("Creating HTML")
    d = '<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<style> * { padding: 0;margin: 0; box-sizing: border-box; font-family: Arial, sans-serif; text-decoration: none;}	body { width: 100%; height: 100vh; border-color: #4158d0; background-image: radial-gradient( circle farthest-corner at 22.4% 21.7%, rgba(4,189,228,1) 0%, rgba(2,83,185,1) 100.2% );; display: grid;    place-items: center;} h1 { width: 100%; font-size: 40px;  text-align: center; font-weight: 600; background-image: linear-gradient(-20deg, #e9defa 0%, #fbfcdb 100%); color: transparent; background-clip: text; -webkit-background-clip: text;	} .container { background-color: white;  width: 60%;  text-align: center; padding: 25px 20px;  border-radius: 10px; margin-bottom: 200px;	}	.button-container { display: flex; justify-content: space-between; text-align: center; margin-bottom: 20px; }	.button-container input {    padding: 10px;    font-size: 10px;    border: none;    cursor: pointer;    border-radius: 4px;    transition: background-color 0.3s;	}	input[type=file]::file-selector-button {   border: 5px solid #4E4FEB; background-color: #4E4FEB;  color: white; transition: 1s; border-radius: 10px;} input[type=file]::file-selector-button:hover { background-color: #068FFF; border: 5px solid #068FFF;  color: black;	}	input[type=submit] { background-color: #4E4FEB; border: 2px solid #4E4FEB; color: white; padding: 1px 6px;	}	#file-table {  width: 100%; border-collapse: collapse;}	#file-table th,	#file-table td { padding: 10px; text-align: center; border-bottom: 1px solid #ddd; word-break: break-word; margin-bottom: 20px;	}#file-table th { background-color: #f2f2f2;	}		.header-image {	background-image: url("./cloud.png");	background-position: center;	background-repeat: no-repeat;	position: relative;	background-size: cover;	width: 550px;	height: 200px;	}	.header-text {	text-align: center;	position: relative;	top: 110px;	left: 1px;	}	</style>\n\t<title>Files</title>\n</head>\n'
    d += f'<body>\n'
    d += f'<h1>Personal Cloud</h1>\n'
    d += f'<div class="container">\n\t<div class="button-container">\n'
    d += f'<form action = "/upload" method = "post" enctype="multipart/form-data">\n\t <input type="file" name="file" />\n\t <input type = "submit" value="Upload">\n </form>\n</div>\n'
    d += f'<table style="width:100%" id="file-table">\n\t <tr>\n\t'

    for var in directory_data[0]:
        d += f'\t<th> {var} </th>\n\t'
    d += f'\t</tr>'
    for ds in directory_data:
        d += f'\n\t<tr>\n\t'
        ct = 1
        for k in ds:
            v = ds[k]
            print(v)
            if (ct==1):
                d += f'\t<td><a href="/download/{v}.{ds["ext"]}"> {v} </a></td>\n\t'
                ct = 0
            else:
                d += f'\t<td> {v} </td>\n\t'
            #print(v)
        d += f'</tr>\n\t'
    d += f'\n</table>\n </div>\n'

    d += f'\n</body>'
    with open("/home/user/personal-cloud/src/templates/index.html", "w") as file:
        file.write(d)
        file.close()