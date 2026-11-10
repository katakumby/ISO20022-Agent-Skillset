---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.1 FinancialInstrumentAttributes138", "7.1.12.1.3 RegistrationForm <RegnForm>"]
file_pages: [328]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.1.3 RegistrationForm <RegnForm>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 328 to 328.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 328

```text
DayCountBasis <DayCntBsis> contains one of the following elements (see
"InterestComputationMethodFormat4Choice" on page 391 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 391
Or}   Proprietary <Prtry> [1..1] ± 394
7.1.12.1.3  RegistrationForm <RegnForm>
Presence: [0..1]
Definition: Specifies the form, this is, ownership, of the security.
RegistrationForm <RegnForm> contains one of the following elements (see "FormOfSecurity6Choice"
on page 401 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 402
Or}   Proprietary <Prtry> [1..1] ± 402
7.1.12.1.4  PaymentFrequency <PmtFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of an interest payment.
PaymentFrequency <PmtFrqcy> contains one of the following elements (see "Frequency23Choice"
on page 346 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 346
Or}   Proprietary <Prtry> [1..1] ± 346
7.1.12.1.5  PaymentStatus <PmtSts>
Presence: [0..1]
Definition: Status of payment of a security at a particular time.
PaymentStatus <PmtSts> contains one of the following elements (see
"SecuritiesPaymentStatus5Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 476
Or}   Proprietary <Prtry> [1..1] ± 476
7.1.12.1.6  VariableRateChangeFrequency <VarblRateChngFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of change to the variable rate of an interest bearing instrument.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 328 March 2026
```

