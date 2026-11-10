---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["9 camt.068.001.02 IntraBalanceMovementConfirmationV02", "9.2 Structure"]
file_pages: [134]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 9.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 134 to 134.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 134

```text
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntConf> [1..1]  
   Identification <Id> [0..1]  136
     Identification <Id> [1..1] Text 136
     CreationDateTime <CreDtTm> [0..1] ± 136
     CopyDuplicate <CpyDplct> [0..1] CodeSet 137
     MessageOriginator <MsgOrgtr> [0..1] ± 137
     MessageRecipient <MsgRcpt> [0..1] ± 137
   AdditionalParameters <AddtlParams> [0..1] ± 138
   CashAccount <CshAcct> [1..1] ± C9, C8 138
   CashAccountOwner <CshAcctOwnr> [0..1] ± 139
   CashAccountServicer <CshAcctSvcr> [0..1] ± 139
   IntraBalance <IntraBal> [1..1]  140
     SettledAmount <SttldAmt> [0..1] ± 141
     PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 142
     RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 142
     SettlementDate <SttlmDt> [1..1] ± 142
     BalanceFrom <BalFr> [1..1]  142
       Type <Tp> [1..1]  143
{Or         Code <Cd> [1..1] CodeSet 143
Or}         Proprietary <Prtry> [1..1] ± 143
       QuantityBreakdown <QtyBrkdwn> [0..*]  144
         LotNumber <LotNb> [0..1] ± 144
         LotAmount <LotAmt> [0..1] ± 144
         LotQuantity <LotQty> [0..1] ± 144
         CashSubBalanceType <CshSubBalTp> [0..1] ± 145
     BalanceTo <BalTo> [1..1]  145
       Type <Tp> [1..1]  145
{Or         Code <Cd> [1..1] CodeSet 146
Or}         Proprietary <Prtry> [1..1] ± 146
       QuantityBreakdown <QtyBrkdwn> [0..*]  146
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities 134 August 2026
```

