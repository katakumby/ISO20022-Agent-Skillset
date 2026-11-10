---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.10 MandateRelatedInformation <MndtRltdInf>", "4.4.3.27.10.1 DirectDebitMandate <DrctDbtMndt>", "4.4.3.27.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "4.4.3.27.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
AmendmentInformationDetails <AmdmntInfDtls> contains the following
AmendmentInformationDetails15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 381
   OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 381
   OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 382
   OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C22,
C21
383
   OriginalDebtor <OrgnlDbtr> [0..1] ± 384
   OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C22,
C21
385
   OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 386
   OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C22,
C21
387
   OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 388
   OriginalFrequency <OrgnlFrqcy> [0..1] ± 388
   OriginalReason <OrgnlRsn> [0..1]  388
{Or     Code <Cd> [1..1] CodeSet 388
Or}     Proprietary <Prtry> [1..1] Text 388
   OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 389
4.4.3.27.10.1.4.1  OriginalMandateIdentification <OrgnlMndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the original
mandate.
Datatype: "Max35Text" on page 1246
4.4.3.27.10.1.4.2  OriginalCreditorSchemeIdentification <OrgnlCdtrSchmeId>
Presence: [0..1]
Definition: Original creditor scheme identification that has been modified.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
381 March 2026
```

