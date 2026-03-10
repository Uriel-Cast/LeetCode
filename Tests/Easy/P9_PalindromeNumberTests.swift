import XCTest
@testable import LeetCode

final class P9_PalindromeNumberTests: XCTestCase {
    func testSolution() {
        let sol = Solution()
        XCTAssertEqual(sol.isPalindrome(121), true)
        XCTAssertEqual(sol.isPalindrome(-121), false)
        XCTAssertEqual(sol.isPalindrome(10), false)
    }
}
