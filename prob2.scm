; Leonard Chan
; 1. Run `mit-scheme`
; 2. Load the ch4-query.scm script by running `(load "ch4-query.scm")`
; 3. The query evaluator is now started with the appropriate database
;    for this problem already loaded. To find the answer to
;    14.3.1, enter the query:
;
;    (grade ?g (L Van Pelt) PH100)
;
;    which will return a match with ?g substituting the grade for L Van Pelt
;    in PH100.
;
;    (grade c+ (l van pelt) ph100)
; 4. While still in the query evaluator, to prove before("CS120", "CS100"),
;    run:
;
;    (before CS120 CS100)
;
;    to receive the expected output
;
;    ;;; Query results:
;    (before cs120 cs100)
;
;    which indicates that this mattern exists in the db.
;
;    To prove before("CS206", "CS100"), run
;
;    (before CS206 CS100)
;
;    to receive the expected output
;
;    ;;; Query results:
;    (before cs206 cs100)
;    (before cs206 cs100)
;
;    which indicates that this mattern exists in the db.
;    No results indicate the intput is false.

(load "ch4-query.scm")

; Create a database of some anwers
(define db '(
    ; part 1 (14.3.1)
    (csg PH100 1 C+)
    (snap 1 (L Van Pelt) (Some address) (Some phone number))
    (csg PH100 2 B)
    (snap 2 Alpha (Some address) (Some phone number))
    (csg PH100 Professor A)
    (snap Professor Beta (Some address) (Some phone number))

    (rule (grade ?g ?n ?c)
        (and (csg ?c ?s ?g) (snap ?s ?n ?a ?p))
    )

    ; part 2 (14.9.2)
    (cp CS101 CS100)
    (cp EE200 CS100)
    (cp CS121 CS120)
    (cp CS206 CS121)
    (cp EE200 EE005)
    (cp CS120 CS101)
    (cp CS205 CS101)
    (cp CS206 CS205)
    (rule (before ?x ?y) (cp ?x ?y))
    (rule (before ?x ?y) (and (cp ?x ?z) (before ?z ?y)))
))

(initialize-data-base db)
(query-driver-loop)
