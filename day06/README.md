#Day 6

## Idea
I wanted to use a custom self writen c function in y python script, C is just sooo much faster

## compile c (doesn't work, because no main())
```
gcc -o faster faster.c
```
## create shared file
```
gcc -o faster.so --shared -fPIC faster.c
```
