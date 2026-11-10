---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.1.1 MessageIdentification <MsgId>"]
file_pages: [144]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.1.1 MessageIdentification <MsgId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 144 to 144.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 144

```text
3.4.1 GroupHeader <GrpHdr>
Presence: [1..1]
Definition: Set of characteristics shared by all individual transactions included in the message.
Impacted by: C33 "TotalInterbankSettlementAmountAndDateRule"
GroupHeader <GrpHdr> contains the following GroupHeader125 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 144
   CreationDateTime <CreDtTm> [1..1] DateTime 145
   Authorisation <Authstn> [0..2] ± 145
   BatchBooking <BtchBookg> [0..1] Indicator 145
   NumberOfTransactions <NbOfTxs> [1..1] Text 145
   ControlSum <CtrlSum> [0..1] Quantity 146
   TotalInterbankSettlementAmount <TtlIntrBkSttlmAmt> [0..1] Amount C1, C10 146
   InterbankSettlementDate <IntrBkSttlmDt> [0..1] Date 146
   SettlementInformation <SttlmInf> [1..1]  C29,
C30
146
     SettlementMethod <SttlmMtd> [1..1] CodeSet 147
     SettlementAccount <SttlmAcct> [0..1] ± C15,
C14
147
     ClearingSystem <ClrSys> [0..1]  148
{Or       Code <Cd> [1..1] CodeSet 148
Or}       Proprietary <Prtry> [1..1] Text 148
   PaymentTypeInformation <PmtTpInf> [0..1] ± 149
   InstructingAgent <InstgAgt> [0..1] ± 149
   InstructedAgent <InstdAgt> [0..1] ± 150
Constraints
• TotalInterbankSettlementAmountAndDateRule
If TotalInterbankSettlementAmount is present, then InterbankSettlementDate must be present.
On Condition
    /TotalInterbankSettlementAmount is present
Following Must be True
    /InterbankSettlementDate Must be present
3.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the instructing party, and sent to the next party in the
chain to unambiguously identify the message.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
144 March 2026
```

