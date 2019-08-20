fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");
    &s
}

fn first_world(s: &String) -> &str {
    let bytes = s.as_bytes();
    
    for (i,&item) in bytes.iter().enumerate(){
        if item = b' '{
            return &s[0..i];
        }
    }
    &s[..]
}