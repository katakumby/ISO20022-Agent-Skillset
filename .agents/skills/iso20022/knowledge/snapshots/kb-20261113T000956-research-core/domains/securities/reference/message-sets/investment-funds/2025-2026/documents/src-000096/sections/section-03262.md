---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.4 FinancialInstrument87", "66.1.18.4.5 ClassType <ClssTp>"]
file_pages: [4498]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.4.5 ClassType <ClssTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4498 to 4498.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4498

```text
66.1.18.4.5  ClassType <ClssTp>
Presence: [0..1]
Definition: Features of units offered by the fund. For example, a unit may have a specific load structure,
for example, front end or back end, an income policy, for example, pay out or accumulate, or a trailer
policy, for example, with or without. Fund classes are typically denoted by a single character, for
example, 'Class A', 'Class 2'.
Datatype: "Max35Text" on page 5403
66.1.18.4.6  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Form, that is, ownership, of the security, that is, registered or bearer.
Datatype: "FormOfSecurity1Code" on page 5304
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
66.1.18.4.7  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to the class type, that is, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 5294
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
66.1.18.4.8  ProductGroup <PdctGrp>
Presence: [0..1]
Definition: Company specific description of a group of funds.
Datatype: "Max140Text" on page 5402
66.1.18.4.9  BlockedHoldingDetails <BlckdHldgDtls>
Presence: [0..1]
Definition: When an account at fund or security level is blocked, this specifies details on how the holding
is blocked.
Impacted by: C18 "HoldingCertificateNumberRule", C26 "PartialHoldingUnits1Rule", C27
"PartialHoldingUnits2Rule", C28 "PartialHoldingUnits3Rule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4498 May 2026
```

