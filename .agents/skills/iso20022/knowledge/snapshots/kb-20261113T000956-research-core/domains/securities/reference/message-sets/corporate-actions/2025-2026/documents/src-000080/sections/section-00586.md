---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.3 Constraints"]
file_pages: [761, 762]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
topic_continuations: [{"constraint_ids": ["C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23"], "until_heading": "14.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 763, "topic": "14.3 Constraints", "reference_path": "domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00587.md"}]
---

# 14.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 761 to 762.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 14.3 Constraints topic continues in [Constraints continuation C16–C23 (file p763)](section-00587.md#file-page-763). Read the text before **14.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 761

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         OutForRegistrationBalance <OutForRegnBal> [0..1] ± 808
         SettlementPositionBalance <SttlmPosBal> [0..1] ± 808
         StreetPositionBalance <StrtPosBal> [0..1] ± 808
         TradeDatePositionBalance <TradDtPosBal> [0..1] ± 808
         InTransshipmentBalance <InTrnsShipmntBal> [0..1] ± 809
         RegisteredBalance <RegdBal> [0..1] ± 809
         ObligatedBalance <OblgtdBal> [0..1] ± 809
         PendingDeliveryBalance <PdgDlvryBal> [0..*]  810
           Balance <Bal> [1..1] ± 810
           PendingTransactions <PdgTxs> [0..*] ± 810
         PendingReceiptBalance <PdgRctBal> [0..*]  810
           Balance <Bal> [1..1] ± 811
           PendingTransactions <PdgTxs> [0..*] ± 811
       SupplementaryData <SplmtryData> [0..*] ± C23 811
   SupplementaryData <SplmtryData> [0..*] ± C23 811
14.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C3 AdditionalReasonInforrmationRule
AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
C4 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
C5 AdditionalReasonInforrmationRule
The AdditionalReasonInformation element must not contain information that can be provided in
a structured field unless bilaterally agreed.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 761 February 2026
```

## File page 762

```text
C6 AdditionalReasonInforrmationRule
AdditionalReasonInformation element must not contain information that can be provided in a
structured field unless bilaterally agreed.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 CorporateActionEventAndBalanceRule
If StatementGeneralDetails/ActivityIndicator is 'true' or '1' (Yes) then at least one occurrence of
AccountAndStatementDetails/CorporateActionEventAndBalance must be present.
If StatementGeneralDetails/ActivityIndicator is 'false' or '0' (No) then
AccountAndStatementDetails/CorporateActionEventAndBalance must not be present in any
occurrences of AccountAndStatementDetails.
This constraint is defined at the MessageDefinition level.
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C11 DescriptionUsageRule
Description must be used alone as the last resort.
C12 DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token
identifier.
C13 EventTypeRule
If Code is present, the code OTHR must only be used in case no other corporate action event
code is appropriate.
If Code is present, the code CHAN must only be used in case no other corporate action event
code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM must only be used when the redemption is decided by the
issuer and not by the securities holders.
C14 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C15 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 762 February 2026
```

