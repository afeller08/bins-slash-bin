import sys
import os

args = sys.argv
bdir = os.environ["BINPATH"]

if len(args) < 3:
    raise Exception("\n\nMust include option and file" +
                    "\n\nOptions:" +
                    "\nset f t     set type of file f to t." +
                    "\nget f   get type of file f."
                   )
contents = None
with open("%s/.meta/filetypes" % bdir, 'r') as f:
    contents = f.read().split('\n')
if args[1] == 'set':
    i = 0
    for line in contents:
        line = line.split()
        if line and line[0] == args[2]:
            line[1] = args[3]
            contents[i] = ' '.join(line)
            break
        i += 1
    else:
        contents.append('%s %s' % (args[2], args[3]))
        with open("%s/.meta/filetypes" % bdir, 'w') as f:
            f.write('\n'.join(contents))
elif args[1] == 'get':
    for line in contents:
        line = line.split()
        if line and line[0] == args[2]:
            print line[1]
            break
    else:
        with open("%s/.meta/filetypes" % bdir, 'a') as f:
            f.write("\n%s sh" % args[2])
        print 'sh'
elif args[1] == 'del':
    i = 0
    for line in contents:
        line = line.split()
        if line and line[0] == args[2]:
            break
        i += 1
    if i < len(contents):
        contents.pop(i)
        with open("%s/.meta/filetypes" % bdir, 'w') as f:
            f.write('\n'.join(contents))
