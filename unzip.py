import zipfile

fh = open("org.wikipedia.beta_2.1.142-beta-2016-03-07-142_minAPI15(armeabi,armeabi-v7a,mips,x86)(nodpi).apk", "rb")
z = zipfile.ZipFile(fh)

def name_with_size(zipfile, file_path):
    return file_path, file_path.split("/")[-1], z.getinfo(file_path).file_size

res_drawables = filter(
    lambda name: name.startswith("res/drawable") and name.endswith("png"),
    z.namelist())
drawable_name_with_size = map(lambda name: name_with_size(z, name), res_drawables)

dic = {}


for file_path, name, size in drawable_name_with_size:
    if not name in dic:
        dic[name] = (file_path, name, size)
    elif dic[name][2] < size:
        dic[name] = (file_path, name, size)
out_path = "./temp/"
html = "<table background = 'back.png'>"
index = 0
for k in dic:
    if index == 0:
        html += "<tr>"
    index = (index + 1) % 10
    print dic[k]
    name = dic[k][1]
    path = dic[k][0]
    fd = open(out_path + name, 'wb')
    fd.write(z.read(path))
    fd.close()
    html += '<td><p>' +  '</p><img src = "' + name + '"  width = 100px height = 100px/></td>'
    if index == 0:
        html += "</tr>"

fd = open(out_path + "index.html", 'w')
fd.write(html)
fd.close()
fh.close()
