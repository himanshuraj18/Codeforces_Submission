#include <iostream>
#include <cstdio>
#include <string>
#include <cctype>
using namespace std;
bool isVowel(char c)
{
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'y');
}
int main ()
{
    string input;
    cin >> input;
 
    for ( int i = 0; i < input.size(); i++ ) 
    {   if (!isVowel(tolower(input[i])))
        {   printf(".%c", tolower(input[i]));
        }
    }
    printf ("\n");
    return 0;
}