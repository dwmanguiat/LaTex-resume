import subprocess
import os

def render_latex_to_pdf(latex_file):
    try:
        subprocess.run(['pdflatex', latex_file], check=True)
        print(f"Successfully rendered {latex_file} to PDF. \n")
    except subprocess.CalledProcessError as e:
        print(f"Error rendering {latex_file} to PDF: {e}")

def convert_pdf_to_png(pdf_file, output_base):
    try:
        # pdftoppm is reliable on Linux and not subject to ImageMagick PDF policy restrictions
        subprocess.run(['pdftoppm', '-r', '300', '-png', '-singlefile', pdf_file, output_base], check=True)
        print(f"Successfully converted {pdf_file} to {output_base}.png.")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {pdf_file} to PNG: {e}")

if __name__ == "__main__":
    latex_file = os.path.abspath('resume.tex')
    pdf_file = os.path.abspath('resume.pdf')
    png_base = os.path.abspath('resume')

    render_latex_to_pdf(latex_file)
    convert_pdf_to_png(pdf_file, png_base)
