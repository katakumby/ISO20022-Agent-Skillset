---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 camt.068.001.02 IntraBalanceMovementConfirmationV02", "4.2 Structure"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.068.001.02"]
---

# 4.2 Structure

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <IntraBalMvmntConf> [1..1]  
   Identification <Id> [0..1]  53
     Identification <Id> [1..1] Text 53
     CreationDateTime <CreDtTm> [0..1] ± 53
     CopyDuplicate <CpyDplct> [0..1] CodeSet 54
     MessageOriginator <MsgOrgtr> [0..1] ± 54
     MessageRecipient <MsgRcpt> [0..1] ± 54
   AdditionalParameters <AddtlParams> [0..1] ± 55
   CashAccount <CshAcct> [1..1] ± C9, C8 55
   CashAccountOwner <CshAcctOwnr> [0..1] ± 56
   CashAccountServicer <CshAcctSvcr> [0..1] ± 56
   IntraBalance <IntraBal> [1..1]  57
     SettledAmount <SttldAmt> [0..1] ± 58
     PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 59
     RemainingSettlementAmount <RmngSttlmAmt> [0..1] ± 59
     SettlementDate <SttlmDt> [1..1] ± 59
     BalanceFrom <BalFr> [1..1]  59
       Type <Tp> [1..1]  60
{Or         Code <Cd> [1..1] CodeSet 60
Or}         Proprietary <Prtry> [1..1] ± 60
       QuantityBreakdown <QtyBrkdwn> [0..*]  61
         LotNumber <LotNb> [0..1] ± 61
         LotAmount <LotAmt> [0..1] ± 61
         LotQuantity <LotQty> [0..1] ± 61
         CashSubBalanceType <CshSubBalTp> [0..1] ± 62
     BalanceTo <BalTo> [1..1]  62
       Type <Tp> [1..1]  62
{Or         Code <Cd> [1..1] CodeSet 63
Or}         Proprietary <Prtry> [1..1] ± 63
       QuantityBreakdown <QtyBrkdwn> [0..*]  63
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.068.001.02
IntraBalanceMovementConfirmationV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
51 March 2024
```

