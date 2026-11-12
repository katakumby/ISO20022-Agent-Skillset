---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.11 RemittanceInformation <RmtInf>", "9.4.3.11.11.2 Structured <Strd>", "9.4.3.11.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "9.4.3.11.11.2.1.4 LineDetails <LineDtls>", "9.4.3.11.11.2.1.4.3 Amount <Amt>", "9.4.3.11.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>"]
file_pages: [1119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.11.2.1.4.3.1 RemittanceAmountAndType <RmtAmtAndTp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1119 to 1119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1119

```text
Amount <Amt> contains the following RemittanceAmount4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemittanceAmountAndType <RmtAmtAndTp> [0..*]  1119
     Type <Tp> [1..1]  1119
{Or       Code <Cd> [1..1] CodeSet 1120
Or}       Proprietary <Prtry> [1..1] Text 1120
     Amount <Amt> [1..1] Amount C2, C8 1120
   AdjustmentAmountAndReason <AdjstmntAmtAndRsn> [0..*]  1120
     Amount <Amt> [1..1] Amount C2, C8 1120
     CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 1121
     Reason <Rsn> [0..1] Text 1121
     AdditionalInformation <AddtlInf> [0..1] Text 1121
Constraints
• RemittanceAmountAndTypeGuideline
If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType,
RemittanceAmountAndType must not be repeated.
9.4.3.11.11.2.1.4.3.1  RemittanceAmountAndType <RmtAmtAndTp>
Presence: [0..*]
Definition: Type and amount of money for the referred document.
RemittanceAmountAndType <RmtAmtAndTp> contains the following DocumentAmount1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1119
{Or     Code <Cd> [1..1] CodeSet 1120
Or}     Proprietary <Prtry> [1..1] Text 1120
   Amount <Amt> [1..1] Amount C2, C8 1120
9.4.3.11.11.2.1.4.3.1.1  Type <Tp>
Presence: [1..1]
Definition: Defines the type of amount.
Type <Tp> contains one of the following DocumentAmountType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1120
Or}   Proprietary <Prtry> [1..1] Text 1120
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1119 March 2026
```

