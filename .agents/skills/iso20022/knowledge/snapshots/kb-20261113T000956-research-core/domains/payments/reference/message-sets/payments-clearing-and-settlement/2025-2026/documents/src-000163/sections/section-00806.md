---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.10 MandateRelatedInformation <MndtRltdInf>", "9.4.3.11.10.1 DirectDebitMandate <DrctDbtMndt>"]
file_pages: [1091, 1092]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.10.1 DirectDebitMandate <DrctDbtMndt>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1091 to 1092.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1091

```text
9.4.3.11.10.1  DirectDebitMandate <DrctDbtMndt>
Presence: [1..1]
Definition: Specific direct debit mandate data.
Impacted by: C3 "AmendmentIndicatorFalseRule", C4 "AmendmentIndicatorTrueRule"
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1091 March 2026
```

## File page 1092

```text
DirectDebitMandate <DrctDbtMndt> contains the following MandateRelatedInformation16 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MandateIdentification <MndtId> [0..1] Text 1093
   DateOfSignature <DtOfSgntr> [0..1] Date 1093
   AmendmentIndicator <AmdmntInd> [0..1] Indicator 1093
   AmendmentInformationDetails <AmdmntInfDtls> [0..1]  1093
     OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 1094
     OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 1094
     OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 1095
     OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C12,
C11
1096
     OriginalDebtor <OrgnlDbtr> [0..1] ± 1097
     OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C12,
C11
1098
     OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 1099
     OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C12,
C11
1100
     OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 1101
     OriginalFrequency <OrgnlFrqcy> [0..1] ± 1101
     OriginalReason <OrgnlRsn> [0..1]  1101
{Or       Code <Cd> [1..1] CodeSet 1101
Or}       Proprietary <Prtry> [1..1] Text 1101
     OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 1102
   ElectronicSignature <ElctrncSgntr> [0..1] Text 1102
   FirstCollectionDate <FrstColltnDt> [0..1] Date 1102
   FinalCollectionDate <FnlColltnDt> [0..1] Date 1102
   Frequency <Frqcy> [0..1] ± 1102
   Reason <Rsn> [0..1]  1102
{Or     Code <Cd> [1..1] CodeSet 1103
Or}     Proprietary <Prtry> [1..1] Text 1103
   TrackingDays <TrckgDays> [0..1] Text 1103
Constraints
• AmendmentIndicatorFalseRule
If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1092 March 2026
```

