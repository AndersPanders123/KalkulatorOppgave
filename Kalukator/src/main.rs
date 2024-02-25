use std::io;

fn main() {
    println!("Kalkukator :)");
    //Skriver det første nummeret her
    let num1 = get_user_input("Skriv det flørste nummeret her a");
    
    //Skriver det andre nummertet her
    let num2 = get_user_input("Skriv det andre her a");

    //Her er Pluss, minus og ganging
    println!("Pluss: {}", num1 + num2);
    println!("Minus: {}", num1 - num2);
    println!("Ganging: {}", num1 * num2);

    if num2 != 0.0 {
        println!("Deling: {}", num1 / num2);
    } else {
        println!("Kompis, du kanke dele på 0");
    }
}

//Får user input
fn get_user_input(promt: &str) -> f64 {
    loop {
        println!("{}", promt);

        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("Klarte ikke å lese linje");

        match input.trim().parse() {
            Ok(num) => return num,
            Err(_) => println!("Skriv et nummer ikke noe mongo")
        }
    }
}
