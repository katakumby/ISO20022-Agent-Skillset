---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks", "57.4.3 StatusReport <StsRpt>", "57.4.3.2 IndividualCancellationStatusReport <IndvCxlStsRpt>", "57.4.3.2.1 MasterReference <MstrRef>"]
file_pages: [4218]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4.3.2.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4218 to 4218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4218

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       CTA <CTA> [1..1] IdentifierSet 4227
Or       QUICK <QUICK> [1..1] IdentifierSet 4227
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 4228
Or       Dutch <Dtch> [1..1] IdentifierSet 4228
Or       Valoren <Vlrn> [1..1] IdentifierSet 4228
Or       Sicovam <SCVM> [1..1] IdentifierSet 4228
Or       Belgian <Belgn> [1..1] IdentifierSet 4228
Or       Common <Cmon> [1..1] IdentifierSet 4228
Or       DTI <DTI> [1..1] IdentifierSet 4228
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  4228
         Identification <Id> [1..1] Text 4229
         IdentificationSource <IdSrc> [1..1] ± 4229
     Name <Nm> [0..1] Text 4229
     ShortName <ShrtNm> [0..1] Text 4229
     SupplementaryIdentification <SplmtryId> [0..1] Text 4229
     ClassType <ClssTp> [0..1] Text 4229
     SecuritiesForm <SctiesForm> [0..1] CodeSet 4230
     DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 4230
     ProductGroup <PdctGrp> [0..1] Text 4230
     SeriesIdentification <SrsId> [0..1]  C9 4230
       SeriesDate <SrsDt> [0..1] ± 4231
       SeriesName <SrsNm> [0..1] Text 4231
57.4.3.2.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
57.4.3.2.2  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4218 May 2026
```

