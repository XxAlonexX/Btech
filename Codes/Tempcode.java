public class Tempcode{
    public static void main(String[] args){
    int score[][] = {
    {2,4,5,6,},
    {3,56,2,5,},
    {3,5,6,1}
    };
    System.out.println("Scores");
    for(int i =0;i<score.length;i++){
    System.out.println("Player" +(i+1) + " ");
    for(int j = 0 ; j < score[i].length ; j++){
    System.out.println(score[i][j]);
    }
    }
    }
}