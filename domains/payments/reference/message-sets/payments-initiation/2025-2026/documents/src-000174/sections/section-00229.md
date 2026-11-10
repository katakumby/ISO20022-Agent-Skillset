---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.10 MandateRelatedInformation <MndtRltdInf>", "4.4.3.8.9.10.1 DirectDebitMandate <DrctDbtMndt>", "4.4.3.8.9.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "4.4.3.8.9.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>"]
file_pages: [336]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 336 to 336.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 336

```text
AmendmentInformationDetails <AmdmntInfDtls> contains the following
AmendmentInformationDetails15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 336
   OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 336
   OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 337
   OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C18,
C17
338
   OriginalDebtor <OrgnlDbtr> [0..1] ± 339
   OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C18,
C17
340
   OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 341
   OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C18,
C17
342
   OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 343
   OriginalFrequency <OrgnlFrqcy> [0..1] ± 343
   OriginalReason <OrgnlRsn> [0..1]  343
{Or     Code <Cd> [1..1] CodeSet 343
Or}     Proprietary <Prtry> [1..1] Text 343
   OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 344
4.4.3.8.9.10.1.4.1  OriginalMandateIdentification <OrgnlMndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the original
mandate.
Datatype: "Max35Text" on page 609
4.4.3.8.9.10.1.4.2  OriginalCreditorSchemeIdentification <OrgnlCdtrSchmeId>
Presence: [0..1]
Definition: Original creditor scheme identification that has been modified.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 336 March 2026
```

