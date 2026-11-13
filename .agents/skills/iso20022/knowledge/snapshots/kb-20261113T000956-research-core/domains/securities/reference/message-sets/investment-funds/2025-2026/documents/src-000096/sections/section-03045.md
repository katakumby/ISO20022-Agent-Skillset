---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "59.4 Message Building Blocks", "59.4.7 OrderReferences <OrdrRefs>"]
file_pages: [4256]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.047.001.03"]
---

# 59.4.7 OrderReferences <OrdrRefs>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4256 to 4256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4256

```text
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
59.4.5 AmendmentIndicator <AmdmntInd>
Presence: [1..1]
Definition: Indicates whether a confirmation amendment message will follow the confirmation
cancellation instruction or not.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
59.4.6 MasterReference <MstrRef>
Presence: [0..1]
Definition: Reference assigned to a set of orders or trades in order to link them together.
Datatype: "Max35Text" on page 5403
59.4.7 OrderReferences <OrdrRefs>
Presence: [1..*]
Definition: Identification of the individual order confirmation to be cancelled.
OrderReferences <OrdrRefs> contains the following InvestmentFundOrder14 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderReference <OrdrRef> [1..1] Text 4256
   ClientReference <ClntRef> [0..1] Text 4257
   DealReference <DealRef> [0..1] Text 4257
   NonceIdentification <NonceId> [0..1] Text 4257
   CancellationReference <CxlRef> [0..1] Text 4257
   CancellationReason <CxlRsn> [0..1] ± 4257
59.4.7.1  OrderReference <OrdrRef>
Presence: [1..1]
Definition: Unique and unambiguous identifier for the order, as assigned by the instructing party.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.047.001.03
SubscriptionOrderConfirmationCancellationInstructi
onV03
Investment Funds - Maintenance 2025 - 2026 4256 May 2026
```

