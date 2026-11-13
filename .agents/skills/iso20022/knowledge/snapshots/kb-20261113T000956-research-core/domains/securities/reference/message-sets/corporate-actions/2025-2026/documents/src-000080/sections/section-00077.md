---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.19 OfferType <OfferTp>", "3.4.10.19.2 Proprietary <Prtry>"]
file_pages: [123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.19.2 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 123 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 123

```text
CodeName Name Definition
ACPR AcceptancePriority Event will be paid in a particular priority
stated in the offering documentation.
Higher tiers of securities will be paid
ahead of lower tiers of securities.
3.4.10.19.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification of the conditions that apply to the offer.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
3.4.10.20  RenounceableEntitlementStatusType <RnncblEntitlmntStsTp>
Presence: [0..1]
Definition: Specifies whether terms of the event allow resale of the rights.
RenounceableEntitlementStatusType <RnncblEntitlmntStsTp> contains one of the following
elements (see "RenounceableEntitlementStatusTypeFormat3Choice" on page 943 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 943
Or}   Proprietary <Prtry> [1..1] ± 943
3.4.10.21  EventStage <EvtStag>
Presence: [0..*]
Definition: Stage in the corporate action event life cycle.
EventStage <EvtStag> contains one of the following elements (see
"CorporateActionEventStageFormat13Choice" on page 931 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 931
Or}   Proprietary <Prtry> [1..1] ± 932
3.4.10.22  AdditionalBusinessProcessIndicator <AddtlBizPrcInd>
Presence: [0..*]
Definition: Specifies the type of the additional business process linked to the corporate action event
such as a claim compensation or tax refund.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 123 February 2026
```

