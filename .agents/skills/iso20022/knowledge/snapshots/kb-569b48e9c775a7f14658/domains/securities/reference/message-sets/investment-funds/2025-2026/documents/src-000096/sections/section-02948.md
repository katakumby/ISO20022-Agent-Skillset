---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.2 IndividualOrderDetailsReport <IndvOrdrDtlsRpt>", "56.4.3.2.1 MasterReference <MstrRef>"]
file_pages: [4139]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.2.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4139 to 4139.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4139

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 4171
Or       CTA <CTA> [1..1] IdentifierSet 4171
Or       QUICK <QUICK> [1..1] IdentifierSet 4171
Or       Wertpapier <Wrtppr> [1..1] IdentifierSet 4171
Or       Dutch <Dtch> [1..1] IdentifierSet 4172
Or       Valoren <Vlrn> [1..1] IdentifierSet 4172
Or       Sicovam <SCVM> [1..1] IdentifierSet 4172
Or       Belgian <Belgn> [1..1] IdentifierSet 4172
Or       Common <Cmon> [1..1] IdentifierSet 4172
Or       DTI <DTI> [1..1] IdentifierSet 4172
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  4172
         Identification <Id> [1..1] Text 4173
         IdentificationSource <IdSrc> [1..1] ± 4173
     FinancialInstrumentName <FinInstrmNm> [0..1] Text 4173
     RedemptionCompletion <RedCmpltn> [0..1] CodeSet 4173
56.4.3.2.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
56.4.3.2.2  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
56.4.3.2.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
56.4.3.2.4  DealReference <DealRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order execution, as assigned by the confirming
party.
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4139 May 2026
```

