---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.1.3 Authorisation <Authstn>"]
file_pages: [285]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.1.3 Authorisation <Authstn>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 285 to 285.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 285

```text
4.4.1.3  Authorisation <Authstn>
Presence: [0..2]
Definition: User identification or any user key to be used to check whether the initiating party is allowed
to initiate transactions from the account specified in the message.
Usage: The content is not of a technical nature, but reflects the organisational structure at the initiating
side.
The authorisation element can typically be used in relay scenarios, payment initiations, payment returns
or payment reversals that are initiated on behalf of a party different from the initiating party.
Authorisation <Authstn> contains one of the following elements (see "Authorisation1Choice" on
page 552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 553
Or}   Proprietary <Prtry> [1..1] Text 553
4.4.1.4  NumberOfTransactions <NbOfTxs>
Presence: [1..1]
Definition: Number of individual transactions contained in the message.
Datatype: "Max15NumericText" on page 608
4.4.1.5  ControlSum <CtrlSum>
Presence: [0..1]
Definition: Total of all individual amounts included in the message, irrespective of currencies.
Datatype: "DecimalNumber" on page 606
4.4.1.6  GroupReversal <GrpRvsl>
Presence: [0..1]
Definition: Indicates whether the reversal applies to the whole group of transactions or to individual
transactions within the original group.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 605):
• Meaning When True: True
• Meaning When False: False
4.4.1.7  InitiatingParty <InitgPty>
Presence: [0..1]
Definition: Party that initiates the reversal message.
Usage: This can be either the creditor or a party that initiates the reversal of the direct debit on behalf of
the creditor.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 285 March 2026
```

