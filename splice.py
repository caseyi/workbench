import sys
taskf, itemf = sys.argv[1], sys.argv[2]
s = open(taskf, encoding='utf-8').read()
item = open(itemf, encoding='utf-8').read().strip('\n')
lines = s.split('\n')
# find the Active section header
ai = next(i for i, l in enumerate(lines) if l.strip() == '## Active')
# back up over any blank lines so the new item sits adjacent to existing Inbox items
j = ai
while j > 0 and lines[j-1].strip() == '':
    j -= 1
lines.insert(j, item)
open(taskf, 'w', encoding='utf-8').write('\n'.join(lines))
print('inserted before line', ai, '-> at', j)
