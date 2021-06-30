struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn roman_to_int(s: String) -> i32 {
        let valmap: HashMap<char, i32> = [
            ('M', 1000),
            ('D', 500),
            ('C', 100),
            ('L', 50),
            ('X', 10),
            ('V', 5),
            ('I', 1),
        ]
        .iter()
        .cloned()
        .collect();

        let mut total = 0;
        let mut previous = 0;

        for c in s.chars() {
            let fetched = valmap.get(&c);
            match fetched {
                Some(&val) => {
                    if val > previous {
                        total += val - previous - previous
                    } else {
                        total += val
                    }
                    previous = val;
                }
                None => (),
            }
        }
        total
    }
}

#[test]
fn test() {
    assert_eq!(Solution::roman_to_int(String::from("III")), 3);
    assert_eq!(Solution::roman_to_int(String::from("IV")), 4);
    assert_eq!(Solution::roman_to_int(String::from("IX")), 9);
    assert_eq!(Solution::roman_to_int(String::from("LVIII")), 58);
    assert_eq!(Solution::roman_to_int(String::from("MCMXCIV")), 1994);
}
