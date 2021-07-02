#!/usr/bin/env python3

# Copyright (c) 2019-2021 Ludovic Drolez

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# Major progressions
prog_maj = [
    "IIm9 V7 bVIIM7 IVM7",
    "Im7 IVm9 Im7 V7#5",
    "Im7 bIIIm7",
    "Im7 IVm7 Im7 bIIIm7 VIIdim7",
    "Im7 bVIIM9",
    "IM9 IVM13",
    "IM7 bIm7 IIm7b5",
    "Im9 bVIM9 IVm11 bVImM7",
    "I bIIM I iii",
    "I bIIM bIIIM bIIM",
    "I IIM iii V6",
    "I II7 IV I",
    "I bIII7 II7 bII7",
    "I bIIIM bVIM bVIIM", # Tadd Dameron turnround
    "I bIII7 bVI7 bII7",
    "I bIIIM bVIIM IV",
    "I ii V vi",
    "I ii7 I6 IV",
    "I biiidim ii7 V7", # Jazz
    "I iii IV vi",
    "I iii vi Isus4",
    "I iii vi IV",
    "I iii vi V",
    "I I I I IV IV I I V IV I I", #  12 bar Blues: Shuffle
    "I IV Isus2 IV",
    "I IV ii V",
    "I IV vi V",
    "I IV V V",
    "I IV V bVIIM",
    "I IV bIIIM bVIM", 
    "I IV bVIIM IV",
    "I IV vii iii vi bVII bIII V7",
    "IM7 IVM7 viidim iii7 vi7 ii7 V7",             # Complete Circle of Diatonic 5ths Progression
    "IM7 #IVM7 VII7 iii7 VI7 ii7 V7",              # Complete Circle of Chromatic 5ths Progression
    "IM7 #IVM7 VII7 IIIM7 IIIm7 VI7 IIM7 IIm7 V7", # Circle of Chromatic 5ths Progression with resolved iis / Vs
    "I iii vi IV ii viidim V",                     # Harmonic function progression in major
    "I V I IV",
    "I V7 ii V",
    "I V vi ii",
    "I V vi IV",            # Axis progression
    "I V vi iii IV",
    "I V vi V",
    "I V vi iii IV I IV V", # Pachiabel's Canon
    "I V bVIIM IV",
    "I bVIM I bIIM",
    "I bVI V",
    "I v v ii",
    "I vi I IV", 
    "I vi ii IV", 
    "I vi ii V",
    "I vi III V", 
    "I vi IV iii",
    "I vi IV V",      # 50's progression, or do wop
    "I vi bVI7#11 V", # Jazz
    "I VIm7 II V",    # Jazz 
    "I vi ii V",      # Jazz
    "I bVIIM bVIM bIIM",
    "I bVIIM IV I",
    "iim7b5 V7 iii VI7", 
    "ii bIIM I bVIIM",
    "ii IV V V",
    "ii V I I",
    "ii V I IV",
    "ii bVIIM7 I", "ii7 V9 I7 I7",
    "iim7 V7 iiim7 vi7 iim7 V7",
    "bIIIM ii bIIM I",
    "bIII V7 I",
    "III7 VI7 II7 V7 I", # Ragtime progression
    "iii vi IV I",
    "iii VI ii V",
    "iii7 vi ii V",
    "iii7 biiidim ii7 V7",
    "IV I ii vi",
    "IV I iii IV",
    "IV I V vi",
    "IV I6 V",
    "IV IV I V",
    "IV iv I",
    "V7 I7 IV IV vim7 II7 iim7 V7", # Jazz: Montgomery-Ward Bridge
    "V I vi V",
    "V IV vi I",
    "V vi IV I",
    "vi IV I V",
    "vi bVIM bVIIM I",
    "vi V IV V",
    "vi7 bVI7 V7 I",
    "bVII V7 I",
]

# minor progressions
prog_min = [
    "i11 IV7 VI7 IIIM7",
    "i i IV6 VI",
    "i ii v i",
    "i III iv VI",
    "i III VII IV",
    "i bIII VII IV", # Plagal cadence
    "i iv v iv",
    "i iv v v",
    "i iv III VI",
    "i iv VI v",
    "i iv VII i",
    "i iv VII v i i ii V",
    "i v iv VII",
    "i VI bi v",
    "i VI III bii",
    "i VI III VII",
    "i VI III VII i VI69 III7 VII",
    "i VI iv ii",
    "i VI iv v",
    "i VI VII VII",
    "i VI VII v",
    "i iv VII III VI iidim V", # Circle of 5ths progression
    "i VII III VI iv iidim V", # Harmonic function progression in minor
    "i bVIIM bVIM bVIIM",
    "i bVIIM VI bii",
    "i VII i v",
    "i VII i v III VII i v i",
    "i VII IV IV",
    "i VII VI III",
    "i VII VI V", # Andalusian cadence
    "i VII VI iv",
    "i VII VI VII",
    "i7 VI III7 VII6 i i7 III7 iv7",
    "ii v i i",
    "ii v i iv",
    "ii VI i iv",
    "ii7 v9 i7",
    "iv i v VI",
    "iv VI VII i",
    "iv III VII i",
    "iv III II I",        # Andalusian cadence
    "iv III VI II I",
    "iv v VI VII",
    "v i iv VII",
    "v iv i i",
    "v VI III i",
    "v VI v i",
    "VI i v v",
    "VI iv i v",
    "VI bVI i VII",
    "VI VIm i VII",
    "VI VI i VII",
    "VI VII i III",
    "VI VII v III",
    "VII iv VII i",
    "VII iv v i",
]

# Chord Types
chord_types = [
    'sus2',  # 0, 2, 7
    'sus4',  # 0, 5, 7
    '6',  # 0, 4, 7, 9
    '7',  # 0, 4, 7, 10
    '7-5',  # 0, 4, 6, 10
    '7+5',  # 0, 4, 8, 10
    '7sus4',  # 0, 5, 7, 10
    'm6',  # 0, 3, 7, 9
    'm7',  # 0, 3, 7, 10
    'm7-5',  # 0, 3, 6, 10
    'dim6',  # 0, 3, 6, 9
    'maj7',  # 0, 4, 7, 11
    'M7+5',  # 0, 4, 8, 11
    'mM7',  # 0, 3, 7, 11
    'add9',  # 0, 4, 7, 14
    'madd9',  # 0, 3, 7, 14
    '2',  # 0, 4, 7, 14
    'add11',  # 0, 4, 7, 17
    'm69',  # 0, 3, 7, 9, 14
    '69',  # 0, 4, 7, 9, 14
    '9',  # 0, 4, 7, 10, 14
    'm9',  # 0, 3, 7, 10, 14
    'maj9',  # 0, 4, 7, 11, 14
    '9sus4',  # 0, 5, 7, 10, 14
    '7-9',  # 0, 4, 7, 10, 13
    '7+11',  # 0, 4, 7, 10, 18
]