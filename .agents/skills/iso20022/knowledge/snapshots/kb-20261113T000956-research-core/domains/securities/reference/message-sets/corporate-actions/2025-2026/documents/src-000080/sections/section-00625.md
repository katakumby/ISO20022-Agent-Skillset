---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["15 seev.044.001.13 CorporateActionMovementPreliminaryAdviceCancellationAdviceV13", "15.3 Constraints"]
file_pages: [816]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.044.001.13"]
topic_continuations: [{"constraint_ids": ["C9", "C10", "C11", "C12", "C13", "C14", "C15"], "until_heading": "15.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 817, "topic": "15.3 Constraints", "reference_path": "domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00626.md"}]
---

# 15.3 Constraints

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 816 to 816.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 15.3 Constraints topic continues in [Constraints continuation C9–C15 (file p817)](section-00626.md#file-page-817). Read the text before **15.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 816

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
   PhysicalSecuritiesAgent <PhysSctiesAgt> [0..1] ± 826
   DropAgent <DrpAgt> [0..1] ± 827
   SolicitationAgent <SlctnAgt> [0..*] ± 827
   InformationAgent <InfAgt> [0..1] ± 827
   SupplementaryData <SplmtryData> [0..*] ± C14 828
15.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C4 DescriptionUsageRule
Description must be used alone as the last resort.
C5 EventTypeRule
If Code is present, the code OTHR (Other) must only be used in case no other corporate action
event code is appropriate.
If Code is present, the code CHAN (Change) must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
If Code is present, the code REDM (Final Maturity) must only be used when the redemption is
decided by the issuer and not by the securities holders.
C6 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C7 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C8 OfficialCorporateActionEventReference
The Securities Market Practice Group (SMPG) has published market practice
recommendations on the structure and usage of the Official Corporate Action Event Reference
Approved by the Securities SEG on 27 January 2026 seev.044.001.13
CorporateActionMovementPreliminaryAdviceCancel
lationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 816 February 2026
```

