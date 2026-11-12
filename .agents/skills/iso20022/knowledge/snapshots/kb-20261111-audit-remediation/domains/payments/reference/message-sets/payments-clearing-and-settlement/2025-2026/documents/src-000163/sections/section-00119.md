---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.12 DirectDebitTransaction <DrctDbtTx>", "3.4.2.12.1 MandateRelatedInformation <MndtRltdInf>", "3.4.2.12.1.4 AmendmentInformationDetails <AmdmntInfDtls>", "3.4.2.12.1.4.1 OriginalMandateIdentification <OrgnlMndtId>"]
file_pages: [170]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.12.1.4.1 OriginalMandateIdentification <OrgnlMndtId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 170 to 170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 170

```text
AmendmentInformationDetails <AmdmntInfDtls> contains the following
AmendmentInformationDetails15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OriginalMandateIdentification <OrgnlMndtId> [0..1] Text 170
   OriginalCreditorSchemeIdentification
<OrgnlCdtrSchmeId>
[0..1] ± 170
   OriginalCreditorAgent <OrgnlCdtrAgt> [0..1] ± 171
   OriginalCreditorAgentAccount <OrgnlCdtrAgtAcct> [0..1] ± C15,
C14
172
   OriginalDebtor <OrgnlDbtr> [0..1] ± 173
   OriginalDebtorAccount <OrgnlDbtrAcct> [0..1] ± C15,
C14
174
   OriginalDebtorAgent <OrgnlDbtrAgt> [0..1] ± 175
   OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> [0..1] ± C15,
C14
176
   OriginalFinalCollectionDate <OrgnlFnlColltnDt> [0..1] Date 177
   OriginalFrequency <OrgnlFrqcy> [0..1] ± 177
   OriginalReason <OrgnlRsn> [0..1]  177
{Or     Code <Cd> [1..1] CodeSet 177
Or}     Proprietary <Prtry> [1..1] Text 177
   OriginalTrackingDays <OrgnlTrckgDays> [0..1] Text 178
3.4.2.12.1.4.1  OriginalMandateIdentification <OrgnlMndtId>
Presence: [0..1]
Definition: Unique identification, as assigned by the creditor, to unambiguously identify the original
mandate.
Datatype: "Max35Text" on page 1246
3.4.2.12.1.4.2  OriginalCreditorSchemeIdentification <OrgnlCdtrSchmeId>
Presence: [0..1]
Definition: Original creditor scheme identification that has been modified.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
170 March 2026
```

