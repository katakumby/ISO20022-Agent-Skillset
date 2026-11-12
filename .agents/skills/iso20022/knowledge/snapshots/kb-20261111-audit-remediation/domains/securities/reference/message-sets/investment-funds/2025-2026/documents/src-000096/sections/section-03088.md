---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "65.4 Message Building Blocks", "65.4.2 RequestDetails <ReqDtls>", "65.4.2.1 Reference <Ref>"]
file_pages: [4309]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.058.001.03"]
---

# 65.4.2.1 Reference <Ref>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4309 to 4309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4309

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or         Dutch <Dtch> [1..1] IdentifierSet 4319
Or         Valoren <Vlrn> [1..1] IdentifierSet 4319
Or         Sicovam <SCVM> [1..1] IdentifierSet 4319
Or         Belgian <Belgn> [1..1] IdentifierSet 4319
Or         Common <Cmon> [1..1] IdentifierSet 4319
Or         DTI <DTI> [1..1] IdentifierSet 4319
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  4319
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
Constraints
• ReferenceElementRule
One of the elements (Reference, RelatedReference, OrderReference) must be present.
65.4.2.1  Reference <Ref>
Presence: [0..1]
Definition: Reference to a linked message that was previously sent.
Reference <Ref> contains one of the following References87Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PreviousReference <PrvsRef> [1..2] ± 4310
Or}   OtherReference <OthrRef> [1..2] ± 4310
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4309 May 2026
```

