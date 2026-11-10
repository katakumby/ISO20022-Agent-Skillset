---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.9 RelatedTransaction <RltdTx>", "6.4.6.11.4.9.3 TransactionDetails <TxDtls>", "6.4.6.11.4.9.3.1 SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp>"]
file_pages: [232]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.9.3.1 SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 232 to 232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 232

```text
TransactionDetails <TxDtls> contains the following PenaltyTransactionRecord2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[1..1] ± 232
   SettlementDate <SttlmDt> [1..1] ± 233
   CorporateActionRelatedDate <CorpActnRltdDt> [0..1] ± 233
   SafekeepingAccount <SfkpgAcct> [1..1] ± 233
   AccountOwner <AcctOwnr> [0..1] ± 233
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 234
   Payment <Pmt> [1..1] CodeSet 234
   PostingQuantity <PstngQty> [1..1] ± 234
   CashAccount <CshAcct> [0..1] ± 235
   CashAccountOwner <CshAcctOwnr> [0..1] ± 235
   PostingAmount <PstngAmt> [0..1] ± 236
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 237
   MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 237
   SettlementStatusFailing <SttlmStsFlng> [0..1]  237
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 237
Or}     Reason <Rsn> [1..*]  237
       Code <Cd> [1..1]  238
{Or         Code <Cd> [1..1] CodeSet 238
Or}         Proprietary <Prtry> [1..1] ± 241
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 242
   BusinessDayEvent <BizDayEvt> [0..1]  242
     Type <Tp> [1..1]  242
{Or       Code <Cd> [1..1] CodeSet 242
Or}       Proprietary <Prtry> [1..1] ± 243
     ScheduledTime <SchdldTm> [1..1] DateTime 243
     EffectiveTime <FctvTm> [0..1] DateTime 243
     StartTime <StartTm> [0..1] DateTime 243
     EndTime <EndTm> [0..1] DateTime 243
6.4.6.11.4.9.3.1  SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp>
Presence: [1..1]
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 232 March 2026
```

