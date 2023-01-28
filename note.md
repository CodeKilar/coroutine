- 其实可以理解为一种特殊的程序调用。特殊的是在执行过程中，在子程序（或者说函数）内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行
- 在有大量IO操作业务的情况下，我们采用协程替换线程，可以到达很好的效果，一是降低了系统内存，二是减少了系统切换开销，因此系统的性能也会提升。
- 进程和线程的切换完全是用户无感，由操作系统控制，**从用户态到内核态再到用户态**,而协程的切换完全是程序代码控制的，在**用户态**的切换
- 协程是非抢占式多任务，线程是抢占式多任务

- **因此在协程调用阻塞IO操作的时候，操作系统会让线程进入阻塞状态，当前的协程和其它绑定在该线程之上的协程都会陷入阻塞而得不到调度，这往往是不能接受的。**

- 如果熟知了python生成器，还可以将协程理解为**生成器+调度策略**