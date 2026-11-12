---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.9 RelatedTransaction <RltdTx>", "81.4.6.11.4.9.4 NetMovementDetails <NetMvmntDtls>", "81.4.6.11.4.9.4.4 TradeTransactionCondition <TradTxCond>"]
file_pages: [2827]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.9.4.4 TradeTransactionCondition <TradTxCond>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2827 to 2827.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2827

```text
ShortfallValuation <ShrtfllValtn> contains the following elements (see "AmountAndDirection5" on
page 2841 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1, C4 2841
   CreditDebit <CdtDbt> [0..1] CodeSet 2842
81.4.6.11.4.9.4.4  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition5Choice" on page 3206 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3206
Or}   Proprietary <Prtry> [1..1] ± 3207
81.4.6.11.4.9.4.5  NumberOfEntries <NbOfNtries>
Presence: [0..1]
Definition: Number of entries related to the net position.
Datatype: "Number" on page 3324
81.4.7 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C15 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2827 August 2026
```

