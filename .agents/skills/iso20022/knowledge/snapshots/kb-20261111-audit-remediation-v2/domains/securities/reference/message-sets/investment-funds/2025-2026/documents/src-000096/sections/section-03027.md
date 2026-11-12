---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "58.3 Constraints"]
file_pages: [4235]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.018.001.05"]
topic_continuations: [{"constraint_ids": ["C3", "C4", "C5", "C6", "C7", "C8", "C9"], "until_heading": "58.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 4236, "topic": "58.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-03028.md"}]
---

# 58.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4235 to 4235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

The 58.3 Constraints topic continues in [Constraints continuation C3–C9 (file p4236)](section-03028.md#file-page-4236). Read the text before **58.4 Message Building Blocks** on that page to include the remaining conditions and qualifications. The file-page range above describes this file only.
<!-- PDF-TOPIC-NAV-END -->

## File page 4235

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 4248
Or           CTA <CTA> [1..1] IdentifierSet 4248
Or           QUICK <QUICK> [1..1] IdentifierSet 4248
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 4249
Or           Dutch <Dtch> [1..1] IdentifierSet 4249
Or           Valoren <Vlrn> [1..1] IdentifierSet 4249
Or           Sicovam <SCVM> [1..1] IdentifierSet 4249
Or           Belgian <Belgn> [1..1] IdentifierSet 4249
Or           Common <Cmon> [1..1] IdentifierSet 4249
Or           DTI <DTI> [1..1] IdentifierSet 4249
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  4249
             Identification <Id> [1..1] Text 4250
             IdentificationSource <IdSrc> [1..1] ± 4250
         Name <Nm> [0..1] Text 4250
         ShortName <ShrtNm> [0..1] Text 4250
         SupplementaryIdentification <SplmtryId> [0..1] Text 4250
         ClassType <ClssTp> [0..1] Text 4250
         SecuritiesForm <SctiesForm> [0..1] CodeSet 4251
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4251
         ProductGroup <PdctGrp> [0..1] Text 4251
         SeriesIdentification <SrsId> [0..1]  C9 4251
           SeriesDate <SrsDt> [0..1] ± 4252
           SeriesName <SrsNm> [0..1] Text 4252
   Extension <Xtnsn> [0..*] ± C3 0
58.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4235 May 2026
```

