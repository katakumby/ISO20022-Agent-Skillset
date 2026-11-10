---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.1 ReferredDocumentInformation <RfrdDocInf>", "6.4.2.47.2.1.4 LineDetails <LineDtls>"]
file_pages: [799]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.1.4 LineDetails <LineDtls>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 799 to 799.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 799

```text
6.4.2.47.2.1.4  LineDetails <LineDtls>
Presence: [0..*]
Definition: Set of elements used to provide the content of the referred document line.
LineDetails <LineDtls> contains the following DocumentLineInformation2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..*]  799
     Type <Tp> [0..1]  800
       CodeOrProprietary <CdOrPrtry> [1..1]  800
{Or         Code <Cd> [1..1] CodeSet 800
Or}         Proprietary <Prtry> [1..1] Text 800
       Issuer <Issr> [0..1] Text 801
     Number <Nb> [0..1] Text 801
     RelatedDate <RltdDt> [0..1] Date 801
   Description <Desc> [0..1] Text 801
   Amount <Amt> [0..1]  C39 801
     RemittanceAmountAndType <RmtAmtAndTp> [0..*]  802
       Type <Tp> [1..1]  802
{Or         Code <Cd> [1..1] CodeSet 803
Or}         Proprietary <Prtry> [1..1] Text 803
       Amount <Amt> [1..1] Amount C2, C12 803
     AdjustmentAmountAndReason
<AdjstmntAmtAndRsn>
[0..*]  803
       Amount <Amt> [1..1] Amount C2, C12 803
       CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 804
       Reason <Rsn> [0..1] Text 804
       AdditionalInformation <AddtlInf> [0..1] Text 804
6.4.2.47.2.1.4.1  Identification <Id>
Presence: [1..*]
Definition: Provides identification of the document line.
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
799 March 2026
```

