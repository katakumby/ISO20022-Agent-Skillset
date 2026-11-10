---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.3 Constraints"]
file_pages: [4286]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.3 Constraints

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4286 to 4286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4286

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 4298
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 4298
Or         CTA <CTA> [1..1] IdentifierSet 4298
Or         QUICK <QUICK> [1..1] IdentifierSet 4298
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 4299
Or         Dutch <Dtch> [1..1] IdentifierSet 4299
Or         Valoren <Vlrn> [1..1] IdentifierSet 4299
Or         Sicovam <SCVM> [1..1] IdentifierSet 4299
Or         Belgian <Belgn> [1..1] IdentifierSet 4299
Or         Common <Cmon> [1..1] IdentifierSet 4299
Or         DTI <DTI> [1..1] IdentifierSet 4299
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  4299
           Identification <Id> [1..1] Text 4300
           IdentificationSource <IdSrc> [1..1] ± 4300
       Name <Nm> [0..1] Text 4300
       ShortName <ShrtNm> [0..1] Text 4300
       SupplementaryIdentification <SplmtryId> [0..1] Text 4300
       ClassType <ClssTp> [0..1] Text 4300
       SecuritiesForm <SctiesForm> [0..1] CodeSet 4301
       DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4301
       ProductGroup <PdctGrp> [0..1] Text 4301
       SeriesIdentification <SrsId> [0..1]  C9 4301
         SeriesDate <SrsDt> [0..1] ± 4302
         SeriesName <SrsNm> [0..1] Text 4302
   Extension <Xtnsn> [0..*] ± C3 0
64.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4286 May 2026
```

