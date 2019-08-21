// fn main() {
//     println!("Hello, world!");
// }


#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
};

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect = Rectangle {width: 30, height: 50};

    println!(
        "the area of the rectangle is {} square pixels",
        rect.area()
    );
}

