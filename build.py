import shutil
import glob

build_dir = "dist/"
build_target = build_dir + "index.html"

def get_lines(filename):
    lines = []
    with open(filename) as i:
        lines = i.readlines()
    return lines

def get_css_lines():
    lines = []
    lines.append("<style>")
    files = glob.glob("src/css/*")
    for f in files:
        lines.extend(get_lines(f))
    lines.append("</style>")
    return lines

def write_lines(filename, lines):
    with open(filename, "w") as o:
        for l in lines:
            o.write(l.strip() + " ")

def copy_images():
    files = glob.glob("src/img/*")
    for f in files:
        shutil.copy(f, build_dir + "img/")

def build():
    lines = get_lines("src/index.html")
    lines.extend(get_css_lines())
    write_lines(build_target, lines)
    copy_images()

build()

