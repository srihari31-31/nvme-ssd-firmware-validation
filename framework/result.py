from dataclasses import dataclass

@dataclass
class TestResult:
    name: str
    status: str   # PASS or FAIL
    message: str

    def __str__(self) -> str:
        return f"{self.name}: {self.status} - {self.message}"
