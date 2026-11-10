---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "65.3 Constraints"]
file_pages: [4305]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.058.001.03"]
---

# 65.3 Constraints

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4305 to 4305.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4305

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 4318
Or           CTA <CTA> [1..1] IdentifierSet 4318
Or           QUICK <QUICK> [1..1] IdentifierSet 4318
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 4319
Or           Dutch <Dtch> [1..1] IdentifierSet 4319
Or           Valoren <Vlrn> [1..1] IdentifierSet 4319
Or           Sicovam <SCVM> [1..1] IdentifierSet 4319
Or           Belgian <Belgn> [1..1] IdentifierSet 4319
Or           Common <Cmon> [1..1] IdentifierSet 4319
Or           DTI <DTI> [1..1] IdentifierSet 4319
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  4319
             Identification <Id> [1..1] Text 4320
             IdentificationSource <IdSrc> [1..1] ± 4320
         Name <Nm> [0..1] Text 4320
         ShortName <ShrtNm> [0..1] Text 4320
         SupplementaryIdentification <SplmtryId> [0..1] Text 4320
         ClassType <ClssTp> [0..1] Text 4320
         SecuritiesForm <SctiesForm> [0..1] CodeSet 4321
         DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4321
         ProductGroup <PdctGrp> [0..1] Text 4321
         SeriesIdentification <SrsId> [0..1]  C9 4321
           SeriesDate <SrsDt> [0..1] ± 4322
           SeriesName <SrsNm> [0..1] Text 4322
   Extension <Xtnsn> [0..*] ± C3 0
65.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4305 May 2026
```

