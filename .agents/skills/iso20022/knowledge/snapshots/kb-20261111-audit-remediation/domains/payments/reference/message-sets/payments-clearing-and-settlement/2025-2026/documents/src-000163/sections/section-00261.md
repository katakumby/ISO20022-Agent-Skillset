---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.10 MandateRelatedInformation <MndtRltdInf>", "4.4.3.27.10.1 DirectDebitMandate <DrctDbtMndt>"]
file_pages: [378, 379]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.10.1 DirectDebitMandate <DrctDbtMndt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 378 to 379.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 378

```text
4.4.3.27.10.1  DirectDebitMandate <DrctDbtMndt>
Presence: [1..1]
Definition: Specific direct debit mandate data.
Impacted by: C3 "AmendmentIndicatorFalseRule", C4 "AmendmentIndicatorTrueRule"
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
378 March 2026
```

## File page 379

```text
DirectDebitMandate <DrctDbtMndt> contains the following MandateRelatedInformation16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 380
   DateOfSignature <DtOfSgntr> [0..1] Date 380
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 380
   AmendmentInformationDetails <AmdmntInfDtls> [0..1]  380
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
{Or       Code <Cd> [1..1] CodeSet 388
Or}       Proprietary <Prtry> [1..1] Text 388
     OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 389
   ElectronicSignature <ElctrncSgntr> [0..1] Text 389
   FirstCollectionDate <FrstColltnDt> [0..1] Date 389
   FinalCollectionDate <FnlColltnDt> [0..1] Date 389
   Frequency <Frqcy> [0..1] ± 389
   Reason <Rsn> [0..1]  389
{Or     Code <Cd> [1..1] CodeSet 390
Or}     Proprietary <Prtry> [1..1] Text 390
   TrackingDays <TrckgDays> [0..1] Text 390
Constraints
• AmendmentIndicatorFalseRule
If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
379 March 2026
```

