---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.18 OriginalTransactionReference <OrgnlTxRef>", "2.4.3.18.10 MandateRelatedInformation <MndtRltdInf>", "2.4.3.18.10.1 DirectDebitMandate <DrctDbtMndt>", "2.4.3.18.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "2.4.3.18.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>"]
file_pages: [65]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.18.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 65 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 65

```text
AmendmentInformationDetails <AmdmntInfDtls> contains the following
AmendmentInformationDetails15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 65
   OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 65
   OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 66
   OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C16,
C15
67
   OriginalDebtor <OrgnlDbtr> [0..1] ± 68
   OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
69
   OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 70
   OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
71
   OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 72
   OriginalFrequency <OrgnlFrqcy> [0..1] ± 72
   OriginalReason <OrgnlRsn> [0..1]  72
{Or     Code <Cd> [1..1] CodeSet 72
Or}     Proprietary <Prtry> [1..1] Text 72
   OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 73
2.4.3.18.10.1.4.1  OriginalMandateIdentification <OrgnlMndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the original
mandate.
Datatype: "Max35Text" on page 1246
2.4.3.18.10.1.4.2  OriginalCreditorSchemeIdentification <OrgnlCdtrSchmeId>
Presence: [0..1]
Definition: Original creditor scheme identification that has been modified.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
65 March 2026
```

