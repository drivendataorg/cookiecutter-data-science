// {% raw %}
#import "@preview/lovelace:0.3.0": pseudocode-list
#set page(paper: "us-letter", margin: 1cm)
#set text(size: 12pt)
#set heading(numbering: "1.1")
#show heading.where(level: 1): it => {
  set align(center)
  set text(size: 16pt)
  it
}
#show heading.where(level: 2): it => {
  set align(center)
  set text(size: 14pt)
  it
}
#show heading.where(level: 3): it => {
  set align(center)
  set text(size: 12pt, fill: blue)
  it
}


#heading(level: 1, numbering: none)[6.1400 PS01]
#align(center)[
  Gatlen Culp (gculp\@mit.edu)
  #sym.dot 2025-05-21 \
  Collaborators: None #sym.dot Resources Used: None
]

#columns(2)[
  = Regular Languages

  Closure under:
  $
    A union B, quad A sect B, quad A^R, quad A^*, quad not A, \
    A dot B, quad A - B = A sect (not B)
  $
]

// {% endraw %}