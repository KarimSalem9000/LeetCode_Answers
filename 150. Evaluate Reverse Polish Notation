class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> cake = new Stack<Integer>();
        for(String s:tokens){
            int right;
            if(s.equals("+")){
                right = cake.pop();
                cake.push(cake.pop()+right);
            }
            else if(s.equals("-")){
                right = cake.pop();
                cake.push(cake.pop()-right);
            }
            else if(s.equals("*")){
                right = cake.pop();
                cake.push(cake.pop()*right);
            }
            else if(s.equals("/")){
                right = cake.pop();
                cake.push(cake.pop()/right);
            }
            else{
                cake.push(Integer.parseInt(s));
            }           
        }
        return cake.pop();

        
    }
}
