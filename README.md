Bổ sung phần phát biểu bài toán,
Bổ sung phần số mũ mã hóa cần giới hạn trong khoảng nào là nhỏ,
Bổ sung phần định nghĩa thời gian đa thức,






Nghĩa bổ sung
Nghĩa bổ sung
Nghĩa bổ sung
Nghĩa bổ sung
Nghĩa bổ sung
Nghĩa bổ sung
Nghĩa bổ sung
Nghĩa bổ sung
Nghĩa bổ sung



Phát biểu bài toán

INPUT:
(n, e): (Khóa công khai)
c: (Bản mã)
t: (Phần văn bản cố định trong bản rõ)
y: (Giới hạn của phần bí mật trong bản rõ)
OUTPUT:
x: (Phần bí bật trong bản rõ)

<!-- - Số mũ mã hóa cần giới hạn trong khoảng nào là nhỏ -->

https://www.youtube.com/watch?v=vxS0DZE_Lvs&t=1s
<!-- - Định nghĩa thời gian đa thức là như thế nào -->

Định nghĩa thời gian đa thức

Theo sách

@book{silverman2008introduction,
  title={An introduction to mathematical cryptography},
  author={Silverman, Joseph H and Pipher, Jill and Hoffstein, Jeffrey},
  volume={1},
  year={2008},
  publisher={Springer}
}





\textbf{Định nghĩa:} Giả sử chúng ta đang cố gắng giải quyết một loại bài toán toán học nhất định, trong đó đầu vào của bài toán là một số có kích thước có thể thay đổi. Ví dụ, hãy xem xét Bài Toán Phân Tích Số Nguyên Tố, đầu vào của bài toán là một số \( N \) và đầu ra là một thừa số nguyên tố của \( N \). Chúng ta quan tâm đến việc biết thời gian cần thiết để giải bài toán này theo kích thước của đầu vào. Thông thường, người ta đo kích thước của đầu vào bằng số bit của nó, vì đó là lượng bộ nhớ cần thiết để lưu trữ đầu vào.

Giả sử rằng có một hằng số \( A \geq 0 \), không phụ thuộc vào kích thước của đầu vào, sao cho nếu đầu vào có độ dài \( O(k) \) bit, thì nó mất \( O(k^A) \) bước để giải bài toán. Khi đó bài toán được gọi là có thể giải được trong thời gian đa thức.


<!-- 
theo công thức chứng minh ![alt text](image.png)
ta có 
https://chatgpt.com/c/00a6fa58-6d59-4a9a-bb34-0615a4b3e4ce -->


\documentclass{article}
\usepackage[utf8]{vietnam}
\usepackage{amsmath}
\usepackage{amsthm}

\newtheorem{lemma}{Bổ đề}

\begin{document}

\section*{Bổ đề 4.2: Giới hạn độ dài cơ sở LLL giảm}

\begin{lemma}[LLL Reduced Basis Length Bound]
Giả sử rằng chúng ta có một cơ sở \( v_1, v_2, \ldots, v_n \in \mathbb{R}^m \) cho một lưới \( L \) là LLL giảm, thì bất đẳng thức sau đây đúng:
\[ \|v_1\|^2 \leq 2^{n-1} \|x\|^2 \]
đối với mọi \( x \in L \) với \( x \neq 0 \).
\end{lemma}

\section*{Giải thích}

Bổ đề này thực chất nói rằng độ dài của \( v_1 \), vector đầu tiên của cơ sở LLL giảm, nhiều nhất là \( 2^{(n-1)/2} \) lần độ dài của bất kỳ vector nào không bằng không trong lưới \( L \). Điều này bao gồm cả vector ngắn nhất trong lưới.

\section*{Khái quát với Điều kiện Lovász}

Điều kiện Lovász cho giảm LLL thường liên quan đến một tham số \( \delta \) (thường được chọn là \( 3/4 \)). Khi xem xét dạng tổng quát với \( \delta \), chúng ta có:
\[ \|v_1\| \leq \left( \frac{4}{4\delta - 1} \right)^{(n-1)/2} \lambda(L), \]
trong đó \( \lambda(L) \) biểu thị độ dài của vector ngắn nhất trong lưới \( L \).

\section*{Lựa chọn Cụ thể của \( \delta \)}

Để đảm bảo thời gian tính toán đa thức của thuật toán LLL, chúng ta sử dụng:
\[ \delta = \frac{1}{4} + \frac{3}{4}\frac{n}{n-1}. \]

Với lựa chọn \( \delta \) này, chúng ta có:
\[ \|v_1\| \leq \left( \frac{2}{\sqrt{3}} \right)^n \lambda(L). \]

Lựa chọn cụ thể này của \( \delta \) đơn giản hóa giới hạn và cung cấp một hàm xấp xỉ rõ ràng \( \psi(n) = \left( \frac{2}{\sqrt{3}} \right)^n \).

\section*{Ý nghĩa}

Mặc dù \( \psi(n) \) là hàm số mũ theo hạng của lưới \( n \), kết quả này vẫn là một thành tựu quan trọng. Giới hạn này không phụ thuộc vào kích thước đầu vào, làm cho nó trở thành một kết quả cơ bản trong nghiên cứu về lưới và cho các thuật toán như thuật toán LLL. Thuật toán LLL là thuật toán đầu tiên cho phép giải quyết chính xác Bài Toán Vector Ngắn Nhất (SVP) trong các kích thước cố định, đại diện cho một bước tiến lớn trong lý thuyết lưới và toán học tính toán.

\section*{Tóm tắt}

- **Bổ đề 4.2**: Cung cấp một giới hạn trên độ dài của vector đầu tiên của cơ sở LLL giảm.
- **Dạng tổng quát**: \( \|v_1\| \leq \left( \frac{4}{4\delta - 1} \right)^{(n-1)/2} \lambda(L) \).
- **Lựa chọn cụ thể của \( \delta \)**: Chọn \( \delta = \frac{1}{4} + \frac{3}{4}\frac{n}{n-1} \) cho \( \|v_1\| \leq \left( \frac{2}{\sqrt{3}} \right)^n \lambda(L) \).
- **Hàm xấp xỉ**: \( \psi(n) = \left( \frac{2}{\sqrt{3}} \right)^n \).

Bổ đề này và các ý nghĩa của nó làm nổi bật hiệu quả của thuật toán LLL trong việc xấp xỉ vector ngắn nhất trong lưới và thời gian tính toán đa thức dưới các điều kiện cụ thể.

\end{document}
