---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.17 Payment Type", "6.1.17.1 PaymentTypeInformation27", "6.1.17.1.3 ServiceLevel <SvcLvl>"]
file_pages: [870]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.17.1.3 ServiceLevel <SvcLvl>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 870 to 870.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 870

```text
6.1.17.1.3  ServiceLevel <SvcLvl>
Presence: [0..*]
Definition: Agreement under which or rules under which the transaction should be processed.
ServiceLevel <SvcLvl> contains one of the following ServiceLevel8Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 870
Or}   Proprietary <Prtry> [1..1] Text 870
6.1.17.1.3.1  Code <Cd>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as published in an
external service level code list.
Datatype: "ExternalServiceLevel1Code" on page 900
6.1.17.1.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies a pre-agreed service or level of service between the parties, as a proprietary code.
Datatype: "Max35Text" on page 916
6.1.17.1.4  LocalInstrument <LclInstrm>
Presence: [0..1]
Definition: User community specific instrument.
Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the
service or service level.
LocalInstrument <LclInstrm> contains one of the following LocalInstrument2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 870
Or}   Proprietary <Prtry> [1..1] Text 870
6.1.17.1.4.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the local instrument, as published in an external local instrument code list.
Datatype: "ExternalLocalInstrument1Code" on page 898
6.1.17.1.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the local instrument, as a proprietary code.
Datatype: "Max35Text" on page 916
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
870 March 2026
```

