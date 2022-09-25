#include<stdio.h>
#include<math.h>
#include<complex.h>
#define PI 3.141592654
typedef double complex cplx;

void splitter(cplx sig[], cplx temp[], int n, int step)
{
	if (step<n) 
    {
		splitter(temp, sig, n, 2*step);
		splitter(temp + step, sig + step, n, 2*step);
 
		for (int i = 0; i<n; i+=2*step) 
        {
			cplx t = cexp(-I * PI * i/n) * temp[i + step];
			sig[i/2] = temp[i] + t;
			sig[(i+n)/2] = temp[i] - t;
		}
	}
}
 
void fft(cplx sig[], int n)
{
	cplx temp[n];
	for (int i = 0; i<n; i++) 
    {
        temp[i] = sig[i];
    }
 
	splitter(sig, temp, n, 1);
}

int main()
{
    cplx sig[] = {0,1,2,3,4,3,2,0};
    fft(sig,8);
    for (int i = 0; i<8; i++)
    {
        printf("%g + %gi \n",creal(sig[i]), cimag(sig[i]));
    }
}