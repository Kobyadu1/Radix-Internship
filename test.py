import csv
from Radix_2019_Internship.invoice import Invoice
import time


def numberparse(numberstring):
    seperated = numberstring.split(',')
    index1 = seperated[0].split('$')[1]
    seperated.pop(0)
    seperated.append(index1)
    seperated.reverse()
    ret = ''.join(seperated)
    return float(ret)


def parse(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            if row[0] != 'Invoice' and row[11] != "Paid":
                invoicenumber = numberparse(row[7])
                if invoicenumber <= value:
                    invoicenumber = int(invoicenumber * 100)

                    cents = int(str(invoicenumber)[-2:])
                    if cents == 0:
                        cents = 100

                    tempinvoice = Invoice(invoicenumber,row[0],cents)
                    invoicelist.append(tempinvoice)


def subset_sum(numbers, target, partial=[]):
    if invoicesum(partial,"value")>value:
        return
    s = invoicesum(partial,"cents")
    #for obj in partial:
    #    print(obj)
    # check if the partial sum is equals to target
    if s == target:
        if value == invoicesum(partial,"value"):
            for obj in partial:
                print(obj)

    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i + 1:]
        #print(str(len(remaining))+" "+str(len(numbers))+" "+str(i)+" "+str(len(partial)))
        subset_sum(remaining, target, partial + [n])


def invoicesum(invoices,para):
    total = 0
    if para == "cents":
        for q in invoices:
            total += q.cent
    if para == "value":
        for w in invoices:
            total += w.value
    return total


def subsetsum(A, N):
    res = {0 : []}
    for i in A:
        newres = dict(res)
        for v, l in res.items():
            if v+i < N:
                newres[v+i] = l+[i]
            elif v+i == N:
                return l+[i]
        res = newres
    return None

if __name__ == "__main__":
    possiblelist = list()
    invoicelist = []
    value = float(input("Enter a value: "))
    parse('Dataset.csv')
    value = int(value * 100)
    starttime = time.time()
    subset_sum(invoicelist, 85)
    for x in range(int(str(value)[-2:]), invoicesum(invoicelist,"cents"), 100):
        subset_sum(invoicelist, x)
    endtime = time.time()
    print(endtime-starttime)
