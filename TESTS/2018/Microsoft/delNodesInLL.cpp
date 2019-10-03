
// C program to delete N nodes after M nodes of a linked list
#include <stdio.h>
#include <stdlib.h>
#include<iostream>
using namespace std;
struct Node
{
    int data;
    struct Node *next;
};
void push(struct Node ** head_ref, int new_data)
{
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->data  = new_data;
    new_node->next = (*head_ref);
    (*head_ref)  = new_node;
}

void printList(struct Node *head)
{
    struct Node *temp = head;
    while (temp != NULL)
    {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

void skipMdeleteN(struct Node  *head, int M, int N)
{
    struct Node *curr = head, *t;
    for (int i = 1; i<M && curr!= NULL; i++)
        curr = curr->next;
    t = curr->next;
    for (int i = 1; i<=N && t!= NULL; i++)
    {
        struct Node *temp = t;
        t = t->next;
        free(temp);
    }
    curr->next=t;
    curr=t;
}
int main()
{
    struct Node* head = NULL;
    int i,eleNo,M,N,ele;
    cin>>M>>N;
    cin>>eleNo;
    for(i=0;i<eleNo;i++){
      cin>>ele;
      push(&head, ele);
    }
    printList(head);
    skipMdeleteN(head, M, N);
    printList(head);
    return 0;
}
