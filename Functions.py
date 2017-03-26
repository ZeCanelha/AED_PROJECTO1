import DoubleNode as DoubleNode
import DoubleLinkedList as DLList


class Functions:
    """ Search , Insert , Edit and Remove """
    """ 1 - Being Double Linked Lists"""
    def __init__(self, data, data_type, par_country_sigla):
        self.data = data
        self.data_structure = data_type
        self.par_country_sigla = par_country_sigla

    def search(self, country):
        """ Se a len do country for maior que 3 estamos a procurar um pais pela sigla """
        if ( self.data == 1 ):
            if ( len(country) == 3):
                #Search by code
                return self.data_structure.binary_search(country,1)
            else:
                sigla = self.par_country_sigla[country]
                return self.data_structure.binary_search(sigla,1)

    def inser_new_country(self, country, sigla ):
        data = [ "" for i in range(58) ]
        data.insert(0,country)
        data.insert(1,sigla)
        self.par_country_sigla[country] = sigla



        return self.data_structure.inser_new_country(sigla,data)

    def insert(self, country, key , data):
        if ( self.data == 1 ):
            if ( len(country) == 3 ):
                return self.data_structure.insert_element(country,key,data,1)
            else:
                sigla = self.par_country_sigla[country]
                return self.data_structure.insert_element(sigla,key,data,1)
        if ( self.data == 2):
            if ( len(country) > 3 ):
                #Search by name
                print("A")
            if ( len(country) == 3):
                #Search by code
                print("A")
        if ( self.data == 3 ):
            if ( len(country) > 3 ):
                #Search by name
                print("A")
            if ( len(country) == 3):
                #Search by code
                print("A")


    def edit(self, country , key , data):
        if ( self.data == 1 ):
            if ( len(country) == 3 ):
                return self.data_structure.edit_element(country,key,data,1)
            else:
                sigla = self.par_country_sigla[country]
                return self.data_structure.edit_element(sigla,key,data,1)
        if ( self.data == 2):
            if ( len(country) > 3 ):
                #Search by name
                print("A")
            if ( len(country) == 3):
                #Search by code
                print("A")
        if ( self.data == 3 ):
            if ( len(country) > 3 ):
                #Search by name
                print("A")
            if ( len(country) == 3):
                #Search by code
                print("A")


    def remove(self , country, key ):
        if ( self.data == 1 ):
            if ( len(country) == 3 ):
                return self.data_structure.remove_element(country,key,1)
            else:
                sigla = self.par_country_sigla[country]
                return self.data_structure.remove_element(sigla,key,1)

    def remove_country( self,country ):
        if ( self.data == 1):
            if ( len(country) == 3):
                return self.data_structure.remove_country(country,1)
            else:
                sigla = self.par_country_sigla[country]
                return self.data_structure.remove_country(country,1)
