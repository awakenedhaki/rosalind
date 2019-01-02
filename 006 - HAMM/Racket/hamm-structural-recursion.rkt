;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname hamm-structural-recursion) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(require spd/tags)

(@HtDD Nucleotide)
;; nucleotide is one of #\a #\t #\g #\c
;; interp. the four components of a dna sequence

#;
(define (fn-for-nt nt)
  (cond [(char=? nt #\a) (...)]
        [(char=? nt #\t) (...)]
        [(char=? nt #\g) (...)]
        [(char=? nt #\c) (...)]))

(@HtDD ListOfNucleotide)
;; listofnucleotide is one of:
;; - empty
;; - (cons nucleotide listofnucleotide)

#;
(define (fn-for-lon lon)
  (cond [(empty? lon) (...)]
        [else
          (... (fn-for-nucleotide (first lon))
               (fn-for-lon (rest lon)))]))

(@HtDF hamming-distance)
(@signature (listof Nucleotide) (listof Nucleotide) -> Natural)
;; produce the hamming distance of two sequences
;; assume: given sequences are equal in length

(check-expect
  (hamming-distance "gagcctactaacgggat"
                    "catcgtaatgacggcct")
  7)

(@template (listof Nucleotide))
(define (hamming-distance seq1 seq2)
  (local [(define SEQ1 (string->list seq1))

          (define SEQ2 (string->list seq2))

          (define (hamming-distance seq1 seq2)
            (cond [(and (empty? seq1) (empty? seq2)) 0]
                  [else
                    (if (char=? (first seq1) (first seq2))
                      (hamming-distance (rest seq1) (rest seq2))
                      (+ 1 (hamming-distance (rest seq1) (rest seq2))))]))]
    
    (hamming-distance SEQ1 SEQ2)))
