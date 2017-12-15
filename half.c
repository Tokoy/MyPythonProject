#include <stdio.h>
#include <stdlib.h>

/*二人零合ゲームとは一方勝つなら、もう一方は必ず負け、ゲーム双方の収益と損益は加えていつも零です*/
int main(int argc,char **argv){
    int n = 0,i,j,k,m,p;
    int num_game;
	int arr[10];
    num_game=atoi(argv[1]);
    /*num_game=2;*/
	int duelist[num_game][10];
    for(j=1;j<=num_game;++j){
        int bet=5000;
        int sum=0;

        for(i=1;i<=9;++i){
            bet=(bet<n?bet:bet/2);
            sum+=bet;
            if (sum > 10000) {
                bet = 0;
            }
            printf("%d\n",bet); //2-9
            fflush(stdout);
            
            scanf("%d",&n);
			arr[i-1]=n;
        }
        
        bet=(sum>=10000?0:10000-sum);
        printf("%d\n",bet); //10
        fflush(stdout);
        sum+=bet;
        scanf("%d",&n);
		arr[9]=n;
		for(m=0;m<10;m++){
			duelist[j-1][m]=arr[m];
		}
    }
    
	for(k=0;k<num_game;k++){
		for(p=0;p<10;p++){
			printf("Element[%d][%d] = %d\n", k, p,duelist[k][p]  );
		}
	}
    exit(EXIT_SUCCESS);
}
