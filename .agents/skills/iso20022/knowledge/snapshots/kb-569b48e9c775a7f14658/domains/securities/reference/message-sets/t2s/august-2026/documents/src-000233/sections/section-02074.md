---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.9 RelatedTransaction <RltdTx>", "81.4.6.11.4.9.4 NetMovementDetails <NetMvmntDtls>", "81.4.6.11.4.9.4.1 SafekeepingAccount <SfkpgAcct>"]
file_pages: [2826]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.9.4.1 SafekeepingAccount <SfkpgAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2826 to 2826.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2826

```text
NetMovementDetails <NetMvmntDtls> contains the following PenaltyNetMovementRecord1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [0..1] ± 2826
   SecuritiesShortfall <SctiesShrtfll> [0..1] ± 2826
   ShortfallValuation <ShrtfllValtn> [0..1] ± 2826
   TradeTransactionCondition <TradTxCond> [0..*] ± 2827
   NumberOfEntries <NbOfNtries> [0..1] Quantity 2827
81.4.6.11.4.9.4.1  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
81.4.6.11.4.9.4.2  SecuritiesShortfall <SctiesShrtfll>
Presence: [0..1]
Definition: Total quantity of securities which failed to settle.
SecuritiesShortfall <SctiesShrtfll> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
81.4.6.11.4.9.4.3  ShortfallValuation <ShrtfllValtn>
Presence: [0..1]
Definition: Valuation of securities which failed to settle.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2826 August 2026
```

