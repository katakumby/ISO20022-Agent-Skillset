---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.9 RelatedTransaction <RltdTx>", "6.4.6.11.4.9.4 NetMovementDetails <NetMvmntDtls>", "6.4.6.11.4.9.4.1 SafekeepingAccount <SfkpgAcct>"]
file_pages: [244]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.9.4.1 SafekeepingAccount <SfkpgAcct>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 244 to 244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 244

```text
NetMovementDetails <NetMvmntDtls> contains the following PenaltyNetMovementRecord1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [0..1] ± 244
   SecuritiesShortfall <SctiesShrtfll> [0..1] ± 244
   ShortfallValuation <ShrtfllValtn> [0..1] ± 244
   TradeTransactionCondition <TradTxCond> [0..*] ± 245
   NumberOfEntries <NbOfNtries> [0..1] Quantity 245
6.4.6.11.4.9.4.1  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 246
   Type <Tp> [0..1] ± 246
   Name <Nm> [0..1] Text 246
6.4.6.11.4.9.4.2  SecuritiesShortfall <SctiesShrtfll>
Presence: [0..1]
Definition: Total quantity of securities which failed to settle.
SecuritiesShortfall <SctiesShrtfll> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 342 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 342
Or   FaceAmount <FaceAmt> [1..1] Amount 342
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 342
6.4.6.11.4.9.4.3  ShortfallValuation <ShrtfllValtn>
Presence: [0..1]
Definition: Valuation of securities which failed to settle.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 244 March 2026
```

