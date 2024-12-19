import subprocess
import os

def render_latex_to_pdf(latex_file):
    try:
        subprocess.run(['pdflatex', latex_file], check=True)
        print(f"Successfully rendered {latex_file} to PDF. \n")
    except subprocess.CalledProcessError as e:
        print(f"Error rendering {latex_file} to PDF: {e}")

def convert_pdf_to_png(pdf_file, output_png):
    try:
        subprocess.run(['magick', 'convert', '-density', '300', os.path.normpath(pdf_file), os.path.normpath(output_png)], check=True)
        print(f"Successfully converted {pdf_file} to {output_png}.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {pdf_file} to PNG: {e}")

if __name__ == "__main__":
    latex_file = os.path.abspath('resume.tex')
    pdf_file = os.path.abspath('resume.pdf')
    png_file = os.path.abspath('resume.jpg')


    render_latex_to_pdf(latex_file)

    print(pdf_file)
    print(png_file)

    convert_pdf_to_png(pdf_file, png_file)