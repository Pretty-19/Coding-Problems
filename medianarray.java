
import java.util.*;
public class Solution {



	static int getMedian(
		int[] a, int[] b, int startA,
		int startB, int endA, int endB)
	{
		if (endA - startA == 1) {
			return (
					Math.max(a[startA],
								b[startB])
					+ Math.min(a[endA], b[endB]))
				/ 2;
		}
	
		int m1 = median(a, startA, endA);


		int m2 = median(b, startB, endB);

	
		if (m1 == m2) {
			return m1;
		}

	
		else if (m1 < m2) {
			return getMedian(
				a, b, (endA + startA + 1) / 2,
				startB, endA,
				(endB + startB + 1) / 2);
		}


		else {
			return getMedian(
				a, b, startA,
				(endB + startB + 1) / 2,
				(endA + startA + 1) / 2, endB);
		}
	}

	static int median(
		int[] arr, int start, int end)
	{
	    int mid,ind,ans;
		int n = end - start + 1;
		System.out.println(start);
		System.out.println(end);
		System.out.println(n);
		if (n % 2 == 0) {
		    mid=(arr[start + (n / 2)]+ arr[start + (n / 2 - 1)])/ 2;
		    System.out.println(mid);
			return (mid);
		}
		else {
		    ind=(start + n / 2);
		    System.out.println("index is: "+ind);
		    mid= arr[ind];
			return (mid);
		}
	}


	public static void main(String[] args)
	{
		int ar1[] = {1, 12, 15, 26, 38};
		int ar2[] = {2, 13, 17, 30, 45};
		int n1 = ar1.length;
		int n2 = ar2.length;
		if (n1 != n2) {
			System.out.println(
				"unequal");
		}
		else if (n1 == 0) {
			System.out.println(" empty");
		}
		else if (n1 == 1) {
			System.out.println((ar1[0] + ar2[0]) / 2);
		}
		else {
			System.out.println(
				"Median is "
				+ getMedian(
					ar1, ar2, 0, 0,
					ar1.length - 1, ar2.length - 1));
		}
	}
}
