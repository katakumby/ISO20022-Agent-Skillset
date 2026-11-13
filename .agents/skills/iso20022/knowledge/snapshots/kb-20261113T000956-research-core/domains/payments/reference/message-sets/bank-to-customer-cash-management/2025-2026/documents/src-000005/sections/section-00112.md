---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "2.4.2.15.18.2.15.2 Structured <Strd>", "2.4.2.15.18.2.15.2.2 ReferredDocumentAmount <RfrdDocAmt>", "2.4.2.15.18.2.15.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [184]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.15.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 184 to 184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  184
     Type <Tp> [1..1]  184
{Or       Code <Cd> [1..1] CodeSet 185
Or}       Proprietary <Prtry> [1..1] Text 185
     Amount <Amt> [1..1] Amount C2, C6 185
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  185
     Amount <Amt> [1..1] Amount C2, C6 185
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 186
     Reason <Rsn> [0..1] Text 186
     AdditionalInformation <AddtlInf> [0..1] Text 186
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
2.4.2.15.18.2.15.2.2.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  184
{Or     Code <Cd> [1..1] CodeSet 185
Or}     Proprietary <Prtry> [1..1] Text 185
   Amount <Amt> [1..1] Amount C2, C6 185
2.4.2.15.18.2.15.2.2.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 185
Or}   Proprietary <Prtry> [1..1] Text 185
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
184 March 2026
```

