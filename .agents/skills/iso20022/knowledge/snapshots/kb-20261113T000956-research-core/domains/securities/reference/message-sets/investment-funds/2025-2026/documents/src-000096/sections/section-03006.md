---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.3 Constraints"]
file_pages: [4209]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
topic_continuations: [{"constraint_ids": ["C8", "C9"], "until_heading": "57.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 4210, "topic": "57.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03007.md"}]
---

# 57.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4209 to 4209.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 57.3 Constraints topic continues in [Constraints continuation C8–C9 (file p4210)](section-03007.md#file-page-4210). Read the text before **57.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 4209

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
         SecuritiesForm <SctiesForm> [0..1] CodeSet 4230
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4230
         ProductGroup <PdctGrp> [0..1] Text 4230
         SeriesIdentification <SrsId> [0..1]  C9 4230
           SeriesDate <SrsDt> [0..1] ± 4231
           SeriesName <SrsNm> [0..1] Text 4231
   Extension <Xtnsn> [0..*] ± C3 0
57.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C4 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C5 MessageNameAndReferenceGuideline
If Reference/RelatedReference/MessageName or Reference/OtherReference/MessageName is
present, it must it must contain 502 or must start with setr.002, setr.005, setr.008, setr.011,
setr.014 or setr.018 and Reference/RelatedReference/Reference must contain the message
reference of a message in this list.
This constraint is defined at the MessageDefinition level.
C6 OrderOriginatorEligibility2Rule
OrderOriginatorEligibility may only be present if one or more of the parties identified in
OwnerIdentification is/are the originator of the order.
C7 OtherReferenceGuideline
OtherReference should be used to reference an order cancellation 'message' sent in a
proprietary way or used for a system reference. If OtherReference is present, OtherReference/
MessageName must contain 'fax' or 'phone' or 'email', etc.
This constraint is defined at the MessageDefinition level.
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4209 May 2026
```

