
## Level 2, Challenge 2: Elevator Maintenance

### Prompt: 

You've been assigned the onerous task of elevator maintenance - ugh! It wouldn't be so bad, except that all the elevator documentation has been lying in a disorganized pile at the bottom of a filing cabinet for years, and you don't even know what elevator version numbers you'll be working on. 

Elevator versions are represented by a series of numbers, divided up into major, minor and revision integers. New versions of an elevator increase the major number, e.g. 1, 2, 3, and so on. When new features are added to an elevator without being a complete new version, a second number named "minor" can be used to represent those new additions, e.g. 1.0, 1.1, 1.2, etc. Small fixes or maintenance work can be represented by a third number named "revision", e.g. 1.1.1, 1.1.2, 1.2.0, and so on. The number zero can be used as a major for pre-release versions of elevators, e.g. 0.1, 0.5, 0.9.2, etc (Commander Lambda is careful to always beta test her new technology, with her loyal henchmen as subjects!).

Given a list of elevator versions represented as strings, write a function solution(l) that returns the same list sorted in ascending order by major, minor, and revision number so that you can identify the current elevator version. The versions in list l will always contain major numbers, but minor and revision numbers are optional. If the version contains a revision number, then it will also have a minor number.

For example, given the list l as ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], the function solution(l) would return the list ["1.0", "1.0.2", "1.0.12", "1.1.2", "1.3.3"]. If two or more versions are equivalent but one version contains more numbers than the others, then these versions must be sorted ascending based on how many numbers they have, e.g ["1", "1.0", "1.0.0"]. The number of elements in the list l will be at least 1 and will not exceed 100.

-- Java cases --
Input:
Solution.solution({"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"})
Output:
    0.1, 1.1.1, 1.2, 1.2.1, 1.11, 2, 2.0, 2.0.0

Input:
Solution.solution({"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"})
Output:
    1.0, 1.0.2, 1.0.12, 1.1.2, 1.3.3

---
### Approach:

I was given 72 hours to complete this challenge. This one was *a little annoying*. It was just a lot of string manipulation and converting from String to ints, comparing those integers, sorting accordingly, and then converting back to String. Very puzzle-like and breaking down the problems into their specific issues made this task a lot easier. No real reason for using merge sort, other than it was better than quick sort, and I needed a sorting algorithm that wasn't fussy with a small set of data.

### Takeaways:

- Got better at parsing Integers to String and vice versa
- Remembered that sorting algorithms exist

##### Completion Time: 4 hours, 9 minutes, 33 seconds

---
Java code:
``` java
public static int strToInt(String ver, int index) {
    for (int i = index; i < ver.length(); i++) {
        if (i+1 == ver.length() || ver.charAt(i+1) == '.') {
            String number = ver.substring(index, i+1);
            return Integer.parseInt(number);
        }
    }
    return -1;
}

public static boolean firstLessThanSecond(String ver1, String ver2) {
    int index = 0;
    boolean firstIsLess;
    int len;
    if (ver1.length() < ver2.length()) {
        firstIsLess = true;
        len = ver1.length();
    }
    else {
        firstIsLess = false;
        len = ver2.length();
    }
    while (index < len) {
        int i = strToInt(ver1, index);
        int j = strToInt(ver2, index);
        
        if (i < j) return true;
        else if (i > j) return false;
        else {
            if (firstIsLess) {
                while (ver1.charAt(index) != '.') {
                    if (index+1 == len) return true;
                    index++;
                }
            }
            else {
                while (ver2.charAt(index) != '.') {
                    if (index+1 == len) return false;
                    index++;
                }
            }
        }
        index++;
    }
    
    // catch-all
    return false;
}

public static void merge(String arr[], int l, int m, int r) 
{ 
    int n1 = m - l + 1; 
    int n2 = r - m; 

    String L[] = new String[n1]; 
    String R[] = new String[n2]; 

    for (int i = 0; i < n1; ++i) 
        L[i] = arr[l + i]; 
    for (int j = 0; j < n2; ++j) 
        R[j] = arr[m + 1 + j]; 

    int i = 0, j = 0; 

    int k = l; 
    while (i < n1 && j < n2) { 
        if (firstLessThanSecond(L[i], R[j])) { 
            arr[k++] = L[i++]; 
        } 
        else { 
            arr[k++] = R[j++]; 
        } 
    } 

    while (i < n1) { 
        arr[k++] = L[i++]; 
    } 

    while (j < n2) { 
        arr[k++] = R[j++]; 
    } 
} 

public static void mergesort(String arr[], int l, int r) 
{ 
    if (l < r) { 
        int mid = (l + r) / 2; 

        mergesort(arr, l, mid); 
        mergesort(arr, mid + 1, r); 

        merge(arr, l, mid, r); 
    } 
}

public static String[] solution(String[] l) {
    mergesort(l, 0, l.length-1);
    return l;
}
```

---

![A successful submission](https://github.com/mikedinhnguyen/google-foobar-challenge/blob/master/images/Screen%20Shot%202020-07-29%20at%201.56.45%20PM.png)