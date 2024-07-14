import java.util.*;
public class try1
{
    static Scanner in= new Scanner(System.in);
    static int month=1,d=0,r=0,day=6;
    static long rep=1,year=0;
    static String m[]= {"January","February","March","April","May","June","July","August","September","October","November","December"};
    static String mat[][]= new String[6][7];
    public void display()
    {
     if(rep==year)
     {
     System.out.println();
     System.out.println("      "+m[month-1]);
     System.out.println("--------------------");
     System.out.println("Su|Mo|Tu|We|Th|Fr|Sa");
     System.out.println("--------------------");
     for(int i=0;i<6;i++)
            {
                for(int j=0;j<7;j++)
                {
                 if(mat[i][j]==null)
                 System.out.print("   ");
                 else
                 System.out.print(mat[i][j]+" ");
                }
                System.out.println();
            }
        }
    }
    public static void main(String args[])
    {
        try1 ob= new try1();
        System.out.print("Enter the year in numeric to get its calendar: ");
        year= in.nextLong();
        while(rep<=year)
        {
            month= 1;
            while(month<=12)
            {
            d++;
            if((d==3) && (month==9) && (rep==1752))
            {
            d=14;
            day=4;
            }
            if(d<10)
            mat[r][day]= "0"+d;
            else
            mat[r][day]= d+"";
            day++;
            if(day>6)
            {
            day=0;
            r++;
            }
            if((d==31)&&((month==1)||(month==3)||(month==5)||(month==7)||(month==8)||(month==10)))
            {
             ob.display();
             mat= new String[6][7];
             r=0;
             d=0;
             month++;
            }
            else if((d==30)&&((month==4)||(month==6)||(month==9)||(month==11)))
            {
                ob.display();
                mat= new String[6][7];
                r=0;
                d=0;
                month++;
            }
            else if(month==2)
            {
               if((d==28)&&(((rep%100!=0)&&(rep%4!=0))||((rep%100==0)&&((rep>=1700)&&(rep%400!=0)))))
               {
                ob.display();
                mat= new String[6][7];
                r=0;
                d=0;
                month++;
               }
               if((d==29)&&(((rep%100!=0)&&(rep%4==0))||((rep%100==0)&&(rep%400==0)&&(rep>=1700))||((rep%100==0)&&(rep<1700))))
               {
                ob.display();
                mat= new String[6][7];
                r=0;
                d=0;
                month++;
               }
            }
            else if((month==12)&&(d==31))
            {
                ob.display();
                mat= new String[6][7];
                r=0;
                d=0;
                month++;
                rep++;
            }
            }
            }
        }
    }