---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.11 RemittanceInformation <RmtInf>", "9.4.3.11.11.2 Structured <Strd>", "9.4.3.11.11.2.1 ReferredDocumentInformation <RfrdDocInf>", "9.4.3.11.11.2.1.4 LineDetails <LineDtls>", "9.4.3.11.11.2.1.4.1 Identification <Id>", "9.4.3.11.11.2.1.4.1.1 Type <Tp>", "9.4.3.11.11.2.1.4.1.1.2 Issuer <Issr>"]
file_pages: [1118]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.11.2.1.4.1.1.2 Issuer <Issr>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1118 to 1118.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1118

```text
Definition: Proprietary identification of the type of the remittance document.
Datatype: "Max35Text" on page 1246
9.4.3.11.11.2.1.4.1.1.2  Issuer <Issr>
Presence: [0..1]
Definition: Identification of the issuer of the reference document line identificationtype.
Datatype: "Max35Text" on page 1246
9.4.3.11.11.2.1.4.1.2  Number <Nb>
Presence: [0..1]
Definition: Identification of the type specified for the referred document line.
Datatype: "Max35Text" on page 1246
9.4.3.11.11.2.1.4.1.3  RelatedDate <RltdDt>
Presence: [0..1]
Definition: Date associated with the referred document line.
Datatype: "ISODate" on page 1239
9.4.3.11.11.2.1.4.2  Description <Desc>
Presence: [0..1]
Definition: Description associated with the document line.
Datatype: "Max2048Text" on page 1245
9.4.3.11.11.2.1.4.3  Amount <Amt>
Presence: [0..1]
Definition: Provides details on the amounts of the document line.
Impacted by: C18 "RemittanceAmountAndTypeGuideline"
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1118 March 2026
```

