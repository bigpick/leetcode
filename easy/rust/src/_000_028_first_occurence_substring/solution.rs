use std::convert::TryInto;

struct Solution;

impl Solution {
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.len() > haystack.len() {
            return -1;
        }

        match haystack.find(&needle) {
            Some(idx) => return idx.try_into().unwrap(),
            _ => return -1,
        }
    }
}

#[test]
fn test() {
    assert_eq!(Solution::str_str("sadbutsad".to_string(), String::from("sad")), 0);
    assert_eq!(Solution::str_str(String::from("leetcode"), String::from("leeto")), -1);
}

// Runtime1 ms Beats 71.91% || Memory 2 MB Beats 56.40%
