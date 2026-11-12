---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.4 FinancialInstrumentAttributes112", "35.1.11.4.3 RegistrationForm <RegnForm>"]
file_pages: [1464]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.4.3 RegistrationForm <RegnForm>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1464 to 1464.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1464

```text
DayCountBasis <DayCntBsis> contains one of the following elements (see
"InterestComputationMethodFormat4Choice" on page 1612 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1612
Or}   Proprietary <Prtry> [1..1] ± 1615
35.1.11.4.3  RegistrationForm <RegnForm>
Presence: [0..1]
Definition: Specifies the form, this is, ownership, of the security.
RegistrationForm <RegnForm> contains one of the following elements (see "FormOfSecurity6Choice"
on page 1630 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1630
Or}   Proprietary <Prtry> [1..1] ± 1630
35.1.11.4.4  PaymentFrequency <PmtFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of an interest payment.
PaymentFrequency <PmtFrqcy> contains one of the following elements (see "Frequency23Choice"
on page 1479 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1479
Or}   Proprietary <Prtry> [1..1] ± 1479
35.1.11.4.5  PaymentStatus <PmtSts>
Presence: [0..1]
Definition: Status of payment of a security at a particular time.
PaymentStatus <PmtSts> contains one of the following elements (see
"SecuritiesPaymentStatus5Choice" on page 1957 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1957
Or}   Proprietary <Prtry> [1..1] ± 1958
35.1.11.4.6  VariableRateChangeFrequency <VarblRateChngFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of change to the variable rate of an interest bearing instrument.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1464 March 2026
```

