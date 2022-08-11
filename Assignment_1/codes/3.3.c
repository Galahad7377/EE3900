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

    FILE *x_val;
    FILE *y_val;
    x_val = fopen("3.3x.txt","w");
    y_val = fopen("3.3y.txt","w");
    for(int i=0; i<6; i++)
    {
        fprintf(x_val,"%f ", x[i]);
    }
    for(int i=0; i<20; i++)
    {
        fprintf(y_val,"%f ", y[i]);
    }
    fclose(x_val);
    fclose(y_val);

}