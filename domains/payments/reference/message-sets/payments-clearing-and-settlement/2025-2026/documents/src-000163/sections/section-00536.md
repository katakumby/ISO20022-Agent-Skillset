---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.2 PaymentTypeInformation <PmtTpInf>"]
file_pages: [740]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.2 PaymentTypeInformation <PmtTpInf>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 740 to 740.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 740

```text
PaymentIdentification <PmtId> contains the following elements (see "PaymentIdentification13" on
page 1183 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionIdentification <InstrId> [0..1] Text 1183
   EndToEndIdentification <EndToEndId> [1..1] Text 1184
   TransactionIdentification <TxId> [0..1] Text 1184
   UETR <UETR> [0..1] IdentifierSet 1184
   ClearingSystemReference <ClrSysRef> [0..1] Text 1184
Constraints
• TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Following Must be True
    /TransactionIdentification Must be present
 Or    /UETR Must be present
6.4.2.2  PaymentTypeInformation <PmtTpInf>
Presence: [0..1]
Definition: Set of elements used to further specify the type of transaction.
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation28" on page 1203 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 1204
   ClearingChannel <ClrChanl> [0..1] CodeSet 1204
   ServiceLevel <SvcLvl> [0..*]  1204
{Or     Code <Cd> [1..1] CodeSet 1205
Or}     Proprietary <Prtry> [1..1] Text 1205
   LocalInstrument <LclInstrm> [0..1]  1205
{Or     Code <Cd> [1..1] CodeSet 1205
Or}     Proprietary <Prtry> [1..1] Text 1205
   CategoryPurpose <CtgyPurp> [0..1]  1205
{Or     Code <Cd> [1..1] CodeSet 1206
Or}     Proprietary <Prtry> [1..1] Text 1206
6.4.2.3  InterbankSettlementAmount <IntrBkSttlmAmt>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
740 March 2026
```

