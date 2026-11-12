---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.2 ReferredDocumentAmount <RfrdDocAmt>", "6.4.2.47.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [805]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 805 to 805.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 805

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  805
     Type <Tp> [1..1]  805
{Or       Code <Cd> [1..1] CodeSet 806
Or}       Proprietary <Prtry> [1..1] Text 806
     Amount <Amt> [1..1] Amount C2, C12 806
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  806
     Amount <Amt> [1..1] Amount C2, C12 806
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 807
     Reason <Rsn> [0..1] Text 807
     AdditionalInformation <AddtlInf> [0..1] Text 807
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
6.4.2.47.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  805
{Or     Code <Cd> [1..1] CodeSet 806
Or}     Proprietary <Prtry> [1..1] Text 806
   Amount <Amt> [1..1] Amount C2, C12 806
6.4.2.47.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 806
Or}   Proprietary <Prtry> [1..1] Text 806
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
805 March 2026
```

