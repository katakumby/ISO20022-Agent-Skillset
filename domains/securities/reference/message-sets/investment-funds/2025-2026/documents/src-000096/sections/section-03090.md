---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "65.4 Message Building Blocks", "65.4.2 RequestDetails <ReqDtls>", "65.4.2.3 OrderReference <OrdrRef>", "65.4.2.3.1 MasterReference <MstrRef>"]
file_pages: [4312]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.058.001.03"]
---

# 65.4.2.3.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4312 to 4312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4312

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or       DTI <DTI> [1..1] IdentifierSet 4319
Or}       OtherProprietaryIdentification <OthrPrtryId> [1..1]  4319
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
65.4.2.3.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
65.4.2.3.2  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
65.4.2.3.3  ClientReference <ClntRef>
Presence: [0..1]
Definition: Unique and unambiguous investor's identification of the order. This reference can typically be
used in a hub scenario to give the reference of the order as assigned by the underlying client.
Datatype: "Max35Text" on page 5403
65.4.2.3.4  CancellationReference <CxlRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for the order cancellation, as assigned by the instructing
party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.058.001.03
RequestForOrderConfirmationStatusReportV03
Investment Funds - Maintenance 2025 - 2026 4312 May 2026
```

