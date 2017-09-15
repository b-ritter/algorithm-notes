# Algorithmic Toolbox Notes

### Master Theorem

The master theorem is used to evaluate the runtime of recursive algorithms, notably divide and conquer patterns such as binary search and polynomial multiplication.

$T(n) = aT(\lceil \frac{n}{b} \rceil) + O(n^d)$

In general:

$$T(n) = \begin{cases}
O(n^d) & \text { if } d > \log_b a\\
O(n^d \log n) & \text { if } d = \log_b a\\
O(n^{\log_b n}) & \text { if } d < \log_b a
\end{cases}$$


For example, binary search can be represented as:

$T(n) = T(\frac{n}{2}) + O(1)$

Or, to simplify:

$T(n) = O(\log n)$