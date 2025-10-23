from backend.parser import extract_skills
from io import BytesIO

def test_extract_skills():
    dummy_pdf = BytesIO(b"Python and Docker developer")
    result = extract_skills(dummy_pdf)
    assert "Python" in result
