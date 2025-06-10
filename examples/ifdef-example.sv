module ifdef_example #(
`ifdef BAR
  parameter PARAM0 = 0,
`endif
  parameter PARAM1 = 0
) (
    input  a_i,
`ifdef FOO
    input  b_i,
`ifdef BAZ
    input  c_i,
`endif
    input  d_i,
`endif
    input  e_i,
    output x_o
);


endmodule
