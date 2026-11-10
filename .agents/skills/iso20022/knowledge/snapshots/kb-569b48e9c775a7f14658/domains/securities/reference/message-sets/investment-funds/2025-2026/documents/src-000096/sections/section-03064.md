---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["62 setr.053.001.03 RedemptionBulkOrderConfirmationCancellationInstructionV03", "63.4 Message Building Blocks", "63.4.7.1 OrderReference <OrdrRef>"]
file_pages: [4280]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.055.001.03"]
---

# 63.4.7.1 OrderReference <OrdrRef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4280 to 4280.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4280

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
63.4.5 AmendmentIndicator <AmdmntInd>
Presence: [1..1]
Definition: Indicates whether a confirmation amendment message will follow the confirmation
cancellation instruction or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
63.4.6 MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
63.4.7 OrderReferences <OrdrRefs>
Presence: [1..*]
Definition: Identification of the individual order confirmation to be cancelled.
OrderReferences <OrdrRefs> contains the following InvestmentFundOrder14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [1..1] Text 4280
   ClientReference <ClntRef> [0..1] Text 4281
   DealReference <DealRef> [0..1] Text 4281
   NonceIdentification <NonceId> [0..1] Text 4281
   CancellationReference <CxlRef> [0..1] Text 4281
   CancellationReason <CxlRsn> [0..1] ± 4281
63.4.7.1  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.055.001.03
SwitchOrderConfirmationCancellationInstructionV03
Investment Funds - Maintenance 2025 - 2026 4280 May 2026
```

