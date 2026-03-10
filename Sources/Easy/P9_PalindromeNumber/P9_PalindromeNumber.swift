/**
 * Problem: 9. Palindrome Number
 * Difficulty: Easy
 * Topic: 
 *
 * Complexity:
 * - Time: O(?)
 * - Space: O(?)
 *
 * Notes:
 * 
 */

import Foundation

class Solution {
    func isPalindrome(_ x: Int) -> Bool {
        guard x >= 0 else {
            return false
        }
        
        var tempValue = x
        var invertedNum = 0

        while tempValue > 0 {
            let digit = tempValue % 10
            invertedNum = invertedNum * 10 + digit
            tempValue = tempValue/10
        }

        return x == invertedNum
    }
}
