import os

def main(directory: str, output: str):
    # For each file in the directory, convert it to .tex for appending it to `alphabet2.sty`
    convert(directory, output)

    # This will create the file `alphabet.sty` in the current directory and write its header.
    with open('alphabet2.sty', 'w', encoding='utf-8') as f:
        f.write(r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{alphabet2}[2022/11/22 Alphabet 2]
\RequirePackage{pstricks}
\RequirePackage{scalerel}
""")
        f.write('\n')
        for file in os.listdir(output):
            if file.endswith('.tex'):
                with open(os.path.join(output, file), 'r', encoding='utf-8') as f2:
                    filename = '\\' + file[:-4]
                    f.write(fr"\newcommand{{{filename}}}{{\scalerel*{{{f2.read()}}}{{B}}}}")
                    f.write('\n')
        
        f.write(r'\ProcessOptions\relax')

def convert(directory: str, output: str):
    # This will convert all .svg files in a directory to .tex using inkscape
    os.chdir(output)
    for filename in os.listdir(f"../{directory}"):
        if filename.endswith('.svg'):
            # Change current directory
            os.system(f'inkscape --export-latex --export-filename={filename[:-4]}.tex ../{directory}{filename}')
            with open(f'{filename[:-4]}.tex', 'r+', encoding='utf-8') as g:
                content = g.readlines()
                g.seek(0)
                # truncate the file
                g.truncate()
                g.writelines(content[3:])
            
    os.chdir('..')

if __name__ == '__main__':
    main('svg/', 'tex/')