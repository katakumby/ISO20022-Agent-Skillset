---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.10 MandateRelatedInformation <MndtRltdInf>", "4.4.3.8.9.10.1 DirectDebitMandate <DrctDbtMndt>"]
file_pages: [333, 334]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.10.1 DirectDebitMandate <DrctDbtMndt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 333 to 334.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 333

```text
4.4.3.8.9.10.1  DirectDebitMandate <DrctDbtMndt>
Presence: [1..1]
Definition: Specific direct debit mandate data.
Impacted by: C3 "AmendmentIndicatorFalseRule", C4 "AmendmentIndicatorTrueRule"
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 333 March 2026
```

## File page 334

```text
DirectDebitMandate <DrctDbtMndt> contains the following MandateRelatedInformation16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 335
   DateOfSignature <DtOfSgntr> [0..1] Date 335
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 335
   AmendmentInformationDetails <AmdmntInfDtls> [0..1]  335
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
{Or       Code <Cd> [1..1] CodeSet 343
Or}       Proprietary <Prtry> [1..1] Text 343
     OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 344
   ElectronicSignature <ElctrncSgntr> [0..1] Text 344
   FirstCollectionDate <FrstColltnDt> [0..1] Date 344
   FinalCollectionDate <FnlColltnDt> [0..1] Date 344
   Frequency <Frqcy> [0..1] ± 344
   Reason <Rsn> [0..1]  344
{Or     Code <Cd> [1..1] CodeSet 345
Or}     Proprietary <Prtry> [1..1] Text 345
   TrackingDays <TrckgDays> [0..1] Text 345
Constraints
• AmendmentIndicatorFalseRule
If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 334 March 2026
```

