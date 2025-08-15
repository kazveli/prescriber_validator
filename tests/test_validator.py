from src.core.validator import Validator

def test_validator_call_others():
    validador = Validator('doc/prescribers.xlsx', cr_type=None, auto=True, headless=True)
    validador.run()
