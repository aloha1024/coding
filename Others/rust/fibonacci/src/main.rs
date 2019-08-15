fn main() {
    fib(5);
}

fn fib(number: u64) {
    let mut n=0;
    let mut a=0;
    let mut b=1;
    let mut c=1;
    while n < number {
        println!("{}",b);
        // a=b;
        b=a+b;
        a=c;
        c=b;
        n=n+1
    }
    println!("OK!")
}