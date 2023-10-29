import markdown
import os
import sys


def main(argv):
    command = argv[1]
    inputfile = argv[2]
    outputfile = argv[3]

    if not os.path.exists(inputfile):
        raise sys.stdout.buffer.write(b'Inputfile does not exist...\n')
    elif len(argv) != 4:
        raise sys.stdout.buffer.write(b'Wrong usage!\nuseage : python3 file-converter.py markdown inputfile outputfile\n')
    elif command != 'markdown':
        raise sys.stdout.buffer.write(b'Command not found...\n')
    else:
        htmlConverter(inputfile,outputfile)

# markdownをhtmlに変換する
def htmlConverter(inputfile,outputfile):
    html = ''

    # inputfileを読み込む
    with open(inputfile,'r') as i:
        html = markdown.markdown(i.read(),extensions=['extra','codehilite','sane_lists','toc'])

    # outputfileに書き込む
    with open(outputfile,'w') as o:
        o.write(html)


if __name__ == '__main__':
    main(sys.argv)
