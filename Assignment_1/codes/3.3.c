#include<stdio.h>

int main()
{
    float x[6] = {1.0,2.0,3.0,4.0,2.0,1.0};
    int k =20;
    float y[20] = {0};

    y[0] = x[0];
    y[1] = -0.5*y[0]+ x[1];

    for (int i=2; i<k; i++)
    {
        if (i<6)
        {
            y[i] = -0.5*y[i-1]+x[i]+x[i-2];
        }
        else if (i>5 && i<8)
        {
            y[i] = -0.5*y[i-1]+x[i-2];
        }
        else
        {
            y[i] = -0.5*y[i-1];
        }
    }
    for (int i =0; i<20; i++)
    {
        printf("%f, ",y[i]);
    }

}