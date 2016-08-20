Leonard Chan

lc599@drexel.edu


Problem 2 Example output
lc599@tux64-14:~/CS360/pa3/prob2$ mit-scheme
MIT/GNU Scheme running under GNU/Linux
Type `^C' (control-C) followed by `H' to obtain information about interrupts.

Copyright (C) 2014 Massachusetts Institute of Technology
This is free software; see the source for copying conditions. There is NO warranty;
not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Image saved on Saturday May 17, 2014 at 2:39:25 AM
  Release 9.2 || Microcode 15.3 || Runtime 15.7 || SF 4.41 || LIAR/x86-64 4.118
  Edwin 3.116

1 ]=> (load "prob2.scm")

;Loading "prob2.scm"...
;  Loading "ch4-query.scm"... done


;;; Query input:
(grade ?g (L Van Pelt) PH100)

;;; Query results:
(grade c+ (l van pelt) ph100)



lc599@tux64-14:~/CS360/pa3/prob2$ mit-scheme
MIT/GNU Scheme running under GNU/Linux
Type `^C' (control-C) followed by `H' to obtain information about interrupts.

Copyright (C) 2014 Massachusetts Institute of Technology
This is free software; see the source for copying conditions. There is NO warranty;
not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

Image saved on Saturday May 17, 2014 at 2:39:25 AM
  Release 9.2 || Microcode 15.3 || Runtime 15.7 || SF 4.41 || LIAR/x86-64 4.118
  Edwin 3.116

1 ]=> (load "prob2.scm")

;Loading "prob2.scm"...
;  Loading "ch4-query.scm"... done


;;; Query input:
(before CS120 CS100)

;;; Query results:
(before cs120 cs100)

;;; Query input:
(before CS120 EE005)

;;; Query results:

;;; Query input:
(before CS206 CS100)

;;; Query results:
(before cs206 cs100)
(before cs206 cs100)

;;; Query input:
(before CS100 CS206)

;;; Query results:





Problem 3 Example Output
Parse tree output
{
    "right_sibling": null,
    "leftmost_child": {
        "right_sibling": {
            "right_sibling": {
                "right_sibling": {
                    "right_sibling": null,
                    "leftmost_child": {
                        "right_sibling": {
                            "right_sibling": {
                                "right_sibling": {
                                    "right_sibling": null,
                                    "leftmost_child": {
                                        "right_sibling": null,
                                        "leftmost_child": null,
                                        "label": "e"
                                    },
                                    "label": "B"
                                },
                                "leftmost_child": null,
                                "label": ")"
                            },
                            "leftmost_child": {
                                "right_sibling": null,
                                "leftmost_child": null,
                                "label": "e"
                            },
                            "label": "B"
                        },
                        "leftmost_child": null,
                        "label": "("
                    },
                    "label": "B"
                },
                "leftmost_child": null,
                "label": ")"
            },
            "leftmost_child": {
                "right_sibling": null,
                "leftmost_child": null,
                "label": "e"
            },
            "label": "B"
        },
        "leftmost_child": null,
        "label": "("
    },
    "label": "B"
}



Problem 4 Example output
