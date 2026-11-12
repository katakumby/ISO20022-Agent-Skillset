---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.40 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "7.4.2.40.30 RemittanceInformation <RmtInf>", "7.4.2.40.30.2 Structured <Strd>", "7.4.2.40.30.2.1 ReferredDocumentInformation <RfrdDocInf>", "7.4.2.40.30.2.1.4 LineDetails <LineDtls>"]
file_pages: [953]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.40.30.2.1.4 LineDetails <LineDtls>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 953 to 953.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 953

```text
7.4.2.40.30.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  953
     Type <Tp> [0..1]  954
       CodeOrProprietary <CdOrPrtry> [1..1]  954
{Or         Code <Cd> [1..1] CodeSet 954
Or}         Proprietary <Prtry> [1..1] Text 954
       Issuer <Issr> [0..1] Text 955
     Number <Nb> [0..1] Text 955
     RelatedDate <RltdDt> [0..1] Date 955
   Description <Desc> [0..1] Text 955
   Amount <Amt> [0..1]  C57 955
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  956
       Type <Tp> [1..1]  956
{Or         Code <Cd> [1..1] CodeSet 957
Or}         Proprietary <Prtry> [1..1] Text 957
       Amount <Amt> [1..1] Amount C2, C9 957
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  957
       Amount <Amt> [1..1] Amount C2, C9 957
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 958
       Reason <Rsn> [0..1] Text 958
       AdditionalInformation <AddtlInf> [0..1] Text 958
7.4.2.40.30.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
953 March 2026
```

