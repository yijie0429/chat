

#讀取檔案
def read_file(filename):
    lines = []
    with open (filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

#轉換檔案
def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:  
            new.append(person + ': ' + line)
    return new     
def write_file(filename,lines):
    with open (filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


#只要讀取到的是人名，那就先保留(person)，然後讀取下一個清單，如果是對話，那就和目前的person一起印出來，再繼續讀取下一個清單
#ex:第一次讀取到Allen，先存成person, continue讀取下一個清單，然後讀取到'你好'，那就person:'Allen'和讀取到的'你好'一起印出來，然後再讀取下一個清單，如果現在讀取
#到'Tom'，那person就會變'Tom'，然後continue讀取下一個清單，同上
        
def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt',lines)
    
main()   

                    







