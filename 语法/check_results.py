import sqlite3
import json

conn = sqlite3.connect('japanese_grammar.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT grammar_point, translation_problems
    FROM grammar_points
    WHERE translation_problems IS NOT NULL
    LIMIT 3
""")

for grammar_point, problems_json in cursor.fetchall():
    print(f"\n{'='*60}")
    print(f"文法ポイント: {grammar_point}")
    print(f"{'='*60}")

    problems = json.loads(problems_json)
    for i, problem in enumerate(problems['problems'], 1):
        print(f"\n問題 {i} (難易度: {problem.get('difficulty', '?')})")
        print(f"  中国語: {problem['chinese']}")
        print(f"  日本語: {problem['japanese_answer']}")

conn.close()