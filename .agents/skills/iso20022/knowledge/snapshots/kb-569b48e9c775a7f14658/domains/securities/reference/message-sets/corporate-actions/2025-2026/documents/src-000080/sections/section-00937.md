---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.27 System Identification"]
file_pages: [1155]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.27 System Identification

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1155 to 1155.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1155

```text
AcceptedReason <AccptdRsn> contains one of the following elements (see
"AcceptedStatus8Choice" on page 1141 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 1142
Or}   Reason <Rsn> [1..*]  C4 1142
     ReasonCode <RsnCd> [1..1]  1142
{Or       Code <Cd> [1..1] CodeSet 1143
Or}       Proprietary <Prtry> [1..1] ± 1143
     AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 1143
16.1.27 System Identification
16.1.27.1  ClearingSystemIdentification2Choice
Definition: Choice of a clearing system identifier.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1155
Or}   Proprietary <Prtry> [1..1] Text 1155
16.1.27.1.1  Code <Cd>
Presence: [1..1]
Definition: Identification of a clearing system, in a coded form as published in an external list.
Datatype: "ExternalClearingSystemIdentification1Code" on page 1209
16.1.27.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing
systems.
Datatype: "Max35Text" on page 1251
16.2 Message Datatypes
16.2.1 Amount
16.2.1.1  ActiveCurrencyAnd13DecimalAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217. The number of fractional digits (or minor unit of currency) is not
checked as per ISO 4217: It must be lesser than or equal to 13.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1155 February 2026
```

