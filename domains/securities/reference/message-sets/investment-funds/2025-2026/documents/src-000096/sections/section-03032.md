---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "58.4 Message Building Blocks", "58.4.2 RequestDetails <ReqDtls>", "58.4.2.3 OrderReference <OrdrRef>", "58.4.2.3.1 MasterReference <MstrRef>"]
file_pages: [4242]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.018.001.05"]
---

# 58.4.2.3.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4242 to 4242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4242

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       DTI <DTI> [1..1] IdentifierSet 4249
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  4249
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
58.4.2.3.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
58.4.2.3.2  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
58.4.2.3.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
58.4.2.3.4  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order cancellation, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.018.001.05 RequestForOrderStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4242 May 2026
```

