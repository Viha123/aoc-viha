#lang racket
; (require fmt)
;; 
(define input (file->string "input.txt"))
(define input-list (string-split input "\n"))

;; part 1 helpers
(define (is-left? arg)
  (char=? (string-ref arg 0) #\L))
(define get-number (lambda (arg) 
  (string->number (substring arg 1))
))
(define (interp-number x) 
  (if (is-left? x) (* -1 (get-number x)) (get-number x)))
;; accumulator holds the answer and total value at the same time
(define dial-start 50) ;; mod num + 50 100 
(define (compute num acc)
  (let ([x (modulo (+ (car acc) num) 100)])
  (if (= x 0) (list x (+ (cadr acc) 1)) (list x (cadr acc))))
)
(define (compute-2 num acc)
  (let* ([x (modulo (+ (car acc) num) 100)] ;; current position of the dial
        [overflow (+ (car acc) (remainder num 100))] ;; how much the dial overflowed
        [div (floor (/ (abs num) 100))] ;; how many circles did this move take
        [remain (abs(floor (/ overflow 100)))] ;; checking if the overflow would have hit 0
        [real-remain (if (and (= 0 x) (not (= remain 1))) (+ remain 1) remain)]) ;; add one if it hits 0 after a move only if the previous overflow check didn't work
  (if (= (car acc) 0) (list x (+ (cadr acc) div)) (list x (+ (cadr acc) (+ div real-remain))))) 
)
;; part 1
(define numbers (map interp-number input-list))
(define ans (foldl compute (list dial-start 0) numbers))
(displayln (cadr ans))

;; part 2
(define p2 (foldl compute-2 (list dial-start 0) numbers))
(displayln (cadr p2)) ;; ans: 6289 