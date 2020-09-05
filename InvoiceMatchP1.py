import csv


def numberparse(numberstring):
    seperated = numberstring.split(',')
    index1 = seperated[0].split('$')[1]
    seperated.pop(0)
    seperated.append(index1)
    seperated.reverse()
    ret = ''.join(seperated)
    return float(ret)


def parse(filename,invoicedict,invoicevalue):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] != 'Invoice' and row[11]!= "Paid":
                invoicenumber = numberparse(row[7])
                if invoicenumber <= invoicevalue:
                    invoicedict[row[0]] = invoicenumber


def possiblelists(elements,amount,start):
    totalpossible = []
    listvalues = list(elements)
    if amount>0:
        i = start
        while i<=(len(listvalues)-amount):
            currentvalue = listvalues.copy().pop(i)
            newlists = possiblelists(listvalues,amount-1,start+1)
            for l in newlists:
                temp = l.copy()
                temp.append(currentvalue)
                totalpossible.append(temp)
            i += 1
    else:
        totalpossible.append([])
    return totalpossible


def filter(sum):
    possibles = list()
    possiblesret = list()
    for x in range(1,len(invoicedict)+1):
        for possibles in possiblelists(invoicedict.values(),x,0):
            if mysum(possibles) == sum:
                possiblesret.append(possibles)
    return possiblesret


def mysum(lis):
    total = 0
    for x in lis:
        total +=x
    return total


def returninvoice(valueslist):
    retlist = list()
    for x in invoicedict.keys():
        if invoicedict.get(x) in valueslist:
            retlist.append(x)
    return retlist


possiblelist = list()
invoicedict = dict()
value = float(input("Enter a value: "))
parse('Dataset.csv',invoicedict,value)
print(len(invoicedict))

for x in filter(value):
    print(returninvoice(x))


