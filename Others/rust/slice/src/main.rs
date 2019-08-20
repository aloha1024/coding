fn main() {
    let my_string = String::from("hello world");
    let word = first_world(&my_string[..]);
    //first_world中传入 string 的slice

    let my_string_literal = "hello world";
    let word = first_world(&my_string_literal[..]);
    //first_world中传入 字符串字面值的slice
    
    let word = first_world("hello world");
    //因为字符串字面值就是字符串 slice
    //所以不用slice语法也可以
}

fn first_world(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }
    &s[..]
}