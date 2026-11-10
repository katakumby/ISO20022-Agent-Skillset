---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.40 FormOfSecurity6Choice", "7.1.18.40.1 Code <Cd>"]
file_pages: [402]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.40.1 Code <Cd>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 402 to 402.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 402

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 402
Or}   Proprietary <Prtry> [1..1] ± 402
7.1.18.40.1  Code <Cd>
Presence: [1..1]
Definition: Form of the security expressed as an ISO 20022 code.
Datatype: "FormOfSecurity1Code" on page 511
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
7.1.18.40.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Form of the security expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.41  SettlingCapacity7Choice
Definition: Choice of format for the settlement capacity information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 402
Or}   Proprietary <Prtry> [1..1] ± 403
7.1.18.41.1  Code <Cd>
Presence: [1..1]
Definition: Settlement capacity expressed as an ISO 20022 code.
Datatype: "SettlingCapacity2Code" on page 540
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 402 March 2026
```

