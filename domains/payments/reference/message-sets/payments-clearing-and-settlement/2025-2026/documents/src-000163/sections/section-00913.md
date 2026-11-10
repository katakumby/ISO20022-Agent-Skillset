---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.14 Payment Type", "10.1.14.2 PaymentTypeInformation27", "10.1.14.2.4 LocalInstrument <LclInstrm>"]
file_pages: [1208]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.14.2.4 LocalInstrument <LclInstrm>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1208 to 1208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1208

```text
10.1.14.2.4  LocalInstrument <LclInstrm>
Presence: [0..1]
Definition: User community specific instrument.
Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the
service or service level.
LocalInstrument <LclInstrm> contains one of the following LocalInstrument2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1208
Or}   Proprietary <Prtry> [1..1] Text 1208
10.1.14.2.4.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the local instrument, as published in an external local instrument code list.
Datatype: "ExternalLocalInstrument1Code" on page 1230
10.1.14.2.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the local instrument, as a proprietary code.
Datatype: "Max35Text" on page 1246
10.1.14.2.5  SequenceType <SeqTp>
Presence: [0..1]
Definition: Identifies the direct debit sequence, such as first, recurrent, final or one-off.
Datatype: "SequenceType3Code" on page 1237
CodeName Name Definition
FRST First First collection of a series of direct debit
instructions.
RCUR Recurring Direct debit instruction where the
debtor's authorisation is used for regular
direct debit transactions initiated by the
creditor.
FNAL Final Final collection of a series of direct debit
instructions.
OOFF OneOff Direct debit instruction where the
debtor's authorisation is used to initiate
one single direct debit transaction.
RPRE Represented Collection used to re-present previously
reversed or returned direct debit
transactions.
10.1.14.2.6  CategoryPurpose <CtgyPurp>
Presence: [0..1]
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1208 March 2026
```

