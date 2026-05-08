class DynamicArray {
    int[] arr;
    int index=0;
    public DynamicArray(int capacity) {
        if(capacity>0){
            arr=new int[capacity];
        }
    }

    public int get(int i) {
        return arr[i];
    }

    public void set(int i, int n) {
        arr[i]=n;
    }

    public void pushback(int n) {
        if (index == arr.length) {
            resize();
        }
        arr[index] = n;
        index++;
    }


    public int popback() {
        if (index == 0) return -1;

        index--;
        return arr[index];
    }

    private void resize() {
        int[] newarr=new int[arr.length*2];
        for(int i=0;i<arr.length;i++){
            newarr[i]=arr[i];
        }
        arr=newarr;
    }

    public int getSize() {
        return index;
    }

    public int getCapacity() {
        return arr.length;
    }
}
