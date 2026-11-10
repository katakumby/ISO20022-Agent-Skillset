---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.2 FinancialInstrumentAttributes92", "82.1.13.2.3 RegistrationForm <RegnForm>"]
file_pages: [2937]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.2.3 RegistrationForm <RegnForm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2937 to 2937.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2937

```text
DayCountBasis <DayCntBsis> contains one of the following elements (see
"InterestComputationMethodFormat4Choice" on page 3032 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3033
Or}   Proprietary <Prtry> [1..1] ± 3036
82.1.13.2.3  RegistrationForm <RegnForm>
Presence: [0..1]
Definition: Specifies the form, this is, ownership, of the security.
RegistrationForm <RegnForm> contains one of the following elements (see "FormOfSecurity6Choice"
on page 3045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3045
Or}   Proprietary <Prtry> [1..1] ± 3046
82.1.13.2.4  PaymentFrequency <PmtFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of an interest payment.
PaymentFrequency <PmtFrqcy> contains one of the following elements (see "Frequency23Choice"
on page 2959 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2959
Or}   Proprietary <Prtry> [1..1] ± 2959
82.1.13.2.5  PaymentStatus <PmtSts>
Presence: [0..1]
Definition: Status of payment of a security at a particular time.
PaymentStatus <PmtSts> contains one of the following elements (see
"SecuritiesPaymentStatus5Choice" on page 3166 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3167
Or}   Proprietary <Prtry> [1..1] ± 3167
82.1.13.2.6  VariableRateChangeFrequency <VarblRateChngFrqcy>
Presence: [0..1]
Definition: Specifies the frequency of change to the variable rate of an interest bearing instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2937 August 2026
```

