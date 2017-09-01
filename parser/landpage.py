import markdown, json
from yattag import Doc, indent

doc, tag, text = Doc().tagtext()

# fonction d'ouverture et traduction des documents markdown
def readMDfile(mdfile):

    with open("sources/" + mdfile + ".md", mode="r", encoding="utf-8") \
    as mdInput:
        texte = mdInput.read()
        mdOutput = markdown.markdown(texte, ["markdown.extensions.extra"])

        # clearing useless p tag around img tags
        while mdOutput.find("<p><img") != -1:
            i = mdOutput.find("<p><img")
            x = mdOutput.find("</p>", i)
            mdOutput = mdOutput[0:i] + mdOutput[i+3:x] + mdOutput[x+4:]

    return mdOutput

def readJSONfile(jsonfile):

    with open(jsonfile + ".json", mode="r", encoding="utf-8") as f:
        jsonInput = json.load(f)

    return jsonInput

class Main():

    def __init__(self, configFile):

        infos = readJSONfile(configFile)

        doc.asis("<!DOCTYPE html>")
        with tag("html", lang="fr"):
            self.head(infos["meta"])
            self.body(infos)

        with open("../website/index.html","w") as output:
            output.write(indent(doc.getvalue()))


    def head(self, meta):

        with tag ("head"):
            doc.stag("meta", charset="utf-8")
            with tag("title"):
                text(meta["title"])
            doc.stag("meta", name="description", content=meta["description"])
            doc.stag("meta", name="keywords", content=meta["keywords"])
            doc.stag("meta", name="author", content="nicolas chesnais")
            doc.stag("link", rel="stylesheet", href="style.css")
            doc.stag("link", rel="stylesheet", href="specific.css")
            doc.stag("link", rel="icon", type="image/png", href="imgs/favicon.png")


    def body(self, infos):

        bod = infos["body"]

        with tag("body"):
            with tag("div", id="main"):
                with tag("div", id="main-title", klass="box flex thinBorder"):
                    with tag("h1"):
                        text("nicolas chesnais")

                with tag("div", id="collectifs"):
                    text(">>")
                    with tag("span", id="plus"):
                        text("+")
                    for i, j in bod["collectifs"].items():
                        with tag("a", href=j):
                            text(i)

                with tag("ul", id="menu"):
                    for i, j in bod["menu"].items():
                        with tag("li"):
                            with tag("a", href=j, klass="black"):
                                with tag("span"):
                                    if i[1][0] == "/":
                                        text("→")
                                    else:
                                        text("↗")
                                text(i)

                with tag("div", klass="options"):
                    for i, j in bod["options"].items():
                        with tag("a", onclick=j):
                            with tag("span", klass="black"):
                                if i[1][0] == "o":
                                    text("+")
                                else:
                                    text("-")
                            text(i)

                for section in infos["sections"]:
                    section = Section(section, infos["sections"][section])

            with tag("footer", klass="black"):
                doc.asis(readMDfile("footer"))

            with tag("script", src="scripts.js"): text()



class Section():

    def __init__(self, section, projects):
        self.generateSection(section, projects)

    def generateSection(self, section, projects):

        with tag("section", id="sect-" + section):
            with tag("div", id=section, klass="folder box flex black thinBorder"):
                with tag("h3"):
                    if(section == "nmilliards"):
                        doc.asis("n × 10<sup>9</sup>")
                    else:
                        text(section)
            with tag("div", klass="triangle"): text()
            with tag("div", klass="black"):
                with tag("div", klass="specontent thinBorder"):
                    doc.asis(readMDfile("sections/" + section))

            for project in projects:
                self.generateProject(project, projects[project])


    def generateProject(self, project, infos):

        with tag("div", klass="file"):
            with tag("div", klass="base-content box flex thinBorder"):
                with tag("h4", klass="targ"):
                    doc.asis(infos["titre"])
                with tag("p", klass="version"):
                    doc.asis(infos["version"])
                with tag("p", klass="licence"):
                    doc.asis(infos["licence"])
                with tag("a", href=infos["adr"], target="_blank"):
                    doc.asis(infos["adrname"])
            with tag("div", id=project, klass="content thinBorder"):
                doc.asis(readMDfile("projets/" + project))



Main("infos")
