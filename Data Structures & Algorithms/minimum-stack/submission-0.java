class MinStack {
    Stack<Integer> stack;
    Stack<Integer> aux;
    public MinStack() {
        stack=new Stack<>();
        aux=new Stack<>();
    }
    
    public void push(int val) {
        stack.push(val);
        if(aux.isEmpty()){
            aux.push(val);
        }else{
            int peek=aux.peek();
            if(val<peek){
                aux.push(val);
            }else{
                aux.push(peek);
            }
        }
    }
    
    public void pop() {
        aux.pop();
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return aux.peek();
    }
}
