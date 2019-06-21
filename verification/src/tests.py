"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[
                        ['A', 'B'],
                        ['B', 'C'],
                        ['C', 'D']
                    ], ['B']],
            "answer": 2,
            "explanation": [
                "One crushed server in the middle separates network on two subnetworks",
                ['',   '',  '',  '',  '',
                 'A',  '', 'C',  '',  '',
                 '',  'B',  '', 'D',  '',
                 '',   '',  '',  '',  '',
                 '',   '',  '',  '',  ''],
            ]
        },
        {
            "input": [[
                        ['A', 'B'],
                        ['A', 'C'],
                        ['A', 'D'],
                        ['D', 'F']
                    ], ['A']],
            "answer": 3,
            "explanation": [
                "crushed server has 3 connected server to it, so it can potentially seporate on 3 subnetworks",
                ['',  '',  '',  '',  '',
                 '', 'B',  '', 'C',  '',
                 '',  '', 'A',  '',  '',
                 '',  '',  '', 'D', 'F',
                 '',  '',  '',  '',  ''],
            ]
        },
        {
            "input": [[
                        ['A', 'B'],
                        ['B', 'C'],
                        ['C', 'D']
                    ], ['C', 'D']],
            "answer": 1,
            "explanation": [
                "Those two crushed servers are in the end of connection line so they doesn't separate anything",
                ['',  '',  '',  '',   '',
                 'A', '', 'C',  '',   '',
                 '', 'B',  '', 'D',   '',
                 '',  '',  '',  '',   '',
                 '',  '',  '',  '',   ''],
            ],
        }
    ],
    "Extra": [
        {
            "input": [[
                        ['A', 'B'],
                        ['A', 'C'],
                        ['A', 'D'],
                        ['D', 'F'],
                        ['B', 'C']
                    ], ['A']],
            "answer": 2,
            "explanation": [
                "crushed server has 3 connected server to it, but 2 of them are connected so they are still in one network",
                ['', '',   '',   '',   '',
                 '', 'B',  '',  'C',   '',
                 '', '',  'A',   '',   '',
                 '', '',   '',  'D',  'F',
                 '', '',   '',   '',   ''],
            ],
        }
    ]
}
