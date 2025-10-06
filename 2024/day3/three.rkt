

;; get from file input
;; use regex to get me a list of pairs of values
;; i mult each pair and sum value

#lang racket

(define input (file->string "2024/day3/exampleInput.txt"))

;; PART 1!!
(string? input)
(foldl + 0 (map 
  (lambda (mult) ;; here we know there are exactly 2 digits
    ; (string->number (car (regexp-match* #px"\\d+" mult)) (string->number (cdr (r)))
    (let* ([lst (regexp-match* #px"\\d+" mult)]
          [n1 (string->number (car lst))]
          [n2 (string->number (car (cdr lst)))])
          (* n1 n2)))
  (regexp-match* #px"mul\\(\\d+,\\d+\\)" input)))

;; PART 2:

;; subtract part 1 - anything after don't 

(regexp-match-positions #px"don\\'t\\(\\)" input)
(regexp-match-positions #px"do\\(\\)" input)
display (regexp-match-positions #px"mul\\(\\d+,\\d+\\)" input)

