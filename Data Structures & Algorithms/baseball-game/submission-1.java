class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stack=new Stack<>();
        int sum=0;
        for(String ops:operations){
            if(ops.equals("C")){
                sum=sum-stack.pop();
            }
            else if(ops.equals("D")){
                int d=stack.peek()*2;
                stack.push(d);
                sum=sum+d;
            }
            else if(ops.equals("+")){
                int lastelement=stack.pop();
                int secondlast=stack.peek();
                stack.push(lastelement);
                int s=lastelement+secondlast;
                stack.push(s);
                sum=sum+s;
            }
            else{
                stack.push(Integer.parseInt(ops));
                sum=sum+Integer.parseInt(ops);
            }
        }
        return sum;
    }
}