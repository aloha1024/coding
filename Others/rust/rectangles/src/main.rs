fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "the area of the rectangle is {} square pixels.",
        area(width1,height1)
    );

//元组
    let rect1 = (30,50);
    println!(
        "the area of the rectangle is {} square pixels.",
        area1(rect1)
    );
}

fn area(width: u32, height: u32) -> u32{
    width * height

}

//使用元组
fn area1(dimensions: (u32,u32)) -> u32 {
    dimensions.0 * dimensions.1
}

//使用结构体
struct Rectangle {
    width: u32,
    height: u32,
}

fn main01() {
    let rect2 = Rectangle {
        width: 30,
        height: 50,
    };
    println!(
        "the area of the recatangle is {} square pixels",
        area(&rect2)
    );
}