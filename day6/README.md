#Day 6

## Idea
As Python and C are close buddys but day and night in performance i wanted to test the difference in this example


## compile c
```
gcc -o faster faster.c
```
## create shared file
```
gcc -o faster.so --shared -fPIC faster.c
```