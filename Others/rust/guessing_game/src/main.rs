use std::io;
use std::cmp::Ordering;
use rand::Rng;

fn main(){
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1,101);
    
    //println!("the secret number is {}", secret_number);
    
    loop{
        println!("please input you guess.");
        
        let mut guess = String::new();
        
        io::stdin().read_line(&mut guess)
            .expect("failed to read line");

        let guess: u32 = match guess.trim().parse(){
            Ok(num) => num,
            Err(_) => continue,
        };
            //.expect("please type a number");
        
        println!("you guess is {}",guess);

        match guess.cmp(&secret_number){
            Ordering::Less => println!("too small"),
            Ordering::Greater => println!("too big"),
            Ordering::Equal => {
                println!("you win");
                break;
            }
        }
    }
}