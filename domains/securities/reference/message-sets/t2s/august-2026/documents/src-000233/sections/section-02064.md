---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.9 RelatedTransaction <RltdTx>", "81.4.6.11.4.9.3 TransactionDetails <TxDtls>", "81.4.6.11.4.9.3.1 SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp>"]
file_pages: [2814]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.9.3.1 SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2814 to 2814.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2814

```text
TransactionDetails <TxDtls> contains the following PenaltyTransactionRecord2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementTransactionOrCorporateActionEventType
<SttlmTxOrCorpActnEvtTp>
[1..1] ± 2814
   SettlementDate <SttlmDt> [1..1] ± 2815
   CorporateActionRelatedDate <CorpActnRltdDt> [0..1] ± 2815
   SafekeepingAccount <SfkpgAcct> [1..1] ± 2815
   AccountOwner <AcctOwnr> [0..1] ± 2815
   SecuritiesMovementType <SctiesMvmntTp> [1..1] CodeSet 2816
   Payment <Pmt> [1..1] CodeSet 2816
   PostingQuantity <PstngQty> [1..1] ± 2816
   CashAccount <CshAcct> [0..1] ± 2817
   CashAccountOwner <CshAcctOwnr> [0..1] ± 2817
   PostingAmount <PstngAmt> [0..1] ± 2818
   AcknowledgedStatusTimeStamp <AckdStsTmStmp> [0..1] DateTime 2819
   MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 2819
   SettlementStatusFailing <SttlmStsFlng> [0..1]  2819
{Or     NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 2819
Or}     Reason <Rsn> [1..*]  2819
       Code <Cd> [1..1]  2820
{Or         Code <Cd> [1..1] CodeSet 2820
Or}         Proprietary <Prtry> [1..1] ± 2823
       AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 2824
   BusinessDayEvent <BizDayEvt> [0..1]  2824
     Type <Tp> [1..1]  2824
{Or       Code <Cd> [1..1] CodeSet 2824
Or}       Proprietary <Prtry> [1..1] ± 2825
     ScheduledTime <SchdldTm> [1..1] DateTime 2825
     EffectiveTime <FctvTm> [0..1] DateTime 2825
     StartTime <StartTm> [0..1] DateTime 2825
     EndTime <EndTm> [0..1] DateTime 2825
81.4.6.11.4.9.3.1  SettlementTransactionOrCorporateActionEventType <SttlmTxOrCorpActnEvtTp>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2814 August 2026
```

