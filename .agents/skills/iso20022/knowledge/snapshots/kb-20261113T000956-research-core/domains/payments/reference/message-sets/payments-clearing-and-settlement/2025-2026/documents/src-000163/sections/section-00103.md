---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.1.2 CreationDateTime <CreDtTm>"]
file_pages: [145]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.1.2 CreationDateTime <CreDtTm>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 145 to 145.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 145

```text
Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party
for a pre-agreed period.
Datatype: "Max35Text" on page 1246
3.4.1.2  CreationDateTime <CreDtTm>
Presence: [1..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 1239
3.4.1.3  Authorisation <Authstn>
Presence: [0..2]
Definition: User identification or any user key to be used to check whether the initiating party is allowed
to initiate transactions from the account specified in the message.
Usage: The content is not of a technical nature, but reflects the organisational structure at the initiating
side.
The authorisation element can typically be used in relay scenarios, payment initiations, payment returns
or payment reversals that are initiated on behalf of a party different from the initiating party.
Authorisation <Authstn> contains one of the following elements (see "Authorisation1Choice" on
page 1190 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1190
Or}   Proprietary <Prtry> [1..1] Text 1190
3.4.1.4  BatchBooking <BtchBookg>
Presence: [0..1]
Definition: Identifies whether a single entry per individual transaction or a batch entry for the sum of the
amounts of all transactions within the group of a message is requested.
Usage: Batch booking is used to request and not order a possible batch booking.
Datatype: One of the following values must be used (see "BatchBookingIndicator" on page 1241):
• Meaning When True: Identifies that a batch entry for the sum of the amounts of all transactions in the
batch or message is requested.
• Meaning When False: Identifies that a single entry for each of the transactions in the batch or
message is requested.
3.4.1.5  NumberOfTransactions <NbOfTxs>
Presence: [1..1]
Definition: Number of individual transactions contained in the message.
Datatype: "Max15NumericText" on page 1244
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
145 March 2026
```

