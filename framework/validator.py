from framework.logger import log_info, log_error
from framework.result import TestResult

class NVMeValidator:
    def pass_test(self, name: str, message: str) -> TestResult:
        log_info(f"{name} PASSED - {message}")
        return TestResult(name, "PASS", message)

    def fail_test(self, name: str, message: str) -> TestResult:
        log_error(f"{name} FAILED - {message}")
        return TestResult(name, "FAIL", message)
