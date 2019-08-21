fn main() {
    println!("Hello, world!");
}


enum IpAddrKind {
    v4,
    v6
}

let four = IpAddrKind::v4;
let six = IpAddrKind::v6;

fn route(ip_type: IpAddrKind) { 

}

route(IpAddrKind::v4);
route(IpAddrKind::v6);

struct IpAddr {
    kind: IpAddrKind,
    address: String,
}

let home = IpAddr {
    kind: IpAddrKind::v4,
    address: String::from("127.0.0.1"),
};

let loopback = IpAddr {
    kind: IpAddrKind::v6,
    adress: String::from("::1"),
};

enum Message {
    Quit,
    Move {x: i32, y: i32},
    ChangeColor(i32, i32, i32),
}

impl Message {
    fn call(&self) {
        // something methoh
    }
}

let m = Message::Wirte(String::from("hello"));
m.call();

