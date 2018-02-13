#include <bits/stdc++.h>
using namespace std;
int main()
{
    srand(time(0));
    int counter = 1,limit =21,x,mode;
    cout<<"enter 1-play against computer or 2-multiplayer mode"<<endl;
    cin>>mode;
    while (mode!=1 && mode!=2)
    {
        cout<<"please enter 1 or 2 only"<<endl;
        cin>>mode;
    }
    cout<<"limit = "<<limit<<endl;
    while (limit>0)
    {
        if (counter%2==1)
        {
            cout<<"player 1 : ";
            cin>>x;
        }
        else
        {
            if (mode==2)
            {
                cout<<"player 2 : ";
                cin>>x;
            }
            else
            {
                cout<<"computer : ";
                x=1+rand()%3;
            }
        }
        while (x>3||x<1||x>limit)
        {
            if(mode==2)
            {
                cout<<"try again"<<endl;
                cin>>x;
            }
            else
                x=1+rand()%3;
        }
        if(counter%2==0 && mode==1)
            cout<<x<<endl;
        limit-=x;
        cout<<"reminder = "<<limit<<endl;
        if (limit>0)
            counter++;
        else
        {
            if (counter%2==1 && mode==2)
                cout<<"player 2 won"<<endl;
            else if (counter%2==1 && mode==1)
                cout<<"computer won"<<endl;if (counter%2==1 && mode==2)
            else
                cout<<"player 1 won"<<endl;
        }
    }
    return 0;
}

