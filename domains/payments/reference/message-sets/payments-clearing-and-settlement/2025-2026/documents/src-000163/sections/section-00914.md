---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.14 Payment Type", "10.1.14.2 PaymentTypeInformation27", "10.1.14.2.6 CategoryPurpose <CtgyPurp>", "10.1.14.2.6.1 Code <Cd>"]
file_pages: [1209]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.14.2.6.1 Code <Cd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1209 to 1209.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1209

```text
Definition: Specifies the high level purpose of the instruction based on a set of pre-defined categories.
Usage: This is used by the initiating party to provide information concerning the processing of the
payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
CategoryPurpose <CtgyPurp> contains one of the following CategoryPurpose1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1209
Or}   Proprietary <Prtry> [1..1] Text 1209
10.1.14.2.6.1  Code <Cd>
Presence: [1..1]
Definition: Category purpose, as published in an external category purpose code list.
Datatype: "ExternalCategoryPurpose1Code" on page 1228
10.1.14.2.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 1246
10.1.15 Person Identification
10.1.15.1  Contact13
Definition: Specifies the details of the contact person.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1209 March 2026
```

