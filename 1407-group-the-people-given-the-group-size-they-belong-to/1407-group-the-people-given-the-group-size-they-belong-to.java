import java.util.*;
class Solution {
    public List<List<Integer>> groupThePeople(int[] groupSizes) {

        SortedMap<Integer,List<Integer>> mp = new TreeMap<Integer,List<Integer>>();

        for(int i=0;i<groupSizes.length;i++)
        {
            if(mp.containsKey(groupSizes[i]))
            {
               mp.get(groupSizes[i]).add(i);
            }
            else
            {
                mp.put(groupSizes[i],new ArrayList<>(Arrays.asList(i)));
            }
        }

        List<List<Integer>> ans = new ArrayList<>();

        for (Map.Entry<Integer,List<Integer>> entry:mp.entrySet())
        {
            Integer key = entry.getKey();
            List<Integer> values = entry.getValue();
            int l= 0;
            List<Integer> lst= new ArrayList<Integer>();
            for(int i=0;i<values.size();i++)
            {
                l++;
                lst.add(values.get(i));
                if(l==key)
                {
                    l=0;
                    ans.add(new ArrayList<>(lst)); 
                    lst.clear();

                }

            }
            
        }

        return ans;
        
    }
}