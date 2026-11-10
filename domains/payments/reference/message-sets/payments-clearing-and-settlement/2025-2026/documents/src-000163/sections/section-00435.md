---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.1 ReversalIdentification <RvslId>"]
file_pages: [601]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.1 ReversalIdentification <RvslId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 601 to 601.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 601

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or       Party <Pty> [1..1] ± 698
Or}       Agent <Agt> [1..1] ± 699
     Purpose <Purp> [0..1] ± 700
   SupplementaryData <SplmtryData> [0..*] ± C35 700
Constraints
• ChargesInformationAndReversedInstructedAmountRule
If ChargesInformation is present, then ReversedInstructedAmount must be present.
On Condition
    /ChargesInformation[1] is present
 And    /ChargesInformation[1]/Amount is present
Following Must be True
    /ReversedInstructedAmount Must be present
• ReversedInstructedAmountAndExchangeRate1Rule
If ReversedInstructedAmount is present and the currency is different from the currency in
InterbankSettlementAmount, then ExchangeRate must be present.
On Condition
    /ReversedInstructedAmount is present
 And    /ReversedInstructedAmount/attribute::Currency is different from /
ReversedInterbankSettlementAmount/attribute::Currency
Following Must be True
    /ExchangeRate Must be present
• ReversedInstructedAmountAndExchangeRate2Rule
If ReversedInstructedAmount is present and the currency is the same as the currency in
InterbankSettlementAmount, then ExchangeRate is not allowed.
On Condition
    /ReversedInstructedAmount is present
 And    /ReversedInstructedAmount/attribute::Currency is equal to /
ReversedInterbankSettlementAmount/attribute::Currency
Following Must be True
    /ExchangeRate Must be absent
5.4.3.1  ReversalIdentification <RvslId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the reversed transaction.
Usage: The instructing party is the party sending the reversal message and not the party that sent the
original instruction that is being reversed.
Datatype: "Max35Text" on page 1246
5.4.3.2  OriginalGroupInformation <OrgnlGrpInf>
Presence: [0..1]
Definition: Provides information on the original message.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
601 March 2026
```

