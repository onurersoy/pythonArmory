# SUBSETS:
# When 'all' the items of one set are also in another set, the contained set is called a 'subset' of the
# containing set.
# F.e 'Birds' is a subset of 'Animals'.
# Birds C Animals (Animals 'kapsar' Birds --- Kümeler Teorisi) >> In Python: (Birds < Animal) "< OR <="
# A proper subset is a subset that also isn't equal to the set that contains it. The distinction is important, in set
# theory.
# In Python, a proper subset would be written as: Birds < Animals (if it was not 'proper', we would go with '<=')

# SUPERSETS:
# 'Birds' is a subset of 'Animals', and we also say that 'Animals' is a superset of 'Birds'.
# That means all the items of 'Birds' are contained in 'Animals'.
# The 2 terms are complementary (tamamlayıcı/tümleyici). If set A is a subset of B, then set B is a superset of A.
# In Python, we use the greater than or equal to symbol:
# Animals >= Birds
# 'Animals' is also a proper superset of 'Birds'.
# A proper superset is a set that contains another set, but isn't equal to it.
# In Python, a proper superset would be written as: Animals > Birds (if it was not 'proper', we would go with '>=')

# A proper subset must contain fewer elements than its superset, and a proper superset must contain more elements
# than the subset.
