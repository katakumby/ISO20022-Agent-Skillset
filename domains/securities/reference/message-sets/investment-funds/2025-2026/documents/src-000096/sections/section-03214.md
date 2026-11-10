---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.2 CostsAndCharges2", "66.1.8.2.2 IndividualCostOrCharge <IndvCostOrChrg>", "66.1.8.2.2.6 ReferencePeriod <RefPrd>", "66.1.8.2.2.6.1 StartDate <StartDt>"]
file_pages: [4450]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.2.2.6.1 StartDate <StartDt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4450 to 4450.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4450

```text
66.1.8.2.2.6.1  StartDate <StartDt>
Presence: [1..1]
Definition: Date on which the range starts.
Datatype: "ISODate" on page 5388
66.1.8.2.2.6.2  EndDate <EndDt>
Presence: [1..1]
Definition: Date on which the range ends.
Datatype: "ISODate" on page 5388
66.1.8.2.2.7  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the individual cost or charge.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.8.2.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about costs and charges.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.8.3  Charge26
Definition: Choice of formats for the type of charge.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4450 May 2026
```

