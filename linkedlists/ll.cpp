/*
*  LINKED LIST IMPLEMENTATION
*  ------------------------------
*  Author: Dhruv Joshi
*  Practicing implementation of Linked Lists
*/

#include <iostream>
#include <stdio.h>

using namespace std;

// node DEFINITION
// structs are named in camelCase by convention
struct node{
  /*
     A node is a single element of a linked list. 
     It has a value/key and a pointer "next" which points to the next element
     By default, next is NULL.
   */
  int value;
  struct node *next; 
};


class sLinkedList {
  /*
    The Linkedlist class implements a singly linked list
  */
  struct node *start;

  public:
    sLinkedList (int value);
    void append(int value);
    void print();
};

sLinkedList::sLinkedList (int value) {
  // Constructor for a linkedlist
  // add value to the start node, make it point to NULL
  start = new(struct node);
  start->value = value;
  start->next = NULL;
}

void sLinkedList::append(int value) {
  // append to the end of the linked list
  // traverse the list, go to the end and insert element
  struct node *currentNode = start;

  while(currentNode->next != NULL) {
    currentNode = currentNode->next;
  }

  struct node *temp = new(struct node);
  temp->value = value;
  temp->next = NULL;
  currentNode->next = temp;
}

void sLinkedList::print() {
  // print out the elements of the singly linked list
  struct node *currentNode = start;

  while(currentNode->next != NULL) {
    cout << currentNode->value << "->";
    currentNode = currentNode->next;
  }
  cout << currentNode->value << "->NULL" << endl;
}


int main() {
  cout << "Will be implementing a simple Linked List." << endl;
  node *newnode = new(struct node);
  sLinkedList one = sLinkedList(5);
  one.append(3);
  one.append(44);
  one.append(0);

  one.print();
}
