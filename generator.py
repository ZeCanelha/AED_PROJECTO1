import  random
import csv
import string

def read_csv_files():
    """ Ler os dados do ficheiro """
    i = 0
    data_list = []
    with open('dados.csv','r') as fp:
        csvreader = csv.reader(fp,delimiter=";", quotechar='"')
        for row in csvreader:
            list = ('|'.join(row)).split('|')
            data_list.append(list[0])
    return data_list

def generate():
    countries = read_csv_files()
    countries = countries[1:]
    year = []
    listt = []
    starting_year = 1960
    for i in range(56):
        year.append(starting_year + i)

    abc = ["ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    fp = open('search_sigla.txt',"w")
    for i in range(1000):
        siglas_txt = abc[0][random.randint(0,24)] +  abc[0][random.randint(0,24)] + abc[0][random.randint(0,24)]
        fp.write(siglas_txt)
        fp.write("\n")
        if ( i % 10 == 0 ):
            listt.append(siglas_txt)
    fp.close()

    size = len(countries) - 1

    fp = open("search_country.txt", "w")
    for i in range(len(countries) -1 ):
        fp.write(countries[random.randint(0,size)])
        fp.write("\n")
    fp.close()

    fp = open("insert_country.txt","w")
    for i in range(1000):
        siglas_txt = abc[0][random.randint(0,24)] +  abc[0][random.randint(0,24)] + abc[0][random.randint(0,24)]
        rand_str = lambda n: ''.join([random.choice(string.lowercase) for i in xrange(n)])
        fp.write(rand_str(8) + " " + siglas_txt)
        fp.write("\n")
    fp.close()

    fp = open("edit.txt", "w")
    for i in range(100):
        fp.write(countries[random.randint(0,size)] + "#" + str(year[random.randint(0,55)]) + "#" + str(random.random()))
        fp.write("\n")
    fp.close()

    fp = open("remove.txt","w")
    for i in range(len(listt) - 1):
        fp.write(listt[i] + "\n")
    fp.close()




if __name__ == '__main__':
    generate()
