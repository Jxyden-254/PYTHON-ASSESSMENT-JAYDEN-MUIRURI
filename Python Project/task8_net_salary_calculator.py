"""
Task 8: Net-Salary Calculator Program
File: task8_net_salary_calculator.py

Captures employee details and computes gross pay, PAYE, NHIF, NSSF,
total deductions and net pay.

Salary components:
    House Allowance  : Ksh 6,500 (fixed)
    Medical Allowance: Ksh 5,500 (fixed)
    PAYE brackets    :  0 – 24 999  →  0 %
                       25 000 – 39 999  →  4 %
                       40 000 – 59 999  →  5 %
                       60 000+          →  6 %
    NHIF             : 2 % of gross pay
    NSSF             : 3 % of basic salary
"""

# ── Calculate PAYE ────────────────────────────────────────────────────────
def compute_paye(gross):
    """Return the PAYE amount based on gross pay brackets.

    Args:
        gross (float): Employee's gross pay in Ksh.

    Returns:
        float: PAYE deduction in Ksh.
    """
    if gross < 25_000:
        rate = 0.00
    elif gross < 40_000:
        rate = 0.04
    elif gross < 60_000:
        rate = 0.05
    else:
        rate = 0.06
    return gross * rate


def main():
    """Run the net-salary calculator."""

    print("=" * 55)
    print("         NET-SALARY CALCULATOR")
    print("         Jeshi Payroll System")
    print("=" * 55)

    # ── Capture employee details ──────────────────────────────────────────
    payroll_number = input("Payroll Number   : ")
    employee_name  = input("Employee Name    : ")
    gender         = input("Gender (M/F)     : ").upper()
    department     = input("Department       : ")

    while True:
        try:
            basic_salary = float(input("Basic Salary (Ksh): "))
            if basic_salary <= 0:
                print("  Salary must be greater than zero.")
                continue
            break
        except ValueError:
            print("  Please enter a valid numeric salary.")

    # ── Fixed allowances ─────────────────────────────────────────────────
    house_allowance   = 6_500.00
    medical_allowance = 5_500.00

    # ── Gross pay ─────────────────────────────────────────────────────────
    gross_pay = basic_salary + house_allowance + medical_allowance

    # ── Deductions ────────────────────────────────────────────────────────
    paye = compute_paye(gross_pay)
    nhif = gross_pay * 0.02         # 2 % of gross pay
    nssf = basic_salary * 0.03      # 3 % of basic salary

    total_deductions = paye + nhif + nssf

    # ── Net pay ───────────────────────────────────────────────────────────
    net_pay = gross_pay - total_deductions

    # ── Formatted output ──────────────────────────────────────────────────
    print("\n" + "=" * 55)
    print("         EMPLOYEE SALARY SLIP")
    print("=" * 55)
    print(f"  Payroll Number  : {payroll_number}")
    print(f"  Employee Name   : {employee_name}")
    print(f"  Gender          : {'Male' if gender == 'M' else 'Female'}")
    print(f"  Department      : {department}")
    print("-" * 55)
    print("  EARNINGS")
    print(f"    Basic Salary          : Ksh {basic_salary:>10,.2f}")
    print(f"    House Allowance       : Ksh {house_allowance:>10,.2f}")
    print(f"    Medical Allowance     : Ksh {medical_allowance:>10,.2f}")
    print(f"                           {'─'*14}")
    print(f"  GROSS PAY             : Ksh {gross_pay:>10,.2f}")
    print("-" * 55)
    print("  DEDUCTIONS")
    print(f"    PAYE                  : Ksh {paye:>10,.2f}")
    print(f"    NHIF (2%)             : Ksh {nhif:>10,.2f}")
    print(f"    NSSF (3%)             : Ksh {nssf:>10,.2f}")
    print(f"                           {'─'*14}")
    print(f"  TOTAL DEDUCTIONS      : Ksh {total_deductions:>10,.2f}")
    print("=" * 55)
    print(f"  NET PAY               : Ksh {net_pay:>10,.2f}")
    print("=" * 55)


if __name__ == "__main__":
    main()
