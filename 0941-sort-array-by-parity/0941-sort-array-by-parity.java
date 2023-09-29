class Solution {
    public int[] sortArrayByParity(int[] arr) {
    
				int right = arr.length -1;
				int left = 0;
				while(left!=right)
				{
					if(arr[left] % 2 == 1 )
					{
						int temp = arr[right];
						arr[right] = arr[left];
						arr[left] = temp;
						right--;
					}
					else
					{
						left++;
					}
				}
        return arr;
        
    }
}