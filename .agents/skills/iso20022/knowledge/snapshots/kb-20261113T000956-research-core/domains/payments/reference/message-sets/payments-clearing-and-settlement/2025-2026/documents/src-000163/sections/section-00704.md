---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.2 ReferredDocumentAmount <RfrdDocAmt>", "7.4.2.40.30.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [959]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 959 to 959.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 959

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  959
     Type <Tp> [1..1]  959
{Or       Code <Cd> [1..1] CodeSet 960
Or}       Proprietary <Prtry> [1..1] Text 960
     Amount <Amt> [1..1] Amount C2, C9 960
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  960
     Amount <Amt> [1..1] Amount C2, C9 960
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 961
     Reason <Rsn> [0..1] Text 961
     AdditionalInformation <AddtlInf> [0..1] Text 961
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
7.4.2.40.30.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  959
{Or     Code <Cd> [1..1] CodeSet 960
Or}     Proprietary <Prtry> [1..1] Text 960
   Amount <Amt> [1..1] Amount C2, C9 960
7.4.2.40.30.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 960
Or}   Proprietary <Prtry> [1..1] Text 960
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
959 March 2026
```

