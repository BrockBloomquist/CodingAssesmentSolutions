class squareRoot {
    public int mySqrt(int x) {
        return (int)binarySearchSqrt(x, 0, x);
    }
    public long binarySearchSqrt(long target, long low, long high) {
        if(low > high) {
            return -1;
        }
        long mid = (high+low)/2;
        long square = mid*mid;

        if(target == square) {
            return mid;
        }
        else if((mid-1)*(mid-1) < target && square > target) {
            return mid-1;
        }
        else if((mid+1)*(mid+1) > target && square < target) {
            return mid;
        }
        else if(square > target) {
            high = mid-1;
        }
        else if(square < target) {
            low = mid+1;
        }
        return binarySearchSqrt(target,low,high);
    }
}
