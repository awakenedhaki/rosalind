(require spd/tags)

(@HtDD Natural)
;; Natural is an integer greater than 0

#;
(define (fn-for-n n)
  (cond [(zero? n) (...)]
        [else
          (... n
               (fn-for-n (sub1 n)))]))

(@HtDF sum-even-fib)
(@signature Natural -> Natural)
;; Sum even numbers in fibonacci sequence up to n terms

(check-expect (sum-even-fib 10) 44)

(define (sum-even-fib n)
  (local [(define (fn-for-n n sum a b)
            (cond [(zero? n) sum]
                  [else
                    (if (even? a)
                      (fn-for-n (sub1 n) (+ sum a) (+ a b) a)
                      (fn-for-n (sub1 n) sum (+ a b) a))]))]
    (fn-for-n (sub1 n) 0 1 1)))
