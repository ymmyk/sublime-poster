# adapted from https://github.com/wbond/sublime_package_control/blob/master/Package%20Control.py
import commandline

def post(url, data, header):
    curl = commandline.find_binary('curl')
    if not curl:
        return False
    command = [curl, '-f', '--user-agent', 'Sublime Github', '-s', '-3', '--insecure']
    if data:
        command.append('-d')
        command.append(data)
    for k,v in header.iteritems():
        command.append('-H')
        command.append("%s: %s" % (k, v))
    command.append(url)

    print command

    return commandline.execute(command)