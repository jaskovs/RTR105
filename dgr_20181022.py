# coding: utf-8
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
get_ipython().run_line_magic('save', 'dgr_20181022.py')
get_ipython().run_line_magic('save', 'dgr_20181022 1-40')
