---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.1 ReferredDocumentInformation <RfrdDocInf>", "3.4.2.35.2.1.4 LineDetails <LineDtls>", "3.4.2.35.2.1.4.3 Amount <Amt>", "3.4.2.35.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 218 to 218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 218

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  218
     Type <Tp> [1..1]  218
{Or       Code <Cd> [1..1] CodeSet 219
Or}       Proprietary <Prtry> [1..1] Text 219
     Amount <Amt> [1..1] Amount C2, C11 219
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  219
     Amount <Amt> [1..1] Amount C2, C11 219
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 220
     Reason <Rsn> [0..1] Text 220
     AdditionalInformation <AddtlInf> [0..1] Text 220
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
3.4.2.35.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  218
{Or     Code <Cd> [1..1] CodeSet 219
Or}     Proprietary <Prtry> [1..1] Text 219
   Amount <Amt> [1..1] Amount C2, C11 219
3.4.2.35.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 219
Or}   Proprietary <Prtry> [1..1] Text 219
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
218 March 2026
```

