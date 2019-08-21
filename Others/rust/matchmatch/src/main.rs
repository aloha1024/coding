fn main() {
    println!("Hello, world!");
}

enum Coin {
    penny,,
    nickel,
    dime,
    quarter,
}

fn value_in_cents(coin: coin) -> u32 {
    match coin {
        coin::penny => 1,
        coin::nickel => 5,
        coin::dime => 10,
        coin::quarter => 25,
    }
}
