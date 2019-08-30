fn main() {
    println!("1+2={}",1u32+2);

    println!("1-2={}",1i32-2);

    println!("true and false is {}",true && false);
    println!("true or false is {}",true || false);
    println!("not true is {}",!true);

    println!("0011 and 0101 is {:04b}", 0b0011u32 & 0b0101);
    println!("0011 or 0101 is {:04b}", 0b0011u32 | 0b0101);
    println!("")
}