---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.30 OwnershipBeneficiaryRate1"]
file_pages: [5018]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.30 OwnershipBeneficiaryRate1

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5018 to 5018.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5018

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.30.30  OwnershipBeneficiaryRate1
Definition: Percentage of ownership or of beneficial ownership of the shares/units in the account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Rate <Rate> [0..1] Rate 5018
   Fraction <Frctn> [0..1] Text 5018
Constraints
• OwnershipBeneficiaryRateRule
Either Rate or Fraction must be present. Both may be present.
66.1.30.30.1  Rate <Rate>
Presence: [0..1]
Definition: Ownership or beneficial ownership expressed as a percentage.
Datatype: "PercentageRate" on page 5401
66.1.30.30.2  Fraction <Frctn>
Presence: [0..1]
Definition: Ownership or beneficial ownership expressed as a fraction or another form.
Datatype: "Max35Text" on page 5403
66.1.30.31  RegulatoryInformation1
Definition: Regulatory information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sector <Sctr> [0..1] Text 5018
   Branch <Brnch> [0..1] Text 5019
   Group <Grp> [0..1] Text 5019
   Other <Othr> [0..1] Text 5019
66.1.30.31.1  Sector <Sctr>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5018 May 2026
```

