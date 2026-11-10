---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.15 RemittanceInformation <RmtInf>", "2.4.2.15.18.2.15.2 Structured <Strd>", "2.4.2.15.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>", "2.4.2.15.18.2.15.2.1.4 LineDetails <LineDtls>", "2.4.2.15.18.2.15.2.1.4.3 Amount <Amt>", "2.4.2.15.18.2.15.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.15.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 181 to 181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 181

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  181
     Type <Tp> [1..1]  181
{Or       Code <Cd> [1..1] CodeSet 182
Or}       Proprietary <Prtry> [1..1] Text 182
     Amount <Amt> [1..1] Amount C2, C6 182
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  182
     Amount <Amt> [1..1] Amount C2, C6 182
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 183
     Reason <Rsn> [0..1] Text 183
     AdditionalInformation <AddtlInf> [0..1] Text 183
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
2.4.2.15.18.2.15.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  181
{Or     Code <Cd> [1..1] CodeSet 182
Or}     Proprietary <Prtry> [1..1] Text 182
   Amount <Amt> [1..1] Amount C2, C6 182
2.4.2.15.18.2.15.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 182
Or}   Proprietary <Prtry> [1..1] Text 182
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
181 March 2026
```

