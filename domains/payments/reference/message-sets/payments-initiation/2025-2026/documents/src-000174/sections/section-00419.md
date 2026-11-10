---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Payment Type", "6.1.14.3 PaymentTypeInformation29", "6.1.14.3.2 ServiceLevel <SvcLvl>"]
file_pages: [570]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.3.2 ServiceLevel <SvcLvl>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 570 to 570.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 570

```text
Datatype: "Priority2Code" on page 600
CodeName Name Definition
HIGH High Priority level is high.
NORM Normal Priority level is normal.
6.1.14.3.2  ServiceLevel <SvcLvl>
Presence: [0..*]
Definition: Agreement under which or rules under which the transaction should be processed.
ServiceLevel <SvcLvl> contains one of the following ServiceLevel8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 570
Or}   Proprietary <Prtry> [1..1] Text 570
6.1.14.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as published in an
external service level code list.
Datatype: "ExternalServiceLevel1Code" on page 597
6.1.14.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as a proprietary code.
Datatype: "Max35Text" on page 609
6.1.14.3.3  LocalInstrument <LclInstrm>
Presence: [0..1]
Definition: User community specific instrument.
Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the
service or service level.
LocalInstrument <LclInstrm> contains one of the following LocalInstrument2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 570
Or}   Proprietary <Prtry> [1..1] Text 571
6.1.14.3.3.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the local instrument, as published in an external local instrument code list.
Datatype: "ExternalLocalInstrument1Code" on page 595
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 570 March 2026
```

