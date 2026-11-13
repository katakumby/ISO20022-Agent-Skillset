---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.8 SubAccountDetails <SubAcctDtls>", "8.4.8.5 FinancialInstrumentDetails <FinInstrmDtls>", "8.4.8.5.7 Transaction <Tx>", "8.4.8.5.7.19 TransactionDetails <TxDtls>", "8.4.8.5.7.19.22 ReversalIndicator <RvslInd>"]
file_pages: [272]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.8.5.7.19.22 ReversalIndicator <RvslInd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 272 to 272.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 272

```text
8.4.8.5.7.19.22  ReversalIndicator <RvslInd>
Presence: [0..1]
Definition: Indicates whether it is the reversal of a previously reported movement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
8.4.8.5.7.19.23  TransactionAdditionalDetails <TxAddtlDtls>
Presence: [0..1]
Definition: Provides additional details on the transaction which cannot be included within the structured
fields of the message.
Datatype: "Max350Text" on page 2192
8.4.8.5.7.20  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C42 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1564 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1565
   Envelope <Envlp> [1..1] (External Schema) 1565
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 272 March 2026
```

