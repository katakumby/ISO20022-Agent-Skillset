---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.17 PendingReceiptBalance <PdgRctBal>", "14.4.3.5.3.17.1 Balance <Bal>"]
file_pages: [811, 812]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.17.1 Balance <Bal>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 811 to 812.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 811

```text
14.4.3.5.3.17.1  Balance <Bal>
Presence: [1..1]
Definition: Signed quantity of balance.
Balance <Bal> contains the following elements (see "SignedQuantityFormat10" on page 1090 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ShortLongPosition <ShrtLngPos> [1..1] CodeSet 1090
   Quantity <Qty> [1..1] ± C13 1090
14.4.3.5.3.17.2  PendingTransactions <PdgTxs>
Presence: [0..*]
Definition: Overall process covering the trade and settlement transactions of financial instruments.
PendingTransactions <PdgTxs> contains the following elements (see
"SettlementTypeAndIdentification25" on page 880 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Payment <Pmt> [1..1] CodeSet 880
   TransactionIdentification <TxId> [1..1] Text 880
   SettlementDate <SttlmDt> [0..1] ± 880
14.4.3.5.4  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Provides additional information related to the event and the balance of the corporate action.
Impacted by: C23 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 924
   Envelope <Envlp> [1..1] (External Schema) 924
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
14.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 811 February 2026
```

## File page 812

```text
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C23 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 924
   Envelope <Envlp> [1..1] (External Schema) 924
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 812 February 2026
```

