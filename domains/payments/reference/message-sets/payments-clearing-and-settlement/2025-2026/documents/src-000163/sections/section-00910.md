---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.14 Payment Type", "10.1.14.1 PaymentTypeInformation28", "10.1.14.1.3 ServiceLevel <SvcLvl>", "10.1.14.1.3.1 Code <Cd>"]
file_pages: [1205]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.14.1.3.1 Code <Cd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1205 to 1205.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1205

```text
ServiceLevel <SvcLvl> contains one of the following ServiceLevel8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1205
Or}   Proprietary <Prtry> [1..1] Text 1205
10.1.14.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as published in an
external service level code list.
Datatype: "ExternalServiceLevel1Code" on page 1233
10.1.14.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as a proprietary code.
Datatype: "Max35Text" on page 1246
10.1.14.1.4  LocalInstrument <LclInstrm>
Presence: [0..1]
Definition: User community specific instrument.
Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the
service or service level.
LocalInstrument <LclInstrm> contains one of the following LocalInstrument2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1205
Or}   Proprietary <Prtry> [1..1] Text 1205
10.1.14.1.4.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the local instrument, as published in an external local instrument code list.
Datatype: "ExternalLocalInstrument1Code" on page 1230
10.1.14.1.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the local instrument, as a proprietary code.
Datatype: "Max35Text" on page 1246
10.1.14.1.5  CategoryPurpose <CtgyPurp>
Presence: [0..1]
Definition: Specifies the high level purpose of the instruction based on a set of pre-defined categories.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1205 March 2026
```

