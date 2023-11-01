f = open("./example.smd", "r")
endlines = []
lines = []
mode = ""
hrefed=""
classed=""
for x in f:
  lines.append(x)
def header(l):
  mode = "h1"
  # print(lines[l])
  dsus = lines[l].strip("$#")
  lines[l] = dsus
  endlines.append(f"<h1>{(lines[l].rstrip("\n")).lstrip("$#")}</h1>")
def breakln():
  endlines.append("<br/>")
def divStart(l):
  mode = "divS"
  dsus = lines[l].strip("$%")
  lines[l] = dsus
  endlines.append(f"<div class=\"{(lines[l].rstrip("\n")).lstrip("$%")}\">")
def title(l):
  mode = "divS"
  dsus = lines[l].strip("$t")
  lines[l] = dsus
  endlines.append(f"<title>{(lines[l].rstrip("\n")).lstrip("$t")}</title>")
def divEnd(l):
  mode = "divS"
  dsus = lines[l].strip("$%")
  lines[l] = dsus
  endlines.append("</div>")
def styles(l):
  mode = "style"
  dsus = lines[l].strip("$=")
  lines[l] = dsus
  endlines.append(f"<link rel=\"stylesheet\" href=\"{(lines[l].rstrip("\n")).lstrip("$=")}\"/>")
def textfr(l):
  mode = "text"
  dsus = lines[l].strip("$!")
  lines[l] = dsus
  endlines.append(f"{(lines[l].rstrip("\n")).lstrip("$!")}")
def atag(l,hrf):
  mode = "a"
  dsus = lines[l].strip("$a")
  lines[l] = dsus
  endlines.append(f"<a href=\"{hrf}\">{(lines[l].rstrip("\n")).lstrip("$!")}</a>")
def span(l,hrf):
  mode = "span"
  dsus = lines[l].strip("$-")
  lines[l] = dsus
  endlines.append(f"<span class=\"{hrf}\">{(lines[l].rstrip("\n")).lstrip("$-")}</span>")
def img(l,hrf):
  mode = "+"
  dsus = lines[l].strip("$+")
  lines[l] = dsus
  endlines.append(f"<img class=\"{hrf}\" src=\"{(lines[l].rstrip("\n")).lstrip("$+")}\" alt=\"nobody\"/>")
def generate():
  dolla = 0
  bolla = 0
  i=0
  for line in lines:
    for elem in line:
      if elem == "$":
        dolla = 1
      if elem == "#" and dolla == 1:
        header(i)
        dolla = 0
      if elem == "b" and dolla == 1:
        breakln()
        dolla = 0
      if elem == "%" and dolla == 1:
        divStart(i)
        dolla = 0
      if elem == "^" and dolla == 1:
        divEnd(i)
        dolla == 0
      if elem == "=" and dolla == 1:
        styles(i)
        dolla = 0
      if elem == "t" and dolla == 1:
        dolla= 0
        title(i)
      if elem == "." and dolla == 1:
        dolla=0
        dsus = lines[i].strip("$.")
        lines[i] = dsus
        hrefed = (lines[i].rstrip("\n")).lstrip("$.")
      if elem == "a" and dolla ==1:
        dolla = 0
        atag(i,hrefed)
      if elem == "-" and dolla ==1:
        dolla = 0
        span(i,classed)
      if elem == "l" and dolla == 1:
        dolla=0  
        dsus = lines[i].strip("$l")
        lines[i] = dsus
        classed = (lines[i].rstrip("\n")).lstrip("$l")
      if elem == "!" and dolla == 1:
        textfr(i)
        dolla = 0
      if elem == "+" and dolla == 1:
        dolla = 0
        img(i,classed)
    i+=1
  z = 0
  for lo in endlines:
    if z==1:
        endlines.append("<head>")
        endlines.append("<meta charset=\"UTF-8\">")
        endlines.append("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">")
        x = open("./flake.html", "a+")
        x.write(lo+"\n")
        z+=1
        endlines.append("</head>")
    else:
      x = open("./flake.html", "a+")
      x.write(lo+"\n")
      z+=1
      # print(lo)
  print("CONVERSION COMPLETE .smd => .html")
generate()
