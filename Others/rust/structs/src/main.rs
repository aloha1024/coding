fn main() {
    println!("Hello, world!");
}


// struct user {
//     username: String,
//     email: String,
//     sign_in_count: u64,
//     active: bool,
// };

let mut user1 = User {
    username: String::from("username"),
    email: String::from("email@email.com"),
    sign_in_count: 1,
    active: true,
};

user1.email = String::from("anotheremail@email.com");

fn build_user(email: String, username: String) -> User {
    User{
        email:email,
        username:username,
        active:true,
        sign_in_count:1,
    }
}

fn build_user_lte(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}

let user1 = User {
    email: String::from("test1@mail.com"),
    username: String::from("user1"),
    active: true,
    sign_in_count: 1,
}

let user2 = User{
    email: String::from("test2@email.com"),
    username: String::from("user2"),
    active: false,
    sign_in_count: 2,
}

struct Color(i32,i32,i32);
struct Point(i32,i32,i32);

let black = Color(0,0,0);
let origin = Point(0,0,0);

