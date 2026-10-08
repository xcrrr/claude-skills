"""Execute documented data-cleaner examples against literal data-integrity cases.

Run with an already available pandas environment. DATA_CLEANER_SKILL can select
an explicit original/candidate entry; no dependency installation or live data.
"""
from pathlib import Path
from contextlib import contextmanager, redirect_stdout
from io import StringIO
import ast
import os
import re
import tempfile
import unittest

import pandas as pd

DEFAULT = Path(__file__).resolve().parents[1] / "skills/data/data-cleaner/SKILL.md"
ENTRY = Path(os.environ.get("DATA_CLEANER_SKILL", DEFAULT))
SOURCE = ENTRY.read_text(encoding="utf-8")


def block(heading):
    section = SOURCE.split(heading, 1)[1]
    return re.search(r"```python\n(.*?)\n```", section, re.S).group(1)


@contextmanager
def fixture(filename, body):
    previous = Path.cwd()
    with tempfile.TemporaryDirectory() as directory:
        os.chdir(directory)
        Path(filename).write_text(body, encoding="utf-8")
        try:
            yield
            assert Path(filename).read_text(encoding="utf-8") == body
        finally:
            os.chdir(previous)


class CleaningExampleTests(unittest.TestCase):
    def execute(self, code, **scope):
        scope = {"pd": pd, **scope}
        with redirect_stdout(StringIO()):
            exec(compile(code, str(ENTRY), "exec"), scope)
        return scope

    def test_csv_audit_preserves_lexical_identifiers_and_literal_na(self):
        raw = "account_id,comment\n0012,NA\nNA,Text\n0042,MixedCase\n"
        with fixture("raw_data.csv", raw):
            scope = self.execute(block("### Step 1:"))
        observed = scope.get("raw_df", scope["df"])
        self.assertEqual(observed["account_id"].tolist(), ["0012", "NA", "0042"])
        self.assertEqual(observed["comment"].tolist(), ["NA", "Text", "MixedCase"])

    def test_empty_categorical_mode_does_not_crash_or_impute(self):
        code = "# Strategy 4:" + block("### Step 2:").split("# Strategy 4:", 1)[1].split("# Strategy 5:", 1)[0]
        frame = pd.DataFrame({"category": [None, None]})
        try:
            result = self.execute(code, df=frame)["df"]
        except (KeyError, IndexError) as error:
            self.fail(f"Documented mode example indexes an empty mode: {error}")
        self.assertTrue(result["category"].isna().all())

    def test_more_than_half_missing_uses_ceiling_for_odd_column_count(self):
        code = "# Strategy 1:" + block("### Step 2:").split("# Strategy 1:", 1)[1].split("# Strategy 2:", 1)[0]
        frame = pd.DataFrame([[1, 2, None, None, None], [1, 2, 3, None, None]])
        self.assertEqual(self.execute(code, df=frame)["df"].index.tolist(), [1])

    def test_five_declared_date_formats_parse_without_guessing(self):
        result = self.execute(block("### Example 2:"))
        self.assertEqual(result["standardized"].tolist(), ["2023-01-15"] * 5)

    def test_type_conversion_distinguishes_missing_invalid_and_ambiguous(self):
        frame = pd.DataFrame({
            "revenue": ["10", "", "bad", "20", "30", "40", "50"],
            "quantity": ["1"] * 7,
            "order_date": ["20230115", "03/04/2023", "99/99/2023", "15/01/2023", "", "12/12/2023", "03/04/23"],
            "is_active": ["Yes"] * 7,
            "region": ["East"] * 7,
        })
        result = self.execute(block("### Step 4:"), df=frame)
        self.assertEqual(result.get("revenue_missing", pd.Series()).tolist(), [False, True, False, False, False, False, False])
        self.assertEqual(result.get("revenue_invalid", pd.Series()).tolist(), [False, False, True, False, False, False, False])
        self.assertEqual(result.get("date_missing", pd.Series()).tolist(), [False, False, False, False, True, False, False])
        self.assertEqual(result.get("date_ambiguous", pd.Series()).tolist(), [False, True, False, False, False, False, True])
        self.assertEqual(result.get("date_invalid", pd.Series()).tolist(), [False, False, True, False, False, False, False])
        dates = result["df"]["order_date"]
        self.assertEqual([None if pd.isna(x) else x.strftime("%Y-%m-%d") for x in dates],
                         ["2023-01-15", None, None, "2023-01-15", None, "2023-12-12", None])

    def test_sales_example_preserves_raw_distinct_rows_and_invalid_amounts(self):
        raw = ("account_id,revenue,region,order_date,comment\n"
               "0012,10,west,2023-01-15,a\n"
               "0012,10,WEST,2023-01-15,a\n"
               "0042,,east,2023-01-15,b\n"
               "0050,broken,east,2023-01-15,c\n"
               "NA,20,east,2023-01-15,NA\n")
        with fixture("sales_raw.csv", raw):
            result = self.execute(block("### Example 1:"))
            written = pd.read_csv("sales_clean.csv", dtype="string", keep_default_na=False)
        self.assertEqual(written["account_id"].tolist(), ["0012", "0012", "0042", "0050", "NA"])
        self.assertEqual(written["revenue_missing"].tolist(), ["0", "0", "1", "0", "0"])
        self.assertEqual(written["revenue_invalid"].tolist(), ["0", "0", "0", "1", "0"])
        self.assertEqual(written["revenue"].tolist(), ["10.0", "10.0", "10.0", "", "20.0"])
        self.assertEqual(result["raw_df"]["region"].tolist(), ["west", "WEST", "east", "east", "east"])

    def test_normalization_preserves_unselected_lexical_columns(self):
        frame = pd.DataFrame({
            "account_id": ["0012", "NA"],
            "comment": [" KeepCase ", "Literal NA"],
            "country": ["USA", "uk"],
            "price": ["$1,200.50", "20"],
            "phone": ["+1 (234) 567-8901", "555-0100"],
            "email": ["USER@EXAMPLE.COM", "other@example.com"],
        })
        result = self.execute(block("### Step 5:"), df=frame)["df"]
        self.assertEqual(result["account_id"].tolist(), ["0012", "NA"])
        self.assertEqual(result["comment"].tolist(), [" KeepCase ", "Literal NA"])
        self.assertEqual(result["country"].tolist(), ["United States", "United Kingdom"])

    def test_sales_output_keeps_date_failure_states(self):
        raw = ("account_id,revenue,region,order_date\n"
               "0001,10,west,\n"
               "0002,20,west,not-a-date\n"
               "0003,30,west,03/04/23\n"
               "0004,40,west,12/12/2023\n")
        with fixture("sales_raw.csv", raw):
            self.execute(block("### Example 1:"))
            written = pd.read_csv("sales_clean.csv", dtype="string", keep_default_na=False)
        self.assertEqual(written["order_date_missing"].tolist(), ["1", "0", "0", "0"])
        self.assertEqual(written["order_date_invalid"].tolist(), ["0", "1", "0", "0"])
        self.assertEqual(written["order_date_ambiguous"].tolist(), ["0", "0", "1", "0"])
        self.assertEqual(written["order_date"].tolist(), ["", "", "", "2023-12-12"])

    def test_all_documented_python_fragments_are_valid_python(self):
        for snippet in re.findall(r"```python\n(.*?)\n```", SOURCE, re.S):
            ast.parse(snippet)


if __name__ == "__main__":
    unittest.main(verbosity=2)
