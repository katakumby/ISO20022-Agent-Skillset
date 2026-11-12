---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.9 Financial Instrument", "9.1.9.2 FinancialInstrumentAttributes92", "9.1.9.2.3 RegistrationForm <RegnForm>"]
file_pages: [212]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.9.2.3 RegistrationForm <RegnForm>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 212 to 212.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 212

```text
DayCountBasis <DayCntBsis> contains one of the following elements (see
"InterestComputationMethodFormat4Choice" on page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 247
Or}   Proprietary <Prtry> [1..1] ± 250
9.1.9.2.3  RegistrationForm <RegnForm>
Presence: [0..1]
Definition: Specifies the form, this is, ownership, of the security.
RegistrationForm <RegnForm> contains one of the following elements (see "FormOfSecurity6Choice"
on page 251 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 251
Or}   Proprietary <Prtry> [1..1] ± 251
9.1.9.2.4  PaymentFrequency <PmtFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of an interest payment.
PaymentFrequency <PmtFrqcy> contains one of the following elements (see "Frequency23Choice"
on page 223 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 223
Or}   Proprietary <Prtry> [1..1] ± 223
9.1.9.2.5  PaymentStatus <PmtSts>
Presence: [0..1]
Definition: Status of payment of a security at a particular time.
PaymentStatus <PmtSts> contains one of the following elements (see
"SecuritiesPaymentStatus5Choice" on page 289 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 289
Or}   Proprietary <Prtry> [1..1] ± 290
9.1.9.2.6  VariableRateChangeFrequency <VarblRateChngFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of change to the variable rate of an interest bearing instrument.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 212 September 2025
```

