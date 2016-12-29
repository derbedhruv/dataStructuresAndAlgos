/*
 * CUSTOM DATA STRUCTURE IMPLEMENTATION - PRACTICE PLAYGROUND
 */

#include <iostream>
#include <stdio.h>
#include "linkedlists/linked_list.h"

using namespace std;

int main() {
  cout << "Will be implementing a simple Linked List." << endl;
  node *newnode = new(struct node);
  sLinkedList one = sLinkedList(5);
  one.append(3);
  one.append(44);
  one.append(0);
  one.append(3);

  one.print();

  one.remove(5);
  one.print();

}