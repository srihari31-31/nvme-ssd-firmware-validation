from scripts import (
    nvme_info,
    nvme_read_test,
    nvme_write_test,
    nvme_error_test
)

tests = [
    nvme_info.run,
    nvme_read_test.run,
    nvme_write_test.run,
    nvme_error_test.run
]

def main():
    print("\nNVMe SSD Firmware Validation Results")
    print("-" * 45)

    passed = 0
    for test in tests:
        result = test()
        print(result)
        if result.status == "PASS":
            passed += 1

    print("-" * 45)
    print(f"Summary: {passed}/{len(tests)} tests PASSED\n")

if __name__ == "__main__":
    main()
