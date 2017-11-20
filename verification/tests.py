
TEXT = '''
When I was One,
I had just begun.
When I was Two,
I was nearly new.
'''

TEXT2 = '''It's flying from somewhere
As fast as it can,
I couldn't keep up with it,
Not if I ran.'''

TESTS = {
    "Basics": [
        {
            "input": [TEXT, ['i', 'was', 'three']],
            "answer": {
                'i': 4,
                'was': 3,
                'three': 0
            }
        }
    ],
    "Extra": [
        {
            "input": [TEXT, ['one', 'two', 'three']],
            "answer": {
                'one': 1,
                'two': 1,
                'three': 0
            }
        },
        {
            "input": [TEXT2, ["it's", "ran"]],
            "answer": {
                "it's": 1,
                "ran": 1
            }
        }
    ]
}
