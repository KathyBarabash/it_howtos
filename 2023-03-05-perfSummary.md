
https://learn.microsoft.com/en-us/windows/wsl/
https://www.brendangregg.com/perf.html
https://www.brendangregg.com/usemethod.html


git clone https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git
cd linux/tools/perf
make -j$(nproc)


## What is perf
Perf is a sampling profiler. Perf collects execution statistics periodically and on specific events. Perf does not perform calculations, e.g., to report execution time of specific blocks of code or functions.

## Perf on WSL2

Source -- (How to Perform Perf Profiling in WSL2)[https://scicoding.com/how-to-perform-perf-profiling-in-wsl2/]

2023-03-05
```
sudo apt update && sudo apt -y upgrade
sudo apt autoremove -y
sudo apt install linux-tools-generic


which perf -> /usr/bin/perf is a wrapper, does not work

/usr/lib/linux-tools-5.4.0-144/perf stat ls
LOGS-2022-06-15-u20base  LOGS-2022-06-16-u20work  wsl-mod-instance.sh  wsl-update.sh.lnk
LOGS-2022-06-16-u20base  test.txt                 wsl-new-distro.sh    wsl.conf

 Performance counter stats for 'ls':

              3.37 msec task-clock:u              #    0.494 CPUs utilized
                 0      context-switches:u        #    0.000 K/sec
                 0      cpu-migrations:u          #    0.000 K/sec
               106      page-faults:u             #    0.031 M/sec
            920435      cycles:u                  #    0.273 GHz
            607907      instructions:u            #    0.66  insn per cycle
            126936      branches:u                #   37.663 M/sec
              8336      branch-misses:u           #    6.57% of all branches

       0.006818999 seconds time elapsed

       0.004283000 seconds user
       0.000000000 seconds sys

cd ../Projects/perf
vi test.c
	#include <stdio.h>
	#include <unistd.h>

	void wait(int ms) {
		usleep(ms * 1000);
	}

	int main() {
		for (int i = 0; i < 5; i++) {
			printf("Step %d\n", i);
			fflush(stdout);
			wait(100);
		}

		return 0;
	}

gcc -O0 -ggdb3 -fno-omit-frame-pointer -o test test.c
/usr/lib/linux-tools-5.4.0-144/perf record -c 1000 -g ./test
Step 0
Step 1
Step 2
Step 3
Step 4
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.074 MB perf.data (1162 samples) ]


/usr/lib/linux-tools-5.4.0-144/perf report -g
Samples: 1K of event 'cycles:u', Event count (approx.): 1162000
  Children      Self  Command  Shared Object     Symbol
+   30.12%    30.03%  test     ld-2.31.so        [.] _dl_exception_free
+   20.65%     0.09%  test     libc-2.31.so      [.] __libc_start_main
+   17.90%     1.89%  test     libc-2.31.so      [.] printf
+   15.15%     0.00%  test     [unknown]         [.] 0x41e589480000b274
+   15.06%     1.12%  test     ld-2.31.so        [.] __get_cpu_features
+   12.91%    11.62%  test     ld-2.31.so        [.] _dl_rtld_di_serinfo
+   12.22%    12.05%  test     libc-2.31.so      [.] psiginfo
+    7.31%     0.00%  test     [unknown]         [.] 0x000055b69818e2a0
+    6.37%     0.00%  test     ld-2.31.so        [.] 0x00007f854fd4e064
+    6.28%     6.28%  test     ld-2.31.so        [.] _dl_debug_state
+    5.42%     0.00%  test     ld-2.31.so        [.] 0x00007f854fd4e53a
+    4.48%     4.30%  test     ld-2.31.so        [.] _dl_catch_error
+    4.39%     4.39%  test     libc-2.31.so      [.] _IO_file_xsputn
+    4.39%     4.30%  test     libc-2.31.so      [.] __nss_database_lookup
+    3.53%     0.00%  test     [unknown]         [.] 0000000000000000
+    3.44%     0.00%  test     ld-2.31.so        [.] 0x00007f854fd4b108
+    3.44%     0.00%  test     [unknown]         [.] 0x00000000000060b3
+    3.36%     3.36%  test     libc-2.31.so      [.] _IO_adjust_column
+    2.75%     0.00%  test     ld-2.31.so        [.] 0x00007f854fd5461b
+    2.24%     0.52%  test     libc-2.31.so      [.] secure_getenv
+    2.15%     0.69%  test     test              [.] main
+    1.55%     0.00%  test     [unknown]         [.] 0x00007f854fd79e10
+    1.46%     0.00%  test     [unknown]         [.] 0x2e34362d3638782d
+    1.38%     1.20%  test     libc-2.31.so      [.] clock_nanosleep
     1.12%     1.12%  test     [unknown]         [k] 0xffffffff82000b40
+    1.12%     1.03%  test     libc-2.31.so      [.] _IO_file_write
+    0.86%     0.86%  test     libc-2.31.so      [.] 0x00000000000225a0
+    0.86%     0.00%  test     libc-2.31.so      [.] 0x00007f854fb6f5a0
     0.77%     0.77%  test     ld-2.31.so        [.] malloc
+    0.77%     0.00%  test     [unknown]         [.] 0x0000001000005f83
+    0.69%     0.69%  test     libc-2.31.so      [.] _IO_file_overflow
+    0.60%     0.60%  test     libc-2.31.so      [.] cuserid
+    0.60%     0.60%  test     libc-2.31.so      [.] usleep
     0.60%     0.60%  test     libc-2.31.so      [.] _IO_fflush
     0.52%     0.52%  test     [unknown]         [k] 0xffffffff82000db0
     0.52%     0.43%  test     libc-2.31.so      [.] write
     0.43%     0.43%  test     test              [.] wait
     0.43%     0.00%  test     [unknown]         [.] 0x000055b69759a318
     0.43%     0.43%  test     libc-2.31.so      [.] _IO_do_write
     0.43%     0.43%  test     libc-2.31.so      [.] exit
     0.34%     0.34%  test     ld-2.31.so        [.] _dl_catch_exception
     0.34%     0.34%  test     ld-2.31.so        [.] 0x00000000000021ba
     0.34%     0.34%  test     libc-2.31.so      [.] _IO_file_sync
     0.34%     0.26%  test     libc-2.31.so      [.] _Exit
     0.34%     0.34%  test     libc-2.31.so      [.] _IO_file_setbuf
     0.34%     0.00%  test     ld-2.31.so        [.] 0x00007f854fd4c1ba
     0.26%     0.26%  test     [unknown]         [k] 0xffffffff82000000
     0.26%     0.26%  test     ld-2.31.so        [.] 0x00000000000042db
Cannot load tips.txt file, please install perf!

```
## Measuring Function Execution Time with Perf
https://scicoding.com/measuring-function-execution-time-with-perf/

me@u20base:/mnt/d/Projects/perf/test2dir$ sudo /usr/lib/linux-tools-5.4.0-144/perf probe -x ./test2 --
add main --add main%return --add wait --add wait%return
Added new events:
  probe_test2:main     (on main in /mnt/d/Projects/perf/test2dir/test2)
  probe_test2:main__return (on main%return in /mnt/d/Projects/perf/test2dir/test2)
  probe_test2:wait     (on wait in /mnt/d/Projects/perf/test2dir/test2)
  probe_test2:wait__return (on wait%return in /mnt/d/Projects/perf/test2dir/test2)

You can now use it in all perf tools, such as:

        perf record -e probe_test2:wait__return -aR sleep 1
		
		
		me@u20base:/mnt/d/Projects/perf/test2dir$ sudo /usr/lib/linux-tools-5.4.0-144/perf record -g -e probe_test2:main -e probe_test2:main__return -e probe_test2:wait -e probe_test2:wait__return ./test2
Step 0
Step 1
Step 2
Step 3
[ perf record: Woken up 1 times to write data ]
[ perf record: Captured and wrote 0.004 MB perf.data (10 samples) ]

## How to Compile Perf with all Features on?
https://scicoding.com/how-to-compile-perf-with-all-features-on/

