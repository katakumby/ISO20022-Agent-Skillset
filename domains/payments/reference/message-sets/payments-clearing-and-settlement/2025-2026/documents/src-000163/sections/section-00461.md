---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.10 MandateRelatedInformation <MndtRltdInf>", "5.4.3.21.10.1 DirectDebitMandate <DrctDbtMndt>", "5.4.3.21.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "5.4.3.21.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>"]
file_pages: [635]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 635 to 635.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 635

```text
AmendmentInformationDetails <AmdmntInfDtls> contains the following
AmendmentInformationDetails15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 635
   OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 635
   OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 636
   OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C20,
C19
637
   OriginalDebtor <OrgnlDbtr> [0..1] ± 638
   OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C20,
C19
639
   OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 640
   OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C20,
C19
641
   OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 642
   OriginalFrequency <OrgnlFrqcy> [0..1] ± 642
   OriginalReason <OrgnlRsn> [0..1]  642
{Or     Code <Cd> [1..1] CodeSet 642
Or}     Proprietary <Prtry> [1..1] Text 642
   OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 643
5.4.3.21.10.1.4.1  OriginalMandateIdentification <OrgnlMndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the original
mandate.
Datatype: "Max35Text" on page 1246
5.4.3.21.10.1.4.2  OriginalCreditorSchemeIdentification <OrgnlCdtrSchmeId>
Presence: [0..1]
Definition: Original creditor scheme identification that has been modified.
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
635 March 2026
```

