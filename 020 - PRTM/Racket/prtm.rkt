(require spd/tags)
(require json)

(define PROT-MASS (call-with-input-file "prot_mass.json" read-json))

(define (protein-mass aa)
  ())
