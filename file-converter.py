import markdown
import sys

def main(argv):
    if argv[1] == 'markdown':
        htmlConverter(argv[2],argv[3])
    else:
        sys.stdout.buffer.write(b'Command not found...\n')

def htmlConverter(inputfile,outputfile):
    html = ''

    with open(inputfile,'r') as i:
        html = markdown.markdown(i.read(),extensions=['extra','sane_lists','toc','codehilite'])

    with open(outputfile,'w') as o:
        o.write(html)
    
if __name__ == '__main__':
    main(sys.argv)