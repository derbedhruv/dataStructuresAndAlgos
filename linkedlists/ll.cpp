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
     By default, next is NULL. In this implementation, the node only contains a single INT.
   */
  int value;
  struct node *next; 
};


class sLinkedList {
  /*
    Implements a singly linked list, which chains nodes together.
    Private elements:
    ==============================================================
    start   - A pointer to the first node
    last    - A pointer to the last element of the linked list (used for internal methods)
    length  - The length of the linked list (updated with each append)

    Public methods:
    ==============================================================
    - Constructor
    - Appending a new element to the end of the linked list
    - printing the linked list
    - finding an element in the linked list, and returning a pointer to it
  */
  struct node *start;
  struct node *last;
  int length;

  public:
    sLinkedList (int value);
    void append(int value);
    void print();
    struct node *find(int key, bool print);
};

sLinkedList::sLinkedList (int value) {
  // Constructor for a linkedlist
  // add value to the start node, make it point to NULL
  start = new(struct node);
  start->value = value;
  start->next = NULL;

  length = 0;   // initial length of the linked list

  last = start;
}

void sLinkedList::append(int value) {
  // append to the end of the linked list
  // start by getting the pointer to the element with the given value
  // create last node as a seperate node
  struct node *temp = new(struct node);
  temp->value = value;
  temp->next = NULL;

  // break the chain and append to the linked list
  last->next = temp;

  // update the pointer to last element
  last = temp;
}

void sLinkedList::print() {
  find(-1, true);
}

struct node * sLinkedList::find(int key, bool print = false) {
  // find a node in the linked list which has value == key, and return a pointer to it.
  // The parameter 'print' toggles whether to print out the elements as it is traversing the list
  // ========================================================================================
  /* TODO: Handle the case when the element doesn't exist */
  struct node *currentNode = start;

  while(currentNode->value != key) {
    if (print) {
      // print flag is TRUE, print values as nodes are traversed
      cout << currentNode->value << "->";
    }

    currentNode = currentNode->next;

    if (currentNode->next == NULL) {
      // reached the end, break and return NULL, i.e. this key was not found
      if (print) {
        cout << currentNode->value << "->NULL" << endl;
      }
      return NULL;
    }
  }

  if (print) {
    cout << currentNode->value << "->NULL" << endl;
  }
  return currentNode;
}


int main() {
  cout << "Will be implementing a simple Linked List." << endl;
  node *newnode = new(struct node);
  sLinkedList one = sLinkedList(5);
  one.append(3);
  one.append(44);
  one.append(0);
  one.append(3);

  one.print();

  // one.find(3, true);
}
