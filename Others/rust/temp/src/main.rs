use std::io;

fn main() {
    println!("1:c2f,2:f2c");
    let mut select = String::new();
    io::stdin()
        .read_line(&mut select)
        .expect("failed to read line");
    let select: u64 = select
        .trim()
        .parse()
        .expect("Please type a number!");
    println!("{}",select);

    println!("please enter the temperature value");
    let mut number = String::new();
    io::stdin()
        .read_line(&mut number)
        .expect("failed to read line");
    let number: u64= number
        .trim()
        .parse()
        .expect("Please type a number!");
    println!("{}",number);

    if select == 1 {
        c2f(number);
    }else if select == 2 {
        f2c(number);
    }
}

fn c2f(num: u64) {
    let result = 9/5*num+32;
    println!("The value is {}",result);
}

fn f2c(num: u64) {
    let result = 5/9*(num-32);
    println!("The value is {}",result);
}