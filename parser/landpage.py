import markdown
from yattag import Doc, indent
from config import *

doc, tag, text = Doc().tagtext()

# fonction d'ouverture et traduction des documents markdown
def readMDfile(mdfile):

    with open("sources/" + mdfile + ".md", mode="r", encoding="utf-8") \
    as mdInput:
        texte = mdInput.read()
        mdOutput = markdown.markdown(texte, ['markdown.extensions.extra'])
    return mdOutput



class Main():

    def __init__(self):
        doc.asis('<!DOCTYPE html>')
        with tag('html', lang='fr'):
            self.head()
            self.body()

        with open('../website/index.html','w') as output:
            output.write(indent(doc.getvalue()))


    def head(self):

        with tag ('head'):
            doc.stag('meta', charset='utf-8')
            with tag('title'):
                text(metaTitre)
            doc.stag('meta', name='description', content=metaDescription)
            doc.stag('meta', name='keywords', content=metaKeywords)
            doc.stag('meta', name='author', content='nicolas chesnais')
            doc.stag('link', rel='stylesheet', href='style.css')
            doc.stag('link', rel='stylesheet', href='specific.css')
            doc.stag('link', rel='icon', type='image/png', href='imgs/favicon.png')


    def body(self):

        with tag('body'):
            with tag('div', id='main'):
                with tag('div', id='main-title', klass='box flex thinBorder'):
                    with tag('h1'):
                        text(titre)

                with tag('div', id='collectifs'):
                    text('>>')
                    with tag('span', id='plus'):
                        text('+')
                    for i, j in collectifs.items():
                        with tag('a', href=j):
                            text(i)

                with tag('ul', id='menu'):
                    for i, j in menu.items():
                        with tag('li'):
                            with tag('a', href=j, klass='black'):
                                with tag('span'):
                                    if i[1][0] == '/':
                                        text('→')
                                    else:
                                        text('↗')
                                text(i)

                with tag('div', klass='options'):
                    for i, j in options.items():
                        with tag('a', onclick=j):
                            with tag('span', klass='black'):
                                if i[1][0] == 'o':
                                    text('+')
                                else:
                                    text('-')
                            text(i)

                for section in sections:
                    section = Section(section)
                    section.generateSection()

            with tag('footer', klass='black'):
                doc.asis(readMDfile('footer'))

            with tag('script', src='scripts.js'):
                text()



class Section():
    def __init__(self, section):
        self.section = section


    def generateSection(self):

        with tag('section', id='sect-'+self.section):
            with tag('div', id=self.section, klass='folder box flex black thinBorder'):
                with tag('h3'):
                    if(self.section == 'nmilliards'):
                        doc.asis('n × 10<sup>9</sup>')
                    else:
                        text(self.section)
            with tag('div', klass='triangle'): text()
            with tag('div', klass='black'):
                with tag('div', klass='specontent thinBorder'):
                    doc.asis(readMDfile('sections/' + self.section))
            sections = eval(self.section)
            for project in sections:
                self.generateProject(project)


    def generateProject(self, project):

        pDict = eval(project)
        with tag('div', klass='file'):
            with tag('div', klass='base-content box flex thinBorder'):
                with tag('h4', klass='targ'):
                    doc.asis(pDict['titre'])
                with tag('p', klass='version'):
                    doc.asis(pDict['version'])
                with tag('p', klass='licence'):
                    doc.asis(pDict['licence'])
                with tag('a', href=pDict['adr'], target='_blank'):
                    doc.asis(pDict['adrname'])
            with tag('div', id=project, klass='content thinBorder'):
                doc.asis(readMDfile('projets/' + project))



Main()
