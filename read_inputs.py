import DoubleLinkedList as DLList
import Functions as F
import csv

_par_sigla_pais = {};

def read_csv_files():
    """ Ler os dados do ficheiro """
    i = 0
    data_list = []
    with open('dados.csv','r') as fp:
        csvreader = csv.reader(fp,delimiter=";", quotechar='"')
        for row in csvreader:
            list = ('|'.join(row)).split('|')
            data_list.append(list)
            _par_sigla_pais[data_list[i][0]] = data_list[i][1]
            i = i + 1
    """ Retorna toda a informcao do ficheiro numa lista """
    return data_list

def read_inputs():
    data = read_csv_files()
    DList = DLList.DoubleLinkedList()
    Function = F.Functions(1,DList,_par_sigla_pais)

    """ Cada no vai ter informacao sobre um pais """
    for i in range(len(data)-1):
        DList.add_end(data[i])

    print("Search")
    with open("search_country.txt", "r") as f:
        for line in f:
            #print(line[:-1])
            Function.search(line[:-1])
    print("Insert\n")
    with open("insert_country.txt", "r") as f:
        for line in f:
            new_l = line.split(" ")
            #print(new_l[1][:-1])
            Function.inser_new_country(new_l[0],new_l[1][:-1])

    print("Remove\n")
    with open("remove.txt","r") as f:
        for line in f:
            Function.remove_country(line[:-1])

    print("Edit\n")
    with open("edit.txt","r") as f:
        for line in f:
            new_l = line.split("#")
            print(new_l[0])
            Function.edit(new_l[0],int(new_l[1]),new_l[2][:-1])

if __name__ == '__main__':
    read_inputs()
