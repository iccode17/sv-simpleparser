// Test case 1: Simple parameters with various data types
module test1 #(
    parameter INT_PARAM = 42,
    parameter REAL_PARAM, BAR_PARAM = 3.14, // comment 1
    // comment 2
    parameter STRING_PARAM = "default",
    parameter LOGIC_PARAM = 1'b1
) ();

endmodule

// Test case 2: Parameters with expressions as defaults
module test2 #(
    parameter WIDTH = 8,
    parameter DEPTH = 16,
    parameter ARRAY_SIZE = WIDTH * DEPTH, // Test comment
    parameter OFFSET = ARRAY_SIZE - 1
) ();

endmodule

// Test case 3: Parameters with different numeric bases
module test3 #(
    parameter BIN = 4'b1010,
    parameter HEX = 16'hDEAD,
    parameter OCT = 8'o377,
    parameter UNSIZED = 'd42
) ();

endmodule

// Test case 4: Parameters with struct-like defaults
module test4 #(
    parameter type T = logic[7:0],
    parameter VECTOR = {8{1'b1}},
    parameter ARRAY = '{1, 2, 3, 4}
) ();

endmodule

// Test case 5: Mixed parameters with and without defaults
module test5 #(
    parameter P1,
    parameter P2 = 2,
    parameter P3,
    parameter P4 = P2 * 2
) ();

endmodule

// Test case 6: String parameters with special characters
module test6 #(
    parameter ESCAPED = "Hello\tWorld\n",
    parameter PATH = "/home/user/default.txt",
    parameter SPECIAL = "!@#$%^&*()"
) ();

endmodule
