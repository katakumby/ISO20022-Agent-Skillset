---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.10 Mandate", "6.1.10.2 MandateTypeInformation2"]
file_pages: [550]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.10.2 MandateTypeInformation2

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 550 to 550.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 550

```text
6.1.10.2  MandateTypeInformation2
Definition: Set of elements used to further detail the information related to the type of payment.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ServiceLevel <SvcLvl> [0..1]  550
{Or     Code <Cd> [1..1] CodeSet 550
Or}     Proprietary <Prtry> [1..1] Text 550
   LocalInstrument <LclInstrm> [0..1]  550
{Or     Code <Cd> [1..1] CodeSet 551
Or}     Proprietary <Prtry> [1..1] Text 551
   CategoryPurpose <CtgyPurp> [0..1]  551
{Or     Code <Cd> [1..1] CodeSet 551
Or}     Proprietary <Prtry> [1..1] Text 551
   Classification <Clssfctn> [0..1] ± 551
6.1.10.2.1  ServiceLevel <SvcLvl>
Presence: [0..1]
Definition: Agreement under which or rules under which the mandate resides.
ServiceLevel <SvcLvl> contains one of the following ServiceLevel8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 550
Or}   Proprietary <Prtry> [1..1] Text 550
6.1.10.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as published in an
external service level code list.
Datatype: "ExternalServiceLevel1Code" on page 597
6.1.10.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as a proprietary code.
Datatype: "Max35Text" on page 609
6.1.10.2.2  LocalInstrument <LclInstrm>
Presence: [0..1]
Definition: User community specific instrument.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 550 March 2026
```

