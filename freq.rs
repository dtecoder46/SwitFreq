use std::fs;

fn main() {

    let text_file = "input.txt";
    let contents = fs::read_to_string(text_file)
        .expect("File has been read");

    println!("{}", contents);

    // list of characters that may appear in traditional text, which will be removed to simplify things
    let junk_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "[", "]", "{", "}", "|", "\\", ":", ";", "\"", "\'", "<", ">", "?", "/", ".", ",", "~", "`"];

    for junk_char in junk_chars {
        let clean_text = contents.replace(junk_char, "");
    }
}