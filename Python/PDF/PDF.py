from fpdf import FPDF
"""
# create FPDF object
# Layout ('P','L')
# Unit ('mm', 'cm', 'in')
# format ('A3', 'A4' (default), 'A5', 'Letter', 'Legal', (100,150))
pdf = FPDF('P', 'mm', 'Letter')

# Add a page
pdf.add_page()

# specify font
# fonts ('times', 'courier', 'helvetica', 'symbol', 'zpfdingbats')
# 'B' (bold), 'U' (underline), 'I' (italics), '' (regular), combination (i.e., ('BU'))
#pdf.set_font('helvetica', 'BIU', 16)
pdf.set_font("Times", size=10)
pdf.set_text_color(0,0,0)
# Add text
# w = width
# h = height
# txt = your text
# ln (0 False; 1 True - move cursor down to next line)
# border (0 False; 1 True - add border around cell)
pdf.cell(120, 100, 'Hello World!', ln=True, border=True)
#pdf.cell(120, 100, 'Hello World!', new_x=XPos.LMARGIN, new_y=YPos.NEXT, border=True)

pdf.set_font('helvetica', '', 12)
pdf.cell(80, 10, 'Good Bye World!')



data = (
    ("First name", "Last name", "Age", "City"),
    ("Jules", "Smith", "34", "San Juan"),
    ("Mary", "Ramos", "45", "Orlando"),
    ("Carlson", "Banks", "19", "Los Angeles"),
    ("Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire"),
)
#pdf.add_page()

#addTable(data)
"""
import Datum
import os.path

#startOfFile = True

#def change_startOfFile(val):
    #global startOfFile
    #startOfFile = val

def addÜberschrift(pdf, Text):
    pdf.set_font("helvetica", "BU", size = 16)
    pdf.set_text_color(0,0,255)
    #if startOfFile:
        #change_startOfFile(False)
    #else:
        #pdf.ln(pdf.font_size * 2.5)
        #pdf.ln(pdf.font_size * 2.5)
    pdf.cell(80, 16, Text)

def addTable(pdf, tableData):
    line_height = pdf.font_size * 2.5
    pdf.set_font("helvetica", "", size = 10)
    pdf.set_text_color(0,0,0)
    col_width = pdf.epw / 4  # distribute content evenly
    for row in tableData:
        pdf.ln(line_height)
        for content in row:
            pdf.multi_cell(col_width, line_height, content, border = 1, new_x = "RIGHT", new_y = "TOP", max_line_height = pdf.font_size)

def generatePDF(DatumStart, DatumEnd, outerDict):
    if len(outerDict.keys()) == 0:
        return False
    #change_startOfFile(True)
    pdf = FPDF('P', 'mm', 'Letter')
    for Dienst in outerDict.keys():
        pdf.add_page()
        addÜberschrift(pdf, Dienst)
        innerDict = outerDict.get(Dienst)
        data = [("Datum", "Teilnehmer/in", "Teilnehmer/in")]
        for listDatum in innerDict.keys():
            stringDatum = listDatum.toString()
            #stringDatum = str(listDatum)
            pair = innerDict.get(listDatum)
            newTuple = (stringDatum, (pair[0]).name, (pair[1]).name)
            data.append(newTuple)
        data = tuple(data)
        addTable(pdf, data)
    PDFNAME_CLEAN = "pdf/Dienstverteilung " + DatumStart + " - " + DatumEnd
    PDFNAME = PDFNAME_CLEAN + ".pdf"
    i = 1
    while os.path.isfile(PDFNAME):
        i += 1
        PDFNAME = PDFNAME_CLEAN + " (" + str(i) + ").pdf"
    try:
        pdf.output(PDFNAME)
    except:
        os.mkdir("pdf")
        pdf.output(PDFNAME)
    return PDFNAME

"""
class testclass:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return str(self.name)

test = {"Waschküchendienst": {(2022, 2, 2): [testclass("Jan"), testclass("Philipp")]}, "Waschküchendienst2": {(2022, 2, 2): [testclass("Jan"), testclass("Philipp")]}}
generatePDF("02.02.2022", "22.22.2222", test)
"""