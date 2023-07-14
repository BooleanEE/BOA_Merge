from pathlib import Path
import PyPDF2

def merge_pdfs_in_directory(directory_path):

    
    # Get a list of all student folders inside the directory
    student_folders = directory_path.glob('*/')
    
    # Iterate over each student folder
    for student_folder in student_folders:
        # Get the student name from the folder name
        student_name = student_folder.stem

        output_path = directory_path / student_name

        # Get a list of all PDF files inside the student folder
        pdf_files = student_folder.glob('*.pdf')
        
        # Merge the PDF files
        merger = PyPDF2.PdfMerger()
        for pdf_file in pdf_files:
            merger.append(str(pdf_file))
    
        # Write the merged PDF to the output file
        output_file = output_path / f"{student_name}_merged.pdf"
        merger.write(output_file)
        merger.close()

# Example usage
directory_path = Path(__file__).parent / 'files'

merge_pdfs_in_directory(directory_path)
