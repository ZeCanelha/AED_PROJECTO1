#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from DoubleNode import DoubleNode
#TODO: Catch para aceder a posicoes do array
#TODO: Actualizar os valores do array; Alterar a insert sem a binary_search
class DoubleLinkedList:
   size = 0
   var = 1958
   def __init__(self):
      self.head = None
      self.tail = None

   def is_empty(self):
      return self.head == None

   def add_beginning(self, item):
      temp = DoubleNode(item)
      if (self.head == None):
         self.head = self.tail = temp
      else:
         temp.set_prev(None)
         temp.set_next(self.head)
         self.head.set_prev(temp)
         self.head=temp
      DoubleLinkedList.size += 1

   def add_end(self, item):
         if (self.head == None):
            self.head = DoubleNode(item)
            self.tail=self.head
         else:
            current=self.head

            while(current.get_next() != None):
               current = current. get_next()
            current.set_next(DoubleNode(item, None, current))
            current.get_next().set_prev(current)
            self.tail = current.get_next()
         DoubleLinkedList.size += 1
         return self

   def get_node(self, index):
      currentNode = self.head
      if currentNode == None:
         return None
      i=0
      while i<index and currentNode.get_next()!= None:
         currentNode = currentNode.get_next()
         if currentNode == None:
            break
         i=i+1
      return currentNode

   def print_list(self):
      currentNode = self.head
      if currentNode == None:
         return 0
      print(currentNode.get_data())
      while currentNode != None:
         currentNode = currentNode.get_next()
         if currentNode != None:
            print(currentNode.get_data())

   def double_list_length(self):
      currentNode = self.head
      if currentNode == None:
         return 0
      count=1
      currentNode = currentNode.get_next()
      while currentNode != None:
         currentNode = currentNode.get_next()
         count = count + 1
      return count

   def par_length_list(self):
      current = self.head
      while current != None and current.get_next() != None:
         current = current.get_next().get_next()
         if current == None:
            return 1
      return 0



   def binary_search(self,item,i):
      begin = self.head
      tail = self.tail
      max_size = DoubleLinkedList.size
      min_size = 0
      start_time = time.time()
      """ Prints the result of the search in case of success and returns node index"""


      while( min_size <= max_size ):
          p_med = (min_size + max_size) / 2

          med = self.get_node(p_med)
          info = med.get_data()

          if ( info[i] == item ):
              print("%s" %(time.time() - start_time))
              return p_med
          if ( item > info[i] ):
              min_size = p_med + 1
          else:
              max_size = p_med - 1
      return -1


   def edit_element(self, country, key, data, i):
       """ Altera a informacao de um determinado no """
       """ So anos """
       start_time = time.time()
       index = self.binary_search(country,i)
       if ( index == -1 ):
           return -1
       currentNode = self.head
       if currentNode == None:
           return None
       i=0
       while i<index and currentNode.get_next()!= None:
           currentNode = currentNode.get_next()
           if currentNode == None:
               break
           i=i+1
       if ( index == i and currentNode != None):
           old_data = currentNode.get_data()
           old_data[key - self.var] = str(data)
           newNode = DoubleNode(old_data)
           currentNode = newNode
           print("#%s" %(time.time() - start_time))
           return 1
       return -1

   def insert_element(self, country, key, data, i):

       start_time = time.time()
       index = self.binary_search(country,i)
       if ( index == -1 ):
           return -1

       currentNode = self.head
       if ( currentNode == None ):
           return None

       data1 = currentNode.get_data()
       pos = len(data1)
       for i in range(2,len(data1)):
           print(data1[i])
           if ( data1[i] > str(key) ):
               pos = i - 1
               break

       i=0
       while i < index and currentNode.get_next()!= None:
           currentNode = currentNode.get_next()
           if currentNode == None:
               break
           i=i+1
       if ( index == i and currentNode != None):
           old_data = currentNode.get_data()
           old_data.insert(pos,str(data))
           newNode = DoubleNode(old_data)
           currentNode = newNode
           print("Insert Data Search Time: %s " %(time.time() - start_time))
           return 1
       return -1




   def inser_new_country( self, sigla, data):
       """ Inserir ordenado por sigla """
       start_time = time.time()
       currentNode = self.head
       if ( currentNode == None ):
           return None

       if currentNode.get_next() == None:
           return None

       currentNode = currentNode.get_next()

       while currentNode.get_next()!= None:
           if ( currentNode.get_next() == None ):
               break
           aux = currentNode.get_next().get_data()
           if ( aux[1] < sigla ):
               currentNode = currentNode.get_next()
           else:
               next_node = currentNode.get_next()
               newNode = DoubleNode(data)
               currentNode.set_next(newNode)
               newNode.set_prev(currentNode)
               newNode.set_next(next_node)
               print("%s" %(time.time() - start_time))
               return 1
       return -1


   def remove_element(self, country, key, i):
       """ Remover informação """
       start_time = time.time()
       print(country)
       currentNode = self.head
       if currentNode == None:
           return None
       if currentNode.get_next() == None:
           return -1
       currentNode = currentNode.get_next()
       while( currentNode.get_next()!= None ):

           aux = currentNode.get_data()
           if ( aux[1] > country ):
               break
           if ( aux[1] != country):
               if ( currentNode.get_next() == None ):
                   break
               currentNode = currentNode.get_next()
           if ( aux[1] == country ):
               if ( aux[key - self.var] == '' or aux[key - self.var] == 0):
                   print("There is no information regarding year: {}.\n".format(key) )
                   return -1
               aux[key - self.var] = str(0)
               newNode = DoubleNode(aux)
               currentNode = newNode
               print("Remove Data Search Time: %s " %(time.time() - start_time))
               return 1

       return -1
   def remove_country(self, country , i):
       start_time = time.time()

       currentNode = self.head
       if currentNode == None:
           return None
       if currentNode.get_next() == None:
           return -1
       currentNode = currentNode.get_next()
       while( currentNode.get_next()!= None ):

           aux = currentNode.get_data()
           if ( aux[1] > country ):
               break
           if ( aux[1] != country):
               if ( currentNode.get_next() == None ):
                   break
               currentNode = currentNode.get_next()
           if ( aux[1] == country ):
               temp = currentNode
               if temp:
                   temp.get_prev().set_next(temp.get_next())
               if temp.get_next():
                   temp.get_next().set_prev(temp.get_prev())
                   temp.set_prev(None)
                   temp.set_next(None)
                   temp.set_data(None)

       print("%s" %(time.time() - start_time))
       return 1
