---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.15 RemittanceInformation <RmtInf>", "4.4.2.14.18.2.15.2 Structured <Strd>", "4.4.2.14.18.2.15.2.1 ReferredDocumentInformation <RfrdDocInf>", "4.4.2.14.18.2.15.2.1.4 LineDetails <LineDtls>", "4.4.2.14.18.2.15.2.1.4.3 Amount <Amt>", "4.4.2.14.18.2.15.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [699]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.15.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 699 to 699.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 699

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  699
     Type <Tp> [1..1]  699
{Or       Code <Cd> [1..1] CodeSet 700
Or}       Proprietary <Prtry> [1..1] Text 700
     Amount <Amt> [1..1] Amount C2, C6 700
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  700
     Amount <Amt> [1..1] Amount C2, C6 700
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 701
     Reason <Rsn> [0..1] Text 701
     AdditionalInformation <AddtlInf> [0..1] Text 701
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
4.4.2.14.18.2.15.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  699
{Or     Code <Cd> [1..1] CodeSet 700
Or}     Proprietary <Prtry> [1..1] Text 700
   Amount <Amt> [1..1] Amount C2, C6 700
4.4.2.14.18.2.15.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 700
Or}   Proprietary <Prtry> [1..1] Text 700
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
699 March 2026
```

