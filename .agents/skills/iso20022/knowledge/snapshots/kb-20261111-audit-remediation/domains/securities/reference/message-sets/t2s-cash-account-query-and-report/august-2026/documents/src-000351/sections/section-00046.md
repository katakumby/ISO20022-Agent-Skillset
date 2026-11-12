---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.3 Constraints"]
file_pages: [53]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
topic_continuations: [{"constraint_ids": ["C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 54, "topic": "3.3 Constraints", "reference_path": "domains/securities/reference/message-sets/t2s-cash-account-query-and-report/august-2026/documents/src-000351/sections/section-00047.md"}]
---

# 3.3 Constraints

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 53 to 53.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 3.3 Constraints topic continues in [Constraints continuation C7–C14 (file p54)](section-00047.md#file-page-54). Read the text before **3.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 53

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
       Group <Grp> [0..*]  103
         GroupIdentification <GrpId> [1..1] Text 103
         Party <Pty> [1..*]  103
           Party <Pty> [1..1] ± 103
           Certificate <Cert> [0..1] Binary 104
   DigitalSignature <DgtlSgntr> [0..*]  105
     Party <Pty> [1..1] ± 105
     Signature <Sgntr> [1..1] (External Schema) 106
   SupplementaryData <SplmtryData> [0..*] ± C14 107
3.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C4 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C5 ContractDates1Rule
ContractDates/TargetGoLiveDate and ContractDates/GoLiveDate should not be used as part of
an account closing process.
C6 ContractDates2Rule
ContractDates/ClosingDate should not be used as part of an account opening and maintenance
process.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 53 August 2026
```

