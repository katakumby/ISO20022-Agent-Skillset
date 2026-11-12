---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "64.4 Message Building Blocks", "64.4.3 IndividualOrderConfirmationDetailsReport <IndvOrdrConfDtlsRpt>", "64.4.3.1 MasterReference <MstrRef>"]
file_pages: [4290]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.057.001.03"]
---

# 64.4.3.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4290 to 4290.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4290

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       Dutch <Dtch> [1..1] IdentifierSet 4299
Or       Valoren <Vlrn> [1..1] IdentifierSet 4299
Or       Sicovam <SCVM> [1..1] IdentifierSet 4299
Or       Belgian <Belgn> [1..1] IdentifierSet 4299
Or       Common <Cmon> [1..1] IdentifierSet 4299
Or       DTI <DTI> [1..1] IdentifierSet 4299
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  4299
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
64.4.3.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
64.4.3.2  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
64.4.3.3  Confirmation <Conf>
Presence: [1..1]
Definition: Status of the order confirmation cancellation.
Approved by the Securities SEG on 27 January 2026 setr.057.001.03 OrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4290 May 2026
```

