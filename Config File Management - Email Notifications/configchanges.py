#Defining the file from yesterday, for comparison.
device_cfg_old = 'cfgfiles/' + ip + '_' + (datetime.date.today() - datetime.timedelta(days = 1)).isoformat()
 
#Writing the command output to a file for today.
with open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'w') as device_cfg_new:
    device_cfg_new.write(output + '\n')
 
 
#Extracting the differences between yesterday's and today's files in HTML format
with open(device_cfg_old, 'r') as old_file, open('cfgfiles/' + ip + '_' + datetime.date.today().isoformat(), 'r') as new_file:
    difference = difflib.HtmlDiff().make_file(fromlines = old_file.readlines(), tolines = new_file.readlines(), fromdesc = 'Yesterday', todesc = 'Today')
