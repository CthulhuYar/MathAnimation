from manim import *

config.background_color = BLACK


class Example(Scene):
    def construct(self):
        definition = MathTex("(0)~~", "S_k = 1^k + 2^k + ... + n^k")
        # framebox1 = SurroundingRectangle(definition[0], buff=.1, color=RED)

        equation_1 = MathTex("x_k=", "(1+1)^k", "+", "(2+1)^k", "+...+", "(n-1+1)^k", "+", "(n+1)^k")
        equation_2 = MathTex("y_k=", "1^k", "+", "2^k", "+...+", "n^k")

        equation_3 = MathTex("(1)~~x_k-y_k=", "(n+1)^k-1")
        minus_eq1 = MathTex("-")
        equation_4 = MathTex("(2)~~x_k-y_k=", "\sum_{m=1}^{n}", "[(m+1)^k-m^k]",
                             "[", "C_k^{0}m^k",
                             "+...+C_k^{k-1}{m}+1^k",
                             "-m^k", "]",
                             "[C_k^{1}m^{k-1}+...+C_k^{k-1}{m}+1^k]")

        equation_5A = MathTex("[", "C_k^1\cdot{1^{k-1}}", "+",
                              "C_k^2\cdot{1^{k-2}}", "+...+",
                              "C_k^{k-1}\cdot{1}", "+",
                              "1", "~]")
        equation_5A1 = MathTex("+\n")
        equation_5B = MathTex("[", "C_k^1\cdot{2^{k-1}}", "+",
                              "C_k^2\cdot{2^{k-2}}", "+...+",
                              "C_k^{k-1}\cdot{2}", "+",
                              "1", "]")
        equation_5B1 = MathTex("\n...\n")
        equation_5C = MathTex("[", "C_k^1\cdot{n^{k-1}}", "+",
                              "C_k^2\cdot{n^{k-2}}", "+...+",
                              "C_k^{k-1}\cdot{n}", "+",
                              "1", "]")
        equation_6 = MathTex("C_k^1\cdot{S_{k-1}}",
                             "C_k^2\cdot{S_{k-2}}",
                             "+...+",
                             "C_k^{k-1}\cdot{S_1}",
                             "{S_0}")
        equation_7 = MathTex("\sum_{m=0}^{k-1}C_k^{k-m}\cdot{S_{m}")

        equation_1.shift(UP)
        equation_3.shift(DOWN)
        equation_4.shift(DOWN)

        equation_2.align_to(equation_1, LEFT)
        equation_3.align_to(equation_2, LEFT).shift(LEFT)
        equation_4.align_to(equation_2, LEFT).shift(LEFT)
        equation_1[4:8].next_to(equation_1[1])
        eq1_eq2 = VGroup(equation_1[1], equation_1[4:8], equation_2)
        eq1_eq2.save_state()
        # Definition Start
        self.wait(0.5)
        self.play(Write(definition[1]))
        self.wait(1)
        self.play(Write(definition[0]))
        self.play(definition.animate.scale(0.6).move_to(3.5 * UP + 4 * LEFT))
        # Definition End

        # Write x_k, y_k
        self.play(Write(equation_1[0]), Write(eq1_eq2))
        self.wait(1)

        # Write (1) x_k-y_k= (n+1)^k-1 START
        self.play(Write(equation_3[0]))
        self.play(equation_1[7].animate.next_to(equation_3[0]))

        minus_eq1.next_to(equation_1[7])
        self.play(Write(minus_eq1), FadeOut(equation_1[6]))
        self.wait(0.5)

        # FadeOut parts of sequences Start
        self.play(FadeOut(
            equation_1[5], equation_2[5]))
        self.wait(0.5)

        self.play(FadeOut(
            equation_1[4], equation_2[4]))
        self.wait(0.5)

        self.play(FadeOut(
            equation_1[1], equation_2[3], equation_2[2]))
        self.wait(0.5)
        # FadeOut parts of sequences End

        # moving to equation_3 x_k - y_k = (n+1)^k-1^k
        self.play(equation_2[1].animate.next_to(minus_eq1).shift(0.05 * UP))
        self.wait(0.5)

        eq1_0_and_eq2_0 = VGroup(equation_1[7], minus_eq1, equation_2[1])
        self.play(FadeTransform(eq1_0_and_eq2_0, equation_3[1]))
        self.wait(0.5)
        self.play(equation_3.animate.scale(0.6).align_to(definition).shift(4 * UP))
        self.wait(0.5)
        # Write (1) x_k-y_k= (n+1)^k-1 END

        # Return to start
        eq1_eq2.restore()
        equation_1[4:8].next_to(equation_1[3])
        eq1_eq2 = VGroup(equation_1[1:8], equation_2[1:6])
        self.play(Write(eq1_eq2))
        self.wait(1)

        # Start writing equation
        self.play(Write(equation_4[0]))

        # moving elements to equation START
        self.play(equation_1[1].animate.next_to(equation_4[0]))
        minus_eq1.next_to(equation_1[1]).shift(0.1 * LEFT)
        self.play(Write(minus_eq1))
        self.play(equation_2[1].animate.next_to(minus_eq1).shift(0.05 * UP + 0.1 * LEFT))
        eq1_group1 = VGroup(equation_1[2], equation_1[3])
        self.play(eq1_group1.animate.next_to(equation_2[1]).shift(0.1 * LEFT))
        minus_eq2 = minus_eq1.copy()
        minus_eq2.next_to(eq1_group1)
        self.play(Write(minus_eq2), FadeOut(equation_2[2]))
        self.play(equation_2[3].animate.next_to(minus_eq2).shift(0.05 * UP))
        plus_multi_dot_plus_eq = MathTex("+...+")
        plus_multi_dot_plus_eq.next_to(equation_2[3]).shift(0.1 * LEFT)
        self.play(FadeOut(equation_1[4:7], equation_2[4]), Write(plus_multi_dot_plus_eq))
        self.play(equation_1[7].animate.next_to(plus_multi_dot_plus_eq))
        minus_eq3 = minus_eq1.copy()
        minus_eq3.next_to(equation_1[7]).shift(0.1 * LEFT)
        self.play(Write(minus_eq3), equation_2[5].animate.next_to(minus_eq3).shift(0.05 * LEFT + 0.05 * UP))
        self.wait(1)
        # moving elements to equation END

        # transforming equation
        eq2_group = VGroup(equation_1[1], minus_eq1, equation_2[1], eq1_group1, minus_eq2, equation_2[3],
                           plus_multi_dot_plus_eq, equation_1[7], minus_eq3, equation_2[5])
        eq3_group = VGroup(equation_4[0], equation_4[1], equation_4[2])
        self.play(FadeTransform(eq2_group, eq3_group))
        self.play(FadeOut(equation_1[0], equation_2[0]))
        self.play(eq3_group.animate.move_to(2*UP+2*LEFT))
        # transforming equation

        eq4_group = VGroup(equation_4[3], equation_4[5], equation_4[7])
        eq5_group = VGroup(eq4_group, equation_4[4], equation_4[6])
        self.play(FadeTransform(equation_4[2], eq5_group.next_to(equation_4[1])))
        self.wait(1)
        self.play(FadeOut(equation_4[4], equation_4[6]))
        self.wait(1)
        self.play(FadeTransform(eq4_group, equation_4[8].next_to(equation_4[1])))
        self.wait(1)

        eq6_group = VGroup(equation_4[1], equation_4[8])
        equation_5A.next_to(equation_4[0])
        equation_5A1.next_to(equation_4[0])
        equation_5B.next_to(equation_4[0])
        equation_5B1.next_to(equation_4[0])
        equation_5C.next_to(equation_4[0])

        eq6_group0 = VGroup(equation_5A, equation_5A1, equation_5B, equation_5B1, equation_5C)
        self.play(FadeTransform(eq6_group, eq6_group0))
        self.play(equation_5A1.animate.shift(DOWN))
        self.play(equation_5B.animate.shift(2*DOWN))
        self.play(equation_5B1.animate.shift(3*DOWN))
        self.play(equation_5C.animate.shift(4*DOWN))
        self.wait(1)

        self.play(
            equation_5C[1].animate.shift(4*UP),
            equation_5B[1].animate.shift(2*UP))
        eq6_group1 = VGroup(equation_5A[1], equation_5C[1], equation_5B[1])
        equation_6[0].next_to(equation_5A[0]).shift(0.2*LEFT)
        self.play(FadeTransform(eq6_group1, equation_6[0]))

        self.play(
            equation_5C[3].animate.shift(4 * UP),
            equation_5B[3].animate.shift(2 * UP))
        eq6_group2 = VGroup(equation_5A[3], equation_5C[3], equation_5B[3])
        equation_6[1].next_to(equation_5A[2]).shift(0.2 * LEFT)
        self.play(FadeTransform(eq6_group2, equation_6[1]))

        self.play(
            equation_5C[4].animate.shift(4 * UP),
            equation_5B[4].animate.shift(2 * UP))
        eq6_group3 = VGroup(equation_5A[4], equation_5C[4], equation_5B[4])
        equation_6[2].next_to(equation_5A[3]).shift(0.2 * LEFT)
        self.play(FadeTransform(eq6_group3, equation_6[2]))

        self.play(
            equation_5C[5].animate.shift(4 * UP),
            equation_5B[5].animate.shift(2 * UP))
        eq6_group4 = VGroup(equation_5A[5], equation_5C[5], equation_5B[5])
        equation_6[3].next_to(equation_6[2]).shift(0.2 * LEFT)
        self.play(FadeTransform(eq6_group4, equation_6[3]))

        self.play(
            equation_5C[7].animate.shift(4 * UP),
            equation_5B[7].animate.shift(2 * UP))
        eq6_group5 = VGroup(equation_5A[7], equation_5C[7], equation_5B[7])
        equation_6[4].next_to(equation_5A[6]).shift(0.2 * LEFT)
        self.play(FadeTransform(eq6_group5, equation_6[4]))

        self.play(FadeOut(equation_5A1,
                          equation_5B[0], equation_5B[2], equation_5B[6], equation_5B[8],
                          equation_5B1,
                          equation_5C[0], equation_5C[2], equation_5C[6], equation_5C[8]))
        eq6_group6 = VGroup(equation_6, equation_5A[0], equation_5A[2], equation_5A[6], equation_5A[7], equation_5A[8])
        equation_7.next_to(equation_4[0])
        self.play(FadeTransform(eq6_group6, equation_7))
        self.wait(0.5)

        eq7_group = VGroup(equation_7, equation_4[0])
        self.play(eq7_group.animate.scale(0.6).align_to(definition, LEFT))
        self.wait(1)

        eq_scale_group = VGroup(eq7_group, equation_3, definition)
        self.play(eq_scale_group.animate.scale(0.6**(-1)).move_to(ORIGIN))
        self.wait(1)
        
