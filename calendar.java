import java.util.Scanner;

public class calendar{
    //Declaring global entities to be used
    static Scanner in= new Scanner(System.in);
    static int month=1,d=0,r=0,day=6;
    static long rep=1,year=0;
    //Array with month names to be displayed on the top of every months array in the calendar
    static String m[]= {"January","February","March","April","May","June","July","August","September","October","November","December"};
    static String mat[][]= new String[6][7];
    //Function to clear the array for next month
    public void clear(){
      display();
      mat= new String[6][7];
      r=0;
      d=0;
      month++;}
    //Function to display the current month values in an array
    public void display(){
     if(rep==year){
     System.out.println();//Decorating the calendar with some basic lines
     System.out.println("      "+m[month-1]);
     System.out.println("--------------------");
     System.out.println("Su|Mo|Tu|We|Th|Fr|Sa");
     System.out.println("--------------------");
     for(int i=0;i<6;i++){
      for(int j=0;j<7;j++){
       if(mat[i][j]==null)//For those dates which starts from middle of week
        System.out.print("   ");
       else
        System.out.print(mat[i][j]+" ");}
        System.out.println();}}}

    public static void main(String args[]){
        calendar ob= new calendar();//To call the above functions
        System.out.print("Enter the year in numeric to get its calendar: ");
        year= in.nextLong();
        while(rep<=year){//Repetition till the process reach the entered year for its calendar 
            month= 1;
            while(month<=12){//Repetition of array filling till next year starts rep=rep+1
            d++;
            if((d==3) && (month==9) && (rep==1752)){ //For the missing 11 days from the past calendars
            d=14;
            day=4;}
            if(d<10)//Converting single digit dates to double digit
            mat[r][day]= "0"+d;
            else
            mat[r][day]= d+"";
            day++;
            if(day>6){//Logic to start the new week day=0
            day=0;
            r++;}
            //Changing the month if previous one was of 31 days
            if((d==31)&&((month==1)||(month==3)||(month==5)||(month==7)||(month==8)||(month==10)))
             ob.clear();
            //Changing the month if previous one was of 30 days
            else if((d==30)&&((month==4)||(month==6)||(month==9)||(month==11)))
              ob.clear();
            //Changing the month if previous one was of February
            else if(month==2){
               //Logic for non-leap years containing 28 days in February and 365 days in the year
               if((d==28)&&(((rep%100!=0)&&(rep%4!=0))||((rep%100==0)&&((rep>1700)&&(rep%400!=0)))))
                ob.clear();
               //Logic for leap years containing 29 days in February and 366 days in the year
               else if((d==29)&&(((rep%100!=0)&&(rep%4==0))||((rep%100==0)&&(rep%400==0)&&(rep>1700))||((rep%100==0)&&(rep<=1700))))
                ob.clear();}
            //Changing the month to January in the beginning of the outer loop's body and year here
            else if((month==12)&&(d==31)){
                ob.clear();
                //Increase in rep means changing the year from one ahead to continue the process
                rep++;}}}}}