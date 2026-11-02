import pytest 

from grading import grade_diarrhoea

@pytest.mark.parametrize("extra_stools, expected_grade", 
                         [
                             (0, 0), 
                             (1, 1), 
                             (3, 1), 
                             (4, 2), 
                             (6, 2), 
                             (7, 3), 
                             (10, 3),
                             (35,3)
                         ],
)
def test_grade_diarrhoea(extra_stools, expected_grade):
    assert grade_diarrhoea(extra_stools) == expected_grade

def test_rejected_negative_value():
    with pytest.raises(ValueError):
        grade_diarrhoea(-1)