---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.19 OfferType <OfferTp>"]
file_pages: [122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.19 OfferType <OfferTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 122 to 122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 122

```text
OccurrenceType <OcrncTp> contains one of the following elements (see
"DistributionTypeFormat7Choice" on page 924 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 925
Or}   Proprietary <Prtry> [1..1] ± 925
3.4.10.19  OfferType <OfferTp>
Presence: [0..*]
Definition: Specifies the conditions that apply to the offer.
OfferType <OfferTp> contains one of the following OfferTypeFormat18Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 122
Or}   Proprietary <Prtry> [1..1] ± 123
3.4.10.19.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify the conditions that apply to the offer.
Datatype: "OfferType7Code" on page 1223
CodeName Name Definition
DISS DissenterRights Securities holder has the right to
disagree with a mandatory event. This
right is not inherent in all offers and
therefore must be noted in
announcements only when applicable.
ERUN RestrictionExchange Exchange of Restricted to Unrestricted
(or vice versa).
FINL FinalOffer Final or last offer to holders subject to
offer conditions being reached, for
example, 50 percent accepted on a
tender.
PART PartialOffer Offer made by the offeror for a portion of
the outstanding shares not already
owned by the offeror.
SQUE SqueezeOutBid Offer launched by a company, in
possession of a large number of the
shares (90% - 95%) of a company
(generally as a result of a tender offer),
in order to acquire the remaining shares
of that company.
NDIS DissenterRightsNotApplicable Dissenter's rights are not applicable for
this option of the offer.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 122 February 2026
```

