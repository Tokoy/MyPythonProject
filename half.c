#include <stdio.h>
#include <stdlib.h>

int main(int argc,char **argv){
    int n = 0,i,j;
    int num_game;
    
    num_game=atoi(argv[1]);
    
    for(j=1;j<=num_game;++j){
        int bet=5000;
        int sum=0;
        
        for(i=1;i<=9;++i){
            bet=(bet>n?bet:bet/2);
            sum+=bet;
            if (sum > 10000) {
                bet = 0;
            }
            printf("%d\n",bet); //2-9
            fflush(stdout);
            
            scanf("%d",&n);
        }
        
        bet=(sum>=10000?0:10000-sum);
        printf("%d\n",bet); //10
        fflush(stdout);
        sum+=bet;
        scanf("%d",&n);
    }
    
    exit(EXIT_SUCCESS);
}
