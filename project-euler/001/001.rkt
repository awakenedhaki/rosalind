(require spd/tags)

(@HtDD Natural)
;; Natural is any integer greater than 0

#;
(define (fn-for-n n)
  (cond [(zero? n) (...)]
        [else
          (... n
               (fn-for-n (sub1 n)))]))

(@HtDF solution solution1)
(@signature Natural -> Natural)
;; Sum multiples of 3 or 5 up to n

(check-expect (solution 10) 23)
(check-expect (solution1 10) 23)

(define (solution n)
  (local [(define (fn-for-n n sum)
            (cond [(zero? n) sum]
                  [else
                    (if (or (= 0 (remainder n 3))
                            (= 0 (remainder n 5)))
                      (fn-for-n (sub1 n) (+ sum n))
                      (fn-for-n (sub1 n) sum))]))]
    (fn-for-n (sub1 n) 0)))

;; Using built-in abstract functions
(define (solution1 n)
  (local [(define (multiple-of-3-5? n)
           (or (= 0 (remainder n 3))
               (= 0 (remainder n 5))))]
    (foldl + 0 (filter multiple-of-3-5? (build-list n identity)))))
