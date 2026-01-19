module alu_formal (
    input [7:0] A,
    input [7:0] B,
    input [4:0] Opcode
);

    wire [7:0] Result;
    wire CarryOut;
    wire Zero;
    wire Negative;
    wire Overflow;
    wire Equal;
    wire Great;
    wire Less;

    ALU #(
        .WIDTH(8)
    ) u_alu (
        .A(A),
        .B(B),
        .Opcode(Opcode),
        .Result(Result),
        .CarryOut(CarryOut),
        .Zero(Zero),
        .Negative(Negative),
        .Overflow(Overflow),
        .Equal(Equal),
        .Great(Great),
        .Less(Less)
    );

    // Verification properties
    always @(*) begin
        // 1. Basic Flag Checks
        assert(Zero == (Result == 8'h00));
        assert(Negative == Result[7]);

        // 2. Comparison Flags (Independent of Opcode)
        assert(Equal == (A == B));
        assert(Less == (A < B));
        assert(Great == (A > B));

        // 3. Operation correctness
        case (Opcode)
            // Arithmetic
            5'd0: begin // ADD
                assert({CarryOut, Result} == {1'b0, A} + {1'b0, B});
            end
            5'd1: begin // SUB
                // Result should be A - B (on 8 bits)
                assert(Result == A - B);
                // CarryOut logic in ALU.sv: temp_result[8] where temp = A + ~B + 1
                // This is the inverted borrow for subtraction A - B.
                // If A >= B, CarryOut = 1. If A < B, CarryOut = 0.
                assert(CarryOut == (A >= B));
            end
            5'd2: begin // INC
                assert({CarryOut, Result} == {1'b0, A} + 1'b1);
            end
            5'd3: begin // DEC
                assert(Result == A - 1'b1);
                // Carry logic matches ALU impl: A + 0xFF
                assert({CarryOut, Result} == {1'b0, A} + 9'h0FF);
            end

            // Shifts
            5'd4: begin // LSL
                assert({CarryOut, Result} == {1'b0, A} << 1);
            end
            5'd5: begin // LSR
                assert(Result == A >> 1);
                assert(CarryOut == A[0]);
            end
            5'd6: begin // ASR
                assert($signed(Result) == $signed(A) >>> 1);
                assert(CarryOut == A[0]);
            end

            // Bitwise Logic
            5'd13: assert(Result == (A & B));      // AND
            5'd14: assert(Result == (A | B));      // OR
            5'd10: assert(Result == (A ^ B));      // XOR
            5'd8:  assert(Result == ~(A & B));     // NAND
            5'd9:  assert(Result == ~(A | B));     // NOR
            5'd11: assert(Result == ~(A ^ B));     // XNOR
            
            // Special
            5'd17: assert(Result == ~A);           // NOT A
            5'd18: assert(Result == ~B);           // NOT B
            5'd12: assert(Result == A);            // PASS A
            5'd15: assert(Result == B);            // PASS B
            5'd7:  begin                           // REV
                assert(Result[0] == A[7]);
                assert(Result[1] == A[6]);
                assert(Result[2] == A[5]);
                assert(Result[3] == A[4]);
                assert(Result[4] == A[3]);
                assert(Result[5] == A[2]);
                assert(Result[6] == A[1]);
                assert(Result[7] == A[0]);
            end
            
            // CMP
            5'd16: begin
                // CMP is subtraction but result is not used (or rather Result is subtraction result)
                // In ALU.sv, CMP executes: temp_result = {1'b0, A} + {1'b0, ~B} + 9'd1;
                // Same as SUB
                assert(Result == A - B);
            end

            default: assert(Result == 0); // ALU.sv defaults to 0
        endcase
    end

endmodule
