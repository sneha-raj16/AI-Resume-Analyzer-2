from fpdf import FPDF
import tempfile



def generate_pdf(data):


    pdf = FPDF()


    pdf.add_page()


    pdf.set_font(
        "Arial",
        size=12
    )


    pdf.cell(
        200,
        10,
        "AI Resume Analysis Report",
        ln=True
    )


    pdf.ln(10)



    for key,value in data.items():


        pdf.multi_cell(
            0,
            8,
            f"{key.upper()}:\n{value}\n"
        )



    path = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ).name



    pdf.output(path)



    with open(
        path,
        "rb"
    ) as file:

        return file.read()
