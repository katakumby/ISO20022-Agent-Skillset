---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "58.4 Message Building Blocks", "58.4.2 RequestDetails <ReqDtls>", "58.4.2.1 Reference <Ref>"]
file_pages: [4239]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.018.001.05"]
---

# 58.4.2.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4239 to 4239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4239

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         Dutch <Dtch> [1..1] IdentifierSet 4249
Or         Valoren <Vlrn> [1..1] IdentifierSet 4249
Or         Sicovam <SCVM> [1..1] IdentifierSet 4249
Or         Belgian <Belgn> [1..1] IdentifierSet 4249
Or         Common <Cmon> [1..1] IdentifierSet 4249
Or         DTI <DTI> [1..1] IdentifierSet 4249
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  4249
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
Constraints
• ReferenceElementRule
One of the elements (Reference, RelatedReference, OrderReference) must be present.
58.4.2.1  Reference <Ref>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
Reference <Ref> contains one of the following References87Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PreviousReference <PrvsRef> [1..2] ± 4240
Or}   OtherReference <OthrRef> [1..2] ± 4240
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4239 May 2026
```

