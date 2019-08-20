fn main() {
    println!("Hello, world!");
}

fn example1 {
    let number = 3;
    if number < 5 {
        println!("condition was true");
    }else{
        println!("condition was false");
    }
}

//This is a wrong example
// fn example2 {
//     let number = 3;
//     if number {
//         println!("number was three");
//     }
// }

//use "if" in "let"
fn example3 {
    let condition = true;
    let number = if condition {
        5
    }else{
        6
    };
    println!("the value of number is : {}",number);
}

fn example4 {
    loop {
        println!("again!");
    }
}

fn example5 {
    let mut counter = 0;

    let result = loop {
        counter += 1;
        
        if counter == 10 {
            break counter * 2;
        }
    };
    assert_eq!(result, 20);
}

fn example6 {
    let x = 5;
    println!("the value of x is: {}", x);
    x = 6;
    println!("the value of x is: {}", x);
}

