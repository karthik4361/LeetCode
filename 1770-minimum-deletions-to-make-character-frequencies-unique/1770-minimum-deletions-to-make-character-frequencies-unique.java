class Solution {
    public int minDeletions(String s) {

        int[] frequency = new int[26];

        for(int i =0;i<s.length();i++)
        {
            frequency[s.charAt(i)-'a']++;
        }

        Arrays.sort(frequency);
        int maxFrequencyAllowed = s.length();
        int numDeletions =0;

        for(int i= 25;i>=0 && frequency[i]>0;i--)
        {
            if(frequency[i] > maxFrequencyAllowed)
            {
               numDeletions += frequency[i] - maxFrequencyAllowed; 
               frequency[i] =  maxFrequencyAllowed; 
             
            }
            maxFrequencyAllowed = Math.max(0, frequency[i] - 1);


        }
        return  numDeletions;
        
    }
}