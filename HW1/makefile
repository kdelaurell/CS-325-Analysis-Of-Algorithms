CFLAGS = -g -Wall -std=c99

insertsort : insertsort.c
	gcc $(CFLAGS) -o $@ $^

mergesort : mergesort.c
	gcc $(CFLAGS) -o $@ $^

all: insertsort.c mergesort.c mergesort insertsort insert.out merge.out

clean :
	-rm mergesort
	-rm insertsort
	-rm merge.out
	-rm insert.out
