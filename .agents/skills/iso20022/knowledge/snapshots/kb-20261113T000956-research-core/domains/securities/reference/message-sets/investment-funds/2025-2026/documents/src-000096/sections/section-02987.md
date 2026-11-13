---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.8 LegInformation <LegInf>", "56.4.3.3.8.1 LegIdentification <LegId>"]
file_pages: [4186]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.8.1 LegIdentification <LegId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4186 to 4186.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4186

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       RIC <RIC> [1..1] IdentifierSet 4198
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 4198
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 4198
Or       CTA <CTA> [1..1] IdentifierSet 4198
Or       QUICK <QUICK> [1..1] IdentifierSet 4198
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 4199
Or       Dutch <Dtch> [1..1] IdentifierSet 4199
Or       Valoren <Vlrn> [1..1] IdentifierSet 4199
Or       Sicovam <SCVM> [1..1] IdentifierSet 4199
Or       Belgian <Belgn> [1..1] IdentifierSet 4199
Or       Common <Cmon> [1..1] IdentifierSet 4199
Or       DTI <DTI> [1..1] IdentifierSet 4199
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  4199
         Identification <Id> [1..1] Text 4200
         IdentificationSource <IdSrc> [1..1] ± 4200
     Name <Nm> [0..1] Text 4200
     ShortName <ShrtNm> [0..1] Text 4200
     SupplementaryIdentification <SplmtryId> [0..1] Text 4200
     ClassType <ClssTp> [0..1] Text 4200
     SecuritiesForm <SctiesForm> [0..1] CodeSet 4201
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4201
     ProductGroup <PdctGrp> [0..1] Text 4201
     SeriesIdentification <SrsId> [0..1]  C19 4201
       SeriesDate <SrsDt> [0..1] ± 4202
       SeriesName <SrsNm> [0..1] Text 4202
56.4.3.3.8.1  LegIdentification <LegId>
Presence: [1..1]
Definition: Identification of a switch leg.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4186 May 2026
```

