---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.8 CalculationData <ClctnData>", "6.4.6.11.4.8.6 SubAmountPenaltyBreakdown <SubAmtPnltyBrkdwn>", "6.4.6.11.4.8.6.2 Type <Tp>"]
file_pages: [228, 229]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.8.6.2 Type <Tp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 228 to 229.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 228

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.4.6.11.4.8.6.2  Type <Tp>
Presence: [0..1]
Definition: Amount type for the penalty breakdown.
Datatype: "PenaltyAmountType1Code" on page 517
CodeName Name Definition
CASH Cash Penalty is based on the amount of cash
failed to be delivered and the penalty
rate is the discount rate of the relevant
currency.
SECU Securities Penalty is based on the quantity of
securities failed to be delivered and
penalty rate of the securities.
6.4.6.11.4.9  RelatedTransaction <RltdTx>
Presence: [0..1]
Definition: Transaction for which the penalties apply.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 228 March 2026
```

## File page 229

```text
RelatedTransaction <RltdTx> contains the following PenaltyTransaction3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] ± C12 230
   ReferenceOwner <RefOwnr> [0..1] ± 230
   TransactionDetails <TxDtls> [0..1]  231
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
{Or       NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 237
Or}       Reason <Rsn> [1..*]  237
         Code <Cd> [1..1]  238
{Or           Code <Cd> [1..1] CodeSet 238
Or}           Proprietary <Prtry> [1..1] ± 241
         AdditionalReasonInformation <AddtlRsnInf> [0..1] Text 242
     BusinessDayEvent <BizDayEvt> [0..1]  242
       Type <Tp> [1..1]  242
{Or         Code <Cd> [1..1] CodeSet 242
Or}         Proprietary <Prtry> [1..1] ± 243
       ScheduledTime <SchdldTm> [1..1] DateTime 243
       EffectiveTime <FctvTm> [0..1] DateTime 243
       StartTime <StartTm> [0..1] DateTime 243
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 229 March 2026
```

