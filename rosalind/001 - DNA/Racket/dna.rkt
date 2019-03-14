;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname dna) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(require spd/tags)

(@HtDD Nucleotide)
;; Nucleotide is one of #\A #\T #\G #\C
;; interp. the four components of a DNA sequence

#;
(define (fn-for-nt nt)
  (cond [(string=? nt #\A) (...)]
        [(string=? nt #\C) (...)]
        [(string=? nt #\G) (...)]
        [(string=? nt #\T) (...)]))

(@HtDD ListOfNucleotide)
;; ListOfNucleotide is one of:
;; - empty
;; - (cons Nucleotide ListOfNucleotide)

#;
(define (fn-for-lon lon)
  (cond [(empty? lon) (...)]
        [else
          (... (fn-for-nucleotide (first lon))
               (fn-for-lon (rest lon)))]))

(@HtDD Counts)
(define-struct counts (a c g t))
;; Counts is (make-counts Natural Natural Natural Natural)
;; interp. Counts is the count of each nucleotide in a DNA sequence

#;
(define (fn-for-counts c)
  (... (counts-a c)
       (counts-c c)
       (counts-g c)
       (counts-t c)))

(@HtDF counts-nt)
(@signature String -> Counts)
;; produce the counts of each nucleotide in a DNA sequence

(check-expect 
 (counts-nt 
  "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")
 (make-counts 20 12 17 21))

(@template Counts Nucleotide (listof Nucleotide) encapsulated)
(define (counts-nt s)
  (local [(define SEQ (string->list s))
            
          (define (counts-nt seq c)
            (cond [(empty? seq) c]
                  [else
                   (counts-nt (rest seq)
                              (check-nt (first seq) c))]))
            
          (define (check-nt nt c)
            (cond [(char=? nt #\A)
                   (make-counts (+ 1 (counts-a c))
                                (counts-c c)
                                (counts-g c)
                                (counts-t c))]
                  [(char=? nt #\C)
                   (make-counts (counts-a c)
                                (+ 1 (counts-c c))
                                (counts-g c)
                                (counts-t c))]
                  [(char=? nt #\G)
                   (make-counts (counts-a c)
                                (counts-c c)
                                (+ 1 (counts-g c))
                                (counts-t c))]
                  [(char=? nt #\T)
                   (make-counts (counts-a c)
                                (counts-c c)
                                (counts-g c)
                                (+ 1 (counts-t c)))]))]
      
    (counts-nt SEQ (make-counts 0 0 0 0))))
