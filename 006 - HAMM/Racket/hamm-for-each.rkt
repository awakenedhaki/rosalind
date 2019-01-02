;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname hamm-for-each) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(require spd/tags)

(@HtDF hamming-distance)
(@signature String String -> Natural)
;; produce the hamming distance of two sequences

(check-expect
  (hamming-distance "GAGCCTACTAACGGGAT"
                    "CATCGTAATGACGGCCT")
  7)

(@template for-each)
(define (hamming-distance seq1 seq2)
  (local [(define SEQ1 (string->list seq1))

          (define SEQ2 (string->list seq2))

          (define hd 0)]

          (begin (for-each 

                   (lambda (nt)
                      (if (char=? (list-ref SEQ1 nt)
                                  (list-ref SEQ2 nt))
                        (set! hd hd)
                        (set! hd (+ 1 hd))))
                   (build-list (length SEQ1) identity))
                 
                 hd)))
