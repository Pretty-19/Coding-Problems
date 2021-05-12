class Solution {
   
	    public double average(int[] salary) {
        double sum = 0;
        Arrays.sort(salary);
        for(int i=0;i<salary.length;i++){
            System.out.println(salary[i]);
        }
        for(int i=1;i<salary.length-1;i++){
            sum = sum+salary[i];
        }
        return (sum/(salary.length-2));
    } 
    public static void main(String args[]) {
        int salary[] = [4000,3000,1000,2000];
    }
}