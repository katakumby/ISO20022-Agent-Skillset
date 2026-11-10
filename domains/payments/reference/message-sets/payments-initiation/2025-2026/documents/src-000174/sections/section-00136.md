---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.10 MandateRelatedInformation <MndtRltdInf>", "3.4.3.7.12.10.1 DirectDebitMandate <DrctDbtMndt>", "3.4.3.7.12.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "3.4.3.7.12.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>"]
file_pages: [205]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 205 to 205.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 205

```text
AmendmentInformationDetails <AmdmntInfDtls> contains the following
AmendmentInformationDetails15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 205
   OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 205
   OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 206
   OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C16,
C15
207
   OriginalDebtor <OrgnlDbtr> [0..1] ± 208
   OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C16,
C15
209
   OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 210
   OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C16,
C15
211
   OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 212
   OriginalFrequency <OrgnlFrqcy> [0..1] ± 212
   OriginalReason <OrgnlRsn> [0..1]  212
{Or     Code <Cd> [1..1] CodeSet 212
Or}     Proprietary <Prtry> [1..1] Text 212
   OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 213
3.4.3.7.12.10.1.4.1  OriginalMandateIdentification <OrgnlMndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the original
mandate.
Datatype: "Max35Text" on page 609
3.4.3.7.12.10.1.4.2  OriginalCreditorSchemeIdentification <OrgnlCdtrSchmeId>
Presence: [0..1]
Definition: Original creditor scheme identification that has been modified.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 205 March 2026
```

