---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.5 DirectDebitTransaction <DrctDbtTx>", "5.4.2.18.5.1 MandateRelatedInformation <MndtRltdInf>", "5.4.2.18.5.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "5.4.2.18.5.1.4.1 OriginalMandateIdentification <OrgnlMndtId>"]
file_pages: [451]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.5.1.4.1 OriginalMandateIdentification <OrgnlMndtId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 451 to 451.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 451

```text
AmendmentInformationDetails <AmdmntInfDtls> contains the following
AmendmentInformationDetails15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 451
   OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 451
   OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 452
   OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C16,
C15
453
   OriginalDebtor <OrgnlDbtr> [0..1] ± 454
   OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
455
   OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 456
   OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
457
   OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 458
   OriginalFrequency <OrgnlFrqcy> [0..1] ± 458
   OriginalReason <OrgnlRsn> [0..1]  458
{Or     Code <Cd> [1..1] CodeSet 458
Or}     Proprietary <Prtry> [1..1] Text 458
   OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 459
5.4.2.18.5.1.4.1  OriginalMandateIdentification <OrgnlMndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the original
mandate.
Datatype: "Max35Text" on page 609
5.4.2.18.5.1.4.2  OriginalCreditorSchemeIdentification <OrgnlCdtrSchmeId>
Presence: [0..1]
Definition: Original creditor scheme identification that has been modified.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 451 March 2026
```

