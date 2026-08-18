# Циклические группы: точные separating-параметры и Question 7.3

**Черновик исследовательской заметки.**  
Версия: 17 августа 2026

## 1. Контекст и соглашения

Пусть \(C_N=\langle s\rangle\) — циклическая группа порядка \(N\geq2\), а \(q\geq2\) — размер алфавита. Для метки \(f:C_N\to[q]\) и упорядоченного набора различных элементов \(Y=(y_1,\ldots,y_t)\) наблюдение в вершине \(g\) есть

\[
W_{f,Y}(g)=(f(gy_1),\ldots,f(gy_t)).
\]

Пара \((f,Y)\) *separating*, если все \(N\) таких слов различны. Используются определения \(\operatorname{sep}_q\), \(\operatorname{csep}_q\) и \(\chi_1\) из Kang–Hsieh [1, §2].

Главный комбинаторный факт ниже — существование **cut-down de Bruijn sequence**: для любых \(q,r\geq1\) и \(1\leq L\leq q^r\) существует циклическое \(q\)-арное слово длины \(L\), в котором все циклические факторы длины \(r\) попарно различны [2].

## 2. Unrestricted separating number

### Теорема 2.1

Для всех \(q\geq2\) и \(N\geq2\),

\[
\boxed{\operatorname{sep}_q(C_N)=\lceil\log_qN\rceil.}
\]

### Доказательство

Положим \(r=\lceil\log_qN\rceil\). Любая separating-пара \((f,Y)\) с \(|Y|=t\) даёт \(N\) различных слов длины \(t\) над \(q\)-буквенным алфавитом. Поэтому \(N\leq q^t\), то есть

\[
t\geq\lceil\log_qN\rceil=r.
\]

Для обратного неравенства имеем \(N\leq q^r\). Выберем cut-down de Bruijn word

\[
c=(c_0,c_1,\ldots,c_{N-1})
\]

длины \(N\), все циклические \(r\)-факторы которого попарно различны. Определим

\[
f(s^i)=c_i,\qquad
Y=(1,s,\ldots,s^{r-1}).
\]

Тогда

\[
W_{f,Y}(s^i)=(c_i,c_{i+1},\ldots,c_{i+r-1}),
\]

где индексы берутся по модулю \(N\). Эти слова различны по выбору \(c\), значит \(Y\) separating и \(\operatorname{sep}_q(C_N)\leq r\). Вместе с нижней границей это доказывает равенство. \(\square\)

## 3. Connected windows и one-step parameters

### Теорема 3.1 (ориентированное циклическое направление)

Для \(S=(s)\),

\[
\boxed{\operatorname{csep}_q(C_N,(s))=
\max\{2,\lceil\log_qN\rceil\}.}
\]

Кроме того,

\[
\boxed{\chi_1(C_N,(s))=\lceil\sqrt N\rceil.}
\]

### Доказательство

Общая нижняя граница для connected window из [1, Proposition 2.5] равна

\[
\operatorname{csep}_q(C_N,(s))
\geq\max\{\lceil\log_qN\rceil,|\{1,s\}|\}
=\max\{\lceil\log_qN\rceil,2\}.
\]

Положим \(r=\max\{2,\lceil\log_qN\rceil\}\). Cut-down слово длины \(N\) с различными \(r\)-факторами вместе с окном

\[
(1,s,\ldots,s^{r-1})
\]

даёт separating window ровно размера \(r\). Его индуцированный подграф — путь (либо весь цикл в крайнем случае), и он содержит \(1,s\). Это доказывает формулу для \(\operatorname{csep}_q\).

Для \(\chi_1\) фиксированное окно \(Y_S=(1,s)\) имеет две координаты. Поэтому \(N\leq q^2\) необходимо. Если \(q=\lceil\sqrt N\rceil\), то \(N\leq q^2\); cut-down слово с различными циклическими факторами длины \(2\) делает наблюдения на \((1,s)\) различными. \(\square\)

### Теорема 3.2 (симметричный цикл)

Пусть \(N\geq3\) и \(S=(s,s^{-1})\). Тогда

\[
\boxed{\operatorname{csep}_q(C_N,(s,s^{-1}))=
\max\{3,\lceil\log_qN\rceil\},}
\]

\[
\boxed{\chi_1(C_N,(s,s^{-1}))=\lceil N^{1/3}\rceil.}
\]

### Доказательство

Нижняя граница для connected window равна \(\max\{3,\lceil\log_qN\rceil\}\), поскольку \(1,s,s^{-1}\) различны. Для

\[
r=\max\{3,\lceil\log_qN\rceil\}
\]

берём cut-down слово длины \(N\) с различными \(r\)-факторами и окно

\[
Y=(s^{-1},1,s,s^2,\ldots,s^{r-2}).
\]

Это \(r\) последовательных позиций циклического слова. Оно содержит \(1,s,s^{-1}\), а индуцированный подграф связен; его наблюдения — циклические \(r\)-факторы с фиксированной циклической перестановкой координат. Следовательно, они различны.

Для one-step окна \((1,s,s^{-1})\) имеется три координаты, так что \(N\leq q^3\) необходимо. При \(q=\lceil N^{1/3}\rceil\) cut-down слово с различными факторами длины \(3\) разделяет вершины, потому что

\[
(f(s^i),f(s^{i+1}),f(s^{i-1}))
\]

есть фиксированная перестановка блока \((c_{i-1},c_i,c_{i+1})\). \(\square\)

## 4. Когда Theorem 3.3 Kang–Hsieh достигает оптимума

Здесь речь идёт именно об оптимальности **конкретной finite-field cyclic-coset construction** из [1, Theorem 3.3], а не о единственном способе построить оптимальное окно.

### Теорема 4.1

Пусть \(q\) — степень простого, \(N\geq2\),

\[
k=\lceil\log_qN\rceil.
\]

Если \(k\geq2\), то Theorem 3.3 из [1] может дать separating pattern оптимального размера \(k\) для \(C_N\) тогда и только тогда, когда

\[
\boxed{\exists m\mid N:\ \operatorname{ord}_m(q)=k.}
\]

При \(k=1\) эта construction sharp тогда и только тогда, когда

\[
\boxed{N\leq q-1.}
\]

### Доказательство

В Theorem 3.3 выбирается элемент \(s\in C_N\) порядка \(m\), значит \(m\mid N\). Также нужен элемент \(\theta\in\mathbb F_{q^k}^{\times}\) порядка \(m\), для которого

\[
1,\theta,\ldots,\theta^{k-1}
\]

есть \(\mathbb F_q\)-базис. При \(m>1\) степень поля \(\mathbb F_q(\theta)\) равна \(\operatorname{ord}_m(q)\). Поэтому базисное условие эквивалентно \(\operatorname{ord}_m(q)=k\).

Если \(k\geq2\) и такое \(m\) существует, то \(m\mid q^k-1\). Оно также делит \(N\). Равенство \(N=q^k\) невозможно, так как тогда \(m\mid\gcd(q^k,q^k-1)=1\), а \(m>1\). Следовательно \(N\leq q^k-1\), а capacity condition Theorem 3.3,

\[
\frac{N}{m}\leq\frac{q^k-1}{m},
\]

выполнено. Обратно, применение Theorem 3.3 с окном размера \(k\) прямо даёт такой \(m\) и базисное условие, а значит \(\operatorname{ord}_m(q)=k\).

При \(k=1\) можно взять элемент порядка \(m=1\). Тогда capacity condition становится \(N\leq q-1\), что одновременно необходимо и достаточно. \(\square\)

## 5. Параметр \(M_q(m,k)\) и результат 2016 года

Kang–Hsieh определяют \(M_q(m,k)\) как максимум числа циклических \(q\)-арных слов длины \(m\), у которых все циклические факторы длины \(k\) различны и внутри каждого слова, и между разными словами [1, Definition 3.1]. Это эквивалентно максимуму числа попарно edge-disjoint замкнутых направленных trails длины \(m\) в de Bruijn digraph, чьи рёбра суть \(q\)-арные слова длины \(k\).

### Теорема 5.1

Пусть \(q\) — степень простого, \(m\mid(q^k-1)\) и \(\operatorname{ord}_m(q)=k\). Тогда

\[
\boxed{M_q(m,k)=\frac{q^k-1}{m}.}
\]

### Доказательство

В обозначениях Grubman–Şekercioğlu–Wood [3, Theorem 5] положим их длину наблюдения \(\ell=k\), а длину цикла — \(m\). Условие их теоремы

\[
m\mid q^k-1,
\qquad
m\nmid q^i-1\quad(1\leq i<k)
\]

эквивалентно \(\operatorname{ord}_m(q)=k\). Их non-primitive LFSR construction строит

\[
\frac{q^k-1}{m}

\]

попарно непересекающихся \(m\)-циклов и доказывает оптимальность: эти циклы покрывают все, кроме одного, из \(q^k\) состояний.

При переходе на конвенцию Kang–Hsieh вершины de Bruijn graph порядка \(k\) становятся рёбрами de Bruijn digraph порядка \(k-1\). Поэтому эти циклы дают ровно допустимое семейство для \(M_q(m,k)\).

Наконец, независимая counting upper bound даёт

\[
M_q(m,k)\,m\leq q^k.
\]

Так как \(m\mid(q^k-1)\), имеем

\[
M_q(m,k)\leq\left\lfloor\frac{q^k}{m}\right\rfloor
=\frac{q^k-1}{m}.
\]

LFSR lower bound совпадает с этой границей. \(\square\)

## 6. Научный статус и корректная формулировка

Новая часть пакета — короткое применение arbitrary-length cut-down de Bruijn sequences к Question 7.3 Kang–Hsieh, дающее точную формулу для \(\operatorname{sep}_q(C_N)\), а также четыре непосредственных exact cyclic refinements для стандартных directed/symmetric Cayley structures.

Теорема 5.1 не должна подаваться как новый результат: это точный перевод Theorem 5 Grubman–Şekercioğlu–Wood в параметр \(M_q(m,k)\). Корректно писать, что найдена прямая связь с их работой, не цитируемой в текущем arXiv v1 Kang–Hsieh.

## References

1. M.-H. Kang and Y.-H. Hsieh, *Information and Locality in Cayley Graphs*, arXiv:2608.04608v1 (2026). https://arxiv.org/html/2608.04608v1
2. B. Cameron, A. Gündoğan, and J. Sawada, *Cut-Down de Bruijn Sequences*, arXiv:2205.02815 (2022). https://arxiv.org/abs/2205.02815
3. T. Grubman, Y. A. Şekercioğlu, and D. R. Wood, *Partitioning de Bruijn Graphs into Fixed-Length Cycles for Robot Identification and Tracking*, Discrete Applied Mathematics 213 (2016), 101–113. https://doi.org/10.1016/j.dam.2016.05.013
