---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.10 MandateRelatedInformation <MndtRltdInf>", "9.4.3.11.10.1 DirectDebitMandate <DrctDbtMndt>", "9.4.3.11.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "9.4.3.11.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>"]
file_pages: [1094]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.10.1.4.1 OriginalMandateIdentification <OrgnlMndtId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1094 to 1094.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1094

```text
AmendmentInformationDetails <AmdmntInfDtls> contains the following
AmendmentInformationDetails15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
{Or     Code <Cd> [1..1] CodeSet 1101
Or}     Proprietary <Prtry> [1..1] Text 1101
   OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 1102
9.4.3.11.10.1.4.1  OriginalMandateIdentification <OrgnlMndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the original
mandate.
Datatype: "Max35Text" on page 1246
9.4.3.11.10.1.4.2  OriginalCreditorSchemeIdentification <OrgnlCdtrSchmeId>
Presence: [0..1]
Definition: Original creditor scheme identification that has been modified.
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1094 March 2026
```

