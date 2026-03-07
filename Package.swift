// swift-tools-version: 5.10
import PackageDescription

let package = Package(
    name: "LeetCode",
    platforms: [
        .macOS(.v13)
    ],
    products: [
        .library(
            name: "LeetCode",
            targets: ["LeetCode"]
        ),
    ],
    targets: [
        .target(
            name: "LeetCode",
            path: "Sources"
        ),
        .testTarget(
            name: "LeetCodeTests",
            dependencies: ["LeetCode"],
            path: "Tests"
        ),
    ]
)
