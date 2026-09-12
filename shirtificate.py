from fpdf import FPDF

userinput= input('Name: ')
pdf = FPDF()
pdf.add_page()

pdf.set_font('Helvetica',size=30)
pdf.cell(0, 10, 'CS50 Shirtificate', align='C')


pdf.image("shirt.png", x=10, y=50, w=190)

pdf.set_text_color(255, 255, 255)
pdf.set_font('Helvetica', size=30)
pdf.text(x=70, y=150, txt=f'{userinput} took CS50')
pdf.output("shirtificate11.pdf")
