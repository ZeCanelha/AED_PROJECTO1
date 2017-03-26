import csv
import DoubleNode as DoubleNode
import DoubleLinkedList as DLList
import Functions as F
import re as split

#TODO Criar um dicionario com os pares de Pais / Sigla

_par_sigla_pais = {};

def create_ddlist(data):
    DList = DLList.DoubleLinkedList()
    Function = F.Functions(1,DList,_par_sigla_pais)

    """ Cada no vai ter informacao sobre um pais """
    for i in range(len(data)-1):
        DList.add_end(data[i])

    while(1):
        print("\t\tDouble Linked Lists\n\n\t1.Search Element\n\t2.Insert Element\n\t3.Edit Element\n\t4.Remove Element\n\t5.Main Menu\n\t6.Print")
        opt = input()
        """ Search """
        if ( opt == 1 ):
            print("Country Name or Country Code:")
            response = raw_input()
            print("Index: %s\n" % Function.search(response))
        """ Insert: Vai dar pra inserir tudo  """
        if ( opt == 2):
            #Inserir um novo pais implica inserir um pais + sigla e um array de anos vazios 1960-2016 | 46 posicoes
            print("1. Insert new country\n")
            print("2. Insert new data on existent countries\n")
            new_opt = input()
            if ( new_opt == 1 ):
                print("Country name: ")
                country = raw_input()
                print("Sigla: ")
                sig = raw_input()
                print(Function.inser_new_country(country,sig))
            if ( new_opt == 2 ):
                print("Country: ")
                country = raw_input()
                print("Year: ")
                year = input()
                print("Data: ")
                data = input()
                Function.insert(country,year,data)
        """ Edit: Penso que seja so editar funcoes em determinados anos """
        if ( opt == 3):
            print("Country: ")
            country = raw_input()
            print("Year: ")
            year = input()
            print("Data: ")
            data = input()
            print(Function.edit(country,year,data))
        """ Remove: Remove deve ser como insert, remover tudo """
        if ( opt == 4):
            print("1.Remove Country")
            print("2.Remove information")
            opt1 = input()
            if ( opt1 == 1 ):
                print("Country: ")
                country = raw_input()
                print(Function.remove_country(country))
                DList.print_list()
            if ( opt1 == 2 ):
                print("Country: ")
                country = raw_input()
                print("Year: ")
                year = input()
                print(Function.remove(country,year))
        if opt == 6:
            DList.print_list()
        if ( opt == 5):
            break

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

def init():
    data = read_csv_files()
    while(1):
        print("\t\tMenu\n\n\t1.Double Linked Lists\n\t2.Exit")
        opt = input()
        if ( opt == 1 ):
            create_ddlist(data)
        if ( opt == 2):
            break;



if __name__ == '__main__':
    init()
