fn reverse(pair: (i32, bool)) -> (bool, i32) {
    let (integer, boolean) = pair;
    (boolean, integer)
}

#[derive(Debug)]
struct Matrix(f32,f32,f32,f32);

fn main() {
    let long_tuple = (1u8, 2u16, 3u32, 4u64, 
                    -1i8, -2i16, -3i32, -4i64, 
                    0.1f32, 0.2f64,
                    'a',true);
    println!("long tuple first value: {}", long_tuple.0);
    println!("long tuple second value: {}", long_tuple.1);

    let tuple_of_tuples = ((1u8, 2u16, 3u32),(4u64, -1i8), -2i16);
    //元组可以充当元组的元素

    println!("tuple of tuples: {:?}", tuple_of_tuples);
    
    let pair = (1, true);
    println!("pair is {:?}", pair);
    println!("the reversed pair is {:?}", reverse(pair));

    println!("one element tuple: {:?}", (5u32,));
    //创建单元素元组需要一个额外的逗号,为了和被括号包含的字面量作区分
    println!("just an integer: {:?}", (5u32));

    //元组可以被解构,从而将值绑定给变量
    
}